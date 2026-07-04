# Quarter-Tone Keyboard – Research & Concept

> **Update (June 2026):** The previously explored piano-like geometry branch is now archived as a `Steinway-like` reference snapshot in `SteinwayLikeArchive.md`. The active workstream switches to a synthesizer / semi-weighted layout direction with Access Virus C as the primary feel reference and Fatar keyboard feel as the family anchor.

> **Archived naming note:** `VT` is the older archive label for what the active branch now groups under `QT`. This archive generally distinguishes `main keys` and `VT keys`, not the active four-family set `MWT`, `MST`, `QWT`, `QST`.

## Project Goal

Build a high-quality, stage-ready quarter-tone keyboard as a MIDI input device for a professional jazz pianist. Requirements:

- Quarter-tone grid (24 tones per octave)
- High-quality, demanding playability (level: Gaspard de la Nuit)
- Impressionistic playing style, improvisation, original compositions
- Stage-ready: Pitchbend, volume control, optional further modulation controllers
- Phase 1: MIDI input device (USB-MIDI and 5-pin DIN)
- Manufacturing: FDM/SLA printing, woodworking, custom electronics/firmware

### 0.1 Requirements from the Pianist's Perspective

These requirements are critical for all mechanical decisions and take priority over manufacturing convenience.

#### Must Criteria

- Professional appearance in look, feel and playing response
- Standard piano technique must not be compromised; the keyboard must be playable from classical technique
- White keys receive original piano key covers as the primary visual and tactile surface
- Black keys receive a high-quality top layer; intended: ABS-like Tough Resin
- Quarter-tone keys must be reliably distinguishable by touch, without looking cheap or provisional
- Consistent, reproducible key action across the entire keyboard

#### Should Criteria

- Quarter-tone keys receive deliberate haptic differentiation from the main keys
- FDM surfaces can be intentionally used as a tactile feature, provided the result is controlled, pleasant, and high-quality
- The keyboard should feel like a serious instrument rather than a controller prototype
- A high-quality synth / semi-weighted action with integrated aftertouch is now preferred over a hammer-action category
- Target playing feel: clearly closer to a high-quality synthesizer keyboard than to weighted stage or piano action
- Reference: Access Virus C with Fatar keyboard feel as the primary direction anchor

#### Not Acceptable

- Stub-key solutions at the expense of pianistic ergonomics
- Visibly improvised surfaces at primary contact points
- Inconsistent friction, lateral wobble, or strongly varying key moments
- Quarter-tone keys that are only visually distinguishable but cannot be reliably identified by touch

#### Immediate Mechanical Consequences

- Pivot point, key mass, and counterweights must not be chosen primarily for packaging or sensor placement, but for playing feel
- Key surfaces are part of the function, not merely cosmetic
- Quarter-tone keys need a defined tactile identity; treating all keys the same is not necessarily optimal here
- The previously explored piano-like / `Steinway-like` branch is archived and no longer defines the active target mechanism
- Simple unweighted levers are acceptable only as an early functional prototype, not as the target mechanism; the active target remains controlled synth / semi-weighted action

### 0.2 Mechanical Target Range

#### Target Playing Feel (updated May 2026)

- Category: **Synthesizer / Semi-Weighted** – not stage piano or hammer action
- Reference: Access Virus C as the preferred feel target; Fatar keyboard feel as the relevant action family
- Hammer action excluded: too heavy, too deep, wrong category for this instrument
- Target: consistent semi-weighted feel across all 122 keys; quarter-tone keys intentionally lighter but controlled

Weight estimate for 122 keys semi-weighted: ~4–7 kg for key mechanism alone. Significantly lighter than a hammer action variant.

#### Implications

- Not a pure geometry solution, but a controlled mass and lever mechanism
- Front weight, return force, and friction level must be deliberately calibrated
- The quarter-tone mechanism must not significantly degrade the feel of the main keys

#### Architecture Option: Donor Mechanism Based on Fatar

A seriously considered option was purchasing two weighted Fatar keyboards as mechanical donors.

