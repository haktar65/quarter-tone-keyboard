# Quarter-Tone Keyboard (QTKB) – Build Guide

This is the active build guide for the synth / semi-weighted workstream and the single active technical source for geometry, prototype rules, and build decisions.

Public shorthand for GitHub-facing material: `QTKB`.

The previously documented piano-like intermediate branch is no longer active and is preserved under `docs/archive/SteinwayLike/`.

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

- CAD source of truth for detailed layout values: `docs/CAD/Design/MasterLayout.csv`
- `MT` octave width at the white-key front: `165.2 mm`
- `MWT` head width: `22.6 mm`
- `MWT` air gap to neighboring key: `1.0 mm` in `X` and `Y`
- `MWT` effective white-key pitch at front: `23.6 mm`
- `MWT` head length: `50.0 mm`
- `MWT` lip length: `2.0 mm`
- `MWT` lip height: `2.0 mm`
- `MWT` tail length: `35.0 mm`
- `MWT` body height: `14.0 mm`
- `MST` black key width: `12.5 mm`
- `MWT` and `QWT` rear-tail raster: equidistant within `C-E` at `13.6 mm` and independently equidistant within `F-B` at `12.475 mm`; the `E/F` transition is intentionally discontinuous
- Pivot layout: retain an equidistant pivot raster for the first printed layout check; correct any required local offset with separately printed levers or, preferably, replaceable SLA bearing inserts.
- `MST` start position: `Y = 51.0 mm`
- `MST` visible length: `64.0 mm`
- `MST` black key height above white: `12.0 mm`
- `MST` body height: `10.0 mm`
- `MST` top slope: `1.0 deg`
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

- global origin: `O = (0, 0, 0)` at the front-left top corner of the lowest `MWT` key at rest
- `X` points rightward toward higher notes
- `Y` points rearward from the player
- `Z` points upward; the resting `MWT` key-top surface is the reference plane `Z = 0`

Active geometry rules:

- use main-key pivot baseline `Y = 210 mm`, `Z = -12 mm`
- `QT` keys are short secondary levers on the shared main pivot axis, not on a separate `QT` pivot axis
- do not silently revive archived defaults such as `Y = 210 mm`, `Z = -24 mm` or the earlier two-axis proposal `MT = (195, -12)`, `QT = (235, 6)`
- treat splint, buffer, and sensor as one compact reaction group per key family while keeping the four family lanes `MWT`, `MST`, `QWT`, and `QST` separate from each other
- keep aftertouch inside the core travel design from the beginning

Active support and stop architecture:

- use pins for lateral guidance and anti-twist control
- use a simple laid-in pivot axle with spacer washers as the current key-spacing baseline
- the pivot axis is now a concrete, print-oriented CAD model at `docs/CAD/_Design/PivotAxis.FCStd`; its detailed geometry is exported in `docs/CAD/_Design/PivotAxis/PivotAxis.csv`
- treat the current pivot-holder wrap as provisional; first-print feedback suggests the present lever-direction capture is too small, so a roughly `180 deg` axle wrap should be tested as the next prototype candidate
- reduce the local lever-side support land in the pivot washer zone to `5 mm` where needed to clear the spacer-washer package inside the available `6.84 mm` width; treat this as an active prototype assumption, not yet as a fully validated final dimension
- allow the axle and spacer stack to be bonded into a removable holder cradle with `UHU Endfest`
- use replaceable Tough Resin bearing inserts rather than making the structural frame the wear part
- use Tough Resin for the local washer-contact region in the current prototype direction
- keep only the rear zero stop behind the pivot; the terminal end stop stays on the split-pin / guide line
- the rear zero stop is now a concrete, print-oriented CAD model at `docs/CAD/_Design/ZeroStop.FCStd`; its active global references are `ZStopCenterY = 285 mm` and `ZStopTopZ = -12 mm` in `docs/CAD/Master/Globals.csv`
- preserve the tail volume behind the pivot for zero-stop packaging, spring hardware, and optional trim mass

Active packaging rules:

- `6 mm` maximum lever body within a `6.8 mm` per-key lane
- `16-18 mm` first-pass box height over most of the hidden lever body
- `20-22 mm` local build-up around pivot, spring eye, guide-bushing pocket, and optional weight pocket
- prototype the lever, cradle, stop, and support geometry in `FDM` first before introducing metal construction

K20 support-frame height:

