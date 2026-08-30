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

## Setup

1. In FreeCAD, add `C:\Work\quarter-tone-keyboard\tools\FreeCAD` to the Macro
  path, or copy/link `tools/FreeCAD/QTKB_Reload.FCMacro` into the configured
  FreeCAD Macro path.
2. Assign `QTKB_Reload.FCMacro` to a keyboard shortcut.
3. Press that shortcut after opening a QTKB document and whenever modules have
  changed in VS Code.

The macro adds the repository `tools/FreeCAD` directory to `sys.path`, imports
`qtkb`, and reloads the editable modules. It is intentionally the only code
that needs to live in the FreeCAD Macro path.

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

Keep module-qualified calls in the FreeCAD Python console:

```python
qtkb.spreadsheet.link_cells("A1:D10", "lMasterGlobals", "A1", "tKeysLayout")
```

After changing a module in VS Code, run `QTKB_Reload.FCMacro` again. Do not use
`from qtkb.spreadsheet import link_cells` for interactive work, because that
name does not follow later module reloads.

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