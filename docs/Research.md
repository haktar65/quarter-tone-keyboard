# Quarter-Tone Keyboard (QTKB) – Research & Concept

## Project Goal

Build a high-quality, stage-ready quarter-tone keyboard as a MIDI input device for a professional player.

Public shorthand for GitHub-facing material: `QTKB`.

Fixed top-level goals:

- quarter-tone grid with `24` tones per octave
- high-quality, repeatable playing feel
- stage-ready controls and robust hardware
- custom mechanics, sensing, electronics, and firmware

## Current Mechanical Direction

Update June 2026: the active target category is now a synthesizer / semi-weighted action with integrated aftertouch.

Primary feel reference:

- Access Virus C
- Fatar-family synth keyboard feel

This replaces the previously explored deeper piano-like intermediate branch as the active target mechanism.

## Pianist-Critical Requirements

The following remain decisive for the active branch:

- professional appearance and tactile quality
- reliable touch distinction between main keys and quarter-tone keys
- controlled, musically usable aftertouch
- consistent response across the full keyboard
- no cheap controller feel

The active branch no longer optimizes around hammer-action-like proportions.

## Fixed Decisions That Remain Active

The branch change does not affect these decisions:

- layout principle: Kassel Principle
- scope: `61` main keys plus `61` quarter-tone keys
- key sensing: one Hall sensor per key
- aftertouch principle: travel into an elastomeric stop rather than FSR-based force sensing
- firmware split: real-time sensor front-end plus higher-level protocol/control layer
- stage focus: USB-MIDI, 5-pin DIN, performance controllers

## Mechanical Consequences of the New Direction

The active synth / semi-weighted branch implies:

- shallower action depth than the archived piano-like branch
- lower moving mass and less emphasis on long piano-style front lever arms
- aftertouch must be designed into the base mechanism from the start
- pivot, travel, and return-force geometry must be re-derived from the synth-action category, not reused from the archived branch
- QT integration should be solved against the lighter action family, not against a deep hammer-style package

## Open Geometry Questions for the Active Branch

The following items now define the active research backlog:

- exact Access Virus C keybed family / concrete Fatar reference if identifiable
- main-key travel target for the synth branch
- black-key travel target for the synth branch
- pivot position and effective lever arms for a synth-like mechanism
- required pivot-axle capture in lever direction; the first print suggests the current wrap is too small, so a roughly `180 deg` capture should be tested as an active candidate where spacer washers already retain the axle laterally
- aftertouch onset travel, reserve travel, and target force range
- how the quarter-tone rows should be coupled to the shallower main-key geometry
- Hall sensor placement for the new shallower package

## Electronics and Firmware Direction

The action-family switch does not change the preferred electronics architecture:

- Teensy remains the real-time sensor front-end
- Hall sensors remain the key-position sensing basis
- multiplexed analog acquisition remains acceptable
- optional second processor / protocol back-end remains open

## Active Zero-Stop Damping Decision

Update June 2026:

- the rear zero stop remains a hard geometric rest-height reference, not a soft free-working stop
- acoustic damping at the zero stop may be added, but only as a thin, strongly constrained working layer in front of a hard rail
- preferred first damping forms are a small solid profile or strip in `TPU` or `PORON`, not a hollow profile
- hollow profiles remain possible as acoustic experiments, but they are not the preferred reference-defining construction because they are more prone to hysteresis, temperature sensitivity, and rest-height drift
- shrink tube may still be used around separate trim-mass pieces as a pragmatic noise-reduction measure, but it should not be shrunk directly on the mounted `ASA` lever and should not define the zero-stop geometry

## Archive Boundary

The previously explored piano-like intermediate branch is now preserved only as an archive snapshot under:

- `docs/archive/SteinwayLike/Research.md`
- `docs/archive/SteinwayLike/BuildGuide.md`
- `docs/archive/SteinwayLike/MP5GeometryReference.md`
- `docs/archive/SteinwayLike/SteinwayLikeArchive.md`

Those files remain useful as historical design context, but they no longer define the active geometry target.

Historical archive terminology may still use earlier internal abbreviations.

## Immediate Next Steps

- identify the best usable Access Virus C / Fatar reference data
- define the active coordinate system for the synth branch
- establish first main-key synth geometry targets
- derive quarter-tone packaging rules from the new shallow action category
- test whether a roughly `180 deg` pivot wrap gives enough directional stiffness in the lever while remaining practical with the washer-retained axle concept
- build a single-key prototype around the synth-action assumptions