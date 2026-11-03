---
title: "Test-Cut Program: Checking the Starting Settings, Coupon by Coupon"
date: 2026-10-28
tags: ["cnc", "plasma", "testing", "cut-chart", "razorweld-45", "x45", "crossfire-pro"]
draft: false
weight: 10
series: ["CrossFire PRO procedures"]
series_order: 10
lastmod: 2026-10-30T18:30:00-07:00
summary: "A planned, coupon-by-coupon test program for checking the Razorweld-supplied chart (and the T45m-format chart's voltages) on a CrossFire PRO with the CUT45 and X45 torch, with every cut logged."
---

{{< lastupdated >}}

**Status: planned; no results logged yet (as of 30 October 2026).**

## Applies to

My CrossFire PRO with IHS and THC, the Razorweld CUT45 CNC (model JRWPC45LH) on 230 V, and the X45 machine torch with the 51206 tip, cutting mild steel, stainless, and aluminum. The goal is to turn the Razorweld-supplied chart (Razorweld to MO-Hacker, [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})) into **my own chart**, checked on my machine, with every cut logged in the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}). Plan settings come from the Razorweld chart, Langmuir's defaults, and Razorweld's manual. The second candidate, the T45m-format chart reportedly supplied by Jasic (FSFab, t/45011; origin unconfirmed), supplies the T2 voltage and an optional 45 A comparison session ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})). **No number in this plan is a tested result until it's been cut and logged.** Doesn't cover: Powermax or other cutters' test charts, or XR/belt-machine calibration.

**One material and thickness per session: 10 coupons plus one or two short test lines**, about one shop afternoon. Don't mix thicknesses in a session; you won't know what changed.

## The test coupon (draw it once, reuse it forever)

Draw this once in Inkscape or Fusion and save it as `test-coupon.dxf`. Origin is the bottom-left corner of the rectangle.

| Feature | Size and position | What it tells me |
|---|---|---|
| Outer rectangle | **3.000 x 2.000 in** | Kerf (two directions), dross, bevel, edge square |
| Large hole | **1.000 in** diameter, center at (0.900, 1.000) | Hole size and roundness, bevel on holes |
| Small hole | **0.500 in** diameter, center at (2.250, 1.000) | Small-hole quality (THC usually off on these) |
| Straight line | **4.000 in** open cut, from (−0.500, −0.750) to (3.500, −0.750) | Clean drop line to read lag lines, dross, and slot width |

The footprint is about 4 x 3 in. Space coupons **5 in apart in X** and **4 in apart in Y**. Ten coupons (two rows of five) fit on a piece about **26 x 9 in**. The H1/H2 test lines need their own strip, about 12 x 3 in. Use flat, clean scrap; for thin sheet, weight or clamp it flat.

**SheetCAM, once** ([SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}}) for the post and tool setup):

1. Import `test-coupon.dxf`. Check the scale: the rectangle must measure 3.000 x 2.000.
2. Operations, in cut order:
   1. Both holes: **inside offset**, lead-in from the center.
   2. The line: **no offset (on the line)**.
   3. The rectangle: **outside offset**.

   Lead-ins in scrap and **no lead-outs** ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}}); [SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})). Check the order in the preview.
3. Make a test tool: **kerf width 0** (so I can measure kerf), pierce height **0.15 in**, pierce delay per the session table, plunge **50 ipm**, cut height **0.08 in** (Langmuir guide; [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). Put the amps in the tool name, for example `TEST MS16 25A`.
4. **Post one program per coupon**, changing only what that coupon tests. Name each file with the session and coupon, for example `S01-L1-091.tap`. Open each file and check that the first line reads `(v1.6-sc)` ([SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})).
5. At the table: jog to the next empty spot, **Zero X and Y** (keep Z as FireControl sets it with IHS), and run the next file.

## Prep, every session (about 15 minutes)

