---
title: "Kerf Width and Hole/Part Accuracy"
date: 2026-10-28
tags: ["cnc", "plasma", "kerf", "holes", "accuracy", "sheetcam", "razorweld-45"]
draft: false
weight: 7
lastmod: 2026-10-30T18:30:00-07:00
summary: "Measuring kerf and cutting accurate holes and parts on a CrossFire PRO with the CUT45 and X45 torch, using SheetCAM v8 kerf offsets: a 2 in square test, a hole coupon, and forum kerf numbers."
series: ["CrossFire PRO procedures"]
series_order: 7
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.**

## Applies to

My CrossFire PRO (rated accuracy 0.002 in per 12 in, step resolution 0.0005 in, ACME lead screws with anti-backlash nuts) with THC. The Razorweld CUT45 CNC (model JRWPC45LH) is on 230 V with the X45 machine torch, and I make kerf offsets in SheetCAM v8 with the FireControl v1.6 post. Doesn't cover: XR ball-screw accuracy figures, Hypertherm kerf tables, and Fusion's kerf compensation (I use SheetCAM).

**Status:** The only Langmuir kerf number for this cutter is **0.06 in**, in the example SheetCAM tool. Community numbers range from 0.021 in to 0.059 in. **Measure your own** for each amps, speed, and thickness combination.

## Steps: measuring kerf

1. Dial in amps, speed, and heights first ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}) and [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). Kerf changes with every one of them.
2. In SheetCAM, make a tool with **kerf width = 0**. Draw a **2.000 x 2.000 in square**. Cut it as an outside profile with **no offset** ("on the line"), with the lead-in in scrap.
3. Let it cool, knock off the dross, and measure the square across the flats in X and in Y with calipers, **top and bottom faces** (bevel makes them differ).
4. **Kerf = 2.000 − measured size.** The torch took half a kerf off each side. Use the **average of X and Y, top side**, for the SheetCAM kerf width. Write down the bottom-side number too.
5. Put the measured kerf in that SheetCAM tool and in the log (`kerf_set_in`, `kerf_measured_in`).
6. **Check it:** cut the same 2.000 in square as an outside-offset part, plus a 1.000 in hole as an inside offset. Measure both. If the square is undersize and the hole oversize, the kerf setting is too small; increase it by the error. If it's the other way around, reduce it.

## Steps: hole test coupon

1. On a 6 x 4 in coupon of the material, draw holes of **1/4, 3/8, 1/2, 3/4 and 1 in**, plus a 2 in outer square. Use inside offsets for the holes and an outside offset for the outer edge.
2. **Lead-ins:** start each hole near its center with a short straight or arc lead-in that **doesn't cross itself**. **No lead-out** (Langmuir; see [THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
3. **Cut order:** holes first, outside last, so the part doesn't move before the holes are cut. Check the cut-order setting in the SheetCAM plasma operation (the v8 default hasn't been confirmed here), and step through the preview to confirm the order.
4. **THC on small holes:** with Langmuir's defaults, THC doesn't act on loops shorter than 0.5 in, and it freezes whenever the feed is under 85 % of the program's fastest feed ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})). You don't need to turn THC off by hand for holes.
5. **Feed rate for holes:** No Langmuir or Razorweld rule for slowing down on small holes turned up in the research. Run the coupon at the line-cut speed first. If holes come out tapered, out of round, or with a divot where the cut finishes, try a second coupon with the **hole operation slower** (separate SheetCAM operation). Record both.
6. **Measure** each hole top and bottom with calipers or pin gauges. Write down the smallest hole that comes out round and usable for each thickness. **Rule of thumb:** if a hole has to be accurate, cut it undersize and drill or ream it to size.

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

- **Estimate kerf from the tip. 72Pony (CUT60)**, t/28035/10 and t/12723/18.
  - Rule of thumb: **kerf ≈ orifice + 0.01 in.** For my X45's 1.0 mm (0.040 in) tip (mechanic416, t/21266), that's about **0.050 in**.
  - mechanic416 (long-time forum member) says the X45 tip's kerf is **at least 0.055 in**. Langmuir's example tool uses 0.06.
  - So expect **0.050–0.060 in**, and measure.
- **72Pony's measuring method.**
  1. Draw a 2 in square with a 1 in hole.
  2. Cut it **on the line** (no kerf offset).
  3. Measure the square. Drawn size minus measured size = kerf. For example, 2.000 in drawn and 1.945 in measured means kerf = 0.055 in.
  - Kerf grows as the tip wears, so re-check with a new tip.
- **Commissioning squares.**
  - TomWS, t/24586/2: 2 in square: IHS dry run with plasma off, THC off cut, THC on cut, then measure and adjust kerf.
  - ChelanJim, t/41575/4: a 2 in box with a 3/4 in circle; and a kerf of 0 is always wrong.
  - Holla2040 (same CUT45), t/35995/10: cut about 30 test squares with 1 in circles to dial his in.
- **SheetCAM's kerf only shifts the path. toolboy (long-time forum member)**, t/24105/2. The real kerf comes from the nozzle, amps, speed, and air. The setting just tells SheetCAM how far to offset.
- **Pierce and lead-in placement.**
  - richarddbeck83 (Everlast), t/39953/6: the pierce offset must be bigger than the kerf, so the pierce lands in scrap. Use a lead-in angle under 90°, and pierce at the largest part of the feature.
  - jamesdhatch (long-time forum member), t/19097/2: lead-in about **2x kerf**. A shorter one leaves a divot.
  - Wsidr1, t/46239/8: pierce inside the circle (the scrap), not on the line.
