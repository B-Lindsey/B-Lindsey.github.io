---
title: "Squaring the Gantry and Fixing Lost Steps"
date: 2026-10-28
tags: ["cnc", "crossfire-pro", "gantry", "squaring", "lost-steps", "maintenance"]
draft: false
weight: 9
lastmod: 2026-10-30T16:15:00-07:00
summary: "Checking and squaring the CrossFire PRO gantry, tightening couplers, and working through Langmuir's lost-steps and stalling checks, from coupler slip to damaged motor plugs."
series: ["CrossFire PRO procedures"]
series_order: 9
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.**

## Applies to

My CrossFire PRO: dual Y lead screws and a single X lead screw (ACME; Langmuir's comparison page lists 3/8 in-8 4-start Y with a 1/2 in 5-start X, while current PRO pages say 1/2 in 5-start on all axes. Measure yours; the procedures are the same either way), acetal anti-backlash lead nuts, NEMA 23 steppers, couplers (2-screw aluminum or 4-screw steel), and V-groove bearing carriages with adjustable bearing blocks. No limit switches unless I add the kit. **The PRO has no belts**, so belt-tension advice doesn't apply. Also doesn't cover:

- The XR's ball screws, pulleys, and set-screw notes (thread 21584 is XR).
- The original CrossFire/XL gantry video.
- The MC4000 electronics.

## Steps: checking for square

1. Put the **Marker Pen Attachment** (or a sharp pointer) in the torch mount.
2. Draw a large rectangle, as big as the table comfortably allows (for example 30 x 30 in), on a flat sheet or on paper taped to a sheet. Program it in SheetCAM and run it following Langmuir's Marker Pen instructions. Dry Run mode doesn't fire the plasma.
3. **Measure both diagonals** with a good steel tape, hooked on the same side of the line each time. If they're equal, the gantry is square. If they differ by more than you can measure reliably, re-square.
4. Also measure the sides. If X and Y sides are both off by a similar percentage, that's a scale problem (lost steps or slipping couplers), not a square problem.

Langmuir staff (thread 9412) also recommend a test square as the check.

## Steps: squaring the gantry (Langmuir PRO assembly, final steps 6–7)

1. **Power on the electronics** so the motors hold. Connect FireControl.
2. **Loosen the lead nuts:** the 2 bolts on the X lead nut, the 2 bolts holding the X lead-nut tab to the X carriage, and the 4 bolts on each Y lead nut. Loosen until the nuts can float.
3. In FireControl, jog to **maximum +X** (right arrow) and **minimum −Y** (down arrow).
4. When the gantry is close to the stanchion plates, **set the jog speed to 50 ipm**. Tap −Y repeatedly until the bearings on **both** gantry carriages lightly touch the stanchion plates. That squares the gantry to the slat bed.
5. Tighten in this order: the **2 bolts on the X lead nut**, then the **2 bolts on the X lead-nut tab**, then the **4 bolts on each Y lead nut**.
6. Re-check with the diagonal test above.

**Staff alternative** (thread 9412, Langmuir staff; summarized from search results, not checked against the full thread, so read it before using this): loosen the Y coupler(s), turn the Y lead screw by hand until that side seats against the stanchions, then re-tighten the couplers using the procedure below, with the **motors powered**.

## Steps: coupler tightening (Langmuir PRO assembly step 6, with motors powered)

1. Tighten the **inside** screws snug.
2. Tighten the **outside** screws snug.
3. Turn the **inside** screws another **1/8–1/4 turn**.
4. Turn the **outside** screws another **1/8–1/4 turn**.
5. Grab the lead screw and try to turn it against the motor. If the coupler slips, repeat steps 3–4.

**Caution (Langmuir):** too much torque can strip the screws or the hex key.

## Steps: when a motor stalls or the table loses position (Langmuir PRO troubleshooting)

Work through these in order:

1. **Coupler slip test.** Put three Sharpie dots in a line: one on the coupler, one on the motor shaft, one on the lead screw. Jog back and forth. If the dots separate, re-tighten the coupler (above).
2. **Y carriage realignment (PRO only).** Redo **PRO assembly Step 5**. On each of the 8 adjustable bearing blocks, seat both cap screws, then back them off about **1/4 turn**. Turn the adjustment set screw clockwise until at least one opposing fixed bearing touches the rail and **no play** can be felt. Then tighten the cap screws.
3. **Dry lead screw.** Lubricate with **machine oil** and jog the full travel so it gets into the lead nuts. **Don't use** white lithium grease, WD-40, or dry lube on the lead screws (Langmuir).
4. **Wrong bearing mount.** The X motor and bearing mounts are **shorter** than the Y ones. Both Y mounts should be the same length.
5. **Mounts out of square** bend the lead screw slightly. Check them with a protractor or square.
6. **Bent lead screw.** Take it out and roll it on a flat, clean surface. Langmuir says to straighten a slight bend by hand.
7. **Lead nut installed wrong.** Compress the anti-backlash spring fully while threading the nut onto the screw.
8. **Lead nut tab out of square** (rare). Loosen its 4 bolts, jog, and see if the binding goes away.
9. **Motor plug arc damage or a loose plug.** This is the usual cause if a motor **sometimes jogs the wrong way**. With power off, unplug each motor's D-sub and look for burning, melting, or charring. Re-plug it and **tighten both D-sub screws**, with no wiggle.
10. **Z axis.** If Z sticks or has play, adjust the eccentric bearing axles with a 5 mm wrench: clockwise adds preload. Use the **minimum** preload that removes play while Z still slides freely. Clean the Z rails with solvent, and check the torch is square with the Z tram video.
11. **After any rebuild,** run Langmuir's **PRO break-in program** (`CrossFire PRO-BreakIn-v1.6.tap`). If you have the Limit Switch Kit, soft limits may need disabling because the break-in program runs the full travel (Langmuir).

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the Razorweld CUT45 CNC (model JRWPC45LH).**

- **If the frame itself is out of square. toolboy (long-time forum member)**, t/26365/27. When adjusting the gantry couldn't fix it, he:
  1. Took the gantry off.
  2. Loosened the frame bolts.
  3. Squared the frame by measuring corner to corner (both diagonals equal), keeping it level.
  4. Tightened the frame, then refit the gantry.
  - It's a big job. Do it only if the diagonal check on this page shows the frame is the problem. Follow Langmuir's assembly steps when refitting.
- **Recheck before the final tightening. 72Pony**, t/45654/4: follow Langmuir's squaring directions exactly, and recheck square before the final tightening.
- **Lost steps that are really noise. Bigdaddy2166**, t/48104/10: EMI ground straps on the motors. Work through [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}}) first.
- **Z bottoming out. ds690 (long-time forum member)**, t/47251: leave about 1/2–3/4 in of Z travel when the tip touches the metal ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})).

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Diagonals unequal; parts are parallelograms | Gantry out of square | Squaring steps (PRO assembly step 7) |
| Parts shift partway through a job, same axis each time | Coupler slipping | Sharpie test; re-tighten (PRO troubleshooting) |
| Motor buzzes or stalls in one spot | Binding: dry screw, bent screw, mount out of square, lead nut | Langmuir PRO troubleshooting guide, stalling and binding sections A–F |
| Stalls only at high speed | Binding plus speed; machine max is 300 ipm | Fix the binding; lower the feed or rapid speed for that job |
| Motor sometimes runs the wrong way | Arc-damaged or loose D-sub motor plug | Inspect, re-seat, screw down (Langmuir PRO troubleshooting guide, section G) |
| Holes oval along one axis | Play in carriage bearings or coupler | Carriage preload Step 5; coupler test |
| Torch hits tipped-up parts and the table loses position | Collision | Clear the slats; the IHS auto-lifts 1/16 in on contact (PRO assembly), but a hard hit can still shift the gantry. Re-zero |

