---
title: "Pierce Height, Pierce Delay, and Cut Height"
date: 2026-10-28
tags: ["cnc", "plasma", "crossfire-pro", "ihs", "pierce", "sheetcam", "razorweld-45"]
draft: false
weight: 6
lastmod: 2026-10-30T18:30:00-07:00
summary: "Pierce height, pierce delay, and cut height for a CrossFire PRO with IHS, THC, the SheetCAM FireControl post v1.6, and the CUT45 with the X45 torch: how IHS works, starting values, and a ten-pierce test."
series: ["CrossFire PRO procedures"]
series_order: 6
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.**

## Applies to

My CrossFire PRO with IHS standard (a floating-head switch), THC, the SheetCAM FireControl post v1.6, and the Razorweld CUT45 CNC (model JRWPC45LH) with the X45 machine torch on 230 V. Doesn't cover:

- The **Fusion post's** heights (it adds springback in a different way; see Where sources disagree).
- Tables without a powered Z.
- Book pierce delays (including the T45m-format chart reportedly from Jasic, [CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})) as final values. FireControl times the pierce delay from the torch-on command, not from arc-on (Langmuir staff quoted by Greg9504, t/12941/2), so book delays run short. Use them as a lower bound.

## How IHS works with the v1.6 post (so the numbers make sense)

Read straight from `FireControl-v1.6.scpost`:

1. Touch off: the torch goes down fast (100 ipm) until the IHS switch trips, then comes back up slowly (20 ipm) until it releases. That's Z = 0.
2. It goes up another **0.02 in** (the "IHS Backlash" move) and calls that Z = 0 again.
3. It rapids to **pierce height**, fires (M3), and waits for the **pierce delay**.
4. It moves down to **cut height** at the **plunge rate**, then turns the THC on.

The touch-off speeds are fixed in the post. The plunge rate only sets the pierce-to-cut-height move. IHS only runs if you set **pierce height, plunge rate, and cut height** (all non-zero).

The SheetCAM post doesn't subtract springback (the small amount the floating head moves before the switch trips). That's why the official SheetCAM tool uses a **0.08 in** cut height to get the THC guide's **0.060 in** real gap. That explanation is worked out here from the two posts; Langmuir doesn't say it directly.

## Starting values (Langmuir's example SheetCAM tool, "Razorcut 45 w/CrossFire PRO")

| SheetCAM field | Start value | Source |
|---|---|---|
| Pierce height | **0.15 in** | SheetCAM guide example tool; THC guide ("around 0.15 in") |
| Pierce delay | **0.5 s** | SheetCAM guide example tool |
| Plunge rate | **50 ipm** | SheetCAM guide example tool |
| Cut height | **0.08 in** | SheetCAM guide example tool |
| Pause at end of cut | **0** | SheetCAM guide example tool |

My JRWPC45LH operating manual gives **no transfer distance**: it only says "The cutting arc will start when the nozzle is moved closer to the edge of the work piece" (p. 11) and that the arc "will initiate when the torch tip is close enough to the work piece" (p. 13). It also has no pierce height or pierce delay. The Razorcut 45 DI manual (a related but different model) says the pilot arc transfers when the torch is **3–5 mm (0.12–0.20 in)** from the work. 0.15 in is inside that range.

For hand piercing, my manual says to "Hold the torch at an angle to the work piece, pull the trigger to start the arc and slowly rotate it to an upright position" (p. 14). On the CrossFire the torch stays vertical, so the pierce height and delay below do that job instead.

**Corroborated heights.** Two sources agree on the real heights: Langmuir, and the T45m-format chart (origin not confirmed):

- **Cut height, real gap 0.060 in:** Langmuir's THC guide (0.060 in typical), and the T45m-format chart reportedly supplied by Jasic for the CUT45 (torch-to-work **0.06 in** on every row, 26 ga to 3/4 in; [CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})).
- **Pierce height 0.15 in:** Langmuir's SheetCAM example tool and THC guide, and the T45m-format chart (initial pierce height **0.15 in, 250 %** on every row).

That chart's Jasic origin is unconfirmed and its format is Hypertherm's, so this is supporting evidence, not proven X45 data. Still, **0.060 in real cut gap and 0.15 in pierce height are solid starting points.** In SheetCAM the cut height stays **0.08 in**: the v1.6 post doesn't subtract IHS springback, so 0.08 in typed gives about 0.06 in real (see above).

## Steps: dialing in pierce and cut height for one material and thickness

1. Use good consumables and 75 psi ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})), and the amps and speed from [CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}).
2. Make a SheetCAM program with **ten small separate loops**, for example 1 in squares, so you get ten pierces.
3. **Run with the starting values.** Watch each pierce:
   - Does the arc transfer right away?
   - Does molten metal blow back up at the shield?
   - Does the arc drop out before the torch moves?
