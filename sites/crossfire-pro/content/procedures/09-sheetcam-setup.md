---
title: "SheetCAM 8.0 Setup for FireControl (Post v1.6)"
date: 2026-10-28
tags: ["cnc", "plasma", "sheetcam", "firecontrol", "post-processor", "inkscape", "fusion"]
draft: false
weight: 8
lastmod: 2026-10-30T16:15:00-07:00
summary: "Setting up SheetCAM 8.0 on Windows to make G-code for FireControl on a CrossFire PRO with IHS and THC, using Langmuir's FireControl-v1.6 post: one-time setup, tools, and an every-job checklist."
series: ["CrossFire PRO procedures"]
series_order: 8
---

{{< lastupdated >}}

**Status: compiled research, not yet tried.**

## Applies to

SheetCAM 8.0 on Windows, making G-code for FireControl on my CrossFire PRO with IHS and THC, using Langmuir's **FireControl-v1.6.scpost**. Designs come from Inkscape (SVG or DXF) and Fusion (DXF). Doesn't cover:

- The **Mach3/Legacy** SheetCAM posts.
- Langmuir's "CrossFire without Z-axis" tool example, which has pierce and cut height set to 0. That would turn off IHS.
- The Fusion post's own settings, if you post from Fusion instead.

**Note:** Langmuir's SheetCAM guide was written for an older SheetCAM and still shows post **V1.1** in its screenshots. Menu names in SheetCAM 8.0 may differ slightly. Look for the same settings by name.

## Steps: one-time setup

1. **Download the post.** Get the latest **FireControl – SheetCAM Post** from Langmuir's Downloads page. As of this writing it's `FireControl-v1.6.scpost`. Langmuir: the latest firmware needs the latest posts.
2. **Install it.** Copy the file into SheetCAM's Posts folder. Langmuir says it's usually `C:\Program Files (x86)\SheetCam TNG\Posts`, but check on your own computer. SheetCAM 8.0 may use a different folder; confirm and write it here: ______.
3. **Options → Machine:**
   - **Machine type:** Jet Cutting **on**, Rotary Cutting **off**.
   - **Post processor:** choose **FireControl-v1.6** (not V1.1 as shown in the guide pictures).
   - **Output units** and **output folder**: your choice. Keep units the same as your FireControl setting.
   - **Z zero: Top of Work.**
4. **Make one plasma (jet) tool per material, thickness, and amps.** Put the amps in the name, for example "MS 3/16 45A", because FireControl doesn't set amps (Langmuir staff, thread 5883). Start values from Langmuir's example "Razorcut 45 w/CrossFire PRO" tool:

| Field | Start value | Replace with |
|---|---|---|
| Kerf width | 0.06 in | Your measured kerf ([Kerf width and hole/part accuracy]({{< relref "/procedures/08-kerf-and-hole-accuracy.md" >}})) |
| Feed rate | (blank in example) | Your speed-ladder winner ([CUT45 cut settings]({{< relref "/procedures/05-razorweld-45-cut-settings.md" >}})) |
| Pierce delay | 0.5 s | Your tested delay ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})) |
| Pierce height | 0.15 in | Your tested value ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})) |
| Plunge rate | 50 ipm | Leave it |
| Cut height | 0.08 in | Your tested value ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})) |
| Pause at end of cut | 0 | Leave it |

   **IHS only runs if pierce height, plunge rate, and cut height are all set** (post file header). Never set them to 0 on the PRO.

5. **Lead-in / lead-out defaults:**
   - Lead-in: a short lead-in that **doesn't cross itself or another cut** (THC guide: self-intersecting leads lose the arc).
   - **Lead-out: none** (Langmuir Fusion guide for PRO + THC: "use NO lead out"; same reason applies in SheetCAM).
   - Put lead-ins on the scrap side: outside of parts, inside of holes.
6. **Save as defaults / save the tools** so every new job starts with them.

## Steps: every job

