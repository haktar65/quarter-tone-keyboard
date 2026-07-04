# Quarter-Tone Keyboard (QTKB) – Build Guide

This is the active build guide for the synth / semi-weighted workstream and the single active technical source for geometry, prototype rules, and build decisions.

Public shorthand for GitHub-facing material: `QTKB`.

The previously documented piano-like intermediate branch is no longer active and is preserved under `docs/Archiv/SteinwayLike/`.

## Active Branch Context

- Active branch: June 2026 onward
- Primary feel reference: Access Virus C
- Keybed family reference: Fatar-style synth action
- Active mechanical category: synthesizer / semi-weighted with integrated aftertouch

Active design anchors:

- shallower package than the archived piano-like branch
- consistent feel across all `122` keys
- quarter-tone keys may differ in force and geometry, but must remain inside the same overall action family
- aftertouch is part of the base key-travel design, not an add-on

## Active Reference Interpretation

Current externally supported reference facts:

- the keyboard Virus C variant (`Virus KC`) is a `61`-key instrument
- it is described publicly as `61 semi-weighted keys`
- it supports velocity and monophonic aftertouch at the keyboard level
- current Fatar synth families such as `TP/9S`, `TP/8S`, and `TP/8SK` are explicitly listed as synthesizer keyboards and are offered with `61`-key variants and aftertouch options

Current working conclusion:

- the player-facing `MT` dimensions can remain unchanged
- the player-facing `QT` top-side dimensions can also remain unchanged for now
- the redesign focus is the internal mechanics, packaging depth, return system, sensor placement, and aftertouch integration

Current interpretation of the reference aftertouch category:

- public Fatar information suggests pressure-oriented aftertouch sensing with very little intentional extra travel
- for this project, Hall-based aftertouch should therefore use a small but deliberate reserve travel instead of blindly copying a near-zero-travel pressure-strip concept
- the active design question is not a published Fatar aftertouch travel number, but the reserve travel that is musically useful in this custom Hall-based action

## Frozen Player-Side Dimensions

These player-facing dimensions remain active until contradicted by prototype evidence:

- `MT` octave width: `165.0 mm`
- `MT` white key width at front: `23.6 mm`
- `MT` white visible length: `150.0 mm`
- `MT` black key width: `12.5 mm`
- `MT` black visible length: `95.0 mm`
- `MT` black key height above white: `12.0 mm`
- `QT` width: `<= 12.5 mm`
- `QWT` top-side span: `Y = 86-170 mm`
- `QWT` rest height above `MWT` plane: `+12 mm`
- `QST` top-side span: `Y = 116-170 mm`
- `QST` rest height above `MWT` plane: `+24 mm`
- `QT` front-travel target band: about `8-10 mm`

## Build Phase Overview

| Phase | Content | Status |
|---|---|---|
| 1 | Define synth-action geometry baseline | Active |
| 2 | Build single-key synth-action test bench | Open |
| 3 | Verify Hall sensor and aftertouch package | Open |
| 4 | Derive quarter-tone integration for the synth branch | Open |
| 5 | Build one-octave mock-up | Open |
| 6 | Electronics prototype | Open |
| 7 | Firmware integration | Open |
| 8 | Full mechanical iteration | Open |

## Phase 1: Active Geometry Baseline

Coordinate system rule:

- white-key front top edge at rest: `O = (0, 0)`
- `Y` points rearward from the player
- `Z` points upward relative to the white-key top reference plane

Active geometry rules:

- use main-key pivot baseline `Y = 210 mm`, `Z = -12 mm`
- `QT` keys are short secondary levers on the shared main pivot axis, not on a separate `QT` pivot axis
- do not silently revive archived defaults such as `Y = 210 mm`, `Z = -24 mm` or the earlier two-axis proposal `MT = (195, -12)`, `QT = (235, 6)`
- treat splint, buffer, and sensor as one compact reaction group per key family while keeping the four family lanes `MWT`, `MST`, `QWT`, and `QST` separate from each other
- keep aftertouch inside the core travel design from the beginning

