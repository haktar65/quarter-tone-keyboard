# Quarter-Tone Keyboard – Build Guide

> **Status:** In preparation. This document is built up in parallel with the research and design phase.  
> Decisions from `Research.md` flow into concrete build steps here.
>
> **Update (June 2026):** The detailed geometry currently documented below represents the archived `Steinway-like` intermediate branch. It is retained as a reference snapshot while the active layout work switches to a synthesizer / semi-weighted direction with Access Virus C / Fatar feel as the new anchor.

> **Archived naming note:** `VT` is the older archive label for what the active branch now calls `QT`. This document predates the active four-family naming `MWT`, `MST`, `QWT`, `QST`.

---

## Build Phase Overview

| Phase | Content | Status |
|---|---|---|
| 1 | Finalize layout & mechanical concept | Open |
| 2 | Mock-up / Proof of Concept | Open |
| 3 | Electronics prototype | Open |
| 4 | Firmware (MIDI, velocity, controllers) | Open |
| 5 | Mechanical series production (printing + woodwork) | Open |
| 6 | Electronics final version | Open |
| 7 | Integration & housing | Open |
| 8 | Test, calibration, stage test | Open |

---

## Phase 1: Layout & Mechanical Concept

### 1.1 Layout Decision

Decided:

- Layout based on Kassel Principle (Organ St. Martin)
- Base keyboard: 61 keys (5 octaves + 1 C)
- Quarter-tone extension as a second, height-offset key structure behind the base keys

To document:
- Chosen keyboard variant with rationale
- Sketches / CAD drawings
- Octave width and key dimensions for the quarter-tone keys

### 1.2 Tools & Materials (Phase 1)

- Cardboard / foam for quick mock-up
- Calipers, angle gauge
- Optionally: first FDM test print of one octave

### 1.3 Reference Geometry Table: Normal Keyboard

This section fixes the baseline reference system for the standard keyboard geometry. Quarter-tone key geometry will be added later as a separate variant.

#### Coordinate System

- Origin `O = (0, 0, 0)`: front top edge of the white key in rest position
- `x`: lateral direction across the keyboard
- `y`: positive toward the rear of the keyboard
- `z`: positive upward
- Positive rotation `theta`: key nose moves downward in side view

#### Fixed Reference Points and Kinematics

| Item | y (mm) | z (mm) | theta (deg) | Status | Note |
|---|---:|---:|---:|---|---|
| White key front top edge, rest position (`O`) | 0.0 | 0.0 | 0.00 | Fixed | Global reference point |
| Hall sensor center on frame | <=35.0 | open | 0.00 | Partial | Must satisfy minimum 25 mm distance to guide pin at `y = 60 mm` |
| Front end-stop contact zone on frame | <=35.0 | -43.0 | 0.00 | Partial | Front felt/Kapton first-contact zone associated with the Hall sensor pocket; current first-contact level |
| PORON buffer zone on frame | 35.0-60.0 | open | 0.00 | Partial | Recessed compression zone behind the front end stop and ahead of the guide pin |
| Aftertouch hard end on frame | 35.0-60.0 | -46.0 | 0.00 | Partial | Current hard endpoint of the front aftertouch zone |
| Front guide pin on frame | 60.0 | open | 0.00 | Fixed | Preferred guide-pin position for the normal keyboard front zone |
| Main-key pivot axis | 210.0 | -24.0 | 0.00 | Fixed | User-defined baseline |
| Return spring attachment point on frame | 228.0 | open | 0.00 | Recommended | Current prototype spring concept: anchor about `18 mm` behind the main-key pivot; paired with `20 mm x 0.5 mm` spring, about `23 mm` installed length at zero position |
| Zero-position stop on frame | 280.0 | open | 0.00 | Partial | Frame-side rest stop fixed in `y`; `z` to be defined after key geometry settles |
| White key front top edge, bottom stop | 0.0 | -10.8 | 2.95 | Fixed | Pure geometric bottom-stop reference, excluding elastic compression and trapped-air effects |
| Black key front start | 51.0 | open | 0.00 | Partial | Front geometric start of the black key including air gap |
| Black key top reference plane, rest position | 53.5 | 12.0 | 0.00 | Fixed | Upper front edge shifted 2.5 mm rearward from black-key start due to front chamfer and gap |
| Black key top reference plane, bottom stop | 53.5 | 2.0 | 3.66 | Fixed | Pure geometric bottom-stop reference, excluding elastic compression and trapped-air effects |

Rotation derivation for the white-key front point:

```text
theta_white = asin(10.8 / 210) = 2.95 deg
theta_black = asin(10.0 / (210 - 53.5)) = asin(10.0 / 156.5) = 3.66 deg
```

#### Reference Rotation Angle Table

This table lists the currently fixed standard-key rotation cases. It uses the same reference points as the geometry table above.