Advantages:
- Defined, musically usable base mechanism
- Existing weights, bearings, and key kinematics
- Significantly lower risk in achieving professional playing feel

Disadvantages:
- Substantial modification work required for the Kassel quarter-tone layout
- Donor mechanism designed for 12-tone geometry, not for a second and third key plane
- Integration of quarter-tone keys behind the pivot remains a custom design regardless
- Geometric degrees of freedom may be constrained by the donor mechanism

**Decision (May 2026): Full custom build**

Purchasing a ready-made keybed was evaluated and rejected. Reasons:
- White key tails occupy exactly the space needed for Keybed 2 and VT actuation
- Any deviation from original geometry requires deep intervention in a design not intended for it
- With the Hall sensor concept (see Section 4.2), custom sensing is simpler than reverse-engineering a keybed
- Custom build gives full freedom in pivot position, lever geometry, weighting, and cutouts

Next step: test bench with a single key (main key + VT key) before any further purchases.

---

## 1. Concept: Keyboard Layout

### 1.1 Core Problem

A quarter-tone keyboard must make 24 tones per octave accessible – twice as many as a standard keyboard. Several established layout approaches exist.

### 1.2 Decided Layout: Kassel Principle (Organ St. Martin, Kassel)

**Reference:** New organ of the Martinskirche Kassel – single-manual quarter-tone keyboard with an extended black-key principle.

#### Principle: Two rows of raised keys behind each standard key row

The octave is organized into **three depth planes** and **three height planes**:

| Key type | Position (depth) | Height | Pitch step |
|---|---|---|---|
| White keys | front | base plane (0) | C D E F G A B |
| Black keys (1st row) | middle | +12 mm (standard) | C# D# F# G# A# |
| Whole steps +¼ | behind white keys | +12 mm (= black key height) | C↑ D↑ E↑ F↑ G↑ A↑ B↑ |
| Half steps +¼ | behind black keys | +12 mm + Δ (further raised) | C#↑ D#↑ F#↑ G#↑ A#↑ |