- `K20FrameZ = -32 mm` is the common nominal global `Z` height for the K20 profiles supporting both the pivot axis and rear zero stop.
- The local `PivotAxis.csv` value `K20Z = -20 mm` is the offset from the pivot's local origin at `PivotAxisZ = -12 mm`; it therefore resolves to the same global height, `Z = -32 mm`.
- Pivot and zero-stop supports remain separately vertically adjustable around this nominal value. Further K20 profiles may use `K20FrameZ` when the supports are connected into a common frame.

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
| Pivot support land in washer zone | `5 mm` provisional | Local reduction to clear the spacer-washer package inside the available `6.84 mm` width; validate stiffness in prototype first |
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
| Guide kinematic rule | Radially matched splint and PTFE tube about the shared pivot axis | Replaces the provisional straight half-angle guide. Each part follows the same nominal circular centreline in its local `YZ` plane. |
| Guide splint material and diameter | Brass, `2.5 mm` | Active guide-pin baseline. Bend on a radius-specific jig; do not use visual or hand-estimated corrective bends. |
| PTFE guide tube | `4 mm` OD, `3 mm` ID | Gives `0.25 mm` radial clearance to the splint. Validate low friction and lateral play on the prototype. |
| Guide tube length | `>30 mm` continuous radial engagement | Replace the `18 mm` MT / `15 mm` QT provisional liners. Determine final length from full-stroke overlap plus end reserve. |
| Splint overlap | Continuous through normal travel and full aftertouch, with `3-5 mm` reserve at each limiting position | The splint end may enter the tube but must not leave it within the mechanical operating range. |
| Splint end treatment | Rounded and polished; tube entry lightly chamfered | Required because the free splint end enters the PTFE tube during part of the stroke. |
| Guide bushing block format | Adapt to the radial tube path | The previous `4 x 6 x 32 mm` straight-bushing package is superseded; retain side-wall and local reinforcement checks, especially for `QWT` and `QST`. |
| Bending-jig correction | Empirically measured per brass stock and radius family | CAD defines the functional centreline radius. Reduce the forming-jig radius only by the measured springback correction; use `10-20 %` reduction solely as an initial sample range. |
| PTFE retention concept | Pocket plus adhesive | PTFE liner should sit in a form-locking pocket; roughen the outer PTFE surface first and use cyanoacrylate only as position-locking support, not as the primary structural element |
| Guide tube retention and end clearance | Form-locking radial pocket plus adhesive; free clearance only beyond the hard stops | The tube must not terminate in an intentionally unguided region during normal travel or aftertouch. |
| Guide-bushing governing case | `QWT` and `QST` | `MT` keys still have more surrounding material at the splint location; the narrow `QT` keys are the actual strength and packaging limit case |
| QT bushing-side wall condition | About `1 mm` per side at `6 mm` key width | Acceptable for the first prototype if the bushing zone is locally reinforced in `Z` and all pocket transitions keep generous radii |
| Full-aftertouch reference angles | `MWT 3.2 deg`, `MST 4.3 deg`, `QWT 5.6 deg`, `QST 7.2 deg` | Fixed user values for the geometric layout at the maximum aftertouch stop |
| Guide-radius data status | Positions and nominal radii remain to be entered per key family | Calculate each centreline radius from the shared pivot to its guide reference point; preserve the same radius for splint and tube. |
| Aftertouch buffer element | `3 mm` EPDM solid round cord, about `60 Shore A` | Current first candidate for the terminal end-stop aftertouch buffer in both families |
| Buffer geometry split | `QT`: integrated into the lever geometry; `MT`: mostly housed in the raster | `MT` buffers should protrude only about `4 mm` so they do not strike too wide into the buffer |
| Buffer groove | Shallow round groove, start range `R = 4.5-5.0 mm`, `t = 1.5 mm` | Applies to the integrated `QT` lever-side buffer geometry; `MT` keeps the buffer mostly in the raster |
| Buffer retainer / contact layer | `2 mm` felt strip | Common contact layer for end stop and aftertouch onset |
| Felt state at normal key pressure | About `1 mm` compressed thickness | Defines the end of the normal playing stroke |
| Additional aftertouch reserve | About `1-1.5 mm` local cord compression | Remaining path comes from EPDM compression after the felt-defined end point |
| Reaction-group orientation at full aftertouch | Horizontal in global `XY` | The fixed reaction surface is horizontal; its normal and the intended resultant reaction force are in global `Z`. |
| Key-side stamp contact face | Horizontal at full aftertouch | Angle the key-side contact face relative to the key-top surface as required so it becomes horizontal in the full-aftertouch reference state. |
| Felt shear from normal to full aftertouch | About `0.10 mm` `MWT`, `0.12 mm` `MST`, `0.16-0.36 mm` `QWT`, `0.21-0.40 mm` `QST` | Small, controlled tangential motion in the felt layer; keep the contact face smooth and free of layer steps, seams, and sharp edges. |
| Contact-area rule | Narrow, continuous, and lightly radiused | Do not use a broad rigid clamping surface. The defined contact zone limits felt wear and permits the small angular adjustment. |
| FDM stamp print orientation | Upright, contact face horizontal and uppermost | The vertical aftertouch load acts mainly in compression through the layer stack. Use a closed, adequately thick top skin, place no support on the contact face, and orient its finishing lines along the expected felt movement when the slicer permits. |
| Geometry reference state | Full-aftertouch end position | Current layout work is now referenced to the maximum aftertouch stop rather than to the normal-travel endpoint |
| Front aftertouch reserve interpretation | Just under `2 mm` target at the key front for each key family | `MWT` is now aligned via about `11.8 mm` full front travel and about `9.8 mm` normal front travel |
| Hall sensor | `Allegro A1324LUA-T`, linear ratiometric analog, `TO-92S` | One sensor per key; continuous position signal supports velocity threshold timing and aftertouch evaluation |
| Key magnet size | Cylindrical `4 x 3 mm`, grade `N45` | Current active Hall-sensing magnet on each key |
| Hall sensor / magnet positioning | Stable local mount and per-key calibration required | The relevant tolerance is the relative position of each sensor and its own magnet; individual rest and full-travel calibration absorbs repeatable key-to-key offsets |
| Hall crosstalk prototype result | No practically visible response at `10 mm` lateral `X` magnet offset in the tested setup | Treat adjacent-magnet crosstalk as negligible for the current geometry, pending confirmation with the final sensor, magnet, and lever placement |
| Hall operating span | About `8 mm` observed useful own-magnet distance range | Current exploratory setup approaches a low calibrated signal near the far end and retains a responsive signal near the close end; verify the final full-aftertouch position remains below output saturation |
| Ferromagnetic hardware | Prefer brass or aluminium inside the local sensor / magnet zone | A steel part can redirect the own-magnet field and is not equivalent to a laterally offset neighbor magnet; retain the current `25-30 mm` rule for unverified steel hardware and validate unavoidable closer parts with an ADC comparison test |
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
- whether the horizontal full-aftertouch reaction surfaces keep guide and pivot drag below perception while the felt accommodates the expected sub-`0.5 mm` tangential displacement
- whether the upright-printed FDM stamp retains a smooth, step-free contact face and shows no layer separation or accelerated felt wear under repeated full-aftertouch loading
- whether `2.5 mm` brass splints and `4 x 3 mm` PTFE tubes on matched pivot radii remain low-friction, laterally controlled, and continuously engaged through normal travel and full aftertouch for all four key families
- measure brass springback for the selected stock with short samples around the critical radius families before making production-length splints; verify that the forming jig creates neither kinks nor out-of-plane error
- whether increasing the pivot-holder wrap toward about `180 deg` gives enough stiffness in lever direction without creating assembly or friction problems with the washer-retained axle concept
- whether the locally reduced `5 mm` pivot support land in the washer zone remains stiff enough in lever direction when executed in Tough Resin
- how far the four package lanes actually need to diverge in `Y` and `Z`
- confirm the `10 mm` lateral magnet-offset crosstalk result with the final sensor, magnet, and lever arrangement, including one resting key while its nearest neighbor is at full travel
- compare the raw ADC curve with and without any steel part that must remain inside the `25-30 mm` local sensor / magnet clearance zone
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

