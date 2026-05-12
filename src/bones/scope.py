"""
EMS Scope of Practice — National NREMT baseline definitions.

Source: NHTSA National EMS Scope of Practice Model (2019), public domain.
        NREMT Practice Analysis (2021), public domain.

These are NATIONAL STANDARDS only. Each state implements its own scope
of practice, which may differ significantly. Always consult state_scope.py
for state-specific overrides before advising a provider.
"""

from dataclasses import dataclass, field

SCOPE_LEVELS = ["EMR", "EMT", "AEMT", "Paramedic"]


@dataclass
class ScopeLevel:
    code: str
    name: str
    certification: str
    airway: list[str] = field(default_factory=list)
    breathing: list[str] = field(default_factory=list)
    circulation: list[str] = field(default_factory=list)
    medications: list[str] = field(default_factory=list)
    monitoring: list[str] = field(default_factory=list)
    trauma: list[str] = field(default_factory=list)
    obstetrics: list[str] = field(default_factory=list)
    medical_direction_required: list[str] = field(default_factory=list)


EMR = ScopeLevel(
    code="EMR",
    name="Emergency Medical Responder",
    certification="NREMT-EMR",
    airway=[
        "Manual airway maneuvers (head-tilt chin-lift, jaw-thrust)",
        "Oropharyngeal airway (OPA)",
        "Nasopharyngeal airway (NPA)",
        "Suctioning (bulb and manual)",
        "BVM ventilation with supplemental O2",
        "Supplemental oxygen (NRB, cannula)",
    ],
    breathing=[
        "Supplemental oxygen",
        "BVM-assisted ventilation",
        "Pulse oximetry (SpO2)",
    ],
    circulation=[
        "CPR — adult, child, infant",
        "AED operation",
        "Hemorrhage control: direct pressure, wound packing, tourniquet",
        "Assist patient with own epinephrine auto-injector",
        "Aspirin (per standing orders)",
    ],
    medications=[
        "Epinephrine auto-injector (patient's own)",
        "Aspirin",
        "Oral glucose (if patient can swallow)",
        "Oxygen",
    ],
    monitoring=[
        "Manual blood pressure",
        "Pulse rate and quality",
        "Respiratory rate",
        "Skin signs",
        "SpO2",
        "Blood glucose (per protocol)",
        "Pupils",
        "GCS",
    ],
    trauma=[
        "Tourniquet application",
        "Wound packing",
        "Rigid and soft splinting",
        "Manual spinal stabilization",
        "Cervical collar application",
        "Burn assessment and covering",
    ],
    obstetrics=[
        "Normal delivery assistance",
        "Newborn airway management (dry, stimulate)",
        "Cord cutting",
    ],
    medical_direction_required=[
        "Epinephrine auto-injector if patient cannot self-administer",
        "Oral glucose",
        "Aspirin (most jurisdictions)",
    ],
)

EMT = ScopeLevel(
    code="EMT",
    name="Emergency Medical Technician",
    certification="NREMT-EMT",
    airway=[
        "All EMR airway skills",
        "OPA and NPA",
        "Supraglottic airway devices (King LT, i-gel) — per jurisdiction",
        "CPAP — per jurisdiction",
        "Rigid and soft suction catheters",
        "Tracheostomy suctioning (per protocol)",
        "PEEP valve with BVM",
        "Colorimetric end-tidal CO2 detection",
    ],
    breathing=[
        "All EMR breathing skills",
        "CPAP initiation — per jurisdiction",
        "Nebulized albuterol (assist with patient's inhaler or per protocol)",
        "Pulse oximetry",
        "Colorimetric capnography",
    ],
    circulation=[
        "All EMR circulation skills",
        "Assist patient with prescribed nitroglycerin SL",
        "EMS-issued epinephrine IM (auto-injector format per protocol)",
        "External hemorrhage control",
    ],
    medications=[
        "All EMR medications",
        "Albuterol MDI (patient's own or per protocol)",
        "Nitroglycerin SL (patient's own, per protocol)",
        "Epinephrine 1:1000 via auto-injector (per protocol)",
        "Oral glucose",
        "Aspirin",
        "Oxygen",
        "Activated charcoal (per protocol)",
        "Ondansetron ODT — per protocol, many jurisdictions",
    ],
    monitoring=[
        "All EMR monitoring",
        "12-lead ECG acquisition and transmission (no interpretation required)",
        "Blood glucose monitoring",
        "Colorimetric capnography",
    ],
    trauma=[
        "All EMR trauma skills",
        "Traction splint (Hare, Sager, Kendrick)",
        "Long backboard / scoop stretcher",
        "Kendrick Extrication Device (KED)",
        "Vented chest seal application",
        "Wound packing with hemostatic gauze",
    ],
    obstetrics=[
        "All EMR OB skills",
        "Breech delivery assistance",
        "Prolapsed cord management",
        "Newborn resuscitation (dry, warm, stimulate, BVM PPV)",
        "Uterine massage for postpartum hemorrhage",
    ],
    medical_direction_required=[
        "Nitroglycerin (verify SBP > 90, no PDE-5 inhibitor use)",
        "Epinephrine IM for anaphylaxis",
        "CPAP initiation (some jurisdictions)",
        "12-lead ECG acquisition (most jurisdictions)",
    ],
)