- **Gaps between parts. Wsidr1**, t/34970/9: at least 2x kerf.
- **Small holes.**
  - ChelanJim, t/32789/3: without Feed Optimization (Fusion) or an equivalent, expect poor hole completion. SheetCAM's matching setting hasn't been identified yet ([SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})).
  - TomWS, t/36785/19, and toolboy, t/35951/14: for accurate holes, mark them (peck or center-punch) with the plasma and **drill** them.
- **Thin-sheet kerf numbers from other setups (rough only).**
  - PWCNC (long-time forum member, torch not confirmed): .021–.026 in at 28 A on .062 steel (t/847/12); .040 in at 35 A on .120 steel (t/847/28).
  - Cletus (CUT60): .025 in at 31 A on 16 ga aluminum, 150 ipm (t/18698/46); and .025 in at 30 A on 16 ga steel, 150 ipm (t/20256/7). These are two different posts on different metals, checked against both posts on 30 October 2026.

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| All parts undersize and holes oversize by the same amount | Kerf set too small | Raise the SheetCAM kerf by the error |
| Kerf wider than before at the same settings | Worn nozzle or low air pressure | New nozzle; check the regulator (Langmuir) |
| Kerf wide on thin sheet | Too many amps | Lower the amps (my JRWPC45LH operating manual, p. 12: on thin material "turn down the amperage and change to a lower-amperage tip to maintain a narrow kerf") |
| Holes tapered (bigger on top) | Bevel: height, speed, nozzle | [Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}}) |
| Divot or notch where the hole closes | Lead-out, or the arc lingering at the end | No lead-out; try a slower hole feed; check pause at end = 0 |
| Holes oval in one direction | Lost steps or play in X or Y; a loose coupler | [Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}}) (coupler Sharpie test; carriage preload) |
| Parts wrong size along a long dimension | Machine accuracy limit, or not square | Langmuir rates 0.002 in / 12 in; [Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}}) |

## Where sources disagree (and the starting choice)

- **Expected X45 kerf.** 72Pony's rule gives about 0.050 in; mechanic416 says at least 0.055 in; Langmuir's example tool uses 0.06 in. These are close. **Starting choice: 0.06 in in SheetCAM, replaced by the measured number** (72Pony's method) for each amps setting.
- **Kerf numbers.**
  - Langmuir example tool: 0.06 in.
  - Thread 31041 (general forum member): 0.045–0.059 in at 45 A.
  - Cletus, thread 20256 (post 7): 0.025 in, 16 ga steel, 30 A, 150 ipm. (His 31 A figure in t/18698/46 is for 16 ga aluminum.)
  - Thread 847 community sheet: 0.021–0.026 in for 0.062 in steel at 28 A.

  These can all be right because kerf shrinks with lower amps and faster speed. Starting choices: **0.06 in at 45 A on 3/16 in**, and **Cletus's 0.025 in at 30 A on 16 ga steel**, then **replace both with your own measurement**.
- **Small-hole feed reduction.** No source turned up in the research. Don't use any percentage until it's tested.

## Sources

- Langmuir, SheetCAM guide (example tool kerf 0.06 in): <https://www.langmuirsystems.com/pages/software-sheetcam>
- Langmuir, CrossFire PRO page and product page (accuracy, resolution): <https://www.langmuirsystems.com/pages/crossfire-pro>, <https://www.langmuirsystems.com/products/crossfire-pro-cnc-plasma-table>
- Langmuir, THC guide (SMART distance; CUTOFF %): <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, Fusion guide (no lead-out with THC): <https://www.langmuirsystems.com/pages/software-fusion>
- Langmuir, consumables and cut problems (wide kerf): <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- Langmuir, SheetCAM post v1.6 (program speed): <https://assets.langmuirsystems.com/firecontrol/posts/FireControl-v1.6.scpost>
- My JRWPC45LH operating manual (amps and kerf, p. 12; it gives no kerf width)
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (kerf and amps): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- SheetCAM plasma manual: <https://www.sheetcam.com/Download/SheetCam%20TNG%20Plasma%20Manual_A4.pdf>
- Forum: <https://forum.langmuirsystems.com/t/20256> (Cletus), <https://forum.langmuirsystems.com/t/31041>, <https://forum.langmuirsystems.com/t/847>
- Forum, experienced members: <https://forum.langmuirsystems.com/t/28035> and <https://forum.langmuirsystems.com/t/12723> (72Pony: kerf), <https://forum.langmuirsystems.com/t/21266> (mechanic416: X45 tip, kerf ≥ 0.055), <https://forum.langmuirsystems.com/t/24586> (TomWS), <https://forum.langmuirsystems.com/t/41575> (ChelanJim), <https://forum.langmuirsystems.com/t/35995> (Holla2040), <https://forum.langmuirsystems.com/t/24105> (toolboy), <https://forum.langmuirsystems.com/t/39953> (richarddbeck83), <https://forum.langmuirsystems.com/t/19097> (jamesdhatch: lead-in), <https://forum.langmuirsystems.com/t/46239> and <https://forum.langmuirsystems.com/t/34970> (Wsidr1), <https://forum.langmuirsystems.com/t/32789> (ChelanJim: holes), <https://forum.langmuirsystems.com/t/36785> (TomWS: drill holes), <https://forum.langmuirsystems.com/t/35951> (toolboy), <https://forum.langmuirsystems.com/t/847> (PWCNC 847/12, 847/28), <https://forum.langmuirsystems.com/t/18698> (Cletus)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will come from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) and be listed here with: Date; Material / thickness; Amps / feed; Kerf measured (top / bottom); 1 in hole measured; Smallest usable hole; Notes.
