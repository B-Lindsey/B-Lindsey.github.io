---
title: "THC Setup, Tuning, and Stopping Torch Dives"
date: 2026-10-28
tags: ["cnc", "plasma", "crossfire-pro", "thc", "firecontrol", "razorweld-45"]
draft: false
weight: 1
lastmod: 2026-10-30T18:30:00-07:00
summary: "Wiring check, Langmuir default settings, and fixes for torch dives with the Langmuir THC on a CrossFire PRO and a CUT45 using the 50:1 divider port."
series: ["CrossFire PRO procedures"]
series_order: 1
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.** The steps and fixes below are collected from Langmuir documents and forum posts.

## Applies to

This covers my CrossFire PRO with the Langmuir LS-THC added on (it's a $400 option on the PRO), IHS standard, FireControl, and a Razorweld CUT45 CNC (model JRWPC45LH) bought from Langmuir (Langmuir lists it as the "Razorweld Razorcut 45 with Machine Torch"). It uses the plug-and-play 50:1 divider port and the X45 machine torch, on 230 V. Some of the Langmuir docs don't apply to this setup:

- The **raw-voltage pigtail wiring** in the THC guide is only for cutters without a divider port. The CUT45 has one, so leave the raw wiring alone.
- The **XR** ships with THC and has its own wiring and ground notes.
- The **Gen1/Mach3** THC kit is a different system.
- Powermax arc-voltage tables are for Hypertherm, not the CUT45.

## Wiring check (do once, and again after any rewiring)

1. Power everything off. Connect the CUT45's 2-pin divider port to the VIM **DIV INPUT** through the Divided Voltage pigtail. Run the VIM output cable to the electronics box. Use **DIV OUTPUT**, not PV OUTPUT.
2. Polarity: the **red** wire goes to the **negative pin (torch)** and the **black** wire to the **positive pin (work clamp)**. The THC only reads positive voltage. Crossed wires read 0 V.
3. **Port-swap check.** My JRWPC45LH operating manual's rear-panel list names the two CNC sockets "13. CNC Torch On/Off Port" and "14. CNC 50:1 Voltage Divider Port" (p. 9), but the text doesn't say which socket is which, and it gives no pin-out. It says the CNC port connects "to the CrossFire Torch On/Off port using the CrossFire Torch wiring cable and CNC port adapter. This is a plug and play solution for automatic torch firing" (pp. 3 and 14), and to contact Langmuir support with CNC questions. Some units shipped with the ports swapped, so check: with Manual Torch Fire in FireControl, check that the torch fires from the firing port. Then check the other port gives THC voltage.
4. Set up **as if ready to cut**: THC, IHS, and USB connected, cutter on, work clamp attached (see [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}})).
5. Click the red **TEST** button (THC Health Check) on the FireControl THC panel.
   - Resting voltage (not firing): **under 5 V** passes. 5–10 V "should still function".
   - Non-zero live volts with the torch off usually means water bridging the IHS brass contact. See the table below.
6. Make a straight cut with **Straight Cut** (Zero All Axes first) with the THC panel **toggled off**, and watch Live Volts.
   - Typical arc voltage is 60–150 V. On the 50:1 port that's about +1.2 to 3 V.
   - The flowchart treats 85–230 V as in range. 230–280 V is "higher than expected". Over 280 V can damage the THC.
   - Under 85 V sends you to the isolation/ground checks in [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}}).
   - For reference, the CUT45's **rated output voltage** is 96 V: "Rated Output Voltage (V) 96" (my JRWPC45LH operating manual, p. 8; Razorweld's CUT45 spec sheet says 98 V). That's a nameplate rating, not a THC setpoint.

## Settings: start at the Langmuir defaults

| Setting | Range | Default (start here) |
|---|---|---|
| Nominal Voltage | 1–300 V | **0 = SMART voltage** |
| Voltage Tolerance | 0.1–10 V | **1.5 V** |
| Voltage Sample Size | 10–300 | **50** |
| SMART Voltage Offset | 0.01–1 in | **0.25 in** |
| SMART Voltage Distance | 0.01–10 in | **0.25 in** |
| Torch Speed CUTOFF | 1–100 % | **85 %** |
| Z-Speed Factor | 1–99 % | **5 %** (corrects up to 4 in out of flat over 48 in) |