1. **Drain the compressor tank** and the filter bowls (my JRWPC45LH operating manual, p. 13: "drain the receiver (tank) on the air compressor at least daily").
2. **Dry-air check:** after the drain, the bowls should stay dry through the session. Write "bowls dry: yes/no" in the notes of the first log row. Water means fix the air first ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})).
3. **Fresh consumables:** new electrode and tip together, assembled in the torch diagram's order ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})). Write **0** in `consumables_pierce_count` on coupon 1 and count up one per pierce. Each coupon has 4 pierces: 2 holes, 1 line, 1 rectangle.
4. **75 psi at the cutter during the gas test** (CUT45 gas check; my manual gives 0.5 MPa (75 psi), p. 8, and the machine can't cut while the gas-check light is on, p. 9, so switch it back off; [Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})). Write the psi you actually saw.
5. **Set the amps on the CUT45 knob** to the session amps. FireControl doesn't set amps (thread 5883).
6. **Clean ground to the work:** clean the work-clamp spot and check continuity from the clamp to the test piece ([Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}})). Grounding of the cutter and house wiring: follow my CUT45 manual and an electrician, not this page.
7. **Square and tram check:** torch vertical in X and Y with a small square (Langmuir Z tram video; [Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}})). Gantry check from [Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}}) if it's been a while.
8. **THC settings at Langmuir defaults** (SMART voltage, 85 % cutoff, 5 % Z-speed; [THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
9. **Safety:** eye protection to ANSI Z87.1 / Z49.1, ventilation, and fire watch (Langmuir safety page; my CUT45 manual). Never cut coated or galvanized test scrap; follow the manufacturers on fumes.

## The coupons in a session (in this order)

| # | Coupon | What changes | Everything else |
|---|---|---|---|
| 1–5 | **L1–L5 speed ladder** | Feed: chart optimum −20 %, −10 %, 0, +10 %, +20 % | Chart amps; ladder pierce delay; THC on, **SMART voltage (0)**. Write the Live Volts reading for each. |
| — | **Pick a provisional winner** | Grade L1–L5 and choose the best feed | The winner's Live Volts is the **SMART** voltage for the 3-way test |
| 6 | **H1 height-reference line** (line only) | [THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})'s manual-nominal test: THC off, **Z motor unplugged**, torch set to a **real 0.060 in** gap with a feeler gauge; read Live Volts | Provisional feed; no IHS loop. This is **my torch's measured voltage at 0.060 in** |
| (6b) | **H2 second height line** (optional, line only) | The same, at a real **0.120 in** gap | Lets me turn any voltage into an estimated torch height (below) |
| 7 | **T1 THC fixed at the Razorweld chart's voltage** | Nominal Voltage = Razorweld chart arc V for this thickness (152 V for S01, 147 V for S04) | Provisional feed; ladder delay |
| 8 | **T2 THC fixed at the Jasic/T45m chart's voltage** | Nominal Voltage = T45m chart voltage for this thickness (session table; for example **118 V** for 3/16 mild; **111 V** for 16 ga mild at that chart's 30 A, or 116 V at its 45 A). **The T45m amps differ from my session amps.** | Provisional feed; ladder delay |
| 9 | **P1 pierce delay** | Delay one step shorter than the ladder | Provisional feed; **the THC choice that won** the 3-way test |
| 10 | **P2 pierce delay** | Delay one step longer (on 25 A rows: no delay, 0 s) | Same |
| 11 | **V1 verification** | Kerf width = my measured kerf | Winning feed, delay, and THC choice |

The THC test comes **before** the pierce-delay tests on purpose. Voltage sets the real torch height, and height affects both the pierce and the edge, so the height gets settled first. The speed ladders are the same as before.

**Speed limit:** never post a rung above **300 ipm** (PRO max). If the +20 % rung is over 300, cut it at 300 and say so in the notes.