1. **Import** the DXF or SVG (File → Import drawing). **Check the scale straight away:** measure one known dimension in SheetCAM. Inkscape SVGs sometimes come in at the wrong scale if document units and import units don't match.
2. **Add a plasma operation** with the right tool. Holes get an inside offset, the part outline an outside offset, and engraving lines no offset.
3. **Cut order:** holes and inside features first, outline last. Step through the preview to check.
4. **Cut direction:** set it so the straight side of the cut is on the part ([Getting rid of dross and bevel]({{< relref "/procedures/06-dross-and-bevel.md" >}}) test).
5. **Mixed speeds in one file:** the post writes the **fastest non-lead-in feed** in the file as program speed (the `(PS…)` line at the end). The THC freezes below **85 %** of that (default Torch Speed CUTOFF). A slower hole operation will run with THC frozen automatically ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})).
6. **Post the code.** Open the `.tap`/`.nc` file in a text editor once to check: the **first line must read `(v1.6-sc)`** (thread 27030). If it doesn't, SheetCAM isn't using the v1.6 post.
7. **In FireControl:** load the program, zero X and Y, and run **Dry Run** (no plasma, no Z moves) to check the path stays on the sheet. Then cut.
8. Note for the future: arcs smaller than 0.05 in come out as straight segments in this post, which is fine for plasma.

## What experienced forum members add

Sources are weighted as described in [About this site]({{< relref "/about.md" >}}): Langmuir first, then Razorweld/Jasic, then experienced forum members. **Numbers from members with a different plasma cutter are only a rough guide for the Razorweld CUT45 CNC (model JRWPC45LH).**

