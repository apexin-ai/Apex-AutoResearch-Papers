"""Builder v0: generate a task-specific harness from a family card alone (zero-shot).

The card describes the task family (goal/environment/feedback/tools/reasoning);
it contains no benchmark items, no scores, no traces.

Usage: python builder.py <family>
"""

import sys
from pathlib import Path

import anthropic

import config
from harness_source import InvalidHarness, parse_generated_harness
from proposer import CONSTRAINTS, _preserve_raw_response

HERE = Path(__file__).resolve().parent


def build(family: str) -> str:
    config.load_env()
    card = (HERE / "family_cards" / f"{family}.md").read_text()

    prompt = f"""You are a harness builder. Given only the following task-family description card,
design and write a harness (agent workflow) specialized for this family.

{card}

A harness is a Python file that wraps a fixed LLM in a workflow: it decides what the
model sees, in what order actions happen, how failures are retried, and when to stop.
The available tools are: read_file(path), write_file(path, content), run_tests(test_path)
— passed in via tool_definitions/tool_dispatch.

Design the workflow to exploit the specifics of this task family as described in the card.

{CONSTRAINTS}

Output format — exactly two blocks:
MECHANISM: <one sentence: what is specialized for this family and why>
```python
<complete harness.py content>
```"""

    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": prompt}]
    last_error = None
    for attempt in range(3):
        response = client.messages.create(
            model=config.PROPOSER_MODEL,
            max_tokens=8192,
            messages=messages,
        )
        text = response.content[0].text
        _preserve_raw_response(
            HERE / "harnesses" / family, "builder", attempt, text
        )
        try:
            code, mechanism = parse_generated_harness(text)
            break
        except InvalidHarness as exc:
            last_error = exc
            if attempt == 2:
                raise
            # This repair sees only the card, the candidate, and its contract error;
            # benchmark items and evaluation results remain hidden.
            messages.extend([
                {"role": "assistant", "content": text},
                {
                    "role": "user",
                    "content": (
                        f"The generated harness is invalid: {exc}. "
                        "Return the same two-block format with a corrected, complete "
                        "harness. Keep any Markdown fences inside Python string "
                        "literals; the outer response still needs one Python fence."
                    ),
                },
            ])
    else:  # pragma: no cover - loop either breaks or raises
        raise InvalidHarness(str(last_error))

    out_dir = HERE / "harnesses" / family / "builder0"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "harness.py").write_text(code)
    (out_dir / "MECHANISM.txt").write_text(mechanism)
    print(f"[{family}] builder0 written: {mechanism}")
    return str(out_dir / "harness.py")


if __name__ == "__main__":
    build(sys.argv[1])