## Where sources disagree (and the starting choice)

- **How tight to make couplers.** PRO assembly: snug plus 1/8–1/4 turn, with a stripping warning. PRO troubleshooting: tighten "until they cannot be tightened any more" if they slip. **Start with the assembly procedure**, and only go tighter if the Sharpie test still shows slip, stopping before anything strips.
- **Lubrication.** Langmuir says no WD-40 on the **lead screws**, but it does say to use WD-40 on the **sidewall of a sticky Z bearing** (troubleshooting). These are different parts, so both apply.
- **Squaring method.** The assembly guide (jog against the stanchions with nuts loose) and staff thread 9412 (seat against the stanchions by turning a Y screw) agree on the principle. Starting choice: the assembly guide.

## Sources

- Langmuir, PRO assembly (Step 5 carriage preload; final steps 6 couplers and 7 squaring; Z table): <https://www.langmuirsystems.com/pages/pro-assembly>
- Langmuir, PRO troubleshooting (stalling and binding A–G; break-in and soft limits; Z preload): <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, coupler tightening video: <https://www.youtube.com/watch?v=tftc32RcxT8>
- Langmuir, Z-axis tram video: <https://www.youtube.com/watch?v=xCbOJz-zfl8>
- Langmuir, PRO break-in program: <https://assets.langmuirsystems.com/file/CrossFire+PRO-BreakIn-v1.6.tap>
- Langmuir, CrossFire PRO specs (lead screws, 300 ipm, accuracy): <https://www.langmuirsystems.com/pages/crossfire-pro>
- Langmuir, Limit Switch Kit: <https://www.langmuirsystems.com/products/limit-switch-kit-for-crossfire-and-crossfire-pro>
- Forum: <https://forum.langmuirsystems.com/t/9412> (staff squaring), <https://forum.langmuirsystems.com/t/21584> (XR only, not used)
- FireShare, "Crossfire Pro Index and squaring gauge" (community): <https://fireshare.langmuirsystems.com/projects/crossfire-pro-index-and-squaring-gauge-3150>
- Forum, experienced members: <https://forum.langmuirsystems.com/t/26365> (toolboy: frame re-square), <https://forum.langmuirsystems.com/t/45654> (72Pony: recheck square), <https://forum.langmuirsystems.com/t/48104> (Bigdaddy2166: EMI straps), <https://forum.langmuirsystems.com/t/47251> (ds690: Z travel)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will be added here as they come in, with: Date; Rectangle size; Diagonal 1; Diagonal 2; Side X / side Y; Action taken; Notes.
