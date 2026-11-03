---
title: "Scenario: FireControl Won't Open (\"Child process exited with code 1\")"
date: 2026-10-30
tags: ["cnc", "plasma", "firecontrol", "crash", "child-process", "windows", "reinstall", "crossfire-pro"]
draft: false
weight: 2
lastmod: 2026-10-30T16:15:00-07:00
summary: "FireControl crashes on startup, or Windows shows \"Child process exited with code 1\". The most-viewed FireControl problem on the forum. Langmuir staff tie it to power-efficient AMD \"U\" CPUs and a Windows update; FireControl 24.1.6 is the staff fix."
---

{{< lastupdated >}}

**Reference: compiled from Langmuir docs and forum threads.**

## Applies to

Any Windows computer that runs FireControl for a CrossFire table. The error comes from the computer, not the table, so the CrossFire model doesn't matter. Reports in the threads below are from the original CrossFire, the PRO and the XR.

- **Versions:** reported on 21.1.4 and 21.1.5. Langmuir staff say **24.1.6 should fix it** (t/26056/67), and the 24.1.6 release notes list "fixes for low power CPU's which was causing Child Process errors" (t/41980/1). The downloads page lists 24.1.6 as the current Windows version and 21.1.5 as the current Mac version (checked 2026-10-28).
- **Mac:** none of the threads read for this page report this error on a Mac.

## Symptom (what you'll see)

- FireControl crashes on startup, and Windows shows a dialog saying **"Child process exited with code 1"**.
- It often starts right after a Windows update.
- Sometimes it appears after loading a file, or with two FireControl windows open.
- On the compatibility build, FireControl may open but show no toolpath picture.

## Likely causes

From langmuir-reilly's PSA (t/31326/1) and the PRO troubleshooting page, most likely first:

1. **A power-efficient CPU plus a Windows power change.** A "child process" is a part of FireControl that runs on its own. Staff name the **digital read-out (DRO)** and the **toolpath visualizer**. When one fails, Windows shows "Child process exited with code 1". Staff link it to a Windows update from around October 2022 that "changed how the operating system distributes power". After it, some power-efficient CPUs no longer give FireControl enough resources.
   - Most reports are **AMD Ryzen processors whose model numbers end in "-U"**. A few are AMD "-H" chips. Under 1 % come from Intel computers (t/31326/20).
   - langmuir-zachary (2025, t/26056/67): "it's mostly caused by the visualizer crashing".
2. **Two copies of FireControl running.** Langmuir-Nick has seen the error "just from having two instances of the same program running" (t/31326/30).
3. **A corrupt post processor**, if the error comes up after loading a file (Bigdaddy2166, t/26056/53).
4. **Hardware or an OS the program can't live with**, if it still crashes after every fix below (PRO troubleshooting).

**Find your CPU model:** in Windows 10 or 11, Settings > System > About, under "Device specifications" > "Processor" (t/31326/1). A model ending in **U** (or an AMD **H**) matches the pattern.

## Fixes (most to least likely)

**Before you reinstall anything, back up:**

- The clean reinstall (fix 4) deletes the `.FireControl` folder. Langmuir says it holds preferences, soft limits and program history.
- Write down your Machine Settings and THC settings first.
- Copy your SheetCAM tool library somewhere safe. One user wiped a computer and lost his (JapScrap, t/26056/27).

Work down the list and stop when FireControl opens.

1. **Install the current Windows FireControl (24.1.6)** from <https://www.langmuirsystems.com/pages/downloads>. This is the staff fix as of 2025 (t/26056/67). Kwikfab fixed his the same way (t/26056/66).
2. **Close every copy of FireControl** (check Task Manager), then reopen one (t/31326/30).
3. **Laptop on wall power: set the power slider to "Best performance".** In 2022, langmuir-reilly asked a user where his battery slider was set and whether "Best Performance" helped (t/26056/9). He didn't say it was a fix. It's a quick check. Then **restart Windows** and open FireControl before opening anything else.
4. **Clean reinstall** (PRO troubleshooting page, "FireControl Reinstallation"):
   1. Uninstall FireControl from the Control Panel.
   2. Delete the folder `C:\Users\[YOUR USERNAME]\.FireControl`.
   3. Restart the computer.
   4. Reinstall FireControl.
