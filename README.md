# Quarter-Tone Keyboard (QTKB)

A professional, stage-ready 24-tone-per-octave MIDI keyboard instrument with a custom quarter-tone layout, custom sensing, and a newly active synthesizer / semi-weighted action direction.

Public shorthand for GitHub-facing material: `QTKB`.

## Current Direction

- Layout: Kassel Principle with `61` standard keys + `61` quarter-tone keys
- Active feel target: Access Virus C / Fatar-family synth action feel
- Active mechanical category: synthesizer / semi-weighted with integrated aftertouch
- Sensors: one Hall sensor per key
- Phase 1: MIDI input device with USB-MIDI and 5-pin DIN

## Documentation Map

- `docs/Research.md`: active concept and design rationale
- `docs/BuildGuide.md`: active geometry, build, and prototyping document
- `docs/archive/SteinwayLike/`: archived piano-like intermediate branch, including former `Research.md`, `BuildGuide.md`, and MP5 reference notes
- `docs/CAD/`: OpenSCAD models and milestone geometry files

## Working Method

This repository is maintained so that design work can continue across fresh checkouts and new VS Code sessions without reconstructing context from scratch.

Operational rules:

- active design decisions belong in `docs/Research.md`
- active geometry, prototype rules, and build-facing tables belong in `docs/BuildGuide.md`
- public project framing and naming belong in `README.md`
- historical branches stay under `docs/archive/` and are used as evidence, not as the active default
- when terminology changes, active documents are updated first and archive material gets explicit mapping notes where needed

## AI Collaboration In VS Code

The project is developed with AI assistance inside VS Code.

Current collaboration pattern:

- the AI first reloads repository instructions and active documents before making design proposals
- active source priority is: `.github/copilot-instructions.md`, `README.md`, `docs/Research.md`, `docs/BuildGuide.md`, then relevant archive files only if needed
- geometry decisions are expected to be carried in OpenSCAD files under `docs/CAD/` when practical
- chat discussion can remain in German, while repository documentation is kept in English
- when a decision changes, the AI is expected to update the relevant repository documents so later sessions inherit the result

Typical startup summary for a fresh session:

- project shorthand: `QTKB`
- active branch: synth / semi-weighted
- feel reference: Access Virus C / Fatar-style synth action
- layout principle: Kassel
- scope: `122` keys total
- active key families: `MWT`, `MST`, `QWT`, `QST`

## Active Technical Direction

The active workstream no longer uses the previously explored deep piano-like geometry as its target mechanism.

Current focus:

- shallower synth-action packaging
- integrated aftertouch as a first-class design feature
- consistent semi-weighted feel across all `122` keys
- quarter-tone integration without inheriting hammer-action geometry penalties

## Preserved Decisions

These decisions remain active across the branch change:

- quarter-tone layout based on the Kassel Principle
- Hall sensor sensing concept
- Teensy-based real-time front-end architecture
- stage-ready control concept including pitch bend and expression controls
- custom mechanical implementation rather than direct reuse of a stock 12-tone keybed

## Status

- [x] Kassel layout selected
- [x] Hall sensor concept selected
- [x] Archived the earlier `Steinway-like` branch under `docs/archive/SteinwayLike/`
- [x] Switched active direction to synth / semi-weighted action
- [ ] Verify exact Access Virus C / Fatar reference geometry
- [ ] Define active main-key synth geometry
- [ ] Define active QT geometry for the synth branch
- [ ] Build synth-branch single-key test bench