What these mean:

- **SMART voltage** reads the arc right after IHS and holds that voltage for the rest of the loop. It resets every loop.
- With the default offset and distance, THC **only engages on loops longer than 0.5 in**. Small holes are left alone.
- THC moves don't show on the Z DRO. The Z axis is open-loop.

## Steps: setting a manual nominal voltage (optional)

Use this only if SMART voltage isn't giving good edges.

1. Pick the amps and feed rate from your cut settings ([CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})).
2. Jog the torch down to the real cut height by hand. The THC guide says a typical gap is 0.060 in; set it with a feeler gauge or shim. Don't use the SheetCAM 0.08 in value here. That number includes IHS springback, and there's no IHS in this test (see [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})).
3. Turn **off** the electronics box and unplug the **Z motor**, then power back up. The line test **can't include an IHS loop**, or FireControl will alarm.
4. Cut an **8–10 in straight line** and read Live Volts.
5. Enter that number as the Nominal Voltage. Plug the Z motor back in.
6. Log it in `thc_voltage` in the test-cut log, for that material, thickness, amps, and speed.

## Steps: stopping dives into corners, holes, and the end of a cut

1. **No lead-outs** on THC toolpaths. Langmuir's Fusion guide: "use NO lead out to avoid losing arc voltage at the end of a cut." The same reasoning applies to SheetCAM.
2. **No self-intersecting lead-ins or lead-outs**, and don't cross a cut you've already made (THC guide, lost arc).
3. **Leave Torch Speed CUTOFF at 85 % or raise it** if the torch dives in corners. Below that percentage of program speed, the THC freezes Z.
   - Program speed is the **fastest non-lead-in feed in the file**. The SheetCAM v1.6 post writes it as `(PS…)` at the end.
   - So if you cut small holes in a slower operation in the same file, they automatically run with the THC frozen once they're below 85 % of the fastest feed. (This is from reading the v1.6 post file. Greg9504 says the same: THC off below 85 % speed, thread 8193.)
4. **Lower the Z-Speed Factor** if it still dives. Default is 5 %.
5. **Intricate art that never reaches full speed:** the THC never switches on. Either lower the CUTOFF % or program a slower feed (THC guide).
6. **Thin sheet that lifts or warps:** THC is what keeps height on warped sheet (Langmuir consumables page). Parts under about 15 x 15 in may not need THC at all (PRO FAQ).

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Torch bobs up and down | THC over-hunting | Raise Sample Size, raise Tolerance, lower Z-Speed Factor (THC guide). |
| Torch plunges into the plate at corners or small holes | Arc voltage rises when slowing down | Raise Torch Speed CUTOFF %, lower Z-Speed Factor (THC guide). No lead-out. |
| Torch dips at the end of the cut | Lead-out losing the arc | Remove the lead-out (Fusion guide). |
| THC never turns on | Loop under 0.5 in, speed never reaches the CUTOFF, or Tolerance too wide | Lower CUTOFF %, check SMART offset + distance, narrow Tolerance (THC guide). |
| Live Volts reads 0.0 V | Computer or monitor frame touching the table frame (shields tied together) | Separate the frames; check USB shield-to-frame resistance (Holla2040, t/31460/1; Langmuir flowchart). |
| Torch goes out right after the pierce | FireControl 21.1.4 bug; bad THC cable joint; crossed or coiled leads; water in the torch | Update FireControl; inspect the THC cable; separate leads; dry the air (t/21622). |
| Odd rising or dipping now and then; non-zero Live Volts with the torch off | Water or conductive water-table chemistry bridging the IHS brass contact to the lead screw | Blow the contact dry and apply dielectric grease (PRO assembly, Z/IHS table; flowchart FLAG 1). |
| Live voltage low (under 85 V) | Enclosure not isolated, laptop charger ground, external monitor/desktop | [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}}) isolation steps; laptop on battery; UPS or USB isolator (flowchart). |
| Live Volts 0 | Polarity crossed, or wrong port | Wiring check steps 2–3. |
| Erratic live voltage on a budget cutter | Noisy arc signal | Raise Sample Size slowly (THC guide). |
| Arc lost right after the pierce on thin sheet | Pierce delay too long | [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}}). |
| False "arc lost" pause at the start | Pierce delay shorter than the cutter's pilot delay | Lengthen the pierce delay (THC guide; [Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). |
| Torch touches the plate mid-cut | IHS switch opens | The machine auto-lifts 1/16 in (PRO assembly). Find out why: tipped part, warped sheet, Z-Speed too low. |

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

