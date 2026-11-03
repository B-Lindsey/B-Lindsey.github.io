---
title: "CrossFire PRO Plasma Procedures"
date: 2026-10-28
tags: ["cnc", "plasma", "crossfire-pro", "razorweld-45", "index"]
draft: false
lastmod: 2026-10-30T18:30:00-07:00
---

{{< lastupdated >}}

**Personal notes, unlisted.** I'm Bernie Lindsey, and I've run my CrossFire PRO since August 2024. These are my notes, put together with help from an AI research assistant that read Langmuir and Razorweld documents and Langmuir forum posts. Where a page says "I" or "my", it means me and my machine. **Most of this is compiled research I haven't tried yet**; each page has a status line saying which. Not affiliated with Langmuir Systems, Razorweld, or Jasic. **Follow the manufacturers' manuals, safety instructions, and support advice over anything here.** More in [About this site]({{< relref "/about.md" >}}), including a glossary.

## My setup

- **Table:** Langmuir CrossFire PRO, 48 x 33 in cut area, ACME lead screws, IHS standard, Langmuir THC added. Electronics on 120 V, in an enclosure wall-mounted away from the table.
- **Cutter:** Razorweld CUT45 CNC (model JRWPC45LH; Langmuir sells it as the "Razorweld Razorcut 45 with Machine Torch") on **230 V** (20–45 A), X45 machine torch in the Machine Torch Mount.
- **Air:** Ingersoll-Rand SS3L3 60-gallon compressor → IR D18IN refrigerated dryer → Harbor Freight filter → cutter.
- **Software:** Inkscape and Fusion (design), SheetCAM 8.0 with the FireControl post v1.6 (CAM), FireControl (machine control).
- **Materials:** mild steel, stainless, and aluminum, mostly 3/16 in and thinner.
- **Shop:** a home shop.

<figure class="chart-figure"><a href="{{< relurl "images/bernie-shop-setup.jpg" >}}"><img src="{{< relurl "images/bernie-shop-setup.jpg" >}}" alt="My shop setup: CUT45 on a shelf above the Ingersoll-Rand D18IN dryer, IR SS3L3 compressor, wall-mounted Langmuir electronics enclosure, and the CrossFire PRO gantry with the X45 torch" loading="lazy"></a><figcaption>My setup: the CUT45 and the Ingersoll-Rand dryer and compressor, the wall-mounted electronics enclosure, and the CrossFire PRO with the X45 torch. Tap to enlarge.</figcaption></figure>

## How to read these pages

- **Status line.** Every procedure page starts with one of: **Tested on my machine** (nothing yet), **Used by me, not formally tested**, or **Compiled research, not yet tried**. The FireControl scenario pages (FC-02 to FC-07) are marked **Reference: compiled from Langmuir docs and forum threads**, and the test-cut pages are marked **planned**.
- **How sources are weighted:** Langmuir's own documents and staff first, then the Razorweld/Jasic manuals (my JRWPC45LH operating manual first; the online Razorcut 45 DI manual is for a related but different model and is used only where mine is silent), then experienced forum members, then everyone else. Every number says where it came from. Numbers from members with a different plasma cutter are only a rough guide for the CUT45.
- **Cut charts.** I couldn't find a published X45 machine-torch cut chart (as of October 2026). My starting chart came from Razorweld: they sent it to forum member MO-Hacker, who posted it (<https://forum.langmuirsystems.com/t/847/29>). Because it's manufacturer data, it's weighted just below Langmuir's own documents. I've cut with these settings and they worked well, but they haven't been formally tested yet. A second candidate is a **T45m-format chart** (laid out like Hypertherm's Powermax45 charts; T45m is Hypertherm's Powermax45 machine torch) that FSFab says Jasic supplied (<https://forum.langmuirsystems.com/t/45011>; origin unconfirmed). Its arc voltages (111–123 V) disagree with the Razorweld chart's (139–152 V). The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) is how I plan to settle that.
- **Safety items** (house wiring, grounding the supply, fumes from coated or galvanized stock) go to the manufacturers' documents. See <https://www.langmuirsystems.com/pages/safety> and the operating manual that came with my cutter (JRWPC45LH).
- **Test results** go in the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}). It has planned rows for test sessions S01 (16 ga mild steel), S04 (3/16 in mild steel), and the optional S04B (3/16 in mild steel, T45m-format chart at 45 A vs. Razorweld chart at 40 A). Results then go into each page's "Bernie's test results" section.

