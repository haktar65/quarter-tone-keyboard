# QTKB FreeCAD Tools

`tools/FreeCAD/` is the repository-local home for interactive QTKB FreeCAD
tools. Edit the Python library in VS Code; call it from FreeCAD through the
reload macro.

## Directory Layout

```text
tools/FreeCAD/
├── README.md                         This document
├── QTKB_Reload.FCMacro               Loader and module reloader
├── QTKB_Status.FCMacro               Non-loading library status check
└── qtkb/                             Reusable Python library
```

New reusable commands belong in `qtkb/`.

## User Workflow

The normal user workflow has four steps:

1. Open the target FreeCAD document.
2. Run `QTKB_Reload.FCMacro` after opening the document and after editing a
  QTKB helper in VS Code.
3. Enter `import qtkb` in the FreeCAD Python console.
4. Run a documented command in the Python console, or run a project macro
  which supplies the same command parameters.

All QTKB commands are written to be repeatable. Commands that change a
document create one FreeCAD undo step; use `Edit -> Undo` to revert one command
run.

## Setup

1. In FreeCAD, add the checked-out repository's `tools/FreeCAD` directory to
  the Macro path. This is the only per-checkout setup step.
2. Assign `QTKB_Reload.FCMacro` to a keyboard shortcut.
3. Press that shortcut after opening a QTKB document and whenever modules have
  changed in VS Code.

The macro discovers its own directory, adds that directory to `sys.path`,
reloads the `qtkb` package itself, and then reloads its editable modules. It
therefore discovers new modules such as `qtkb.sketch` without restarting
FreeCAD. It contains no machine-specific path, so the same checkout can be
used from another location. Keep the macro inside this directory; it is
intentionally the only code that needs to be registered in FreeCAD's Macro
path.

## Library Status Check

Run `QTKB_Status.FCMacro` to check whether this FreeCAD session has already
loaded QTKB. It does not import or reload the library itself.

Expected Python-console output after the reload macro has run:

```text
QTKB is loaded from: C:\Work\quarter-tone-keyboard\tools\FreeCAD\qtkb\__init__.py
```

Before loading, it instead directs you to run `QTKB_Reload.FCMacro`. The status
macro can also have its own toolbar button or keyboard shortcut.

## Calling Commands

Run `QTKB_Reload.FCMacro` first. In the Python console, then enter
`import qtkb`. Use module-qualified, parameterized calls either in that console
or in another small project macro:

```python
qtkb.spreadsheet.link_cells(
  "<<tKeysLayout>>.A1:D10",
  "<<lMasterGlobals>>.A1",
)
```

The arguments are deliberately explicit: full target expression with target
range, full source expression with its start cell, and optional transpose mode.
Every call is one undoable FreeCAD transaction.

For a repeatable task, create a thin macro beside `QTKB_Reload.FCMacro` that
only supplies project-specific parameters. Do not duplicate the library logic:

```python
import qtkb

qtkb.spreadsheet.link_cells(
  "<<tKeysLayout>>.A1:D10",
  "<<lMasterGlobals>>.A1",
)
```

After changing a module in VS Code, run `QTKB_Reload.FCMacro` again. Do not use
`from qtkb.spreadsheet import link_cells` for interactive work, because that
name does not follow later module reloads.

## Spreadsheet Range Binding

`qtkb.spreadsheet.link_cells(...)` fills a target spreadsheet range with
expressions pointing to an `App::Link` object's linked source spreadsheet. It
is intended for exposing master parameters locally without copying numerical
values.

### Prerequisites

- Run `QTKB_Reload.FCMacro` in the current FreeCAD session.
- A complete FreeCAD expression for the source spreadsheet or linked source
  spreadsheet is known, including its source start cell.
- The target spreadsheet's internal `Name` or unique visible `Label`, plus its
  target A1 range, are known.

Use internal names inside source expressions. For example,
`<<lMasterGlobals>>.A1` names the linked source and its upper-left source
cell. `<<tKeysLayout>>.A1:D10` identifies the target sheet and its complete
target range. The target may alternatively use its unique visible label.

### Command

```python
qtkb.spreadsheet.link_cells(
  target_range,
  source_cell,
  transpose=False,
)
```

| Argument | Meaning | Example |
|---|---|---|
| `target_range` | Direct target spreadsheet expression ending in an A1 range. | `"<<tKeysLayout>>.B3:E8"` or `"<<tKeysLayout>>.A1"` |
| `source_cell` | FreeCAD expression ending in the upper-left source cell. The target range determines the source extent. | `"<<lMasterGlobals>>.C5"` |
| `transpose` | Optional mode, default `False`. `True` mirrors the source mapping at the range diagonal. | `False` or `True` |

