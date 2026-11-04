---
title: "Water Table Chemistry and Maintenance (KOH Routine)"
date: 2026-11-03
tags: ["cnc", "plasma", "crossfire-pro", "water-table", "maintenance", "aluminum", "safety"]
draft: false
weight: 10
lastmod: 2026-11-03T20:40:00-08:00
summary: "My low-cost water table routine (softened house water plus a little potassium hydroxide), why it works, what the blue and green additives are and cost, the aluminum/hydrogen procedure, pH checks, and dumping and refilling in San Diego."
series: ["CrossFire PRO procedures"]
series_order: 10
---

{{< lastupdated >}}

**Status: the KOH routine is what I've done since about January 2025, with no rust or cut problems I've noticed. It hasn't been formally tested or measured. Everything else on this page is compiled research, not yet tried.**

## Applies to

- My **CrossFire PRO** stainless water table (built-in, about 15 gal when full; Wsidr1 gives "roughly 15 gallons" for the PRO tray, t/41806/2). Langmuir's PRO assembly guide describes it as two pans sealed with silicone, with two brass drain plugs.
- **My table water is softened, not raw city water.** San Diego city water runs through a whole-house **water softener** in my house: an ASI "White Glove Water Treatment" softening system (installed by ASI) with a **Pentair control valve, model 269869, P/N 4001442** (made in Italy by Pentair International S.A.R.L.). It's a stainless media tank plus a separate brine tank of potassium chips that regenerate it. See "My water source" below.
- My Razorweld CUT45 CNC, cutting mild steel, stainless, and aluminum, mostly 3/16 in and thinner. Some parts get powder coated afterward.
- Advice tagged **(original CrossFire)** or **(XR)** came from those tables. The original CrossFire table is smaller (Langmuir typically put in about 5 gal, ~8 gal max; langmuir-daniel, t/596/7), and the XR pans are thought to be powder-coated mild steel, not stainless (72Pony, t/43655/4). Anything about corrosion of the pan itself may not carry over to my stainless PRO pan.

## Doesn't cover

- Drain tank, pump, and filter builds (see "When a drain tank would make sense" below for links only).
- Freezing. That's not an issue in San Diego. Don't use automotive (ethylene glycol) antifreeze anyway: forum members call it toxic (rat196426, t/24652/2), and jamesdhatch warns some antifreeze "can be explosive" in a plasma water table (t/8276/3).
- Downdraft tables.

## Safety first: defer to the manufacturers

- **Potassium hydroxide (KOH, "caustic potash") is corrosive.** The Fisher/Thermo SDS for KOH flake (85–100 % KOH, CAS 1310-58-3) says it causes severe skin burns and eye damage, is harmful if swallowed, and may be corrosive to metals. **Follow the SDS for the container I actually have.** See "Safe KOH handling" below.
- **Hypertherm (Powermax manuals):** don't touch the water while cutting; ground the water table; and when cutting aluminum with water touching the underside, "free hydrogen gas may collect under the workpiece and detonate."
- **Langmuir:** fill the table only after the PRO seam silicone has cured 24 h (PRO assembly guide).
- Keep children and pets away from the table water. It's mildly caustic and has metal fines in it.

## Bernie's current routine (step-by-step)

What I do now, written down so I do it the same way each time. The small changes from my old habits are marked **(new)**.

### My water source

- **The table is filled and topped off from my house water, which goes through my whole-house water softener first.** City water runs through a stainless media tank. A separate brine tank next to it holds **potassium chips** (potassium chloride), used to regenerate (backflush) the tank.
- **What it is: an ion-exchange water softener.** It's an ASI "White Glove Water Treatment" water softening system. The control valve label reads **Pentair, model 269869, P/N 4001442**, made in Italy (Pentair International S.A.R.L.), and the control head display reads PENTAIR. The 269 valve / 869 controller naming appears to be Pentair's **Autotrol Performa 269 valve with a Logix 869 controller**; Pentair's installer manual for that pair covers water-softener installation, brine line connection, and regeneration cycles. A media tank plus a potassium-chip brine tank is the standard softener layout.
- **What a softener does to my water** (general chemistry, my reasoning):
  - It swaps the hardness (calcium and magnesium) for potassium, because I use potassium chloride.
  - It **doesn't remove bicarbonate (alkalinity), chloride, or much else**, and it **doesn't make the water neutral**. San Diego water leaves the plants at about pH 8.1–8.4 (City report), and softening shouldn't change that much.
  - **I think my water is near neutral, but a strip on the faucet water will settle that.** Log it once.