| Key / reference point | Effective lever arm (mm) | Travel at reference point (mm) | Rotation angle (deg) | Use case |
|---|---:|---:|---:|---|
| White key, front top edge | 210.0 | 10.8 | 2.95 | Standard white-key play travel |
| White key, front top edge | 210.0 | `10.8 + 4.03 = 14.83` | `2.95 + 1.10 = 4.05` | Current white-key aftertouch construction state with front first contact at `z = -43 mm` and aftertouch hard end at `z = -46 mm` |
| Black key, top reference plane at `y = 53.5 mm` | 156.5 | 10.0 | 3.66 | Standard black-key front reference |
| Black key, top reference plane at `y = 53.5 mm` | 156.5 | `10.0 + 3.0 = 13.0` | `3.66 + 1.10 = 4.76` | Current black-key aftertouch construction state with front first contact at `z = -43 mm` and aftertouch hard end at `z = -46 mm` |

Bottom-stop values in this table are hard-geometry reference points only. Felt, PORON/elastomer compression, and any trapped-air spring effect are handled separately in the play/clearance budget.

Current front-zone aftertouch increment: from first contact at `z = -43 mm` to aftertouch hard end at `z = -46 mm`, the additional rotation is currently taken as about `1.1 deg`.

Separate CAD rule: the global normal-key design ceiling remains `theta_max = 5.0 deg` for pocket, guide-slot, and clearance dimensioning. It is not a target playing angle; it is only an upper design limit.

Front-zone order in positive `y` direction is currently fixed as: front felt end stop + Hall sensor pocket -> recessed PORON damping zone -> front guide pin.

With guide pin `y = 60 mm` and minimum guide pin to Hall sensor center distance of `25 mm`, the Hall sensor center must satisfy `y <= 35 mm`.

#### Fixed Scalar Dimensions (Normal Keyboard)

| Parameter | Value (mm) | Status | Note |
|---|---:|---|---|
| Octave width | 165.0 | Fixed | 7 white keys |
| White key width at front | 23.6 | Fixed | Head width |
| White key visible length | 150.0 | Fixed | Front section to case line |
| White key front travel | 10.8 | Fixed | Measured / standard reference |
| White key rear travel | 5.0 | Fixed | Measured |
| Black key width | 12.5 | Fixed | Base width |
| Black key visible length | 95.0 | Fixed | Standard reference used in docs |
| Black key height above white plane | 12.0 | Fixed | Rest position |
| Black key front travel | 10.0 | Fixed | Standard reference |
| Maximum rotation angle, all keys/pockets | 5.0 deg | Fixed | Global design limit for pocket and guide clearance |

#### Open Items for the Next Geometry Pass

- Exact `z` coordinate and final chosen `y` coordinate of Hall sensor center within `y <= 35 mm`
- Exact `z` coordinate and final chosen `y` coordinate of the front end-stop contact zone within `y <= 35 mm`
- Exact `z` coordinate and final chosen `y` range of the PORON buffer zone within `35 mm < y < 60 mm`
- Final guide-pin `z` coordinate and required PTFE-slot clearance at `theta_max = 5 deg`
- Exact `z` coordinate of the frame-side return spring attachment point
- Exact `z` coordinate of the frame-side zero-position stop
- Exact `z` reference location for black-key front start
- Reference point(s) for rear white-key geometry relative to the pivot
- Equivalent table for the quarter-tone keyboard variant

### 1.4 Reference Geometry Table: Quarter-Tone Keyboard

This section starts the same reference system for the VT keyboard variant. Coordinates remain referenced to the front top edge of the white key in rest position.

#### Fixed Reference Points and Kinematics

| Item | y (mm) | z (mm) | theta (deg) | Status | Note |
|---|---:|---:|---:|---|---|
| VT front top edge above whole-tone keys, rest position | 90.0 | 12.0 | 0.00 | Fixed | Front exposed VT edge in the white-key VT row |
| VT front top edge above semitone keys, rest position | 120.0 | 23.5 | 0.00 | Fixed | Front exposed VT edge in the black-key VT row |
| VT front top edge above whole-tone keys, 10 mm target hub | 90.0 | 2.0 | 3.70 | Fixed | Targeted to match the normal black-key front travel |
| VT front top edge above semitone keys, 10 mm target hub | 120.0 | 13.5 | 4.59 | Fixed | Targeted to match the normal black-key front travel; dimensioning VT case |
| VT pivot axis | 245.0 | 10.0 | 0.00 | Recommended | Preferred packaging anchor; gives clear separation from the main-key pivot and more room for the VT tail geometry |
| VT rear guide pin on frame | 290.0 | open | 0.00 | Recommended | Guide pin enters from below; about 45 mm behind the VT pivot for a more stable guidance lever arm |
| VT return spring attachment point on frame | 263.0 | open | 0.00 | Recommended | Current prototype spring concept: anchor about `18 mm` behind the VT pivot; paired with `20 mm x 0.4 mm` spring, about `25 mm` installed length at zero position |
| VT counterweight center | 305.0 | open | 0.00 | Open / to be rechecked | Previous start value; exact `y` must be rechecked after the VT aftertouch package is shifted rearward |
| VT upper buffer / aftertouch zone on frame ceiling | 370.0 | open | 0.00 | Recommended | New common VT PORON / aftertouch target, dimensioned from the semitone row for about `1:1` local-to-front travel there |
| VT rear end-stop zone on frame ceiling | 380.0 | open | 0.00 | Recommended | Harder end-stop package behind the relocated VT aftertouch zone |
| VT upper Hall sensor zone on frame ceiling | 390.0 | open | 0.00 | Recommended | Common sensor package behind the relocated rear end stop; keeps the former about `20 mm` offset behind the VT aftertouch zone |