- **How SMART picks its voltage. 72Pony (PrimeWeld CUT60, but this is about FireControl, not the cutter)**, t/27956/23 and t/21289/10.
  - The THC samples the arc voltage in the first few seconds after IHS sets the height, then holds that voltage.
  - So **SMART is only as good as the height at the start of the cut.** If IHS leaves the torch too high, SMART locks onto the too-high height. Check the real height by pausing a cut ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})).
- **Voltage goes up as the torch goes up. Cletus**, t/14406/2. This matches the THC guide: the THC lowers Z when the voltage reads high.
- **Live Volts reads 0.0 V. Holla2040 (CrossFire PRO with a CUT45, the same cutter as mine)**, t/31460/1.
  - The cause was a computer monitor frame touching the machine frame. The HDMI shield then tied into the USB shield.
  - His fix: a mini PC on an ungrounded wall-wart power supply. Use one that's built that way; don't cut off a ground pin.
  - Check with a meter: resistance from the USB shield to the table frame, as in the Langmuir flowchart ([Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}})).
- **Torch goes out right after the pierce**, sometimes with "TORCH MOVING BEFORE CUTTING VOLTAGE SENSED". This was thread t/21622, on a CUT45 with a PRO. Causes found there:
  - **A FireControl bug** in 21.1.4, fixed in 21.1.5. Update FireControl first.
  - **Turning THC off made the cut run** (ds690, nicaDd, TinWhisperer, toolboy). That's a way to diagnose, not a fix.
  - **A bad solder joint in the THC cable** (FultzForge).
  - **Torch lead and work lead crossed or coiled** (ds690).
  - **Water in the torch** (jnc5908404). See [Air supply, air quality, and X45 consumables]({{< relref "/procedures/04-air-quality-and-consumables.md" >}}).
  - nicaDd: plunge rate at least 50 ipm.
- **Commissioning order. TomWS**, t/24586/2:
  1. Cut a 2 in square.
  2. Do an IHS dry run with the plasma off.
  3. Cut with THC off.
  4. Then cut with THC on.
  5. Measure the part and adjust kerf.
- **ChelanJim's checklist (Hypertherm 45XP)**, t/41575/4:
  - 6 CFM at 90 psi, and dry.
  - Work lead on clean metal.
  - Torch cable, work lead, THC cable, and USB not touching, crossed, or coiled.
  - Test with a 2 in box with a 3/4 in circle inside.
- **Ferrites. Cletus**, t/17886/36: no ferrite on the raw arc-voltage line into his THC. This setup uses the divider port, not raw voltage, so it mostly doesn't apply. Staff's advice is chokes on USB ([Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}})). These don't conflict.

## Where sources disagree (and the starting choice)

- **THC off as a fix.** Several posters in t/21622 got cuts to run by turning THC off. That hides the problem; it doesn't fix it. **Go with Langmuir's fix (update FireControl) and the wiring checks.** THC off is only a diagnostic step.
- **Normal arc-voltage range.** The THC guide says 90–150 V when cutting (raw wiring). The flowchart and PRO troubleshooting say 60–150 V typical, and the flowchart uses 85–230 V as "in range". **Starting choice: the flowchart and troubleshooting numbers.** They're newer (Rev B 2021, troubleshooting updated Dec 2024) and written for the divider port, which this setup uses.
- **THC REF to GND.** The flowchart says 3.9–4.3 V DC; PRO troubleshooting says "around 4.0–4.2 V". Both are Langmuir. Treat 4.0–4.2 V as normal. A reading of 3.9 or 4.3 is borderline: note it and ask Langmuir support.
- **Typical CUT45 cutting voltage.** There's no official value. One community post (thread 38627, an XR owner, general forum member) reports 115–128 V. Langmuir staff in thread 5883 recommend SMART voltage. **Starting choice: SMART voltage plus a line test on your own machine** (planned here as the [test-cut program]({{< relref "/testing/test-cut-program.md" >}})'s V1 and H1 steps) over any posted number.
- **Lead-out.** Langmuir only says "no lead-out" in the Fusion guide. The SheetCAM guide doesn't say it. The reason (losing arc voltage at the end) is the same with either CAM, so it's followed in SheetCAM too.

