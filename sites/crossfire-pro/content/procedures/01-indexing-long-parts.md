---
title: "Indexing Parts Longer Than the Table"
date: 2026-10-28
tags: ["cnc", "plasma", "crossfire-pro", "indexing", "firecontrol", "fusion", "sheetcam"]
draft: false
weight: 11
lastmod: 2026-10-30T16:15:00-07:00
summary: "How to cut a part longer than the CrossFire PRO's 33 in of Y travel by splitting it into two programs and sliding the sheet. Compiled from Langmuir features and forum methods."
series: ["CrossFire PRO procedures"]
series_order: 11
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.**

## Applies to

Written for my setup: a CrossFire PRO with 48 in (X) x 33 in (Y) cut area, ACME lead screws, IHS standard, Langmuir THC installed, no Limit Switch Kit unless I add one. Torch is the Razorweld X45 machine torch in the Machine Torch Mount, on a Razorweld CUT45 CNC (model JRWPC45LH) running on 230 V. Langmuir says a full 4 x 8 sheet can pass through the PRO front to back, so a long part has to lie along **Y**. The PRO can't be expanded to 4 x 8. Doesn't cover: the XR has 48 x 96 travel and needs no indexing. The PRO MAX (48 x 48) and the original CrossFire/XL have different travel limits. The Mach3 indexing write-ups are for Gen1 legacy machines.

I couldn't find an **official Langmuir indexing or tiling procedure** (as of October 2026). The steps below combine Langmuir's own features (zeroing, Dry Run, Go to XY Zero, the Marker Pen) with community methods. Try the method on scrap first.

## Before you start

- Check that the gantry is square (see [Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}})). Any racking error shows up twice when you index.
- Have adjustable-height stands ready. Langmuir recommends them for any sheet hanging off the table.
- A full sheet is heavy and the edges are sharp. Use gloves and get help lifting.

## Steps