Geometry check at recommended `VT pivot = (245, 10)`:

```text
delta_main_to_vt_y = 245 - 210 = 35 mm
delta_main_to_vt_z = 10 - (-24) = 34 mm
axis_distance = sqrt(35^2 + 34^2) = 48.8 mm

lever_whole = 245 - 90 = 155 mm
lever_semitone = 245 - 120 = 125 mm

hub_whole_at_5deg = 155 * sin(5 deg) = 13.5 mm
hub_semitone_at_5deg = 125 * sin(5 deg) = 10.9 mm

theta_whole_for_10mm = asin(10 / 155) = 3.70 deg
theta_semitone_for_10mm = asin(10 / 125) = 4.59 deg

guide_travel_at_y290_whole = (290 - 245) * sin(3.70 deg) = 2.90 mm
guide_travel_at_y290_semitone = (290 - 245) * sin(4.59 deg) = 3.60 mm

spring_travel_at_y263_whole = (263 - 245) * sin(3.70 deg) = 1.16 mm
spring_travel_at_y263_semitone = (263 - 245) * sin(4.59 deg) = 1.44 mm

buffer_travel_at_y370_whole = (370 - 245) * sin(3.70 deg) = 8.06 mm
buffer_travel_at_y370_semitone = (370 - 245) * sin(4.59 deg) = 10.00 mm

front_travel_from_3mm_buffer_whole = 3.0 * (155 / 125) = 3.72 mm
front_travel_from_3mm_buffer_semitone = 3.0 * (125 / 125) = 3.00 mm

end_stop_travel_at_y380_whole = (380 - 245) * sin(3.70 deg) = 8.70 mm
end_stop_travel_at_y380_semitone = (380 - 245) * sin(4.59 deg) = 10.80 mm

sensor_travel_at_y390_whole = (390 - 245) * sin(3.70 deg) = 9.35 mm
sensor_travel_at_y390_semitone = (390 - 245) * sin(4.59 deg) = 11.60 mm

pin_to_sensor_clearance = 390 - 290 = 100 mm
```

Implication: `VT pivot = (245, 10)` is the better first packaging anchor if the required pivot-to-pivot clearance must exceed `40 mm`. It gives about `48.8 mm` center-to-center axis spacing relative to the normal-key pivot at `(210, -24)`. The consequence is explicit: VT key geometry is now substantially different from the normal keys, with longer effective front lever arms and mirrored sensing/aftertouch moved behind the pivot on the upper frame.

Design rule for the current VT variant: both VT key types target the same `10.0 mm` front travel as the normal black keys. The resulting required rotation angles are `3.70 deg` for the VT row above whole tones and `4.59 deg` for the VT row above semitones. The global `theta_max = 5.0 deg` still provides about `0.41 deg` reserve in the dimensioning semitone VT row.

Practical guide-pin placement rule: start the VT guide pin around `y = 290 mm`. This places the guide about `45 mm` behind the VT pivot, which is a better compromise between guidance leverage and easy insertion from below than the earlier compact zone near the pivot.

Corrected VT buffer placement rule: use the VT semitone row as the dimensioning case and relocate the common VT PORON / aftertouch zone to about `y = 370 mm`. This gives about `1:1` local-to-front travel for the VT semitone row and about `1.24:1` for the VT whole-tone row, which is a much more plausible common compromise than the earlier short rear package.

With `3.0 mm` local PORON compression at `y = 370 mm`, the expected front aftertouch travel becomes about `3.00 mm` on the VT semitone row and about `3.72 mm` on the VT whole-tone row.

Practical end-stop placement rule: if the translated VT package keeps the previous about `10 mm` spacing from aftertouch zone to firmer terminal stop, place the VT harder rear end stop at about `y = 380 mm`.

Practical sensor placement rule: if the translated VT package keeps the previous about `20 mm` offset from aftertouch zone to Hall sensor center, place the common VT Hall sensor package at about `y = 390 mm`. This gives about `9.35 mm` sensor travel for the VT row above whole tones and about `11.60 mm` for the VT row above semitones, while increasing guide-pin to Hall-sensor spacing to about `100 mm`.

Practical counterweight placement rule: the earlier start value around `y = 305 mm` is no longer automatically tied to the middle of the VT rear package. Counterweight `y` must be rechecked after the translated VT aftertouch package and the resulting pivot-section geometry are fixed.

