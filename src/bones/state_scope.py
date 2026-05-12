"""
State-specific EMS scope of practice overrides.

Structure per state, per provider level:
  - additional: skills/meds authorized beyond NREMT baseline
  - restricted: NREMT baseline skills NOT authorized in this state
  - notes: important state-specific protocol notes
  - fema_required: FEMA/NIMS courses required for EMS certification/recertification
  - source: official state regulatory source URL
  - verified_date: when this data was last verified against official source

IMPORTANT: State scopes change. Always cite the source and verify against
the official state EMS regulatory office before clinical use.

Data marked 'VERIFY' has not been confirmed against current official state sources.
"""

from dataclasses import dataclass, field

SCOPE_LEVELS = ["EMR", "EMT", "AEMT", "Paramedic"]


@dataclass
class LevelScope:
    """Scope additions/restrictions for one provider level in one state."""
    additional: list[str] = field(default_factory=list)   # beyond NREMT baseline
    restricted: list[str] = field(default_factory=list)   # NREMT skill NOT allowed here
    notes: list[str] = field(default_factory=list)        # important state-specific notes


@dataclass
class StateScope:
    state: str
    state_code: str
    regulatory_body: str
    source_url: str
    verified_date: str        # ISO date of last verification, or "UNVERIFIED"
    fema_required: list[str]  # FEMA IS course numbers required for EMS in this state
    nims_required: list[str]  # NIMS ICS course numbers (may overlap fema_required)
    levels: dict[str, LevelScope] = field(default_factory=dict)
    general_notes: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# State scope data
# Format: STATE_SCOPES["XX"] = StateScope(...)
# ---------------------------------------------------------------------------

STATE_SCOPES: dict[str, StateScope] = {}


# --- Nebraska ---------------------------------------------------------------
STATE_SCOPES["NE"] = StateScope(
    state="Nebraska",
    state_code="NE",
    regulatory_body="Nebraska Department of Health and Human Services — EMS",
    source_url="https://dhhs.ne.gov/Pages/Emergency-Medical-Services.aspx",
    verified_date="2026-05-12",
    fema_required=["IS-100.c", "IS-200.c", "IS-700.b"],
    nims_required=["IS-100.c", "IS-200.c", "IS-700.b"],
    general_notes=[
        "Licenses expire every 2 years on March 31 of odd years.",
        "Nebraska follows NREMT NCCP model — only National (NCCR) portion required for state recert.",
        "Recertification hours: EMT 40h, AEMT 50h, Paramedic 60h per 2-year cycle.",
        "Nebraska accepts NREMT national certification; providers must also hold state license.",
    ],
    levels={
        "EMR": LevelScope(
            notes=["VERIFY — Contact NE DHHS EMS for current EMR-specific state additions."],
        ),
        "EMT": LevelScope(
            notes=[
                "Nebraska EMT scope generally follows NREMT 2019 national standards.",
                "CPAP: authorized per protocol in many NE agencies — confirm with medical director.",
                "12-lead acquisition authorized for EMT with training per medical director protocol.",
                "VERIFY specific medication additions with NE DHHS EMS office.",
            ],
        ),
        "AEMT": LevelScope(
            notes=[
                "Nebraska AEMT scope follows national NHTSA model.",
                "VERIFY current NE AEMT medication list with DHHS EMS.",
            ],
        ),
        "Paramedic": LevelScope(
            additional=[
                "RSI authorized per medical director protocol",
                "Ketamine IV/IM authorized for analgesia and RSI induction",
            ],
            notes=[
                "Nebraska paramedic scope generally tracks NREMT national standards.",
                "RSI requires specific training and medical director authorization.",
                "VERIFY current NE Paramedic formulary with NE DHHS EMS.",
            ],
        ),
    },
)

