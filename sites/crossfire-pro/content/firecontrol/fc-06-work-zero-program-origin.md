---
title: "Scenario: The Part Cuts in the Wrong Place (Work Zero, Set Program Origin, and the SheetCAM Origin)"
date: 2026-10-30
tags: ["cnc", "plasma", "firecontrol", "work-zero", "program-origin", "sheetcam", "soft-limits", "crossfire-pro"]
draft: false
weight: 6
lastmod: 2026-10-30T16:15:00-07:00
summary: "The part cuts in the middle of the sheet, off the edge, or FireControl says it's out of bounds. On a PRO without limit switches there are three things to line up: where the torch is when you press Zero All Axes, which corner Set Program Origin points at, and where SheetCAM put the part relative to its origin."
---

{{< lastupdated >}}

**Reference: compiled from Langmuir docs and forum threads.**

## Applies to

A CrossFire PRO with THC and IHS and **no Limit Switch Kit** (my table has none), with programs from SheetCAM 8.0 (Langmuir post). Drawings come from Inkscape or Fusion.

- **Versions:** FireControl 21.1.x and 24.1.6. Set Program Origin and Zero All Axes are on Langmuir's FireControl features page.
- **No limit switches** means there's no machine home and no soft limits. Langmuir staff say the kit "is what is required to home and use soft / hard limits" (t/19048/2). The homing and soft-limit notes below are only for readers who have the kit.
- **Related:** [SheetCAM setup]({{< relref "/procedures/09-sheetcam-setup.md" >}}) and [Indexing long parts]({{< relref "/procedures/01-indexing-long-parts.md" >}}), which uses Zero All Axes with a shared origin.
- Check the fixes with a small test file before a real sheet.

## Symptom (what you'll see)

- The part cuts **far from where the torch was zeroed**, for example in the middle of the sheet.
- The part is **offset by its own width or height**.
- After a **rotate**, the origin sits in the middle of the part.
- A **circle** doesn't start where expected.
- The cut **runs off the sheet or into the frame**.
- With the Limit Switch Kit: **"Out of range"**, "out of bounds", or "Program Check Encountered an Error".

## Likely causes

There are three origins, and the part lands in the wrong place when they don't line up (per Langmuir staff and experienced forum members). Most likely first:

1. **The SheetCAM origin is in one corner and the part in another.** The SheetCAM origin is the corner of SheetCAM's red sheet rectangle that you chose as the origin. "Wherever you put the part on that red rectangle is where Sheetcam will put it in relation to your chosen table origin" (ds690, t/46038/33). That was TheRock's six-year mistake, fixed in t/46038/34.
2. **The program origin corner doesn't match the zero corner.** The **program origin** is the point of the drawing that FireControl puts at the work zero. Langmuir: "Change the origin location of your program directly in FireControl" (features page). Click **Set Program Origin**, and green boxes appear on the corners and the middle of the drawing (ChelanJim, t/34321/2; ds690, t/46038/4).
3. **The work zero isn't where you meant it.** The **work zero** is where the torch is when you press **Zero All Axes**. ChelanJim: it's "the location that you plan for your torch to represent the 'Program Origin'" (t/34321/2).
4. **A rotate moved the program origin** (ChelanJim, t/33962/28).
5. **FireControl's origin box on circles.** ds690 warns that "Firecontrol does weird stuff when the drawing is a circle" (t/46038/4).
6. **No soft limits** on a PRO without the kit, so nothing stops a program that runs past the sheet (staff, t/19048/2). With the kit, a program past the soft limits gives the Program Check error (PRO troubleshooting; t/31188).

**Machine home** is just where the machine parks. Without limit switches it has no bearing on this (Craig1, t/46038/31).

## Fixes (most to least likely)

### 1. Place the part the same way at every step

