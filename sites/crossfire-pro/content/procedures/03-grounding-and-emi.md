---
title: "Work Clamp, Grounding, and Electrical Noise (EMI)"
date: 2026-10-28
tags: ["cnc", "plasma", "crossfire-pro", "grounding", "emi", "thc", "safety"]
draft: false
weight: 2
lastmod: 2026-10-30T18:30:00-07:00
summary: "Where to put the work clamp, how to run Langmuir's electronics isolation test, and how to break ground loops safely, without ever defeating a safety ground."
series: ["CrossFire PRO procedures"]
series_order: 2
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.** The clamp location below is my starting choice; the isolation test and fixes come from Langmuir documents and forum posts.

## Applies to

Bernie's setup:

- CrossFire PRO with THC and IHS, in a home shop.
- The electronics enclosure is **wall-mounted on plywood away from the table**: not touching any metal, and joined to the table only by the motor cables. It sits on one side of the compressor, with the Razorweld CUT45 CNC (model JRWPC45LH) on the other side. That gives the frame isolation Langmuir's isolator mount is there for.
- Because the box isn't on the leg, if the flowchart's isolation test ever reads low, check the motor cable shields and connectors instead of the leg mount.
- FireControl runs on a computer next to the table.
- The CUT45 is on a **230 V** circuit (my JRWPC45LH operating manual, p. 8: "Power Supply / Phases (V-Ph) 230v - 1 +/- 15%"; the 95–265 V range quoted here before was from the dual-voltage Razorcut 45 DI manual, a different model). The table electronics run on a separate **120 V, 20 A** outlet.

Doesn't cover:

- The XR's grounding instructions (clamp straight to the workpiece) are for a different machine.
- The Mach3/Gen1 legacy noise fixes are for old electronics.
- Hypertherm's HF-start notes don't apply. The CUT45 uses a non-high-frequency (NHF) pilot start.

## Safety first: defer to the manufacturers

- **House wiring, the 230 V receptacle, and grounding the supply are an electrician's job.** Langmuir: wire to the National Electrical Code and hire a licensed electrician. My JRWPC45LH operating manual says: "Connect the primary input cable according to American standards and regulations. ANSI Z49.1." and "Incorrectly installed or improperly grounded equipment is dangerous." (p. 4); "We recommend (RCD) safety switch is used with this equipment to detect any leakage of current to earth." (p. 4); and "PLEASE AVOID USING AN EXTENSION LEAD ON ALL INVERTER WELDING AND CUTTING MACHINES" (p. 3). My manual doesn't give a breaker size, plug type, or input current; that's for the electrician (the Razorcut 45 DI manual, a related model, has its own figures that I don't use here).
- **Residential supply:** an earlier version of this page quoted an EMC Class A, "not to be connected to a residential low-voltage power supply grid" warning. That came from the Razorcut 45 DI manual, a different model. My JRWPC45LH operating manual has no such wording: its safety section (pp. 4–6) has no EMC class or residential-supply warning, and only lists the EU Low Voltage and EMC Directives it was designed to (p. 6). So I've removed it. Follow your own cutter's manual and Langmuir's safety page, and have a licensed electrician handle the 230 V circuit. **Never defeat or remove a safety ground** on the cutter, the table, or the house wiring.
- **The power supply switch on the table electronics** must match the **wall outlet the electronics plug into** (120 V), not the plasma cutter's voltage (Langmuir PRO page).
- Make every connection with the power off. My manual: "Disconnect power source before performing any service or repairs" (p. 4), and repairs are for "qualified technicians" only (p. 6). The Razorcut 45 DI manual (related model) also warns that high voltage stays inside after switch-off; treat the CUT45 the same way.
- **Placement:** my manual says to keep the cutter 1 ft from the wall and keep the louvers clear (p. 6). Its listed use limits are up to 80 % humidity and "-14°F to +104°F" (p. 6).

Links: <https://www.langmuirsystems.com/pages/safety>, my JRWPC45LH operating manual (safety pp. 4–6), and (related model only) the Razorcut 45 DI manual (§5, Installation).

## Steps: work clamp and grounding

