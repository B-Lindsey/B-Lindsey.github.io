---
title: "Scenario: FireControl Won't Load the Program (\"No Program Speed Found\", \"Program Check Encountered an Error\", \"Unsupported GCode\")"
date: 2026-10-30
tags: ["cnc", "plasma", "firecontrol", "gcode", "post-processor", "sheetcam", "validation-error", "crossfire-pro"]
draft: false
weight: 7
lastmod: 2026-10-30T16:15:00-07:00
summary: "FireControl rejects a file while it's validating it. On the forum the cause is nearly always the post processor, a CAM rule that writes a code FireControl doesn't know, or loading with the table disconnected. How to read the file's first and last lines to tell which."
---

{{< lastupdated >}}

**Reference: compiled from Langmuir docs and forum threads.**

## Applies to

A CrossFire PRO with THC and IHS, with programs from SheetCAM 8.0 and the Langmuir FireControl post (Fusion's Langmuir post also works).

- **Versions:** reports run from FireControl 20.6.2 (2021) to 24.1.6 (2025). The post versions in the files are v1.6 (`(v1.6-sc)` for SheetCAM, `(v1.6-af)` for Fusion).
- **Related:**
  - [SheetCAM setup]({{< relref "/procedures/09-sheetcam-setup.md" >}}) covers choosing the FireControl-v1.6 post and the `(PS…)` program-speed line, and how it affects THC.
  - [THC setup]({{< relref "/procedures/02-thc-setup-and-diving.md" >}}) covers the 85 % speed cutoff.
  - This page is only about files that **won't load**.

## Symptom (what you'll see)

FireControl rejects a file on the "Validating Program" screen, with one of these:

- **"No Program Speed Found … will not be loaded"**
- **"Program Check Encountered an Error"**, sometimes pointing at `M30` (the last line) when the file looks fine
- **"Unsupported GCode Command"** on a line like `DTHC-OFF` or `M67`

FireControl guide: the "'Validating Program' screen" means "the USB motion control board is scanning the lines of g-code and checking for any errors". "If your program has an error, FireControl will let you know the error and the line in the g-code file where the error is present."

## Likely causes

Most likely first:

1. **The wrong or a missing post processor.** PRO troubleshooting, "Program Check Encountered an Error": "Common causes include using the incorrect PostProcessor or uploading a G-code file that surpasses your specified Soft Limits."
   - "The PS value gets inserted by the post processor" (langmuir-daniel, t/12255/7).
   - Every file from Langmuir's posts ends with a comment like `(PS100)`. Mach3 programs "will sometimes fail in this way" (langmuirsystems, t/12255/9).
2. **A SheetCAM rule writing a code FireControl doesn't use** ("Unsupported GCode Command"; jbrown9709, t/13798/5, /8).
3. **The enclosure isn't connected to the table and switched on** (Program Check error at `M30`). ChelanJim: "FireControl relies on the enclosure to get some of its information when loading a program" (t/42366/15).
4. **A file that's only small circles,** where the cut never reaches the tool's full speed ("No Program Speed Found"; t/42026/10; t/41980/22).
5. **A program past the soft limits,** if you have limit switches (PRO troubleshooting).
6. **A damaged FireControl install,** if nothing else explains it.

## Fixes (most to least likely)

1. **Read the error and line number.** FireControl names the line (guide). Open the `.tap` file in a text editor (Notepad) and go to that line.
2. **Check the first line.** A file from Langmuir's v1.6 post starts with `(v1.6-sc)` (SheetCAM) or `(v1.6-af)` (Fusion) (ChelanJim, t/42026/8).
   - Anything else (e.g. `( VENDOR AVID CNC)`) means it came from the **wrong post or machine** (TomWS, t/42026/11). Re-post with FireControl-v1.6 ([SheetCAM setup]({{< relref "/procedures/09-sheetcam-setup.md" >}})).
   - **Fusion:** pick the post from the setup menu every time unless you've saved it as a preference (TinWhisperer, t/19336/2). Tell Fusion where the post file is (ChelanJim, t/42026/6).
3. **Check the last line.** It should be `(PS…)` with the program speed, e.g. `(PS249)` (ChelanJim, t/42026/10; staff, t/12255/9).
   - **Missing:** wrong post, or a downloaded file that wasn't posted for FireControl (e.g. a Mach3 file from FireShare) (t/12255/9).
   - **Files that are only small circles:** ChelanJim relays Sticks's point that if the cut never reaches the tool's full speed, you can get this error too (t/42026/10). Sticks reports the same thing with Fusion's post in t/41980/22. This comes from forum users, not staff.
4. **"Unsupported GCode Command" on a line like `DTHC-OFF` or `M67`.** A **SheetCAM rule** is writing a code that FireControl doesn't use.
   - jbrown9709's came from a tool library he copied from another machine, which brought along a rule ("EOCAnti-Dive … output code: DTHC-OFF").
   - He fixed it by **building his own tool library** (t/13798/5, /8).
   - Check SheetCAM's rules for anything you didn't add.
5. **"Program Check encountered an error" at `M30` (the last line) when the file looks fine.** Check that the **enclosure is connected to the table and switched on**.
   - ChadS's file was fine (ds690 and ChelanJim checked it, t/42366/5, /7). It loaded once the enclosure was back on the table (t/42366/14).
   - My enclosure is wall-mounted by the table, so this mainly matters if the box is ever taken indoors to check files.
6. **"Program Check" with limit switches on:** re-zero or reposition so the program fits inside the soft limits ([Scenario: the part cuts in the wrong place]({{< relref "/firecontrol/fc-06-work-zero-program-origin.md" >}}); PRO troubleshooting).
7. **Still failing:** do a clean FireControl reinstall (steps in [Scenario: FireControl won't open]({{< relref "/firecontrol/fc-02-child-process-crash.md" >}})). Then post the G-code and the error on the forum, or send them to support. ChelanJim asks for the G-code text before anything else (t/42366/2).
8. **Old files.** The downloads page says "Programs posted with older versions of the Post Processors can be converted within FireControl". Try that before re-posting old jobs.

### Quick lookup

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| "No Program Speed Found … will not be loaded" | Wrong or missing post; no `(PS…)` line | Re-post with FireControl-v1.6; check the last line (t/12255/7, /9; t/19336/2) |
| Same error, file only has small circles | Cut never reaches the tool speed | See Sticks's fix in t/42026/10 and t/41980/22 (forum users' reports) |
| First line isn't `(v1.6-sc)` / `(v1.6-af)` | Posted for another machine | Select the Langmuir post (t/42026/6, /8, /11) |
| "Unsupported GCode Command" | A CAM rule outputs a code FireControl doesn't support | Remove the rule or rebuild the tool library (t/13798/5, /8) |
| "Program check encountered an error … M30" | Enclosure not connected to the table | Connect the enclosure to the table and switch it on (t/42366/14) |
| "Program Check" with limit switches on | Program past the soft limits | Re-zero or reposition ([Scenario: the part cuts in the wrong place]({{< relref "/firecontrol/fc-06-work-zero-program-origin.md" >}}); PRO troubleshooting) |

## Where sources disagree

- **Delete the bad lines by hand?** jbrown9709 first deleted the four `M67` lines and the file cut (t/13798/3). The real fix was removing the rule that wrote them (#5). **Starting choice: fix it in CAM.** Hand-edited files get overwritten the next time you post.
- **Reinstall vs. connect the enclosure** (t/42366). ChelanJim suggested a reinstall (#7). It didn't help, and connecting the table did (#14). **For an M30 Program Check error, check the connections first.**

## What experienced forum members add

- **ChelanJim**, t/42366/7: `H0` is in every program's opening lines so the controller takes charge of Z for the IHS sequence. ChelanJim says this comes from Langmuir. Don't strip it out.
- **ds690**, t/42366/5: `M30` at the end is normal, and the `(PS60)` line is the program speed.
- **Wsidr1**, t/42366/16: suggests a small enclosure simulator would let people check files indoors. There isn't one; plan to load files at the table.

## Safety

A file from the wrong post can contain moves or Z commands the PRO isn't set up for. **Never "fix" a file by deleting lines you don't understand** and then cut with it. Re-post it, then Dry Run with the Razorweld CUT45 CNC (model JRWPC45LH) off ([SheetCAM setup]({{< relref "/procedures/09-sheetcam-setup.md" >}})).

## Sources

- Langmuir, FireControl guide (Validating Program; error line): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, PRO troubleshooting (Program Check Encountered an Error): <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, downloads (post processors; converting older programs): <https://www.langmuirsystems.com/pages/downloads>
- Forum: <https://forum.langmuirsystems.com/t/12255> (3,574 views; langmuir-daniel #7; langmuirsystems #9)
- Forum: <https://forum.langmuirsystems.com/t/19336/2> (TinWhisperer)
- Forum: <https://forum.langmuirsystems.com/t/42026> (ChelanJim #6, #8, #10; TomWS #11)
- Forum: <https://forum.langmuirsystems.com/t/13798> (solved; jbrown9709 #3, #5, #8)
- Forum: <https://forum.langmuirsystems.com/t/42366> (solved; ChelanJim #2, #7, #15; ds690 #5; ChadS #14; Wsidr1 #16)
- Forum: <https://forum.langmuirsystems.com/t/41980/22> (Sticks, Fusion post and circles)
