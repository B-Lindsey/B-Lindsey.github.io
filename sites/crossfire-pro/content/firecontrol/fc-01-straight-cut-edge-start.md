---
title: "FireControl Straight Cut: Starting a Cut at the Plate Edge"
date: 2026-10-28
tags: ["cnc", "plasma", "firecontrol", "straight-cut", "edge-start", "ihs", "thc", "crossfire-pro"]
draft: false
weight: 1
lastmod: 2026-10-30T18:30:00-07:00
summary: "Three ways to start a FireControl Straight Cut right at the plate edge with IHS on a CrossFire PRO. Method 1, a scrap lead-in piece, is the one I've used."
---

{{< lastupdated >}}

**Status: Method 1 used by me a few times; not formally tested. Methods 2 and 3 are compiled research, not yet tried.**

## Applies to

Written for my setup: a CrossFire PRO with IHS and THC, FireControl's **Straight Cut** tool, the Razorweld CUT45 CNC (model JRWPC45LH) on 230 V, and the X45 machine torch. The job is a straight cut that has to start right at the edge of a plate, like trimming a sheet or cutting a strip.

Doesn't cover: Mach3 / Gen1 legacy machines, or programs made in SheetCAM or Fusion. Those use the post's IHS sequence ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})), not the Straight Cut tool.

I couldn't find a written Langmuir edge-start procedure for the Straight Cut tool (as of October 2026). **Method 1 is the one I use; I've used it a few times and it worked, but it isn't formally tested.** Methods 2 and 3 are worked out from forum posts and **haven't been tried.** Try every method on scrap first.

## What the Straight Cut tool does (per Langmuir staff and support)

From <https://forum.langmuirsystems.com/t/20335>:

- **IHS on** (support's answer, quoted in post #4): "In Straight Cut mode, IHS will automatically set pierce height to 0.15" and THC will automatically set cut height to 0.06". These defaults cannot be changed at this time."
- **IHS off** (Langmuir staff, account `langmuirsystems`, post #5):
  - The tool only does XY moves.
  - The cut height is **wherever the Z axis is sitting** when you press start.
  - "The no-IHS straight cut program does not have THC enable and disable commands so THC will not activate."
- ChelanJim (experienced forum member) agrees, post #10.
- Other posters in the same thread: toolboy (#3) says with THC on, start with the torch just above the metal edge. ds690 (#2) says the cut height is always 0.06.
- Newer FireControl versions may behave differently. Check the version you have.

## Why edge starts fail

- **IHS on:** IHS needs metal under the torch to touch off. Start just off the edge and there's nothing to touch, so the torch keeps going down or the sequence faults.
- **IHS off:** the torch stays at whatever height Z is parked at. That's usually far too high for the arc to transfer. My JRWPC45LH operating manual gives no distance; it only says the cutting arc starts "when the nozzle is moved closer to the edge of the work piece" (p. 11). The Razorcut 45 DI manual (a related but different model) gives a **3–5 mm** transfer distance ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})).
- **Torch goes out right after the pierce.** t/21622 (a CUT45 on a PRO) found three causes:
  - **A FireControl bug in 21.1.4, fixed in 21.1.5.** Update first.
  - **A bad solder joint in the THC cable** (FultzForge).
  - **Torch lead and work lead crossed or coiled** (ds690).
  - Turning THC off made the cut run for several people, but that's a diagnostic step, not the fix ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).

## Before you start (every method)

1. **FireControl 21.1.5 or newer** (t/21622).
2. **Z travel check.** Lower the torch until the tip just touches the metal. There should still be about **1/2–3/4 in** of Z travel left below that (ds690, t/47251). If Z bottoms out first, IHS trips early and the heights are wrong. Raise the torch in the mount.
3. **Clean work clamp on the work**, and separate the leads: torch lead, work lead, THC cable, and USB not crossed or coiled ([Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}})).
4. **Air 75 psi** with the gas test ([Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})). Amps set on the knob ([CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})).
5. Eye protection, ventilation, and fire watch (Langmuir safety page; my CUT45 manual).

## Method 1: Scrap lead-in piece (Bernie's method)

**Status: used by me a few times; worked; not formally tested.** Log each use until there are measured results.

The idea: butt a scrap piece tight against the edge where the cut starts. IHS touches off on the scrap and the arc pierces and gets going there, then carries across the joint into the part.

1. **Pick the scrap.**
   - Same thickness as the part.
   - Flat, with a straight, clean edge.
   - Big enough to start the cut about **0.5 in** back from the joint, plus room to clamp or weight it.
2. **Make a tight butt joint.** Push the scrap's edge hard against the part's edge where the cut starts. **There should be no gap**, and the top surfaces should be level, so the torch doesn't hit a step.
3. **Keep both pieces in the work-clamp circuit.**
   - The part has the work clamp on clean metal.
   - The scrap sits on the slats and touches the part, so it's connected too.
   - If you're not sure, check continuity from the work clamp to the scrap with a meter.