**Pierce delay steps** use the delays that appear in the Razorweld chart: 0, 0.25, 0.50, 0.75, 1.00 s. The chart gives **no delay for its 25 A rows**, so those ladders use **0.5 s** (Langmuir's SheetCAM guide example), and P1/P2 test **0.25 s** and **0 s**.

### Session table (planned settings, from the Razorweld chart on the cut settings page; T2 from the T45m-format chart)

| Session | Material | Thickness | Amps | Chart arc V (T1) | T2 V (T45m row used) | Ladder pierce delay (s) | Chart optimum | L1 −20 % | L2 −10 % | L3 0 | L4 +10 % | L5 +20 % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 | Mild steel | 16 ga | 25 A | 152 | 111 (16 ga, 30 A; 116 at 45 A) | — (use 0.5) | 114 | 91 | 103 | 114 | 125 | 137 |
| S02 | Mild steel | 14 ga | 40 A | 144 | 117 (14 ga, 45 A) | 0.25 | 221 | 177 | 199 | 221 | 243 | 265 |
| S03 | Mild steel | 10 ga | 40 A | 146 | 117 (10 ga, 45 A) | 0.50 | 98 | 78 | 88 | 98 | 108 | 118 |
| S04 | Mild steel | 3/16 in | 40 A | 147 | 118 (3/16, 45 A) | 0.75 | 63 | 50 | 57 | 63 | 69 | 76 |
| S05 | Stainless | 16 ga | 40 A | 144 | 116 (16 ga, 45 A; 111 at 30 A) | 0.25 | 243 | 194 | 219 | 243 | 267 | 292 |
| S06 | Stainless | 14 ga | 40 A | 144 | 117 (14 ga, 45 A) | 0.25 | 144 | 115 | 130 | 144 | 158 | 173 |
| S07 | Stainless | 10 ga | 40 A | 147 | 117 (10 ga, 45 A) | 0.50 | 70 | 56 | 63 | 70 | 77 | 84 |
| S08 | Stainless | 3/16 in | 40 A | 149 | 118 (3/16, 45 A) | 0.75 | 44 | 35 | 40 | 44 | 48 | 53 |
| S09 | Aluminum | 1/16 in | 25 A | 152 | 118 (16 ga, 30 A) | — (use 0.5) | 174 | 139 | 157 | 174 | 191 | 209 |
| S10 | Aluminum | 1/8 in | 40 A | 149 | 122 (10 ga 0.135, 45 A; nearest row) | 0.50 | 133 | 106 | 120 | 133 | 146 | 160 |
| S11 | Aluminum | 3/16 in | 40 A | none | 123 (3/16, 45 A) | 1.00 | none | 38 | 49 | 59 | 71 | 85 |

- **T2 note:** the T45m chart has only 30 A and 45 A rows. For 25 A sessions, use its 30 A row; for 40 A sessions, its 45 A row. The amps don't match exactly, so T2 is a ballpark, not a like-for-like setting. The T45m chart has no 1/8 in aluminum row; S10 uses the nearest (10 ga, 0.135 in).
- **S09 (aluminum 1/16 in)** stands in for "16 ga" in aluminum; the Razorweld chart lists aluminum in fractions, not gauges.
- **S11 (aluminum 3/16 in) has no chart row.** Its ladder isn't ±20 %. It starts at **38 ipm** (the Razorcut 45 DI manual's 5 mm figure, a related model), then **49 ipm** (the Razorweld chart's 1/4 in row, which 3/16 should at least match), then +20 % steps (59, 71, 85). Delay starts at **1.00 s** (the 1/4 in row), with P1/P2 at 0.75 and 0.50 s. Amps 40 A, the same as the chart's 1/8 and 1/4 rows.
- Mild 14 ga uses the **221 optimum**; ignore the chart's odd 640 max ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}), oddities).
- 11 ga isn't in the chart. If it's stocked later, give it its own session later, starting from a ladder that covers both neighbors.

## Steps: running a session

1. Do the prep list above.
2. Cut **L1 to L5** in order, slowest first. **Watch the arc under the plate** through proper lenses. Razorweld: the arc should trail "at a slight angle away from the direction of travel"; straight down is too slow; sparks spraying up on top is too fast. Read **Live Volts** in FireControl partway along the line cut and write it in that row's notes as `liveV=___`.
3. Let the coupons cool. Knock them out and **grade each one** (judging guide below). Pick the **provisional winner**: the rung with the least dross that's easy to remove, the squarest edge, and a clean line cut. If two tie, take the **faster** one. If the winner is L1 or L5 (an end of the ladder), the best may be beyond it. Note it, and run another ladder past that end next session.
4. **3-way THC voltage test** at the provisional feed and the ladder delay. The three candidates are:
   - **SMART:** the winner's Live Volts from step 2. That rung is already cut; no new coupon.
   - **The Razorweld chart's voltage:** T1.
   - **The Jasic/T45m chart's voltage for this thickness:** T2 (session table).

   The sub-steps:
   1. **H1 first** ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})'s manual-nominal steps). Gauge the torch to a real **0.060 in** gap; don't use SheetCAM's 0.08 here, because there's no IHS springback in this test ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). Turn the electronics box off, unplug the Z motor, power up, cut an 8–10 in line, and read Live Volts. Write it in `thc_voltage` on the H1 row. If you can, start the line at the plate edge rather than piercing at 0.060 in, which is hard on the tip; the T45m-format chart uses edge starts on thick plate. See `firecontrol/fc-01-straight-cut-edge-start.md` for edge-start methods.
   2. **H2 (optional):** repeat at a real **0.120 in** gap.
   3. With the electronics box off, plug the Z motor back in, power up, and check that IHS works on a scrap touch-off before going on.
   4. **Cut T1, then T2,** each with the THC on and Nominal Voltage set. **Stand by the pause/E-stop.** If the torch dives into the plate, climbs away, or loses the arc, stop, set Nominal back to **0**, and write what happened. A stopped coupon is a valid result.
   5. **Measure the real torch height.** FireControl's Z readout **won't** show THC moves (THC guide), so read height from voltage. Arc voltage rises as the torch goes up and drops as it gets closer (THC guide).
      - A voltage near **H1** means about 0.060 in. Higher means higher; lower means lower.
      - With H2 too, estimate: **height ≈ 0.060 + (V − H1) × 0.060 ÷ (H2 − H1)**. That's a straight-line approximation worked out for this plan, not a Langmuir formula. Use it for SMART, T1, and T2.
      - **Better, direct check: pause and measure** (ChelanJim, t/32789/3; [Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}})). On a long straight line, press the space bar partway through, wait for the arc and post-flow to stop, switch the CUT45 off, and slide a feeler gauge under the torch. Write it as `gap=___` in the notes. Do this at least on the SMART winner, T1, and T2.
      - Watch the **THC up/down LEDs** at the start of each cut. A long run of one direction means the THC is driving the torch away from the 0.060 in it started at.
   6. **Measure bevel** on the rectangle of the SMART winner, T1, and T2. Put a small square against each long edge, and write `square`, `slight`, `heavy`, or `one-side` in `result_bevel`. A torch running too high shows bevel on all edges ([Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}})). Also note the slot width of the line.
   7. **Pick the THC choice.** It's the best edge (dross, then bevel) of the three. **SMART (0) stays the default** unless T1 or T2 is clearly better (Langmuir staff recommend SMART; thread 5883). Write down whether the Razorweld chart's voltage (139–152 V range) or the T45m chart's (111–123 V) lands closer to H1 on my torch. That answers [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})'s voltage conflict.
