# BONES — Biomedical On-scene Navigator for Emergency Services

> *"He's dead, Jim."* — Dr. Leonard H. McCoy, USS Enterprise

**BONES** is an AI assistant fine-tuned on emergency medical services (EMS) protocols, pharmacology references, triage frameworks, and clinical decision support knowledge — built to assist **EMRs, EMTs, and Paramedics** in the field and in training.

Part of the **Ronin 48** suite alongside SELMA, ABBY, ATTICUS, and BRUNO.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?logo=apache)](https://opensource.org/licenses/Apache-2.0)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Ronin48LLC%2Fbones--lora--adapter-FFD21E?logo=huggingface&logoColor=000)](https://huggingface.co/Ronin48LLC/bones-lora-adapter)
[![Codeberg](https://img.shields.io/badge/Codeberg-Ronin48%2FBONES-2185D0?logo=codeberg&logoColor=white)](https://codeberg.org/Ronin48/BONES)
[![GitHub](https://img.shields.io/badge/GitHub-CryptoJones%2FBONES-181717?logo=github&logoColor=white)](https://github.com/CryptoJones/BONES)

---

## Supporters

BONES is community-funded. Every contribution keeps this project free, open, and in the hands
of the providers who need it most.

| Donor | Amount | Note |
|---|---|---|
| Ronin 48, LLC | N/A | Founding donor & primary sponsor of research time and equipment |

*Want to support BONES? Reach out to the maintainers.*

---

## Overview

| Attribute | Value |
|---|---|
| **Full Name** | Biomedical On-scene Navigator for Emergency Services |
| **Named After** | Dr. Leonard "Bones" McCoy, *Star Trek* |
| **Role** | EMS clinical decision support |
| **Users** | EMRs, EMTs, Paramedics |
| **Base Model** | `meta-llama/Llama-3.3-70B-Instruct` (fine-tuned) |
| **Baseline** | `meta-llama/Llama-3.3-70B-Instruct` (prompt-only) |
| **Suite** | Ronin 48 — Model #4 |

---

## Capabilities

- **Protocol lookup** — AHA ACLS/PALS/BLS algorithms, NWC protocols, NREMT scope of practice
- **Drug reference** — EMS formulary, dosing by weight, contraindications, interactions
- **Triage support** — START/SALT/JumpSTART triage, mass-casualty incident (MCI) guidance
- **Differential support** — symptom-to-differential reasoning for field assessment
- **Trauma guidance** — hemorrhage control, spinal precautions, burn classification
- **OB/Peds** — childbirth emergencies, pediatric dosing (Broselow), neonatal resuscitation
- **Toxicology** — overdose recognition, antidote references, decontamination
- **Documentation** — PCR narrative generation, patient assessment templates

---

## Architecture

```
BONES
├── src/bones/          Core library (prompts, model interface)
├── scripts/
│   ├── data_collection/    Protocol and guideline scrapers
│   ├── training/           QLoRA fine-tuning pipeline
│   └── evaluation/         Clinical accuracy benchmarks
├── configs/            Training and model configuration
├── data/
│   ├── raw/            Source protocol documents and datasets
│   ├── processed/      Cleaned, formatted training data
│   └── synthetic/      AI-generated clinical scenario examples
├── ollama/             Modelfile for local deployment
└── tests/              Unit tests
```

---

## Training Data Sources

| Source | Description | License |
|---|---|---|
| AHA ACLS/PALS/BLS Guidelines | Cardiac arrest and resuscitation algorithms | Public guidelines |
| NAEMSP / NASEMSO Protocols | National EMS protocols and scope of practice | Public |
| OpenMedSpel / MedQA | Medical Q&A datasets | Open |
| PubMed Central | EMS and emergency medicine literature | Open Access |
| NREMT Scope of Practice | EMR/EMT/AEMT/Paramedic scope tables | Public |
| Synthetic Scenarios | AI-generated dispatch-to-treatment examples | Proprietary |

---

## Quick Start

```bash
# Baseline (prompt-only, no fine-tuning required)
ollama run Ronin48/bones:v0.1.0

# Fine-tuned (after training completes)
ollama run Ronin48/bones:v1.0.0
```

---

## Training

```bash
# Generate synthetic scenarios
python scripts/data_collection/generate_synthetic.py

# Prepare dataset
python scripts/training/prepare_dataset.py

# Train (QLoRA on 70B)
python scripts/training/train_qlora.py --config configs/training_config.yaml

# Merge adapter
python scripts/training/merge_adapter.py --config configs/training_config.yaml
```

---

## Related Models — Ronin 48 First Responder Suite

BONES, BRUNO, and SELMA are the three first responder models. They share scenes constantly — consult the appropriate model for each domain.

| Model | Domain | Use When... |
|---|---|---|
| **BONES** | EMS — EMR / EMT / AEMT / Paramedic | Patient assessment, treatment protocols, drug dosing, triage, transport |
| **[BRUNO](https://codeberg.org/Ronin48/BRUNO)** *(Building Rescue and Unified Navigation Operations)* | Fire Service — Company Officer / IC | Fireground tactics, size-up, hazmat, extrication, water supply, ICS |
| **[SELMA](https://codeberg.org/Ronin48/SELMA)** | Law Enforcement | Criminal statute identification, charge elements, constitutional flags |

### Common Shared Scenes

| Scene Type | Primary | Support |
|---|---|---|
| Structure fire with casualties | BRUNO (fireground ops) | BONES (patient care) |
| Vehicle accident with entrapment | BRUNO (extrication) | BONES (patient care during extrication) |
| Hazmat with patient exposures | BRUNO (mitigation, decon zone) | BONES (patient decon and treatment) |
| Mass casualty incident | BONES (triage, treatment) | BRUNO (ICS, sectors) + SELMA (criminal nexus if applicable) |
| Overdose call | BONES (patient care, naloxone) | SELMA (applicable charges if distribution involved) |
| Domestic violence with injuries | BONES (patient care) | SELMA (criminal charges, elements) |
| Active shooter / active threat | SELMA (legal authority, charges) | BONES (casualty care, TECC) + BRUNO (scene safety, ICS) |
| Cardiac arrest in a burning structure | BRUNO (scene safety, egress) | BONES (resuscitation protocol) |
| Mental health crisis with violence | SELMA (criminal elements) | BONES (patient assessment, excited delirium protocol) |

> ABBY (digital forensics) operates independently of the first responder suite. SELMA pairs with [ATTICUS](https://codeberg.org/Ronin48/ATTICUS) on the legal side — prosecution and defense counterparts.

---

## ⚠ Disclaimer

**BONES is a clinical decision support tool, not a replacement for medical direction.**

- All treatment decisions must follow your agency's standing orders and medical director protocols.
- BONES does not replace online medical control for ALS interventions.
- In mass-casualty or unusual situations, always escalate to your medical director.
- Drug dosing information must be verified against your agency formulary before administration.
- This tool is intended for training and reference only — it is not an FDA-cleared medical device.

**When in doubt, call medical control.**

---

## Training Notes

If you're training BONES on RunPod or another GPU cloud provider, read [LESSONS_LEARNED.md](LESSONS_LEARNED.md)
before you start. ABBY's file has the most complete record of first-run errors and fixes —
BONES's file links there and will capture any BONES-specific issues as they arise.

---

## License

MIT License — see [LICENSE](LICENSE)

---

Proudly Made in Nebraska. Go Big Red! 🌽
