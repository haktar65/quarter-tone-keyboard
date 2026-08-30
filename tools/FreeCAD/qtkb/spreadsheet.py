"""Spreadsheet commands for QTKB FreeCAD documents."""

import re

import FreeCADGui as Gui

from .transaction import transactional


_CELL_PATTERN = re.compile(r"^([A-Za-z]+)(\d+)$")


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
    return _column_to_number(match.group(1)), int(match.group(2))


def _get_target_sheet(document, target_sheet_name):
    if target_sheet_name:
        sheet = document.getObject(target_sheet_name)
    else:
        selection = Gui.Selection.getSelection()
        sheet = next(
            (object_ for object_ in selection
             if object_.TypeId == "Spreadsheet::Sheet"),
            None,
        )

    if sheet is None or sheet.TypeId != "Spreadsheet::Sheet":
        raise RuntimeError("No target spreadsheet found.")
    return sheet


@transactional("Link spreadsheet cells")
def link_cells(
    target_range,
    source_link_name,
    source_start_cell="A1",
    target_sheet_name=None,
    *,
    document=None,
):
    """Link a target spreadsheet range to cells from an App::Link target.

    ``source_link_name`` is the internal object name of an App::Link whose
    LinkedObject is the source Spreadsheet.
    """
    target_sheet = _get_target_sheet(document, target_sheet_name)

    start_cell, _, end_cell = target_range.partition(":")
    end_cell = end_cell or start_cell
    target_start_column, target_start_row = _parse_cell(start_cell)
    target_end_column, target_end_row = _parse_cell(end_cell)
    source_start_column, source_start_row = _parse_cell(source_start_cell)

    if target_end_column < target_start_column or target_end_row < target_start_row:
        raise ValueError(f"Invalid target range: {target_range}")

    for row_offset in range(target_end_row - target_start_row + 1):
        for column_offset in range(target_end_column - target_start_column + 1):
            target_cell = (
                f"{_number_to_column(target_start_column + column_offset)}"
                f"{target_start_row + row_offset}"
            )
            source_cell = (
                f"{_number_to_column(source_start_column + column_offset)}"
                f"{source_start_row + row_offset}"
            )
            target_sheet.set(
                target_cell,
                f"=<<{source_link_name}>>.LinkedObject.{source_cell}",
            )

    print(f"Linked {target_range} from {source_link_name}.")