## Safety

The VIM's maximum input is **300 V**. My JRWPC45LH operating manual doesn't give a no-load (open-circuit) voltage; its tech data table (p. 8) lists only the 96 V rated output. The Razorcut 45 DI manual (a related but different model) lists 300 V no-load, so treat the CUT45's open-circuit voltage as at least that. Never connect raw arc voltage on this setup. The divider port is the factory method. Any wiring inside the plasma cutter is for a qualified person only (Langmuir THC guide; my JRWPC45LH operating manual, p. 6: "Only qualified technicians are authorized to undertake the repair of this Plasma cutter equipment"). Follow the Langmuir safety page: <https://www.langmuirsystems.com/pages/safety>

## Sources

- Langmuir, LS-THC guide: <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, THC troubleshooting flowchart, Rev B 6/16/2021: <https://assets.langmuirsystems.com/file/THC+TROUBLESHOOTING+FLOW+CHART.pdf>
- Langmuir, PRO troubleshooting: <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, PRO assembly (Z-Axis & IHS table, 1/16 in auto-lift): <https://www.langmuirsystems.com/pages/pro-assembly>
- Langmuir, Fusion guide ("use NO lead out"): <https://www.langmuirsystems.com/pages/software-fusion>
- Langmuir, CrossFire PRO FAQ (when THC is needed): <https://www.langmuirsystems.com/pages/crossfire-pro>
- Langmuir, consumables and cut-problem table: <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- Langmuir, SheetCAM post v1.6 (program speed logic): <https://assets.langmuirsystems.com/firecontrol/posts/FireControl-v1.6.scpost>
- My JRWPC45LH operating manual (rated output 96 V, p. 8; CNC Torch On/Off and 50:1 divider ports, p. 9; CNC port notes, pp. 3 and 14; repairs by qualified technicians, p. 6)
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (300 V no-load voltage, which mine doesn't list): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- Forum: <https://forum.langmuirsystems.com/t/8193> (langmuir-mike troubleshooting guide; Greg9504), <https://forum.langmuirsystems.com/t/5883> (staff: FireControl doesn't set amps; SMART voltage), <https://forum.langmuirsystems.com/t/12670> (IHS on, FireControl/post v1.6, laptop on battery), <https://forum.langmuirsystems.com/t/38627> (XR, community voltages)
- Forum, experienced members: <https://forum.langmuirsystems.com/t/27956> and <https://forum.langmuirsystems.com/t/21289> (72Pony: THC sampling), <https://forum.langmuirsystems.com/t/14406> (Cletus: voltage vs. height), <https://forum.langmuirsystems.com/t/31460> (Holla2040: 0.0 V from monitor frame), <https://forum.langmuirsystems.com/t/21622> (torch out after pierce; FC 21.1.5), <https://forum.langmuirsystems.com/t/24586> (TomWS: commissioning), <https://forum.langmuirsystems.com/t/41575> (ChelanJim checklist), <https://forum.langmuirsystems.com/t/17886> (Cletus: ferrites), <https://forum.langmuirsystems.com/t/35204> (langmuir-mike: THC troubleshooting)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will come from the [test-cut log]({{< relref "/testing/test-cut-log.md" >}}) and be listed here with: Date; Material / thickness; Amps; Feed (ipm); SMART V read; Manual nominal V; CUTOFF %; Z-Speed %; Dive?; Notes.
