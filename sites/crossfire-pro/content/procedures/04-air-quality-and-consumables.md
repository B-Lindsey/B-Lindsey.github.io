---
title: "Air Supply, Air Quality, and X45 Consumables"
date: 2026-10-28
tags: ["cnc", "plasma", "razorweld-45", "x45", "air", "consumables"]
draft: false
weight: 3
lastmod: 2026-10-30T18:30:00-07:00
summary: "Air pressure, flow, and dryness for the CUT45, plus X45 machine-torch consumable part numbers, inspection, and the order to reassemble them."
series: ["CrossFire PRO procedures"]
series_order: 3
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.** The air chain is my setup; the checks and fixes come from Razorweld, Langmuir, and forum posts.

## Applies to

My Razorweld CUT45 CNC (model JRWPC45LH) on 230 V with the X45 machine torch (25 ft lead, shielded consumables) on a CrossFire PRO. My air chain is: Ingersoll-Rand SS3L3 60-gallon compressor → Ingersoll-Rand D18IN refrigerated dryer → Harbor Freight filter → the CUT45's own rear regulator and filter cup → torch. Doesn't cover:

- Hypertherm consumable advice, SYNC cartridges, and Powermax air specs.
- The J45XC hand torch's drag shield. On the CrossFire, Langmuir says to use the **machine shield**.
- Langmuir's consumables page applies to every cutter. Where it says "check your plasma cutter's manual", my JRWPC45LH operating manual decides. The Razorcut 45 DI manual (a related but different model) is only used where mine is silent, and is labeled.

## Air: the numbers that come from the manufacturer

