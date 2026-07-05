# QTKB STEP Exports

The STEP files in this folder are currently direct exports from the active QTKB working drawing.

At this stage they should be treated as working geometry snapshots, not as a curated release set.
The source drawing still contains parallel design experiments, intermediate variants, and naming that reflects the current TurboCAD work structure rather than a final part taxonomy.
In particular, `QTKB.stp` should currently be expected to change substantially over time because it is the direct export of the active working map.

Because of that, the exported STEP files are intentionally not documented one by one yet.
Adding detailed per-file notes at this point would create documentation overhead without much long-term value.

Current meaning of the exported files:

- `QTKB.stp`: full export of the current working drawing; this file may change strongly and often because the underlying working map is still in active exploratory use
- `QTKB-blocks/`: per-block STEP exports generated from the same working drawing; these are also still provisional, but the individual block exports are expected to stabilize earlier than the full drawing export

Once the design stabilizes, the STEP exports will be cleaned up, grouped more deliberately, and documented individually.