## Site map

- [About this site]({{< relref "/about.md" >}}): who wrote this, what's tested, how sources are weighted, and a glossary.
- [Charts]({{< relref "/charts.md" >}}): the Razorweld chart and the T45m-format charts as images. The typed-in tables are on the [cut settings page]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}).
- [Test-cut log]({{< relref "/testing/test-cut-log.md" >}}): the planned and logged coupons, with a CSV download.
- [Sources]({{< relref "/sources.md" >}}): every forum and official link.

## Procedures

1. [THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})
2. [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}})
3. [Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})
4. [CUT45 cut settings: starting points and dialing in]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}}). Razorweld-supplied chart first; T45m-format chart reportedly from Jasic as a second candidate (the voltage conflict is spelled out).
5. [Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}})
6. [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})
7. [Kerf width and hole/part accuracy]({{< relref "/procedures/08-kerf-and-hole-accuracy.md" >}})
8. [SheetCAM 8.0 setup for FireControl]({{< relref "/procedures/09-sheetcam-setup.md" >}})
9. [Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}})
10. [Test-cut program: checking the starting settings]({{< relref "/testing/test-cut-program.md" >}}), with a [printable worksheet]({{< relref "/testing/test-cut-worksheet.md" >}}). The order is: a speed ladder, then a 3-way THC voltage test (SMART voltage vs. the Razorweld chart's voltage vs. the T45m-format chart's voltage), then pierce delays. An optional session (S04B) compares the two charts head to head on 3/16 in mild steel.
11. [Indexing parts longer than the table]({{< relref "/procedures/01-indexing-long-parts.md" >}}). Compiled research, kept for reference and listed last, since my parts fit within the PRO’s roughly 33 in of Y travel.

### FireControl

