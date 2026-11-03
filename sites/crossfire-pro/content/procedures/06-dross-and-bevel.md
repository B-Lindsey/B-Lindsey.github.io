---
title: "Getting Rid of Dross and Bevel"
date: 2026-10-28
tags: ["cnc", "plasma", "razorweld-45", "x45", "dross", "bevel", "cut-quality"]
draft: false
weight: 5
lastmod: 2026-10-30T18:30:00-07:00
summary: "Fixing dross and bevel on a CrossFire PRO with the CUT45 and X45 torch, in order from cheapest and most likely: consumables, air, torch square, height, speed, amps, cut direction, material."
series: ["CrossFire PRO procedures"]
series_order: 5
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.**

## Applies to

My CrossFire PRO with THC, the Razorweld CUT45 CNC (model JRWPC45LH) on 230 V, and the X45 machine torch with the machine shield. Mild steel, stainless, and aluminum, mostly 3/16 in and thinner. Doesn't cover: Hypertherm "cut-quality" guides that depend on Hypertherm cut charts and swirl direction, and the J45XC hand-torch drag technique.

## Order to work in (cheapest and most likely first)

Langmuir: "Worn consumables cause most cut-quality problems. Check them before you change any settings." So:

1. **Consumables.** Look at the nozzle orifice (oval, oversized, spatter) and the electrode pit. If in doubt, replace both ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})).
2. **Air.** 75 psi set during gas check, drains emptied, no water at the cutter ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})).
3. **Torch square to the table.** Check the torch is vertical in both X and Y with a small square against the torch body and the slats. If it isn't, follow Langmuir's Z-axis tram video (5/32 hex and 7/16 wrench). My JRWPC45LH operating manual: a tilted torch gives "Unequal bevel, one side may be excessively beveled" (p. 12).
4. **Torch height.**
   - My manual: too high gives "Excessive bevel, plasma stream may not cut all the way through the material"; too low gives "Reverse bevel" and the tip may short out or be damaged (p. 12). It gives no height number.
   - Langmuir THC guide: too close gives "more backside dross" and nozzle wear.
   - The target gap is about **0.060 in** (THC guide). In SheetCAM that's a **0.08 in** cut height ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}}) explains why). Make sure THC is on for anything bigger than about 15 x 15 in, or any warped sheet ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
5. **Speed.** Run the speed ladder from [CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}).
   - Heavy bottom dross: too slow.
   - Small hard beads, or spatter on top: too fast.
6. **Amps.** Thin sheet: lower the amps until the cut is cleanest (my manual, p. 12: "On thinner material, you need to turn down the amperage"). 3/16 in: full 45 A and adjust speed.
7. **Cut direction (which side gets the bevel).** My manual: "The plasma stream swirls as it exits the tip, biting one side and finishing off on the other leaving a bevelled edge and a straight edge… you want the straight side of the cut to be on the finished piece you keep" (p. 12).
   - **Test:** cut a 2 x 2 in square and a 1 in hole in 3/16 mild. Check the part's outside edge and the hole edge with a square.
   - If the part edge is the bevelled one, reverse the cut direction for outside profiles in SheetCAM. Make the inside profiles (holes) go the opposite way to the outside profiles.
   - Neither Langmuir nor Razorweld says which direction the X45 swirls, so **this test is the only way to know**.
8. **Material.** Stainless and aluminum act differently from mild steel. My manual: "The faster you move (especially on aluminium), the cleaner your cut will be" (p. 12). Dial in each one separately ([CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})).

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

- **Measure the real standoff by pausing a cut. ChelanJim (Hypertherm 45XP)**, t/32789/3. It adds a direct check that the other sources don't give.
  1. Start a long straight cut on scrap.
  2. Partway through, press the **space bar** to pause.
  3. Wait for the arc and post-flow to stop. **Switch the CUT45 off** before reaching under the torch (added here; not in the original post).
  4. Slide a feeler gauge under the torch and measure the real gap.
  5. Compare it with 0.060 in.
  - ChelanJim found his real height was too high and lowered his post's cut height from 0.06 to 0.022. That's his machine and post; **don't copy the number. Measure your own.**
- **Bottom dross on straight cuts.** Three experienced forum members agree on the usual causes:
  - ChelanJim, t/32789/3: cut height too high, amps too low, or speed too fast.
  - Bigdaddy2166 (Everlast), t/48287/5: torch too high, worn-out consumables, or too slow.
  - Speed and amps are in Razorweld's and Langmuir's tables too. Experienced members add **torch height**, so check it first (pause-and-measure above).
