# BONES Changelog

## Versioning Scheme

| Component | When to bump | Example |
|---|---|---|
| **Major** (X.0.0) | Base model swap or complete domain overhaul | v1.0.0 |
| **Minor** (0.X.0) | New protocol sets, new scope of practice coverage | v0.2.0 |
| **Patch** (0.0.X) | Parameter tuning, bug fixes, prompt adjustments | v0.1.1 |

**Tags on Ollama:** `Ronin48/bones:latest` always points to the most recent stable version.
Named tags (`Ronin48/bones:v0.1.0`) are permanent and never overwritten.

**Pre-fine-tune versions (v0.x.x):** Base Llama 3.1 8B + BONES system prompt.
No fine-tuned weights yet. These are prompt-engineered baselines.

**Fine-tuned versions (v1.x.x+):** QLoRA fine-tuned on EMS protocol and clinical data.

---

## [v0.1.0] — In Progress (2026-05-12)

**Base model:** `meta-llama/Llama-3.1-8B-Instruct` (no fine-tuning)
**Type:** Prompt-engineered baseline
**Status:** 🚧 Scaffolding — not yet published

### Added
- Initial BONES system prompt with EMS clinical decision support framework
- Protocol lookup, drug reference, triage, trauma, OB/Peds, toxicology coverage
- Scope of practice guardrails (EMR / EMT / AEMT / Paramedic levels)
- Medical direction disclaimer — flags ALS interventions requiring medical control
- QLoRA training pipeline (prepare_dataset, train_qlora, merge_adapter)
- Synthetic scenario generator (dispatch-to-treatment examples)
- fetch_medical_guidelines.py for PubMed / OpenMedSpel data collection

---

## [v1.0.0] — Planned

**Base model:** `meta-llama/Llama-3.3-70B-Instruct` (QLoRA fine-tuned)
**Type:** Fine-tuned on EMS protocols and clinical scenarios
**Status:** 📋 Planned — pending training data collection

### Planned
- QLoRA fine-tuning on EMS protocol corpus
- ACLS/PALS/BLS algorithm training data
- Pediatric dosing (Broselow) integration
- AHA 2020/2024 guideline updates