1. **Orient the part.** In Fusion or Inkscape, turn the part so its long side runs along Y (front to back).
2. **Pick the split line(s).** Each segment has to fit inside the 33 in Y travel with room to spare. Community examples: segments laid out to fit a 32 x 48 window (JPep, thread 20780) and 30 in segments (Brian344, same thread). Put each split across a straight section of the part, not on a curve or a small feature.
3. **Split the drawing into separate programs that share one origin.**
   - Program A holds everything from Y = 0 up to the split line.
   - Program B holds the rest, moved by exactly the index distance **D** toward −Y (for example, 30.000 in). Use the same X zero and the same coordinate system (JPep, 20780).
   - JPep breaks the profile at the split with a 0.001 in gap so each program gets an open path that ends right at the split. Don't overlap the lines. A double-cut leaves a notch.
   - Put lead-ins in scrap, not at the split. Leave out lead-outs on the THC table (see [THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
4. **Set a fence along Y.** Clamp a straight bar on the slats, parallel to Y travel, for the sheet's left edge to ride against. To check it's parallel, put the Marker Pen (or a pointer) in the torch mount and jog the full Y travel along the fence. The gap shouldn't change.
5. **Set a stop for the index distance.** Clamp a stop block on the fence, or make two scribe marks D apart on the sheet. Mark them both on the sheet and on a fixed point of the table.
6. **Zero the machine.** Jog to your corner and use **ZERO ALL AXES**. IHS sets Z, so don't zero Z by hand. Write down the DRO position of a physical reference: tape a scrap of tape on the frame and line up a mark on it.
7. **Dry run Program A.** FireControl Dry Run mode runs with no plasma and no Z moves. Watch for anything running off the sheet or hitting a clamp.
8. **Cut Program A.**
9. **Don't move the gantry zero.** With the torch parked up and out of the way, slide the sheet by exactly D toward −Y, so the line that was at Y = D now sits at Y = 0. Check which physical direction −Y is on your table by jogging first. Keep it against the fence until it hits the stop or the marks line up.
10. **Check the alignment before cutting.** Load Program B and use "Go to XY Zero". Jog the marker or pointer to one end of the cut from Program A and confirm it lands on the cut. Brian344 (20780) dry-runs with a pointer before each segment.
    - If it's off in Y, re-slide the sheet. Re-zeroing to make up for a bad slide works, but then your reference is the cut, not the fence.
11. **Dry run Program B, then cut it.**
12. **Measure the joint.** Look for a step (an X error) and a gap or overlap (a Y error). Write it in the test-cut log.

## Symptoms -> causes -> fixes

| Symptom at the split | Likely cause | Fix |
|---|---|---|
| Step sideways (X) | Sheet moved off the fence, or fence not parallel to Y | Re-check the fence with the marker (step 4). Clamp the sheet lightly to the fence while sliding. |
| Gap or overlap along Y | Index distance D wrong, or the stop moved | Measure D with a steel rule or tape, re-set the stop, and check with "Go to XY Zero" before cutting. |
| Segments meet at an angle | Gantry out of square, or the sheet rotated while sliding | Square the gantry ([Squaring the gantry and fixing lost steps]({{< relref "/procedures/10-gantry-squaring-and-lost-steps.md" >}})). Use two fence contact points. |
| Notch or double-burn at the join | The two programs overlap at the split | Break the path at the split (0.001 in gap, JPep). Keep lead-ins away from the split. |
| Lost position after a pause | Gantry was jogged, or the zero was overwritten | Re-find the cut from Program A with the pointer and re-zero there. Use Run From Here for the rest. |

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

- **Indexing pin vs. scribe line** (t/21633#2).
  - The idea (DRotblatt, long-time forum member): put a 1/8 in pin about 0.25 in in from the X25/Y0 corner as a stop. Have Program A cut a 0.125 in index hole in the sheet. Slide the sheet, drop the hole over the pin, then run Program B.
  - **TomWS** (experienced forum member) replied that he doubts a plasma-cut index hole is any more accurate than lining up a scribe line.
  - **Suggested starting point:** use the scribe line or stop block plus the pointer check (steps 5 and 10). Treat the pin as an experiment; if you try it, measure the joint (step 12) and compare.
- **TinWhisperer** points to his video for cutting images larger than the table (t/46165). The thread has no written steps; watch the video before trying anything different.
- No Langmuir staff advice on indexing turned up in the research.

## Where sources disagree (and the starting choice)

- **Index pin vs. scribe line** (t/21633). A plasma-cut pin hole has kerf and dross, so it's only as good as the cut. TomWS doubts it beats a scribe line. **Starting choice: follow TomWS** (scribe line or stop, plus the pointer check).
- **Re-zero after sliding vs. not re-zeroing.** A community method (threads 20200, 8748, 13570) is to slide against blocks and run the second program **without re-zeroing**. Brian344 (20780) checks each segment with a pointer. **Starting choice: combine them.** Keep the zero (fewer places to make a mistake) **and** check with the pointer before firing. These are general forum posters; no Langmuir staff or frequently cited members posted on this in the threads found.
- **Work offsets.** FireControl has stored work coordinates, but homing and work offsets need the **Limit Switch Kit**, which isn't standard on the PRO. Without the kit, don't count on returning to a stored offset after a power cycle.

## Sources

- Langmuir, CrossFire PRO page (full sheet passes through; use stands; can't expand to 4 x 8): <https://www.langmuirsystems.com/pages/crossfire-pro>
- Langmuir, CrossFire PRO product page: <https://www.langmuirsystems.com/products/crossfire-pro-cnc-plasma-table>
- Langmuir, FireControl guide (zeroing, Go to XY Zero, Run From Here): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, FireControl page (Dry Run mode): <https://www.langmuirsystems.com/pages/firecontrol>
- Langmuir, Limit Switch Kit (needed for homing and work offsets): <https://www.langmuirsystems.com/products/limit-switch-kit-for-crossfire-and-crossfire-pro>
- Langmuir, PRO assembly (gantry squaring step): <https://www.langmuirsystems.com/pages/pro-assembly>
- Langmuir, Safety: <https://www.langmuirsystems.com/pages/safety>
- FireShare user project, "Crossfire Pro Index and squaring gauge" (community): <https://fireshare.langmuirsystems.com/projects/crossfire-pro-index-and-squaring-gauge-3150>
- Forum (general forum members): <https://forum.langmuirsystems.com/t/20780> (JPep, Brian344)
- Forum (community; summarized from search results, not checked against the full thread): <https://forum.langmuirsystems.com/t/20200>, <https://forum.langmuirsystems.com/t/8748>, <https://forum.langmuirsystems.com/t/13570>
- Forum: <https://forum.langmuirsystems.com/t/21633> (#2 TomWS: pin vs. scribe line; DRotblatt pin method), <https://forum.langmuirsystems.com/t/46165> (TinWhisperer video on big images)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will come from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) and be listed here with: Date; Material / thickness; Index distance D; X step at join; Y gap/overlap; Method used; Notes.
