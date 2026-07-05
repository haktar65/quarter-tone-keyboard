# Export-TurboCADStep.vbs

Small helper script for exporting one TurboCAD `.tcw` drawing and its blocks as STEP files.

## What it does

- opens the source `.tcw` through TurboCAD COM automation
- creates a temporary working copy inside `_tcw-temp`
- exports the full drawing as `<project>.stp`
- clears the working drawing, inserts one block, and exports that state as one STEP file per block
- writes block STEP files into `<project>-blocks`

## Requirements

- Windows
- TurboCAD 2020 installed locally
- TurboCAD COM automation available as `TurboCAD.Application`
- the source drawing should contain 3D geometry that TurboCAD can actually write to STEP

Pure 2D blocks may not produce useful STEP output.

## Usage

```cmd
cscript //nologo Export-TurboCADStep.vbs <input.tcw> <output-dir> [visible]
```

Example:

```cmd
cscript //nologo Export-TurboCADStep.vbs "C:\path\to\drawing.tcw" "C:\path\to\export" True
```

## Parameters

- `input.tcw`: source TurboCAD file
- `output-dir`: target folder for the exported STEP files
- `visible`: optional Boolean, usually `True` or `False`; default is `True`

## Output layout

```text
export/
├── <project>.stp
├── <project>-blocks/
│   ├── BlockA.stp
│   ├── BlockB.stp
│   └── ...
└── _tcw-temp/
    └── <project>-working-<timestamp>.tcw
```

## Current behavior

- the script aborts immediately if any `tcw27.exe` process is already running
- existing STEP files with the same name are overwritten
- block names are sanitized for Windows file names
- the script prints `Writing: ...` for each STEP file it exports
- the script attempts to delete the temporary working copy at the end

## Notes

- the block export path currently uses the block name in `AddBlockInsertion`
- runtime errors are intentionally not masked; VBScript should stop directly on the failing line
- after `SaveCopyAs`, the script still checks whether the STEP file was actually written

## First troubleshooting steps

- run once with `True` as the third argument so you can watch TurboCAD during the export
- if the script aborts on a specific line, use that exact VBScript line number as the primary debugging anchor
- test the same drawing manually in TurboCAD with a normal STEP export to confirm that the geometry is STEP-compatible