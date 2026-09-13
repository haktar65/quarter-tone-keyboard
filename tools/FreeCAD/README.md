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

The normal user workflow has three steps:

1. Open the target FreeCAD document.
2. Run `QTKB_Reload.FCMacro` after opening the document and after editing a
  QTKB helper in VS Code.
3. Run a documented command in the Python console, or run a project macro
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
imports `qtkb`, and reloads the editable modules. It contains no
machine-specific path, so the same checkout can be used from another location.
Keep the macro inside this directory; it is intentionally the only code that
needs to be registered in FreeCAD's Macro path.

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

Run `QTKB_Reload.FCMacro` first. Then use module-qualified, parameterized
calls either in the Python console or in another small project macro:

```python
qtkb.spreadsheet.link_cells("A1:D10", "lMasterGlobals", "A1", "tKeysLayout")
```

The arguments are deliberately explicit: target range, internal source-link
name, required first source cell, optional internal target-sheet name, and
optional transpose mode. If the target-sheet name is omitted, the command uses
the selected spreadsheet. Every call is one undoable FreeCAD transaction.

For a repeatable task, create a thin macro beside `QTKB_Reload.FCMacro` that
only supplies project-specific parameters. Do not duplicate the library logic:

```python
import qtkb

qtkb.spreadsheet.link_cells(
  "A1:D10",
  "lMasterGlobals",
  "A1",
  "tKeysLayout",
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
- The active document contains an `App::Link` to the source spreadsheet.
- The link's internal `Name`, not its user-visible `Label`, is known.
- The target spreadsheet's internal `Name` is known, or it is selected in the
  FreeCAD tree before the command is run.

Use the internal names shown in the tree's property editor. For example,
`lMasterGlobals` and `tKeysLayout` are names, while a translated or manually
renamed label is not a stable command argument.

### Command

```python
qtkb.spreadsheet.link_cells(
  target_range,
  source_link_name,
  source_start_cell,
  target_sheet_name=None,
  transpose=False,
)
```

| Argument | Meaning | Example |
|---|---|---|
| `target_range` | One cell or a rectangular target range in A1 notation. | `"B3:E8"` or `"A1"` |
| `source_link_name` | Internal name of the `App::Link` whose `LinkedObject` is the source spreadsheet. | `"lMasterGlobals"` |
| `source_start_cell` | Required upper-left source cell. Source cells advance by the same row and column offsets as the target range. | `"C5"` |
| `target_sheet_name` | Optional internal name of the target spreadsheet. When omitted, the currently selected spreadsheet is used. | `"tKeysLayout"` |
| `transpose` | Optional mode, default `False`. `True` mirrors the source mapping at the range diagonal. | `False` or `True` |

### Examples

Link a `4 x 10` region in a named target spreadsheet, starting at the top-left
cell of the linked master spreadsheet:

```python
qtkb.spreadsheet.link_cells(
  "A1:D10",
  "lMasterGlobals",
  "A1",
  "tKeysLayout",
)
```

Link one target cell to a different source cell:

```python
qtkb.spreadsheet.link_cells(
  "B7",
  "lMasterGlobals",
  "F12",
  "tKeysLayout",
)
```

Link a range to the spreadsheet currently selected in the tree:

```python
qtkb.spreadsheet.link_cells(
  "C3:F6",
  "lMasterGlobals",
  "H2",
)
```

The first example writes expressions such as:

```text
=<<lMasterGlobals>>.LinkedObject.A1
```

The target cell at `D10` then refers to source cell `D10`.
`source_start_cell` is required so the intended source region is never
implicit. `transpose` defaults to `False`, so normal bindings do not need to
state it. Existing expressions or values in the selected target range are
replaced. The full write operation is a single undoable action and triggers one
final document recompute.

### Transposed Matrix Binding

Set `transpose` to `True` when the target matrix is to receive the source
matrix mirrored at its main diagonal. The range limits stay in their ordinary
top-left to bottom-right order; only the source-cell mapping changes.

For example, this writes a `4 x 10` target range while reading a `10 x 4`
source region:

```python
qtkb.spreadsheet.link_cells(
  "A1:D10",
  "lMasterGlobals",
  "A1",
  "tKeysLayout",
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
| `No target spreadsheet found.` | Pass `target_sheet_name="..."` with the internal sheet name, or select a spreadsheet in the tree. |
| `Invalid spreadsheet cell` or `Invalid target range` | Use normal A1 notation and make the end cell down and right of the start cell, for example `"A1:D10"`. |
| `transpose must be True or False.` | Pass `False` for direct binding or `True` for transposed binding. |
| Formula evaluates to an error | Verify that `source_link_name` is an `App::Link` and that its `LinkedObject` is the intended source spreadsheet. |

## Module Responsibilities

- `transaction.py`: document lookup, one-step undo transactions, and the
  standard command decorator.
- `spreadsheet.py`: spreadsheet selection, validation, formulas, aliases, and
  links.
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