Active support and stop architecture:

- use pins for lateral guidance and anti-twist control
- use a simple laid-in pivot axle with spacer washers as the current key-spacing baseline
- allow the axle and spacer stack to be bonded into a removable holder cradle with `UHU Endfest`
- use replaceable Tough Resin bearing inserts rather than making the structural frame the wear part
- keep only the rear zero stop behind the pivot; the terminal end stop stays on the split-pin / guide line
- preserve the tail volume behind the pivot for zero-stop packaging, spring hardware, and optional trim mass

Active packaging rules:

- `6 mm` maximum lever body within a `6.8 mm` per-key lane
- `16-18 mm` first-pass box height over most of the hidden lever body
- `20-22 mm` local build-up around pivot, spring eye, guide-bushing pocket, and optional weight pocket
- prototype the lever, cradle, stop, and support geometry in `FDM` first before introducing metal construction

Current key-family naming:

- `MWT` = Main Whole-tone key
- `MST` = Main Semitone key
- `QWT` = Quarter Whole-tone key
- `QST` = Quarter Semitone key

## Phase 2: Single-Key Test Bench

Immediate prototype goal:

- one main key in the new synth-action category
- one matching quarter-tone key concept for packaging comparison
- Hall sensor position and magnet geometry representative of the active branch
- integrated aftertouch travel reserve as part of the base design

The first prototype must answer:

- whether the intended synth-like feel is reachable with the chosen lever and return concept
- how much travel reserve is available for aftertouch without destroying the main playing feel
- how much depth the active branch actually needs

Current first-pass key-family tables:

### MWT Key

| Field | Current value | Note |
|---|---|---|
| Motion concept | Main lever | Standard white-key family |
| Front reference point | `Y = 0 mm`, `Z = 0 mm` | White-key front top edge at rest |
| Pivot axis | `Y = 210 mm`, `Z = -12 mm` | Active working baseline |
| Lever width | `6 mm` maximum | Shared current lever width inside a `6.8 mm` per-key lane |
| Box height over hidden lever | `16-18 mm` | FDM baseline |
| Box height at pivot section | `20-22 mm` | Local reinforced height |
| Normal front travel | `9.8 mm` | Current white-key reference under the fixed full-aftertouch geometry |
| Key angle at normal travel | `2.67 deg` | From `asin(9.8 / 210)` |
| Key angle at full aftertouch | `3.2 deg` | Fixed user value for the full-aftertouch end position |
| Spring start | `20 x 4 x 0.5 mm`, `22.0 mm` eye-to-eye at rest | First fixed start value without trim weights |
| Zero stop | `Y = 285 mm` | Hard printed rail |
| End stop | Split-pin / guide line | Terminal stop line |

### MST Key

| Field | Current value | Note |
|---|---|---|
| Motion concept | Main lever | Standard black-key family |
| Front reference point | `Y = 53.5 mm`, `Z = 12.0 mm` | Black-key top reference plane at rest |
| Pivot axis | `Y = 210 mm`, `Z = -12 mm` | Shared main-key pivot |
| Lever width | `6 mm` maximum | Shared current lever width inside a `6.8 mm` per-key lane |
| Box height over hidden lever | `16-18 mm` | FDM baseline |
| Box height at pivot section | `20-22 mm` | Local reinforced height |
| Normal front travel | `10.0 mm` | Current standard black-key travel |
| Key angle at normal travel | `3.66 deg` | From `asin(10.0 / 156.5)` |
| Key angle at full aftertouch | `4.3 deg` | Fixed user value for the full-aftertouch end position |
| Spring start | `20 x 4 x 0.4 mm`, `21.5 mm` eye-to-eye at rest | First fixed start value without trim weights |
| Zero stop | `Y = 285 mm` | Hard printed rail |
| End stop | Split-pin / guide line | Terminal stop line |

### QWT Key

