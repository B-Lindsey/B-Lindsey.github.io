---
title: "CUT45 (X45 Torch) Cut Settings"
date: 2026-10-28
tags: ["cnc", "plasma", "razorweld-45", "x45", "cut-chart", "settings"]
draft: false
weight: 4
lastmod: 2026-10-30T18:30:00-07:00
summary: "Starting cut settings for the CUT45 with the X45 machine torch: the Razorweld-supplied chart, a T45m-format chart reportedly from Jasic, the manual's table, forum numbers, and how to dial them in."
series: ["CrossFire PRO procedures"]
series_order: 4
---

{{< lastupdated >}}

**Status: Razorweld chart settings used by me, not formally tested. Everything else on this page is compiled research, not yet tried.**

## Applies to

My Razorweld CUT45 CNC (model JRWPC45LH) on **230 V** (20–45 A; my JRWPC45LH operating manual, p. 8, gives the supply as "230v - 1 +/- 15%", so it's a 230 V single-phase machine, and the 120 V figures in the Razorcut 45 DI manual are for that dual-voltage model) with the X45 machine torch, the 51206 "20–50 amp" tip, and the machine shield, on a CrossFire PRO with IHS and THC (300 ipm max). Materials: mild steel, stainless, and aluminum, mostly 3/16 in and thinner. Doesn't cover:

- Hypertherm, Everlast, and Primeweld charts as settings. The T45m-format chart below is in, because FSFab reports Jasic supplied it for the CUT45. Numbers from experienced members on other cutters (Everlast, PrimeWeld CUT60, Hypertherm) are rough guides only.
- The "Razorcut 45 chart" in forum thread 10695 (since removed from the forum), which a long-time forum member says is for the **older IPT-style torch**.
- Any 120 V figures.

<figure class="chart-figure"><a href="{{< relurl "images/x45-cnc-torch-diagram.jpg" >}}"><img src="{{< relurl "images/x45-cnc-torch-diagram.jpg" >}}" alt="TM70 / X45 CNC torch exploded parts diagram: 52574 electrode, 60041 swirl ring, 51206 cutting tip 20-50 amp, 60305T retaining cup, 51924 CNC shield" loading="lazy"></a><figcaption>TM70 / X45 CNC torch parts diagram: 52574 electrode, 60041 swirl ring, 51206 cutting tip (20–50 A), 60305T retaining cup, 51924 CNC shield. Tap to enlarge.</figcaption></figure>

I couldn't find an **X45 machine-torch cut chart published by Langmuir** (Langmuir pages checked in 2026; thread 11738). My starting chart is **manufacturer data that came via the forum**: Razorweld sent it to forum member **MO-Hacker**, who posted it on 2019-09-20: "Here is the cut chart that Razorweld sent me for the 45" (<https://forum.langmuirsystems.com/t/847/29>). PWCNC (t/847/45) and TinWhisperer (t/21266/8) reposted it. I've cut with these settings and they worked well, but **they haven't been formally tested on my machine yet.** The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) is the plan for that.

## Which Razorweld manual applies

My cutter is the **Razorweld CUT45 CNC, model JRWPC45LH** ("CNC - CROSSFIRE COMPATIBLE" on the manual cover, built by Jasic). **My JRWPC45LH operating manual is the one that applies.** I couldn't find it online, so this site cites my printed copy by its printed page numbers.

Langmuir sells the cutter as the "Razorweld Razorcut 45 with Machine Torch", and Langmuir's Reference page links the **Razorcut 45 DI** manual (2022) under that name. That DI manual is for a **related but different model**: it's dual-voltage (120/230 V), lists 25 % duty cycle, and has error codes and a Mesh mode. My manual has none of those: it's 230 V only and 30 % at 45 A (p. 8), shows only 2T and 4T (pp. 9–10), and uses indicator lights instead of error codes (p. 9). It also has none of the DI manual's residential-supply warning.

Notes on my manual:

- It has **no cut chart or speed table**, no torch height, and no pierce delay. The Razorweld-supplied chart below is still my starting point for machine settings.
- It looks adapted from the sister model's manual (**JRWPC45LT**, same CUT45 machine with a hand torch). Its Contents page (p. 3) still says "TRF-45-6-CC1 Plasma Torch Parts Breakdown" and "JRWPC45LT Machine spare parts", and its trigger safety note (p. 14) names a "Suregrip TRF-45-6-CC1 torch". The rest of it, including the tech data, panel, parts list, and CNC port notes, is for the JRWPC45LH.
- The Contents page numbers for parts and warranty are off by one or two (the parts list is on p. 18; the warranty is pp. 19–21).

Figures from the DI manual are still used on this page only where my manual is silent, and they're labeled as such.

<figure class="chart-figure"><a href="{{< relurl "images/jrwpc45lh-manual-cover.jpg" >}}"><img src="{{< relurl "images/jrwpc45lh-manual-cover.jpg" >}}" alt="Cover of my Razorweld operating manual, model JRWPC45LH, CNC CrossFire compatible, showing the CUT45 unit with Jasic badge" loading="lazy" style="max-width:420px"></a><figcaption>Cover of my printed manual: Razorweld JRWPC45LH, &ldquo;CNC &ndash; CrossFire compatible.&rdquo; Tap to enlarge.</figcaption></figure>

How sources are weighted on this page:

1. **Langmuir docs and staff:** heights, THC, and machine limits.
2. **Razorweld data:** my JRWPC45LH operating manual (machine specs, panel, air, tips and techniques; no cut chart), **this Razorweld-supplied chart (Razorweld to MO-Hacker)**, and the Razorcut 45 DI manual (a related but different model; a rough hand-cutting table, only two thicknesses). For machine settings I start from the chart and use the manuals as a sanity check.
3. **The T45m-format chart reportedly supplied by Jasic** (FSFab, t/45011). It's a second candidate set, to be tested side by side in the [test-cut program]({{< relref "/testing/test-cut-program.md" >}}). Its Jasic origin is unconfirmed.
4. **Experienced forum members**, then everyone else.

Caveats from the forum about the Razorweld chart:

- PWCNC (t/847/30): the CrossFire only goes 300 ipm, and "I still make my own, test cut all material first".
- TinWhisperer (t/21266/8): a good start only; machines vary a lot unit to unit.
- Another 847 poster says its speeds don't suit the CrossFire.
- The chart doesn't name a torch, and it's from 2019. It's assumed here to fit the X45 machine torch; the test-cut program is meant to confirm or reject that.

## Razorweld chart (my starting settings)

**Source:** Razorweld, via forum member MO-Hacker (t/847/29). **Status:** used by me, worked well, not formally tested.

Typed in from my saved image of the chart ([view image](/images/rw_chart.jpeg)) and **checked cell by cell against the forum copy on 28 October 2026: every ipm, voltage, delay, and amps value matches.** **Use the Optimum column** as the starting feed. "Max" is the fastest the chart says will still sever the metal, not a quality speed. ⚠ marks speeds over the PRO's **300 ipm** limit, which the PRO can't reach. "—" means the chart gives no pierce delay.

The chart gives **no cut height, pierce height, air pressure, or kerf**. Use the defaults from [Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}}), [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}}), and [Kerf width and hole/part accuracy]({{< relref "/procedures/08-kerf-and-hole-accuracy.md" >}}) for those: 75 psi, pierce height 0.15 in, cut height 0.08 in in SheetCAM (0.060 in real gap), and kerf measured. The arc voltages are only valid at Razorweld's unstated torch height (see Where sources disagree).