These remain available only in `docs/archive/SteinwayLike/`.

## CAD Repository Structure And Link Rules

The CAD repository is organized by document role rather than by a prematurely fixed manufacturing process. A primary `.FCStd` document is kept directly in its role directory. Its exports, previews, spreadsheets, and other supporting data are kept in a same-named subdirectory.

Target structure:

```text
docs/CAD/
├─ Master.FCStd
├─ Master/
│  └─ global spreadsheet exports, reference data, and previews
├─ Design/
│  ├─ Keys.FCStd
│  ├─ Keys/
│  │  ├─ MasterLayout.csv
│  │  └─ KeysPreview.FCStd
│  ├─ PivotYZ.FCStd
│  ├─ LeverEnvelope.FCStd
│  ├─ ReactionGroupYZ.FCStd
│  └─ Controls.FCStd
├─ Assemblies/
│  ├─ QTKB_Current.FCStd
│  ├─ QTKB_OneOctave.FCStd
│  └─ Production/
├─ BuildParts/
├─ BoughtParts/
└─ STPs/
```

Role definitions:

- `Master.FCStd` holds global, technology-independent reference geometry and scalar parameters. Its spreadsheet must not contain references to bodies, features, or assemblies.
- `Design/` holds functional design documents. `PivotYZ.FCStd` is the first YZ-space study for the pivot, lever bearing, and rear zero stop; it is not yet a released part.
- A same-named data directory belongs to its primary document. For example, `Design/Keys/MasterLayout.csv` is the data export for `Design/Keys.FCStd`; `KeysPreview.FCStd` remains with the key-design data because it is not a system-level assembly.
- `Assemblies/` holds linked system views, collision and packaging checks, and later production assemblies. `QTKB_Current.FCStd` is the current visible system state, not an authoring source for upstream geometry.
- `BuildParts/` holds concrete part documents without separating them by process or maturity. Manufacturing method, material, quantity, and revision are assigned later by a production assembly rather than by moving the master part document.
- `BoughtParts/` holds CAD representations of purchased components needed for placement, clearance, and assembly checks.
- `STPs/` holds neutral exchange and fabrication exports only; it does not become a second editable source for a part.