- **Bevel that returns on parts that were clean. ChelanJim**, t/32789/3: an enlarged (but still round) nozzle orifice. Swap the electrode and nozzle together.
- **Dross only in small radii and holes. ChelanJim**, t/32107/16 and t/32789/3. The machine slows in tight curves, so the cut gets too slow there. Without Fusion's Feed Optimization, or an equivalent in SheetCAM, he says you get poor hole completion ([Kerf width and hole/part accuracy]({{< relref "/procedures/08-kerf-and-hole-accuracy.md" >}})).
- **Cut direction. toolboy (long-time forum member; Everlast)**, t/28381/41: outside cuts clockwise, inside cuts counter-clockwise, so the good edge is on the part. Check this with a bevel test on your own torch.
- **Measure the actual height. toolboy**, t/28381/41: his software setting and his real 0.06 in gap weren't the same number. Same lesson as ChelanJim's.
- **Chipping dross off. Wsidr1**, t/46239/8: chip it at a shallow angle.
- **Aluminum spatter. Bigdaddy2166**, t/36639/3: MIG nozzle anti-spatter gel on the shield.
- **Torch height limit. mechanic416 (long-time forum member)**, t/20285: 75–80 psi and a height no more than .060 in (already covered above).

## Symptoms -> causes -> fixes

| What you see | Likely cause | Fix (source) |
|---|---|---|
| Heavy, bubbly dross stuck on the bottom; arc goes straight down | Too slow | Raise the feed (Razorweld; Langmuir) |
| Small, hard beads on the bottom; sparks spray up; may not cut through | Too fast, or not enough amps | Slow down or raise the amps (Razorweld; Langmuir) |
| More dross than usual on a setting that used to work | Worn nozzle | Replace the nozzle and electrode (Langmuir) |
| More backside dross along with fast nozzle wear | Torch too close | Check the cut height and THC (THC guide) |
| Bevel on all edges, worse on thicker plate | Torch too high, wrong speed, or worn nozzle | Height, speed ladder, new nozzle (Razorweld; Langmuir) |
| Bevel on one side only, the same everywhere | Torch tilted | Square the torch; Z tram video (Razorweld; Langmuir) |
| Bevel on the part side, straight on the scrap side | Cut direction reversed for that swirl | Reverse the direction in SheetCAM (Razorweld) |
| Bevel that comes and goes on a big sheet | Plate warping, height changing | THC on; check THC settings (Langmuir) |
| Swirl marks or rough face | Moisture in the air | [Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}}) (thread 42217) |
| Dross only at the start of each cut | Pierce height or delay | [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}}) |

Community agreement: mechanic416 (thread 20285) lists the same dross causes: too slow, standoff too high, worn parts, wrong amps. He keeps the torch height at or under 0.060 in for cutters up to 60 A.

## Where sources disagree (and the starting choice)

- **ChelanJim's 0.022 in post cut height vs. Langmuir's 0.060 in gap.** ChelanJim's number was a correction for his own machine reading high; it isn't a new target. **Keep Langmuir's 0.060 in real gap as the target** and use his pause-and-measure method to check it.
- **Cut height: 0.060 vs. 0.080 in.** Not a real conflict. 0.060 in is the actual gap (THC guide; mechanic416). SheetCAM's 0.08 in setting includes IHS springback ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). Both are right; use **0.08 in in SheetCAM**.
- **Community thin-steel heights of 0.065–0.075 in** (community sheet and PWCNC, thread 847; PWCNC's posts are 847/12, 847/24, and 847/28). It isn't clear whether these are the real gap or the CAM setting. If they're the CAM setting, they're lower than Langmuir's 0.08. Start at Langmuir's numbers and test.

## Safety

See the safety links in [CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}). Never cut coated, painted, oily, or galvanized stock without following Langmuir's safety page and the material's MSDS.

## Sources

- My JRWPC45LH operating manual, cutting procedure and techniques (amperage, speed, direction, torch height and tilt), pp. 11–12
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH), "Plasma cutting tips & techniques" (same advice as mine): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- Langmuir, consumables and cut problems: <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- Langmuir, THC guide (0.060 in gap; too close means more backside dross): <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, PRO assembly / troubleshooting (Z tram video): <https://www.langmuirsystems.com/pages/pro-assembly>, <https://www.youtube.com/watch?v=xCbOJz-zfl8>
- Langmuir, Safety: <https://www.langmuirsystems.com/pages/safety>
- Forum: <https://forum.langmuirsystems.com/t/20285> (mechanic416), <https://forum.langmuirsystems.com/t/847> (thin-steel heights), <https://forum.langmuirsystems.com/t/42217> (moisture)
- Forum, experienced members: <https://forum.langmuirsystems.com/t/32789> (ChelanJim: pause and measure; dross causes; bevel), <https://forum.langmuirsystems.com/t/32107> (ChelanJim: small radii), <https://forum.langmuirsystems.com/t/48287> (Bigdaddy2166: dross), <https://forum.langmuirsystems.com/t/28381> (toolboy: cut direction, real height), <https://forum.langmuirsystems.com/t/46239> (Wsidr1: dross chipping), <https://forum.langmuirsystems.com/t/36639> (Bigdaddy2166: anti-spatter gel)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will come from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) (`result_dross`, `result_bevel` columns) and be listed here with: Date; Material / thickness; Change made; Dross before → after; Bevel before → after; Cut direction that keeps the part square.