1. **Clean the clamp spot to bare metal.** Langmuir: "poor clamp contact on clean metal" is a cause of the arc not transferring. My manual: "Connect the Earth Clamp securely to the work piece or the work bench" (p. 11); the earth lead goes to the "Output connector (DC+)" (p. 9). The Razorcut 45 DI manual's error table (related model) also lists checking the earth clamp when the cutting circuit is blocked.
2. **Clamp location (see the conflict below).** **My starting choice is the water-table drain plug**, as the FireControl guide and the CrossFire assembly guide say. Follow the THC flowchart's tests using the **slat bed** as the flowchart says.
3. **Check that the clamp spot, slats, and workpiece are all connected.** Set a multimeter to resistance (or continuity). Probe from the clamp spot to a slat, then to the top of the workpiece. If you don't get continuity to the workpiece (rust, mill scale, paint under the sheet), clamp to the workpiece directly for that job.
4. **Keep the clamp lead and the torch lead apart from the USB cable and the motor cables** wherever you can. This isn't stated as a step in the official docs checked for this page; it follows from the general reason Langmuir gives for EMI (see the forum sources) and costs nothing to do.

## Steps: isolating the electronics (from the Langmuir THC flowchart)

Do these with everything set up as for cutting: THC, IHS, and USB connected, computer on, cutter on, work clamp on.

1. **Resistance test.** Set the meter to resistance. Probe the silver shell of the USB plug where it enters the electronics box, then the slat bed where the work clamp is connected. **Langmuir's pass value is more than 10,000 ohms.**
2. If it's under 10,000 ohms, unplug the USB cable from the electronics box, take the work clamp off the slat bed, and measure again.
   - **Still low:** the enclosure is touching the frame. Take the box off the leg (3 screws) and try a cut. (My box is already off the table on the wall, so on my setup this step means checking that nothing metal touches it.) It has to sit on the **boomerang-shaped plastic isolator mount**, and the mounting screws mustn't dig into the box's sheet metal. If you never got the isolator, contact Langmuir support (support@langmuirsystems.com, per the flowchart).
   - **OK with the USB unplugged:** the problem is the computer's ground.
3. **Laptop:** unplug the charger and run on battery. If the laptop sits on a metal stand that touches the frame, put **cardboard** between laptop and stand. Repeat the live-voltage test.
4. **Desktop PC or external monitor:** run them on a **UPS**, or power the electronics through a **USB voltage isolator** (Langmuir sells one).
5. **Motor and IHS plugs:** check that the D-sub motor plugs are screwed in and not arc-damaged (PRO assembly troubleshooting). Keep the IHS contact dry; water-table water bridging the brass contact gives false voltage ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
6. Re-run the THC **TEST** (Health Check) and a straight-line cut and confirm normal Live Volts ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| Arc won't transfer; pilot arc only | Poor clamp contact, worn electrode, loose consumables | Clean bare-metal clamp spot; check consumables (Langmuir consumables page). |
| Low live voltage (under about 85 V) | Enclosure touching the frame; computer ground through the charger or monitor | Isolation steps 1–4 (flowchart). |
| Non-zero voltage with the torch off; random THC moves | Moisture or water-table chemistry at the IHS brass contact | Blow dry, apply dielectric grease, re-test (flowchart FLAG 1; PRO assembly). |
| FireControl disconnects, or motion freezes when the arc starts | Electrical noise into USB | Laptop on battery; UPS or USB isolator; route cables apart; then see the staff fix below. |
| Motor skips only while cutting | Noise or arc damage at the motor plugs | Check and screw in the D-sub plugs (PRO assembly troubleshooting). |

## If noise problems persist

These are **not first steps**. Do them only after the steps above, ideally after talking to Langmuir support.

- **Ferrite chokes on cables / a board-level inductor fix.** Posted by Langmuir staff (langmuir-daniel) in thread 9175. The board version it was written for isn't confirmed. Ask Langmuir whether it applies to your PRO's board before soldering anything.
- **An isolated 0–5 V signal converter.** A community fix from Kytor (thread 39578, long-time forum member). It's a modification, so don't do it unless support agrees.
- **A dedicated earth ground rod for the table.** One community post (thread 38627, an XR owner, general forum member) gives a resistance target. Don't take an earthing number from a forum post. Grounding rods and bonding are for a licensed electrician.

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the CUT45.**