### Mild steel

| Thickness | mm | Amps | Arc V | Pierce delay (s) | Max ipm | **Optimum ipm** | Usable on the PRO? |
|---|---|---|---|---|---|---|---|
| 26 ga | 0.5 | 25 A | 147 | — | **638** ⚠ over 300 | **415** | No: optimum is over 300 ipm |
| 22 ga | 0.8 | 25 A | 148 | — | **500** ⚠ over 300 | **325** | No: optimum is over 300 ipm |
| 18 ga | 1.3 | 25 A | 149 | — | **312** ⚠ over 300 | **203** | Yes (max is over 300; ignore it) |
| 16 ga | 1.5 | 25 A | 152 | — | 178 | **114** | Yes; chart mm/min typo (see oddities) |
| 14 ga | 1.9 | 40 A | 144 | 0.25 | **640** ⚠ over 300 | **221** | Yes (max is over 300; ignore it); max looks wrong (see oddities) |
| 10 ga | 3.4 | 40 A | 146 | 0.50 | 151 | **98** | Yes |
| 3/16 in | 4.7 | 40 A | 147 | 0.75 | 97 | **63** | Yes |
| 1/4 in | 6.4 | 40 A | 149 | 1.00 | 74 | **48** | Yes |

### Stainless steel

| Thickness | mm | Amps | Arc V | Pierce delay (s) | Max ipm | **Optimum ipm** | Usable on the PRO? |
|---|---|---|---|---|---|---|---|
| 26 ga | 0.5 | 25 A | 139 | — | **631** ⚠ over 300 | **410** | No: optimum is over 300 ipm |
| 22 ga | 0.8 | 25 A | 139 | — | **496** ⚠ over 300 | **322** | No: optimum is over 300 ipm; chart mm/min typo (see oddities) |
| 18 ga | 1.3 | 40 A | 142 | 0.25 | **592** ⚠ over 300 | **335** | No: optimum is over 300 ipm |
| 16 ga | 1.5 | 40 A | 144 | 0.25 | **374** ⚠ over 300 | **243** | Yes (max is over 300; ignore it) |
| 14 ga | 1.9 | 40 A | 144 | 0.25 | 221 | **144** | Yes |
| 10 ga | 3.4 | 40 A | 147 | 0.50 | 107 | **70** | Yes |
| 3/16 in | 4.7 | 40 A | 149 | 0.75 | 67 | **44** | Yes |
| 1/4 in | 6.4 | 40 A | 149 | 1.00 | 47 | **31** | Yes |