### Examples

Link a `4 x 10` region in a named target spreadsheet from a linked source
starting at `A1`:

```python
qtkb.spreadsheet.link_cells(
  "<<tKeysLayout>>.A1:D10",
  "<<lMasterGlobals>>.A1",
)
```

Link one target cell to a different source cell:

```python
qtkb.spreadsheet.link_cells(
  "<<tKeysLayout>>.B7",
  "<<lMasterGlobals>>.F12",
)
```

Link a range in a second named target spreadsheet:

```python
qtkb.spreadsheet.link_cells(
  "<<tKeysPrototype>>.C3:F6",
  "<<lMasterGlobals>>.H2",
)
```

The first example writes expressions such as:

```text
=<<lMasterGlobals>>.A1
```

The target cell at `D10` then refers to source cell `D10`.
`transpose` defaults to `False`, so normal bindings do not need to state it.
Existing expressions or values in the selected target range are replaced. The
full write operation is a single undoable action and triggers one final document
recompute.

## Sketch Point Distribution

`qtkb.sketch.add_points(...)` adds construction points to an existing sketch.
Each coordinate may be one number, one FreeCAD expression, or one horizontal
or vertical spreadsheet range embedded in a FreeCAD expression. Expressions
remain parametric: the helper assigns them to generated sketch constraints
rather than copying spreadsheet values.

```python
qtkb.sketch.add_points(
  x,
  y,
  sketch_name=None,
)
```

| Argument | Meaning | Example |
|---|---|---|
| `x` | Number, FreeCAD expression, or expression ending in a one-dimensional A1 range. | `0.0`, `"<<tZeroStop>>.SplintPositionY"`, or `"<<lKeysLayout>>.A11:X11"` |
| `y` | Number, FreeCAD expression, or expression ending in a one-dimensional A1 range. | `12.0` or `"<<lKeysLayout>>.B3:B26"` |
| `sketch_name` | Optional internal target-sketch `Name`. When omitted, use the sketch selected in the FreeCAD tree. A user-visible `Label` is not a valid name argument. | `"Sketch001"` |

A scalar or expression without a final A1 range broadcasts across the other
coordinate range. The helper expands only an expression whose final component
is a valid A1 range containing `:`. Two spreadsheet ranges must have the same
length; rectangular ranges are rejected. Select the target sketch itself in
FreeCAD tree before a normal interactive call; merely opening it in the editor
does not select it. Select exactly one target sketch. Examples:

```python
# X values from the linked sheet, constant Y from a local spreadsheet alias.
qtkb.sketch.add_points(
  "<<lKeysLayout>>.A11:X11",
  "<<tZeroStop>>.SplintPositionY",
)

# Constant X; Y values from the linked sheet.
qtkb.sketch.add_points(
  0.0,
  "<<lKeysLayout>>.B3:B26",
)

# Pairwise X and Y coordinates from the same linked sheet.
qtkb.sketch.add_points(
  "<<lKeysLayout>>.A11:X11",
  "<<lKeysLayout>>.A12:X12",
)
```

For a project macro that must not rely on the tree selection, provide the
internal sketch name as the third positional argument:

```python
qtkb.sketch.add_points(
  "<<lKeysLayout>>.A11:X11",
  "<<tZeroStop>>.SplintPositionY",
  "Sketch001",
)
```

The helper adds new points on every call. Use `Edit -> Undo` to remove a run,
or use a dedicated empty sketch when regenerating a point set.

### Sketch Circle Distribution

`qtkb.sketch.add_circles(...)` adds normal sketch circles. Their center X, center
Y, and radius accept the same scalar, FreeCAD-expression, and one-dimensional
spreadsheet-range inputs as `add_points(...)`. A scalar or single expression
broadcasts across the other ranges; all non-scalar ranges must have equal
lengths.

```python
qtkb.sketch.add_circles(
  x,
  y,
  radius,
  sketch_name=None,
)
```

| Argument | Meaning | Example |
|---|---|---|
| `x` | Circle-center X coordinate. | `0.0` or `"<<lKeysLayout>>.A11:X11"` |
| `y` | Circle-center Y coordinate. | `12.0` or `"<<lKeysLayout>>.B3:B26"` |
| `radius` | Circle radius. | `2.0` or `"<<tPivot>>.BearingRadius"` |
| `sketch_name` | Optional internal target-sketch `Name`; when omitted, use the selected sketch. | `"Sketch001"` |