| Field | Current value | Note |
|---|---|---|
| Motion concept | Short secondary lever | Shared main pivot axis, no separate QT pivot axis |
| Front reference point | `Y = 86 mm`, `Z = 12 mm` | QWT top front edge at rest |
| Pivot axis | `Y = 210 mm`, `Z = -12 mm` | Shared main-key pivot |
| Lever arm to front reference | `124 mm` | `210 - 86` |
| Top-side width | `<= 12.5 mm` | Current QT width limit |
| Visible length | `84 mm` | Top-side span `Y = 86-170 mm` |
| Rest height above MWT plane | `+12 mm` | Whole-step quarter-tone row |
| Normal front travel target | About `8-10 mm` | Current target band |
| Key angle at normal travel | `3.70-4.63 deg` | From `asin(8/124)` to `asin(10/124)` |
| Key angle at full aftertouch | `5.6 deg` | Fixed user value for the full-aftertouch end position |
| Box height at pivot section | `20-22 mm` | Shared first-pass reinforcement zone; use the upper end where the guide-bushing pocket sits in the `6 mm` body |
| Local QT body height | `16-18 mm` | Same first-pass box height as the main-key family; increase only where splint, spring, or local insert packaging demands it |
| Spring start | `25 x 4 x 0.4 mm`, `26.0 mm` eye-to-eye at rest | First fixed start value without trim weights |

### QST Key

| Field | Current value | Note |
|---|---|---|
| Motion concept | Short secondary lever | Shared main pivot axis, no separate QT pivot axis |
| Front reference point | `Y = 116 mm`, `Z = 24 mm` | QST top front edge at rest |
| Pivot axis | `Y = 210 mm`, `Z = -12 mm` | Shared main-key pivot |
| Lever arm to front reference | `94 mm` | `210 - 116` |
| Top-side width | `<= 12.5 mm` | Current QT width limit |
| Visible length | `54 mm` | Top-side span `Y = 116-170 mm` |
| Rest height above MWT plane | `+24 mm` | Semitone quarter-tone row |
| Normal front travel target | About `8-10 mm` | Current target band |
| Key angle at normal travel | `4.88-6.11 deg` | From `asin(8/94)` to `asin(10/94)` |
| Key angle at full aftertouch | `7.2 deg` | Fixed user value for the full-aftertouch end position |
| Box height at pivot section | `20-22 mm` | Shared first-pass reinforcement zone; use the upper end where the guide-bushing pocket sits in the `6 mm` body |
| Local QT body height | `16-18 mm` | Same first-pass box height as the main-key family; increase only where splint, spring, or local insert packaging demands it |
| Spring start | `25 x 4 x 0.4 mm`, `26.5 mm` eye-to-eye at rest | First fixed start value without trim weights |

### Shared Summary