5. **Try the compatibility build.** Download "FireControl 21.1.5-compatibility" ("for older graphics hardware") and install it the same clean way.
   - The PRO troubleshooting page lists this step.
   - PatriotPits fixed it this way (t/26056/29). So did Burnswelding (#41) and Bradw_00 (#49).
   - It didn't work for everyone. geaarogers (#30) and Rodent (#55) still got the crash on the compatibility build.
   - langmuir-zachary still offers it as the fallback in 2025 (t/26056/67).
   - **The compatibility version may turn the toolpath visualizer off** to save resources. Langmuir: "This is a feature, not a bug!" Turn it back on from the **View** tab, top left.
6. **If the error comes up after loading a file:** reload the post processor in case it's corrupt (Bigdaddy2166, t/26056/53).
7. **Only if nothing else works:** update the CPU drivers or the BIOS. Staff call these "relatively drastic steps" (t/26056/7). Follow the computer maker's instructions.
8. **Last resort: use a different computer.** The troubleshooting page says this may be necessary.
   - Bigdaddy2166 runs three Intel mini PCs that "work perfectly" (t/31326/11, t/31326/32).
   - ChelanJim uses a mini PC at his table (t/31326/26).
   - Langmuir doesn't recommend specific products (t/31326/20).

### Quick lookup

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| "Child process exited with code 1" at startup | Power-efficient CPU plus the Windows power change; the visualizer crashes | Fixes 1–5 (t/31326/1; t/26056/67) |
| Started right after a Windows update | Same | Same; then pause auto-updates (t/31326/1) |
| Opens on the compatibility build, but there's no toolpath picture | The compatibility build turns the visualizer off | View tab > turn the visualizer on (PRO troubleshooting) |
| Error appears with two FireControl windows open | Two copies running | Close both, then reopen one (t/31326/30) |
| Still crashes after fixes 1–7 | Hardware or OS the program can't live with | Different computer (PRO troubleshooting) |

## Keeping it from coming back

- **On a "U" CPU, staff advise turning off automatic Windows updates.** Staff warn that "disabling Windows updates may cause you to miss out on important security updates" (t/31326/1). Turning updates off now won't fix a computer that already has the update (t/31339/6).
- **Don't let Windows update while you cut.** jamesdhatch (t/26056/45) and ChelanJim (t/26056/43) both say this.
- Keep a copy of the working installer, and write down which version works.

## Where sources disagree

- **Is it Windows or FireControl?** In 2023, staff said "this issue stems from Windows, not a problem with the FireControl software" (t/31326/1, t/31339/6). In 2025, staff said 24.1.6 "should fix the issue" (t/26056/67), and the 24.1.6 release notes say the same (t/41980/1). Both are staff. **The newer advice comes first here: update first.** The older PSA steps are the fallback.
- **Rolling back to 20.6.2.** Some users got running again on 20.6.2 (JapScrap, t/26056/27). Phillipw says it works "as long as you are not running a xr or a pro with limit switches" (t/26056/26). Phillipw also reports that another user couldn't get 20.6 to install on Windows 11 (t/28310/22). It isn't a Langmuir recommendation, so it's not in the fix list; it ranks behind the compatibility build.
- **Downgrading Java** (jsvalentin, t/26056/61). He made three changes at once: older Java, a new AMD graphics driver, and the compatibility build. **There's only one report, and an old Java build is a security risk, so it's not in the fix list.** The compatibility build is the part that matches the staff advice.
- **Bigdaddy2166's USB-voltage explanation** (t/26056/65): a power-saving AMD chip "tries to regulate the USB voltage". Staff point to the visualizer instead (t/26056/67). **Staff's explanation of the cause is used here.** His practical advice (use a non-power-saving CPU) agrees with staff anyway.
- **Downloading with Chrome instead of Edge** (Bently69, t/26056/68). One report, no explanation. Listed only as something to try.

## What experienced forum members add

- **Bigdaddy2166**, t/26056/53: if the error comes up after loading a file, reload the post processor in case it's corrupt.
- **ChelanJim**, t/26056/57: if FireControl asks to "update" the motion-control firmware from v1.3 to v1.2, let it. It should then offer v1.3; take that too. Turn the control box off and on if needed. He calls this a workaround Langmuir's techs found. **It's not in the official docs.**
- **TomWS**, t/31339/2: points new reports to the staff PSA.

## Safety

Do these fixes with the **Razorweld CUT45 CNC (model JRWPC45LH) switched off** and nothing running on the table. If a reinstall resets your settings, check soft limits and THC settings before the next cut. A table running without its usual limits can crash the gantry.

## Sources

- Forum, crash on startup: <https://forum.langmuirsystems.com/t/26056> (6,229 views, 67 posts; langmuir-reilly #7, #9; Phillipw #26; JapScrap #27; PatriotPits #29; ChelanJim #43, #57; jamesdhatch #45; Bigdaddy2166 #53, #65; jsvalentin #61; Kwikfab #66; langmuir-zachary #67; Bently69 #68; compatibility-build reports #30, #41, #49, #55)
- Forum, staff PSA: <https://forum.langmuirsystems.com/t/31326> (langmuir-reilly #1, #6, #20; TomWS #10; Bigdaddy2166 #11, #25, #32; ChelanJim #26; Langmuir-Nick #30)
- Forum: <https://forum.langmuirsystems.com/t/31339> (langmuir-reilly #6; TomWS #2)
- Forum, 24.1.6 beta notes: <https://forum.langmuirsystems.com/t/41980/1> (langmuir-zachary)
- Forum, 20.6 on Windows 11: <https://forum.langmuirsystems.com/t/28310/22> (Phillipw)
- Langmuir, PRO troubleshooting (Child Process Error; FireControl Reinstallation; compatibility version): <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, downloads (current versions; 21.1.5-compatibility): <https://www.langmuirsystems.com/pages/downloads>