Practical return-spring placement rule: current prototype concept places the VT frame-side spring anchor around `y = 263 mm`, about `18 mm` behind the VT pivot. This keeps the spring very close to the pivot so spring force changes only weakly over the key stroke; current preferred VT spring is `20 mm x 0.4 mm` with about `25 mm` installed length at zero position.

Updated VT rear package order in positive `y`: guide pin -> felt / PORON buffer (`y ~ 370 mm`) -> rear end stop (`y ~ 380 mm`) -> Hall sensor (`y ~ 390 mm`).

The earlier assumption that the VT rear damper geometry could directly reuse the main-key felt/PORON stack is no longer accepted as a baseline. The VT aftertouch geometry must now be dimensioned from the semitone-row lever arm, while the VT pivot-section cross-section must be recalculated for the translated package.

Minimum fallback: `VT pivot = (240, 10)` still gives `45.3 mm` axis spacing and remains plausible if later CAD shows that `245 mm` is not required.

#### VT Rear Sensor / Damper Geometry Table

This table records the current recommended VT package order behind the pivot.

| Element | Longitudinal position | Thickness / level | Current decision | Function |
|---|---|---|---|---|
| VT return spring attachment point | `y = 263 mm` | open | Recommended | Frame-side spring anchor, about `18 mm` behind the VT pivot |
| VT rear guide pin | `y = 290 mm` | open | Recommended | Guidance point, inserted from below |
| VT counterweight center | `y = 305 mm` | open | Open / to be rechecked | Previous balancing-mass start value; no longer coupled to the middle of the translated VT aftertouch package |
| VT felt support / first contact layer | `y = 370 mm` | `2.0 mm` felt | Recommended | Common semitone-dimensioned VT first-contact and substrate level |
| VT PORON aftertouch layer | `y = 370 mm` | `4.0 mm` PORON, exact recess open | Recommended | Common VT aftertouch zone; target about `1:1` local-to-front travel on the VT semitone row |
| VT PORON deeper tuning option | `y = 370 mm` | recess and stack tuning open | Open | To be tuned after the translated VT package and feel target are verified |
| VT rear end-stop zone | `y = 380 mm` | harder felt / elastomer stop | Recommended | Defines the firmer terminal stop behind the relocated aftertouch zone |
| VT Hall sensor package center | `y = 390 mm` | Ceiling-mounted package | Recommended | Common analog position sensing zone behind the relocated VT end stop |
| Pin-to-sensor clearance | `290 mm` to `390 mm` | `100 mm` in `y` | Fixed by translated package | Strong magnetic clearance reserve to the steel guide pin |

#### VT Sensor Rail / Reaction Rail Split (Interim)

- Current preferred VT architecture separates the non-force sensor rail from the force-bearing reaction rail.
- Lower VT sensor rail:
	- sits directly under the keys where packaging allows
	- should be adjustable and service-friendly
	- current preferred carrier is a `20 x 20 mm` aluminium mounting profile (KLAK20 or equivalent)
	- sensor-side mounting hardware in this zone should preferably be brass or aluminium rather than steel
	- current preferred fastening concept in this zone: printed nut stones / sliding inserts for the KLAK20 slot with embedded brass nuts
	- floating / guided 3D-printed inserts may clip into this profile
- Upper VT reaction rail:
	- carries buffer, end stop, and any upper guidance load
	- must be substantially stiffer than the elastomer stack itself
	- current preferred carrier is a `16 x 16 mm` steel square profile
- Design consequence: Hall sensors no longer need to share the same structural package as the VT force path. Full travel can still be measured if the upper reaction rail is stiff and correctly referenced.

#### Sensor Environment Rules (Interim)

- Keep steel guide pins at least `25 mm` from Hall sensor centres; `30 mm` is now the preferred practical minimum where packaging allows.
- Keep Hall sensors and magnet paths away from external ferromagnetic surroundings.
- Brass is acceptable in direct sensor proximity for brackets, threaded inserts, spacers, and mounting screws; current preferred rule for the KLAK20 sensor-side mount is brass/aluminium hardware instead of steel.
- Practical current implementation: use printed KLAK20 nut stones with embedded brass nuts rather than steel T-nuts in the sensor-side mounting zone.
- Current enclosure rule: keep at least `30 mm` from Hall sensor / magnet path to the outer housing skin in zones where steel stands, brackets, or other ferromagnetic parts can approach; `40 mm` is preferred in especially exposed zones.
- Avoid placing transformers, large power supplies, loudspeaker magnets, or similar magnetic sources directly under or on the keyboard.
- The upper steel VT reaction rail is acceptable because it is mechanically useful and can be kept well separated from the Hall sensor rail.

#### Prototype Return Spring Table

This table records the current shared near-pivot spring concept for both key families.

