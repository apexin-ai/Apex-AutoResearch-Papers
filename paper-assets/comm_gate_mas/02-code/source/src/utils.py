"""Shared utilities for comm_gate_mas pipeline."""

from __future__ import annotations

import re


def model_supports_system_role(model_name: str) -> bool:
    """Check if a model supports the system role in chat completions."""
    no_system_patterns = ["gemma"]
    return not any(p in model_name.lower() for p in no_system_patterns)


def convert_system_to_user(messages: list[dict]) -> list[dict]:
    """Convert system role messages to user role for models that don't support system role.
    Prepends system content to the first user message, or adds as a user message."""
    result = []
    system_content = []
    for msg in messages:
        if msg["role"] == "system":
            system_content.append(msg["content"])
        else:
            if system_content and msg["role"] == "user":
                combined = "\n\n".join(system_content) + "\n\n" + msg["content"]
                result.append({"role": "user", "content": combined})
                system_content = []
            else:
                if system_content:
                    result.append({"role": "user", "content": "\n\n".join(system_content)})
                    system_content = []
                result.append(msg)
    if system_content:
        result.append({"role": "user", "content": "\n\n".join(system_content)})
    return result


def strip_eos_residue(text: str) -> str:
    """Strip hallucinated text after EOS tokens left by vLLM."""
    for token in ("<|im_end|>", "<|eot_id|>", "<|end_of_text|>", "</s>"):
        idx = text.find(token)
        if idx != -1:
            text = text[:idx]
    return text


def extract_final_answer(text: str) -> str | None:
    text = strip_eos_residue(text)
    numeric_patterns = [
        r"[Tt]he answer is\s*\[?\s*\$?\s*([0-9,.\-]+)\s*\]?",
        r"####\s*\$?\s*([0-9,.\-]+)",
        r"[Ff]inal [Aa]nswer[:\s]+\$?\s*([0-9,.\-]+)",
        r"\*\*[Aa]nswer:?\*\*:?\s+\$?\s*([0-9,.\-]+)",
        r"\*\*[Aa]nswer:?\*\*:?\s.*?\$\s*([0-9,.]+)",
        r"\*\*[Aa]nswer:?\*\*:?\s.*?(?:is |= )([0-9,.\-]+)",
        r"\*\*[Aa]nswer:?\*\*:?[^\d]*(\d[\d,.]*)",
        r"\\boxed\{([0-9,.\-]+)\}",
    ]
    for pat in numeric_patterns:
        matches = re.findall(pat, text)
        if matches:
            return matches[-1].strip().replace(",", "").replace("$", "")
    bool_patterns = [
        r"[Tt]he answer is\s+(yes|no|true|false)",
        r"####\s*(yes|no|true|false)",
        r"[Ff]inal [Aa]nswer[:\s]+(yes|no|true|false)",
        r"\*\*[Aa]nswer\*\*[:\s]+(yes|no|true|false)",
    ]
    for pat in bool_patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            return matches[-1].strip().lower()
    return None
