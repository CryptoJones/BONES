"""Tests for BONES prompt templates."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src" / "bones"))

from prompts import SYSTEM_PROMPT, format_clinical_prompt


def test_system_prompt_not_empty():
    assert len(SYSTEM_PROMPT) > 100


def test_system_prompt_has_scope_guidance():
    assert "EMR" in SYSTEM_PROMPT
    assert "EMT" in SYSTEM_PROMPT
    assert "Paramedic" in SYSTEM_PROMPT


def test_system_prompt_has_disclaimer():
    assert "DISCLAIMER" in SYSTEM_PROMPT


def test_system_prompt_flags_als():
    assert "ALS INTERVENTION" in SYSTEM_PROMPT
    assert "CONTACT MEDICAL CONTROL" in SYSTEM_PROMPT


def test_format_clinical_prompt():
    messages = format_clinical_prompt("58M chest pain, diaphoretic, BP 90/60")
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert "58M chest pain" in messages[1]["content"]


def test_format_clinical_prompt_system_content():
    messages = format_clinical_prompt("test presentation")
    assert messages[0]["content"] == SYSTEM_PROMPT
