"""Spreadsheet commands for QTKB FreeCAD documents."""

import re

from .transaction import transactional


_CELL_PATTERN = re.compile(r"^([A-Za-z]+)(\d+)$")
_CELL_EXPRESSION_PATTERN = re.compile(
    r"^(?P<prefix>.+\.)(?P<cell>[A-Za-z]+\d+)$"
)
_TARGET_RANGE_EXPRESSION_PATTERN = re.compile(
    r"^<<(?P<sheet_name>[^>]+)>>\.(?P<cell_range>[A-Za-z]+\d+(?::[A-Za-z]+\d+)?)$"
)
_SOURCE_REFERENCE_EXPRESSION_PATTERN = re.compile(
    r"^<<(?P<object_name>[^>]+)>>\.(?P<reference>[A-Za-z_][A-Za-z0-9_]*)$"
)
_ALIAS_PREFIX_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_ALIAS_TRANSLITERATION = str.maketrans(
    {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
    }
)


def _column_to_number(column):
    number = 0
    for character in column.upper():
        number = number * 26 + ord(character) - ord("A") + 1
    return number


def _number_to_column(number):
    column = ""
    while number > 0:
        number, remainder = divmod(number - 1, 26)
        column = chr(65 + remainder) + column
    return column


def _parse_cell(cell):
    match = _CELL_PATTERN.fullmatch(cell)
    if match is None:
        raise ValueError(f"Invalid spreadsheet cell: {cell}")
    row = int(match.group(2))
    if row < 1:
        raise ValueError(f"Invalid spreadsheet cell: {cell}")
    return _column_to_number(match.group(1)), row


def _parse_range(cell_range, description):
    start_cell, separator, end_cell = cell_range.partition(":")
    if not separator:
        end_cell = start_cell
    start_column, start_row = _parse_cell(start_cell)
    end_column, end_row = _parse_cell(end_cell)
    if end_column < start_column or end_row < start_row:
        raise ValueError(f"Invalid {description.lower()}: {cell_range}")
    return start_column, start_row, end_column, end_row


def _parse_source_expression(source_cell):
    match = _CELL_EXPRESSION_PATTERN.fullmatch(source_cell)
    if match is None:
        raise ValueError("Source cell must be a FreeCAD expression ending in an A1 cell.")
    return match.group("prefix"), _parse_cell(match.group("cell"))


def _get_spreadsheet(document, sheet_name):
    sheet = document.getObject(sheet_name)
    if sheet is None:
        matching_sheets = [
            candidate
            for candidate in document.Objects
            if candidate.TypeId == "Spreadsheet::Sheet" and candidate.Label == sheet_name
        ]
        if len(matching_sheets) > 1:
            raise RuntimeError(
                f"Target spreadsheet label is ambiguous: {sheet_name}"
            )
        if matching_sheets:
            sheet = matching_sheets[0]
    if sheet is None or sheet.TypeId != "Spreadsheet::Sheet":
        raise RuntimeError(f"Target spreadsheet not found: {sheet_name}")
    return sheet


def _parse_target_expression(document, target_range):
    match = _TARGET_RANGE_EXPRESSION_PATTERN.fullmatch(target_range)
    if match is None:
        raise ValueError(
            "Target range must be a spreadsheet expression ending in an A1 range."
        )
    sheet = _get_spreadsheet(document, match.group("sheet_name"))
    return sheet, _parse_range(match.group("cell_range"), "target range")


def _parse_source_reference_expression(source_start):
    match = _SOURCE_REFERENCE_EXPRESSION_PATTERN.fullmatch(source_start)
    if match is None:
        raise ValueError(
            "Source start must be a FreeCAD expression ending in a cell or "
            'alias, for example "<<lMasterGlobals>>.B17".'
        )
    return match.group("object_name"), match.group("reference")


def _get_source_spreadsheet(document, source_name):
    source = document.getObject(source_name)
    if source is None:
        matching_objects = [
            candidate
            for candidate in document.Objects
            if candidate.Label == source_name
        ]
        if len(matching_objects) > 1:
            raise RuntimeError(f"Source object label is ambiguous: {source_name}")
        if matching_objects:
            source = matching_objects[0]
    if source is None:
        raise RuntimeError(f"Source object not found: {source_name}")
    while source.TypeId == "App::Link":
        source = source.LinkedObject
        if source is None:
            raise RuntimeError(f"Source link has no linked object: {source_name}")
    if source.TypeId != "Spreadsheet::Sheet":
        raise RuntimeError(
            f"Source object is not a spreadsheet or spreadsheet link: {source_name}"
        )
    return source


def _normalise_alias_component(value, cell):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Header cell {cell} must contain text.")

    characters = []
    for character in value.strip().translate(_ALIAS_TRANSLITERATION):
        if character.isascii() and character.isalnum():
            characters.append(character)
        elif character.isspace():
            continue
        elif not characters or characters[-1] != "X":
            characters.append("X")

    normalised = "".join(characters)
    if not normalised:
        raise ValueError(f"Header cell has no usable alias characters: {cell}")
    if normalised[0].isdigit():
        normalised = f"N{normalised}"
    return normalised


