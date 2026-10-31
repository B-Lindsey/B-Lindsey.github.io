# CrossFire PRO Procedures & Reference

Step-by-step procedures and reference notes for running a **Langmuir Systems CrossFire PRO** CNC plasma table. I wrote them for my own shop and turned them into a small website.

**Live site:** <https://b-lindsey.github.io/>

## Purpose

The Langmuir forum has years of good advice, but it's spread across thousands of threads, and much of it applies to a different CrossFire model or plasma cutter. This site pulls the parts that apply to my setup into clear procedures that cite their sources. It's mainly for my own use, and other CrossFire owners may find it useful too.

## My setup

- Langmuir Systems CrossFire PRO with torch height control (THC), owned since August 2024
- Razorweld CUT45 CNC plasma cutter, model JRWPC45LH, with the X45 machine torch
- Ingersoll-Rand SS3L3 compressor, then an Ingersoll-Rand D18IN refrigerated dryer, then a final filter
- Inkscape and Fusion for design, SheetCam for toolpaths and G-code, FireControl to run the table
- Mostly mild steel, stainless, and aluminum, 3/16 in and thinner

## What's on the site

- **Procedures:** indexing parts longer than the table, THC setup and torch dives, grounding and electrical noise, air quality and consumables, cut settings, dross and bevel, pierce height and delay, kerf and hole accuracy, SheetCam setup, and gantry squaring and lost steps.
- **FireControl:** common FireControl problems and fixes.
- **Testing:** a test-cut program, a worksheet, and a log of my real settings and results.
- **Charts and Sources:** cut charts, plus every source the pages cite, grouped by who published it.

## How sources are weighted

1. Langmuir Systems documentation and staff
2. Manufacturer manuals and cut charts, starting with my own JRWPC45LH manual
3. Experienced forum members whose advice others have confirmed
4. Everyone else

Where sources disagree, the page says so and explains which one I trust and why. On safety (grounding, electrical work, and fumes from galvanized or coated metal), the manufacturer's guidance always wins.

## How this repository works

- The site is built with [Hugo](https://gohugo.io/) and the [Blowfish](https://blowfish.page/) theme.
- This repository holds only the **built site**, in the `docs/` folder. GitHub Pages serves it from the `master` branch, `/docs` folder. The `.nojekyll` file tells GitHub not to run Jekyll on it.
- The Hugo source (Markdown content, config, and theme) is kept separately and isn't in this repository.
- To update the site, rebuild it from the source and replace `docs/` through a pull request.

## Disclaimer

This is a personal project. It isn't affiliated with or endorsed by Langmuir Systems, Razorweld, or Jasic. Plasma cutting involves high voltage, compressed air, heat, and fumes, so follow the manufacturers' manuals and safety instructions. Use these notes at your own risk.
