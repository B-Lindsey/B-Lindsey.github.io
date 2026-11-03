---
title: "Test-Cut Worksheet (Print and Fill In)"
date: 2026-10-28
tags: ["cnc", "plasma", "testing", "worksheet"]
draft: false
weight: 2
lastmod: 2026-10-30T18:30:00-07:00
summary: "The printable shop-floor sheet for the test-cut program's sessions on a CrossFire PRO, CUT45 (230 V), and X45 machine torch. Print one page per session, then copy the results into the test-cut log."
printLandscape: true
---

{{< lastupdated >}}

<div class="no-print">

> **Printing:** use your browser's Print. Session sheets print landscape on letter paper, one session per page, with the menus hidden. Turn on "Background graphics" only if you want the colors.

</div>

<div class="print-wide">

**Status: planned; no results logged yet (as of 30 October 2026).**

## Applies to

The shop-floor sheet for the [test-cut program]({{< relref "/testing/test-cut-program.md" >}})'s test sessions on my CrossFire PRO, Razorweld CUT45 CNC (model JRWPC45LH, 230 V), and X45 machine torch. Print one page per session and copy it into `test-cut-log.csv` afterward. Planned settings come from the Razorweld-supplied chart (Razorweld to MO-Hacker), the T45m-format chart reportedly from Jasic for T2 ([CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})), and Langmuir's defaults. **Planned, not proven.**

**Fixed for every coupon:** 75 psi · pierce height 0.15 in · plunge 50 ipm · cut height 0.08 in (SheetCAM; about 0.060 in real) · kerf 0 except V1 · max 300 ipm.

**Order:** L1–L5 (SMART) → pick a provisional winner → H1 (and H2) height lines → T1 Razorweld chart V → T2 Jasic/T45m chart V → pick the THC choice → P1, P2 → V1.

**Real gap check:** pause a straight cut with the space bar, let the arc and post-flow stop, switch the CUT45 off, and feeler-gauge the torch (ChelanJim, t/32789/3). Write `gap=___` in Est. height.

**Torch height from voltage (with H1 and H2):** height ≈ 0.060 + (V − H1) × 0.060 ÷ (H2 − H1). Higher volts mean a higher torch. This is an approximation worked out for the test-cut program, not a Langmuir formula.

**Judging key:**

- **Dross:** none / light / heavy-bubbly (slow) / hard-beads (fast) / not-through
- **Bevel:** square / slight / heavy / one-side (which side?)
- **Lag lines:** straight / vertical (slow?) / curved back (fast?)
- **Spatter:** none / some / heavy

---

## Blank session sheet

Session ID: ____________

| Date | Material | Thickness (calipered) | Amps (knob) | PSI at gas test | Bowls dry? | New consumables? | Ground checked? | Torch square? |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

| Coupon | Feed ipm | Delay s | THC (0/fixed V/off) | Live V | Est. height | Pierce count | Bottom dross | Top spatter | Bevel | Lag lines | X (3.000) | Y (2.000) | 1.000 hole | 0.500 hole |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L2 |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L3 |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L4 |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L5 |  |  | 0 |  |  |  |  |  |  |  |  |  |  |  |
| **Provisional winner →** | ___ |  | SMART V = ___ |  |  |  |  |  |  |  |  |  |  |  |
| H1 (line, 0.060 gauged) | win: ___ | — | off, Z unplugged |  | 0.060 |  |  |  |  |  | — | — | — | — |
| H2 (line, 0.120 gauged; optional) | win: ___ | — | off, Z unplugged |  | 0.120 |  |  |  |  |  | — | — | — | — |
| T1 (Razorweld chart V) | win: ___ |  | fixed: ___ |  |  |  |  |  |  |  |  |  |  |  |
| T2 (Jasic/T45m chart V) | win: ___ |  | fixed: ___ |  |  |  |  |  |  |  |  |  |  |  |
| **THC choice →** |  |  | ___ |  |  |  |  |  |  |  |  |  |  |  |
| P1 | win: ___ |  | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |
| P2 | win: ___ |  | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |
| V1 | win: ___ | best: ___ | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |

**Winner:** feed ______ ipm · delay ______ s · THC ______ (closest to H1: Razorweld V / T45m V / SMART?) · kerf ______ in (= ((3.000 − X) + (2.000 − Y)) ÷ 2)
**Chart confirmed?** yes / no / run another ladder · **Copied to [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}) and the CSV?** ☐

---

## S01: Mild steel 16 ga, 25 A (Razorweld chart optimum 114 ipm, arc V 152; T45m chart 111 V at 30 A / 116 V at 45 A)

| Date | Material | Thickness (calipered) | Amps (knob) | PSI at gas test | Bowls dry? | New consumables? | Ground checked? | Torch square? |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

