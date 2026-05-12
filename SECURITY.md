# BONES Security Policy

## Reporting Security Vulnerabilities

**DO NOT** open a public issue for security vulnerabilities.

**Email:** security@ronin48.io
**Subject:** [BONES Security] Brief description

We will acknowledge within 48 hours and respond within 7 business days.

## Security Design Principles

### 1. Human-in-the-Loop (MANDATORY)

BONES is an advisory tool. All treatment decisions MUST be made by licensed EMS personnel following their agency's protocols and medical director guidance. BONES must never be deployed as an autonomous clinical decision-making system.

### 2. No Agency

BONES is text-in, text-out. It cannot:
- Contact medical control on your behalf
- Access patient records or EMS databases
- Transmit data to external systems
- Issue orders or modify documentation

### 3. Not an FDA-Cleared Medical Device

BONES is not FDA-cleared and must not be used as the sole basis for clinical decisions. It is a training and reference tool.

### 4. Open Source Transparency

All code, prompts, and training frameworks are open source for community audit.

### 5. Supply Chain Security

- Base model: Meta Llama (U.S.-origin, verified provenance)
- All dependencies version-pinned in requirements.txt

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | Yes       |

## Security Contact

- **Email:** security@ronin48.io
- **Organization:** Ronin 48, LLC