| Key family | Spring anchor position | Distance behind pivot | Prototype spring | Installed length at zero position | Additional spring extension over full front travel |
|---|---|---:|---|---:|---|
| Main keys | `y = 228 mm` | `18 mm` | `20 mm x 0.5 mm` tension spring | `23 mm` | about `0.93 mm` |
| VT keys above whole tones | `y = 263 mm` | `18 mm` | `20 mm x 0.4 mm` tension spring | `25 mm` | about `1.16 mm` |
| VT keys above semitone keys | `y = 263 mm` | `18 mm` | `20 mm x 0.4 mm` tension spring | `25 mm` | about `1.44 mm` |

#### Open Items for the Next Geometry Pass

- Exact `z` coordinate and insertion geometry of the VT rear guide pin from below
- Exact `z` positions of the VT Hall sensor package and the felt / PORON contact region behind the VT pivot
- Frame clearances between VT tail geometry and the reinforced main-key pivot beam

---

## Phase 2: Mock-up / Proof of Concept

### 2.1 Goal

Test the playability of the layout physically. The pianist should be able to grip the mock-up and give feedback **before** complex manufacturing parts are produced.

### 2.2 Mock-up from FDM Print

*Detailed steps follow after layout decision.*

To document:
- Print parameters (material, resolution, infill)
- File paths of STL/CAD files
- Adjustments based on feedback

---

## Phase 3: Electronics Prototype

### 3.1 Bill of Materials

#### Electronics

| Component | Qty | Specification | Source | Unit price | Total |
|---|---|---|---|---|---|
| Microcontroller | 1 | Teensy 4.1 | PJRC / Mouser | ~€30 | €30 |
| System / control MCU | 1 | ESP32 module (current preferred control/calibration layer) | Mouser / AliExpress | ~€8 | €8 |
| Hall sensor | 150 | A1324LUA-T, TO-92S | AliExpress / Mouser | ~€0.36 | €54 |
| Multiplexer | 8 | CD74HC4067, 16:1 analog | Reichelt / AliExpress | ~€0.50 | €4 |
| External ADC for slow controls | 1 | MCP3204 / MCP3208 or equivalent (optional, preferred for expression inputs on second controller) | Mouser / Reichelt | ~€4 | €4 |
| Bypass capacitor | 200 | 100 nF, 0603 SMD | Reichelt | ~€0.02 | €4 |
| RC filter resistor | 10 | 1 kΩ, 0603 SMD | Reichelt | ~€0.02 | €0.20 |
| RC filter capacitor | 10 | 10 nF, 0603 SMD | Reichelt | ~€0.02 | €0.20 |
| 5-pin DIN MIDI socket | 1 | Standard DIN 41524 | Reichelt | ~€1 | €1 |
| Pitchbend potentiometer | 1 | Alps RK09D or similar | Mouser | ~€2 | €2 |
| Volume/Expression pot | 1 | Alps RK09D or similar | Mouser | ~€2 | €2 |
| Prototype PCBs | 2–3 | Stripboard 160×100 mm | Reichelt | ~€2 | €6 |
| Final PCBs | 10–12 | Octave module PCB, custom design | JLCPCB / PCBWay | ~€5/ea | €60 |

#### Mechanics

| Component | Qty | Specification | Source | Unit price | Total |
|---|---|---|---|---|---|
| Neodymium magnet | 150 | Ø4×2 mm, N45 | Supermagnete.de | ~€0.15 | €23 |
| Pivot pin | 6 | Ø4 mm steel, ~175 mm | Per meter, metal supplier | ~€1/m | €6 |
| Front guide pin | 122 | Nail drill Ø2 mm, HSS, ~28 mm | Set of 50 | ~€0.10 | €12 |
| PTFE guide tube | 1 m | Ø4/2 mm | AliExpress / Conrad | ~€2/m | €2 |
| Tension spring | 130 | Prototype set: free length about `20 mm`, body Ø about `4 mm`, wire Ø `0.4 mm` for VT and `0.5 mm` for main keys | Gutekunst Federn | ~€0.30 | €39 |
| Lead weight | 122 | ~15–20 g/key (fishing lead or similar) | Fishing supplies | ~€0.20 | €25 |
| ASA filament | ~1 kg | For key blanks FDM | Prusament / Fillamentum | ~€25/kg | €25 |
| Tough Resin | ~0.5 l | For frame modules SLA | Formlabs / Phrozen | ~€50/l | €25 |
| Flexible Resin | ~0.2 l | For elastomer stops SLA | Formlabs Elastic 50A or similar | ~€60/l | €12 |
| Piano felt strip | 2 m | 2.0 mm dense felt, adhesive-backed preferred | Piano supply / felt supplier | ~€4/m | €8 |
| PORON sheet | 1 | 4 mm polyurethane microcellular foam sheet | Keyboard mod supplier / industrial foam supplier | ~€8 | €8 |
| Kapton tape | 1 roll | 50–100 µm, electrical/mechanical sensor isolation | Electronics supplier | ~€3 | €3 |
| Contact adhesive | 1 | Rubber/foam compatible (for felt/PORON bonding) | Hardware store | ~€8 | €8 |
| Plywood 10 mm | 1 sheet | Birch BB, 1200×600 mm | Hardware store | ~€15 | €15 |
| Aluminium angle profile | 2 m | 15×15×2 mm | Metal supplier | ~€3/m | €6 |
| Adjustable aluminium profile | 2 m | KLAK20 / 20×20 mounting profile | Aluminium profile supplier | ~€6/m | €12 |
| Steel square profile | 2 m | 16×16 mm | Metal supplier | ~€4/m | €8 |
| White piano key covers | 62 | Standard size 50×23 mm | Piano parts supplier | ~€1 | €62 |