4. **Look at the shield and nozzle after ten pierces.** Spatter stuck to the tip means the pierce is too low or the delay too long for that thickness. Langmuir lists "pierce height that's too low" as a cause of fast consumable wear.
5. **Thin sheet (16 ga and lighter):** if the arc goes out or FireControl pauses for lost arc right after the pierce, the **delay is too long** (THC guide). Shorten it in small steps (for example 0.1 s at a time) and re-test.
6. **3/16 in:** if the torch starts moving before the plate is pierced through (a blow-back gouge at the start, or a start that isn't cut through), **lengthen the delay** in small steps.
7. **If you get "arc lost" right at the start on any thickness,** the delay may be **shorter than the cutter's pilot-to-cut time**. Lengthen it (THC guide).
8. **If the very first pierce of a job misfires but the rest are fine,** the post has a setting called `firstPierceTime` ("an extra delay added to the first pierce as needed by some machines"). It's 0 by default. Changing it means editing the post file. Keep a copy of the original, and note the change in this page.
9. **Cut height:** leave it at 0.08 in unless you see the problems in [Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}}) (too high: bevel; too low: backside dross and nozzle wear). Change it in 0.01 in steps and record the THC voltage it gives.
10. **Log** `pierce_height_in`, `pierce_delay_s`, and `cut_height_in` for every test.

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

- **Why book pierce delays run short. Langmuir staff, quoted by Greg9504 (long-time forum member)**, t/12941/2: FireControl starts the pierce-delay timer at the torch-on command, not when the arc actually transfers. The time the CUT45 takes to fire eats into the delay. So **set a little longer than a chart says**, and judge by the pierce test (the [test-cut program]({{< relref "/testing/test-cut-program.md" >}}), P1/P2).
- **Check the real height by pausing a cut. ChelanJim**, t/32789/3: space bar to pause, arc off, CUT45 off, then feeler gauge under the torch (full steps in [Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}})). toolboy (long-time forum member), t/28381/41, found the same thing: the software number and the real gap aren't always equal. Measure once per new setup.
- **SMART locks onto the starting height. 72Pony**, t/27956/23: THC samples voltage in the first seconds after IHS. A wrong start height becomes a wrong cut height.
- **Leave Z travel below the zero. ds690 (long-time forum member)**, t/47251: when the tip touches the metal, there should still be about **1/2–3/4 in** of Z travel left. Otherwise Z bottoms out and trips IHS early. Read the generated code if heights look wrong.
- **Blow-back. gamblegarage (long-time forum member)**, t/236: piercing too-thick plate with the torch too low blows molten metal back into the tip and kills it fast. Don't lower the pierce height to save time.
- **Plunge rate. nicaDd (long-time forum member)**, t/21622: at least 50 ipm. This matches Langmuir's example tool.
- **What a FireControl pierce looks like in G-code. TomWS**, t/27189/6, posted this sequence:
  ```
  G38.2 Z-5 F100
  G38.4 Z.5 F20
  G92 Z0
  G0 Z0.15
  M3
  G4 P0.4
  G1 Z0.06 F100
  H1
  ```
  In plain words: probe down, back off until the switch releases, zero Z, rise to the 0.15 pierce height, fire, wait 0.4 s, drop to 0.06 cut height, then THC on. It's an example from his post, not a value to copy. The v1.6 post's sequence is in the section above.
- **Heights from experienced members on other cutters (rough only).**
  - Bigdaddy2166 (Everlast), t/43254/14, 30 A thin steel: pierce height .12, cut height .062, pierce delay ".05–.07" as written.
  - Bigdaddy2166, t/36639/3, 11 ga aluminum at 40 A: pierce .12–.15, delay .7, cut .06.
  - PWCNC (long-time forum member, 2019), t/847/24 and t/847/28: height about .070 in, delays .9–1.0 s on .105–.120 in steel.

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Arc doesn't transfer at the pierce | Pierce height too high; clamp contact; worn electrode | Lower the pierce height toward 0.12 in; clean the clamp spot (THC guide; Razorcut 45 DI manual 3–5 mm, related model; Langmuir consumables) |
| Arc lost right after the pierce on thin sheet | Delay too long, so the arc blows a hole and runs out of metal | Shorter delay (THC guide) |
| Arc-lost pause right at fire on any thickness | Delay shorter than the cutter's start time | Longer delay (THC guide) |
| Blow-back gouge or not pierced through at the start on thicker plate | Delay too short | Longer delay |
| Spatter welded to the shield or nozzle; parts wear fast | Pierce too low | Raise the pierce height (Langmuir consumables) |
| Lost arc at the lead-in | Lead-in crosses itself or another cut | Fix the lead-in (THC guide; [SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})) |
| IHS errors or a false trigger before touching | No slack in the torch lead pulling the floating head; water at the IHS contact | Give the lead slack; dry and grease the contact (Langmuir) |
| Pilot arc held long, then cuts out | Pilot over 2 s | Check height and transfer (Razorweld) |

## Where sources disagree (and the starting choice)