AEMT = ScopeLevel(
    code="AEMT",
    name="Advanced Emergency Medical Technician",
    certification="NREMT-AEMT",
    airway=[
        "All EMT airway skills",
        "Supraglottic airways (King LT, i-gel, Combitube) — full insertion/management",
        "CPAP and BiPAP initiation and management",
        "Waveform capnography",
        "Nasogastric tube insertion",
    ],
    breathing=[
        "All EMT breathing skills",
        "Waveform capnography (EtCO2)",
        "Nebulized albuterol and ipratropium",
        "CPAP/BiPAP",
    ],
    circulation=[
        "All EMT circulation skills",
        "Peripheral IV access",
        "Intraosseous (IO) access — tibial and sternal",
        "IV fluid administration (NS, LR)",
        "Cardiac monitoring",
        "12-lead ECG acquisition",
    ],
    medications=[
        "All EMT medications",
        "Epinephrine 1:1000 IM",
        "Epinephrine 1:10000 IV (cardiac arrest)",
        "50% Dextrose (D50) IV",
        "Glucagon IM",
        "Normal saline IV bolus",
        "Lactated Ringer's IV bolus",
        "Naloxone IN/IM/IV",
        "Albuterol nebulized",
        "Ipratropium nebulized",
        "Nitrous oxide (per jurisdiction)",
        "Ondansetron IV/IM/ODT",
        "Nitroglycerin IV/SL (per protocol)",
    ],
    monitoring=[
        "All EMT monitoring",
        "Waveform capnography",
        "Cardiac rhythm monitoring",
        "12-lead ECG acquisition",
    ],
    trauma=[
        "All EMT trauma skills",
        "IV/IO fluid resuscitation",
        "Permissive hypotension strategy",
    ],
    obstetrics=[
        "All EMT OB skills",
        "IV access in obstetric emergencies",
        "IV fluids for eclampsia (per protocol)",
    ],
    medical_direction_required=[
        "IO access",
        "IV epinephrine",
        "D50 IV",
        "All IV medication administration",
    ],
)