| Field | Current value | Note |
|---|---|---|
| Return-spring line | `Y = 235 mm` | Common first spring line for all four key types |
| Zero-stop material | Printed hard rail, preferred `ASA`, `PETG` acceptable for fast tests | Height should be defined by the hard rail even when a damping layer is added |
| Zero-stop contact width in `Y` | `2.5-3.0 mm` | Narrow, defined contact band for repeatable rest height |
| Zero-stop contact width across lever | `4-5 mm` on a `6 mm` lever | Keeps contact defined without using the full width as a hard impact plane |
| Zero-stop damping option | Thin constrained solid `TPU` or `PORON` strip/profile in front of the hard rail | Preferred first damping approach; do not use a hollow profile as the default reference-defining stop |
| Zero-stop height adjustment | Shim or tape on hard rail | Prototype-friendly replacement for paper punching / key punching |
| Optional trim-mass zone | `Y = 255-285 mm` | Can stay in the original active zone; shrink-wrapped weight may also damp the zero stop when weights are used, but should not define the stop geometry |
| First trim-mass test piece | `5 g`, `19 x 11 x 3 mm` | Current available test weight; usable on a `6 mm` lever if mounted lengthwise in `Y` and upright in `Z` |
| First trim-mass test placement | Center about `Y = 275 mm` | Fits the restored active trim-mass zone well; use a local carrier or reinforced lever section if needed |
| Weight packaging note | `19 mm` in `Y`, `3 mm` across lever width, `11 mm` in `Z` | Standing lengthwise packaging is acceptable because height is available behind the pivot |
| Functional package lanes | `MWT`, `MST`, `QWT`, `QST` | Separate reaction-group lanes by key family; within each lane splint, buffer, and sensor are now packaged together |
| Reaction-group reference | `5 mm` behind the key front edge in the full-aftertouch tilt state | Current placement reference for each splint / buffer / sensor group |
| Reaction-group sensor / splint spacing | `22 mm` centre-to-centre | Current brass-splint packaging distance inside the reaction group |
| Guide-splint angle rule | Splint axis and splint-bushing axis each use half of the maximum local key tilt angle | Keeps the PTFE-lined bore closer to horizontal inside the key while sharing angular error between pin and bushing |
| Guide splint orientation | Aligned with the local key travel | Minimize corrective post-bending; use bending only for small final fitting corrections |
| Guide splint material and diameter | Brass, `2.5 mm` | Current active guide-pin baseline; small corrective bending remains possible if needed during fitting |
| Guide splint length | Variable by key family | Do not force one common splint length for `MWT`, `MST`, `QWT`, and `QST`; set the effective length per key type |
| Guide bushing block format | `4 x 6 x 32 mm` | First-pass rectangular outer package |
| PTFE-lined length inside bushing | `18 mm` for `MT`, `15 mm` for `QT` | Current fixed guide-liner baseline |
| PTFE retention concept | Pocket plus adhesive | PTFE liner should sit in a form-locking pocket; roughen the outer PTFE surface first and use cyanoacrylate only as position-locking support, not as the primary structural element |
| Guide bushing overlength | `+2 mm` relative to splint | Gives end margin beyond the effective splint length for each key family |
| Guide-bushing governing case | `QWT` and `QST` | `MT` keys still have more surrounding material at the splint location; the narrow `QT` keys are the actual strength and packaging limit case |
| QT bushing-side wall condition | About `1 mm` per side at `6 mm` key width | Acceptable for the first prototype if the bushing zone is locally reinforced in `Z` and all pocket transitions keep generous radii |
| Full-aftertouch reference angles | `MWT 3.2 deg`, `MST 4.3 deg`, `QWT 5.6 deg`, `QST 7.2 deg` | Fixed user values for the geometric layout at the maximum aftertouch stop |
| Guide half-angle values | `MWT 1.6 deg`, `MST 2.15 deg`, `QWT 2.8 deg`, `QST 3.6 deg` | Splint axis and splint-bushing axis each use half of the local full-aftertouch angle |
| Guide-angle data status | Positions still open per key family | Angular values are now fixed; exact locations still need to be entered separately for `MWT`, `MST`, `QWT`, and `QST` |
| Aftertouch buffer element | `3 mm` EPDM solid round cord, about `60 Shore A` | Current first candidate for the terminal end-stop aftertouch buffer in both families |
| Buffer geometry split | `QT`: integrated into the lever geometry; `MT`: mostly housed in the raster | `MT` buffers should protrude only about `4 mm` so they do not strike too wide into the buffer |
| Buffer groove | Shallow round groove, start range `R = 4.5-5.0 mm`, `t = 1.5 mm` | Applies to the integrated `QT` lever-side buffer geometry; `MT` keeps the buffer mostly in the raster |
| Buffer retainer / contact layer | `2 mm` felt strip | Common contact layer for end stop and aftertouch onset |
| Felt state at normal key pressure | About `1 mm` compressed thickness | Defines the end of the normal playing stroke |
| Additional aftertouch reserve | About `1-1.5 mm` local cord compression | Remaining path comes from EPDM compression after the felt-defined end point |
| Geometry reference state | Full-aftertouch end position | Current layout work is now referenced to the maximum aftertouch stop rather than to the normal-travel endpoint |
| Front aftertouch reserve interpretation | Just under `2 mm` target at the key front for each key family | `MWT` is now aligned via about `11.8 mm` full front travel and about `9.8 mm` normal front travel |
| Key magnet size | Cylindrical `4 x 3 mm`, grade `N45` | Current active Hall-sensing magnet on each key |
| Hall sensor to ferromagnetic hardware clearance | `30 mm` preferred, `25 mm` minimum, centre-to-centre | Applies to steel screws, washers, frame parts, and other ferromagnetic hardware in all directions, including below the sensor; brass splints may be closer |
| Prototype material strategy | FDM first | No metal construction required in the first iteration |