> **Never remove or defeat a safety ground.** Some forum members posted that they removed the ground pin on a PC or monitor, or used a 2-prong "cheater" adapter. **Don't do that. This page doesn't recommend it.** Follow the manufacturers' grounding instructions and a licensed electrician; experienced members TomWS and Bigdaddy2166 also warn against it (t/24659/16). To break a ground loop, run the laptop on battery, or use a USB ground-loop isolator or a UPS.

- **Why isolation matters. TomWS**, t/35669/19.
  - The work clamp is both the plasma's current return and the THC's voltage reference. The table touches it all the time through the slats.
  - So keep the control electronics isolated from the table, and tie together **only the grounds that need to be tied**, at one point (a "star" ground). He built this into his own enclosure. On the PRO, Langmuir's design already does the job (the control box's isolation and the flowchart's >10,000 ohm test), so follow Langmuir's steps and take TomWS's idea as the reason why.
- **Don't float the whole system. TomWS and Bigdaddy2166 **, t/24659/16: removing the safety ground from the whole system is "craziness".
- **Ground loops between the computer and the control box. Bigdaddy2166 (Everlast cutter)**, t/32012/17 and t/36138/1.
  - A computer and a control box on the same building ground can make a loop. Use an ohm test to find it.
  - His fix: a **USB ground-loop isolator**. That's the recommended fix here too.
  - He also suggested a non-grounding plug adapter on the control box. **Don't do that part; it defeats the safety ground.**
  - EMI ground straps on the motors (t/48104/10) are a later step if noise persists.
- **Cletus (PrimeWeld CUT60)**, t/17886/36 and t/9175/136.
  - He has the control box isolated, and a 15 ft USB cable with ferrites on both ends.
  - He found his interference was a ground loop.
  - He also removed PC and monitor ground pins. **Don't copy that; never remove ground pins.**
- **Monitor frame touching the table. Holla2040 (same CUT45)**, t/31460/1. The THC read 0.0 V until he separated the frame. His fix was a mini PC on a factory-ungrounded wall wart. Keep computer and monitor frames off the table and gantry.
- **72Pony**, t/24052/24: ferrite chokes on the USB. He also suggested an ungrounded plug. **Don't do that part; it defeats the safety ground.**
- **Cable routing and clamping.**
  - ChelanJim, t/41575/4: work lead on clean metal. Torch cable, work lead, THC cable, and USB must not touch, cross, or coil.
  - Wsidr1, t/35218/5: clamp onto the part at the start of every cut, and uncoil power cords.
  - Bigdaddy2166, t/43254/14, and nicaDd (long-time forum member), t/45396/3: clamp on the metal being cut, not on the slats.
  - ds690, t/21622: crossed or coiled leads caused torch-out problems.
- **Magnetic clamps on aluminum or stainless. jamesdhatch (long-time forum member)**, t/31161/8: put a steel strip under the sheet so the magnet clamp has something to grab and the circuit still goes through the work.

## Where sources disagree (and the starting choice)

- **Safety ground (some forum members remove the PC ground pin or use a 2-prong adapter).** Cletus, 72Pony, and Bigdaddy2166 (in one post) suggested it. TomWS and Bigdaddy2166 (t/24659/16) call floating the safety ground "craziness". **Never remove or defeat a safety ground.** Follow the manufacturers' grounding instructions and a licensed electrician (TomWS and Bigdaddy2166 agree). To break a ground loop, use a laptop on battery, a USB ground-loop isolator, or a UPS instead.
- **Clamp on the part vs. the drain plug.** Several experienced members (Wsidr1, Bigdaddy2166, ChelanJim, nicaDd) clamp on the workpiece itself, on clean metal. That agrees with my manual ("securely to the work piece or the work bench", p. 11) and the Razorcut 45 DI manual's general advice to clamp close to the cut. **Suggested:** clamp on the part when you can, and always on clean metal.
- **Where the work clamp goes (Langmuir documents give different clamp locations).**
  - THC guide (2020): machine frame.
  - FireControl guide and CrossFire assembly: water-table drain plug.
  - THC flowchart Rev B (2021): slat bed (one step also says "machine frame").
  - XR guide: straight to the workpiece.
  - Community (thread 12670): ground to the material.

  **Bernie's starting choice:** the **drain plug by default** (the PRO-era operating guide), the slat bed for the flowchart tests, and the workpiece as a test whenever transfer or cut quality is poor. **Not yet confirmed:** whether the slats and drain plug are bonded to the frame. It's on my list to ask Langmuir support: "On a CrossFire PRO with the stainless water table, which clamp point do you recommend now, and are the slats and drain plug bonded to the frame?"