PARAMEDIC = ScopeLevel(
    code="Paramedic",
    name="Paramedic",
    certification="NREMT-Paramedic",
    airway=[
        "All AEMT airway skills",
        "Endotracheal intubation (ETI) — direct laryngoscopy and video laryngoscopy",
        "Rapid sequence intubation (RSI)",
        "Surgical airway — needle cricothyrotomy, surgical cricothyrotomy",
        "Pediatric intubation",
        "Digital/tactile intubation",
        "Full waveform capnography interpretation",
    ],
    breathing=[
        "All AEMT breathing skills",
        "Full ventilator management",
        "Needle thoracostomy (tension pneumothorax)",
        "Chest tube insertion (per jurisdiction)",
    ],
    circulation=[
        "All AEMT circulation skills",
        "Cardioversion (synchronized)",
        "Defibrillation",
        "Transcutaneous cardiac pacing (TCP)",
        "12-lead ECG interpretation — STEMI, arrhythmia recognition",
        "IO access — all sites",
        "Central venous access (per jurisdiction)",
        "Whole blood administration (per jurisdiction/TEMS)",
    ],
    medications=[
        "All AEMT medications",
        "Full prehospital formulary",
        "Amiodarone IV",
        "Adenosine IV rapid push",
        "Lidocaine IV",
        "Procainamide IV",
        "Atropine IV",
        "Dopamine IV drip",
        "Norepinephrine IV drip",
        "Vasopressin IV",
        "Epinephrine IV drip",
        "Furosemide IV",
        "Morphine IV/IM",
        "Fentanyl IV/IN/IM",
        "Ketamine IV/IM",
        "Etomidate IV",
        "Succinylcholine IV/IM",
        "Rocuronium IV",
        "Vecuronium IV",
        "Midazolam IV/IM/IN",
        "Diazepam IV/PR",
        "Lorazepam IV/IM",
        "Tranexamic acid (TXA) IV",
        "Sodium bicarbonate IV",
        "Calcium chloride IV",
        "Calcium gluconate IV",
        "Magnesium sulfate IV",
        "Labetalol IV",
        "Metoprolol IV",
        "Diltiazem IV",
        "Oxytocin IV",
        "Terbutaline SQ",
        "Dexamethasone IV",
        "Methylprednisolone IV",
        "Haloperidol IV/IM",
        "Thiamine IV",
        "Ondansetron IV",
        "Droperidol IM (per protocol)",
    ],
    monitoring=[
        "All AEMT monitoring",
        "Full 12-lead ECG interpretation",
        "STEMI, LBBB, BBB, WPW recognition",
        "Full arrhythmia identification and treatment",
        "Invasive blood pressure (per jurisdiction)",
    ],
    trauma=[
        "All AEMT trauma skills",
        "Needle thoracostomy bilateral",
        "Chest tube (per jurisdiction)",
        "RSI for airway protection in trauma",
        "Blood products (per TEMS/jurisdiction)",
        "Fasciotomy (per jurisdiction/TEMS)",
    ],
    obstetrics=[
        "All AEMT OB skills",
        "Magnesium sulfate IV for eclampsia",
        "RSI for eclamptic patient",
    ],
    medical_direction_required=[
        "RSI / neuromuscular blockade",
        "Surgical airway",
        "Cardioversion",
        "Transcutaneous pacing",
        "Blood products",
        "Field termination of resuscitation",
        "Withholding resuscitation (DNR verification)",
    ],
)

SCOPE_MAP: dict[str, ScopeLevel] = {
    "EMR": EMR,
    "EMT": EMT,
    "AEMT": AEMT,
    "Paramedic": PARAMEDIC,
}


def get_scope(level: str) -> ScopeLevel | None:
    return SCOPE_MAP.get(level)


def scope_summary(level: str, state: str | None = None) -> str:
    """
    Return a text block describing scope for prompt injection.
    If state is provided, includes state-specific overrides.
    """
    from state_scope import get_state_scope, format_state_overrides

    s = SCOPE_MAP.get(level)
    if not s:
        return f"Unknown scope level: {level}"

    lines = [
        f"NREMT BASELINE — {s.code}: {s.name} ({s.certification})",
        "Source: NHTSA National EMS Scope of Practice Model 2019",
        "",
        "Medications (NREMT baseline): " + "; ".join(s.medications),
        "Airway (NREMT baseline): " + "; ".join(s.airway),
        "Monitoring (NREMT baseline): " + "; ".join(s.monitoring),
        "Trauma (NREMT baseline): " + "; ".join(s.trauma),
        "Requires medical control: " + "; ".join(s.medical_direction_required),
    ]

    if state:
        state_block = format_state_overrides(state, level)
        if state_block:
            lines += ["", state_block]
        else:
            lines += [
                "",
                f"⚠ STATE DATA: No specific {state} overrides loaded.",
                f"  Default to NREMT baseline and advise provider to verify with {state} DHHS/EMS office.",
            ]

    lines += [
        "",
        f"Flag anything beyond {level} scope (national or state) as:",
        f"  '⚠ BEYOND {level} SCOPE — requires higher certification or online medical control.'",
        "",
        "Always distinguish: 'NREMT national standard' vs '[State] state protocol' in your response.",
    ]
    return "\n".join(lines)


def _next_level(code: str) -> str:
    idx = SCOPE_LEVELS.index(code) if code in SCOPE_LEVELS else -1
    return SCOPE_LEVELS[idx + 1] if idx < len(SCOPE_LEVELS) - 1 else "higher level provider"
