#!/usr/bin/env python3
from pathlib import Path

from transformers import AutoTokenizer


ROOT = Path(
    "."
)
MODELS = {
    "qwen3_8b": ROOT / "models/Qwen/Qwen3-8B",
    "deepseek14b": (
        ROOT / "models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
    ),
}


for name, model_path in MODELS.items():
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        trust_remote_code=True,
        local_files_only=True,
    )
    messages = [{"role": "user", "content": "Return NEW_CONFIG JSON only."}]
    default = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    try:
        disabled = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
    except Exception as exc:
        disabled = f"ERROR: {exc!r}"
    print(f"MODEL={name}")
    print(f"DEFAULT_TAIL={default[-500:]!r}")
    print(f"DISABLED_TAIL={disabled[-500:]!r}")
    print(f"DIFFERENT={default != disabled}")
