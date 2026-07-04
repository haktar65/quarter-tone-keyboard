# Steinway-Like Archive

This document freezes the previously explored piano-like intermediate state as an archive snapshot.

Archived naming note:

- `VT` is the historical archive label for the quarter-tone key family and corresponds to the active `QT` terminology
- this archive snapshot predates the active four-family naming `MWT`, `MST`, `QWT`, `QST`

Project shorthand: `Steinway-like` does **not** mean reverse-engineered Steinway geometry. It means a deeper, more piano-oriented action family with comparatively long front lever arms, piano-like pivot placement, and a correspondingly heavier mechanical category than the newly selected synth / semi-weighted target.

## Status

- Archived: June 2026
- Reason for archive: the pianist now clearly prefers a synthesizer / semi-weighted keyboard with aftertouch, and the Access Virus C feel is currently the strongest reference
- Active successor direction: Access Virus C / Fatar-style synth action with dedicated aftertouch integration

## What Is Archived Here

The archived branch includes the current geometry and packaging assumptions for:

- piano-like main-key pivot placement
- front-side standard-key aftertouch package
- VT geometry behind the pivot
- reinforced pivot-frame concept for the deeper action family
- MP5-derived reference proportions used as a design anchor

## Archived Main-Key Reference Geometry

Archived normal-key baseline from the current documentation:

- White-key front reference point at rest: `O = (0, 0)`
- Main-key pivot axis: `Y = 210.0 mm`, `Z = -24.0 mm`
- Front guide pin: `Y = 60.0 mm`
- White-key bottom-stop front travel: `10.8 mm`
- Black-key bottom-stop front travel: `10.0 mm`
- White-key bottom-stop rotation: `2.95 deg`
- Black-key bottom-stop rotation: `3.66 deg`

Archived current standard-key aftertouch construction state:

- Front first contact / end-stop contact zone: `Z = -43.0 mm`
- Aftertouch hard end: `Z = -46.0 mm`
- Additional aftertouch rotation: about `1.10 deg`
- White-key front point with aftertouch: `14.83 mm`, `4.05 deg`
- Black-key front reference with aftertouch: `13.0 mm`, `4.76 deg`

## Archived VT Geometry Snapshot

Archived VT reference state from the current documentation:

- VT pivot axis: `Y = 245.0 mm`, `Z = 10.0 mm`
- VT rear guide pin: `Y = 290.0 mm`
- VT return spring anchor: `Y = 263.0 mm`
- Current translated VT aftertouch zone: `Y = 370.0 mm`
- VT rear hard end-stop: `Y = 380.0 mm`
- VT Hall sensor zone: `Y = 390.0 mm`
- Pin-to-sensor clearance in the translated package: `100 mm`

Archived VT lever interpretation:

- VT row above whole tones: front lever arm `155 mm`
- VT row above semitones: front lever arm `125 mm`
- A `3.0 mm` local compression at `Y = 370 mm` corresponds to about `3.72 mm` front travel on the whole-tone VT row and `3.00 mm` on the semitone VT row

## Archived Structural Interpretation

The archived deeper-action branch also includes the following structural assumptions:

- main-key pivot category remains piano-like rather than synth-like
- VT pivot packaging is the main geometric bottleneck
- VT lever body may remain around `13 x 20 mm` in the main load-bearing zone
- VT pivot region may locally grow to about `22 mm` total height
- pivot bushings / local bearing inserts may use Tough Resin with about `5 mm` wall thickness

## Archived MP5 Reference

The archived branch also includes the MP5 comparison gathered in the separate reference note:

- action family confirmed publicly: `AHA IV-E with AR technology`
- public external envelope confirmed: `1356 x 340 x 172 mm`
- project-side MP5-like working pivot reference: `Y = 210 mm`, `Z = -24 mm`

That MP5 note remains useful as a proportional reference for the archived branch, but it is not a factory-proven internal Kawai CAD dataset.

## Active Direction After the Archive Decision

This archive means the project should no longer treat the above geometry as the active target mechanism.

New active mechanical direction:

- category: synthesizer / semi-weighted
- primary feel reference: Access Virus C
- keybed family reference: Fatar keyboard feel
- aftertouch integration should be designed as a first-class feature, not as an add-on to a hammer-action-like mechanism
- new layout work should start from the lighter synth-action category rather than from the archived piano-like proportions

## Source Documents Preserved by This Archive

The archive snapshot is distilled from the following current project files:

- `docs/BuildGuide.md`
- `docs/Research.md`
- `docs/Archiv/SteinwayLike/MP5GeometryReference.md`

These files may continue to evolve, but this archive records the state that should now be regarded as the closed `Steinway-like` branch.