5. Cut **P1 and P2** at the provisional feed with the **winning THC choice**. Look at the start of each cut. Too short: a blow-back gouge, or not pierced through at the start. Too long: on thin sheet the arc blows a hole and is lost right after the pierce ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). Keep the **shortest delay that pierces cleanly** every time. The T45m chart's delays are shorter than the Razorweld chart's. FireControl times the delay from the torch-on command, not arc-on (staff quoted by Greg9504, t/12941/2), so book delays run short. Treat the T45m delays only as a **floor**. If a delay shorter than the T45m value looks clean, repeat it on a second coupon before trusting it.
6. **Measure kerf** on the winning coupon (method below). Set that kerf in the tool and cut **V1**. Measure V1's rectangle and holes, and write the error from nominal in the notes.
7. Fill in all rows in the CSV. Copy the winner into [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})'s "Bernie's test results" table.

## Optional session S04B: 45 A T45m settings vs. the Razorweld chart (3/16 mild steel)

Why: FSFab (t/45011) says the T45m-format 3/16 settings fixed "pierces, then torch goes out" on his CUT45 machine torch. This session checks whether they beat the Razorweld chart's 40 A settings on my machine. Run it **after S04**, on the same batch of 3/16 plate, with consumables that still look good.

| # | Coupon | Amps (knob) | Feed | Pierce delay | THC | Source |
|---|---|---|---|---|---|---|
| J1 | Razorweld chart baseline | 40 A | 63 ipm (or the S04 winner) | 0.75 s (or the S04 winner) | SMART (0) | Razorweld chart; S04 result |
| J2 | T45m settings, delay with margin | 45 A | 85 ipm | **0.75 s** (0.5 book + 0.25 margin for FireControl's start delay; a margin chosen for this plan, not a measured number) | SMART (0) | T45m 3/16 row; t/12941/2 |
| J3 | T45m settings, book delay | 45 A | 85 ipm | 0.5 s | SMART (0) | T45m 3/16 row |
| J4 | T45m settings, fixed voltage | 45 A | 85 ipm | the better of J2/J3 | Nominal **118 V** | T45m 3/16 row |

Steps:

1. Cut J1 at 40 A. **Turn the CUT45 knob to 45 A** before J2. Write the amps in every row.
2. Cut J2, J3, J4. Use the pause-and-measure check on J2 and J4 (`gap=___`).
3. Grade all four with the judging guide. Measure kerf on J1 and J2 (it's likely wider at 45 A).
4. **Duty cycle:** 45 A on 3/16 is hard on the cutter (my JRWPC45LH operating manual, p. 8: 30 % at 45 A, at 104 °F). Let it rest between coupons. If the overheating light comes on (p. 9), leave the machine on so the fan cools it, and wait for the light to go out (p. 6) ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})).
5. Verdict: if J2 or J3 is clearly cleaner than J1, run a short 45 A ladder (68, 77, 85, 94, 102 ipm) next time before adopting it. Otherwise keep the Razorweld chart's 40 A settings.