4. **Line up the cut.** Jog the torch over the scrap, on the cut line, about **0.5 in** before the joint. Use the Marker Pen or a pointer to check that the line crosses the joint where you want it.
5. **Straight Cut with IHS on.** Set the length so it runs from the scrap start point, across the joint, through the part. FireControl sets the 0.15 in pierce and 0.06 in cut height (t/20335 #4).
6. **Dry run** with the plasma off and watch the path.
7. **Cut.** Watch the arc cross the joint. Note whether it stutters, the torch moves up or down, or the arc goes out.
8. **Log it:** thickness, amps, feed, joint gap (none / small), what happened at the joint, and the quality of the edge where the cut entered the part.

Why it probably works (reasoning worked out for this page, not from a source): IHS and the pierce both happen on solid metal, and the arc is already cutting at full height and speed when it reaches the part's edge.

## Method 2: start just inside the edge with IHS on (not yet tried)

**Not yet tried.** It follows from support's description of IHS-on behavior (t/20335 #4).

1. Place the start **0.25–0.5 in inside the plate edge**, on the cut line, so IHS has metal to touch.
2. Straight Cut, IHS on. FireControl pierces at 0.15 and cuts at 0.06.
3. **Trade-off:** the pierce leaves a mark in the plate. Use this only if the pierce lands on the scrap side or the first bit can be trimmed off.
4. Log the result as for Method 1.

## Method 3: IHS off, torch set by hand, start just off the edge (not yet tried)

**Not yet tried.** It follows from staff's description of IHS-off behavior (t/20335 #5).

1. **Switch the CUT45 off.**
2. Jog the torch over the plate near the edge. Lower Z until a **0.060 in feeler gauge** just slides between the shield and the plate.
3. Jog in **X/Y only** to a start point just off the edge (Z stays put).
4. Switch the CUT45 back on. Run Straight Cut with **IHS off**.
5. **There's no THC in this mode** (staff, t/20335 #5). If the plate isn't flat, the height drifts. Use it only on short, flat cuts, and weight or clamp the plate flat.
6. Log the result as for Method 1.

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Torch keeps going down off the edge, or IHS faults | IHS-on start with no metal under the torch | Method 1 or 2 (t/20335 #4) |
| No arc transfer; torch stays high | IHS off with Z parked too high | Method 3 height set by gauge (t/20335 #5; Razorcut 45 DI manual 3–5 mm transfer, related model) |
| Pierces, then torch goes out | FireControl 21.1.4 bug; THC cable joint; crossed leads | Update to 21.1.5+; inspect the THC cable; separate leads (t/21622) |
| IHS trips early or heights look wrong | Z bottoming out | Leave 1/2–3/4 in of Z travel (ds690, t/47251) |
| Arc stutters at the scrap joint (Method 1) | Gap at the joint, step in height, or scrap not grounded | Tighter butt; same-thickness flat scrap; check continuity to the clamp |
| Height drifts along the cut (Method 3) | No THC in IHS-off Straight Cut | Flatten the plate; keep the cut short; or use Method 1 |

## Where sources disagree (and the starting choice)

- **Cut height in Straight Cut.** Support (t/20335 #4): with IHS on, it's fixed at 0.06. ds690 (#2): "always 0.06". Staff (#5): with IHS off, it's wherever Z sits. These don't conflict; they describe the two modes. **Go with the Langmuir staff and support answers.**
- **THC on edge starts.** toolboy (#3) talks about THC on with the torch above the edge. Staff (#5) says THC doesn't activate with IHS off. **Go with staff:** no THC in IHS-off Straight Cut.
- **Turning THC off to stop torch-out** (t/21622). It worked for several people, but the real fixes were the FireControl update and wiring. **THC off is a diagnostic step only.**
- **Methods 2 and 3 vs. Method 1.** I've used Method 1 a few times on my machine and it worked. Methods 2 and 3 haven't been tried yet. **Method 1 is my first choice.**

## Safety

Follow Langmuir's safety page and my CUT45 manual: eye protection to ANSI Z87.1 / Z49.1, ventilation, fire watch. **Switch the CUT45 off before putting a gauge or hands under the torch.** Plate and scrap edges are sharp; wear gloves.

## Sources

- Forum, Straight Cut behavior: <https://forum.langmuirsystems.com/t/20335> (#2 ds690; #3 toolboy; #4 support quote; #5 Langmuir staff `langmuirsystems`; #10 ChelanJim)
- Forum, torch out after pierce: <https://forum.langmuirsystems.com/t/21622> (FireControl 21.1.4 → 21.1.5; FultzForge THC cable; ds690 leads; THC-off reports)
- Forum, Z travel: <https://forum.langmuirsystems.com/t/47251> (ds690)
- Langmuir, FireControl guide: <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, THC guide: <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, Safety: <https://www.langmuirsystems.com/pages/safety>
- My JRWPC45LH operating manual (edge start by hand, p. 11)
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (transfer distance; safety): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- Bernie's own shop experience (Method 1, used a few times; no measurements recorded).

## Bernie's test results

| Date | Method | Material / thickness | Amps | Feed (ipm) | FireControl version | Joint gap (Method 1) | Arc start OK? | Crossed joint / edge clean? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Not recorded | 1 | Not recorded | Not recorded | Not recorded | Not recorded | Not recorded | Worked | Not recorded | Used a few times; worked; no measurements or dates recorded. |

Methods 2 and 3: no results yet (as of 30 October 2026).