For example, create one circle per linked X position with a shared Y coordinate
and radius:

```python
qtkb.sketch.add_circles(
  "<<lKeysLayout>>.A11:X11",
  "<<tZeroStop>>.SplintPositionY",
  "<<tPivot>>.BearingRadius",
)
```

The circles are normal sketch geometry. Their `DistanceX`, `DistanceY`, and
`Radius` constraints retain their spreadsheet expressions, so later spreadsheet
edits update the sketch parametrically.

### Transposed Matrix Binding

Set `transpose` to `True` when the target matrix is to receive the source
matrix mirrored at its main diagonal. The range limits stay in their ordinary
top-left to bottom-right order; only the source-cell mapping changes.

For example, this writes a `4 x 10` target range while reading from `A1` as a
`10 x 4` source region:

```python
qtkb.spreadsheet.link_cells(
  "<<tKeysLayout>>.A1:D10",
  "<<lMasterGlobals>>.A1",
  True,
)
```

In this mode, target `A1` refers to source `A1`, target `D1` to source `A4`,
and target `A10` to source `J1`. State `True` explicitly only for this
transposed special case.

### Troubleshooting

| Console message | Cause and action |
|---|---|
| `QTKB is not loaded` | Run `QTKB_Reload.FCMacro`. |
| `No active FreeCAD document.` | Open or activate the intended document before running the command. |
| `Target range must be a spreadsheet expression ...` | Pass a direct target expression, for example `"<<tKeysLayout>>.A1:D10"`. |
| `Target spreadsheet not found: ...` | Verify the target sheet's internal `Name` in the FreeCAD tree. |
| `Invalid spreadsheet cell` or `Invalid target range` | Use normal A1 notation and make the end cell down and right of the start cell, for example `"<<tKeysLayout>>.A1:D10"`. |
| `Source range must be a FreeCAD expression ending in an A1 range.` | Pass a complete source expression with an explicit range, for example `"<<lMasterGlobals>>.A1:D10"`. |
| `Source range dimensions do not match ...` | Make the source range the same size as the target range, or use its transposed size when `transpose=True`. |
| `transpose must be True or False.` | Pass `False` for direct binding or `True` for transposed binding. |
| Formula evaluates to an error | Verify the source expression and its internal object name, for example `<<lMasterGlobals>>.A1`. |
| `No sketch selected.` | Select the target `Sketcher::SketchObject` itself in the FreeCAD tree before calling `qtkb.sketch.add_points(...)` without a third argument. |
| `Sketch not found: ...` | Pass the target sketch's internal `Name`, not its visible `Label`, as the third argument. |

## Module Responsibilities

- `transaction.py`: document lookup, one-step undo transactions, and the
  standard command decorator.
- `spreadsheet.py`: spreadsheet selection, validation, formulas, aliases, and
  links.
- `sketch.py`: parametric construction-point distributions from scalars,
  FreeCAD expressions, and linked spreadsheet ranges.
- Future modules should be grouped by QTKB domain, for example `keys.py`,
  `pivot.py`, `reaction_group.py`, or `diagnostics.py`.

Only place reusable library logic in this package. Keep `QTKB_Reload.FCMacro`
as a thin loader.

## Transaction-Based Command Template

Every command that mutates a FreeCAD document should use `@transactional` and
accept `document=None` as a keyword-only or regular keyword argument.

```python
from .transaction import transactional


@transactional("Describe the undo step")
def command_name(parameter, *, document=None):
    object_ = document.getObject("ObjectName")
    if object_ is None:
        raise RuntimeError("Required object not found.")

    object_.Label = parameter
    return object_
```

The decorator opens one FreeCAD undo transaction, supplies the active document
when no document is passed, recomputes after a successful command, and aborts
the entire transaction when the command raises an exception.

For a coordinated sequence of several commands, use one explicit transaction
instead of nesting decorated commands:

```python
from qtkb.transaction import transaction


with transaction("Update key layout") as document:
    # Make all related changes through document.
    pass
```

## Development Rules

- Use internal `Name` values, not user-editable `Label` values, for stable
  object references and expressions.
- Make a command validate inputs before changing the document whenever
  practical.
- Let the transaction wrapper perform the final recompute; do not recompute
  repeatedly inside a cell-writing loop.
- Raise exceptions for failures so FreeCAD aborts the transaction and retains a
  meaningful traceback in the Python console.