@transactional("Link spreadsheet cells")
def link_cells(
    target_range,
    source_cell,
    transpose=False,
    *,
    document=None,
):
    """Link an explicit target spreadsheet range from a source start cell.

    ``target_range`` identifies a local Spreadsheet::Sheet and its A1 range,
    for example ``<<tKeysLayout>>.A1:D10``. ``source_cell`` is a FreeCAD
    expression ending in the first source cell, for example
    ``<<lMasterGlobals>>.A1``. Set ``transpose`` to True to swap the source
    row and column offsets along the target-range diagonal.
    """
    if not isinstance(transpose, bool):
        raise TypeError("transpose must be True or False.")

    target_sheet, (
        target_start_column,
        target_start_row,
        target_end_column,
        target_end_row,
    ) = _parse_target_expression(document, target_range)
    source_prefix, (source_start_column, source_start_row) = _parse_source_expression(
        source_cell
    )

    target_column_count = target_end_column - target_start_column + 1
    target_row_count = target_end_row - target_start_row + 1

    for row_offset in range(target_row_count):
        for column_offset in range(target_column_count):
            target_cell = (
                f"{_number_to_column(target_start_column + column_offset)}"
                f"{target_start_row + row_offset}"
            )
            source_column_offset, source_row_offset = (
                (row_offset, column_offset)
                if transpose
                else (column_offset, row_offset)
            )
            source_cell = (
                f"{_number_to_column(source_start_column + source_column_offset)}"
                f"{source_start_row + source_row_offset}"
            )
            target_sheet.set(
                target_cell,
                f"={source_prefix}{source_cell}",
            )

    mode = "transposed" if transpose else "direct"
    print(f"Linked {target_range} from {source_cell} ({mode}).")


@transactional("Link spreadsheet aliases")
def link_aliases(
    target_range,
    source_start,
    transpose=False,
    *,
    document=None,
):
    """Link a target range to source cells through their spreadsheet aliases.

    ``source_start`` identifies the top-left source cell by either its A1
    address or its alias. Each generated formula references the corresponding
    source-cell alias rather than a source-cell address. Set ``transpose`` to
    True to swap source row and column offsets along the target-range diagonal.
    """
    target_sheet, (
        target_start_column,
        target_start_row,
        target_end_column,
        target_end_row,
    ) = _parse_target_expression(document, target_range)
    if not isinstance(transpose, bool):
        raise TypeError("transpose must be True or False.")
    source_name, source_reference = _parse_source_reference_expression(source_start)
    source_sheet = _get_source_spreadsheet(document, source_name)
    if _CELL_PATTERN.fullmatch(source_reference):
        source_start_column, source_start_row = _parse_cell(source_reference)
    else:
        source_cell = source_sheet.getCellFromAlias(source_reference)
        if not source_cell:
            raise ValueError(f"Source alias not found: {source_reference}")
        source_start_column, source_start_row = _parse_cell(source_cell)

    assignments = []
    for row_offset, row in enumerate(range(target_start_row, target_end_row + 1)):
        for column_offset, column in enumerate(
            range(target_start_column, target_end_column + 1)
        ):
            target_cell = f"{_number_to_column(column)}{row}"
            source_column_offset, source_row_offset = (
                (row_offset, column_offset)
                if transpose
                else (column_offset, row_offset)
            )
            source_cell = (
                f"{_number_to_column(source_start_column + source_column_offset)}"
                f"{source_start_row + source_row_offset}"
            )
            source_alias = source_sheet.getAlias(source_cell)
            if not source_alias:
                raise ValueError(f"Source cell has no alias: {source_cell}")
            assignments.append((target_cell, source_alias))

    for target_cell, source_alias in assignments:
        target_sheet.set(target_cell, f"=<<{source_name}>>.{source_alias}")

    mode = "transposed" if transpose else "direct"
    print(f"Linked {len(assignments)} source alias(es) from {source_start} ({mode}).")


