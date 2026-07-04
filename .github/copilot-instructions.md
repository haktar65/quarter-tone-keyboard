# Copilot Instructions – Quarter-Tone Keyboard

## Project Context

Building a professional, stage-ready **quarter-tone keyboard** as a MIDI input device.

**Builder:** Physicist with fully equipped workshop (wood, metal, electronics), experienced in firmware development.  
**Player:** Professional jazz pianist (highest technical level, impressionistic improvisation, original compositions).

## Key Requirements

- 24 tones per octave (quarter-tone grid)
- High-quality playability — synth / semi-weighted, reference: Access Virus C with Fatar-style synth action feel
- Stage-ready: pitchbend wheel, volume/expression control
- Phase 1: MIDI input device (USB-MIDI + 5-pin DIN)
- White keys: original piano key covers; black keys: Tough Resin top layer
- Quarter-tone keys: deliberately tactile-distinguishable

## Available Manufacturing

- FDM and SLA 3D printers
- Full woodworking shop (jointer, table saw, band saw, planers, sanders)
- Fully equipped electronics workshop
- Firmware experience (microcontrollers)

## Workspace Structure

```
repo-root/
├── .github/
│   └── copilot-instructions.md   ← this file
├── README.md                     ← English project overview
├── .gitignore
└── docs/
    ├── Research.md               ← active concept decisions and archive boundary (English)
    ├── BuildGuide.md             ← active geometry, build phases, prototype rules, BOM, schematics (English)
    ├── CAD/                      ← OpenSCAD parametric models and milestone geometry files
    └── archive/                  ← historical branches and prior design evidence
```

## Session Continuity

When starting on a new machine or in a new session, do not restart from first principles.

These instructions are repository-relative and must be applied the same way even if the project is checked out into a different directory.

## Startup Reinitialization Protocol

At the beginning of a fresh VS Code session for this repository, first rebuild working context before answering design questions or making proposals.

Mandatory startup routine:

1. Read `.github/copilot-instructions.md` completely.
2. Read `README.md` for the current public project framing and naming.
3. Read `docs/Research.md` as the active concept source.
4. Read `docs/BuildGuide.md` as the active geometry and build source of truth.
5. Only then read the relevant files under `docs/archive/` if historical evidence is needed.
6. Extract and restate internally the current active branch, coordinate baseline, active key-family naming, aftertouch concept, and archive boundary before continuing.
7. Treat active documents as authoritative over archive material unless the user explicitly overrides them in the current session.
8. When a new session reveals that active docs and instructions diverge, update the active docs or this file so the next session inherits the correction.

Minimum context that must be reloaded on startup:

- public project shorthand: `QTKB`
- active branch: synth / semi-weighted
- feel reference: Access Virus C / Fatar-style synth action
- layout principle: Kassel
- scope: `61` main + `61` quarter-tone = `122` keys
- active key families: `MWT`, `MST`, `QWT`, `QST`
- main-key pivot baseline: `Y = 210 mm`, `Z = -12 mm`
- shared pivot rule: `QT` keys share the main pivot axis
- archive rule: archive is historical evidence, not active default

Standard startup summary to reconstruct before continuing work:

- Project: `QTKB`
- Active branch: synth / semi-weighted
- Feel reference: Access Virus C / Fatar-style synth action
- Layout: Kassel
- Scope: `122` keys = `61` main + `61` quarter-tone
- Active key families: `MWT`, `MST`, `QWT`, `QST`
- Main-key pivot baseline: `Y = 210 mm`, `Z = -12 mm`
- Shared pivot rule: `QT` keys use the main pivot axis
- Active source of truth: `docs/Research.md` + `docs/BuildGuide.md`
- Archive rule: use archive as evidence, not as active default

Read in this order before making geometry proposals:

1. `.github/copilot-instructions.md`
2. `docs/Research.md`
3. `docs/BuildGuide.md`
4. only then the relevant files under `docs/archive/`

Use the archive as prior evidence and resolved experimental history, not as an implicit active default.

If active documents and archive disagree:

- active documents win
- explicit user statements in the current session override both
- after a decision change, update the active docs so the next session inherits it

## Ongoing Repository Maintenance

This repository should be maintained so that a later session can continue work without reconstructing project state from scratch.

Mandatory maintenance rules:

- when an active design decision changes, update `docs/Research.md` and `docs/BuildGuide.md` in the same workstream
- when project naming, branch status, or public framing changes, update `README.md`
- when session-start behavior or context-loading rules change, update this file
- keep archive material clearly marked as historical; do not silently merge archived assumptions back into active documents
- prefer adding short explicit mapping notes when terminology changes over rewriting historical archive evidence
- keep the active naming `QTKB`, `MWT`, `MST`, `QWT`, `QST` consistent across new files and edits

## Active Source Hierarchy