- **Pierce height 0.12 vs. 0.15 in.** Bigdaddy2166 uses .12 on an Everlast. Langmuir and the T45m-format chart both say 0.15. **Starting choice: 0.15.** Bigdaddy's number is from a different cutter.
- **Pierce delay timing.** Book delays (chart or T45m) assume arc-on timing; FireControl times from the command (t/12941/2). **Starting choice: the Razorweld chart's delays plus some margin**, then test.
- **Cut height 0.060 / 0.063 / 0.08 in.** THC guide: a 0.060 in typical gap. Fusion post: 0.063 in cut height plus a 0.020 in springback setting. SheetCAM example: 0.08 in. These all agree once you count springback (0.063 + 0.020 is about 0.08). The T45m-format chart (Hypertherm's Powermax45 format; origin not confirmed) also uses a 0.06 in torch-to-work distance. **Starting choice: 0.08 in in SheetCAM (about 0.060 in real), and 0.063 in Fusion's post as shipped.**
- **Plunge rate 50 vs. 100 ipm.** The SheetCAM guide's text says 100; its example tool screenshot says 50. In the v1.6 post, plunge only sets the short pierce-to-cut move. Starting choice: **50 ipm** (the CUT45-specific example).
- **Pierce height rule.** The Fusion guide says about 2x cut height; the THC guide and SheetCAM example say 0.15 in. These are close (2 x 0.063 = 0.126; 2 x 0.08 = 0.16). The T45m-format chart also uses 0.15 in (250 % of 0.06). **Starting choice: 0.15 in.**
- **Pierce delay.** The Fusion guide says "consult plasma documentation", but neither my JRWPC45LH operating manual nor the Razorcut 45 DI manual gives a **pierce delay**. Community notes from thread 847 include ".001 pierce" and ".3 pierce" for 16 ga and .062 in steel (shorthand; it isn't clear whether that's seconds or height). Hypertherm's T45m delays (0.0–0.9 s by thickness) are for a different torch and run short on Langmuir tables (Greg9504, thread 8193), so they're **a lower bound only**. **Starting choice: Langmuir's 0.5 s, or the Razorweld chart's delay in the [test-cut program]({{< relref "/testing/test-cut-program.md" >}}), then tune by test.**
- **Jasic's posted pierce and cut heights** (thread 44500): a search-result summary suggests they're for Jasic's own CNC torch, not the X45. That hasn't been checked against the full thread. Not used.

## Sources

- Langmuir, SheetCAM guide (example "Razorcut 45 w/CrossFire PRO" tool; plunge note): <https://www.langmuirsystems.com/pages/software-sheetcam>
- Langmuir, SheetCAM post v1.6 (IHS sequence; firstPierceTime): <https://assets.langmuirsystems.com/firecontrol/posts/FireControl-v1.6.scpost>
- Langmuir, THC guide (0.060 in gap; around 0.15 in pierce; lost-arc causes): <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, Fusion guide (pierce about 2x cut height; consult plasma docs; IHS force): <https://www.langmuirsystems.com/pages/software-fusion>
- Langmuir, consumables (pierce too low wears parts): <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- My JRWPC45LH operating manual (arc start, pp. 11 and 13; hand piercing, p. 14; no transfer distance, pierce height, or delay)
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (3–5 mm transfer distance; pilot arc over 2 s): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- T45m-format "Torch Setup" chart reportedly supplied by Jasic for the CUT45 (FSFab, <https://forum.langmuirsystems.com/t/45011>; origin unconfirmed; Hypertherm format): 0.06 in torch-to-work, 0.15 in pierce height ([CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})).
- Forum: <https://forum.langmuirsystems.com/t/8193> (Greg9504: book delays run short), <https://forum.langmuirsystems.com/t/847> (community sheet), <https://forum.langmuirsystems.com/t/44500> (Jasic chart discussion)
- Forum, experienced members: <https://forum.langmuirsystems.com/t/12941> (Greg9504 quoting staff: pierce delay timing), <https://forum.langmuirsystems.com/t/32789> (ChelanJim: pause and measure), <https://forum.langmuirsystems.com/t/28381> (toolboy), <https://forum.langmuirsystems.com/t/27956> (72Pony), <https://forum.langmuirsystems.com/t/47251> (ds690: Z travel), <https://forum.langmuirsystems.com/t/236> (gamblegarage: blow-back), <https://forum.langmuirsystems.com/t/21622> (nicaDd: plunge), <https://forum.langmuirsystems.com/t/27189> (TomWS: G-code sequence), <https://forum.langmuirsystems.com/t/43254> and <https://forum.langmuirsystems.com/t/36639> (Bigdaddy2166), <https://forum.langmuirsystems.com/t/45011> (FSFab: T45m-format chart)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will come from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) and be listed here with: Date; Material / thickness; Amps; Pierce ht; Delay; Cut ht; Pierce result (transfer / blow-back / arc lost); Notes.
