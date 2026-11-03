---
title: "Scenario: FireControl Won't Connect (CrossFire Greyed Out, COM Port Instead of Firmware)"
date: 2026-10-30
tags: ["cnc", "plasma", "firecontrol", "usb", "drivers", "connection", "motion-control-board", "crossfire-pro"]
draft: false
weight: 3
lastmod: 2026-10-30T16:15:00-07:00
summary: "FireControl opens, but the CrossFire indicator stays grey, shows a COM port number instead of a firmware version, or comes and goes. Causes and fixes from the computer to the drivers to the motion control board, from Langmuir's troubleshooting page and the forum."
---

{{< lastupdated >}}

**Reference: compiled from Langmuir docs and forum threads.**

## Applies to

A CrossFire PRO with THC and IHS (a Gen 2, FireControl machine), on a Windows computer. On my table the electronics enclosure is wall-mounted away from the table.

This is the **at-startup** problem: FireControl never makes a full connection. If it connects and then drops during a cut, see [Scenario: connection lost or freeze mid-cut]({{< relref "/firecontrol/fc-04-connection-lost-mid-cut.md" >}}).

- **Versions:** the threads cover FireControl 20.6 through 21.1.4. Staff in 2021–2022 asked first whether the user was on "the latest 21.1.4 version" (t/14728/13, /17). The current Windows version is 24.1.6 (downloads page, checked 2026-10-28).
- **Doesn't cover:** Gen 1 / Mach3 CrossFires. Langmuir says those need Mach3 (PRO troubleshooting page, section 4A).

## Symptom (what you'll see)

- FireControl opens, but the **CrossFire** indicator next to 'Machine' stays **grey**, or comes and goes.
- A **COM port number** shows where the firmware version should be (ds690, t/28310/11). That's the "not so bright" green box in t/28310/1.
- Sometimes **Connection Help** pops up after about 10 seconds.
- In Device Manager, 'USB Serial Device' is missing, or Windows reports 'Device Descriptor Failed'.
- The THC may connect (its LS THC version shows) while the CrossFire won't.

**What "connected" looks like (per Langmuir):**

- The FireControl guide says that when fully connected, the window shows **'CrossFire'** and the **firmware version** (for example v1.2ls).
- There are two USB devices in the enclosure. Langmuir's troubleshooting page (4E) says Device Manager should list both:
  - the motion control board, as **USB Serial Device**
  - the LS-THC, as **USB-SERIAL CH340**

## Likely causes

Most likely first:

1. **The USB link: cable, port, hub or extension.** Langmuir says to connect "directly" (FireControl guide; troubleshooting 4C).
2. **Not connected by hand yet,** or the board isn't getting USB power. The logic boards run on **USB power from the computer**, even with the enclosure switch off (TinWhisperer, t/28310/3; nicaDd, t/28310/24). The main switch only powers the motors.
3. **Corrupted firmware or EEPROM.** Langmuir notes that "firmware and EEPROM memory can become corrupted" (troubleshooting 4D).
4. **A damaged driver or FireControl install,** often after an update or after the machine sat unused, for example over winter (staff t/14728/36; Greg9504 t/14728/45).
5. **The motion control board itself.** If the same failure shows on a second computer, staff say it "may point to the MCB" (t/14728/36). Staff also say a torch or arc problem can damage the board (t/14728/43).

## Fixes (most to least likely)

Work down the list and stop when the CrossFire shows its firmware version.

1. **Plug straight into the computer.** The guide and troubleshooting page (4C) say to connect "directly", with no USB extensions or hubs. Try a different USB port, then a different printer-style (USB-A to USB-B) cable. TinWhisperer gives the same advice (t/28310/6). If the cable runs to a wall-mounted enclosure, as on my table, check its whole length for damage too.
2. **Check the lights with the USB plugged in.**
   - The **green** light at the USB jack on the enclosure should be on (TinWhisperer, t/28310/6).
   - Inside, the motion control board's **green** LED and the THC board's **red** LED should be on (JDE, t/15811/2, /4).
   - **Switch the enclosure off and unplug it from the wall before you open it.**
3. **Connect by hand.** Next to 'Machine', click **Connect** and choose CrossFire from the list. Its LED should turn green (troubleshooting page, section 4).
4. **If 'CrossFire' is greyed out with no firmware version,** wait about 10 seconds for **Connection Help** and use it to **re-flash the firmware**. Then restart FireControl (troubleshooting 4D).
5. **Reinstall the driver** (FireControl guide):
   1. Open Device Manager > Ports (COM & LPT).
   2. Unplug and replug the USB to see which entry is the CrossFire.
   3. Right-click it > **Uninstall Device**, and tick **"Delete the driver software for this device"**.
   4. Replug and let Windows reinstall the driver.
   5. If that fails, install the **CrossFire Gen2 Driver** and the THC driver by hand from the downloads page (troubleshooting 4B). Staff also suggested a driver reinstall (t/14728/36).
   - Manual install is **required** on Windows 7 and 8.
   - nicaDd's order (t/18079/4, /10, /12, /19):
     1. **Unplug** the enclosure.
     2. Unzip the driver. Unzipping doesn't install it; **double-click the installer** to do that.
     3. Run it **as administrator**.
     4. Reboot.
     5. Plug the enclosure back in, then open FireControl.