## Kerf measurement (coupons cut with kerf width 0)

Use calipers on the **top side**, away from the lead-in. Write bottom-side numbers in the notes if they differ.

1. Rectangle: measure X (nominal 3.000) and Y (nominal 2.000). Cut on the line with kerf 0, the part comes out **undersize by one kerf width**.
   - **Kerf = ((3.000 − X) + (2.000 − Y)) ÷ 2.**
2. Holes: with kerf 0 they come out **oversize by about one kerf**. The 1.000 hole minus 1.000 should roughly match the rectangle number. It's a cross-check.
3. Line: the slot width in the middle of the line (caliper inside jaws) is a direct, rough kerf reading.
4. Put the rectangle number in `kerf_measured_in`. [Kerf width and hole/part accuracy]({{< relref "/procedures/08-kerf-and-hole-accuracy.md" >}}) has the full method.

## Judging guide

| Look at | Good | Too slow | Too fast | Other causes |
|---|---|---|---|---|
| **Bottom dross** | None, or a thin line that falls off | **Heavy, bubbly** globs that knock off easily (low-speed dross) | **Small, hard beads** rolled onto the bottom edge, hard to remove (high-speed dross) | Worn tip; wrong height (files 04, 06) |
| **Top spatter** | Clean top edge | — | Sparks spraying up during the cut; spatter on top | Pierce too low or delay too short at the start only ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})) |
| **Bevel** (square against the edge) | Square, or about the same on both sides | Can widen | Can increase | Torch tilted (one side, everywhere); torch too high (all edges); cut direction reversed (part side only) ([Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}})) |
| **Lag lines** (drag lines on the cut face) | Fairly straight down the face | Nearly vertical, with heavy dross | Curving strongly backward against the travel, often with beads | — |
| **Line cut** | Cut through end to end | — | Not cut through in spots | Amps too low |

