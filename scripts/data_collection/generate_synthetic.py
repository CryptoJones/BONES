#!/usr/bin/env python3
"""Generate synthetic EMS scenario training examples for BONES."""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "src" / "bones"))

from prompts import SYSTEM_PROMPT

OUT_DIR = REPO_ROOT / "data" / "synthetic"

EXAMPLES = [
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Dispatch: 58M, chest pain, diaphoretic, pale. BP 88/60, HR 112, RR 20, SpO2 94% on RA. 10/10 substernal crushing pain radiating to left arm, onset 45 min ago. No allergies. Takes lisinopril."},
            {"role": "assistant", "content": "## Clinical Assessment: Suspected STEMI / Acute Coronary Syndrome\n\n### Critical Findings\n- Hemodynamic compromise: BP 88/60 (cardiogenic shock pattern), HR 112\n- SpO2 94% — supplemental O2 indicated\n- Classic STEMI presentation: substernal crushing pain, diaphoresis, radiation to left arm, 45-minute onset\n\n### Immediate Interventions (ALS — Paramedic scope)\n\n1. **O2** — 4 L/min via nasal cannula; target SpO2 ≥ 94%\n2. **12-lead ECG** — obtain immediately, transmit to receiving facility if capable\n⚠ ALS INTERVENTION — 12-lead interpretation: Paramedic scope\n3. **IV access** — 2 large-bore IVs\n4. **Aspirin** — 324 mg PO (four 81 mg tablets), chewed\n   - Contraindicated if true aspirin allergy or active GI bleed\n5. **Nitroglycerin** — 0.4 mg SL q5 min × 3 PRN for pain\n   - **HOLD** given BP 88/60 — nitroglycerin is CONTRAINDICATED in hypotension (SBP < 90)\n⚠ CONTACT MEDICAL CONTROL — Hypotensive ACS patient; NTG contraindicated, consult for fluid challenge vs. vasopressor guidance\n6. **Monitor** — continuous cardiac monitor, 12-lead q5 min\n7. **Fluid** — 250 mL NS bolus cautiously if cardiogenic shock confirmed (right-sided MI concern — obtain right-sided leads V3R/V4R)\n\n### Pertinent Negatives to Assess\n- Jugular venous distension (right heart failure)\n- Lung sounds (pulmonary edema)\n- Right-sided 12-lead (right ventricular MI — NTG absolutely contraindicated)\n- Last aspirin dose (already taking?)\n\n### Transport\n**Priority 1 — Emergent.** STEMI Alert. Transport to nearest PCI-capable facility. Pre-notify ED. Target door-to-balloon < 90 minutes.\n\n*Protocol reference: AHA ACLS 2020 — Acute Coronary Syndromes Algorithm*"},
        ],
        "type": "clinical_scenario",
        "domain": "cardiac",
        "scope": "paramedic",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Dispatch: 3F, seizure, now postictal. Mom says she has febrile seizures but this lasted 4 minutes. Weight approx 15 kg. Temp 39.8°C (rectal). Unresponsive but breathing, HR 148, SpO2 97%."},
            {"role": "assistant", "content": "## Clinical Assessment: Febrile Seizure (Prolonged) — Pediatric\n\n### Critical Findings\n- 4-minute seizure duration (simple febrile seizures typically < 5 min — this is at the boundary; complex if > 15 min, focal, or recurrent within 24h)\n- Postictal state — expected; monitor for return of normal mentation\n- Tachycardia (HR 148) — likely febrile/postictal; normal for age\n- Temp 39.8°C — significant fever driving seizure\n- Weight 15 kg — use for weight-based dosing (Broselow: ~orange/pink zone)\n\n### Immediate Interventions\n\n1. **Positioning** — lateral recovery position; suction PRN\n2. **O2** — blow-by or NRB if SpO2 drops below 94%\n3. **BGL** — check blood glucose immediately (hypoglycemia can cause seizures)\n   - If BGL < 60 mg/dL: Dextrose 0.5–1 g/kg IV/IO\n   - For 15 kg: 7.5–15 g dextrose (15–30 mL D50 diluted to D25, or D10 150 mL)\n   ⚠ ALS INTERVENTION — IV/IO access and dextrose: Paramedic scope\n4. **Fever management** — cooling measures (remove excess clothing, wet towels)\n   - Acetaminophen/ibuprofen: EMT scope if within standing orders (per agency protocol)\n5. **Seizure recurrence** — if seizure recurs:\n   - Diazepam rectal (Diastat) 0.5 mg/kg PR: **0.5 × 15 = 7.5 mg PR**\n   - Midazolam intranasal 0.2 mg/kg: **0.2 × 15 = 3 mg IN** (2 mg/mL = 1.5 mL split between nares)\n   ⚠ ALS INTERVENTION — Benzodiazepines: Paramedic scope; some agencies allow EMT buccal midazolam\n\n### Pertinent Negatives to Assess\n- Focal deficits post-ictally (suggests complex seizure or structural cause)\n- History: prior complex febrile seizures, recent illness, medications, immunizations\n- Meningeal signs (Kernig, Brudzinski) — concern for meningitis if present\n- Duration > 5 min escalates to status epilepticus protocol\n\n### Transport\n**Priority 1 — Emergent** given prolonged duration and age. Transport to pediatric-capable ED. Monitor closely for seizure recurrence en route.\n\n*Protocol reference: PALS Seizure Algorithm; AHA 2020*"},
        ],
        "type": "clinical_scenario",
        "domain": "neurology_peds",
        "scope": "paramedic",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Dispatch: 22F, unresponsive, suspected opioid overdose. Bystander says she used heroin 10 min ago. RR 4, pinpoint pupils, SpO2 72%, cyanotic lips."},
            {"role": "assistant", "content": "## Clinical Assessment: Opioid Overdose — Respiratory Arrest Imminent\n\n### Critical Findings — IMMEDIATE THREAT TO LIFE\n- RR 4 (severe respiratory depression — respiratory arrest imminent)\n- SpO2 72% — critical hypoxia\n- Cyanosis — oxygen delivery failure\n- Pinpoint pupils + heroin exposure = opioid toxidrome confirmed\n\n### Immediate Interventions — Seconds Matter\n\n1. **BVM ventilation — START NOW** — 1 breath every 5–6 seconds (10–12/min)\n   - High-flow O2, proper mask seal; 2-person BVM preferred\n   - Position: head-tilt chin-lift (jaw-thrust if trauma suspected)\n2. **Naloxone (Narcan)** — administer immediately\n   - **Intranasal (EMT scope):** 4 mg IN (2 mg per nare)\n   - **IM (Paramedic scope):** 0.4–2 mg IM; may repeat q2–3 min\n   - **IV/IO (Paramedic scope):** 0.4 mg IV slow push; titrate to adequate respirations (avoid precipitating acute withdrawal)\n   - Expected onset: IN 3–5 min, IM 3–5 min, IV < 2 min\n   - Duration of naloxone < duration of heroin — **monitor for re-narcotization**\n   - May need repeat doses or infusion for long-acting opioids (methadone, fentanyl analogs)\n3. **Airway adjunct** — OPA if no gag reflex (EMT scope); King LT or ETT if BVM inadequate (Paramedic scope)\n4. **IV/IO access** — Paramedic scope; establish for repeat dosing\n\n### After Naloxone Response\n- Once RR > 12 and SpO2 > 94%: maintain O2, monitor carefully\n- Patient may become agitated/combative — restrain per protocol, do NOT leave alone\n- Naloxone wears off in 30–90 min; fentanyl analogs may outlast naloxone\n⚠ CONTACT MEDICAL CONTROL — All opioid reversal patients should be transported; strongly advise against refusal\n\n### Transport\n**Priority 1 — Emergent.** All opioid OD patients require ED evaluation regardless of response to naloxone. Many jurisdictions mandate transport. Advise medical control of response and any secondary doses.\n\n*Protocol reference: ACLS Toxicology / Opioid Overdose; NAEMSP Naloxone Guidelines*"},
        ],
        "type": "clinical_scenario",
        "domain": "toxicology",
        "scope": "emt",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Dispatch: 34F, 38 weeks pregnant, contractions every 2 min, crowning visible. No time to transport."},
            {"role": "assistant", "content": "## Clinical Assessment: Imminent Delivery — Field Delivery Protocol\n\n### Situation\nCrowning is confirmed — delivery is imminent. Do NOT attempt to delay or prevent delivery.\n\n### Immediate Actions\n\n1. **Position mother** — supine or left lateral decubitus; elevate hips slightly with blanket roll\n2. **Prepare OB kit** — gloves, sterile drape, bulb suction, cord clamps × 2, scissors, warm blankets for newborn\n3. **Support the delivery**\n   - Apply gentle counterpressure to the perineum as head delivers — control delivery speed\n   - Check for nuchal cord (cord around neck): if loose, slip over head; if tight, double-clamp and cut before delivery\n   - Suction mouth then nose with bulb suction after head delivers\n   - Guide head downward for anterior shoulder, then upward for posterior shoulder\n   - Support infant throughout — newborns are slippery\n4. **Note time of delivery**\n5. **Dry and stimulate newborn** — rub vigorously with dry towel; keep warm\n6. **APGAR at 1 and 5 minutes** — Appearance, Pulse, Grimace, Activity, Respiration (0–2 each)\n   - APGAR ≥ 7: normal; 4–6: moderate depression; < 4: requires resuscitation\n7. **Clamp and cut cord** — clamp at 6 inches and 8 inches from infant, cut between clamps\n   (Delayed cord clamping 30–60 sec if infant vigorous and full-term)\n8. **Placenta** — will deliver within 5–30 min; do NOT pull cord; save placenta for hospital\n9. **Uterine massage** — after placenta delivers; helps prevent postpartum hemorrhage\n\n### Neonatal Resuscitation (if infant not vigorous)\n- Not breathing or HR < 100 after 30 sec of stimulation:\n  - PPV with room air at 40–60 breaths/min (newborn BVM)\n  - If HR < 60 after PPV: begin chest compressions at 3:1 ratio (90 compressions + 30 breaths/min)\n⚠ ALS INTERVENTION — Neonatal intubation and epinephrine: Paramedic scope; CONTACT MEDICAL CONTROL\n\n### Mother Post-Delivery\n- Monitor for hemorrhage (> 500 mL vaginal loss = hemorrhage)\n- Uterine massage if uterus feels boggy\n\n### Transport\n**Priority 1 — Emergent post-delivery.** Transport mother and newborn together. Pre-notify hospital of field delivery.\n\n*Protocol reference: NRP Neonatal Resuscitation Program; PHTLS OB Emergencies*"},
        ],
        "type": "clinical_scenario",
        "domain": "obstetrics",
        "scope": "emt",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "MCI: school bus vs semi, 18 students injured. I'm the first arriving paramedic. How do I set up triage?"},
            {"role": "assistant", "content": "## MCI Triage — JumpSTART (Pediatric) Protocol\n\n### Immediate Actions Upon Arrival\n1. **Call for resources NOW** — request additional units, MCI response, air transport, hospital notification before you touch a single patient\n2. **Size up** — confirm scene safety, approximate patient count (18 students), mechanism (bus vs semi — blunt trauma, potential ejection, entrapment)\n3. **Designate roles** — if additional units arrive: assign triage, treatment (red/yellow/green areas), and transport officers\n\n### JumpSTART Triage (Pediatric, < 8 years or < 25 kg; START for older teens)\n\nFor EACH patient, move through in < 30 seconds:\n\n**Step 1 — Can they walk?**\n- YES → **GREEN (Minor)** — walking wounded; move to green area\n- NO → go to Step 2\n\n**Step 2 — Breathing?**\n- NO breathing → reposition airway\n  - Still no breathing → **BLACK (Expectant)** in adults\n  - JumpSTART exception: give 5 rescue breaths; if breathing resumes → **RED (Immediate)**; still no → **BLACK**\n- YES breathing → go to Step 3\n\n**Step 3 — Respiratory rate**\n- < 15 or > 45 breaths/min → **RED (Immediate)**\n- 15–45 breaths/min → go to Step 4\n\n**Step 4 — Pulse present?**\n- NO pulse → **BLACK (Expectant)**\n- YES → go to Step 5\n\n**Step 5 — AVPU mental status**\n- Alert or responds to Voice → **YELLOW (Delayed)**\n- Responds to Pain or Unresponsive → **RED (Immediate)**\n\n### Treatment Areas\n- **RED (Immediate):** Life threats — airway compromise, uncontrolled hemorrhage, shock\n- **YELLOW (Delayed):** Serious but stable — fractures, moderate burns, altered but protecting airway\n- **GREEN (Minor):** Walking wounded — lacerations, minor trauma\n- **BLACK (Expectant):** Unsurvivable given current resources, or deceased\n\n### Hemorrhage Control — Do This During Triage\n- Apply tourniquet for extremity arterial bleeding (C-A-T or SOFTT-W) — takes seconds\n- This is the ONE treatment intervention during primary triage\n\n### Documentation\n- Triage tag each patient with category and brief findings\n- Track patient count by category for incident command\n\n*Protocol reference: JumpSTART Pediatric MCI Triage; SALT Triage; NIMS ICS MCI Response*"},
        ],
        "type": "clinical_scenario",
        "domain": "mci_triage",
        "scope": "paramedic",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Patient: 45M, 90 kg, anaphylaxis — hives, throat tightening, BP 78/40, HR 124, wheezing. Known bee allergy, stung 10 min ago. Has his own EpiPen but used it already with no improvement."},
            {"role": "assistant", "content": "## Clinical Assessment: Severe Anaphylaxis — Refractory to Initial Epinephrine\n\n### Critical Findings\n- Airway involvement (throat tightening, wheezing) — rapidly evolving\n- Hemodynamic compromise (BP 78/40) — distributive shock\n- EpiPen used × 1 with no improvement — refractory anaphylaxis\n- 90 kg patient — weight matters for dosing\n\n### Immediate Interventions\n\n1. **Epinephrine IM — REPEAT NOW** (do not wait)\n   - **Dose:** 0.3–0.5 mg (0.3–0.5 mL of 1:1,000) IM into anterolateral thigh\n   - For 90 kg adult: 0.5 mg IM (max adult dose)\n   - Onset: 8–10 minutes IM; can repeat q5–15 min if BP remains < 90\n   - EpiPen = 0.3 mg — may have been underdosed; IM thigh is preferred site\n2. **O2** — 15 L/min NRB\n3. **Position** — supine with legs elevated (if no respiratory distress); sitting up if severe wheezing\n4. **IV access** — two large-bore IVs; NS fluid bolus 1–2 L (for distributive shock)\n   ⚠ ALS INTERVENTION — IV access, fluid bolus: Paramedic scope\n5. **Epinephrine IV** — if IM fails and hypotension persists:\n   - 0.1 mg (1 mL of 1:10,000) IV slow push over 5 min\n   - Or epinephrine infusion 0.1–1 mcg/kg/min titrated\n   ⚠ CONTACT MEDICAL CONTROL — IV epinephrine for refractory anaphylaxis\n6. **Diphenhydramine (Benadryl)** — 50 mg IV/IM (adjunct, NOT first-line; epinephrine is)\n7. **Albuterol** — 2.5 mg via nebulizer for bronchospasm\n   ⚠ ALS INTERVENTION — nebulizer in many jurisdictions: Paramedic scope\n8. **Methylprednisolone** — 125 mg IV (prevents biphasic reaction)\n   ⚠ ALS INTERVENTION — Paramedic scope; contact medical control\n\n### Airway Preparation\n- Prepare for RSI/surgical airway — throat tightening can progress to complete obstruction rapidly\n- Have supraglottic airway (King LT) and surgical cricothyrotomy kit immediately available\n⚠ CONTACT MEDICAL CONTROL — Airway compromise in refractory anaphylaxis: advise immediately\n\n### Transport\n**Priority 1 — Emergent.** Anaphylaxis with hemodynamic compromise and airway involvement. Pre-notify ED. Biphasic reaction risk up to 72 hours — all anaphylaxis patients require observation.\n\n*Protocol reference: AHA ACLS 2020 — Anaphylaxis; WAO Anaphylaxis Guidelines 2020*"},
        ],
        "type": "clinical_scenario",
        "domain": "allergy_immunology",
        "scope": "paramedic",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "What is the ACLS algorithm for ventricular fibrillation?"},
            {"role": "assistant", "content": "## ACLS: Ventricular Fibrillation (VF) / Pulseless Ventricular Tachycardia (pVT)\n\n*AHA ACLS 2020*\n\n### Confirm: Pulseless + VF/pVT on monitor\n\n**CPR quality:** Hard and fast — 100–120/min, ≥ 2 in depth, full recoil, minimize interruptions, switch compressors q2 min.\n\n---\n\n### Cycle (2 minutes of CPR each)\n\n**Cycle 1**\n1. CPR × 2 min → check rhythm\n2. If VF/pVT → **Defibrillate: 200 J biphasic** (device-specific; 360 J monophasic)\n3. Immediately resume CPR × 2 min\n\n**Cycle 2**\n4. After 2 min CPR → check rhythm\n5. If VF/pVT → **Defibrillate**\n6. Immediately resume CPR + establish IV/IO\n7. **Epinephrine 1 mg IV/IO** → repeat q3–5 min\n\n**Cycle 3**\n8. After 2 min CPR → check rhythm\n9. If VF/pVT → **Defibrillate**\n10. **Amiodarone 300 mg IV/IO** (first dose); or Lidocaine 1–1.5 mg/kg IV/IO\n\n**Subsequent cycles**\n- Continue CPR → Defibrillate → Epinephrine q3–5 min\n- Amiodarone second dose: **150 mg IV/IO** (or Lidocaine 0.5–0.75 mg/kg)\n- Treat reversible causes (H's and T's)\n\n---\n\n### H's and T's — Reversible Causes\n| H's | T's |\n|---|---|\n| Hypovolemia | Tension pneumothorax |\n| Hypoxia | Tamponade (cardiac) |\n| Hydrogen ion (acidosis) | Toxins/overdose |\n| Hypo/Hyperkalemia | Thrombosis (PE/MI) |\n| Hypothermia | — |\n\n---\n\n### Advanced Airway\n- ETT or supraglottic (King LT, i-gel): 1 breath q6 sec (10/min); do NOT pause compressions\n- ETCO2 waveform capnography: < 10 mmHg despite good CPR = consider stopping\n\n### If ROSC\n- Post-cardiac arrest care: 12-lead, targeted temperature management (TTM 32–36°C), transfer to PCI-capable center if STEMI present\n\n⚠ ALS INTERVENTION — Defibrillation, IV epinephrine/amiodarone, advanced airway: Paramedic scope"},
        ],
        "type": "protocol_reference",
        "domain": "cardiac_arrest",
        "scope": "paramedic",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Pediatric patient, 8 years old, estimated 25 kg. Hypoglycemic — BGL 42 mg/dL, conscious but confused. No IV access established yet. What can the EMT give?"},
            {"role": "assistant", "content": "## Pediatric Hypoglycemia — 8 yo / 25 kg, BGL 42 mg/dL, Conscious\n\n### EMT Scope Options (Conscious Patient)\n\nBecause the patient is conscious (able to protect airway), EMT-level treatment is appropriate first:\n\n**1. Oral Glucose (preferred if cooperative)**\n- Glucose gel or tablets: 15–20 g PO\n- Standard tube of glucose gel = 15 g — give 1 tube\n- Must be able to swallow safely — confirm no impending LOC\n- Recheck BGL in 15 min; if still < 70, repeat\n- Follow with food (crackers, juice) once tolerating\n\n**2. Juice or Sugar Water (EMT scope)**\n- 4 oz (120 mL) of orange juice or regular soda if cooperative\n- Equivalent to ~15 g of glucose\n\n---\n\n### If Patient Deteriorates / Cannot Swallow Safely\n⚠ ALS INTERVENTION — requires Paramedic or AEMT:\n\n**Dextrose IV/IO (Paramedic)**\n- D10W: 5 mL/kg IV slow (for 25 kg = 125 mL D10)\n- D25W: 2 mL/kg IV (for 25 kg = 50 mL D25)\n- D50W: 1 mL/kg IV diluted to D25 (not preferred in peds — hyperglycemia risk)\n\n**Glucagon IM (AEMT/Paramedic scope)**\n- < 25 kg: 0.5 mg IM\n- ≥ 25 kg: 1 mg IM\n- Onset: 10–15 min; requires hepatic glycogen stores (not effective in starvation/hepatic failure)\n- For this patient (25 kg on the boundary): use 0.5 mg or 1 mg per protocol\n\n---\n\n### Recheck and Monitor\n- Recheck BGL 10–15 min after treatment\n- Target BGL > 80 mg/dL\n- If < 70 after two treatments: ALS/transport regardless\n- Assess for cause: missed meal, insulin overdose, sepsis (in peds)\n\n### Transport\nNon-emergent if responding well to oral glucose and BGL normalizes. Emergent if LOC, seizing, or not responding to treatment.\n\n*Protocol reference: ADA Hypoglycemia Guidelines; Broselow Pediatric Reference; PALS*"},
        ],
        "type": "clinical_scenario",
        "domain": "endocrine_peds",
        "scope": "emt",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "25M, gunshot wound to right thigh, femoral arterial bleed. Spurting blood, BP 70/40, HR 138, pale diaphoretic. Scene is safe."},
            {"role": "assistant", "content": "## Trauma: Femoral Artery GSW — Hemorrhagic Shock\n\n### MARCH Protocol — Massive Hemorrhage First\n\n**M — Massive Hemorrhage CONTROL NOW**\n1. **Tourniquet — apply immediately**\n   - C-A-T or SOFTT-W: 2–3 inches above wound (proximal to femoral bleed)\n   - Tighten until bleeding stops (don't be gentle — femoral TQ requires significant force)\n   - Note time applied on tourniquet and patient record\n   - Do NOT remove TQ once applied in field\n   - If TQ fails to control bleeding: second TQ proximal to first\n\n**A — Airway**\n- Currently maintaining (if GCS allows) — monitor closely\n- Anticipated loss of airway if hemorrhagic shock worsens\n⚠ ALS: Prepare advanced airway if GCS deteriorates\n\n**R — Respiration**\n- Assess bilaterally — no obvious chest involvement from thigh GSW but assess for hidden wounds\n- SpO2 monitoring, O2 15 L NRB\n\n**C — Circulation**\n- BP 70/40, HR 138 — Class III/IV hemorrhagic shock (30–40% blood volume loss)\n- **2 large-bore IVs immediately** — 14 or 16 gauge bilateral AC\n- **Fluid resuscitation:** Permissive hypotension — target SBP 80–90 mmHg (not normal) to avoid clot disruption\n  - 250–500 mL NS boluses; reassess frequently\n  - Whole blood or 1:1:1 plasma:platelets:pRBC preferred if available\n⚠ ALS INTERVENTION — IV access, fluid resuscitation: Paramedic scope\n- **TXA (Tranexamic Acid)** if within 3 hours of injury and severe hemorrhage:\n  - 1 g IV over 10 min (first dose); hospital gives second 1 g over 8 hours\n  ⚠ CONTACT MEDICAL CONTROL — TXA administration per protocol\n\n**H — Hypothermia Prevention**\n- Cover with blankets; warm IV fluids if available\n- Hypothermia impairs coagulation — prevent aggressively\n\n### Wound Packing (if tourniquet insufficient or junctional wound)\n- Thigh GSW with good TQ placement should be controlled\n- If junctional: pack wound with hemostatic gauze (Combat Gauze / QuikClot), firm direct pressure × 3 min\n\n### Additional Assessment\n- Log roll: check for exit wound, additional entry wounds\n- DCAP-BTLS: deformity, contusion, abrasions, penetrations, burns, tenderness, lacerations, swelling\n- Full vitals every 5 min en route\n\n### Transport\n**Priority 1 — Emergent. Load and go.** This patient needs the OR. Do not delay transport for IV access — get one large-bore, move. Trauma center pre-notification now.\n\n*Protocol reference: PHTLS 9th Ed; TCCC (Tactical Combat Casualty Care) MARCH; ACS TQIP Hemorrhage Control*"},
        ],
        "type": "clinical_scenario",
        "domain": "trauma",
        "scope": "paramedic",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "EMR scope: patient with suspected stroke, onset 45 min ago, left-sided facial droop, arm drift, slurred speech. What can I do?"},
            {"role": "assistant", "content": "## Stroke — EMR Scope Response\n\n### Confirm Stroke Suspected: Cincinnati Prehospital Stroke Scale\n- **Facial droop** ✓ — asymmetric\n- **Arm drift** ✓ — left arm drifts down\n- **Abnormal speech** ✓ — slurred\nAny 1 of 3 positive = 72% probability of stroke. All 3 positive = 85%.\n\n**Onset: 45 minutes ago** — this is within the tPA window (< 3–4.5 hours). Time is brain.\n\n---\n\n### EMR Scope Interventions\n\n1. **Position** — head of bed at 30° or semi-Fowler (do NOT lay flat — increases ICP risk)\n2. **Airway** — ensure patent; suction if secretions; no NPA/OPA unless unconscious\n3. **O2** — supplemental O2 only if SpO2 < 94%; do NOT hyperoxgenate a stroke patient\n4. **BGL** — check blood glucose: hypoglycemia mimics stroke\n   - If BGL < 60: this may not be stroke — EMR may assist with oral glucose if patient conscious and can swallow per agency protocol\n5. **Do NOT give anything by mouth** — dysphagia is common; aspiration risk\n6. **Note exact time of symptom onset** — critical for tPA eligibility; document precisely\n7. **Keep patient calm and warm**\n8. **No aspirin** — contraindicated until hemorrhagic stroke ruled out by CT\n\n### Activate the System — Your Most Important Action\n- Call for ALS intercept immediately\n- Pre-notify hospital — activate Stroke Alert / Code Stroke\n- Time saved = neurons saved\n\n### Do NOT\n- Give aspirin (hemorrhagic stroke risk)\n- Allow patient to eat or drink\n- Lower blood pressure in field (controlled hypertension is protective in acute stroke)\n- Delay transport for additional assessment\n\n### Transport\n**Priority 1 — Emergent.** Transport to nearest stroke center (Comprehensive Stroke Center preferred). Pre-notify with Cincinnati Stroke Scale findings and exact onset time.\n\nTarget: **Door-to-CT < 25 min, door-to-needle < 60 min** if tPA candidate.\n\n*Protocol reference: AHA/ASA Stroke Guidelines 2019; Cincinnati Prehospital Stroke Scale*"},
        ],
        "type": "clinical_scenario",
        "domain": "neurology",
        "scope": "emr",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "What is the Broselow tape and how do I use it?"},
            {"role": "assistant", "content": "## Broselow Pediatric Emergency Tape\n\n### What It Is\nThe Broselow-Luten Tape is a length-based pediatric resuscitation tool. It estimates a child's **weight** from **length (height)**, then provides color-coded dosing for drugs, fluid, and equipment sizing.\n\nDeveloped because children's weights are often unknown in emergencies and weighing wastes critical time.\n\n### How to Use\n\n1. **Position the patient** — place child in a supine straight position\n2. **Align the tape** — place the red end at the top of the child's head (crown)\n3. **Read the color zone** — the color zone at the child's heel gives estimated weight and dosing\n4. **Use the dosing chart for that color** — each color zone lists:\n   - Estimated weight (kg)\n   - ET tube size (uncuffed/cuffed)\n   - Laryngoscope blade size\n   - Defibrillation dose (2 J/kg, 4 J/kg)\n   - Drug doses: epinephrine, atropine, adenosine, glucose, naloxone, etc.\n   - IV fluid bolus volume\n   - BP cuff, mask, and equipment sizing\n\n### Color Zones (Approximate Weight Ranges)\n| Color | Weight |\n|---|---|\n| Gray | 3–5 kg |\n| Pink | 6–7 kg |\n| Red | 8–9 kg |\n| Purple | 10–11 kg |\n| Yellow | 12–14 kg |\n| White | 15–18 kg |\n| Blue | 19–22 kg |\n| Orange | 24–29 kg |\n| Green | 30–36 kg |\n\nChildren over approximately 36 kg (> green zone): use adult dosing.\n\n### Key Points\n- Length is a better predictor of weight than visual estimation in children\n- Never guess pediatric weights — errors cause fatal dosing mistakes\n- The Broselow tape is a **guideline** — if you know the actual weight, use it\n- Pre-calculate and verify against your agency's approved formulary\n\n*Reference: Luten RC, Wears RL, Broselow J, et al. 1992; Broselow-Luten Pediatric Resuscitation Tape, current edition*"},
        ],
        "type": "protocol_reference",
        "domain": "peds_reference",
        "scope": "emt",
    },
    {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Patient: 67F, difficulty breathing, 2+ pitting edema bilateral lower extremities, JVD, pink frothy sputum, SpO2 86%, history of CHF, BP 168/92, HR 102."},
            {"role": "assistant", "content": "## Clinical Assessment: Acute Pulmonary Edema / Acute Decompensated CHF\n\n### Critical Findings\n- SpO2 86% — critical hypoxia\n- Pink frothy sputum — pulmonary edema (fluid in alveoli)\n- JVD + bilateral pitting edema — fluid overload / right heart failure\n- Hypertensive (168/92) — hypertensive pulmonary edema (common; preload/afterload excess)\n- Known CHF — acute decompensation\n\n### Immediate Interventions\n\n1. **Position** — sit upright (high Fowler / tripod) — gravity moves fluid away from lungs; do NOT lay flat\n2. **O2 — CPAP (preferred)**\n   - CPAP 5–10 cmH2O with 100% FiO2\n   - CPAP reduces preload, recruits alveoli, rapidly improves SpO2\n   - Target SpO2 ≥ 94%\n   ⚠ ALS INTERVENTION — CPAP initiation: Paramedic scope in most jurisdictions; some EMT protocols include it\n3. **BVM with PEEP valve** if CPAP unavailable and SpO2 not improving\n4. **Nitroglycerin 0.4 mg SL** — reduces preload and afterload\n   - Check BP before each dose: hold if SBP < 90\n   - Repeat q5 min × 3 if BP allows and SpO2 not improving\n   - NTG paste (1 inch) may also be applied\n   ⚠ ALS INTERVENTION — NTG in most jurisdictions: Paramedic/AEMT scope\n5. **Furosemide (Lasix)** — 40–80 mg IV (or double home dose if patient on chronic furosemide)\n   - Venodilation within minutes (before diuresis)\n   - Diuresis begins in 15–30 min\n   ⚠ ALS INTERVENTION — IV furosemide: Paramedic scope; CONTACT MEDICAL CONTROL for dose\n6. **IV access** — establish but DO NOT bolus fluids — patient is volume overloaded\n7. **12-lead ECG** — rule out concurrent ACS (MI can precipitate CHF decompensation)\n\n### What Not To Do\n- No IV fluid bolus (patient is already fluid overloaded)\n- No supine positioning\n- No rapid intubation without attempting CPAP first\n\n### Assess for Concurrent ACS\n- CHF decompensation can be triggered by STEMI\n- Obtain 12-lead early and transmit\n\n### Transport\n**Priority 1 — Emergent.** CPAP initiated if available; continue en route. Pre-notify ED of ADHF with hypoxia. Goal: avoid intubation with early CPAP and nitrates.\n\n*Protocol reference: AHA Heart Failure Guidelines 2022; NAEMSP CPAP Guideline*"},
        ],
        "type": "clinical_scenario",
        "domain": "cardiac",
        "scope": "paramedic",
    },
]


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "ems_scenarios.jsonl"
    with open(out_path, "w") as f:
        for ex in EXAMPLES:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    print(f"Wrote {len(EXAMPLES)} synthetic EMS scenarios to {out_path}")


if __name__ == "__main__":
    main()