1. **Fill** with my softened house water (from a hose or faucet after the Pentair softener) to about **3/4 in below the top of the slats** (Langmuir's original CrossFire assembly guide says ¾ in below the top slat surface; Wsidr1 gives ½–¾ in for the PRO, t/41806/2). Kwikfab runs ¾–1 in below the plate per Hypertherm (t/41806/3).
2. **Add KOH: about 1 tsp (about 4–6 g) per 15 gal fill.** Dissolve it first in a quart of cold water in a plastic container (KOH into water, never water onto KOH), then pour that into the table and stir with a stick. **(new: pre-dissolve)**
3. **Check pH with a strip** about an hour later, and log it in `water-table-log.csv` (see Monitoring). **(new)** Target **9–10.5** on a fresh fill (see the softened-water math below). Don't add more KOH just because a strip reads below 11.
4. **Cut.** Clamp on the work or the drain plug as in [Work clamp, grounding, and electrical noise]({{< relref "/procedures/03-grounding-and-emi.md" >}}).
5. **Pull and rinse parts right away** (I already do this). For parts going to powder coat: rinse in fresh house water (softened water leaves fewer spots), blow or wipe dry right away, then do my normal powder coat prep. The goal is no dried-on table residue (white mineral film, dross mud) under the powder. **(new: fresh-water rinse before coat)**
6. **Top off** with plain house (softened) water as it evaporates. **Don't add KOH at every top-off.** KOH doesn't evaporate, so the water already has it. Check pH at top-offs, and add ½ tsp only if the strip reads below about 8.5. In softened water that should be rare (see below). **(new)**
7. **After any aluminum job,** follow the aluminum procedure below.
8. **Every 4–6 months (a couple of times a year), dump and refill** using the dump/refill procedure below.

## Why it works

**What any additive is for.** Plain water does the cooling. Additives mainly keep the water from going rank and keep slats, dross, and wet parts from rusting quickly (TomWS, t/29989/3; Jemejia, t/10443/2: "Any fluid other than water is optional... the idea is an alkaline solution that keeps the slats and parts from rusting"). Langmuir's water table page says the splash-back cools the part and cuts warp, noise, and smoke. That's from the water, not the chemistry.

**Why alkaline water slows rust.** The cheap home recipes forum members use (borax, washing soda, sodium nitrite) all raise the pH. Members keep their tables around pH 9–10 (keith1, borax, about 9, t/25422/8; toolboy, GreenCut and later SterlingCool, "around 9 to 10", t/13505/7, and "around 9", t/36889/9; Lil_Abners_Kustoms, above 9, t/596/8). The commercial fluids do the same: SterlingCool-PlasmaCut's data sheet gives about pH 9.5 at a 5 % mix, and LubeCorp's GreenCut FAQ says to keep pH at 9–10. KOH is just a stronger, cheaper way to get the same pH. It doesn't have the organic rust inhibitors or biocide the commercial fluids have. My table has been fine for about two years because I rinse parts right away and dump twice a year.

### What 1 tsp of KOH really does (my math, with assumptions)

Assumptions:

- 1 level tsp of KOH flake or pellets is about **4–6 g**. It depends on flake size; I haven't weighed mine.
- Hardware-store or lab KOH is **85–100 % KOH** (Fisher's flake product is labeled 85 %; the rest is mostly water).
- 15 gal = 56.8 L. KOH is 56.1 g/mol and fully dissolves.
- Room temperature. The math ignores activity corrections. It's a rough estimate, not a lab result.

- **Softened water (my actual supply):** calcium and magnesium are replaced by potassium. Bicarbonate is unchanged at the City's 2025 plant averages of **96–121 mg/L alkalinity as CaCO3** (ranges 46–155). The starting pH is about 8.2. Air CO2 is about 420 ppm.
- Script: `research/water/ph_soft.py` (softened water); `ph_calc.py` and `ph2.py` (distilled and raw tap water, kept for comparison).

Results:

| Case | pH |
|---|---|
| 4–6 g in **distilled** water, fresh | **11.0–11.3** (1.1–1.9 mM hydroxide) |
| 4–6 g in **softened house water (mine)**, fresh | **about 10.2–10.6** |
| Same, weeks later, open to air (absorbs CO2) | drifts to **about 8.7–8.8** and stays there |
| Softened water with **no KOH**, open to air | **about 8.5–8.6** |
| 15 g (about 1 Tbsp) in softened water, fresh → weeks later | about 11.3–11.4 → about 9.0 |
| *For comparison:* 4–6 g in **raw (hard) city water** | about 10.1–10.6 fresh, then white calcium carbonate scale settles out and the pH can fall to about 8.2–10.1 |

San Diego figures: 2025 plant averages of **96–121 mg/L alkalinity**, **145–243 mg/L total hardness**, **87–156 mg/L chloride**, pH 8.1–8.4 (City of San Diego 2025 water quality report; calcium from the "additional characteristics" sheet).

**What that means in plain words:**

- **"Near neutral" is probably not right.** Softened San Diego water still carries its bicarbonate, so plain house water should read around 8–8.5, even before any KOH. **The strips decide.** If the faucet water really reads about 7, my house water differs from the City averages, so I'll trust the strip and re-run the numbers.
- **The "about pH 11" estimate only holds in distilled water.** In my softened water, the KOH first reacts with the bicarbonate. A fresh fill should read **about 10–10.5**.
- **No calcium means no scale step,** so the pH doesn't drop the way it would in hard water. Over weeks, air CO2 pulls it down to **about 8.7–8.8** and holds it there. That's only slightly above what plain softened water reaches on its own (about 8.5–8.6).
- **Devil's advocate:** in softened water, **1 tsp of KOH mostly buys a few weeks of pH 10+ after each fill.** After that, the table sits near 8.7 with or without it. That still rust-proofs fresh parts better than plain water during those weeks. My two years of good results are consistent with that. But **more KOH isn't the answer**: even 1 Tbsp only reaches about 9.0 long-term, and it makes aluminum dross fizz harder.
- **Revised target:** **9–10.5** on a fresh fill, and **8.5–9 later** is normal. Add ½ tsp only if it falls **below about 8.5**. Plain air won't take it that low, so a reading that low suggests acid from cutting or a measuring problem. (The arc makes nitrogen oxides, which form acids in water; that's my reasoning, not a sourced number.) **This replaces the earlier "pH 9–11, about 11" guidance.**

### Softened-water side effects for the table

- **Less white scale.** Most of the calcium is gone, so the KOH won't drop out calcium carbonate crust. I should see much less white build-up on the pan and slats than raw city water gives. Any white crust now is more likely dried salts, or the softener running out (time to add chips).
- **Buffering against acid is the same; the KOH just goes further.** Softening leaves the bicarbonate (the acid buffer) in place. What's gone is the calcium that, in hard water, "used up" part of the KOH as scale. So each teaspoon raises the pH a little more and for longer than in raw city water. **Pre-dissolve, measure, and don't double-dose.**
- **Chloride is unchanged.** Softening doesn't remove chloride (City averages 87–156 mg/L), and potassium chloride regeneration doesn't add any meaningful amount to the water once the softener rinses after regenerating. Brine carryover should be negligible; that's my reasoning, not a sourced figure. Chloride is what drives pitting on stainless and rust on steel. **Evaporation concentrates it with every top-off,** which is another reason to keep dumping and refilling twice a year.
- **Slightly more conductive, not less.** Each calcium ion gets swapped for two potassium ions. Softened water adds about 110–190 mg/L of potassium (my estimate from the hardness figures), so the water is a bit more conductive than plain city water. **Keep the IHS contact dry and greased** (see below).
- **Aluminum precautions matter at least as much.** Softened water by itself already sits near **pH 8.5**, the top of aluminum's safe range. With KOH it's above that for weeks after every fill. The aluminum procedure below stays as written.

- **1 tsp per 15 gal is a very dilute solution: about 0.01 % by weight.** At top-off strength it's mildly alkaline, a bit like strong soapy water. It's not lye-strength.

### Things that were checked and are not a concern

- **Caustic embrittlement: not a concern.** It's stress-corrosion cracking of carbon steel in concentrated hydroxide, usually several percent NaOH or more, often hot, at stressed seams in boilers (NACE SP0403; Georgia Tech/IPST caustic SCC report). My table is about 0.01 % KOH at room temperature, hundreds of times weaker, and the pan is stainless.
- **Effect on cut quality: none found.** No Langmuir or Hypertherm source says pH changes the cut. Forum members using borax or KOH-like alkaline water report "no issues with the water table or cut quality" (rodjava, t/13505/15).

### Things that do matter (corrections to the earlier advice)

- **Conductive water can bother the THC / IHS. This one is official (PRO).** Langmuir's PRO assembly troubleshooting says: "If conductive medium (such as chemically treated water table water) can bridge the small gap between the brass screw contact and the lead screw, it will energize the machine frame with a low voltage that is readable by the THC controller." Langmuir's fix: blow the contact area dry and apply dielectric grease. So pH itself doesn't change the cut, but **any treated water (KOH included) is more conductive than plain water, and splash on the Z/IHS contact can cause odd THC/IHS behavior.** Splash on the torch can also matter: KeithBarr found the torch wet under the tip cover, and thinks his additive (Pico Quench Guard) reached the small spring-loaded safety pins there, giving an E04 error (t/25263/6; Everlast 62i, rough guide only).
- **Galvanic corrosion of zinc-plated screws.** langmuir-daniel (staff): any rust inhibitor is an electrolyte, so zinc-plated screws in the pan will corrode. It stops once the zinc is gone, or you can swap to stainless screws (t/23574/12, t/23574/27; Bigdaddy2166's test, t/23574/28). **(XR)** caution: on the XR's mild steel pan, stainless screws make the pan the sacrificial metal (72Pony, t/43655/4). My PRO pan is stainless, so stainless screws are the right match.
- **Seam leaks.** DakotaEngineer reports seam leaks starting after adding an additive (t/43655/9; table type not stated). Check the center seam at each dump.

## Aluminum/hydrogen procedure

**Why it matters more with KOH.** Aluminum's oxide film protects it only between about **pH 4 and 8.5**. Above 8.5, alkaline water dissolves the film, and then the aluminum corrodes quickly (Aluminium Federation fact sheet 04). When aluminum corrodes in water, it gives off hydrogen. **So KOH water at pH 9–10 makes aluminum dross and fines give off hydrogen faster than plain water would.** That agrees with the earlier advice, and with langmuir-daniel's staff advice that aluminum slats should only be used with pure water, because "any" inhibitor starts aluminum corrosion (t/25422/2, t/25422/4).

**How big the risk is on my table.**

- **Hypertherm FAQ:** on an open water table, hydrogen bubbles are "most likely harmless". The danger is gas trapped under something. Hypertherm also says: "Do not cut aluminum alloys underwater or on a water table unless you can prevent the accumulation of hydrogen gas." **Never cut aluminum-lithium alloys near water.**
- **ESAB:** the biggest danger is a plate left on the table, where gas collects underneath. Their fix is an aerator.
- **Torchmate safety notice:** ventilate under the sheet, wait at least 5 minutes between sheets, and warped sheets trap more gas.
- **Forum veterans (CrossFire-sized tables):**
  - jamesdhatch: real hazard, "but context matters," and the industrial scenario isn't something you can replicate on a CrossFire (t/9176/11).
  - mr540602: the real danger is in drain tanks, where aluminum fines keep making hydrogen, and in leaving a plate sitting on the table (t/9176/12).
  - OffRoadDevilDog: it would take a trapped pocket under a sheet left for hours, then a re-light (t/2725/12).
  - gamblegarage cuts a lot of aluminum. He sees bubbles and has had "a few loud pops". Run the water lower, don't leave the plate on, stir the water (t/2972/3).
  - john543 (t/2972/11): melted aluminum droplets that sink keep giving off hydrogen; blow air over the table before cutting if you've cut aluminum recently. His context is industrial, at a much larger scale.

**My aluminum procedure (all variants; my table has no drain tank, which removes the biggest risk):**

1. **Before:** check the strip. If the water is at pH 10 or higher, consider lowering the water about ½ in below the slats (rat196426 runs ½ in below the slats for aluminum, t/34932/2). For a big aluminum job, consider a fresh plain-water fill with no KOH, then add KOH back afterward.
2. **Never cut aluminum-lithium alloys over water** (Hypertherm). Mine are ordinary 5052/6061-type sheet. Check the alloy if unsure.
3. **During:** cut, then **lift the sheet off promptly.** Don't leave a sheet or skeleton lying flat on the slats. Pause a few minutes between sheets, and slosh the water with a stick to release bubbles (Torchmate; gamblegarage). Expect harmless fizzing; occasional small pops are reported (gamblegarage). **Keep flames, the torch, and grinding sparks away from any trapped area.**
4. **After:** **scoop out the aluminum dross and fines the same day.** They keep fizzing in alkaline water. Let them dry in an open metal can outdoors, not a sealed bag or bucket, before they go in the trash or scrap.
5. **Don't mix steel and aluminum fines in a sealed container.** Aluminum and iron oxide are the thermite pair. This is my own reasoning, and a reason to keep the two cleanups apart.

**A product claim to treat with caution:** KCI says **Plasma Green 9010** is formulated for aluminum and "will not produce hydrogen gas" (KCI product page). Hydrogen comes from the aluminum reacting with water, not from the fluid, so no additive can stop it entirely. It may slow the reaction. **I trust Hypertherm's guidance over the marketing line.**

## Additives compared

Prices checked 3 November 2026 except where dated. Cost per fill assumes my 15 gal table.

| Option | Active ingredient(s) | Price (source) | About cost per 15 gal fill | Pros vs my KOH | Cons vs my KOH |
|---|---|---|---|---|---|
| **KOH (mine)** | Potassium hydroxide | Already on hand | Pennies (1 tsp) | Cheapest; tiny amount; easy to hit pH 9–10 | Corrosive solid to store; no organic inhibitor or biocide; speeds aluminum corrosion; fiddly to dose (easy to overdo) |
| **SterlingCool-PlasmaCut (the blue one)** | Triethanolamine 10–15 %, ethanolamine 1–5 %, n-butylethanolamine 1–5 %, triazine biocide 1–5 %, trimethylhexanoic acid 1–5 % (SDS as posted by TinWhisperer, t/19486/35); no nitrites; about pH 9.5 at 5 % (TDS) | **$192 / 5 gal pail**, $1,377 / 55 gal; free US shipping except a $25 flat fee to CA (Cutting Fluids Direct) | 20:1 → about 0.75 gal ≈ **$29** + CA fee | Real rust inhibitor and biocide; "most use Sterling Cool" (Bigdaddy2166, t/38248/5); toolboy's water stays clear (t/20264/2); maker says it "helps prevent hydrogen build-up" | About 100× the cost per fill; disposal per its SDS (Knick's question and Wsidr1's answer, t/47725) |
| **Plasma Green 9010 (KCI, a green one)** | Triethanolamine-based (MSDS found by TinWhisperer, t/19486/28); no propylene glycol (KCI's chemist, t/19486/26) | **9010: $124 / 5 gal, $39 / 1 gal** (KCI) | 20:1 → about **$19** | Cheaper than SterlingCool; 9010 aimed at aluminum; forum users like it (GaltsGarage, one jug for almost three years, t/43938/10; Sticks, t/43938/7) | Same cost and handling objections, on a smaller scale; "will not produce hydrogen" is a marketing claim (see above) |
| **GreenCut Plasma (LubeCorp, a green one)** | 1,2-propylene glycol 15–40 % (SDS); pH 9.6–9.7 | **About $225 / 5 gal pail + $53 shipping (toolboy, 2021, t/12797/6)**; BrettMavriK paid $200 (t/596/36). Not rechecked in 2026. | 20:1 → about **$34**+ | SDS says it "can be generally disposed into sewer" (consult local authorities); FAQ: check pH every 2 weeks, keep 9–10 | Price; brownfox got a "syrupy residue" at the recommended mix and runs it thinner (t/12797/7); KCI's chemist says propylene glycol can feed microbes (t/19486/26) |
| **Pico Quench Guard (Pico Chemical)** | Not checked | Not checked (Trick Tools, Wsidr1, t/13505/24) | — | Commercial | Wsidr1 got repeated algae/slime with it and doesn't recommend it (t/42405/12, t/36889/5) |
| **Borax** | Sodium borate | About $5–6 a box (rodjava, t/13505/15; JaVelin, t/8276/10) | About 1–2 cups | **Langmuir staff-endorsed** (langmuir-daniel, t/596/2; fine on stainless, t/596/39); Langmuir-Nick (staff): "That'll work just fine" (t/32823/7); gentle; not a caustic | Leaves hard white deposits (JaVelin, t/8276/7; rat196426, t/35059/13); Scoopburt's slats rusted on borax (t/38248/24); bulkier dose |
| **Washing soda** | Sodium carbonate | Grocery store | About ⅓ cup (Dirtboater, t/10443/9) | Cheap, mild, easy to buy | Not perfect against rust (Dirtboater); still raises pH, so same aluminum issue |
| **Sodium nitrite homebrew** | Sodium nitrite + Physan 20 + blue dye | About $15/lb (ChelanJim, t/32823/3) | Small | **Staff-endorsed and tested** (langmuir-daniel, t/596/2, t/596/5) | **Toxic if swallowed** (Tankueray's livestock-death account, t/8276/1); hard to buy now; disposal issues (pacesetter, t/596/55). **Not recommended here.** |

**Langmuir's official stance:** "We don't have an official recommendation or affiliated brand" (Langmuir-Nick, staff, t/32823/7, 2024). The original CrossFire assembly guide only says "a plasma compatible rust inhibiting solution." Langmuir staff have endorsed borax and sodium nitrite over the years. **No Langmuir source mentions KOH.** I found no Hypertherm-branded table additive.

**Devil's advocate on my choice:** KOH works for the same reason borax and washing soda work (it raises the pH), and my results back it up. The honest downsides:

1. It's the only option here that's a corrosive solid in the house.
2. It's easy to overdose. 1 Tbsp would be 3 tsp, still under pH 12, but it would chew aluminum faster.
3. Without a biocide, rankness depends on my dumping twice a year.

If I ever want something milder to store, **borax is the staff-endorsed cheap swap.**

## Safe KOH handling

**The SDS on my actual container overrides anything here.** If mine has no SDS, use the Fisher/Thermo KOH flake SDS (linked in Sources). The basics it covers:

- **Eye protection (goggles) and chemical-resistant gloves** when handling the dry KOH or the pre-mix. Dry flakes pick up moisture and burn skin.
- **Add KOH to water, never water to KOH.** It heats up as it dissolves. Use a plastic or stainless container, not aluminum.
- Store it **sealed, labeled, dry, and away from aluminum and acids**, out of reach of kids and pets.
- **Skin or eye contact: flush with lots of water and follow the SDS first-aid section.** Eyes get medical attention.
- At table strength (about 0.01 %), it's mildly irritating. Still rinse hands after reaching into the table.

## Dump/refill procedure

1. **Settle.** Stop cutting and leave the table still overnight, so the fines settle (ds690 lets it settle a day, t/15924/10; keith1, t/15924/9).
2. **Drain the clear water** from the brass drain plugs into buckets, stopping before the sludge comes out.
3. **Where the clear water can go (San Diego; hedged):**
   - **Never** into a storm drain, street, or gutter. San Diego Municipal Code §43.0304 bans non-storm-water discharges, and the City's minimum BMPs say process and wash water must be contained and disposed of properly.
   - **Sanitary sewer (house drain) only within limits.** The City's Industrial Wastewater code (§64.0510) bans sewer discharges at pH ≥12.5 or below 5.0, plus metal particles, mud, and toxic metals. My settled water should be about pH 8.5–10, under the limit. **It isn't clear that a household drain dump of shop wastewater is covered or allowed, so call ESD at 858-694-7000 and ask** before using the sewer.
   - Lowest-risk option for small volumes: **let it evaporate in shallow open trays** (Wsidr1, a licensed Certified Hazardous Material Technician, for non-business users, t/47725/6), then treat the residue like the sludge.
   - Forum members also report pouring borax/plain-water tables on dirt (jamesdhatch, t/15924/16). The City's BMPs allow landscaped areas for some wash water. **I'm not relying on that for KOH and metal-fines water without asking the City.**
4. **Sludge.**
   - Scoop or wet-vac it out (clio, t/36889/3), or let the table dry 3–5 days and scrape it with a drywall knife (Wsidr1, t/36889/5).
   - Let it **dry fully in an open container** (aluminum fines especially).
   - Then bag it for the trash or scrap. Wsidr1's rule of thumb: landfills take non-hazardous waste with no free liquids (t/47725/6).
   - **Caveat:** stainless dross carries chromium and nickel, and California's hazardous-waste rules are stricter than federal. If in doubt, ask the **City HHW Transfer Facility at Miramar** (5161 Convoy St; free for City residents with proof of residency, by appointment, Wed/Sat 9–3; containers up to 5 gal, call 858-694-7000 for more). The City says hazardous waste can't legally go to the sewer, storm drain, ground, or trash.
5. **California's corrosive line is pH ≥12.5** (Title 22 §66261.22; DTSC). My table water is well under that. **Leftover dry KOH is a corrosive product. Take it to HHW; don't trash it or pour it out** (see Cletus's disposal bill, t/596/94).
6. **Inspect and clean.**
   - Rinse the pan.
   - Check the center seam silicone and the drain plugs for leaks, and the zinc screws for corrosion.
   - Wipe the Z/IHS contact area dry and re-grease it per Langmuir.
7. **Refill** per steps 1–3 of my routine, and log the fill.

## Monitoring: pH strips, what to log

- **Strips:** a cheap pH 0–14 strip roll, or better, strips that read 7–14 in 0.5 steps. Dip, wait for the time on the label, compare in daylight. **Target 9–10.5 fresh, 8.5–9 later is normal.** Below 8.5: add ½ tsp KOH (pre-dissolved) and recheck. Above about 10.5: just top off with water. Don't add KOH. **Also strip-test the faucet water once** and log it, to confirm whether my softened water is near 7 or near 8.
- **When:** right after a fill (about 1 hour), before cutting sessions, and at each top-off.
- **Log in `water-table-log.csv`** (in my CNC folder), one row each time. Columns: **Date, pH, Top-off (gal), KOH added (g or tsp), Notes.**
  - In Notes, record: materials cut (especially aluminum), smell or slime, rust on slats or parts, white scale, leaks, odd THC/IHS behavior, and dump/refill dates.
- **Signals to act on:**
  - rotten or swampy smell, or slime: dump early;
  - rust on fresh parts within a day: check the pH;
  - THC acting up after heavy splash: dry and grease the IHS contact;
  - white crust building up: shouldn't happen much with softened water. Check the softener's chip level and settings, and scrape at the next dump.

## When a drain tank would make sense

Many forum veterans use them: "Most use Sterling Cool and hold it in a tank underneath the table" (Bigdaddy2166, t/38248/5), and toolboy filters and keeps his fluid (t/20264/2). The point is to save expensive fluid and avoid standing water. Those reasons don't fit my cheap-KOH, 15 gal, dump-twice-a-year setup. **It would make sense if:**

- I switch to SterlingCool or Plasma Green. At about $20–30 a fill, saving and filtering the fluid pays off (toolboy's 5 µm filter, t/20264/2; his fluid hasn't been changed in years, t/47725/2).
- The table goes rank or rusty between dumps, or I start leaving it for weeks unused. Draining it dry stops the "standing water gets nasty" problem (brownfox: standing fluid "will get nasty anyway if you aren't using it frequently", t/38248/6).
- I start cutting a lot more, so the sludge builds faster.

**Devil's advocate:** a drain tank is where the aluminum hydrogen risk actually lives (mr540602, t/9176/12). If I ever build one, it should be vented, never sealed, and cleaned of aluminum fines. Build threads: ntkfabworks (t/1060), Shrules' drain valve (t/7168), TinWhisperer's filter thread (t/20264).

## What experienced forum members add

- **TomWS** (t/29989/3): plain water does the cooling. Additives are for clear water and rust-free slats.
- **toolboy** (t/13505/7, t/36889/9, t/12797/3): keeps the pH around 9–10. Not draining and filtering "means the mixture works harder", so the pH is harder to hold.
- **TinWhisperer** (t/36889/4, PRO): with a lid, he drained only a few times a year and got a few 5-gal buckets of "iron mud". That's similar to my routine.
- **ChelanJim** (t/36518/5): aluminum makes H2, but with open systems and small output an explosive situation is unlikely. In his own build he added 8 oz washing soda and about 3 oz Physan, no filtration or draining (t/20034/14).
- **Wsidr1** (t/36889/5, t/47725/6): even with additive he got slime from adding rain-barrel water, so use tap (house) water. For home disposal: evaporate, solidify, landfill if non-hazardous.

## Where sources disagree (and the starting choice)

- **Which additive?**
  - Langmuir has no official recommendation (Langmuir-Nick). Staff have endorsed borax and sodium nitrite (langmuir-daniel).
  - Veterans split between commercial fluids (SterlingCool, Plasma Green, GreenCut) and borax or washing soda.
  - No one in the sources uses KOH.
  - **Starting choice:** keep KOH at about pH 9–10, since it's working. Borax is the fallback.
- **pH target.**
  - The earlier guidance said 9–11.
  - Forum and GreenCut say 9–10. SterlingCool is about 9.5.
  - My softened-water math: about 10–10.5 fresh, settling to about 8.7.
  - **Starting choice: 9–10.5 fresh, and accept 8.5–9 between fills.**
- **Water level.**
  - Langmuir: ¾ in below the slats (original CrossFire guide).
  - Hypertherm's SYNC machine-cutting guide: 3 in below the plate for best cut quality and to protect the cartridge (curmudgeon quoting p. 65, t/45698/4).
  - Kwikfab: ¾–1 in below the plate.
  - **Starting choice:** about ¾ in below the slats (Langmuir) for steel and ½ in lower for aluminum. The SYNC figure is for Hypertherm SYNC torches, not my X45.
- **Hydrogen on an open CrossFire table.**
  - Industrial accounts (john543) and Hypertherm's general warning point to a serious hazard.
  - Hypertherm's FAQ and most veterans say it's low on an open small table.
  - **Starting choice:** treat it as low but real. Don't leave sheets on the table, clean out aluminum fines, don't seal up wet aluminum waste, and no drain tank.
- **Plasma Green 9010 "no hydrogen".** That's KCI's claim. It conflicts with Hypertherm and basic chemistry. **Trust Hypertherm.**

## Sources

- Langmuir, PRO assembly (24 h silicone cure, brass drain plugs, treated-water IHS bridging, dielectric grease; PRO): <https://www.langmuirsystems.com/pages/pro-assembly>
- Langmuir, CrossFire assembly step 8 (rust-inhibiting solution, ¾ in below slats; original CrossFire): <https://www.langmuirsystems.com/pages/crossfire-assembly>
- Langmuir, water table product page (cooling, warp, smoke; original CrossFire table, not PRO): <https://www.langmuirsystems.com/products/water-table>
- Langmuir, FireControl guide (clamp on drain plug): <https://www.langmuirsystems.com/pages/firecontrol-guide>
- Langmuir staff on the forum:
  - langmuir-daniel: <https://forum.langmuirsystems.com/t/596> (posts 2, 5, 7, 39, 42: sodium nitrite, borax, homebrew, table volume, stainless);
  - langmuir-daniel: <https://forum.langmuirsystems.com/t/23574> (posts 12, 27: galvanic corrosion of zinc screws);
  - langmuir-daniel: <https://forum.langmuirsystems.com/t/25422> (posts 2, 4: aluminum slats, pure water only);
  - Langmuir-Nick: <https://forum.langmuirsystems.com/t/32823> (post 7: no official recommendation).
- Hypertherm, Powermax600 operator manual (hydrogen under aluminum; aeration manifold; don't touch water; ground table): <https://www.hypermaxonline.com/assets/images/pdfs/Powermax600%20Operator%20Manual.pdf>
- Hypertherm FAQ, aluminum on a water table: <https://www.hypertherm.com/resources/faqs/is-it-okay-to-plasma-cut-aluminum-on-a-water-table/>
- Hypertherm HT4001 manual, aeration manifold appendix: <https://www.manualsdir.com/manuals/772254/hypertherm-ht4001-plasma-arc-cutting-system.html?page=235>
- ESAB, plasma cutting aluminum on a water table: <https://esab.com/us/nam_en/esab-university/blogs/can-you-plasma-cut-aluminum-on-a-water-table/>
- Torchmate, safety notice (aluminum and hydrogen): <https://torchmate.com/uploads/images/PDFs/SafetyNotice.pdf>
- Aluminium Federation, fact sheet 04 (oxide stable pH 4.0–8.5): <https://alfed.org.uk/wp-content/uploads/2023/10/Aluminium-Corrosion.pdf>
- Cutting Fluids Direct, SterlingCool-PlasmaCut 5 gal (price, CA shipping): <https://www.cuttingfluidsdirect.com/products/sterlingcool-plasmacut-premium-plasma-cutting-fluid-5-gallon-pail>
- SterlingCool-PlasmaCut technical data sheet (pH, mix ratio, no nitrites): <https://www.plasmatech.co.uk/pdf/SterlingCool-PlasmaCutTDS.pdf>
- KCI (Konzen Chemical), Plasma Green 9010 (price, aluminum and hydrogen claims): <https://konzenchemical.com/products/plasma-green-9010-5-gallon-pail>
- Plasma Green 9010 MSDS and SterlingCool SDS contents (TinWhisperer, KCI's chemist): see forum thread t/19486 below.
- LubeCorp, GreenCut Plasma SDS: <https://www.lubecorp.com/wp-content/uploads/GreenCut-Plasma-SDS-150707.pdf>
- LubeCorp, GreenCut FAQ (pH 9–10): <https://www.lubecorp.com/wp-content/uploads/GreenCut-Plasma_Frequently-Asked-Questions-160804.pdf>
- Fisher Scientific / Thermo, potassium hydroxide flake 85 % (SDS via the product page): <https://www.fishersci.com/shop/products/potassium-hydroxide-flake-85-thermo-scientific/AAA1619936>
- NACE SP0403 preview (caustic SCC of carbon steel): <https://webstore.ansi.org/preview-pages/NACE/preview_NACE+SP0403-2008.pdf>
- Georgia Tech / IPST, caustic stress corrosion cracking of carbon steels: <https://repository.gatech.edu/server/api/core/bitstreams/65987bfd-7884-49b2-92fa-eccdac3f66a0/content>
- Pentair, Autotrol Performa UF 269 / Logix 869 installer manual (water softener valve and controller; brine and regeneration; my valve is labeled Pentair 269869, P/N 4001442, and appears to be from this line): <https://blaulain.com/wp-content/uploads/2022/12/Autotrol_Performa_UF_269_Logix_869_en.pdf>
- City of San Diego, 2025 drinking water quality report (alkalinity, hardness, chloride, pH): <https://www.sandiego.gov/sites/default/files/2026-06/pud-annual-drinking-water-quality-report-2025.pdf>
- City of San Diego, 2025 additional characteristics (calcium, bicarbonate): <https://www.sandiego.gov/sites/default/files/2026-06/additional-characteristics.pdf>
- San Diego Municipal Code ch. 4 art. 3 div. 3 (§43.0304, storm drain discharges): <https://docs.sandiego.gov/municode/MunicodeChapter04/Ch04Art03Division03.pdf>
- City of San Diego, minimum BMPs (process and wash water): <https://www.sandiego.gov/sites/default/files/2025-04/minimum-best-mgmt-practices.pdf>
- San Diego Municipal Code ch. 6 art. 4 div. 5 (§64.0510, sewer pH and solids limits): <https://docs.sandiego.gov/municode/MuniCodeChapter06/Ch06Art04Division05.pdf>
- City of San Diego, Household Hazardous Waste (Miramar facility, appointments): <https://www.sandiego.gov/environmental-services/ep/hazardous>
- California DTSC, corrosive wastes (pH ≤2 or ≥12.5): <https://dtsc.ca.gov/corrosive-wastes/>
- Comparison page (via ChelanJim): <https://cncplasmainfo.com/watertreatement.html>
- Forum, experienced members:
  - <https://forum.langmuirsystems.com/t/29989> (TomWS);
  - <https://forum.langmuirsystems.com/t/13505> (toolboy, rodjava, Wsidr1);
  - <https://forum.langmuirsystems.com/t/36889> (toolboy, TinWhisperer, Wsidr1, clio);
  - <https://forum.langmuirsystems.com/t/12797> (toolboy prices, brownfox);
  - <https://forum.langmuirsystems.com/t/19486> (SDS contents, KCI chemist);
  - <https://forum.langmuirsystems.com/t/9176> (jamesdhatch, mr540602);
  - <https://forum.langmuirsystems.com/t/2972> (gamblegarage, john543, Lil_Abners_Kustoms);
  - <https://forum.langmuirsystems.com/t/2725> (OffRoadDevilDog);
  - <https://forum.langmuirsystems.com/t/36518> and <https://forum.langmuirsystems.com/t/20034> (ChelanJim);
  - <https://forum.langmuirsystems.com/t/47725> (Wsidr1, toolboy: disposal);
  - <https://forum.langmuirsystems.com/t/15924> (wastewater handling);
  - <https://forum.langmuirsystems.com/t/38248> (Bigdaddy2166, brownfox, Scoopburt);
  - <https://forum.langmuirsystems.com/t/43655> (72Pony, DakotaEngineer);
  - <https://forum.langmuirsystems.com/t/41806> (Wsidr1, Kwikfab: water level);
  - <https://forum.langmuirsystems.com/t/45698> (Hypertherm SYNC water level);
  - <https://forum.langmuirsystems.com/t/34932> (rat196426);
  - <https://forum.langmuirsystems.com/t/10443> (Jemejia, Dirtboater);
  - <https://forum.langmuirsystems.com/t/8276> (Tankueray, JaVelin, jamesdhatch);
  - <https://forum.langmuirsystems.com/t/24652> and <https://forum.langmuirsystems.com/t/35059> (rat196426);
  - <https://forum.langmuirsystems.com/t/42405> (Wsidr1: slime);
  - <https://forum.langmuirsystems.com/t/43938> (GaltsGarage, Sticks: Plasma Green);
  - <https://forum.langmuirsystems.com/t/25263> (KeithBarr);
  - <https://forum.langmuirsystems.com/t/23574> (Bigdaddy2166: stainless screws);
  - <https://forum.langmuirsystems.com/t/5656> (jamesdhatch: borax per 7 gal);
  - <https://forum.langmuirsystems.com/t/20264>, <https://forum.langmuirsystems.com/t/1060>, <https://forum.langmuirsystems.com/t/7168> (drain/filter builds).

## Bernie's test results

**No results logged yet (as of 3 November 2026).** My routine has run since about January 2025 with no rust or cut problems I've noticed, but no pH readings were recorded. Readings go in `water-table-log.csv` with: Date; pH; Top-off (gal); KOH added (g or tsp); Notes.