Source notes:

- Dross types: Langmuir's consumables page (slow = heavy dross on the bottom, fast = small beads) and Razorweld's tips.
- Arc angle: Razorweld.
- Lag-line reading: general plasma-shop practice. **Neither Langmuir nor Razorweld describes it**, so treat it as a supporting clue, not the deciding one.

How to write results in the log (keep the words the same every time so it can be sorted):

- `result_dross`: `none`, `light`, `heavy-bubbly`, `hard-beads`, or `not-through`.
- `result_bevel`: `square`, `slight`, `heavy`, or `one-side`, plus which side in the notes.

## What to record in test-cut-log.csv, one row per coupon

| Column | What to write |
|---|---|
| `date` | Cut date, YYYY-MM-DD |
| `material` | `mild_steel`, `stainless`, or `aluminum` |
| `thickness_in` | Actual thickness, calipered if you can (16 ga steel is nominally 0.0598) |
| `amps` | Knob setting |
| `psi` | What the gauge showed during the gas test |
| `feed_ipm` | Feed used for that coupon |
| `pierce_height_in`, `pierce_delay_s`, `cut_height_in` | As set in the SheetCAM tool. On H1/H2: the real gauged gap (0.060 or 0.120) in `cut_height_in`, with pierce fields blank |
| `thc_on` | `yes` or `no` |
| `thc_voltage` | `0` for SMART, the number for a fixed nominal (T1, T2), or the Live Volts reading on H1/H2 |
| `kerf_set_in` | `0` on test coupons; your measured kerf on V1 |
| `kerf_measured_in` | Kerf from the rectangle formula |
| `consumables_pierce_count` | Running pierce total on this electrode and tip at the **end** of this coupon |
| `result_dross`, `result_bevel` | Words from the judging guide |
| `notes` | `liveV=___`, bowls dry yes/no, hole sizes, anything odd. **No commas**; use semicolons |
| `source_setting` | Where the setting came from, for example `chart opt 114 -20%` or `Langmuir example 0.5s` |
| `session_id` | For example `S01-MS-16GA` |

The log already has **planned rows** for **S01 (mild steel 16 ga)**, **S04 (mild steel 3/16 in)**, and the optional **S04B**. Results are blank, so fill them in as you go. For the H, T, P, and V rows, write the provisional winning feed into `feed_ipm` once it's known. Write each estimated height in the notes as `height~___`.

## Deciding the winner and updating the chart notes

1. The winner is the coupon with the cleanest dross, then the squarest bevel, then the fastest feed.
2. If the winner is within one rung of the chart optimum, the Razorweld chart is **confirmed** for that row. Write "confirmed" in [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})'s results table.
3. If the winner is at L1 or L5, the Razorweld chart is **off** for that row. Run another ladder beyond it before calling it.
4. Write the winning amps, feed, pierce delay, THC choice, and measured kerf into [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})'s results table. Then make a SheetCAM tool for it ([SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})).
5. **Re-check a winner** after any change of consumable brand, air setup, or cutter, or after a big crash or rebuild.

## Symptoms -> causes -> fixes (during testing)