### Aluminum

| Thickness | mm | Amps | Arc V | Pierce delay (s) | Max ipm | **Optimum ipm** | Usable on the PRO? |
|---|---|---|---|---|---|---|---|
| 1/32 in | 0.8 | 25 A | 150 | — | **610** ⚠ over 300 | **397** | No: optimum is over 300 ipm |
| 1/16 in | 1.5 | 25 A | 152 | — | 266 | **174** | Yes |
| 3/32 in | 2.4 | 40 A | 146 | 0.25 | 293 | **190** | Yes; chart mm/min typo (see oddities) |
| 1/8 in | 3.2 | 40 A | 149 | 0.50 | 204 | **133** | Yes |
| 1/4 in | 6.4 | 40 A | 151 | 1.00 | 78 | **49** | Yes |

Aluminum has **no 3/16 in row** (it jumps from 1/8 to 1/4). Don't average between the rows. Start a 3/16 aluminum ladder from the Razorcut 45 DI manual's 5 mm figure (38 ipm, below; related model) and work up.

### Oddities in the Razorweld chart (check these by test)

1. **Mild steel 14 ga max 640 ipm looks wrong.** On every other row, Optimum is about 0.65 x Max (on stainless 18 ga it's about 0.57). On mild 14 ga it's 221 / 640 = 0.35. Also, 14 ga mild has a higher max than 18 ga mild (312), and stainless 14 ga's max is exactly **221**, the same number as mild 14 ga's optimum. It may be a typing error in Razorweld's original. **Trust the 221 optimum only after a ladder test, and ignore the 640.**
2. **The mm/min columns have typos** that don't match the ipm (ipm x 25.4):
   - stainless 22 ga optimum shows 6179 mm/min, but 322 ipm = 8179;
   - aluminum 3/32 optimum shows 4626, but 190 ipm = 4826;
   - smaller slips on mild 16 ga max, aluminum 1/16 max, 1/8 max, and 1/4 max.

   **Use the ipm columns only.**
3. **The 25 A rows have no pierce delay.** It may mean no delay is needed on thin sheet, or just missing data. The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) plans to test 0, 0.25, and 0.5 s.
4. **No cut height, pierce height, PSI, kerf, or consumable list.** The chart can't be copied whole. Those settings come from the other procedure pages (air, pierce height, kerf).
5. **The chart tops out at 40 A**, though my cutter can do 45 A. Razorweld's rule says full output on thick material (see Where sources disagree).
6. **Amps don't follow thickness the same way in each material.** Stainless jumps to 40 A at 18 ga; mild steel stays at 25 A through 16 ga. That's why stainless 18 ga (335 ipm) is "faster" than mild 18 ga (203 ipm).
7. **Arc voltages are 139–152 V.** That's at or above the top of Langmuir's "typical 60–150 V" (and the THC guide's 90–150 V). It's still inside the flowchart's 85–230 V "in range" and well under the 280 V that can damage the THC. Arc voltage depends on torch height, and the chart doesn't give one.
8. **Thin-sheet rows are mostly out of reach.** Optimum speeds over 300 ipm on mild 26 and 22 ga, stainless 26, 22, and 18 ga, and aluminum 1/32 can't be run on the PRO. Following Razorweld's thin-material rule, the likely fix is lower amps at a reachable speed, found by test. The chart has no such rows.

## Speed table from a related model (Razorcut 45 DI manual, Table 7.1.3)

This table is from the Razorcut 45 DI manual, **not my JRWPC45LH manual**. Mine has no speed or cut table at all; its cutting and tips sections (pp. 11–12) only describe speed by how the sparks and arc look. Razorweld calls it "approximate only". It's in ft/min, with no amps or torch height, and it's from a hand-cutting manual. (Razorweld's CUT45 spec sheet, which covers JRWPC45LT and JRWPC45LH, gives only thick-plate figures: 1/2 in at 18 ipm recommended, 3/4 in at 8 ipm, sever 1 in at 4 ipm.) Converted (x 12):

| Material | 1.0 mm (0.039 in) | 5.0 mm (0.197 in, close to 3/16 in) |
|---|---|---|
| Mild steel | 26 ft/min = **312 ipm** (over 300) | 4 ft/min = **48 ipm** |
| Stainless | 19 ft/min = **228 ipm** | 3.2 ft/min = **38.4 ipm** |
| Aluminum | 19 ft/min = **228 ipm** | 3.2 ft/min = **38.4 ipm** |

## Other forum starting points (weighted below both charts; test before use)

| Material / thickness | Amps | Feed | Other | Who; cutter | Thread |
|---|---|---|---|---|---|
| 16 ga mild steel | 28 A | 72 ipm | ".001 pierce"; height .070–.075 in | community sheet in 847 (general forum members); torch not confirmed | 847 |
| .062 in cold-rolled steel | 28 A | 70 ipm | pierce .3; height .073 in; kerf .021–.026 in | PWCNC, 2019; torch not confirmed | 847/12 |
| .105 in cold-rolled steel | 30 A | 70 ipm best (50 ipm gave back dross) | pierce delay .9; torch .070 in; .8 mm nozzle; water table | PWCNC | 847/24 |
| .120 in cold-rolled steel | 35 A | 70 ipm | pierce delay 1.0 s; height .070 in; 70 psi; kerf .040 in | PWCNC | 847/28 |
| 1/8 in aluminum | — | about 45 ipm | — | community sheet in 847 (general forum members) | 847 |
| Thin steel | 30 A | 110 ipm | pierce delay ".05–.07" (as written); pierce height .12; cut height .062; 75 psi while cutting | Bigdaddy2166; **Everlast**, so rough only | 43254/14 |
| 11 ga aluminum (3000 series) | 40 A | 46 ipm | pierce .12–.15; delay .7; cut .06; 70 psi; 1.2 mm tip | Bigdaddy2166; **Everlast** | 36639/3 |
| 16 ga aluminum | 31 A | 150 ipm | kerf .025 in; "virtually zero dross" | Cletus; **PrimeWeld CUT60** | 18698/46 |
| 16 ga steel | 30 A | 150 ipm | kerf .025 in; "zero dross" | Cletus; **PrimeWeld CUT60** | 20256/7 |
| (thickness not stated in the research summary) | 45 A | — | kerf .045–.059 in | community | 31041 |

Notes:

- The first 847 row comes from shorthand research notes; check the thread before using it. The torch in the 847 posts isn't confirmed, and PWCNC's are 2019 numbers.
- The two Cletus rows are separate posts on different metals (checked against both posts on 30 October 2026).
- Numbers from another cutter (Everlast, CUT60) show the general ballpark only. Amps don't mean the same thing on a different torch.
- The forum also keeps a shared Google Sheet ("Razorweld Cut Chart"; threads 18563 and 8921): <https://docs.google.com/spreadsheets/d/12SPhiHimP9lWIOJTGaHhDAiaQoUz5Hq0YjbL92mMBSo>. Its contents haven't been checked for this site. **Open it and check before using any number from it.**

## T45m-format chart (FSFab reports Jasic supplied it; origin not confirmed)

> **⚠ Voltage conflict, read this first.**
> - **This chart says 111–123 V** for 3/16 in and thinner, at a stated **0.06 in** torch-to-work distance.
> - **The Razorweld chart says 139–152 V**, with no height given.
>
> Row for row, they're about 20–40 V apart. Arc voltage rises as the torch goes up (THC guide; Cletus), so either Razorweld's numbers were taken higher off the plate or one chart is for a different torch. **Don't type either voltage into FireControl as fact.** The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) is planned to test both against SMART voltage, and measure the real torch height, before either is picked.

**Where it comes from.**

- FSFab posted these charts in <https://forum.langmuirsystems.com/t/45011> (2025-08-13). He says **Jasic supplied them for the CUT45 machine torch.** Jasic builds the CUT45.
- He ran the **3/16 in settings** on an XR with a CUT45 machine torch. They cured a "pierces, then torch goes out" problem; he cut three test pieces start to finish.
- Phillipw replied that they're "very close to Hypertherm spec".
- **Origin not confirmed.** FSFab's post says Jasic supplied this chart, but its layout, the "T45m shielded consumables" label, and the 400 ipm test-table footnote match Hypertherm's Powermax45 charts. My saved copies (labeled Razorweld) are identical to the ones in FSFab's thread.

**How it's used here.**

- It's a **second candidate setting set**, no longer reference only. It's weighted below the Razorweld chart (origin unconfirmed; one tester, a general forum member), and above other forum numbers.
- The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) runs its voltage as T2 in every session. There's also an optional session comparing its 45 A, 3/16 mild steel settings against the Razorweld chart.
- **Amps differ:** this chart uses **30 A and 45 A**; the Razorweld chart uses 25 A and 40 A.

**What it agrees on.** Every row uses **0.06 in torch-to-work** and **0.15 in initial pierce height** (250 %). Both match Langmuir's 0.060 in gap and 0.15 in pierce height ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})).

Chart notes:

- Air flow 320 scfh hot / 360 scfh cold.
- "*Maximum cut speed is limited by the test table's maximum speed (400 ipm)." The PRO stops at 300 ipm.
- "Edge start" means the chart recommends starting from the plate edge, not piercing.

### Mild steel (T45m)

| Amps | Thickness | Pierce delay (s) | Rec. ipm | Rec. V | Max ipm | Max V |
|---|---|---|---|---|---|---|
| 30 | 26 ga (0.018) | 0.0 | 360 | 117 | 400* | 118 |
| 30 | 22 ga (0.030) | 0.0 | 340 | 116 | 400* | 117 |
| 30 | 20 ga (0.036) | 0.0 | 320 | 115 | 400* | 117 |
| 30 | 16 ga (0.060) | 0.2 | 225 | 111 | 280 | 115 |
| 45 | 20 ga (0.036) | 0.0 | 380 | 115 | 400* | 112 |
| 45 | 16 ga (0.060) | 0.0 | 350 | 116 | 400* | 115 |
| 45 | 14 ga (0.075) | 0.1 | 280 | 117 | 360 | 115 |
| 45 | 12 ga (0.105) | 0.3 | 190 | 117 | 240 | 115 |
| 45 | 10 ga (0.135) | 0.4 | 140 | 117 | 175 | 115 |
| 45 | 3/16 (0.188) | 0.5 | 85 | 118 | 110 | 115 |
| 45 | 1/4 (0.250) | 0.6 | 60 | 120 | 75 | 116 |
| 45 | 3/8 (0.375) | 0.9 | 32 | 122 | 40 | 116 |
| 45 | 1/2 (0.500) | edge start | 20 | 132 | 25 | 125 |

### Aluminum (T45m)

| Amps | Thickness | Pierce delay (s) | Rec. ipm | Rec. V | Max ipm | Max V |
|---|---|---|---|---|---|---|
| 30 | 26 ga (0.018) | 0.0 | 360 | 117 | 400* | 120 |
| 30 | 16 ga (0.060) | 0.2 | 340 | 118 | 400* | 121 |
| 30 | 14 ga (0.075) | 0.2 | 215 | 118 | 270 | 121 |
| 45 | 16 ga (0.060) | 0.0 | 360 | 116 | 400* | 114 |
| 45 | 14 ga (0.075) | 0.0 | 340 | 117 | 400* | 116 |
| 45 | 12 ga (0.105) | 0.0 | 280 | 120 | 360 | 119 |
| 45 | 10 ga (0.135) | 0.1 | 220 | 122 | 280 | 120 |
| 45 | 3/16 (0.188) | 0.2 | 100 | 123 | 130 | 120 |
| 45 | 1/4 (0.250) | 0.3 | 80 | 123 | 100 | 120 |
| 45 | 3/8 (0.375) | 0.5 | 33 | 130 | 42 | 125 |
| 45 | 1/2 (0.500) | edge start | 20 | 134 | 25 | 130 |
| 45 | 3/4 (0.750) | edge start | 8 | 143 | 10 | 138 |

### Stainless steel (T45m)

| Amps | Thickness | Pierce delay (s) | Rec. ipm | Rec. V | Max ipm | Max V |
|---|---|---|---|---|---|---|
| 30 | 26 ga (0.018) | 0.0 | 360 | 117 | 400* | 123 |
| 30 | 22 ga (0.030) | 0.0 | 340 | 116 | 400* | 121 |
| 30 | 20 ga (0.036) | 0.0 | 320 | 115 | 400* | 119 |
| 30 | 16 ga (0.060) | 0.2 | 145 | 111 | 185 | 118 |
| 45 | 20 ga (0.036) | 0.0 | 300 | 115 | 400* | 109 |
| 45 | 16 ga (0.060) | 0.0 | 320 | 116 | 400* | 125 |
| 45 | 14 ga (0.075) | 0.1 | 280 | 117 | 360 | 115 |
| 45 | 12 ga (0.105) | 0.3 | 160 | 117 | 200 | 116 |
| 45 | 10 ga (0.135) | 0.4 | 120 | 117 | 150 | 118 |
| 45 | 3/16 (0.188) | 0.5 | 70 | 118 | 85 | 118 |
| 45 | 1/4 (0.250) | 0.6 | 44 | 120 | 55 | 120 |
| 45 | 3/8 (0.375) | 0.8 | 30 | 122 | 32 | 121 |
| 45 | 1/2 (0.500) | edge start | 14 | 132 | 18 | 128 |
| 45 | 3/4 (0.750) | edge start | 7 | 140 | 9 | 131 |

### What this does and doesn't change

- **Voltage:** see the warning at the top of this section. The [test-cut program]({{< relref "/testing/test-cut-program.md" >}})'s T1 uses the Razorweld chart's voltage and T2 uses this chart's voltage for the same thickness. For example:
  - 3/16 mild steel: 147 V vs. **118 V**.
  - 16 ga mild steel: 152 V vs. **116 V at 45 A** or **111 V at 30 A**. The amps don't match the Razorweld chart's 25 A.
- **Pierce delays run short on Langmuir tables.** Greg9504 (t/12941/2, also t/8193) quotes Langmuir staff: **FireControl times the pierce delay from the torch-on command, not from arc-on.** Book values like these assume arc-on, so add the time the arc takes to start. **Treat this chart's delays as a minimum.** They're already shorter than the Razorweld chart's: 0.5 vs. 0.75 s on 3/16 mild, 0.1 vs. 0.25 s on 14 ga mild.
- **Speeds:** a real alternative at 45 A, for example 3/16 mild at **85 ipm** vs. the Razorweld chart's 63 ipm at 40 A. Many thin rows are over 300 ipm and can't be reached on the PRO.

## How the sources compare

| Case | Razorweld chart (optimum) | Razorcut 45 DI manual | Others | Verdict |
|---|---|---|---|---|
| Thin mild steel, about 1 mm | 22 ga (0.8 mm) 325; 18 ga (1.3 mm) 203 | 1 mm: 312 | — | **Agree**: the official figure falls between the chart's neighbors |
| 3/16 mild steel | 63 (max 97) at 40 A | 5 mm: 48 | T45m/Jasic: 85 at 45 A (max 110) | **Close**. The official figure is slower but for thicker 5 mm stock; the test ladder's −20 % rung (50) nearly reaches it |
| 16 ga mild steel | 114 (max 178) at 25 A | none | 847: 72 at 28 A; T45m/Jasic: 225 at 30 A, 350 at 45 A | **Conflict**: wide spread. The T45m rows use more amps |
| Thin stainless, about 1 mm | 22 ga 322 (25 A); 18 ga 335 (40 A) | 1 mm: 228 | — | **Conflict**: the Razorweld chart is faster, partly from 40 A on 18 ga |
| 3/16 stainless | 44 | 5 mm: 38.4 | T45m/Jasic: 70 at 45 A | **Close** (manual); T45m faster at 45 A |
| Thin aluminum, about 1 mm | 1/32 (0.8 mm) 397; 1/16 (1.5 mm) 174 | 1 mm: 228 | — | **Agree**: official is between the neighbors |
| 1/8 aluminum | 133 at 40 A | none | 847: about 45; T45m 10 ga (0.135): 220 at 45 A | **Big conflict** |
| 3/16–1/4 aluminum | 1/4: 49 (no 3/16 row) | 5 mm: 38.4 | T45m/Jasic 3/16: 100 at 45 A | Manual and Razorweld chart **close**; T45m much faster |

## Steps: dialing in one material and thickness

The full plan, with coupon, ladder, pierce test, THC test, and logging, is in the **[test-cut program]({{< relref "/testing/test-cut-program.md" >}})**. Short version:

1. Fresh or known-good consumables, 75 psi at the gas check, clean dry air ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})). Clean flat scrap.
2. Set the **chart amps** on the CUT45 knob (FireControl doesn't set amps; Langmuir staff, thread 5883).
3. **Speed ladder** around the **chart optimum**: −20 %, −10 %, 0, +10 %, +20 %. Capped at 300 ipm.
4. **Watch the arc under the plate** (with eye protection; see Safety). Razorweld: the arc should leave the bottom "at a slight angle away from the direction of travel".
   - Straight down means too slow, with dross build-up.
   - Sparks spraying up on top means too fast, or not enough amps.
5. Grade dross, bevel, and top spatter. Langmuir: slow cuts leave heavy dross on the bottom; fast cuts leave small beads.
6. Then test pierce delay, check the THC voltage, and measure the kerf on the winning setting ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}}); [THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}}); [Kerf width and hole/part accuracy]({{< relref "/procedures/08-kerf-and-hole-accuracy.md" >}})).
7. Log every coupon in the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}). Put the winner in the results table below and in a SheetCAM tool with the amps in the tool name ([SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})).

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Heavy, bubbly dross on the bottom; arc goes straight down | Too slow | Raise the feed 10 % at a time (Razorweld, Langmuir) |
| Sparks up on top, small hard beads on the bottom, not cut through | Too fast, or amps too low | Slow down, or raise the amps (Razorweld, Langmuir) |
| Wide kerf and rough edge on thin sheet | Too many amps for thin material | Turn the amps down (Razorweld tips) |
| Chart speed is over 300 ipm | PRO's limit | Lower the amps and ladder-test at ≤300 ipm (Razorweld thin-material rule) |
| Results drift worse over a session | Nozzle wearing, wet air | [Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}}) |
| Can't match the chart speed | Machine differences (Bigdaddy2166, thread 44500) | Trust your ladder test, not the chart |