# --- Georgia ----------------------------------------------------------------
STATE_SCOPES["GA"] = StateScope(
    state="Georgia",
    state_code="GA",
    regulatory_body="Georgia Department of Public Health — EMS",
    source_url="https://dph.georgia.gov/emergency-medical-services",
    verified_date="UNVERIFIED",
    fema_required=["IS-100.c", "IS-700.b"],
    nims_required=["IS-100.c", "IS-700.b"],
    general_notes=[
        "Georgia uses NREMT certification as the standard.",
        "VERIFY all scope details with Georgia DPH EMS before clinical use.",
    ],
    levels={
        "EMR": LevelScope(notes=["VERIFY with GA DPH EMS."]),
        "EMT": LevelScope(
            notes=[
                "Georgia EMT scope follows NREMT 2019 model.",
                "CPAP authorized per protocol.",
                "VERIFY current GA EMT formulary with DPH EMS.",
            ],
        ),
        "AEMT": LevelScope(notes=["VERIFY with GA DPH EMS."]),
        "Paramedic": LevelScope(
            additional=[
                "RSI authorized per medical director protocol",
                "Ketamine authorized (analgesic and RSI induction)",
                "12-lead interpretation and STEMI alert activation",
                "TXA IV per protocol for hemorrhagic shock",
            ],
            notes=["VERIFY current GA Paramedic formulary with DPH EMS."],
        ),
    },
)

# --- Texas ------------------------------------------------------------------
STATE_SCOPES["TX"] = StateScope(
    state="Texas",
    state_code="TX",
    regulatory_body="Texas Department of State Health Services — EMS",
    source_url="https://www.dshs.texas.gov/emergency-medical-services",
    verified_date="UNVERIFIED",
    fema_required=["IS-100.c", "IS-200.c", "IS-700.b"],
    nims_required=["IS-100.c", "IS-200.c", "IS-700.b"],
    general_notes=[
        "Texas has its own EMS certification levels: First Responder, EMT, AEMT, Paramedic.",
        "Texas First Responder is roughly equivalent to NREMT EMR.",
        "Texas uses state-based certification; NREMT is accepted but state license is required.",
        "VERIFY all details with TX DSHS EMS.",
    ],
    levels={
        "EMR": LevelScope(
            notes=["Texas calls this level 'First Responder' — scope aligns with NREMT EMR. VERIFY with TX DSHS."],
        ),
        "EMT": LevelScope(
            notes=["Texas EMT scope aligns with NREMT national model. VERIFY current TX formulary with DSHS."],
        ),
        "AEMT": LevelScope(notes=["VERIFY with TX DSHS EMS."]),
        "Paramedic": LevelScope(
            additional=[
                "RSI authorized per medical director protocol",
                "Ketamine IV/IM for analgesia and induction",
                "Whole blood (pRBC) authorized at select TEMS/trauma systems",
                "TXA IV for hemorrhagic trauma",
            ],
            notes=["VERIFY current TX Paramedic formulary and protocol with DSHS and local medical director."],
        ),
    },
)

# --- California -------------------------------------------------------------
STATE_SCOPES["CA"] = StateScope(
    state="California",
    state_code="CA",
    regulatory_body="California Emergency Medical Services Authority (EMSA)",
    source_url="https://emsa.ca.gov/ems-personnel/",
    verified_date="UNVERIFIED",
    fema_required=["IS-100.c", "IS-200.c", "IS-700.b", "IS-800.d"],
    nims_required=["IS-100.c", "IS-200.c", "IS-700.b", "IS-800.d"],
    general_notes=[
        "California uses county-based EMS systems — county EMS agencies set protocols within state guidelines.",
        "California has additional level: EMT-I (basic) and Paramedic. No AEMT level in CA.",
        "Local EMS Agency (LEMSA) protocols may significantly expand or restrict state baseline.",
        "VERIFY with both CA EMSA and your county LEMSA.",
    ],
    levels={
        "EMR": LevelScope(notes=["California First Responder. VERIFY with CA EMSA and county LEMSA."]),
        "EMT": LevelScope(
            notes=[
                "California EMT (EMT-I) scope is set by CA EMSA but implemented by county LEMSA.",
                "CPAP: authorized in many California counties per LEMSA protocol.",
                "Some counties authorize EMTs to perform 12-lead acquisition.",
                "VERIFY with your specific county LEMSA — significant variation exists.",
            ],
        ),
        "AEMT": LevelScope(
            notes=["California does not have an AEMT certification level as of last verification. VERIFY with CA EMSA."],
        ),
        "Paramedic": LevelScope(
            additional=[
                "RSI authorized per LEMSA protocol",
                "Ketamine IV/IM per LEMSA protocol",
                "TXA per LEMSA protocol",
                "Whole blood per select trauma systems",
                "Ultrasound (POCUS) per LEMSA protocol — some counties",
                "12-lead STEMI alert and hospital bypass",
            ],
            notes=[
                "Paramedic scope varies significantly by county LEMSA in California.",
                "VERIFY with your specific county LEMSA medical director.",
            ],
        ),
    },
)