| Symptom | Likely cause | Fix |
|---|---|---|
| Every rung has heavy dross | Wrong amps, worn tip, or height too high | New consumables; check the height ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})); try one ladder at 45 A on thick stock (Razorweld rule; [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})) |
| Every rung has hard beads or isn't cut through | Feed too high for the amps | Run a lower ladder starting at L1's speed |
| Results get worse coupon by coupon | Tip wearing, or water arriving | Look at the tip; check the bowls ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})) |
| Torch dives or climbs on T1 or T2 | That voltage doesn't match a sensible height on my torch | Back to SMART (0); that's a valid result. Compare with H1 |
| H1 voltage far from all three candidates | Gap not really 0.060, or worn tip | Re-gauge with the Z motor unplugged; check the tip ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})) |
| Holes oval or undersized on one side | Gantry or coupler issue, not cutting | [Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}}) |

## Where sources disagree (and the starting choice)

- **Ladder center:** the Razorweld chart's optimum (Razorweld to MO-Hacker; weighted with the Razorweld manual, below Langmuir) over the T45m/Jasic chart and other forum numbers ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})). The manual's figures are the sanity check. The T45m chart gets its own test in T2 and S04B.
- **Pierce delay on 25 A rows:** the chart gives none. Start from Langmuir's 0.5 s example and test shorter.
- **Fixed voltage vs. SMART:** Langmuir staff favor SMART. The Razorweld chart's voltages (139–152 V) have no height attached. The T45m/Jasic chart gives 111–123 V at a stated 0.06 in, but its origin is unconfirmed ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})). **SMART stays the default** unless T1 or T2 proves better. H1 is my torch's own measured voltage at 0.060 in, and that beats both charts.
- **Order of tests:** the THC test now comes right after the ladder, before the pierce tests, so the pierce tests run at the height that will actually be used. The ladder runs on SMART because that's the default.
- **Pierce delays:** the Razorweld chart's steps are the plan. The T45m chart's shorter delays are a lower bound only, because FireControl times from the torch-on command (t/12941/2).

## Sources

- Razorweld-supplied chart (Razorweld to MO-Hacker, <https://forum.langmuirsystems.com/t/847/29>; its settings have worked well for me, not formally tested): [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}).
- My JRWPC45LH operating manual (duty cycle and air, p. 8; indicator lights, p. 9; overheating, p. 6; amperage rule and speed check, p. 12; tank draining, p. 13)
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (Table 7.1.3 speed for S11; arc-angle speed check): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- Langmuir, consumables and cut problems (dross types): <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- Langmuir, THC guide (SMART voltage, defaults, manual nominal test): <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, SheetCAM guide (example tool: pierce 0.15 in, delay 0.5 s, cut height 0.08 in): <https://www.langmuirsystems.com/pages/software-sheetcam>
- Langmuir, CrossFire PRO (300 ipm): <https://www.langmuirsystems.com/pages/crossfire-pro>
- Langmuir, Safety: <https://www.langmuirsystems.com/pages/safety>
- Langmuir, Z-axis tram video: <https://www.youtube.com/watch?v=xCbOJz-zfl8>
- T45m-format chart reportedly supplied by Jasic for the CUT45 (FSFab, <https://forum.langmuirsystems.com/t/45011>; Jasic origin unconfirmed; Hypertherm format): T2 voltages and session S04B, [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}).
- Forum: <https://forum.langmuirsystems.com/t/5883> (staff: amps not set by FireControl; SMART voltage), <https://forum.langmuirsystems.com/t/8193> and <https://forum.langmuirsystems.com/t/12941> (Greg9504 quoting staff: pierce delay timed from the torch-on command), <https://forum.langmuirsystems.com/t/32789> (ChelanJim: pause and measure)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** The table below lists the planned sessions; it gets one summary row per session, with details in the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) (`test-cut-log.csv`).

| Session | Date | Material / thickness | Winner feed | Delay | SMART V | H1 V (0.060 in) | THC choice | Kerf | Chart confirmed? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | | Mild steel 16 ga | | | | | | | | |
| S04 | | Mild steel 3/16 in | | | | | | | | |