- [FC-01: Straight Cut starting at the plate edge]({{< relref "/firecontrol/fc-01-straight-cut-edge-start.md" >}}). Method 1 (a scrap lead-in piece) is the one I've used, a few times; not formally tested. Methods 2 and 3 are collected from forum posts and haven't been tried.
- [FC-02: Scenario: FireControl won't open ("Child process exited with code 1")]({{< relref "/firecontrol/fc-02-child-process-crash.md" >}}). The most-viewed FireControl problem on the forum. Reference: compiled from Langmuir docs and forum threads.
- [FC-03: Scenario: FireControl won't connect]({{< relref "/firecontrol/fc-03-wont-connect.md" >}}): CrossFire greyed out, or only a COM port shows. Reference: compiled from Langmuir docs and forum threads.
- [FC-04: Scenario: connection lost or frozen mid-cut, computer side]({{< relref "/firecontrol/fc-04-connection-lost-mid-cut.md" >}}). Check EMI in [grounding]({{< relref "/procedures/03-grounding-and-emi.md" >}}) first. Reference: compiled from Langmuir docs and forum threads.
- [FC-05: Scenario: resuming a cut after a stop]({{< relref "/firecontrol/fc-05-resume-run-from-here.md" >}}): Resume, Run From Loop or Line, and M00 pauses. Reference: compiled from Langmuir docs and forum threads.
- [FC-06: Scenario: the part cuts in the wrong place]({{< relref "/firecontrol/fc-06-work-zero-program-origin.md" >}}): work zero, Set Program Origin, and the SheetCAM origin. Reference: compiled from Langmuir docs and forum threads.
- [FC-07: Scenario: a program won't load]({{< relref "/firecontrol/fc-07-program-wont-load.md" >}}): No Program Speed Found, Program Check error, Unsupported GCode. Reference: compiled from Langmuir docs and forum threads.

## Quick-start values (Langmuir SheetCAM guide example tool for a Razorweld 45A cutter on the PRO; test before trusting)

Pierce height 0.15 in · pierce delay 0.5 s · plunge 50 ipm · cut height 0.08 in in SheetCAM (about 0.060 in real; heights also match the T45m-format chart reportedly from Jasic, see [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})) · kerf 0.06 in · air 75 psi · THC defaults (SMART voltage, 85 % cutoff, 5 % Z-speed).

Feed rate and amps: start from the Razorweld chart's Optimum column ([CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})), then check them with the [test-cut program]({{< relref "/testing/test-cut-program.md" >}})'s speed ladder.

## Questions I plan to ask Langmuir or Razorweld support (no answers yet)

1. On a PRO with the stainless water table, where should the work clamp go now: frame, drain plug, slat bed, or workpiece? (Langmuir's documents give different locations.)
2. Can Razorweld confirm the chart it gave MO-Hacker (t/847/29) is for the X45 machine torch, and which arc voltages are right? Is there an official X45 machine-torch cut chart: amps, speed, kerf, pierce delay, and arc voltage by thickness?
3. Which trigger mode (2T or 4T) should the CUT45 be in for CNC use? (My manual describes both, p. 10, but doesn't say which to use with the CNC port.)
4. Is the CUT45's output range 20–45 A or 20–40 A? My manual says both on the same page (p. 8). I'm treating it as 45 A.

## Answered or decided

- **Which manual applies to my cutter:** my Razorweld **JRWPC45LH** operating manual ("CNC - CROSSFIRE COMPATIBLE", unit "Razorweld CUT45 CNC", built by Jasic). I couldn't find an electronic copy online (October 2026), so the pages cite my printed copy. They cite it as "my JRWPC45LH operating manual, p. N". The online **Razorcut 45 DI** manual that earlier versions of this site cited is for a related but different model, so the pages now say so wherever they use it. See [Sources]({{< relref "/sources.md" >}}).
- **Residential-supply (EMC Class A) warning:** dropped. It came from the Razorcut 45 DI manual, not my JRWPC45LH manual, whose safety section (pp. 4–6) has no such wording. House wiring and the 230 V circuit are still a licensed electrician's job, and I follow my manual and Langmuir's safety page.
- **X45 nozzle RW51206 orifice size:** working answer **1.0 mm (0.040 in)**, per forum member mechanic416 (<https://forum.langmuirsystems.com/t/21266>), consistent with the torch diagram's "20–50 amp" label. Worth confirming with Razorweld only if it matters.
- **X45 retaining cup part number:** Razorweld's number is **RW60305T** (my manual, p. 15: "RW60305T End Retaining Cap"; my X45 torch diagram agrees). Langmuir's listing shows RW603505T, which looks like a typo there; I order from Langmuir's X45 retaining cap page ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})).
- **Duty cycle:** **30 % at 45 A, at 104 °F** (my manual, p. 8). The 25 % figure was the DI model's.
- **Supply voltage:** **230 V single-phase ±15 %** (my manual, p. 8). The 120 V and 95–265 V figures were the DI model's.
- **Air:** **0.5 MPa (75 psi), 6.7 CFM**, with the pressure preset at the factory (my manual, pp. 8 and 13).
- **Trigger modes and lights:** 2T and 4T only, no Mesh mode (pp. 8–10). Overheating, torch protection, and gas-check indicator lights instead of error codes (p. 9).
- **Electrode pit depth, arc transfer distance, gas-check time-out, no-load voltage, and a cut chart:** **not in my manual.** The pages keep Langmuir's 1/16 in pit rule, the Razorweld-supplied cut chart, and the DI manual's figures (labeled as the related model's) for the rest.
- **CNC ports:** my manual names a "CNC Torch On/Off Port" and a "CNC 50:1 Voltage Divider Port" (p. 9) and calls the CrossFire hookup "plug and play" (pp. 3 and 14). It gives no pin-out, so the port-swap check in [THC setup]({{< relref "/procedures/02-thc-setup-and-diving.md" >}}) stays.