6. **Clean-reinstall FireControl.** Use the PRO troubleshooting steps in [Scenario: FireControl won't open]({{< relref "/firecontrol/fc-02-child-process-crash.md" >}}): uninstall, delete the `.FireControl` folder, restart, reinstall. toolboy, a long-time forum member, gives the same advice: delete the FC folder in your profile, then reinstall FireControl and the drivers (t/14728/2, /46). Write down your settings first.
7. **Try another computer.** Staff: "Getting the same issue on another computer may point to the MCB" (t/14728/36).
   - nicaDd says you can take the control box to a computer inside, because the board is USB-powered (t/28310/24).
   - With a wall-mounted enclosure, like mine, a laptop brought to the enclosure is the easier test.
8. **Contact Langmuir support** (support@langmuirsystems.com). Staff: "we can try manually re-flashing the motion control board firmware, and if that doesn't do the trick, your motion control board will need to be replaced" (langmuir-aksel, t/14728/47). Include:
   - FireControl version
   - Windows version
   - what Device Manager shows
   - which LEDs are on
   - what you've already tried
   JGeorgiadis's machine was fixed by a new board (t/28310/28).

### Quick lookup

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| CrossFire box shows a COM port, no firmware version | Not fully connected; firmware or board | Fixes 3–5, then 7–8 (ds690 t/28310/11; troubleshooting 4D) |
| CrossFire greyed out, Connection Help appears | Corrupted firmware or EEPROM | Re-flash from Connection Help; restart FireControl (troubleshooting 4D) |
| No 'USB Serial Device' in Device Manager, or 'Device Descriptor Failed' | Cable, port, hub, or a dead USB jack or board | A different printer-style (USB-A to USB-B) cable, a different port, a different computer, then support (troubleshooting 4C, 4E; t/28310/6) |
| THC connects (LS THC version shows) but CrossFire won't | Motion control board side | Re-flash, driver, other computer, then support (t/28310; t/14728/47) |
| Worked before; fails after an update or winter storage | Driver or install damaged; sometimes the board | Fixes 5–8 (staff t/14728/36; Greg9504 t/14728/45) |
| Same failure on a second computer | Motion control board | Support: re-flash or replace (t/14728/36, /47) |
| Motors hiss when the USB is unplugged | Normal | Nothing to fix (toolboy, t/14728/28) |

## Where sources disagree

- **Driver install order.** nicaDd says to install the drivers with the box **unplugged**, then plug it in, because "for some reason it doesn't work the way the instructions say" (t/18079/12). It doesn't contradict anything Langmuir says; it's just a stricter order. **Starting choice: nicaDd's order.** It costs nothing.
- **Going back to an older FireControl** (Phillipw, t/28310/18). In that thread, older versions didn't help, and the fix was a new board (t/28310/21, /28). **Starting choice: the staff order instead:** current version, re-flash, driver, then support.
- **"It's the board."** Bigdaddy2166 tells people to get a new board: "They fail on occasion. I'm on my second one" (t/14728/53). Staff put the board **after** the driver, re-flash and second-computer checks (t/14728/36, /47). **Starting choice: the staff order.** Only buy a board after a second computer fails too.

## What experienced forum members add

- **Bigdaddy2166**, t/14728/49, /51: the computer's USB powers the control board. The 36 V DC supply powers motion through the motor drivers. If it connects but won't move, that's a different problem from not connecting.
- **Greg9504**, a long-time forum member, t/14728/45: a PRO that sat all winter wouldn't connect on the same laptop, even with the green USB light on and the COM ports showing. It isn't just new installs.
- **Staff**, t/14728/43: a torch or arc problem can damage the motion control board. If it stopped connecting right after a cutting incident, tell support. Also see [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}}).

## Safety

**Unplug the enclosure from the wall before opening it,** even though the logic boards run on USB power. The 36 V supply and the mains wiring are inside. The Razorweld CUT45 CNC (model JRWPC45LH) stays off for all of these checks.

## Sources

- Forum: <https://forum.langmuirsystems.com/t/14728> (4,766 views, 55 posts; staff `langmuirsystems` #13, #17, #36, #43; langmuir-aksel #47; toolboy #2, #28, #46; Greg9504 #45; Bigdaddy2166 #49, #51, #53; TinWhisperer #55)
- Forum: <https://forum.langmuirsystems.com/t/28310> (marked Solved; TinWhisperer #3, #6; ds690 #11; Phillipw #18; nicaDd #24; JGeorgiadis #1, #21, #28)
- Forum, driver install: <https://forum.langmuirsystems.com/t/18079> (7,098 views; nicaDd #4, #10, #12, #19)
- Forum, LEDs: <https://forum.langmuirsystems.com/t/15811> (JDE #2, #4)
- Langmuir, FireControl guide (connection; driver reset): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, PRO troubleshooting, "4: FireControl Not Connecting": <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, downloads (Gen2 driver; THC driver): <https://www.langmuirsystems.com/pages/downloads>