- **Back up the SheetCAM settings folder. TomWS**, t/2424/59. It's at `C:\Users\<you>\AppData\Roaming\SheetCam TNG`. **Copy it, don't move it.** Do this before changing the post or tools.
- **What actually reaches FireControl. ChelanJim**, t/1146/14 and t/31750/2. With the Fusion post, only the cut speed and kerf go into the G-code. Amps and air are set on the cutter. Langmuir staff say the same for SheetCAM (amps aren't set by FireControl, t/5883). Put the amps in the tool name.
- **Lead-ins.**
  - jamesdhatch (long-time forum member), t/19097/2: about 2x kerf. With a 0.06 in kerf, that's roughly 0.12 in.
  - richarddbeck83, t/39953/6: pierce offset bigger than the kerf; lead-in angle under 90°; pierce at the largest part of the feature.
- **Open lines vs. closed shapes. Wsidr1**, t/34970/9:
  - Use a separate operation with **center** (no offset) compensation for open lines.
  - Keep gaps between parts at least 2x kerf.
- **Cut direction. toolboy (long-time forum member)**, t/28381/41: outside cuts clockwise, inside counter-clockwise.
- **Marking holes for drilling. toolboy**, t/35951/14: use a drilling-type operation to mark holes, then drill them.
- **Plunge rate. nicaDd**, t/21622: at least 50 ipm.
- **Small holes.** ChelanJim says Fusion's Feed Optimization matters for hole quality (t/32789/3). SheetCAM's matching option hasn't been identified yet; it isn't covered in the Langmuir sources used here.
- **Holla2040 (same cutter)**, t/31460: spent hours on 18 ga SheetCAM settings, and made his own Fusion post changes. His changes aren't covered here; this page sticks to the stock v1.6 post.
- **Inkscape. jamesdhatch**, t/12525/1: stroke settings when exporting (see Langmuir's Inkscape guidance).

## Symptoms -> causes -> fixes

| Symptom | Likely cause | Fix (source) |
|---|---|---|
| FireControl won't run the file or shows a program error | Not a Langmuir post, or an old post | Re-post with FireControl-v1.6 (FireControl guide) |
| First line isn't `(v1.6-sc)` | Wrong or old post selected; more than one copy installed | Remove old posts, clean-reinstall v1.6, re-select it in Options → Machine (thread 27030, DannyD) |
| No IHS before cuts | Pierce height, plunge rate, or cut height is 0 | Set all three (post header) |
| Program bigger than the table or soft-limit alarm | Wrong units or scale on import | Check scale (step 1) and output units |
| Arc lost at the lead-in | Lead-in crosses itself or another cut | Redraw the lead-in (THC guide) |
| Torch dips at the end of each cut | Lead-out on | Set lead-out to none (Fusion guide) |
| THC never engages on any of the job | One fast operation sets the program speed and everything else is under 85 % | Split into separate files, or lower CUTOFF % ([THC setup, tuning, and stopping torch dives]({{< relref "/procedures/02-thc-setup-and-diving.md" >}})) |
| Torch rises 1 in after every cut | Normal; hard-coded in the post | Nothing to fix (SheetCAM guide) |

## Where sources disagree (and the starting choice)

- **Plunge rate.** SheetCAM guide text: 100 ipm. Example tool: 50 ipm. In v1.6 the IHS speeds are hard-coded (fast down 100, slow up 20), and plunge only sets the short pierce-to-cut move. **Starting choice: 50.**
- **Cut height on thin gauge.** Langmuir's guide says to add extra cut height on thin gauge because of springback, without a number. The example tool's 0.08 in already includes about 0.02 in ([Pierce height, pierce delay, and cut height]({{< relref "/procedures/07-pierce-height-and-delay.md" >}})). **Raise it only if a test cut on thin sheet shows the torch too close.**
- **Pierce and cut heights.** The guide says "consult your plasma cutter manufacturer". Razorweld doesn't publish them for the X45. **Starting choice: Langmuir's example values.**

## Sources

- Langmuir, SheetCAM guide: <https://www.langmuirsystems.com/pages/software-sheetcam>
- Langmuir, Downloads (latest posts): <https://www.langmuirsystems.com/pages/downloads>
- Langmuir, SheetCAM post v1.6: <https://assets.langmuirsystems.com/firecontrol/posts/FireControl-v1.6.scpost>
- Langmuir, FireControl guide (approved posts only; Dry Run): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir, Fusion guide (no lead-out with THC): <https://www.langmuirsystems.com/pages/software-fusion>
- Langmuir, THC guide (lead-in self-intersection): <https://www.langmuirsystems.com/pages/thc-guide>
- SheetCAM plasma manual: <https://www.sheetcam.com/Download/SheetCam%20TNG%20Plasma%20Manual_A4.pdf>
- Forum: <https://forum.langmuirsystems.com/t/27030> (`(v1.6-sc)` check; DannyD reinstall), <https://forum.langmuirsystems.com/t/5883> (amps not set in FireControl), <https://forum.langmuirsystems.com/t/12670> (update FireControl / post v1.6); not yet read for this site: <https://forum.langmuirsystems.com/t/6321>, <https://forum.langmuirsystems.com/t/17006>
- Forum, experienced members: <https://forum.langmuirsystems.com/t/2424> (TomWS: settings folder), <https://forum.langmuirsystems.com/t/1146> and <https://forum.langmuirsystems.com/t/31750> (ChelanJim: what reaches G-code), <https://forum.langmuirsystems.com/t/19097> and <https://forum.langmuirsystems.com/t/12525> (jamesdhatch), <https://forum.langmuirsystems.com/t/39953> (richarddbeck83), <https://forum.langmuirsystems.com/t/34970> (Wsidr1), <https://forum.langmuirsystems.com/t/28381> and <https://forum.langmuirsystems.com/t/35951> (toolboy), <https://forum.langmuirsystems.com/t/21622> (nicaDd), <https://forum.langmuirsystems.com/t/32789> (ChelanJim), <https://forum.langmuirsystems.com/t/31460> (Holla2040)

## Bernie's test results

**No results logged yet (as of 30 October 2026).** Results will be added here as they come in, with: Tool name; Material / thickness; Amps; Feed; Kerf; Pierce ht / delay; Cut ht; Proven on (date).
