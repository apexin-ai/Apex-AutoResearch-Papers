"""Prompt templates and formatting utilities for probe generation.

Input: Training samples with question, buggy_code, good_probe, etc.
Output: Formatted prompts for SFT training and GRPO generation.
Dependencies: none
"""

PROBE_GENERATION_SYSTEM = (
    "You are a professional code debugging assistant. "
    "Given a buggy piece of code and a problem description, generate diagnostic runtime probes "
    "(print/assert/variable inspection statements) that, when inserted into the code and executed, "
    "help locate the bug. Output 1-5 lines of probe code wrapped in ```probe\\n...\\n``` "
    "followed by a one-sentence explanation of what the probe checks."
)

PROBE_GENERATION_PROMPT = """\
## Problem Description
{question}

## Buggy Code
```python
{buggy_code}
```

Generate diagnostic runtime probes to help locate the bug in the code above. \
Output your probe code inside ```probe``` fences, then a brief explanation.
/no_think"""

PROBE_GENERATION_WITH_OUTPUT_PROMPT = """\
## Problem Description
{question}

## Buggy Code
```python
{buggy_code}
```

## Probe Output
The following diagnostic output was captured when running probes on the buggy code:
```
{probe_output}
```

Based on the probe output above, fix the buggy code. Output the corrected code inside ```python``` fences.
/no_think"""


FIX_GENERATION_PROMPT = """\
You are a code debugger. Given:
1. A buggy Python code
2. The failing test output
3. Diagnostic probe output showing variable states

Fix the bug and output ONLY the corrected complete code in ```python``` fences (no explanations).

## Buggy Code
```python
{buggy_code}
```

## Failing Test Output
```
{test_output}
```

## Diagnostic Probe Output
```
{probe_output}
```

Output the fixed code:
/no_think"""


def format_sft_example(sample: dict) -> dict:
    """Format a training sample as a chat-format messages list for SFT.

    Args:
        sample: Dict with keys question, buggy_code, good_probe, probe_rationale.

    Returns:
        Dict with key "messages" containing the chat conversation.
    """
    user_content = PROBE_GENERATION_PROMPT.format(
        question=sample["question"],
        buggy_code=sample["buggy_code"],
    )
    assistant_content = f"```probe\n{sample['good_probe']}\n```\n{sample['probe_rationale']}"
    return {
        "messages": [
            {"role": "system", "content": PROBE_GENERATION_SYSTEM},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ]
    }


def format_grpo_prompt(sample: dict) -> str:
    """Format a sample as a GRPO prompt string (user turn only).

    Args:
        sample: Dict with keys question, buggy_code.

    Returns:
        The formatted prompt string.
    """
    return PROBE_GENERATION_PROMPT.format(
        question=sample["question"],
        buggy_code=sample["buggy_code"],
    )
