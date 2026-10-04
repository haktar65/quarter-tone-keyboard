"""Sketch commands for interactive QTKB FreeCAD work."""

import re
from numbers import Real

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Sketcher

from .transaction import transactional


_CELL_PATTERN = re.compile(r"^([A-Za-z]+)(\d+)$")
_RANGE_EXPRESSION_PATTERN = re.compile(
    r"^(?P<prefix>.+\.)(?P<cell_range>[A-Za-z]+\d+:[A-Za-z]+\d+)$"
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


def _range_cells(cell_range):
    start_cell, separator, end_cell = cell_range.partition(":")
    end_cell = end_cell or start_cell
    start_column, start_row = _parse_cell(start_cell)
    end_column, end_row = _parse_cell(end_cell)

    if start_column != end_column and start_row != end_row:
        raise ValueError(
            "Spreadsheet point data must be a single row or a single column."
        )
    if end_column < start_column or end_row < start_row:
        raise ValueError(f"Invalid spreadsheet range: {cell_range}")

    if start_column == end_column:
        return [
            f"{_number_to_column(start_column)}{row}"
            for row in range(start_row, end_row + 1)
        ]
    return [
        f"{_number_to_column(column)}{start_row}"
        for column in range(start_column, end_column + 1)
    ]


def _coordinate_values(value, coordinate):
    if isinstance(value, str):
        range_expression = _RANGE_EXPRESSION_PATTERN.fullmatch(value)
        if range_expression is None:
            return [value]
        prefix = range_expression.group("prefix")
        return [
            f"{prefix}{cell}"
            for cell in _range_cells(range_expression.group("cell_range"))
        ]
    if isinstance(value, Real) and not isinstance(value, bool):
        return [value]
    raise TypeError(
        f"{coordinate} must be a number or a one-dimensional spreadsheet range."
    )


def _broadcast_coordinates(x_values, y_values):
    point_count = max(len(x_values), len(y_values))
    if len(x_values) not in (1, point_count):
        raise ValueError("X and Y spreadsheet ranges must have equal lengths.")
    if len(y_values) not in (1, point_count):
        raise ValueError("X and Y spreadsheet ranges must have equal lengths.")
    return (
        x_values * point_count if len(x_values) == 1 else x_values,
        y_values * point_count if len(y_values) == 1 else y_values,
    )


def _get_sketch(document, sketch_name):
    if sketch_name:
        sketch = document.getObject(sketch_name)
    else:
        selection = Gui.Selection.getSelection()
        sketch = next(
            (object_ for object_ in selection
             if object_.TypeId == "Sketcher::SketchObject"),
            None,
        )
    if sketch is None or sketch.TypeId != "Sketcher::SketchObject":
        if sketch_name:
            raise RuntimeError(f"Sketch not found: {sketch_name}")
        raise RuntimeError("No sketch selected.")
    return sketch


@transactional("Add distributed sketch points")
def add_points(x, y, sketch_name=None, *, document=None):
    """Add construction points from scalar or linked spreadsheet coordinates.

    ``x`` and ``y`` each accept one numeric scalar, a FreeCAD expression, or
    a FreeCAD expression ending in one horizontal/vertical spreadsheet range.
    A scalar broadcasts across the other coordinate's range. Expressions remain
    parametric when assigned to the generated sketch constraints. With no
    ``sketch_name``, the selected sketch is the target.
    """
    x_values = _coordinate_values(x, "X")
    y_values = _coordinate_values(y, "Y")
    x_values, y_values = _broadcast_coordinates(x_values, y_values)
    sketch = _get_sketch(document, sketch_name)

    point_indices = []
    for x_value, y_value in zip(x_values, y_values):
        point_index = sketch.addGeometry(Part.Point(App.Vector(0, 0, 0)), True)
        x_constraint = sketch.addConstraint(
            Sketcher.Constraint("DistanceX", point_index, 1, x_value if not isinstance(x_value, str) else 0)
        )
        y_constraint = sketch.addConstraint(
            Sketcher.Constraint("DistanceY", point_index, 1, y_value if not isinstance(y_value, str) else 0)
        )

        if isinstance(x_value, str):
            sketch.setExpression(f"Constraints[{x_constraint}]", x_value)
        if isinstance(y_value, str):
            sketch.setExpression(f"Constraints[{y_constraint}]", y_value)
        point_indices.append(point_index)

    print(f"Added {len(point_indices)} construction point(s) to {sketch.Name}.")
    return point_indices