What the first prototype should verify specifically:

- whether the rear zero stop gives a stable and repeatable rest height without introducing bounce
- whether the hard zero-stop rail at `Y = 285 mm` is easy enough to adjust in practice with tape/shim build-up
- whether a thin constrained solid `TPU` or `PORON` damping layer reduces noise without adding noticeable rest-height drift or hysteresis
- whether the fixed first spring set at `Y = 235 mm` gives a useful initial force spread across `MWT`, `MST`, `QWT`, and `QST`
- whether shrink-wrapped trim weights in the `255-285 mm` zone provide sufficient acoustic damping at the zero stop when weights are used
- whether the split-pin line is the correct place for the final end stop in the simplified synth branch
- whether the `3 mm` EPDM cord plus `2 mm` felt stack produces the desired compliance and noise behavior
- whether `2.5 mm` brass guide splints with key-family-specific lengths plus `18 mm` MT PTFE lining and `15 mm` QT PTFE lining avoid tip entry and edge rubbing at maximum tilt for all four key families
- how far the four package lanes actually need to diverge in `Y` and `Z`
- whether a spring line around `Y = 230-240 mm` gives the right return feel without too much force increase over the stroke
- whether an optional trim-mass pocket around `Y = 255-285 mm` is sufficient if balancing mass is needed later
- whether a single `5 g` trim weight at about `Y = 275 mm` produces a useful feel change without over-biasing the low-force action

## Preserved Technical Decisions

The following remain active independent of the mechanical branch change:

- Kassel quarter-tone layout
- one Hall sensor per key
- Teensy-based real-time scanning front-end
- USB-MIDI and 5-pin DIN in phase 1
- elastomer-based aftertouch reserve rather than FSR force sensing

## Mechanical Tasks Now Considered Closed in the Active Root

The following topics are no longer maintained in this active build guide because they belong to the archived branch:

- piano-like main-key pivot geometry around the archived long-lever proportion
- archived QT pivot package derived from the deeper action family
- MP5-based proportional reference as an active anchor

These remain available only in `docs/Archiv/SteinwayLike/`.

## Phase 1 Open Data And Prototype Questions

Data still worth collecting:

- exact Access Virus C keyboard family or the closest reliable Fatar equivalent
- representative front travel of the reference action
- key length and effective pivot distance of the reference action
- aftertouch onset position and useful reserve travel
- force impression over the main stroke and aftertouch zone
- packaging depth required for the reference category

Immediate CAD / prototype questions:

- What is the minimum viable main-key depth for the active branch?
- Can the Hall sensor sit in front of, above, or behind the pivot without creating feel penalties?
- How should `QT` keys be packaged so they remain consistent with the shallower main-key action?
- Which return-force concept best matches a Fatar-like synth feel in a custom build?

## Immediate Deliverables

- identify usable Access Virus C / Fatar reference measurements
- define first active main-key travel target
- define first active aftertouch travel target
- choose provisional pivot and sensor packaging concept for the shallow action
- derive first QT layout sketch relative to the new main-key geometry
- define first lane map for `MWT`, `MST`, `QWT`, and `QST` for split pins, buffers, and sensors
- define the first lever cross-section around a `6 mm` maximum body width and `16-18 mm` box height
- prototype the rear zero-stop, spring line, and optional trim-mass zone in FDM before any metal work

## Documentation Rule

Any new active geometry decision should be documented in this build guide before it is propagated into `docs/CAD/` or prototype steps.