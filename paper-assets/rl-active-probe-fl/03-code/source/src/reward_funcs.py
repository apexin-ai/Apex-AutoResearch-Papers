"""Reward functions for GRPO training — fix-based reward.

Each function follows TRL GRPOTrainer signature:
    (prompts: list[str], completions: list[str], **kwargs) -> list[float]

Core idea: probe quality is measured by whether a fix generated
using probe output passes all tests.
Dependencies: src.sandbox, src.prompts, src.validate_tests
"""

import random
import re
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.prompts import FIX_GENERATION_PROMPT
from src.sandbox import execute_probe, run_tests
from src.validate_tests import clean_test_code

_policy_model = None
_tokenizer = None


def set_policy_model(model, tokenizer):
    """Register the policy model for fix generation. Called by train_grpo.py at startup."""
    global _policy_model, _tokenizer
    _policy_model = model
    _tokenizer = tokenizer


def _unwrap_completion(completion) -> str:
    """TRL 1.1.0 passes completions as list[dict] (conversation format)."""
    if isinstance(completion, list):
        return completion[-1]["content"] if completion else ""
    return completion


def _extract_probe(completion: str) -> str | None:
    match = re.search(r"```probe\s*\n(.*?)```", completion, re.DOTALL)
    return match.group(1).strip() if match else None


def _extract_code(text: str) -> str | None:
    match = re.search(r"```python\s*\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"```\s*\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


@lru_cache(maxsize=256)
def _get_failing_output(buggy_code: str, test_code: str) -> str:
    return run_tests(buggy_code, test_code, timeout=10).output


def _generate_fix(buggy_code: str, test_output: str, probe_output: str,
                  max_new_tokens: int = 512) -> str | None:
    if _policy_model is None or _tokenizer is None:
        raise RuntimeError("Call set_policy_model() first")

    user_content = FIX_GENERATION_PROMPT.format(
        buggy_code=buggy_code,
        test_output=test_output,
        probe_output=probe_output,
    )
    messages = [{"role": "user", "content": user_content}]
    text = _tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
    )
    inputs = _tokenizer(text, return_tensors="pt")
    inputs = {k: v.to(_policy_model.device) for k, v in inputs.items()}

    with torch.no_grad():
        output_ids = _policy_model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    new_tokens = output_ids[0][inputs["input_ids"].shape[1]:]
    generated = _tokenizer.decode(new_tokens, skip_special_tokens=True)
    return _extract_code(generated) or generated.strip()


def fix_based_reward(
    prompts: list[str], completions: list[str], **kwargs: Any
) -> list[float]:
    """Main reward: probe → execute → generate fix → run tests.
    Returns 1.0 if fix passes all tests, 0.0 otherwise.
    """
    buggy_codes: list[str] = kwargs["buggy_code"]
    test_codes: list[str] = kwargs["test_code"]
    rewards = []

    for completion, buggy_code, test_code in zip(completions, buggy_codes, test_codes):
        completion = _unwrap_completion(completion)
        probe = _extract_probe(completion)
        if probe is None:
            rewards.append(0.0)
            continue

        clean_test = clean_test_code(test_code)

        probe_result = execute_probe(buggy_code, probe, test_code=clean_test, timeout=5)
        probe_output = probe_result.stdout if probe_result.stdout.strip() else ""

        failing_output = _get_failing_output(buggy_code, clean_test)

        fix_code = _generate_fix(buggy_code, failing_output, probe_output)
        if fix_code is None:
            rewards.append(0.0)
            continue

        test_result = run_tests(fix_code, clean_test, timeout=10)
        rewards.append(1.0 if test_result.passed else 0.0)

    return rewards


def probe_execution_bonus(
    prompts: list[str], completions: list[str], **kwargs: Any
) -> list[float]:
    """Bonus: probe executes without error → +0.1."""
    buggy_codes: list[str] = kwargs["buggy_code"]
    test_codes: list[str] = kwargs["test_code"]
    rewards = []
    for completion, buggy_code, test_code in zip(completions, buggy_codes, test_codes):
        completion = _unwrap_completion(completion)
        probe = _extract_probe(completion)
        if probe is None:
            rewards.append(0.0)
            continue
        clean_test = clean_test_code(test_code)
        result = execute_probe(buggy_code, probe, test_code=clean_test, timeout=5)
        rewards.append(0.1 if (result.success or result.stdout.strip()) else 0.0)
    return rewards


def probe_dependence_reward(
    prompts: list[str], completions: list[str], **kwargs: Any
) -> list[float]:
    """Counterfactual probe-dependence on 20% of samples.
    Generates fix with real probe output vs empty probe output.
    If the two fixes differ → +0.1.
    """
    buggy_codes: list[str] = kwargs["buggy_code"]
    test_codes: list[str] = kwargs["test_code"]
    sample_rate: float = kwargs.get("probe_dep_sample_rate", 0.2)
    rewards = []

    for completion, buggy_code, test_code in zip(completions, buggy_codes, test_codes):
        if random.random() > sample_rate:
            rewards.append(0.0)
            continue

        completion = _unwrap_completion(completion)
        probe = _extract_probe(completion)
        if probe is None:
            rewards.append(0.0)
            continue

        clean_test = clean_test_code(test_code)
        probe_result = execute_probe(buggy_code, probe, test_code=clean_test, timeout=5)
        probe_output = probe_result.stdout if probe_result.stdout.strip() else ""
        failing_output = _get_failing_output(buggy_code, clean_test)

        real_fix = _generate_fix(buggy_code, failing_output, probe_output)
        null_fix = _generate_fix(buggy_code, failing_output, "")

        if real_fix and null_fix and real_fix != null_fix:
            rewards.append(0.1)
        else:
            rewards.append(0.0)

    return rewards