1. **In SheetCAM, put the part at the origin corner.** If the origin is bottom-left, move the part so its bottom-left is at or just inside the origin, then post. Do the same in Inkscape or Fusion before exporting (ds690, t/46038/33; Craig1, #31).
2. **Load it in FireControl.** Fix any errors first ([Scenario: a program won't load]({{< relref "/firecontrol/fc-07-program-wont-load.md" >}})).
3. **Click Set Program Origin and pick the same corner** you'll zero on. Do it every time, especially after **rotating**. ChelanJim has had the origin end up in the middle of the part after a rotate, so he always picks it again (t/33962/28).
4. **Jog the torch to that corner of the sheet**, plus your edge margin, and press **Zero All Axes**. IHS sets the Z height, so you don't need to zero Z by hand ([Indexing long parts]({{< relref "/procedures/01-indexing-long-parts.md" >}})).

### 2. Check the fit before cutting

- Jog the torch around the design's extents, using the visualizer as a guide, to check it fits on the sheet and inside the travel. ds690 (t/26050/3) and Langmuir staff (t/19048/2) both describe this.
- Or run a **Dry Run** ("without Plasma firing and Z-axis moves"; features page). Staff say a Dry Run also checks it, "albeit likely slower" (t/19048/2).

### 3. Circles

The origin may not line up with the circle's edge (ds690, t/46038/4). Check a circle's position by jogging before you cut, and adjust the zero.

### 4. If you have the Limit Switch Kit (my table doesn't)

- The machine homes to the **back-left** (upper-left) corner. Most CAD and CAM programs default to a lower-left origin, which is where much of the confusion comes from (ds690, t/31188/2; t/34324).
- "Out of range" or "out of bounds" with soft limits on usually means the work zero and the program's position don't fit inside the soft limits. Re-zero so it fits, and check the soft limits.
  - The troubleshooting page lists G-code past your soft limits as a common cause of "Program Check Encountered an Error".
- **Break-in program out of bounds:** disable soft limits in Machine Settings, run it, then re-enable them (langmuir-reilly, t/30621/4).
- **Typed coordinates:** staff's sequence is Home > set the work coordinates in the DRO > Go to Work Zero (t/26293/2). When that gave a limit error, staff suggested flipping the signs, e.g. (-13, 13) (t/26293/4).
- **Homing in the wrong direction:** use Reset Defaults in Machine Settings (PRO troubleshooting).

### Quick lookup

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Part cuts far from where the torch was zeroed | SheetCAM origin in one corner, part in another | Move the part to the origin in SheetCAM, then repost (t/46038/31, /33, /34) |
| Part offset by its own width or height | Program origin corner doesn't match the zero corner | Set Program Origin to the corner you zeroed (t/34321/2) |
| Origin in the middle of the part after a rotate | Rotate moved the program origin | Pick the program origin again after a rotate (t/33962/28) |
| Circle doesn't start where expected | FireControl's origin box on circles | Check by jogging; adjust the zero (t/46038/4) |
| Runs off the sheet or into the frame (no limit switches) | No soft limits on a PRO without the kit | Jog the extents or Dry Run first (staff, t/19048/2) |
| "Out of range" / Program Check error (with the kit) | Program past the soft limits | Re-zero so it fits; check soft limits (PRO troubleshooting; t/31188) |

## Where sources disagree

- **Fix it in CAM or in FireControl?** TinWhisperer and ds690 say Set Program Origin can fix it without going back to Fusion (t/26050/2; t/46038/4). Craig1 and ds690 (#31, #33) say to fix SheetCAM's part placement, and that's what solved t/46038. These aren't really in conflict. **Starting choice: place the part at the SheetCAM origin first, then use Set Program Origin** to choose the corner.
- **"Override" or "generate" re-zeroing.** Sticks reports that after an override, the generate step may re-zero to wherever the torch is (t/41980/26). No staff confirmation turned up in the research, so treat it as **unverified**. Check the work zero after any regenerate.

## What experienced forum members add

- **ChelanJim**, t/34321/5: made annotated screenshots of the FireControl screen explaining these terms.
- **TinWhisperer**, t/46038/2: you can't type in a coordinate to move to (as of Nov 2025). Users have asked for it for years. You jog and Zero All Axes.
- **DKent**, t/46038/35: the CAD > SheetCAM > FireControl origin chain is "a topic not well discussed". That's why this page exists.

## Safety

Jogging the extents moves the torch over clamps and tip-ups. Keep hands clear and the **Razorweld CUT45 CNC (model JRWPC45LH) off** while jogging and dry-running. Before **Go to XY Zero**, check the DRO for a safe path. The button rapids at 300 IPM (FireControl guide).

## Sources

- Langmuir, FireControl features (Set Program Origin; Dry Run): <https://www.langmuirsystems.com/pages/firecontrol>
- Langmuir, FireControl guide (Go to XY Zero): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, PRO troubleshooting (Program Check error; homing direction): <https://www.langmuirsystems.com/pages/protroubleshooting>
- Forum: <https://forum.langmuirsystems.com/t/46038> (TinWhisperer #2; ds690 #4, #33; Craig1 #31; TheRock #34; DKent #35)
- Forum: <https://forum.langmuirsystems.com/t/34321> (ChelanJim #2, #5)
- Forum: <https://forum.langmuirsystems.com/t/26050> (TinWhisperer #2; ds690 #3)
- Forum, staff: <https://forum.langmuirsystems.com/t/19048/2>; <https://forum.langmuirsystems.com/t/26293> (#2, #4); <https://forum.langmuirsystems.com/t/30621/4> (langmuir-reilly)
- Forum: <https://forum.langmuirsystems.com/t/31188/2> (ds690); <https://forum.langmuirsystems.com/t/34324>; <https://forum.langmuirsystems.com/t/33962/28> (ChelanJim); <https://forum.langmuirsystems.com/t/41980/26> (Sticks)