## Duty cycle

**30 % at 45 A, at 104 °F.** My JRWPC45LH operating manual, p. 8: "Duty Cycle @ 104°F 30% @ 45Amps". Langmuir and the JRWPC45LT sister manual agree. (The 25 % figure used here before came from the Razorcut 45 DI manual, a different model.) Rest the cutter between long 45 A cuts. If it overheats, the **overheating indicator** comes on: "It illuminates when the working temperature of the IGBT is overly high. Meanwhile, the machine stops working" (p. 9). My manual has no E60/E61-style error codes; those are the DI's. **Leave the machine switched on** so the fan cools it, and wait for the light to go out: "leave the machine switched on to keep the built-in fan working to bring down the temperature inside the equipment" (p. 6).

## Safety

Plasma arc light, fumes, and fire are covered by my JRWPC45LH manual's safety section and Langmuir's safety page. Langmuir: never cut materials coated with paint, oil, grease, or solvents, and consult the MSDS. Razorweld: read the MSDS for the metal and any coating, and use ventilation or fume extraction. **Galvanized or coated stock: follow those documents. This page doesn't cover it.** Use eye protection to ANSI Z87.1 / Z49.1 (Langmuir).

## Fixed settings on the cutter

1. **Amps are set on the CUT45 knob.** FireControl doesn't control amps (Langmuir staff, thread 5883). Write the amps in the CAM tool name so you remember to set them.
2. **Air: 75 psi** ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})).
3. **Trigger mode: 2T or 4T, set on the front panel.** My JRWPC45LH operating manual lists "2T/4T Functionality" (p. 8) and 2T and 4T indicator lights (p. 9), and describes them: "When 2T operation is selected press trigger Arc starts, release trigger Arc stops. When 4T operation is selected press and release trigger Arc starts, press and release trigger Arc stops" (p. 10). It has **no Mesh mode** (that's the DI model). It doesn't say which mode to use with the CNC port; it only says the CNC port connection is "a plug and play solution for automatic torch firing" (p. 14). **2T is my assumption** because it simply follows the table's on/off signal, as a held trigger would. Confirm with Langmuir (it's on my list of support questions).
4. **Amps: start from the Razorweld chart** (25 A on thin sheet, 40 A from 14 ga up). Razorweld's general rule (my JRWPC45LH operating manual, p. 12; the DI manual says the same) is: "On thick material, set the machine to full output and vary your travel speed. On thinner material… turn down the amperage." That suggests 45 A for 3/16 in and 1/4 in, while the chart says 40 A. See Conflicts.