#### Total Estimate (test bench + complete keyboard)

| Category | Estimate |
|---|---|
| Electronics | ~€177 |
| Mechanics | ~€299 |
| **Total** | **~€476** |

*Prices excluding shipping. Quantities for 5 octaves + 1 C (61 base + 61 VT = 122 keys). ~20% reserve included.*

### 3.2 Schematic

*To follow.*

### 3.3 Assembly

*To follow.*

### 3.4 Main-Key Aftertouch Stack (Prototype Decision)

For the normal-tone keybed (main keys), the aftertouch stack is placed at the front key zone.

- Hall sensor is mounted in a front frame pocket (about 8 mm deep region).
- Sensor is covered with 2-layer Kapton tape (50–100 µm each).
- Mechanical load path is carried by the surrounding frame geometry, not by the sensor package.
- First contact/end-stop layer: 2.0 mm dense piano felt.
- Hall sensor pocket and front end-stop share the same front zone in `y`.
- Behind the front stop, add a second compression zone: PORON strip, 4 mm thick, recessed by 2 mm.
- PORON sits on the same 2.0 mm felt layer that is used as the front end damping layer.
- This creates a direct felt-to-PORON top transition without a step in the contact path.
- Front guide pin target position: `y = 60 mm`.
- Guide pin is placed only after this damping zone.
- Minimum guide pin to Hall sensor center distance: 25 mm.
- Derived constraint: Hall sensor center must lie at `y <= 35 mm`.
- Front-zone order in `y`: front felt end stop + Hall sensor pocket -> recessed PORON -> guide pin.

#### Main-Key Aftertouch / Damper Geometry Table

This table records the current front-zone prototype geometry for the main keys.

| Element | Longitudinal size / position | Thickness / level | Current decision | Function |
|---|---|---|---|---|
| Hall sensor pocket | Front zone, within `y <= 35 mm` | Pocket depth about 8 mm | Fixed as local sensor mount | Analog key-position sensing |
| Kapton sensor cover | Directly above Hall sensor | 2 layers, `50-100 um` each | Fixed | Electrical and mechanical isolation of the sensor face |
| Front end-stop felt | `15 mm` longitudinal contact zone in front sensor region | `2.0 mm` felt | Fixed | First tactile strike point and end damping |
| Felt support under PORON | Continues below rear compression zone | `2.0 mm` felt base | Fixed | Continuous substrate for PORON and direct material transition |
| PORON aftertouch zone | Behind front end stop, before guide pin | `4.0 mm` PORON recessed by `2.0 mm` | Fixed | Controlled aftertouch compression after first stop |
| PORON top level | Same rear zone as above | Flush with felt top because of `2.0 mm` recess over `2.0 mm` felt base | Fixed | Step-free transition from first stop into aftertouch zone |
| Front guide pin | `y = 60 mm` target | open | Fixed in `y` | Guidance after sensor and damping zones |
| Sensor-to-guide clearance | Hall sensor center to guide pin | minimum `25 mm` | Fixed | Magnetic and packaging clearance |

Target feel:

- Clear tactile strike point at first felt contact.
- Additional controlled aftertouch travel of about 2 mm to hard endpoint.

### 3.5 Interim Result (May 2026): VT Mechanics, Pivot Geometry, and Guidance

This section captures the current interim design state from recent geometry and mechanics discussions.

#### Main/VT Pivot Architecture (Interim)

- Main-key pivot target geometry follows piano-like proportions:
	- pivot axis about 24 mm below key top surface
	- pivot position about 210 mm behind the front edge
- Main-key pivot region may use a local Tough Resin bearing bushing with about `5 mm` wall thickness where the shaft geometry needs more material and larger radii.
- Main keys are expected to move downward in the rear section to create vertical space for VT mechanics.
- VT pivot should not be placed directly above main-key pivot (stack height and collision risk become too high).
- Current VT key-body assumption: the VT lever can remain around `13 x 20 mm` in the main load-bearing zone, but may grow locally to about `22 mm` total height at the VT pivot region to provide more material for the bearing block and smooth transitions.
- Current support split:
	- main-key pivot: simpler mounted/on-top support is preferred
	- VT pivot: custom hybrid support is preferred only here, because the VT pivot region is the actual packaging bottleneck
- Current VT pivot support stack, from top to bottom:
	- Tough Resin bearing geometry
	- Tough Resin bearing bushing / local shaft insert in the VT pivot block
	- FDM coupling structure
	- aluminium U-profile
	- wood spacer strip
	- steel strap as lower stiffening belt
