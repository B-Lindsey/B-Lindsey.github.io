---
title: "Scenario: Resuming a Cut After a Stop (Resume, Run From Loop, Run From Line)"
date: 2026-10-30
tags: ["cnc", "plasma", "firecontrol", "run-from-here", "resume", "pause", "torch-out", "m00", "crossfire-pro"]
draft: false
weight: 5
lastmod: 2026-10-30T16:15:00-07:00
summary: "The torch went out, a consumable failed, or you had to stop part-way through a sheet. When Resume works, when you need Run From Here (loop or line), how to keep the work zero, and why the orange button sometimes does nothing."
---

{{< lastupdated >}}

**Reference: compiled from Langmuir docs and forum threads.**

## Applies to

A CrossFire PRO with THC and IHS, running SheetCAM programs (Langmuir post) in FireControl.

- **Versions:** "Run From Line" arrived in FireControl 20.5 (staff, t/10840/2). The fixes below match the guide for the current interface. Most forum reports are on 21.1.4–21.1.5.
- **Related:**
  - [Indexing long parts]({{< relref "/procedures/01-indexing-long-parts.md" >}}) uses Run From Here on purpose, to cut a part longer than the table. This page is for **recovering** from an unplanned stop.
  - If the stop was a frozen or dropped connection, fix that first: [Scenario: connection lost or freeze mid-cut]({{< relref "/firecontrol/fc-04-connection-lost-mid-cut.md" >}}).
- Practise on scrap before you need it: start a small two-part program, stop it during the first part, and recover it.

## Symptom (what you'll see)

- A cut stopped part-way: the torch went out, a consumable failed, or you paused or stopped mid-sheet.
- **Resume** faults with "retry the path".
- FireControl says it **can't start in the middle of a loop**.
- The restarted cut lands in the **wrong place**.
- The orange **Loop/Line** button does nothing, or Run From Line moves but doesn't cut.
- After an **M00** planned pause, the Torch Enable switch is greyed out.

## Likely causes

Most likely first:

