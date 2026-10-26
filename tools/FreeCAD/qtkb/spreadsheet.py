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


def _parse_target_expression(document, target_range):
    match = _TARGET_RANGE_EXPRESSION_PATTERN.fullmatch(target_range)
    if match is None:
        raise ValueError(
            "Target range must be a spreadsheet expression ending in an A1 range."
        )
    sheet_name = match.group("sheet_name")
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
    return sheet, _parse_range(match.group("cell_range"), "target range")


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