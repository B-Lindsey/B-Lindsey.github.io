---
title: "About This Site"
date: 2026-10-30
lastmod: 2026-10-30T18:30:00-07:00
draft: false
showTableOfContents: true
summary: "Who wrote these CrossFire PRO notes, how they were researched, what's tested and what isn't, and a glossary of the terms used."
---

{{< lastupdated >}}

## About this site

These are my personal notes (Bernie Lindsey). I've run my CrossFire PRO since August 2024. I put them together with help from an AI research assistant that read Langmuir and Razorweld documents and Langmuir forum posts. Where a page says "I" or "my", it means me and my machine: a CrossFire PRO with THC, a Razorweld CUT45 CNC (model JRWPC45LH) on 230 V with the X45 machine torch, and a wall-mounted electronics enclosure, in a home shop. The full list is under "My setup" on the [home page]({{< relref "/_index.md" >}}).

The site is **unlisted**: it isn't in search engines, but anyone with the link can read it. I'm sharing it in case it helps other CrossFire owners.

## What's tested and what isn't

**Most of this site is compiled research that I haven't tried yet.** The settings from the forum-posted Razorweld chart have worked well for me, and I've used the scrap lead-in edge start ([FC-01]({{< relref "/firecontrol/fc-01-straight-cut-edge-start.md" >}}) Method 1) a few times. Nothing here has been formally tested yet. The [test-cut program]({{< relref "/testing/test-cut-program.md" >}}) is how I plan to do that.

Each page starts with a status line:

- **Tested on my machine:** cut and logged in the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}). Nothing has reached this yet.
- **Used by me, not formally tested:** I've done it and it worked, but there are no measured results.
- **Compiled research, not yet tried:** collected from the sources listed on the page.
- **Reference: compiled from Langmuir docs and forum threads:** the FireControl scenario pages (FC-02 to FC-07). They collect common problems forum members run into, with the fixes the forum and Langmuir settled on. They're for looking things up, not steps I've run.
- **Planned:** the test-cut program, worksheet and log. No results are logged yet.

Where a page says "Starting choice", "my starting choice" or "suggested starting point", that's the setting I plan to start from, not a result.

## How sources are weighted

1. Langmuir's own documents and staff.
2. Razorweld/Jasic manuals and manufacturer-supplied charts. My own JRWPC45LH operating manual comes first (my printed copy; cited as "my JRWPC45LH operating manual, p. N"). The online Razorcut 45 DI manual is for a related but different model, so its figures are used only where mine is silent, and are labeled.
3. Experienced forum members whose posts are cited often here (for example TomWS/TinWhisperer, ChelanJim, Bigdaddy2166, richarddbeck83, 72Pony, Cletus, Wsidr1, Holla2040).
4. Other long-time forum members.
5. Everyone else.

Every number on the site says where it came from. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.** Forum members are quoted from public posts, with links. The forum citations were gathered with the research assistant, and not every quote has been checked against the full thread, so read the linked post before relying on it.

## Not official

I'm not affiliated with Langmuir Systems, Razorweld, or Jasic. **Always follow the manufacturers' manuals, safety instructions, and support advice over anything here.** Settings are starting points, not proven values. Corrections are welcome on the Langmuir forum.

## Glossary

- **CUT45 (JRWPC45LH):** my cutter, the Razorweld CUT45 CNC, model JRWPC45LH, built by Jasic. Langmuir sells it as the "Razorweld Razorcut 45 with Machine Torch". Earlier versions of this site called it the "Razorcut 45" or "Razorweld 45". The **Razorcut 45 DI** is a related but different Razorweld model with its own manual.
- **THC (torch height control):** Langmuir's add-on that reads the arc voltage during a cut and moves Z to keep the torch at a steady height.
- **Arc voltage / Live Volts:** the voltage across the arc while cutting. Higher voltage means a higher torch. The CUT45's divider port sends it to the THC divided by 50 (the "50:1" port).
- **SMART voltage:** the THC setting (Nominal Voltage = 0) that reads the arc voltage right after IHS and holds it for the rest of that cut loop. Langmuir staff recommend it.
- **IHS (initial height sensing):** the PRO touches the torch to the plate before each pierce to find the surface, then lifts to the pierce height. It uses a floating-head switch.
- **Pierce height / pierce delay:** how high the torch sits while the arc first burns through the plate, and how long it waits there before moving.
- **Cut height vs. real gap:** the cut height typed into SheetCAM (0.08 in) is larger than the actual gap under the torch (about 0.060 in), because the floating head springs back after IHS. See [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}}).
- **Kerf:** the width of the cut slot. CAM offsets the toolpath by half of it so parts come out the right size.
- **Dross / bevel:** dross is the re-solidified metal stuck to the bottom edge; bevel is an edge that isn't square.
- **Razorweld chart:** the CUT45 cut chart Razorweld sent to forum member MO-Hacker (t/847/29). It's my starting chart. Its **Optimum** column is the suggested feed; **Max** is the fastest that will still sever the metal.
- **T45m-format chart:** a CUT45 chart that forum member FSFab says Jasic supplied (t/45011). Its layout and its "T45m shielded consumables" label match Hypertherm's Powermax45 charts (T45m is Hypertherm's Powermax45 machine torch), so its origin is unconfirmed.
- **Post processor ("post"), v1.6:** the SheetCAM or Fusion file that turns toolpaths into G-code FireControl understands. Langmuir's current one is v1.6.
- **Test sessions S01–S11:** one session per material and thickness in the [test-cut program]({{< relref "/testing/test-cut-program.md" >}}). For example S01 = 16 ga mild steel and S04 = 3/16 in mild steel. **S04B** is an optional extra session on 3/16 in mild steel that compares the T45m-format chart's 45 A settings with the Razorweld chart's 40 A settings.
- **Coupon codes within a session:** L1–L5 = a speed ladder (chart feed −20 % to +20 %); H1/H2 = height-reference lines for reading voltage at a known gap; T1/T2 = THC fixed at the Razorweld or T45m-format chart's voltage; P1/P2 = pierce-delay checks; V1 = a final verification coupon with the measured kerf.
- **Forum links like t/847/29:** thread 847, post 29 on forum.langmuirsystems.com.