- Updated structural direction for the pivot carrier: a directly coupled lower square tube is acceptable and currently preferred over a larger spaced secondary frame, provided the whole assembly works as one stiff pivot frame.
- Current preferred practical frame concept:
	- aluminium U-profile carries the exchangeable Tough Resin shaft holders / fins
	- a steel square tube may sit directly below the aluminium profile as the main lower stiffener
	- both members should be screwed/clamped so they act as one structural pivot frame, not as two loosely coupled rails
- Return-spring load-path rule: spring reaction forces must be introduced into the same structural pivot frame that carries the pivot shafts.
- Do not anchor the springs against a decoupled auxiliary frame, because any relative compliance between spring frame and pivot frame would change the effective key feel and unnecessarily load the chassis.
- Consequence for detailed design: spring anchors may sit on the lower square tube only if that square tube is rigidly coupled to the pivot carrier and therefore belongs to the same structural frame reference.
- Anti-slip / service rule for the exchangeable Tough Resin holders: use geometric interlock into the aluminium U-profile (for example about `2 mm` penetration plus serration / tooth pattern against longitudinal slip), but avoid permanent bonding so worn holders remain replaceable.

#### Required CAD Method (TurboCAD)

- Build two envelope studies before final key solids:
	- side-view volume envelope (all end positions, collisions, support clearances)
	- top-view volume envelope (key spacing, supports, side clearances)
- Reserve support space at pivot blocks: **5 mm per side per octave**.
- Final key geometry is the intersection of side/top envelopes.

#### Guidance Strategy (Interim)

- Primary guidance concept: **central guide rib (Kimme)** in key/tas pocket pair.
- Side spacers at pivot are downgraded to secondary/backup role.
- With around 1.0 mm key-to-key gap, dedicated inter-key spacers are not practical.
- Nominal spacing targets:
	- visible key gap: ~1.0 mm
	- complex motion clearances near pivots/turning zones: 1.5-2.0 mm

#### Bearing/Contact Pairing (Interim)

- Guide noses around the 4 mm brass shaft are planned in **Tough Resin**.
- Current geometry target for the guide nose is about `3 mm` height and `3 mm` thickness, with generous radii so the local resin detail is not left as a thin sharp fin.
- VT pivot block should use a dedicated **Tough Resin bearing bushing** so the precise local shaft geometry is carried by a replaceable SLA insert rather than by the full FDM key body.
- Same design rule can also be used for the main-key pivot when local geometry benefits from a dedicated resin insert; current target wall thickness for these pivot bushings is about `5 mm`.
- Key-side bearing seat in ASA is planned as a non-binding contact arc (~160 deg seat geometry).
- Brass shaft must not be clamped under resin preload.
- Slots/grooves for shaft guidance should allow slight movement; target condition is “just freely rotatable shaft.”
- The bearing bushing is a geometry carrier only, not a preload element; the shaft must remain freely rotatable after full assembly.
- Practical fit rule for the Tough Resin bushing on the `4.0 mm` brass shaft: do not aim for line-to-line fit. Start with about `0.06-0.12 mm` diametral running clearance (roughly `4.06-4.12 mm` finished bore), then trim by test print / reaming if the actual resin process runs tighter or looser.

#### Tribology and Wear Philosophy

- Avoid ASA-on-ASA as primary sliding pair in critical guidance.
- Preferred pairing: ASA contact region against brass shaft, lubricated with a thin Silbergleit film.
- Keep lubrication minimal; no paste buildup in pockets.

#### Manufacturing Consequence

- Keys may be split into sub-parts for load-path-oriented print orientation and stronger joints.
- This is preferred over one-piece support-heavy prints when structural anisotropy would weaken pivot regions.

#### Next Verification Steps

- Check four collision end states in CAD (main up/down, VT up/down).
- Verify free shaft rotation after assembly (empty and fully built).
- Validate no hard rubbing in complex turning regions under full travel.

---

## Phase 4: Firmware

### 4.1 Development Environment

Decided: VS Code + PlatformIO (Teensy 4.1 / Teensyduino).

### 4.2 MIDI Protocol

Decided: 24-tone mapping, no MPE. See `Research.md` Section 3.

### 4.3 Velocity Algorithm

Basic principle with continuous Hall sensor:
```
t1 = time when signal crosses upper threshold (key moving)
t2 = time when signal crosses lower threshold (key struck)
dt = t2 - t1
velocity = f(1 / dt)   // inverse: small dt = hard strike
```
Calibration: mapping dt → MIDI Velocity (0–127) via lookup table or curve fitting.

### 4.4 Scan Loop

Requirements:
- Scan cycle time < 1 ms (for timing accuracy ≥ ±0.5 ms → velocity error < 5%)
- Timer-driven polling; no interrupt required for Hall sensors (analog level polling)

### 4.5 Multi-Processor Architecture (Current Preferred Direction)

- **Teensy 4.1** remains the real-time sensor front-end.
	- scans all Hall channels
	- calculates velocity and aftertouch-relevant real-time events
	- applies stored calibration locally
	- should stay independent from high-level protocol and UI load
