---
title: "Scenario: FireControl Drops the Connection or Freezes Mid-Cut (the Computer Side)"
date: 2026-10-30
tags: ["cnc", "plasma", "firecontrol", "freeze", "disconnect", "usb", "laptop", "power-settings", "crossfire-pro"]
draft: false
weight: 4
lastmod: 2026-10-30T16:15:00-07:00
summary: "A cut stops part-way: FireControl freezes, goes blank, says \"Machine disconnected\" or \"Program cancelled\", or throws a Java error. Electrical noise is the usual suspect and has its own page. This page covers the computer, USB, power-saving, and FireControl-install causes, plus a test to tell them apart."
---

{{< lastupdated >}}

**Reference: compiled from Langmuir docs and forum threads.**

## Applies to

A CrossFire PRO with THC and IHS, with FireControl on a Windows computer. On my table the electronics enclosure is wall-mounted away from the table.

- **Electrical noise (EMI) and grounding** are the most common cause of mid-cut dropouts, and they have their own page: [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}}). **Work through that page first.** This page is for what's left after it: the computer, the USB link, Windows power settings, and the FireControl install.
- **To pick the job back up afterwards,** see [Scenario: resuming a cut]({{< relref "/firecontrol/fc-05-resume-run-from-here.md" >}}).
- **Versions:** the reports span FireControl 20.5 to 21.1.5 on Windows 10 and 11. A 2025 XR report (t/42107) doesn't give a version, and the replies there treat it as noise (TinWhisperer #2, Sticks #3). The fixes below don't depend on the version, except where noted.

## Symptom (what you'll see)

- A cut stops part-way. FireControl **freezes**, goes blank, or says **"Machine disconnected"** or **"Program cancelled"**.
- The THC or the machine is lost after a pause or overnight.
- Jogging is laggy, or keys act late.
- A Java error (`java.lang.NullPointerException … ThcConfiguration …`) appears, then the job drops to a hold, often during the IHS probe.
- FireControl closes itself mid-cut.
- In the worst case, motion freezes with the **arc still on** (t/16264/1). See Safety below.

## Likely causes

Most likely first:

1. **Electrical noise (EMI) from the arc.** The most common cause; see the [grounding page]({{< relref "/procedures/03-grounding-and-emi.md" >}}).
2. **Windows power saving:** the computer sleeps or turns off the USB device (jamesdhatch, t/7850/2; Bigdaddy2166, t/39348/9). A Windows update can switch a power setting back on (brownfox, t/39348/6).
3. **The USB link:** a loose plug at the control box or a bad solder joint on the USB connector (jindano, t/39348/16; TomWS, t/39348/17), a worn cable or port, or a USB cable routed against the table frame (t/24624/78, /81).
4. **The computer itself:** bad USB ports (Fortifyfabworks, t/16264/19), or an old computer that can't run the current FireControl (rmeyers, t/28606/9, /11).
5. **The FireControl install:** a stale `.FireControl` folder, "especially after switching between versions" (langmuirsystems, t/22160/6), or FireControl left open and idle too long (t/24624/59; t/12629/20).
6. **Something closed FireControl:** a Windows update in the background (t/26056/44–45) or the window's X clicked by accident (t/33962/15).

## Fixes (most to least likely)

### 1. Find out whether it's noise or the computer

JA6's isolation test (t/16264/17). Welder6131 ran it in the same thread, found a bad laptop, and was "up and running" again (#20, #21).

1. **Switch the Razorweld CUT45 CNC (model JRWPC45LH) off and unplug it.** Dry-run the same file that has been failing.
   - **Still fails with the plasma unplugged?** Then it **isn't** plasma noise. Go to fix 2.
   - **Only fails with the arc on?** It's noise. Go back to the [grounding page]({{< relref "/procedures/03-grounding-and-emi.md" >}}).
