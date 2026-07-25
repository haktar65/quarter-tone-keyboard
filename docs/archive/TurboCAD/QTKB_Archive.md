# QTKB Archived STEP Exports

The STEP files covered by this note are archive exports only.

They represent drawings and geometry snapshots that are no longer part of the active QTKB workstream, but may still be worth keeping for selective reuse, comparison, or extraction of isolated ideas.

These files should not be treated as active design defaults.
Active geometry and active branch decisions remain defined by:

- `docs/Research.md`
- `docs/BuildGuide.md`
- the current active CAD work under `QTKB.stp` and `QTKB-blocks/`

Current meaning of the archived files:

- `QTKB_Archive.stp`: full archived STEP export of drawings that are no longer needed in the active workstream
- `QTKB_Archive-blocks/`: archived per-block STEP exports kept only for possible later reuse of individual geometry fragments

Usage rule:

- reuse material from this archive deliberately, not implicitly
- when reusing geometry, re-check it against the current synth / semi-weighted branch assumptions before bringing it back into active CAD
- do not interpret archived naming, dimensions, or package logic as current defaults

This archive is intentionally retained as a parts and ideas reservoir, not as a maintained parallel design branch.