# --- Florida ----------------------------------------------------------------
STATE_SCOPES["FL"] = StateScope(
    state="Florida",
    state_code="FL",
    regulatory_body="Florida Department of Health — Bureau of EMS",
    source_url="https://www.floridahealth.gov/licensing-and-regulation/emergency-medical-services/",
    verified_date="UNVERIFIED",
    fema_required=["IS-100.c", "IS-700.b"],
    nims_required=["IS-100.c", "IS-700.b"],
    general_notes=[
        "Florida uses NREMT certification and state licensure.",
        "Florida has EMT and Paramedic levels; limited AEMT presence.",
        "VERIFY with FL DOH Bureau of EMS.",
    ],
    levels={
        "EMR": LevelScope(notes=["VERIFY with FL DOH Bureau of EMS."]),
        "EMT": LevelScope(
            notes=["Florida EMT scope aligns with NREMT national model. VERIFY current FL formulary with DOH."],
        ),
        "AEMT": LevelScope(notes=["Limited AEMT presence in Florida. VERIFY with FL DOH."]),
        "Paramedic": LevelScope(
            additional=[
                "RSI per medical director protocol",
                "Ketamine IV/IM per protocol",
                "TXA per protocol",
                "12-lead interpretation and STEMI alert",
            ],
            notes=["VERIFY current FL Paramedic formulary with DOH Bureau of EMS."],
        ),
    },
)

# --- New York ---------------------------------------------------------------
STATE_SCOPES["NY"] = StateScope(
    state="New York",
    state_code="NY",
    regulatory_body="New York State Department of Health — Bureau of EMS",
    source_url="https://www.health.ny.gov/professionals/ems/",
    verified_date="UNVERIFIED",
    fema_required=["IS-100.c", "IS-200.c", "IS-700.b"],
    nims_required=["IS-100.c", "IS-200.c", "IS-700.b"],
    general_notes=[
        "New York has unique certification structure: CFR, EMT, AEMT, Paramedic.",
        "CFR (Certified First Responder) is NY's EMR-equivalent.",
        "NYC operates under FDNY EMS protocols which may differ from state protocols.",
        "Regional Medical Advisory Committees (REMAC) set regional protocols within state guidelines.",
        "VERIFY with NY DOH BEMS and your regional REMAC.",
    ],
    levels={
        "EMR": LevelScope(
            notes=["NY calls this level 'CFR' (Certified First Responder). VERIFY with NY DOH BEMS."],
        ),
        "EMT": LevelScope(
            notes=[
                "NY EMT scope generally follows NREMT model with regional REMAC variations.",
                "CPAP: authorized in most NY regions per protocol.",
                "VERIFY with your regional REMAC for local protocol additions.",
            ],
        ),
        "AEMT": LevelScope(notes=["VERIFY with NY DOH BEMS and your REMAC."]),
        "Paramedic": LevelScope(
            additional=[
                "RSI per REMAC protocol",
                "Ketamine per REMAC protocol",
                "TXA per REMAC protocol",
                "12-lead interpretation and STEMI alert",
                "CPAP/BiPAP",
                "Video laryngoscopy",
            ],
            notes=[
                "NYC/FDNY paramedic scope may differ from state/REMAC protocols.",
                "VERIFY with your specific REMAC and medical director.",
            ],
        ),
    },
)

# --- Placeholder for all 50 states + territories ---------------------------
# States to be populated as data is verified:
_PLACEHOLDER_STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana",
    "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
    "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "UT": "Utah", "VT": "Vermont",
    "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin",
    "WY": "Wyoming",
    # Territories
    "PR": "Puerto Rico", "GU": "Guam", "VI": "U.S. Virgin Islands",
    "AS": "American Samoa", "MP": "Northern Mariana Islands",
    "DC": "District of Columbia",
}