2. **Swap computers** and dry-run again.
3. If it fails only with the arc on, try a run with **THC off** as a diagnostic step (JA6, #17). It's **not a fix**; see [THC setup]({{< relref "/procedures/02-thc-setup-and-diving.md" >}}).

### 2. Stop the computer sleeping and turning off USB

- jamesdhatch, a long-time forum member, t/7850/2: if the laptop sleeps, it "loses the connection to the THC". Restarting FireControl doesn't fix it; you have to unplug and replug the USB. He made a separate Windows power profile for the CrossFire that never sleeps.
- Bigdaddy2166, t/39348/9, after a "Machine disconnect" report:
  1. In Settings > System > Power & battery, choose a performance power mode instead of a power-saving one.
  2. In Device Manager, right-click the USB device > Properties > **Power Management**, and untick **"Allow the computer to turn off this device to save power."**
- brownfox, a long-time forum member, t/39348/6: a Windows update can switch a power setting back on. Check these again after big Windows updates.

### 3. Fix the USB link

1. **Plug in directly with a sound cable and a tight plug.** The guide says no extensions or hubs.
   - jindano's "Machine disconnect" turned out to be a **loose USB plug at the control box** (t/39348/16). TomWS says it may be a bad solder joint on the USB connector (t/39348/17).
   - A different cable or a different port on the computer is the first swap (Bigdaddy2166, t/39348/2).
   - PixelTamer (t/39348/18): packing a loose plug with foil is "a poor solution". Fix or replace the connector.
2. **Keep the USB cable off the table frame.**
   - Wsidr1 stopped running the cable through the laptop-tray hole and had no more freezes in 6–8 signs (t/24624/78).
   - RAMtech marked his thread solved after moving the USB cables away from the frame (t/24624/81).
   - With a wall-mounted enclosure, like mine, check where the USB run between the computer and the enclosure touches metal.

### 4. Test the jog, and restart FireControl before cutting

- Wsidr1, t/24624/59: press the arrow keys a few times. If there's a delay, close and reopen FireControl, or restart the computer. "If I get good jog function repeatedly, I never have a freeze up when cutting."
- 72Pony, t/12629/20: doesn't leave FireControl open and idle. If he isn't using it, he closes it.

### 5. Suspect the computer

- **USB ports.** Fortifyfabworks's freezes were the laptop's USB ports, and his USB mouse misbehaved too. He bought a cheap laptop just for the table (t/16264/19).
- **Java error, then lost connection (often during the IHS probe).** rmeyers got `java.lang.NullPointerException … ThcConfiguration …`, and the job dropped to a hold, always during the G38 probe (t/28606/1, /3). It was fixed by a **newer computer running the newest FireControl**. His old PC "could not support it graphically" (t/28606/9, /11).

### 6. Clean up the FireControl install

1. **Slow, laggy, or stuck jogging:** staff say to delete the `.FireControl` folder, "especially after switching between versions" (langmuirsystems, t/22160/6). Then reinstall (steps in [Scenario: FireControl won't open]({{< relref "/firecontrol/fc-02-child-process-crash.md" >}})).
2. **Install the current version** (24.1.6 on Windows) unless you have a reason not to. On older graphics hardware, use the 21.1.5-compatibility build (downloads page).

### 7. Keep anything from closing FireControl mid-job

- **No Windows updates while cutting.** jamesdhatch (t/26056/45): updates in the background can kill a running FireControl. DnKFab lost a 40-minute cut that way (t/26056/44).
- **Don't touch the close-window X while a job runs.** holla2040 hit it by accident mid-cut, and FireControl "promptly quit" (t/33962/15).

### Recovering when it hangs

- FireControl guide:
  - The **circular reset icon** next to the connection resets the connection and auto-connects again. It's for clearing an alarm "or if the machine is unresponsive".
  - **"Your XY position may be lost if you reset or disconnect while the machine is in motion."**
- Before you resume, check the work zero against the part (jog the torch over a cut you know). Then follow [Scenario: resuming a cut]({{< relref "/firecontrol/fc-05-resume-run-from-here.md" >}}).

### Quick lookup

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Freezes only with the arc on | Electrical noise | [Grounding page]({{< relref "/procedures/03-grounding-and-emi.md" >}}); isolation test (t/16264/17) |
| Freezes in a dry run with the plasma unplugged | Computer, USB, or install | Swap computers (t/16264/20–21); fixes 2–6 |
| Lost THC or machine after a pause or overnight | Computer slept or turned off the USB | Never-sleep power profile; untick USB power saving (t/7850/2; t/39348/9) |
| "Machine disconnect" from a fussy plug | Loose USB at the control box; bad connector joint | Reseat; repair or replace the connector (t/39348/16–17) |
| Laggy jog, keys acted on late | Install or folder problem; FireControl open too long | Delete `.FireControl`, reinstall (t/22160/6); restart FC before cutting (t/24624/59) |
| Java NullPointerException, then a hold during IHS | Old computer can't run the current FC | Newer computer and the newest FC (t/28606/9, /11) |
| "Program cancelled" mid-cut | USB cable against the frame | Re-route the USB (t/24624/81) |
| FireControl closed itself mid-cut | Window X clicked, or Windows update | Keep clear of the X; pause updates (t/33962/15; t/26056/44–45) |

## Where sources disagree

- **Laptop on battery vs. 3-to-2-prong "cheater" plugs.**
  - nicaDd (t/16264/2), toolboy (t/12629/9, /14) and jamesdhatch (t/12629/10) suggest a 3-to-2 adapter or cutting off the ground prong.
  - That defeats a safety ground, and TomWS and Bigdaddy2166 call floating the safety ground "craziness" ([grounding page]({{< relref "/procedures/03-grounding-and-emi.md" >}}), t/24659/16).
  - **Don't do it.** Run the laptop on battery, or use a USB ground-loop isolator (see the [grounding page]({{< relref "/procedures/03-grounding-and-emi.md" >}})).
- **Staying on an old version** (nicaDd on 20.5, t/24624/49; Bill_A on 20.6.2, t/22160/2). Staff suggest a clean `.FireControl` folder and a current install (t/22160/6). rmeyers's fix included the newest version (t/28606/11). **Starting choice: staff's advice,** current version first.
- **Ground rod for the frame** (Bigdaddy2166, t/24624/42, /75; RAMtech #81). That's a grounding question; follow the [grounding page]({{< relref "/procedures/03-grounding-and-emi.md" >}}), not this page.

## What experienced forum members add

- **Wsidr1**, t/24624/59: test the jog every time; if it's slow, restart FireControl, and sometimes the computer.
- **72Pony**, t/12629/20: close FireControl when you're not using it.
- **TomWS**, t/39348/14: if the metal rim of the USB plug touches the enclosure, "that would definitely cause interference problems".
- **Fortifyfabworks**, t/16264/19: a cheap laptop just for the table, with CAD on another computer.

## Safety

If the motion freezes with the **arc still on** (t/16264/1), **switch the CUT45 off at the cutter first**. Then deal with FireControl. Don't put hands near the torch until the cutter is off. **Never defeat a safety ground** to fix noise (see the grounding page). Follow Langmuir's safety page and my CUT45 manual.

## Sources

- Forum: <https://forum.langmuirsystems.com/t/16264> (2,467 views; Welder6131 #1, #20, #21; nicaDd #2; JA6 #17; Fortifyfabworks #19)
- Forum: <https://forum.langmuirsystems.com/t/28606> (solved; rmeyers #1, #3, #9, #11)
- Forum: <https://forum.langmuirsystems.com/t/24624> (81 posts, solved; Bigdaddy2166 #42, #75; nicaDd #49; Wsidr1 #59, #78; RAMtech #81)
- Forum: <https://forum.langmuirsystems.com/t/39348> (Bigdaddy2166 #2, #9; brownfox #6; TomWS #14, #17; jindano #16; PixelTamer #18)
- Forum, sleep drops the THC: <https://forum.langmuirsystems.com/t/7850/2> (jamesdhatch)
- Forum, lag fixed by deleting the folder: <https://forum.langmuirsystems.com/t/22160> (Bill_A #2, #5; langmuirsystems #6)
- Forum: <https://forum.langmuirsystems.com/t/12629> (toolboy #9, #14; jamesdhatch #10; 72Pony #20)
- Forum: <https://forum.langmuirsystems.com/t/26056> (DnKFab #44; jamesdhatch #45); <https://forum.langmuirsystems.com/t/33962/15> (holla2040); <https://forum.langmuirsystems.com/t/42107> (XR with a Cut60; TinWhisperer #2; Sticks #3)
- Langmuir, FireControl guide (reset connection; XY may be lost; plug in directly): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, downloads: <https://www.langmuirsystems.com/pages/downloads>