- **ESP32** is the currently preferred system / control processor.
	- reads expressions, pedals, wheels, buttons, and other slow controls
	- orchestrates calibration sequences
	- can already emit standalone MIDI / MPE if the Raspberry Pi layer is omitted
	- stores and manages system settings
- **Raspberry Pi** becomes an optional higher-level back-end.
	- MIDI / MPE / OSC translation
	- optional SuperCollider host and audio engine
	- optional DAW-independent instrument stage

### 4.6 Internal Communication Split (Interim)

- Current preferred logical split:
	- Teensy -> ESP32 push-style event/data stream over UART
	- ESP32 -> Teensy control/calibration path may use SPI or an equivalent dedicated command channel
- Architectural rule: Teensy must remain autonomous in the scan loop and must not depend on polling by the ESP32.
- Parameter updates from the control side should become active only at safe synchronization points.

### 4.7 Slow Controllers / Expressions (Interim)

- `2-4` expression / pedal / wheel channels are currently expected.
- Preferred approach: measure them on the second controller, not on the Teensy real-time front-end.
- Best-quality path: second controller plus dedicated external ADC.
- Practical recommendation for the first stable build:
	- ESP32 for logic / control
	- external ADC such as `MCP3204` / `MCP3208` for expression channels
	- `10 kOhm` linear pots / pedals as preferred source impedance
	- RC filtering and software calibration / hysteresis on the control side

---

## Phase 5: Mechanical Series Production

### 5.1 Keys

*Follows after mock-up sign-off.*

- FDM print: Polymaker PolyLite ASA, printed upright
- Post-processing: sanding of bearing surfaces, press-fit inserts for lead weights
- SLA: frame modules, bearing blocks, aftertouch buffers

### 5.2 Keyboard Frame

*To follow.*

- Aluminium square tube 10×10×1 mm as structural member
- ASA node connectors with internal knurling, M4 heat-set inserts, epoxy bond
- Half-octave SLA Tough Resin modules with integral pivot web and partition walls

### 5.3 Print Files

*Paths to STL/STEP files will be linked here once available.*

---

## Phase 6: Electronics Final Version

*Follows after prototype validation.*

- PCB layout (KiCad or similar)
- Assembly drawing
- Manufacturing files

---

## Phase 7: Integration & Housing

### 7.1 Housing Concept

- Wooden corpus, stage-suitable
- Dimensions: width per key count, depth ≤ 350 mm, height ≤ 120 mm
- Control panel: pitchbend wheel, volume slider, optional octave-shift buttons
- Connectors: USB-C, 5-pin DIN MIDI Out, optional pedal socket (sustain)

### 7.2 Surface & Appearance

*To be discussed with the pianist.*

#### Post-Prototype Surface Strategy (Future Decision)

This is intentionally not part of the first prototype build. It records the current preferred direction for a later, more finished instrument state.

- VT key levers: ASA structural bodies, currently dimensioned around `13 x 20 mm` box section in the main load-bearing region, with lower front height where geometry permits.
- Functional guide / pivot inserts: SLA Tough Resin remains preferred for locally stressed bearing and guide details.
- Visible playing surfaces: ABS-like SLA resin remains acceptable as a later finish material because tactile feel is good and expected functional service life is likely much longer than purely cosmetic life.
- Current assumption for playing surfaces: optical ageing (gloss, yellowing, wear marks) is expected earlier than play-impairing failure; service life before functionally relevant replacement is expected to be in the `>15 years` range if the resin surface is well supported by the ASA substrate and does not carry the primary structural bending load.

#### Future Bonding Strategy for Playing Surfaces

- Later, finished instruments may use full-surface bonding of SLA playing surfaces to the ASA key body with a high-strength epoxy such as `UHU Endfest`.
- Do not rely on the adhesive to define alignment. The ASA carrier should still provide geometric seating and full-area support.
- Prepare both bonding faces by sanding and degreasing before bonding.
- Keep a thin continuous adhesive layer; do not squeeze the joint dry.
- UV protective clear coat is currently not planned for the actual playing surfaces, because finger abrasion would likely make the visual result worse before it provides meaningful lifetime benefit.

#### Prototype Boundary

- The first prototype does not need removable surface parts.
- The first prototype does not need final visual surface finishing.
- The notes above are kept only as a documented later-stage option.

---

## Phase 8: Test & Calibration

*To follow.*

- Guided service calibration per key should use three points:
	- `0` = rest position
	- `pressed` = user-defined weighted press point
	- `aftertouch` = defined aftertouch / end-zone point
- ESP32 should guide and store the calibration process; Teensy should measure and maintain the low-level sensor model.
- Optional slow zero-drift correction in true rest state is acceptable.
- Full in-play re-learning of `pressed` and `aftertouch` points is currently not desired.
- Velocity calibration: comparison with reference keyboard
- Latency measurement (target: < 5 ms)
- Stage test: stage suitability, handling, transport