FreeCAD dependency rules:

- allowed dependency direction: `Master -> Design -> BuildParts -> Assemblies`
- `Master.FCStd` must not reference `Design`, `BuildParts`, or `Assemblies`
- assemblies may reference upstream documents but must not reconfigure their source spreadsheets through Tracking Links
- global spreadsheets carry scalar data only; family-local spreadsheets may contain links only to objects within the same family document
- after a document has external links, avoid moving or renaming it; create a named design study for alternatives instead

## CAD Naming Conventions

Names identify the owning domain and role rather than relying on generic labels such as `Spreadsheet`, `Body001`, or `MasterLayout` outside its key-layout context. Once a name is used by an external link or an expression, keep that name stable.

- primary document: `<Domain>.FCStd`, for example `Master.FCStd`, `Keys.FCStd`, `PivotYZ.FCStd`, and `Controls.FCStd`
- supporting-data directory: `<DocumentName>/`, for example `Keys/` for `Keys.FCStd` and `Master/` for `Master.FCStd`; it holds exports, previews, and document-local data
- preview document: `<Domain>Preview.FCStd`, for example `KeysPreview.FCStd`; a preview remains with the supporting data of its design document unless it becomes a multi-document system assembly
- system assembly: `QTKB_<Scope>.FCStd`, for example `QTKB_Current.FCStd` and `QTKB_OneOctave.FCStd`
- design study: `<Domain>_<Purpose>.FCStd`, for example `PivotYZ.FCStd`, `LeverEnvelope.FCStd`, and `ReactionGroupYZ.FCStd`
- document names carry no object-type prefix; use CamelCase descriptive names, for example `PivotZeroStopYZ.FCStd`, `Keys.FCStd`, and `Master.FCStd`
- FreeCAD Part object: `p<Name>`, for example `pPivotReference` and `pZeroStopReference`
- FreeCAD Part container: `pc<Name>`, for example `pcPivotZeroStopYZ`; use `pc` rather than `p` where the object exists primarily to group child objects
- FreeCAD Body object: `b<Name>`, for example `bMWT`, `bMST`, `bQWT`, `bQST`, and `bPivotCradle`; do not rely on automatically assigned names such as `Body001`
- FreeCAD Sketch object: `s<Name>`, for example `sPivotAxisYZ`, `sZeroStopYZ`, and `sLeverEnvelopeYZ`
- FreeCAD Spreadsheet object: `t<Name>`, for example `tMasterGlobals`, `tKeysLayout`, `tKeysMWT`, `tKeysMST`, `tKeysQWT`, and `tKeysQST`
- FreeCAD Link object: `l<Name>`, for example `lMWT`, `lPivotAxisYZ`, and `lZeroStopReference`
- parameter alias: use the shortest unambiguous technical name, for example `OctaveWidth`, `PivotX`, `PivotY`, `PivotZ`, `MWT_HeadWidth`, and `QWT_StartY`
- add a family, domain, or role prefix only when it distinguishes otherwise ambiguous values. Do not add a prefix merely because the value is part of a spreadsheet; for example, prefer `PivotY` to `Coord_PivotY`.
- use `X`, `Y`, and `Z` only as coordinate suffixes. Keep units in the property type or spreadsheet cell; do not encode units in names.
- use `Master` only for the owner-level integration table or document. A domain-specific key-layout table is `tKeysLayout`; do not call it merely `MasterLayout`.

Spreadsheet scope rule:

- `tMasterGlobals` grows only when a scalar is a system reference or is needed by more than one independent design document.
- a downstream spreadsheet receives a master scalar through a local expression, for example `tKeysLayout.PivotY = tMasterGlobals.PivotY`.
- local formulas and bodies reference that local alias, for example `tKeysLayout.PivotY`, rather than repeatedly reaching into `tMasterGlobals`.
- this local alias is an expression-backed interface, not a copied numerical value.

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
- How much pivot-axle wrap is actually needed for sufficient lever-direction stiffness, and is a roughly `180 deg` capture practical with the current washer-retained axle stack?
- Is the local `5 mm` support land at the pivot washer zone sufficient once the local load-bearing region is switched to Tough Resin?

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

`MasterLayout.csv` and later equivalent CAD exports are authoritative for detailed parameterized geometry. This build guide records the active design decisions and the values needed to interpret or build from that geometry. Update both in the same workstream when an active decision changes.