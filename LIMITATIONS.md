# BONES — Limitations, Scope, and Use Guidance

Read this before deploying BONES in any operational context.

---

## What BONES Does

Given a patient presentation or dispatch scenario, BONES provides EMS protocol guidance, drug references, triage support, and clinical decision support across the full scope of practice chain — from EMR through Paramedic.

## What BONES Does Not Do

- **BONES is not a physician, and its outputs do not constitute medical advice.** All clinical decisions must be made by a licensed provider operating under medical direction.
- **BONES does not replace your regional protocols.** Local EMS protocols, offline medical direction, and base hospital contact requirements always take precedence over BONES output.
- **BONES cannot assess the patient.** It works from what you tell it. Incomplete or inaccurate information produces inaccurate guidance.
- **BONES does not know your scope.** It will answer questions across the full EMR–Paramedic spectrum. You are responsible for operating within your certified scope of practice.
- **BONES is not FDA approved as a medical device.** It has not undergone clinical validation and should not be the sole basis for any patient care decision.
- **BONES has a training data cutoff.** AHA guideline updates, new NAEMSP position statements, and protocol changes after the training data cutoff may not be reflected.
- **Drug dosing must always be verified.** Pediatric weight-based dosing (Broselow), maximum doses, and contraindications must be verified against your formulary before administration.

---

## Scope of Practice

BONES is designed to assist certified EMS personnel operating under medical direction in:

- Protocol lookup and reference during training and non-emergency preparation
- Differential considerations for patient presentations
- Drug reference and dosing ranges (must be verified against formulary before use)
- Triage category guidance (START/SALT)
- PCR documentation assistance
- Training and scenario-based learning

**BONES is a decision-support tool. It does not replace offline medical direction, base hospital contact, or the judgment of the treating provider.**

---

## Medical Direction Requirement

Deployment of BONES in any operational EMS context requires review and approval by the agency's medical director. The medical director should:

- Review sample outputs against current regional protocols
- Determine appropriate use cases and restrictions for their system
- Establish documentation requirements when BONES is consulted
- Conduct periodic audits of outputs against current AHA/NAEMSP guidelines

---

## Known Limitations

| Area | Limitation |
|------|-----------|
| Protocol currency | AHA guidelines version: 2020 (updates may not be reflected) |
| Regional protocols | Local offline medical direction and base hospital protocols not included |
| Scope enforcement | BONES does not restrict answers by certification level — provider must self-limit |
| Drug dosing | Ranges are reference only; always verify against formulary and medical direction |
| Pediatric dosing | Broselow weight-based dosing included but must be verified before administration |
| Clinical validation | Not clinically validated; no FDA clearance |
| Training size | Fine-tuned on a small dataset; rare presentations and edge cases may degrade performance |

---

## Before You Deploy

- Obtain written approval from your medical director
- Define permitted use cases in a written policy (e.g., training only vs. operational reference)
- Train all users that BONES output must be cross-referenced with local protocols
- Establish a feedback mechanism for providers to report incorrect or dangerous outputs
- Audit BONES outputs against current AHA guidelines annually or when guidelines are updated

---

## Version and Training Data

| Field | Value |
|-------|-------|
| Base model | meta-llama/Llama-3.3-70B-Instruct |
| Fine-tune method | QLoRA (4-bit) |
| Adapter | [Ronin48LLC/bones-lora-adapter](https://huggingface.co/Ronin48LLC/bones-lora-adapter) |
| Training date | May 2026 |
| AHA guidelines | 2020 |
| NAEMSP guidelines | Current as of training data cutoff |

---

## Reporting Errors

If BONES produces an incorrect, dangerous, or potentially harmful clinical output:

- **GitHub:** [CryptoJones/BONES/issues](https://github.com/CryptoJones/BONES/issues)
- **Codeberg:** [Ronin48/BONES/issues](https://codeberg.org/Ronin48/BONES/issues)

For clinically dangerous outputs, also notify your medical director immediately.