## Where sources disagree (and the starting choice)

- **Razorweld chart vs. Razorcut 45 DI manual vs. T45m/Jasic chart vs. forum.** The Razorweld chart and the manual are both Razorweld data, and they mostly agree where they overlap. The chart is the more complete one for machine cutting, so **ladders start from its Optimum column**, with the manual used as a sanity check (and as the start for 3/16 aluminum). The T45m/Jasic chart is the second candidate (the [test-cut program]({{< relref "/testing/test-cut-program.md" >}})'s T2 and the optional 45 A session). Forum numbers are weighted last. **All of it is unverified until the test-cut program's results are logged.**
- **16 ga mild steel speed.** Chart 114 vs. Cletus 150 vs. thread 847 72. A ±20 % ladder from 114 covers 91–137. If the best rung is at either end, run a second ladder beyond it.
- **1/8 aluminum.** Chart 133 vs. thread 847's about 45. Too far apart to both be right for the same setup. Test from 133 and go down if needed. The 847 shorthand is unverified.
- **Amps on thick material.** Chart 40 A vs. Razorweld's "full output on thick material" (45 A). **Starting choice: the chart's 40 A.** If 3/16 shows dross at every rung, try one ladder at 45 A.
- **Arc voltage.** Chart 139–152 V vs. the community 115–128 V (thread 38627, an XR owner) vs. Langmuir's "typical 60–150 V" and the CUT45's rated output voltage (96 V, my JRWPC45LH operating manual, p. 8: "Rated Output Voltage (V) 96"; other Razorweld documents say up to 98 V). **Don't type chart voltages into FireControl as fact.** SMART voltage stays the default (Langmuir staff, thread 5883). The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) compares a fixed chart voltage to the SMART reading.
- **Arc voltage, T45m/Jasic vs. Razorweld chart (the big one).** T45m: 111–123 V at 0.06 in (3/16 and under). Razorweld: 139–152 V at an unstated height. Both claim to be for the CUT45. **Planned 3-way test in the [test-cut program]({{< relref "/testing/test-cut-program.md" >}}):** the SMART reading, the Razorweld chart's voltage (T1), and the T45m chart's voltage for that thickness (T2), with the real torch height measured.
- **Duty cycle (settled).** My JRWPC45LH operating manual: 30 % at 45 A, at 104 °F (p. 8). Langmuir and the JRWPC45LT sister manual agree. The Razorcut 45 DI manual's 25 % is for a different model. **I plan on 30 % at 45 A.**
- **Output range: 20–45 A or 20–40 A?** My manual's feature list says "20-45 Amp Variable cutting adjustment", but its tech data table on the same page says "Output Current Range (A) Plasma 20-40" (p. 8), while the duty cycle line is rated at 45 A. Thread 236's "older manual" also says 20–40 A. Langmuir lists the cutter as 45 A. **I treat the dial as going to 45 A** (the feature list, the duty-cycle rating, and the dial), and the 20–40 A table entry as a leftover. Worth confirming with Razorweld only if it matters.
- **Jasic charts.** Thread 45011 (FSFab): the T45m-format charts above, now a candidate in the test-cut program. Thread 44500: a search-result summary (not checked against the full thread) suggests those heights were for Jasic's own CNC torch. **Not used.**
- **Pierce delays.** Razorweld chart: 0.25–1.00 s on 40 A rows, none on 25 A rows. T45m/Jasic: 0.0–0.9 s, and it runs short on FireControl, which starts timing at the torch-on command (staff via Greg9504, t/12941/2). **Starting choice: the Razorweld chart's delays**, then test them (the [test-cut program]({{< relref "/testing/test-cut-program.md" >}})).

## Sources

- Razorweld-supplied cut chart (Razorweld to MO-Hacker); its settings have worked well for me, not formally tested: <https://forum.langmuirsystems.com/t/847/29>. Reposted at <https://forum.langmuirsystems.com/t/847/45> (PWCNC) and <https://forum.langmuirsystems.com/t/21266/8> (TinWhisperer). Local copy: [rw_chart.jpeg](/images/rw_chart.jpeg). Unverified by test.
- T45m-format "Torch Setup" charts (mild steel, aluminum, stainless; English), reportedly supplied by Jasic for the CUT45: FSFab, <https://forum.langmuirsystems.com/t/45011> (2025-08-13). Copies on this site: [aluminum](/images/cut45_1.jpeg), [mild steel](/images/cut45_2.jpeg), [stainless](/images/cut45_3.jpeg) (see [Charts]({{< relref "/charts.md" >}})), identical to Bernie's saved images. Jasic origin unconfirmed; Hypertherm format.
- My JRWPC45LH operating manual (Razorweld CUT45 CNC; Jasic Technologies America; my printed copy): supply, duty cycle, output, air (p. 8), front panel and indicator lights (p. 9), 2T/4T (p. 10), overheating (p. 6), amperage rule and tips (pp. 12–14), CNC port (p. 14). - Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (Table 7.1.3 speed table; used only where my manual is silent): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf> (Langmuir mirror, linked from Langmuir's Reference page as the "Razorweld Razorcut 45" manual: <https://cdn.shopify.com/s/files/1/0639/3695/4602/files/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>)
- Razorweld JRWPC45LT operating manual (sister model; agrees with mine on duty cycle, air, front panel, amperage rule, overheat): <https://www.manualslib.com/manual/963728/Razorweld-Jrwpc45lt.html>
- Razorweld CUT45 spec sheet (lists JRWPC45LT and JRWPC45LH; 230 V ±15 %, 30 % at 45 A, 60–85 psi, thick-plate speeds): <https://weldfabulous.com/content/Spec%20Sheets/Razorweld-CUT45-Air-Plasma-machine-spec-sheet.pdf>
- Langmuir Reference page (links the DI manual): <https://www.langmuirsystems.com/pages/reference>
- Langmuir, "Razorweld Razorcut 45 with Machine Torch" (Langmuir's name for my cutter): <https://www.langmuirsystems.com/products/razorweld-razorcut-45-with-machine-torch>
- Langmuir, plasma cutters (30 % @ 45 A; 6.7 CFM @ 75 psi): <https://www.langmuirsystems.com/pages/plasma-cutters>
- Langmuir, consumables and cut problems (dross types): <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- Langmuir, THC guide (typical arc voltage): <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, Safety: <https://www.langmuirsystems.com/pages/safety>
- Langmuir, CrossFire PRO (300 ipm max): <https://www.langmuirsystems.com/pages/crossfire-pro>
- Forum: <https://forum.langmuirsystems.com/t/847> (community sheet; PWCNC 847/12, 847/24, 847/28, 847/30), <https://forum.langmuirsystems.com/t/20256> and <https://forum.langmuirsystems.com/t/18698> (Cletus, CUT60), <https://forum.langmuirsystems.com/t/43254> and <https://forum.langmuirsystems.com/t/36639> (Bigdaddy2166, Everlast), <https://forum.langmuirsystems.com/t/12941> (Greg9504 quoting staff: pierce delay timed from the torch-on command), <https://forum.langmuirsystems.com/t/31041> (kerf at 45 A), <https://forum.langmuirsystems.com/t/5883> (staff: amps not set by FireControl; SMART voltage), <https://forum.langmuirsystems.com/t/38627> (115–128 V report), <https://forum.langmuirsystems.com/t/8193> (Greg9504: book pierce delays run short), <https://forum.langmuirsystems.com/t/11738> (no X45 chart), <https://forum.langmuirsystems.com/t/44500> (Jasic chart discussion; Bigdaddy2166), <https://forum.langmuirsystems.com/t/236> (CUT45 tech data from an older manual), <https://forum.langmuirsystems.com/t/18563> and <https://forum.langmuirsystems.com/t/8921> (forum Google Sheet)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Only the Razorweld chart's optimum feed is filled in below, as the planned starting point. The other columns get filled from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) after each test-cut program session.

| Material | Thickness | Amps | Feed (ipm) | Razorweld chart optimum | Pierce delay (s) | Cut ht (SheetCAM) | THC V (SMART read) | Kerf | Dross / bevel | Session / date |
|---|---|---|---|---|---|---|---|---|---|---|
| Mild steel | 16 ga | | | 114 | | | | | | |
| Mild steel | 14 ga | | | 221 | | | | | | |
| Mild steel | 10 ga | | | 98 | | | | | | |
| Mild steel | 3/16 | | | 63 | | | | | | |
| Stainless | 16 ga | | | 243 | | | | | | |
| Stainless | 14 ga | | | 144 | | | | | | |
| Stainless | 10 ga | | | 70 | | | | | | |
| Stainless | 3/16 | | | 44 | | | | | | |
| Aluminum | 1/16 | | | 174 | | | | | | |
| Aluminum | 1/8 | | | 133 | | | | | | |
| Aluminum | 3/16 | | | none (official 5 mm: 38) | | | | | | |