- **Ground-rod resistance target.** That's community (XR) only. Defer to a licensed electrician and the NEC.

## Sources

- Langmuir, Safety (NEC, electrician): <https://www.langmuirsystems.com/pages/safety>
- Langmuir, THC troubleshooting flowchart Rev B: <https://assets.langmuirsystems.com/file/THC+TROUBLESHOOTING+FLOW+CHART.pdf>
- Langmuir, THC guide (clamp on frame; wiring): <https://www.langmuirsystems.com/pages/thc-guide>
- Langmuir, FireControl guide (clamp on drain plug): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, CrossFire assembly (clamp on drain plug): <https://www.langmuirsystems.com/pages/crossfire-assembly>
- Langmuir, XR assembly (clamp on workpiece; XR only): <https://www.langmuirsystems.com/pages/xr-assembly>
- Langmuir, PRO troubleshooting: <https://www.langmuirsystems.com/pages/protroubleshooting>
- Langmuir, PRO assembly (motor plugs, IHS contact): <https://www.langmuirsystems.com/pages/pro-assembly>
- Langmuir, CrossFire PRO page (power supply switch matches the outlet): <https://www.langmuirsystems.com/pages/crossfire-pro>
- Langmuir, consumables and cut problems: <https://www.langmuirsystems.com/pages/crossfire-parts-consumables>
- My JRWPC45LH operating manual (230 V ±15 %, p. 8; extension-lead warning, p. 3; ANSI Z49.1, grounding, and RCD, p. 4; placement and repairs, p. 6; earth clamp, pp. 9 and 11)
- Razorweld Razorcut 45 DI manual 2022 (a related but different model, not my JRWPC45LH) (§5 Installation; earth clamp; high voltage after switch-off. Its Class A EMC / residential-supply warning isn't in my JRWPC45LH manual and is no longer used here): <https://razorweld.com/wp-content/uploads/2022/11/RAZORCUT45DI-INSTRUCTION-MANUAL-2022.pdf>
- Langmuir, "Razorweld Razorcut 45 with Machine Torch" product page (NHF start): <https://www.langmuirsystems.com/products/razorweld-razorcut-45-with-machine-torch>
- Forum: <https://forum.langmuirsystems.com/t/9175> (langmuir-daniel, chokes/inductor fix), <https://forum.langmuirsystems.com/t/39578> (Kytor, isolated converter), <https://forum.langmuirsystems.com/t/31057> (laptop on battery), <https://forum.langmuirsystems.com/t/12670> (ground to material), <https://forum.langmuirsystems.com/t/38627> (XR grounding, community)
- Forum, experienced members: <https://forum.langmuirsystems.com/t/35669> (TomWS: isolation, star ground), <https://forum.langmuirsystems.com/t/24659> (TomWS/Bigdaddy2166: don't float the safety ground), <https://forum.langmuirsystems.com/t/32012> and <https://forum.langmuirsystems.com/t/36138> (Bigdaddy2166: ground loop; USB isolator), <https://forum.langmuirsystems.com/t/48104> (Bigdaddy2166: EMI straps), <https://forum.langmuirsystems.com/t/17886> and <https://forum.langmuirsystems.com/t/9175> (Cletus), <https://forum.langmuirsystems.com/t/31460> (Holla2040), <https://forum.langmuirsystems.com/t/24052> (72Pony), <https://forum.langmuirsystems.com/t/41575> (ChelanJim), <https://forum.langmuirsystems.com/t/35218> (Wsidr1), <https://forum.langmuirsystems.com/t/43254> (Bigdaddy2166), <https://forum.langmuirsystems.com/t/45396> (nicaDd), <https://forum.langmuirsystems.com/t/31161> (jamesdhatch: steel strip)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will be added here as they come in, with: Date; USB shell to slat resistance; Clamp location; Computer power; Live V on a test line; Notes.