for _code, _name in _PLACEHOLDER_STATES.items():
    if _code not in STATE_SCOPES:
        STATE_SCOPES[_code] = StateScope(
            state=_name,
            state_code=_code,
            regulatory_body=f"{_name} State EMS Regulatory Office",
            source_url="",
            verified_date="UNVERIFIED",
            fema_required=["IS-100.c", "IS-700.b"],
            nims_required=["IS-100.c", "IS-700.b"],
            general_notes=[f"⚠ UNVERIFIED — No state-specific data loaded for {_name}. Default to NREMT national baseline. Verify with {_name} state EMS regulatory office."],
            levels={
                "EMR":      LevelScope(notes=[f"UNVERIFIED — verify with {_name} EMS office."]),
                "EMT":      LevelScope(notes=[f"UNVERIFIED — verify with {_name} EMS office."]),
                "AEMT":     LevelScope(notes=[f"UNVERIFIED — verify with {_name} EMS office."]),
                "Paramedic": LevelScope(notes=[f"UNVERIFIED — verify with {_name} EMS office."]),
            },
        )


# ---------------------------------------------------------------------------
# Query functions
# ---------------------------------------------------------------------------

def get_state_scope(state_code: str) -> StateScope | None:
    return STATE_SCOPES.get(state_code.upper())


def list_states() -> list[tuple[str, str]]:
    return sorted((code, s.state) for code, s in STATE_SCOPES.items())


def format_state_overrides(state_code: str, level: str) -> str:
    """Return a prompt-ready block for one state + one provider level."""
    ss = STATE_SCOPES.get(state_code.upper())
    if not ss:
        return f"⚠ No data for state code '{state_code}'. Default to NREMT national baseline."

    lv = ss.levels.get(level, LevelScope())
    lines = [
        f"STATE SCOPE: {ss.state} ({ss.state_code}) — {level}",
        f"Regulatory body: {ss.regulatory_body}",
        f"Source: {ss.source_url or 'See state EMS office'}",
        f"Data status: {ss.verified_date}",
    ]

    if lv.additional:
        lines += ["", f"State additions beyond NREMT baseline ({level}):"]
        lines += [f"  + {item}" for item in lv.additional]

    if lv.restricted:
        lines += ["", f"NREMT skills NOT authorized in {ss.state} at {level} level:"]
        lines += [f"  ✗ {item}" for item in lv.restricted]

    if lv.notes:
        lines += ["", "State-specific notes:"]
        lines += [f"  • {note}" for note in lv.notes]

    if ss.general_notes:
        lines += ["", "General state EMS notes:"]
        lines += [f"  • {note}" for note in ss.general_notes]

    if ss.fema_required:
        lines += ["", f"FEMA/NIMS courses required in {ss.state}: {', '.join(ss.fema_required)}"]

    lines += [
        "",
        "⚠ ALWAYS verify current scope with your state EMS office and medical director.",
        "  State protocols change — this data reflects the verified_date above.",
    ]
    return "\n".join(lines)


def format_full_state_summary(state_code: str) -> str:
    """Return a summary of all four levels for a given state."""
    ss = STATE_SCOPES.get(state_code.upper())
    if not ss:
        return f"No data for '{state_code}'."

    lines = [
        f"=== {ss.state} EMS Scope of Practice ===",
        f"Regulatory body: {ss.regulatory_body}",
        f"Source: {ss.source_url or 'See state EMS office'}",
        f"Data status: {ss.verified_date}",
        f"FEMA required: {', '.join(ss.fema_required) or 'None specified'}",
        "",
    ]
    for level in SCOPE_LEVELS:
        lv = ss.levels.get(level, LevelScope())
        lines.append(f"--- {level} ---")
        if lv.additional:
            lines.append("  State additions: " + "; ".join(lv.additional))
        if lv.restricted:
            lines.append("  Restricted vs NREMT: " + "; ".join(lv.restricted))
        if lv.notes:
            for note in lv.notes:
                lines.append(f"  Note: {note}")
        lines.append("")

    return "\n".join(lines)