| Item | Value | Source |
|---|---|---|
| Set pressure | **0.5 MPa (75 psi)** | My JRWPC45LH operating manual, p. 8: "Air Flow Pressure (MPA) 0.5 (75 psi)". It also says "The RazorCut45 air pressure is pre-set" (p. 13) and lists an "Enclosed Air Regulator with preset air pressure" (p. 8). Langmuir lists 75 psi |
| Allowed working range | 0.35–0.55 MPa (about 51–80 psi) | **Not in my manual.** Razorcut 45 DI manual, troubleshooting table (related model) |
| Flow needed | **6.7 CFM** | My JRWPC45LH operating manual: "Air Flow Rate (CFM) 6.70" (p. 8) and "requires a flow rate of 6.7 CFM" (p. 13). Langmuir: "6.7 CFM @ 75 psi" |
| Compressor size for lots of cutting | 1.5–2 x the plasma requirement, so about 10–13.4 CFM (calculated from the manual's ratio) | My JRWPC45LH operating manual, p. 13: "choose a compressor at 1.5 to 2 times the plasma system requirement" |
| Tank draining | At least daily | My JRWPC45LH operating manual, p. 13: "drain the receiver (tank) on the air compressor at least daily" |
| Extra filter | A sub-micronic particulate filter that traps water, "installed close as possible to the air intake of the plasma cutter" | My JRWPC45LH operating manual, p. 13. Its p. 8 lists Razorweld options **50500-12** Sub-Micronic Air Filter and **50505-48** Sub-Micronic Cartridge |
| Post-flow after cutting | "The air flow will continue for 30 seconds to cool the torch head." | My JRWPC45LH operating manual, p. 11 |

## Steps: checking the air system (once, then whenever cut quality drops)

1. **Compressor capacity.** Find the SS3L3's delivered CFM at 90 psi on its nameplate or in the IR manual and compare it to 6.7 CFM (minimum) and 10–13.4 CFM (heavy cutting). **SS3L3 delivered CFM: not yet recorded.**
2. **Dryer capacity.** Find the D18IN's rated SCFM and its inlet temperature limit in the IR manual. The community order of parts (thread 42217) is: aftercooler (if any), then the refrigerated dryer, then the final filter or desiccant stage **last**, closest to the cutter. **D18IN rated SCFM: not yet recorded.**
3. **Order of parts.** Compressor → dryer → Harbor Freight filter → **final filter right at the CUT45 inlet** → CUT45 regulator. The Harbor Freight filter in my chain is a mechanical filter, and Razorweld recommends a water-absorbing submicronic filter close to the cutter, so adding one there is the suggested next step.
4. **Check the pressure while air is flowing.** Put the CUT45 in **gas check** mode. My manual says that while the gas-check light is on, "the machine cannot cut" (p. 9). It doesn't say whether gas check times out; the Razorcut 45 DI manual (related model) says 20 s. Read the CUT45's air pressure gauge while air flows: you want **75 psi** (0.5 MPa, my manual p. 8). My manual calls the built-in regulator "preset" (pp. 8 and 13) and doesn't describe adjusting it, so if the gauge reads low, fix the supply (compressor, hose, filters) first. Don't go over 80 psi (0.55 MPa, the DI manual's upper limit). mechanic416 (thread 20285, long-time forum member) runs 75–80 psi, which agrees. Switch gas check off again before cutting.
5. **Drain daily:** the compressor tank (my manual, p. 13: "at least daily"), the dryer drain if it's manual, the HF filter bowl, and the **CUT45's regulator filter cup**. The Razorcut 45 DI manual lists moisture in the regulator cup as a cause of an intermittent pilot arc.
6. **Moisture check.** Signs of wet air: swirl marks on the cut face (thread 42217), consumables wearing fast (Langmuir), and an intermittent pilot arc (Razorcut 45 DI manual). If you see any of these, check the whole chain before touching cut settings.

## X45 consumables (part numbers from Langmuir, cross-checked with my copy of the torch diagram and my manual)

My JRWPC45LH operating manual, p. 15 ("HYP 45 PARTS"), lists the consumables for the HYP 45 style hand torch that came with the cutter (UBHY45-6CC13, 19 ft). The electrode, swirl ring, nozzle, retaining cap, and machine shield numbers are the same ones used on the X45, so the manual backs up the numbers below. Its "Cross Reference" column (220669, 220670, 220671, 220673, 220674) looks like Hypertherm Powermax45-style numbering; the manual doesn't say, and I haven't checked them.

| Diagram # | Part | Langmuir part no. | Torch diagram says | Notes |
|---|---|---|---|---|
| 1a | O-ring (on the torch head) | — | O-ring | Not sold as an X45 consumable on Langmuir's pages; check that it's there and undamaged |
| 3 | Electrode | RW52574 (5-pack) | 52574 | Replace with the nozzle. My manual p. 15: "Cutting Electrodes RW52574" |
| 4 | Swirl ring | RW60041 | 60041 | Replace if cracked, burned, or it won't seat. My manual p. 15: "Swirl Ring RW60041" |
| 5 | Nozzle (cutting tip) | RW51206 (5-pack) | 51206, "cutting tip 20–50 amp" | Replace when the hole is oval or oversized, or spatter is stuck to it. My manual p. 15: "Cutting Nozzle RW51206" |
| 6 | Retaining cap (cup) | Listed by Langmuir as RW603505T | 60305T | **Razorweld's number is RW60305T** (my manual p. 15: "RW60305T End Retaining Cap"). Order it from Langmuir's X45 retaining cap page (see Where sources disagree). **Don't overtighten** |
| 7 | Machine (CNC) shield | RW51924 | 51924 | Use this one on the CrossFire. My manual p. 11: "the outside shield Part no# 51924 is to be used with the system"; p. 15: "End Shield-Machine RW51924". (RW51923 is the hand-torch end shield.) |
| 9 | Ohmic retaining cup | — | "Omic retaing cup" | Not used. My PRO senses height with the IHS switch in the Z axis, not ohmic sensing |

My copy of the diagram is titled "TM70 or X45 CNC torch", with an STM-70 torch head. It lists #1 torch head, #2 torch tube, and #8 torch tube with rack; those are torch body parts, not consumables.

## Steps: changing consumables (order from the X45 torch diagram)

**Before you start:** turn the CUT45 **off** and let the torch cool. Follow my JRWPC45LH operating manual's safety section (pp. 4–6): "Disconnect power source before performing any service or repairs" and "Allow a cooling period before working on the plasma torch" (pp. 4–5).

1. **Take it apart, from the outside in:** CNC shield (#7), retaining cup (#6), cutting tip (#5), swirl ring (#4), electrode (#3).
2. **Inspect.** Langmuir: "Worn consumables cause most cut-quality problems. Check them before you change any settings."
   - **Nozzle:** look at the orifice. Replace it if it's oval, oversized, or has spatter stuck to it.
   - **Electrode:** Langmuir says to replace it when the center pit is "about 1/16" deep on most systems", and to check the plasma cutter manual for the exact limit. My JRWPC45LH operating manual gives **no depth**: the insert "develops a pit in the end of the electrode, when the pit becomes too much poor quality cuts will result and necessitate replacement of the electrode" (p. 12). Use 1/16 in until Razorweld says otherwise.
   - **Swirl ring:** replace it if it's cracked or burned.
   - **O-ring (#1a)** on the torch head: make sure it's in place and not cut.
3. **Change the nozzle and electrode as a pair.** A new nozzle on a worn electrode wears out quickly (Langmuir).
4. **Put it back together, from the torch head outward:** O-ring (#1a) checked → **electrode (#3)** → **swirl ring (#4)**, fully seated → **cutting tip (#5)** → **retaining cup (#6)** → **CNC shield (#7)**.
5. **Retaining cup: snug, not as tight as possible.** Langmuir PRO troubleshooting: an overtightened X45 cap can stop the electrode moving, so the torch won't fire a pilot arc.
6. **Torch in the mount:** tighten the Machine Torch Mount's 4 stainless screws only enough that the torch doesn't spin. Overtightening can squeeze internal parts and cause misfires (Langmuir PRO assembly).
7. **Leave slack in the torch lead.** Without slack the IHS gets pulled and errors out (Langmuir).
8. **Run the gas check** and confirm 75 psi at the cutter (air steps above). Then make a short test cut before a real job.
9. **Write down the change** in the results table below. Reset the running pierce count in the `consumables_pierce_count` column of the test-cut log. Count pierces (one per cut loop) from your programs and keep a running total between changes.

## How to make consumables last

From Langmuir:

- Keep the air clean and dry.
- Use the correct pierce height. Too low wears parts.
- Don't fire the torch in open air.
- Use THC.
- Change nozzle and electrode together.

From Razorweld:

- Keep the air clean and dry: "clean dry air gives longer parts life" and "We recommend use of a Plasma Air Filter" (my JRWPC45LH operating manual, p. 7).
- Use the right tip for the amps; a tip run above its rating will "blow out and distort the tip orifice" (my manual, p. 12).
- Don't hold the pilot arc without cutting. Pilot arc over 2 s causes problems (Razorcut 45 DI manual, related model; my manual doesn't give a time).

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

**Air**

- **TomWS**, t/27875/8 and t/10443/54: "#1 plenty of very dry air, then quality consumables".
- **Check pressure while cutting, not just at rest.**
  - Bigdaddy2166 (Everlast), t/43254/14: 75 psi at the machine while cutting.
  - richarddbeck83 (Everlast), t/43254/26: pressure can collapse right after the pierce. He fixed his with a high-flow regulator and 1/2 in hose.
  - 72Pony (CUT60), t/46610/17: use the cutter's air test to check both static and flowing pressure. It should hold 70+ psi.
  - **Suggested:** watch the CUT45 gauge during a long cut. If it drops below the DI manual's 0.35 MPa (51 psi) range (my manual gives no lower limit), fix the supply. Don't just raise the setting.
- **Compressor about to kick on. Wsidr1**, t/35218/5: force the compressor on before a long cut so it doesn't cycle mid-pierce.
- **Compressor size.**
  - langmuir-daniel (staff), t/236: a 110 V, 26 gal compressor got him by on Razorwelds (5.6 cfm at 90 psi).
  - shaunlb, t/236: Langmuir told him 6 cfm at 90 psi.
  - ChelanJim, t/41575/4: 6 CFM at 90 psi, dry.
  - These are all just under my manual's 6.7 CFM (p. 13). **Size the air supply to the manual.**
- **The CUT45 regulator bowl drains itself. mechanic416 (long-time forum member)**, t/22679.
  - It's an auto-bleeder that should close at about 40 psi.
  - Air leaking from the drain means dirt is holding the valve open. Clean it.
  - A compressor over 135 psi can crack the bowl.
  - Phillipw: a leak isn't normal.
- **toolboy (long-time forum member; Everlast)**, t/28381/41:
  - 3/8 in air line minimum.
  - Watch the desiccant color.
  - Drain the tank.
  - Let the post-flow run (he says 30 s or more) before shutting off, so the torch cools. My manual agrees on the time: after you release the trigger, "The air flow will continue for 30 seconds to cool the torch head" (p. 11). Don't cut power or air right after a job.
- **Aftercooler. brownfox (long-time forum member)**, t/8504/1: an aftercooler ahead of the dryer cuts the water load.
- **Dryer placement. gamblegarage**, t/236: put the dryer close to the cutter.

**Consumables**

- **Use the full matched stack from one maker. mechanic416 (long-time forum member)**, t/25275/61: electrode, tip, swirl ring, retaining cup, and shield. Mixing brands caused misfires. He also got poor cuts on low supply voltage (200 V).
- **The X45 tip. mechanic416**, t/21266:
  - 1.0 mm, rated 45–50 A, **0.040 in orifice**.
  - It's the only tip offered for that torch.
  - Kerf at least 0.055 in.
  - toolboy (same thread) cuts 1/4 in down to 24 ga with it.
- **How long a set lasts. ChelanJim (Hypertherm 45XP)**, t/32592/1, quoting **Hypertherm**:
  - About 2–3 hours of arc-on time hand cutting, **3–5 hours machine cutting.**
  - In machine cutting the electrode usually wears out first.
  - That's a Hypertherm figure for a different torch, so **it's a rough expectation, not an X45 spec.**
- **Spares and stacking. ChelanJim**, t/37146/1:
  - Keep about half a dozen nozzle and electrode sets, plus swirl rings.
  - Never use knock-offs.
  - Keep a chart of how the stack goes together (the torch diagram does this).
- **Replace parts before they ruin a job. TomWS**, t/30637/6. Bigdaddy2166, t/43254/14: new, genuine consumables (not knock-offs).
- **What kills tips. gamblegarage (long-time forum member)**, t/236:
  - Long pilot-arc time.
  - Wet air.
  - Wrong cut height.
  - Piercing too-thick plate with the torch low (molten blow-back).
  - Running more amps than the orifice is made for.

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Consumables wear out fast | Water or oil in the air; pierce height too low; firing in open air | Fix the air chain; pierce height ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})) (Langmuir) |
| Pilot arc cuts in and out | Moisture or dirt in the air; pressure too high; pilot arc over 2 s; worn parts | Drain the regulator cup; set 0.35–0.55 MPa; replace consumables (Razorcut 45 DI manual) |
| Torch won't fire a pilot arc | Retaining cap too tight; worn electrode; debris in the electrode spring | Loosen the cap slightly; replace parts; work the spring (Langmuir PRO troubleshooting, THC guide) |
| No pilot arc at all | Cutter left in gas check mode | Switch gas check off; the machine "cannot cut" while the gas-check light is on (my manual, p. 9). The DI manual (related model) says it times out after 20 s; mine doesn't say |
| Torch protection light on; won't cut | Consumables not seated, or torch head shorted | Power off, reseat the consumables (my manual, p. 9: it lights "when the consumable parts of the machine are not well installed or the torch head is shorted") |
| Wide or wandering kerf | Worn nozzle; low air pressure | Replace the nozzle; check the regulator (Langmuir) |
| Swirl marks on the cut face | Moisture | Drain, dryer, final filter (thread 42217) |
| Marks on the tip | Often pilot-arc strikes | Check pierce height and the arc-start sequence (thread 44335) |
| Bevel and extra dross on parts that used to be clean | Worn nozzle | Replace the nozzle and electrode (Langmuir) |

## Where sources disagree (and the starting choice)

- **Air pressure 75 vs. 85 psi.** Beefmaster (t/22679#5) says Razorweld phone support told him 85 psi. My JRWPC45LH operating manual says 0.5 MPa (75 psi) (p. 8), the Razorcut 45 DI manual says 75 psi with 51–80 psi allowed, and Langmuir says 75. **Starting choice: 75 psi** (written manufacturer data beats a second-hand phone call). If you try higher, keep it under 80.
- **Air flow.** My JRWPC45LH operating manual says 6.70 CFM (p. 8) and 6.7 CFM (p. 13), the Razorcut 45 DI manual says 190 L/min, and Langmuir says 6.7 CFM. Those match. The J45XC torch sheet lists 100 L/min (3.55 cfm), but that's the hand torch. **Size the air to 6.7 CFM** (the whole cutter's requirement, from my manual).
- **Air pressure.** J45XC sheet: 65–75 psi. Razorcut 45 DI manual: 75 psi set, 51–80 psi allowed. mechanic416: 75–80 psi. **Starting choice: 75 psi.** That's my manual (p. 8), the DI manual, and Langmuir agreeing, and it stays inside every range listed.
- **How long consumables last.** There's no Razorweld or Langmuir figure. ChelanJim quotes Hypertherm: **3–5 h of arc-on time machine cutting** (t/32592/1). Thread 44335 quotes 600–900 pierces for a Powermax45. Both are Hypertherm numbers for a different torch. **Use 3–5 h only as a rough expectation, and track your own arc-on time and pierce counts.**
- **Tip amp rating and size.** My copy of the torch diagram labels the 51206 cutting tip **"20–50 amp"**. That covers the CUT45's full 20–45 A range on 230 V, so it should be fine at 45 A. **Orifice size:** mechanic416 (long-time forum member, t/21266) says the X45 tip is **1.0 mm (0.040 in), 45–50 A**, the only tip offered. My JRWPC45LH operating manual's general advice is "a tip with a 3/64\" orifice is good for 0-40 amps whereas a 1/16\" orifice is better for 40-80 amps" (p. 12); the Razorcut 45 DI manual's says 1.0 mm for 0–40 A. Those are general rules, not the X45 tip's size, and neither Razorweld nor Langmuir states the X45 orifice. **Working answer: 1.0 mm / 0.040 in** (community, but it agrees with the diagram's 20–50 A rating). Worth confirming with Razorweld if it ever matters.
- **Retaining cup part number (settled by my manual).** My JRWPC45LH operating manual lists **"RW60305T End Retaining Cap"** (p. 15). Razorweld's JRWPC45LH torch-parts sheet and my copy of the X45 torch diagram say the same (60305T). Langmuir's X45 retaining cap listing shows **RW603505T**, which looks like a typo in the listing. **Razorweld's part number is RW60305T.** When ordering from Langmuir, order from their X45 retaining cap page (link in Sources) rather than by typing either number into a search.

## Sources

- My JRWPC45LH operating manual (Razorweld/Jasic Technologies America; my printed copy): air pressure and flow (p. 8, p. 13), compressor sizing, tank draining and filter (p. 13), post-flow (p. 11), gas check and torch protection lights (p. 9), tip and electrode wear (pp. 7, 12), consumable part numbers (pp. 11, 15). - Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (used only where my manual is silent: pressure range, gas check time-out, pilot arc over 2 s, troubleshooting table): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- Razorweld JRWPC45LH HY1 torch parts sheet (hand torch for my model; RW51206, RW52574, RW60041, RW60305T): <https://razorweld.com/wp-content/uploads/2017/02/HYP45_parts.pdf>
- Razorweld J45XC torch sheet (hand-torch air figure; a hand torch published alongside the Razorcut 45 DI manual, not my X45 machine torch): <https://razorweld.com/wp-content/uploads/2022/11/J45XC-TORCH-diagram.pdf>
- Langmuir, plasma cutters ("Razorweld Razorcut 45": 6.7 CFM @ 75 psi): <https://www.langmuirsystems.com/pages/plasma-cutters>
- Langmuir, consumables and cut problems: <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- Langmuir, X45 parts: <https://www.langmuirsystems.com/products/razorweld-x45-consumable-electrode>, <https://www.langmuirsystems.com/products/razorweld-x45-consumable-nozzle>, <https://www.langmuirsystems.com/products/razorweld-x45-consumable-swirl-ring>, <https://www.langmuirsystems.com/products/razorweld-x45-consumable-retaining-cap>, <https://www.langmuirsystems.com/products/razorweld-x45-consumable-machine-shield>
- Langmuir, X45 machine torch: <https://www.langmuirsystems.com/products/razorweld-x45-machine-torch>
- Langmuir, Machine Torch Mount: <https://www.langmuirsystems.com/products/crossfire-crossfire-pro-machine-torch-mount>
- Langmuir, PRO troubleshooting (X45 retaining cap): <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, PRO assembly (torch mount tightening, lead slack): <https://www.langmuirsystems.com/pages/pro-assembly>
- Langmuir, THC guide (misfire causes): <https://www.langmuirsystems.com/pages/thc-guide>
- My own copy of a torch diagram, "TM70 or X45 CNC torch" (STM-70 head): parts order and the "20–50 amp" tip rating. Where it came from isn't recorded, so it isn't posted here. Razorweld's J45XC torch sheet (above) is the published Razorweld torch document.
- Forum: <https://forum.langmuirsystems.com/t/20285> (mechanic416), <https://forum.langmuirsystems.com/t/42217> (moisture, dryer order), <https://forum.langmuirsystems.com/t/44335> (tip marks; Powermax pierce counts), <https://forum.langmuirsystems.com/t/22679> (CUT45 water-separator leak; Beefmaster's 85 psi report, #5)
- Forum, experienced members: <https://forum.langmuirsystems.com/t/27875> and <https://forum.langmuirsystems.com/t/10443> (TomWS: air first), <https://forum.langmuirsystems.com/t/30637> (TomWS: replace before they ruin a job), <https://forum.langmuirsystems.com/t/43254> (Bigdaddy2166, richarddbeck83: pressure while cutting), <https://forum.langmuirsystems.com/t/46610> (72Pony: air test), <https://forum.langmuirsystems.com/t/35218> (Wsidr1), <https://forum.langmuirsystems.com/t/236> (langmuir-daniel, shaunlb, gamblegarage), <https://forum.langmuirsystems.com/t/41575> (ChelanJim), <https://forum.langmuirsystems.com/t/22679> (mechanic416: auto-drain bowl; 85 psi report), <https://forum.langmuirsystems.com/t/28381> (toolboy), <https://forum.langmuirsystems.com/t/8504> (brownfox: aftercooler), <https://forum.langmuirsystems.com/t/25275> (mechanic416: matched stack), <https://forum.langmuirsystems.com/t/21266> (mechanic416: X45 1.0 mm tip), <https://forum.langmuirsystems.com/t/32592> and <https://forum.langmuirsystems.com/t/37146> (ChelanJim: life, spares)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will come from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) and be listed here with: Date changed; Part(s) changed; Pierces since last change; Why changed (oval tip / pit / quality); Air notes (psi, water in bowls).