**In detail:**
- **Whole steps + ¼ tone** (e.g. C+¼): sit behind the white keys at black-key height. For the player they are like a second row of black keys, but more accessible in width.
- **Half steps + ¼ tone** (e.g. C#+¼): sit behind the black keys, raised by the same increment again.

#### Playing Concept
- Piano technique remains fully intact – standard repertoire playable without adaptation
- Quarter tones are reachable by reaching backward/upward with the finger, similar to reaching far back on the black keys
- Intuitive assignment: every key has its quarter-tone neighbor directly behind it
- No remapping of the tonal space required

---

## 2. Dimensions (Research State)

From `Tastatur.txt` and standard sources:

| Component | Dimension (mm) | Note |
|---|---|---|
| Octave width | 165.0 | 7 white keys |
| White key width (head) | 23.6 | front section |
| White key length (visible) | 150.0 | to housing |
| Black key width (base) | 12.5 | top ~11.5 mm |
| Black key length | 95.0 | visible |
| Black key height | 12.0 | above white level |
| Key travel (white, front) | 10.8 | |
| Key travel (black) | 10.0 | |
| Pivot point | 180–250 | from front end |

**Quarter-tone keys – geometric constraints:**

- Width: ≤ black key width (≤ 12.5 mm), must fit in the same lateral space
- Length: as long as reachable without blocking black keys; likely 30–50 mm visible
- Height whole steps+¼: equal to black key height = +12 mm above white
- Height half steps+¼: black key height + Δ (Δ = step height white→black ≈ 12 mm) → ~+24 mm above white
- Travel: likely 8–10 mm (like black keys)
- Pivot: approximately 180–250 mm behind the front end of the white key, same as main keys

---

## 3. MIDI Implementation

### 3.1 MIDI 1.0 – Microtonality

Standard MIDI knows only 128 semitones. Several approaches exist for microtonality:

| Method | Description | Drawback |
|---|---|---|
| **Pitch Bend per note** | Each key sends Note + individual Pitch Bend | Only 1 bend per channel → limited polyphony |
| **MPE** (MIDI Polyphonic Expression) | Each note on its own channel (1–15) | Max. 15 simultaneous notes, broad synth support |
| **MIDI 2.0** | Per-note pitch with full resolution | Still limited synth support (2024–2026) |
| **Multi-channel mapping** | Quarter-tone keys on separate channel with global bend | Simple but inflexible |

> **Decision (May 2026): 24-tone mapping – no MPE.**
> The 122 keys (61 base + 61 VT) are mapped to MIDI notes 0–121. Each note has a defined frequency via Scala tuning table (.scl) in the synthesizer. No pitch bend trick, no MPE. Standard MIDI Note On/Off + Velocity. Aftertouch as Channel Aftertouch or CC.
>
> **Target software:** Logic Pro (native Scala support) and later SuperCollider (tuning classes, later OSC for continuous-board extension).
>
> MPE is entirely dropped – it was only needed to enable per-note pitch bend, which is not required with the 24-tone mapping approach.

### 3.2 Pitch Bend Resolution

Standard: ±2 semitones (200 cents) at 14-bit resolution → ~0.024 cents resolution. One quarter tone = 50 cents → easily representable.

### 3.3 Interfaces

- **USB-MIDI** (primary, class-compliant, no driver required)
- **5-pin DIN MIDI Out** (for older stage synthesizers)
- Optional: **TRS-MIDI** (3.5 mm, Type A or B)

---

## 4. Electronics

### 4.1 Microcontroller Candidates

| Controller | Advantages | Disadvantages |
|---|---|---|
| **Teensy 4.1** | Native USB-MIDI, very fast (600 MHz), extensive MIDI library, proven in DIY keyboards | Proprietary, more expensive (~€30) |
| **Raspberry Pi Pico (RP2040)** | Cheap (~€4), PIO for precise timing, USB-MIDI via TinyUSB | Fewer ready-made MIDI libraries |
| **Raspberry Pi Pico 2 (RP2350)** | Newer version, more RAM/Flash | Same limitations |
| **STM32F4xx** | Very common in professional MIDI hardware | More complex setup |

> **Recommendation:** Teensy 4.1 for quick start and proven MIDI libraries. For large key counts (>88 keys) possibly Raspberry Pi Pico as distributed architecture with I²C/SPI multiplexing.

### 4.2 Key Sensing – Decided Concept: Hall Effect

#### Basic Principle

**One linear Hall effect sensor per key**, permanent magnet fixed to the key. The sensor continuously outputs a DC voltage proportional to field strength – no pulse, no switch.

- **Velocity:** Teensy measures time between two voltage thresholds (software side, no second sensor)
- **Aftertouch:** the last 1–2 mm of travel past the main strike point (into elastomer stop) are measured directly
- **No FSR needed** – one sensor handles all three functions

#### Recommended Components

| Sensor | Type | Advantage |
|---|---|---|
| SS49E / SS495A | linear, analog | cheap, 5 V, readily available |
| A1324 / A1325 | linear, analog | more precise, ratiometric |
| DRV5055 | linear, analog | very small (SOT-23), Texas Instruments |

Small neodymium magnet (3×2 mm or 4×2 mm) on/under the key; Hall sensor on its own PCB in the frame.

#### Mounting Orientation

| Key group | Sensor position | Magnet position | Signal direction |
|---|---|---|---|
| Main keys | PCB at frame floor | underside of key tail | voltage drops when pressed |
| VT keys | PCB at frame ceiling | top of VT key | voltage rises when pressed (`value = MAX - raw`) |

VT keys have no space for sensor and stop below → PCB sits at the top of the frame, directly above the playing zone. Simple firmware inversion.

#### Aftertouch: Elastomer Stop instead of FSR

At the end of normal travel, the key presses into an **SLA-printed stop made of Flexible/Elastic Resin** (~Shore A 40–60). This yields 1–2 mm – the Hall sensor measures this travel directly.

- **No separate FSR, no additional wiring**
- Stop geometry (wall thickness, cavity) determines force–travel curve → iterate on test bench
- Suitable resins: Formlabs Flexible 80A / Elastic 50A, Phrozen Aqua Flexible, Liqcreate Flexible X
- Firmware: voltage range below `V_bottom_mechanical` is mapped to Aftertouch 0–127

#### Calibration (service / setup sequence, not continuous in-play learning)

Current preferred direction is a guided **three-point calibration per key**:

1. `0` = rest position
2. `pressed` = user-defined weighted press point
3. `aftertouch` = defined aftertouch / end-zone point

Role split:

- **Teensy** measures and delivers the raw values / stable averages
- **ESP32** or equivalent system controller leads the sequence, prompts the user, and stores / commits the resulting parameters

Important design intent:

- this is a setup / service calibration, not a continuous adaptation to the player's touch
- optional slow zero-point tracking in true rest state is acceptable
- the full `pressed` and `aftertouch` points should not be re-learned automatically during normal playing

#### Electronics

122 analog channels → 8× CD74HC4067 (16:1 mux) → 8 analog pins on Teensy 4.1. Teensy 4.1 has 18 analog pins – sufficient with reserve. Current packaging preference is to keep Hall sensor wiring local and distribute the mux boards close to the sensor groups where possible. Scan rate at 600 MHz: all 122 channels in under 1 ms.

### 4.3 Key Matrix & Multiplexing

With 61 base keys (5 octaves + 1 C) and doubled layout → 122 analog Hall channels:
- 8× `CD74HC4067` is sufficient for the full keyboard (`128` available channels for `122` sensors)
- preferred topology: shared `S0-S3` select lines, one dedicated analog output per mux to the Teensy ADC inputs
- enable lines are only required if several muxes are intentionally bussed onto one analog input; this is not the preferred baseline
- target: full scan cycle < `1 ms` for latency-free velocity measurement

### 4.4 Controllers (Pitchbend, Volume, etc.)

- 2× Alps RK09D potentiometer or endless encoder for pitchbend wheel
- 1× slider or pot for volume/expression
- Optional buttons for octave shift, program change, etc.
- Current preferred system split: these slow controls should be measured by the second controller, not by the Teensy real-time sensor front-end
- Preferred implementation quality: second controller + external ADC for `2-4` expression / pedal channels

---

## 5. Mechanics & Structure

### 5.1 Key Mechanism – Decided Concept

#### Basic Principle: Long Lever with Weight and Tension Spring

- Total lever length: ~230 mm (50 mm playing zone + 102 mm under black keys + ~80 mm tail)
- Pivot: captured 4 mm steel pin, one pin per half-octave (~82 mm)
- Return: tension spring near pivot (wire Ø0.3 mm, k ≈ 0.12 N/mm)
- Weight: ~15–20 g lead in key tail, press-fit
- Key blank material: **Polymaker PolyLite ASA** (Tg ~108°C, low warp, UV-resistant)

#### Target Forces

| Parameter | Target value |
|---|---|
| Downweight (strike weight) | ~45–50 g at finger point |
| Upweight (return force) | ~25–35 g |
| Aftertouch onset | ~50 g (= 0.5 N) |
| Aftertouch end | ~100 g (= 1.0 N) |
| Aftertouch travel | 3–4 mm (clavichord reference) |

#### Pivot Bearing

- **Pivot bearing:** 4 mm steel pin continuous, key hooked in via hook-nut geometry
- Hook-nut in ASA runs directly on steel pin, silicone oil applied once at assembly
- **Front guide:** HSS nail drill Ø2 mm (~28 mm long), bonded into Tough Resin frame (Loctite 638 or press fit), PTFE tube Ø4/2 mm as bushing in key
- Guide slot in key: elongated hole ~2.2 × 8 mm (allows travel without binding)
- **Side guidance:** integral partition walls in SLA frame, gap ~0.15–0.2 mm

#### Modular Frame

- Unit per **half-octave** (~82 mm) = C–E and F–B separate
- Fits in SLA print bed (120 mm width)
- Split at E/F: natural gap in black key row, shared bearing block = central support against pin deflection
- Supports at octave boundaries: **aluminium square tube 10×10×1 mm** as structural insert in printed ASA/Tough Resin shell
- Frame Tough Resin (SLA): precise, with integral pivot web and partition walls

#### End Stop and Aftertouch Buffer

- Front guide pin carries a slip-on **silicone O-ring** (Shore A 30–40, cord Ø3–4 mm)
- O-ring yields 3–4 mm travel at ~1 N end force → aftertouch zone
- Below that: **felt pad on hard substrate** as firm end stop (no click noise)
- Hall sensor just behind the guide pin (15–20 mm from front end) → measures full travel directly

**Option B: SLA-printed slotted hollow cylinder (Formlabs Elastic 50A)**
- Hollow cylinder with closed top and bottom rings + 4 axial rounded slots in middle zone
- Sits freely on frame floor in centering recess, key presses from above (no captive pocket)
- Closed end rings distribute stress at slot terminations → far better fatigue life than through-slots
- Hard stop ring (Standard Resin) on top limits travel to hub_max = 3 mm
- Optional outer sleeve with ~9.6 mm bore creates progressive force onset at near-full travel
- Parametric SCAD model: `docs/CAD/aftertouch_puffer_schlitz.scad`
- Estimated force: ~1.7 N at 3 mm with default parameters; tunable via slot depth/width

**Option C (preferred for prototype and long-term): EPDM commercial profiles**
- No printing required; purchased by the metre; trivially serviceable
- **Guide pin is independent** of the buffer — buffer sits on frame floor, key has flat contact surface
- Guide pin material: **hardened steel Ø2 mm** (dental/nail drill bits, already ordered)
  - Martensitic stainless steel; may be remanently magnetised by key magnet
  - Mitigation: minimum **25 mm distance** between pin and Hall sensor centre
  - At 25 mm: stray field < 0.3 mT → < 1.5 mV offset at sensor, negligible
  - Ceramic (ZrO₂) ruled out: brittle under bending loads from glissandi → fracture risk
  - CFK ruled out: fibre splitting at PTFE sliding surface (experience from aeromodelling)
  - Steel at 25 mm spacing is the final solution, not just a prototype choice
- Hall sensor mounted **directly below the buffer** in the frame floor:
  - EPDM is non-magnetic; field passes through without distortion
  - Buffer contact point = Aftertouch zero point, mechanically and sensorially identical
  - Rest position: magnet far → low field; EPDM contact: magnet ~2 mm above sensor → Aftertouch zone begins; full travel: hard stop → maximum value

**Current prototype stack (main keys, May 2026): felt + PORON with Kapton isolation**
- Hall sensor sits in front frame pocket (about 8 mm deep region)
- Sensor top is covered by **2-layer Kapton tape** (50–100 um each), then 1.2 mm dense piano felt
- No FR4 cover plate in baseline build (height budget and precision geometry control)
- Mechanical load path is carried by surrounding frame geometry, not by sensor package
- Behind front end-stop zone: PORON strip, 4 mm thick and 4 mm wide, as felt/PORON/felt sandwich
- Initial PORON height: flush with end-stop level; tuning option: lower PORON by 1.0 mm
- Target feel: clear strike point + additional ~2 mm controlled aftertouch travel

**Option C1 – EPDM D-profile (solid rubber, hollow cross-section)**
- D-profile 9 × 10 mm (height × width), wall ~1.5 mm, Shore A 60
- Cut to 12 mm per key; flat base for bonding (contact adhesive or cold vulcanising)
- 2 mm compression = 22 % → force ~1.5–2.5 N; clear tactile onset from hollow collapse
- Best choice for a clearly perceptible aftertouch entry point
- Search term: *„EPDM D-Profil 9×10 selbstklebend Shore 60"*

**Option C2 – EPDM closed-cell foam rubber strip**
- Rectangular strip 10 × 10 mm, cut to 12 mm per key
- 2 mm compression = 20 % → force ~0.15–0.4 N; very soft, no distinct onset click
- Better for slow, gradual aftertouch; less suited for precise entry-point detection
- Search term: *„EPDM Moosgummi geschlossenzellig Streifen 10 mm"*

**Option C3 – Combined D-profile + foam sandwich**
- D-profile (C1) bonded on top of foam strip (C2), cold-vulcanised together
- Phase 1 (0–2 mm): D-profile compresses → clear onset, defined resistance
- Phase 2 (2–4 mm): D-profile near collapsed, foam takes over → progressive softening
- Mechanically progressive without any calculation; tunable by varying foam thickness
- First experiment: measure C1 alone, then add foam layer and compare

**Decided layout for main keys:**
- Buffer, magnet, and Hall sensor clustered at front of key (~front 20 mm zone)
- Guide pin (hardened steel Ø2 mm) placed after damping zone, minimum 25 mm from Hall sensor centre
- Key underside is flat and clean — all functional elements are on the frame

#### Sensor Position (Main Keys)

- Hall sensor **at front floor** in dedicated pocket, before guide pin location
- Magnet on underside of key, directly above sensor
- Rest distance magnet–sensor: ~12–15 mm → voltage ~1.5–2.0 V
- End stop: ~4 mm distance → voltage ~3.5–4.0 V
- Aftertouch (felt/PORON stack compression): ~2 mm → voltage ~4.0–4.3 V
- PCB lies flat on base plate, sensor soldered lying (legs bent 90°), flat side up

#### VT Keys (Quarter-Tone Plane)

- Shorter lever, pivot further forward (spatially behind main keys)
- Sensing and guidance **mirrored from above**: PCB traverse fixed in frame above VT keys
- Hall sensor pointing down, magnet on top of VT key
- Elastomer stop (or O-ring) in upper traverse = aftertouch + end stop from above
- Firmware inversion: `value = MAX - raw`
- **Force path note:** With short VT lever, pivot rail takes increased reaction force (~1.5× finger force) → rail must be dimensioned accordingly (aluminium insert)

#### Print Materials

| Component | Material | Process |
|---|---|---|
| Key blanks (main + VT) | Polymaker PolyLite ASA | FDM, printed upright |
| Frame modules, bearing blocks | Tough Resin | SLA |
| Aftertouch buffer (Option A) | Silicone O-ring Shore A 30–40 | Purchased part |
| Aftertouch buffer (Option B) | Elastic 50A slotted hollow cylinder | SLA (Formlabs) |
| Aftertouch buffer (Option C1) | EPDM D-profile 9×10 mm Shore A 60 | Purchased, cut to length |
| Aftertouch buffer (Option C2) | EPDM closed-cell foam strip 10×10 mm | Purchased, cut to length |
| Aftertouch buffer (Option C3) | C1 + C2 sandwich, cold-vulcanised | Purchased + bonded |
| Guide pin (all options) | Hardened steel Ø2 mm (nail drill bits), 25 mm from sensor | Ordered |
| Structural insert supports | Aluminium square tube 10×10×1 mm | Purchased, bonded in |

#### Base Frame Concept: Aluminium Tube Frame with Printed Node Connectors

Instead of a plywood base plate: **aluminium square tube frame** with printed ASA node connectors.

**Connection principle:**
- Aluminium tubes butt-join into printed ASA connectors
- Connectors have internal **knurling** (0.3–0.5 mm deep, 0.8–1.0 mm pitch) → mechanical form-lock for epoxy → adhesion independent of plastic–metal adhesion
- Bond with epoxy (UHU Endfest / Loctite EA 9461), aluminium roughened and degreased beforehand
- **M4 heat-set inserts** (Ruthex or similar) in ASA connectors (200–220°C soldering iron, Ø5.7 mm bore)
- Screws from outside through aluminium tube into heat-set inserts → mechanical retention in addition to bonded joint

**Advantages over plywood:**
- Lighter and stiffer
- Fully demountable despite bonded tubes
- Octave modules individually mountable and replaceable
- Node connectors simultaneously serve as mounting points for pivot rail, sensor bridge, and supports

### 5.2 Housing

- Wooden corpus (plywood/MDF as base structure, solid wood veneer for appearance)
- Aluminium rails for guidance and rigidity
- Target stage-box dimensions: depth ≤ 350 mm, height ≤ 120 mm

### 5.3 Scope

Decided:
- Base keyboard: 5 octaves + 1 C = 61 keys (classic organ/synth format)
- Quarter-tone extension: doubled key layout (additional quarter-tone row)
- Advantage: standard spare parts from 61-key instruments are readily available for sensing and mechanics

To clarify:
- Whether the topmost additional C+¼ is implemented as its own key (122 vs. 121 keys total)

---

## 5b. Firmware Architecture

### Design Principle: Two-Controller Separation

Processing is split between two independent units – clear responsibilities, independently upgradeable.

#### Teensy 4.1 – Sensor Front-End (Real-Time)

- Single responsibility: raw data acquisition with maximum achievable precision
- Hard real-time loop without OS jitter (no Linux, no RTOS needed)
- 122 channels via 8× CD74HC4067 mux, ADC scan at fixed rate
- Velocity: time between two voltage thresholds (requires µs resolution → only feasible on Teensy)
- Aftertouch: last portion of travel from the same analog signal
- Data transmission **compressed** – events only on state change
- Teensy should remain autonomous in the scan loop and should not depend on host polling

**Compressed event format (draft):**

| Field | Width | Content |
|---|---|---|
| Key index | 7 bit | 0–121 |
| Type | 2 bit | down / up / aftertouch |
| Value | 12 bit | velocity or aftertouch intensity |
| Timestamp | 16 bit | µs relative to last event |

→ ~4 bytes/event, only on change. Channels with no movement are not transmitted.

Interface to the system controller: push-style event stream (UART preferred as baseline). A separate control/calibration path may be split off if this later proves cleaner than a single duplex channel.

#### ESP32 – System / Control Layer (Current Preferred Intermediate Stage)

- Reads expressions, pedals, wheels, buttons, and other slow controls
- Orchestrates calibration sequences for the Teensy front-end
- Stores settings and operating modes
- Can already emit standalone MIDI / MPE without requiring the Raspberry Pi layer
- Provides a clean middle stage between raw sensor front-end and optional high-level host processing

#### Raspberry Pi – Protocol Back-End

- Receives compressed events from Teensy
- Transforms to MIDI, OSC, and further formats
- No real-time constraint at this level (latency budget sits in the Teensy)
- Optional rather than mandatory in the current architecture; the ESP32 layer may already cover standalone MIDI / MPE operation
- **Phase 2:** SuperCollider directly on RPi (Sclang + scsynth)
  - Native OSC support in SC
  - Tuning tables, synthesis, routing all in Sclang
  - RPi 4/5 sufficient for SC synthesizer layer
  - Instrument becomes DAW-independent

### Upgrade Stages

| Phase | Configuration |
|---|---|
| 1 (current real-time core) | Teensy front-end only |
| 2 | Teensy → ESP32 (standalone MIDI / MPE, calibration + controls) |
| 3 | Teensy → ESP32 → RPi (protocol flexibility / OSC / SuperCollider) |
| 3b | MPE layer: per-note pitch bend from aftertouch zone → Bebung effect |

**Key architectural rule:** the Teensy layer remains the real-time master for sensing, while ESP32 / RPi layers are additive system and protocol layers.

### Sensor Environment / Drift Notes

- Hall-sensor drift risk is considered manageable if ferromagnetic parts are kept away from the immediate sensor zone.
- Steel guide pins should preferably stay about `30 mm` from Hall sensor centres where packaging allows; `25 mm` remains the hard lower design limit already used elsewhere.
- Brass mounting parts are acceptable close to the Hall sensors; for the adjustable KLAK20 sensor rail, brass/aluminium fastening hardware is currently preferred over steel.
- Practical mounting consequence: for the KLAK20 sensor rail, printed slot nuts / nut stones with embedded brass nuts are currently preferred over steel T-nuts.
- Keep Hall sensors and magnet paths at least about `30 mm` from the outer housing skin in zones where metal stands or brackets can approach; `40 mm` is preferred in exposed areas.
- Avoid locating transformers, strong power supplies, loudspeaker magnets, or other magnetic sources directly under or on the instrument.
- The VT design may deliberately use a steel upper reaction rail if that rail is kept structurally separate from the Hall sensor rail and sufficiently far from the sensor path.

### Phase 3b: Bebung via MPE (Optional Expressive Layer)

The Hall sensor already measures the full travel continuously, including the elastomer aftertouch zone. This makes a Bebung effect physically feasible without any hardware changes:

- **Bebung principle:** Post-strike pressure modulates pitch – the only historical keyboard instrument with this capability was the clavichord (tangent stays in contact with string).
- **MPE implementation:** Each key on its own MIDI channel (1–15). Aftertouch zone maps to both Aftertouch intensity (CC) *and* a small per-note Pitch Bend (±N cents, configurable). Other simultaneously held notes are unaffected.
- **Firmware split:** lower aftertouch range → intensity; upper range → pitch modulation. Boundary configurable.
- **Hardware requirement:** none – sensor, mechanics, and event format already support it.
- **Constraint:** MPE limits simultaneous expressive notes to 15. Sufficient for impressionistic playing style; not a limitation for this instrument's primary use case.

This option is kept open deliberately (maximize options, test later). The 24-tone mapping remains the base; MPE is an additive expressive layer for Phase 3.

---

## 6. Reference Projects & Literature

- **Fokker Organ** (31-tone equal temperament): Historical reference instrument
- **Tonal Plexus (H-Pi Instruments)**: Commercial microtonal MIDI keyboard
- **Lumatone**: Isomorphic honeycomb layout, 280 keys, MPE
- **Jankó keyboard**: Symmetric layout, all keys identical across all keys
- **Teensy USB-MIDI** (PJRC official docs): https://www.pjrc.com/teensy/td_midi.html
- **MIDI Polyphonic Expression (MPE)**: https://midi.org/mpe
- **Xenharmonic Wiki**: https://en.xen.wiki

---

## 7. Open Questions / Next Steps

- [x] Layout decision: Kassel Principle (Organ St. Martin) – two height-offset rows behind the standard keys
- [x] Sensor concept: Hall effect sensor per key, magnet on key, elastomer stop for aftertouch – no FSR, no keybed purchase
- [x] Scope: 61 base keys (5 octaves + 1 C)
- [x] MIDI protocol: 24-tone mapping, no MPE; Scala tuning in Logic Pro / SuperCollider
- [x] Mechanics: custom build fully defined (lever, pivot, guide, weight, spring, end stop, O-ring aftertouch)
- [x] Sensor position main keys: Hall sensor at front floor pocket in front zone, magnet under key, guide pin placed after damping zone
- [x] Aftertouch solution: felt (1.2 mm) + PORON (4 mm) stack with Kapton sensor isolation; target additional ~2 mm controlled travel
- [x] Frame concept: half-octave SLA modules, aluminium square tube as structural insert
- [x] Filament: Polymaker PolyLite ASA (Tg 108°C, 3 kg ordered)
- [x] Electronics: A1324LUA-T ordered (50 pcs), CD74HC4067 mux, Teensy 4.1, VS Code + PlatformIO
- [ ] Build test bench: one main key with Hall sensor, felt/PORON stack, steel guide pin (>=25 mm from sensor), spring, weight
- [ ] Playability test: mock-up for reach check (accessibility of half-steps+¼)
- [ ] Determine exact quarter-tone key dimensions (width, length, travel, height offset)
- [ ] Pivot position analysis: optimal pivot location for main and VT keys
- [ ] After test bench: 1-octave build for playability test by the pianist