@transactional("Link spreadsheet header aliases")
def link_header_aliases(
    target_range,
    context="",
    swap_headers=False,
    *,
    document=None,
):
    """Link cells through aliases constructed from target column and row headers.

    ``target_range`` identifies the local data matrix. Its headers are the row
    immediately above and the column immediately left of that matrix.
    ``context`` is an optional literal formula prefix, such as
    ``<<tMaster>>.Stamp_``. The command constructs an alias for each target
    cell using the same normalized header convention as
    :func:`create_header_aliases`, then writes a formula with the context
    immediately before that alias.
    """
    target_sheet, (
        start_column,
        start_row,
        end_column,
        end_row,
    ) = _parse_target_expression(document, target_range)
    if start_column == 1 or start_row == 1:
        raise ValueError(
            "Header alias matrix needs one row above and one column to its left."
        )
    if context is None:
        context = ""
    if not isinstance(context, str):
        raise TypeError("context must be text, an empty string, or None.")
    if not isinstance(swap_headers, bool):
        raise TypeError("swap_headers must be True or False.")

    column_names = {}
    for column in range(start_column, end_column + 1):
        header_cell = f"{_number_to_column(column)}{start_row - 1}"
        column_names[column] = _normalise_alias_component(
            target_sheet.get(header_cell), header_cell
        )

    row_names = {}
    for row in range(start_row, end_row + 1):
        header_cell = f"{_number_to_column(start_column - 1)}{row}"
        row_names[row] = _normalise_alias_component(
            target_sheet.get(header_cell), header_cell
        )

    assignments = []
    for row in range(start_row, end_row + 1):
        for column in range(start_column, end_column + 1):
            target_cell = f"{_number_to_column(column)}{row}"
            primary_header, secondary_header = (
                (row_names[row], column_names[column])
                if swap_headers
                else (column_names[column], row_names[row])
            )
            alias = f"{primary_header}_{secondary_header}"
            assignments.append((target_cell, alias))

    for target_cell, alias in assignments:
        target_sheet.set(target_cell, f"={context}{alias}")

    print(f"Linked {len(assignments)} header-derived alias expression(s).")


@transactional("Create spreadsheet matrix aliases")
def create_matrix_aliases(
    target_range,
    matrix_id,
    *,
    document=None,
):
    """Assign relative aliases to every cell in an inclusive spreadsheet range.

    For ``matrix_id="Stamp"`` and ``target_range="<<tStampLayout>>.C5:E6"``,
    the aliases are ``Stamp_A01`` through ``Stamp_C02``.
    """
    if not isinstance(matrix_id, str):
        raise TypeError("matrix_id must be text, for example 'Stamp'.")
    if not matrix_id:
        raise ValueError("matrix_id must not be empty; use a prefix such as 'Stamp'.")
    if not _ALIAS_PREFIX_PATTERN.fullmatch(matrix_id):
        raise ValueError(
            f"Invalid matrix_id {matrix_id!r}: it must begin with a letter or "
            "underscore and contain only letters, numbers, and underscores."
        )

    sheet, (
        start_column,
        start_row,
        end_column,
        end_row,
    ) = _parse_target_expression(document, target_range)
    alias_count = 0
    for row_offset, row in enumerate(range(start_row, end_row + 1), start=1):
        for column_offset, column in enumerate(
            range(start_column, end_column + 1), start=1
        ):
            cell = f"{_number_to_column(column)}{row}"
            alias = f"{matrix_id}_{_number_to_column(column_offset)}{row_offset:02d}"
            sheet.setAlias(cell, alias)
            alias_count += 1

    print(
        f"Created {alias_count} matrix alias(es) in {sheet.Name}: "
        f"{matrix_id}_A01..."
    )


@transactional("Create spreadsheet header aliases")
def create_header_aliases(
    target_range,
    context=None,
    swap_headers=False,
    *,
    document=None,
):
    """Assign aliases from a matrix's top-column and left-row headers.

    ``target_range`` identifies the local data matrix. Column headers are read
    from the row immediately above it, and row headers from the column
    immediately to its left. The data cells receive aliases in the form
    ``<Context>_<ColumnName>_<RowName>`` after deterministic normalization.
    ``swap_headers=True`` reverses the header priority to
    ``<Context>_<RowName>_<ColumnName>``. ``context`` is optional.
    """
    sheet, (
        start_column,
        start_row,
        end_column,
        end_row,
    ) = _parse_target_expression(document, target_range)
    if start_column == 1 or start_row == 1:
        raise ValueError(
            "Header alias matrix needs one row above and one column to its left."
        )
    if not isinstance(swap_headers, bool):
        raise TypeError("swap_headers must be True or False.")

    if context is not None and not isinstance(context, str):
        raise TypeError("context must be text, an empty string, or None.")
    context_name = (
        _normalise_alias_component(context, "context")
        if context and context.strip()
        else None
    )
    column_names = {}
    for column in range(start_column, end_column + 1):
        header_cell = f"{_number_to_column(column)}{start_row - 1}"
        column_names[column] = _normalise_alias_component(
            sheet.get(header_cell), header_cell
        )

    row_names = {}
    for row in range(start_row, end_row + 1):
        header_cell = f"{_number_to_column(start_column - 1)}{row}"
        row_names[row] = _normalise_alias_component(sheet.get(header_cell), header_cell)

    aliases = {}
    for row in range(start_row, end_row + 1):
        for column in range(start_column, end_column + 1):
            cell = f"{_number_to_column(column)}{row}"
            alias_parts = (
                [column_names[column], row_names[row]]
                if not swap_headers
                else [row_names[row], column_names[column]]
            )
            if context_name is not None:
                alias_parts.insert(0, context_name)
            alias = "_".join(alias_parts)
            if alias in aliases:
                raise ValueError(
                    f"Header normalization creates duplicate alias {alias}: "
                    f"{aliases[alias]} and {cell}"
                )
            aliases[alias] = cell

    for alias, cell in aliases.items():
        sheet.setAlias(cell, alias)

    print(f"Created {len(aliases)} header alias(es) in {sheet.Name}.")