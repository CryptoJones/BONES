# Contributing to BONES

## How to Contribute

1. **Fork** the repository on Codeberg
2. **Create a branch** for your feature or fix
3. **Make your changes** with clear commit messages
4. **Run tests** — `pytest tests/`
5. **Submit a pull request** with a description of your changes

## Development Setup

```bash
git clone https://codeberg.org/Ronin48/BONES.git
cd BONES
pip install -r requirements.txt
pytest tests/
```

## High-Value Contributions

- **Clinical scenario examples** — high-quality synthetic dispatch-to-treatment JSONL examples
- **Protocol coverage** — ACLS/PALS/BLS algorithm training data
- **Drug reference data** — EMS formulary Q&A pairs with dosing
- **Evaluation** — clinical accuracy benchmark cases
- **PDF parsers** — scripts to extract training data from EMS textbooks and protocols

## Adding Training Data

EMS scenario format:
```json
{
  "messages": [
    {"role": "system", "content": "<BONES system prompt>"},
    {"role": "user", "content": "Patient presentation..."},
    {"role": "assistant", "content": "Clinical decision support response..."}
  ],
  "type": "clinical_scenario",
  "domain": "cardiac",
  "scope": "paramedic"
}
```

Valid `scope` values: `emr`, `emt`, `aemt`, `paramedic`
Valid `type` values: `clinical_scenario`, `protocol_reference`, `drug_reference`, `literature_reference`

Drop new JSONL files into `data/synthetic/` — `prepare_dataset.py` picks them up automatically.

## Code Style

- PEP 8
- Type hints on public functions
- Tests for new functionality
- Use `Path(__file__).resolve().parent...` for all file paths — never `os.getcwd()` or relative paths

## Medical Accuracy

All contributed clinical content must:
- Cite the source protocol or guideline (e.g., "AHA ACLS 2020")
- Correctly attribute scope of practice to EMR/EMT/AEMT/Paramedic levels
- Include appropriate medical direction disclaimers for ALS interventions
- Not contain real patient information

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
