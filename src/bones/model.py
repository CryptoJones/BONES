"""BONES model interface for local inference via Ollama."""

import json
import urllib.request


OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "Ronin48/bones:latest"
DEFAULT_OPTIONS = {"temperature": 0.2, "top_p": 0.9, "num_predict": 2048}


def chat(messages: list[dict], model: str = DEFAULT_MODEL, options: dict | None = None) -> str:
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "stream": False,
        "options": options or DEFAULT_OPTIONS,
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())["message"]["content"]