- `docs/Research.md`: active branch choice, concept decisions, archive boundary
- `docs/BuildGuide.md`: active geometry source of truth plus practical build summary, prototype sequence, and implementation-facing tables
- `docs/archive/SteinwayLike/`: archived piano-like branch; still valuable for lessons, spring history, sensor-clearance rules, and rejected alternatives

## Working Style

- Design decisions and research → `docs/Research.md`
- Concrete build steps, BOM, schematics → `docs/BuildGuide.md`
- Geometry discussions → OpenSCAD `.scad` files in `docs/CAD/` (preferred over ASCII diagrams)
- Technical depth: physicist level, no basics
- Chat language: German; documentation language: English
- Concise, no padding

## Current Active Mechanics Snapshot (June 2026)

- Active branch: synth / semi-weighted, with Access Virus C and Fatar-style synth action as feel reference
- Layout principle remains Kassel
- Scope remains `122` keys total: `61` main + `61` quarter-tone
- Main-key pivot baseline: `Y = 210 mm`, `Z = -12 mm` relative to the front top edge of a white key at rest
- Main and quarter-tone keys share the same pivot axis; QT keys are short secondary levers, not plungers
- Current active key families: `MWT`, `MST`, `QWT`, `QST`
- QWT top-side span: `Y = 86-170 mm`, rest height `+12 mm` above MWT plane
- QST top-side span: `Y = 116-170 mm`, rest height `+24 mm` above MWT plane
- Active aftertouch stack: `3 mm` EPDM solid cord plus `2 mm` felt strip; `QT` integrates the buffer groove in the lever geometry, while `MT` keeps the buffer mostly in the raster with only about `4 mm` protruding above it
- Current direct-under-key aftertouch assumption: same local force law per key type, with about `+2 mm` additional reserve beyond normal travel, but with different `MT` and `QT` buffer packaging
- Splint / buffer / sensor are now packaged as one reaction group per key family, referenced `5 mm` behind the key front edge in the full-aftertouch tilt state
- Active guide splints: brass, `2.5 mm` diameter, with variable lengths by key family; current sensor-to-splint spacing inside the reaction group is about `22 mm` centre-to-centre
- Current PTFE guide lengths: `18 mm` for `MT`, `15 mm` for `QT`
- The `30 mm` clearance rule now applies to ferromagnetic hardware around the Hall sensors, especially steel screws, washers, frame parts, and floor-side metal below the sensor
- Rear zero stop remains at `Y = 285 mm`; terminal end stop remains on the split-pin / guide line

## Archive Usage Rules

- Search the archive deliberately when a design question feels already explored.
- Reuse archive knowledge such as measurements, failure modes, spring tests, sensor spacing, and packaging lessons.
- Do not silently revive discarded piano-like geometry or obsolete MT/QT kinematics.
- When pulling a value from the archive into the active branch, state that explicitly and verify it against the current synth branch assumptions.

## Decided Design Questions (May 2026)

- **Layout:** Kassel Principle (Organ St. Martin, Kassel) — three depth planes, three height planes per octave
- **Scope:** 61 base keys (5 octaves + 1 C) = 122 keys total with QT extension
- **Sensor concept:** One A1324LUA-T linear Hall sensor per key, Ø4×3 mm N45 magnet on key. Continuous analog signal → velocity from time between thresholds; aftertouch from last 1–2 mm into elastomer stop. No FSR, no purchased keybed.
- **Aftertouch:** Resione F80 form part in captive pocket geometry (preferred) or Shore A 30–40 O-ring. Target: 3–4 mm travel, 0.5–1.0 N.
- **MIDI:** 24-tone mapping, notes 0–121, no MPE. Scala tuning in Logic Pro + SuperCollider.
- **Microcontroller:** Teensy 4.1 (600 MHz, native USB-MIDI). 8× CD74HC4067 16:1 mux → 8 analog pins for 122 channels.
- **Firmware architecture:** Teensy = real-time sensor front-end only. Raspberry Pi (Phase 2) = protocol back-end (MIDI/OSC/SuperCollider). Compressed event format ~4 bytes/event.
- **Frame:** SLA Tough Resin half-octave modules. 4 mm steel pivot pin per module.
- **Base structure:** Aluminium square tube frame with ASA node connectors (internal knurling + epoxy + M4 heat-set inserts).
- **Key material:** Polymaker PolyLite ASA (Tg ~108°C), printed upright.
- **Springs:** Tension spring Ø3–4 mm, wire Ø0.3 mm, k ≈ 0.12 N/mm.
- **Weights:** ~15–20 g lead in key tail.

## Purchased / Ordered (May 2026)

- A1324LUA-T Hall sensors: 50 pcs ordered
- Polymaker PolyLite ASA: 3 kg ordered
- Springs: ordered, awaiting delivery

## Current Open Questions

1. Final guide / bearing execution for tilted QT guide pins and whether PTFE inserts or direct ASA guidance work better in practice
2. Final sensor position, split-pin line, and full-aftertouch conversion for the active synth branch
3. Test bench build: one main key + one QT key with full sensor, spring, weight, and aftertouch stack