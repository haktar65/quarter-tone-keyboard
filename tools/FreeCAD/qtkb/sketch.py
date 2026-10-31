"""Sketch commands for interactive QTKB FreeCAD work."""

import re
from numbers import Real

import FreeCAD as App
import FreeCADGui as Gui
import Part
import Sketcher

from . import spreadsheet
from .transaction import transactional


_CELL_PATTERN = re.compile(r"^([A-Za-z]+)(\d+)$")
_RANGE_EXPRESSION_PATTERN = re.compile(
    r"^(?P<prefix>.+\.)(?P<cell_range>[A-Za-z]+\d+:[A-Za-z]+\d+)$"
)
_CELL_REFERENCE_PATTERN = re.compile(
    r"<<(?P<object_name>[^>]+)>>\.(?P<cell>[A-Za-z]+\d+)"
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


def _broadcast_circle_values(x_values, y_values, radius_values):
    circle_count = max(len(x_values), len(y_values), len(radius_values))
    if len(x_values) not in (1, circle_count):
        raise ValueError("X, Y, and radius spreadsheet ranges must have equal lengths.")
    if len(y_values) not in (1, circle_count):
        raise ValueError("X, Y, and radius spreadsheet ranges must have equal lengths.")
    if len(radius_values) not in (1, circle_count):
        raise ValueError("X, Y, and radius spreadsheet ranges must have equal lengths.")
    return (
        x_values * circle_count if len(x_values) == 1 else x_values,
        y_values * circle_count if len(y_values) == 1 else y_values,
        radius_values * circle_count if len(radius_values) == 1 else radius_values,
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


def _resolve_cell_reference(
    document,
    object_name,
    cell,
    resolution_stack,
    unresolved=None,
):
    """Return an alias expression or recursively resolved formula for one cell."""
    reference = (object_name, cell.upper())
    if reference in resolution_stack:
        chain = " -> ".join(
            f"<<{name}>>.{cell_name}"
            for name, cell_name in (*resolution_stack, reference)
        )
        raise RuntimeError(f"Circular spreadsheet cell reference: {chain}")

    sheet = spreadsheet._get_source_spreadsheet(document, object_name)
    alias = sheet.getAlias(cell)
    if alias:
        return f"<<{object_name}>>.{alias}"

    cell_contents = sheet.get(cell)
    if not isinstance(cell_contents, str) or not cell_contents.startswith("="):
        raise ValueError(
            f"Spreadsheet cell <<{object_name}>>.{cell} has no alias or formula "
            "to resolve."
        )

    return _resolve_expression_cell_references(
        document,
        cell_contents[1:],
        (*resolution_stack, reference),
        unresolved,
    )


def _resolve_expression_cell_references(
    document,
    expression,
    resolution_stack=(),
    unresolved=None,
):
    def replace_reference(match):
        try:
            return _resolve_cell_reference(
                document,
                match.group("object_name"),
                match.group("cell"),
                resolution_stack,
                unresolved,
            )
        except (RuntimeError, ValueError) as error:
            if unresolved is None:
                raise
            unresolved.append((match.group(0), str(error)))
            return match.group(0)

    return _CELL_REFERENCE_PATTERN.sub(replace_reference, expression)


def _resolve_sketch_expressions(document, sketch):
    assignments = []
    unresolved = []
    for property_path, expression in sketch.ExpressionEngine:
        if not isinstance(expression, str) or not _CELL_REFERENCE_PATTERN.search(
            expression
        ):
            continue
        expression_unresolved = []
        resolved_expression = _resolve_expression_cell_references(
            document,
            expression,
            unresolved=expression_unresolved,
        )
        if resolved_expression != expression:
            assignments.append((sketch, property_path, resolved_expression))
        unresolved.extend(
            (sketch.Name, property_path, reference, reason)
            for reference, reason in expression_unresolved
        )
    return assignments, unresolved


def _print_unresolved_references(unresolved):
    if not unresolved:
        return
    print(f"Could not resolve {len(unresolved)} spreadsheet cell reference(s):")
    for sketch_name, property_path, reference, reason in unresolved:
        print(f"  {sketch_name} {property_path}: {reference} ({reason})")


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


@transactional("Add distributed sketch circles")
def add_circles(x, y, radius, sketch_name=None, *, document=None):
    """Add circles from scalar or linked spreadsheet center and radius values.

    ``x``, ``y``, and ``radius`` each accept one numeric scalar, a FreeCAD
    expression, or a FreeCAD expression ending in one horizontal/vertical
    spreadsheet range. A scalar broadcasts across the other ranges.
    Expressions remain parametric when assigned to the generated sketch
    constraints. With no ``sketch_name``, the selected sketch is the target.
    """
    x_values = _coordinate_values(x, "X")
    y_values = _coordinate_values(y, "Y")
    radius_values = _coordinate_values(radius, "Radius")
    x_values, y_values, radius_values = _broadcast_circle_values(
        x_values, y_values, radius_values
    )
    sketch = _get_sketch(document, sketch_name)

    circle_indices = []
    for x_value, y_value, radius_value in zip(x_values, y_values, radius_values):
        circle_index = sketch.addGeometry(
            Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 1),
            False,
        )
        x_constraint = sketch.addConstraint(
            Sketcher.Constraint(
                "DistanceX", circle_index, 3, x_value if not isinstance(x_value, str) else 0
            )
        )
        y_constraint = sketch.addConstraint(
            Sketcher.Constraint(
                "DistanceY", circle_index, 3, y_value if not isinstance(y_value, str) else 0
            )
        )
        radius_constraint = sketch.addConstraint(
            Sketcher.Constraint(
                "Radius", circle_index, radius_value if not isinstance(radius_value, str) else 1
            )
        )

        if isinstance(x_value, str):
            sketch.setExpression(f"Constraints[{x_constraint}]", x_value)
        if isinstance(y_value, str):
            sketch.setExpression(f"Constraints[{y_constraint}]", y_value)
        if isinstance(radius_value, str):
            sketch.setExpression(f"Constraints[{radius_constraint}]", radius_value)
        circle_indices.append(circle_index)

    print(f"Added {len(circle_indices)} circle(s) to {sketch.Name}.")
    return circle_indices


@transactional("Resolve sketch spreadsheet references")
def resolve_cell_references(sketch_name=None, *, document=None):
    """Replace spreadsheet cell references in a sketch with alias expressions.

    The selected sketch is used when ``sketch_name`` is omitted. Each
    ``<<Table>>.A1`` reference in its expression engine is replaced with the
    cell's alias. When that cell has no alias but contains a formula, cell
    references inside that formula are resolved recursively. This supports
    local tables which themselves link to aliases in another spreadsheet.
    """
    sketch = _get_sketch(document, sketch_name)
    assignments, unresolved = _resolve_sketch_expressions(document, sketch)

    for _, property_path, resolved_expression in assignments:
        sketch.setExpression(property_path, resolved_expression)

    print(
        f"Resolved {len(assignments)} spreadsheet cell reference expression(s) "
        f"in {sketch.Name}."
    )
    _print_unresolved_references(unresolved)
    return len(assignments)


@transactional("Resolve document spreadsheet references")
def resolve_all_cell_references(*, document=None):
    """Resolve spreadsheet cell references in every sketch in the document.

    References that cannot be converted are left unchanged and printed with
    their sketch name, expression path, and cause. All successfully resolved
    expressions across the document are committed as one undoable operation.
    """
    sketches = [
        object_
        for object_ in document.Objects
        if object_.TypeId == "Sketcher::SketchObject"
    ]
    assignments = []
    unresolved = []
    for sketch in sketches:
        sketch_assignments, sketch_unresolved = _resolve_sketch_expressions(
            document,
            sketch,
        )
        assignments.extend(sketch_assignments)
        unresolved.extend(sketch_unresolved)

    for sketch, property_path, resolved_expression in assignments:
        sketch.setExpression(property_path, resolved_expression)

    print(
        f"Resolved {len(assignments)} spreadsheet cell reference expression(s) "
        f"in {len(sketches)} sketch(es)."
    )
    _print_unresolved_references(unresolved)
    return len(assignments)