| Coupon | Feed ipm | Delay s | THC (0/fixed V/off) | Live V | Est. height | Pierce count | Bottom dross | Top spatter | Bevel | Lag lines | X (3.000) | Y (2.000) | 1.000 hole | 0.500 hole |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | 91 | 0.5 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L2 | 103 | 0.5 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L3 | 114 | 0.5 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L4 | 125 | 0.5 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L5 | 137 | 0.5 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| **Provisional winner →** | ___ |  | SMART V = ___ |  |  |  |  |  |  |  |  |  |  |  |
| H1 (line, 0.060 gauged) | win: ___ | — | off, Z unplugged |  | 0.060 |  |  |  |  |  | — | — | — | — |
| H2 (line, 0.120 gauged; optional) | win: ___ | — | off, Z unplugged |  | 0.120 |  |  |  |  |  | — | — | — | — |
| T1 (Razorweld chart V) | win: ___ | 0.5 | 152 |  |  |  |  |  |  |  |  |  |  |  |
| T2 (Jasic/T45m 16 ga 30 A row; 116 at 45 A) | win: ___ | 0.5 | 111 |  |  |  |  |  |  |  |  |  |  |  |
| **THC choice →** |  |  | ___ |  |  |  |  |  |  |  |  |  |  |  |
| P1 | win: ___ | 0.25 | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |
| P2 | win: ___ | 0 | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |
| V1 | win: ___ | best: ___ | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |

**Winner:** feed ______ ipm · delay ______ s · THC ______ (closest to H1: Razorweld V / T45m V / SMART?) · kerf ______ in (= ((3.000 − X) + (2.000 − Y)) ÷ 2)
**Chart confirmed?** yes / no / run another ladder · **Copied to [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}) and the CSV?** ☐

---

## S04: Mild steel 3/16 in, 40 A (Razorweld chart optimum 63 ipm, arc V 147; T45m chart 118 V at 45 A)

| Date | Material | Thickness (calipered) | Amps (knob) | PSI at gas test | Bowls dry? | New consumables? | Ground checked? | Torch square? |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

| Coupon | Feed ipm | Delay s | THC (0/fixed V/off) | Live V | Est. height | Pierce count | Bottom dross | Top spatter | Bevel | Lag lines | X (3.000) | Y (2.000) | 1.000 hole | 0.500 hole |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | 50 | 0.75 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L2 | 57 | 0.75 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L3 | 63 | 0.75 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L4 | 69 | 0.75 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| L5 | 76 | 0.75 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| **Provisional winner →** | ___ |  | SMART V = ___ |  |  |  |  |  |  |  |  |  |  |  |
| H1 (line, 0.060 gauged) | win: ___ | — | off, Z unplugged |  | 0.060 |  |  |  |  |  | — | — | — | — |
| H2 (line, 0.120 gauged; optional) | win: ___ | — | off, Z unplugged |  | 0.120 |  |  |  |  |  | — | — | — | — |
| T1 (Razorweld chart V) | win: ___ | 0.75 | 147 |  |  |  |  |  |  |  |  |  |  |  |
| T2 (Jasic/T45m 3/16 45 A row) | win: ___ | 0.75 | 118 |  |  |  |  |  |  |  |  |  |  |  |
| **THC choice →** |  |  | ___ |  |  |  |  |  |  |  |  |  |  |  |
| P1 | win: ___ | 0.50 | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |
| P2 | win: ___ | 1.00 | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |
| V1 | win: ___ | best: ___ | choice: ___ |  |  |  |  |  |  |  |  |  |  |  |

**Winner:** feed ______ ipm · delay ______ s · THC ______ (closest to H1: Razorweld V / T45m V / SMART?) · kerf ______ in (= ((3.000 − X) + (2.000 − Y)) ÷ 2)
**Chart confirmed?** yes / no / run another ladder · **Copied to [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}) and the CSV?** ☐

---

## S04B (optional): Mild steel 3/16 in, T45m 45 A vs. Razorweld 40 A

Run after S04, same plate batch. **Change the knob to 45 A after J1.** Rest the cutter between coupons (25 % duty at 45 A).

| Date | Material | Thickness (calipered) | Amps (knob) | PSI at gas test | Bowls dry? | New consumables? | Ground checked? | Torch square? |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

| Coupon | Feed ipm | Delay s | THC (0/fixed V/off) | Live V | Est. height | Pierce count | Bottom dross | Top spatter | Bevel | Lag lines | X (3.000) | Y (2.000) | 1.000 hole | 0.500 hole |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J1 (Razorweld 40 A) | 63 or S04 win: ___ | 0.75 or S04 win: ___ | 0 |  |  |  |  |  |  |  |  |  |  |  |
| J2 (T45m 45 A, delay + margin) | 85 | 0.75 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| J3 (T45m 45 A, book delay) | 85 | 0.5 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| J4 (T45m 45 A, fixed V) | 85 | better of J2/J3: ___ | 118 |  |  |  |  |  |  |  |  |  |  |  |

**Verdict:** J1 / J2 / J3 / J4 best? ______ · kerf J1 ______ J2 ______ · If a 45 A coupon wins, next time run a 45 A ladder: 68, 77, 85, 94, 102 ipm.

---

## Where results go

Copy each session's winner into [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})'s results table.

## Sources

Settings come from [CUT45 (X45 torch) cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}) (the Razorweld-supplied chart, Razorweld to MO-Hacker, <https://forum.langmuirsystems.com/t/847/29>; T2 and S04B from the T45m-format chart reportedly supplied by Jasic, FSFab <https://forum.langmuirsystems.com/t/45011>, origin unconfirmed) and the [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) (the method and its sources: my JRWPC45LH operating manual, the Razorcut 45 DI manual, Langmuir THC and SheetCAM guides).


</div>
