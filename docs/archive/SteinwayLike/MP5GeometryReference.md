# Kawai MP5 Geometry Reference

> **Archive role (June 2026):** This MP5 note now belongs to the archived `Steinway-like` branch. It remains useful as a proportional reference for the earlier piano-like geometry study, but it is no longer the active target direction for the keyboard layout.

This note collects the geometry-related information currently available for the Kawai MP5 and separates public source-backed facts from project-side geometric inference.

## 1. Publicly Confirmed MP5 Data

The following items could be confirmed from Kawai's public MP5 archive/specification material:

- Keyboard action: `88 weighted keys, Advanced Hammer Action IV-E with AR technology`
- Overall dimensions: `1356 x 340 x 172 mm` (`W x D x H`)
- Weight: `20.5 kg`

These are useful packaging anchors, but they do **not** include an internal pivot drawing or a service-level action section with exact key-axis coordinates.

## 2. Public Geometry That Could Not Be Confirmed Directly

The following internal action data has **not** been found in a public Kawai source during this research pass:

- exact white-key pivot coordinates relative to the front edge
- exact pivot height relative to the white-key top surface
- exact white-key overall length or hammer-stick length
- exact black-key reference point and black-key lever arm
- exact guide-pin or balance-pin coordinates
- exact MP5 service drawing for the AHA IV-E action

Therefore, any concrete pivot coordinate stated below must be treated as a **project reference estimate**, not as a factory-proven MP5 CAD value.

## 3. Current Project Reference Geometry Derived from the MP5 Comparison

For the current keyboard project, the MP5 comparison was condensed into the following working reference geometry for the normal key row:

- White-key front reference point at rest: `O = (0, 0)`
- Main-key pivot axis: `Y = 210.0 mm`, `Z = -24.0 mm`
- Interpretation: pivot about `210 mm` behind the white-key front edge and about `24 mm` below the white-key top reference surface

This reference is already the active baseline in the project documentation and is treated as a plausible MP5-like proportion rather than a measured Kawai internal dimension.

## 4. Derived Lever Arms and Motion References

Using the current project reference pivot above, the following effective lever arms are in use:

- White key front lever arm: `210.0 mm`
- Black key front reference plane: `Y = 53.5 mm`
- Effective black-key front lever arm: `210.0 - 53.5 = 156.5 mm`

Associated geometric motion references currently used in the project:

- White-key front travel: `10.8 mm`
- Black-key front travel: `10.0 mm`
- White-key bottom-stop rotation: `asin(10.8 / 210.0) = 2.95 deg`
- Black-key bottom-stop rotation: `asin(10.0 / 156.5) = 3.66 deg`

These values are not public MP5 measurements. They are the current project-side geometric interpretation of an MP5-like normal-key proportion.

## 5. Confidence and Use Rule

Current confidence split:

- **High confidence:** the MP5 uses the `AHA IV-E` action with AR technology, and the external instrument envelope is `1356 x 340 x 172 mm`
- **Medium confidence:** a pivot around `Y = 210 mm` from the white-key front edge is a realistic MP5-like proportion
- **Medium confidence:** a pivot around `Z = -24 mm` relative to white-key top reference is a realistic MP5-like vertical placement
- **Low confidence as a factory claim:** `Y = 210 mm`, `Z = -24 mm` as the literal internal Kawai MP5 production coordinate

Design rule for this project: use `Y = 210 mm`, `Z = -24 mm` as the working MP5-style reference geometry unless direct measurement from a real MP5 action or a service drawing becomes available.

## 6. Source Notes

Public sources checked during this pass:

- Kawai MP5 archive/specification page
- Kawai MP5 owner's manual PDF
- public manual mirrors and general web results

Outcome of the source pass:

- official/public sources were sufficient to confirm the action family and external instrument dimensions
- official/public sources were **not** sufficient to confirm an internal pivot drawing or an exact service-level coordinate set

## 7. Practical Consequence for Further Work

If tighter fidelity to the MP5 action is required, one of the following would be needed:

- direct measurement on a real MP5 keybed
- a genuine service manual with mechanical drawings
- teardown photography with a known dimensional reference in the same plane

Until then, the project should treat the MP5 comparison primarily as a **proportional reference**, not as a fully known reverse-engineered mechanism.