1. **Paused or stopped in the middle of a cut** (torch on). Resume only works between cuts (FireControl guide; 72Pony, t/28506/2, /4).
2. **The work zero changed:** Zero All Axes pressed, or the torch or sheet moved (DonP, t/30573/2, /5).
3. **Dry Run left on,** so the orange button does nothing or the restart "acts as a dry run" (Simsworx, t/31759/7).
4. **XY position lost** by a reset during motion (guide) or by a reinstall (brownfox, t/30573/9).
5. **A FireControl version problem** with the button (ChelanJim, t/31759/4; fixed on 21.1.4, #8).
6. **A hardware fault,** rarely: one 2026 user later replaced his motion control board (strongautoandfab, t/10840/7, /9).

### How FireControl thinks about it (per Langmuir)

From the FireControl guide:

- **Pause between cuts** (for example during a rapid move), and you can carry on with **Resume**.
- **Pause or stop in the middle of a cut** (torch on), and you can't simply resume. "Note the current g-code line and use this to pick up the cut again using the 'Run From Here' feature."
- "FireControl automatically stores your work position when pausing and stopping programs."
- "Since a cut program cannot start in the middle of a cut loop, FireControl will automatically determine the start of the cutting loop" and ask you to confirm. Afterwards, the visualizer doesn't show the loops before the restart point.
- Keys: **Alt+R** start, **Space Bar** pause, **Alt+S** stop.

**Loop vs. line** (toolboy and brownfox, t/14626/2, /4; TinWhisperer, t/10840/4, /5):

- A **loop** is one whole torch-on, cut, torch-off path, from pierce to the end of that cut. **Run From Loop** re-pierces at the start of that path and cuts all of it again.
- A **line** is a piece of that path. **Run From Line** starts part-way along it. TinWhisperer says it writes in a new pierce at that point (t/10840/4).

## Fixes (most to least likely)

### 1. Recover with Run From Here after a torch-out or mid-cut stop

1. **Make it safe.** If the motion stopped with the arc on, switch the Razorweld CUT45 CNC (model JRWPC45LH) off. Fix the cause: consumables ([Air and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}})), grounding, or the arc-loss settings ([THC setup]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
2. **Don't move the sheet. Don't press "Zero All Axes".**
   - DonP: zeroing again "will create new starting point", and you have to restart from the **original work zero** (t/30573/2, /5).
   - ChelanJim: this only works if FireControl still shows the part, you haven't moved the torch or sheet, and the settings are intact (t/37966/4).
3. **Note the line.** Before clearing the alarm, write down the G-code line FireControl was on (guide). If you missed it, click the spot in the **visualizer** where the cut stopped. It jumps to that code line (brownfox, t/14626/4; TinWhisperer, t/30573/3).
4. **Choose Loop or Line.** The orange button on that line offers **Run From Loop** or **Run From Line**. If FireControl says it can't start mid-loop, accept the loop start it offers (guide; t/10840).
   - **Loop:** the safer choice for a small part, or when the miss is near the start of a cut. The whole profile is cut again; the already-cut part just gets a second pass.
   - **Line:** use it on a long profile, to start just **before** where the cut stopped. Expect a pierce mark where it restarts.
5. **Confirm "generate".** FireControl asks whether to generate the program from that point. Say yes (ChelanJim, t/37966/4; DonP, t/30573/2).
6. **Go to Work Zero, then Start.** ChelanJim's order (t/37966/4): generate, **Go to Work Zero**, **Start**. Before Go to Work Zero, check the DRO for a clear path (guide).
7. **Watch the first pierce** and be ready to stop.

### 2. If the restart lands in the wrong place

Return to the **original work zero**; don't re-zero (DonP, t/30573/2, /5). If XY was lost after a freeze, reset or reinstall, re-find the zero on a known feature. Without limit switches there's no home to fall back on (brownfox, t/30573/9).

### 3. If the orange Loop/Line button does nothing, or the restart doesn't cut

1. **Turn Dry Run off** (Simsworx, t/31759/7).
2. **Then try another listed FireControl version** (ChelanJim, t/31759/4; A7MOSPHERIC fixed it on 21.1.4, #8).
3. If Start stays grey after you pick the line, try **Go to Work Zero** (ChelanJim, t/30573/17). It didn't help OkieBuckeye in that case (#18).
4. If it still moves without cutting, suspect hardware: strongautoandfab later replaced his motion control board (t/10840/7, /9).

### 4. After a planned pause (M00), for scribing or swapping tools

- **M00 works; M01 doesn't.** jamesdhatch, a long-time forum member: "Use M00. M01 requires an optional stop switch" (t/8048/2).
- **Resuming after M00 (2026 reports):**
  - poppabear (t/48685/17, /21) and rat196426 (t/48685/9, /12, /16) both say the torch **does** fire again when you carry on.
  - The **Torch Enable switch stays greyed out**, but the torch-on indicator at the bottom and the table itself show it firing. poppabear calls it a display bug.
  - poppabear's two posts differ on the button: #17 says "the pause button, then the Start button"; #21 says "Resume". rat196426 says hit **Start**, not Resume.
  - **Try Start first, on scrap.**
- **Simpler option:** ds690 suggests separate gouge or scribe and cut files (t/48685/7).
- **Older versions:** on 20.6.2, users reported FireControl froze after M00 (t/13735/1), and nicaDd had "no success" with it (t/23300/5).

### Quick lookup

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Resume faults with "retry the path" | Paused in the middle of a cut | Run From Line or Loop instead (72Pony, t/28506/2, /4; guide) |
| "Can't start in the middle of a loop" | Expected behavior | Accept the loop start FireControl offers (guide; t/10840) |
| Restarted cut lands in the wrong place | Work zero changed (Zero All Axes, torch moved, or sheet moved) | Return to the original work zero; don't re-zero (DonP, t/30573/2, /5) |
| Orange Loop/Line button does nothing | Dry Run on; version problem | Turn Dry Run off (Simsworx, t/31759/7); try another listed version (ChelanJim, t/31759/4; fixed on 21.1.4, #8) |
| Lost position after a freeze, reset, or restart | XY lost by a reset during motion (guide), or by a reinstall | Re-find the zero on a known feature. Without limit switches there's no home to fall back on (brownfox, t/30573/9) |
| Run From Line moves but doesn't cut ("acts as a dry run") | Dry Run left on, or a hardware fault | Check the Dry Run toggle (t/31759/7). That 2026 user later replaced his motion control board (strongautoandfab, t/10840/7, /9) |
| Torch Enable greyed after M00 | Display bug | Press Start; the torch fires anyway (t/48685/17, /21) |

## Where sources disagree

- **Pause = stop?** In 2021, MotoRider42HC reported that Pause acted like Stop mid-cut (t/12401/1). jamesdhatch says CNC machines don't agree on what pause should do (#6). The guide spells out the current behavior: resume between cuts, Run From Here mid-cut. **The guide's behavior is used here.** Pause between cuts when you can.
- **Older version to fix the button.** A7MOSPHERIC fixed the dead button with 21.1.4 (t/31759/8), while OkieBuckeye's 2025 attempts didn't help (t/30573/18). It's a workaround; there's no staff answer. **Check Dry Run first,** then the version.
- **M00 on resume.** 2021–2022 reports say it freezes on 20.6.2. 2026 reports say it works with the greyed-out switch. **The 2026 reports are used here** for current versions. Test on scrap before relying on it for a real job.

## What experienced forum members add

- **72Pony**, t/28506/2, /4: "In the future if you need to pause do it between cuts."
- **ChelanJim**, t/30573/17: if Start stays grey after you pick the line, try **Go to Work Zero**. It didn't help OkieBuckeye in that case (#18).
- **brownfox**, a long-time forum member, t/30573/9: an uninstall and reinstall loses the zero "UNLESS… you have limit switches and you had honed [homed] your table prior to the program". My PRO has no limit switches, so after a reinstall, re-find the zero by hand.
- **toolboy**, a long-time forum member, t/16514/2: after an error, click the program and choose loop or point.

## Safety

Never reach under the torch until the **CUT45 is switched off**. A restart pierces again; keep hands and the fire watch clear. The Run From Here move goes back to the work zero, so check the path for clamps and tip-ups first (guide: check the DRO before Go to Work Zero).

## Sources

- Langmuir, FireControl guide (pausing; Run From Here; shortcuts; Go to XY Zero): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, FireControl features (Run From Here; Dry Run): <https://www.langmuirsystems.com/pages/firecontrol>
- Forum: <https://forum.langmuirsystems.com/t/10840> (staff #2: Run From Line in FC20.5; TinWhisperer #4, #5; strongautoandfab #7, #9)
- Forum: <https://forum.langmuirsystems.com/t/14626> (toolboy #2; brownfox #4)
- Forum: <https://forum.langmuirsystems.com/t/16514> (toolboy #2)
- Forum: <https://forum.langmuirsystems.com/t/30573> (DonP #2, #5; TinWhisperer #3; brownfox #9; ChelanJim #17; OkieBuckeye #18)
- Forum: <https://forum.langmuirsystems.com/t/31759> (ChelanJim #4; Simsworx #7; A7MOSPHERIC #8)
- Forum: <https://forum.langmuirsystems.com/t/37966/4> (ChelanJim)
- Forum: <https://forum.langmuirsystems.com/t/28506> (72Pony #2, #4)
- Forum: <https://forum.langmuirsystems.com/t/12401> (MotoRider42HC #1; jamesdhatch #6)
- Forum, M00: <https://forum.langmuirsystems.com/t/8048/2> (jamesdhatch); <https://forum.langmuirsystems.com/t/13735/1>; <https://forum.langmuirsystems.com/t/23300/5> (nicaDd); <https://forum.langmuirsystems.com/t/48685> (ds690 #7; rat196426 #9, #12, #16; poppabear #17, #21)
