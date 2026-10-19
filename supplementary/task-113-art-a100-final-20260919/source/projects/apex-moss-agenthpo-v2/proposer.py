"""Proposer: reads a family's harness lineage, diagnoses failures, writes the next version.

The proposer sees ONLY training-benchmark results. It must preserve the run()
signature and the frozen MODEL line, and self-report what it changed (mechanism tag).
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import anthropic

import config
from harness_source import InvalidHarness, parse_generated_harness

CONSTRAINTS = """Hard constraints (violations cause automatic rejection by the scorer):
- Keep the exact line: MODEL = "claude-haiku-4-5"  (executor model is frozen)
- Keep the exact signature: def run(work_dir: str, tool_definitions: list, tool_dispatch: dict) -> dict
- run() must return {"steps": int, "tokens": int, "messages": list}
- Use only the provided tools via tool_dispatch; each dispatch function accepts exactly
  one input dict, e.g. tool_dispatch["read_file"]({"path": path}); never pass **kwargs
- Tool results have fixed types: read_file returns str; write_file returns str;
  run_tests returns {"returncode": int, "stdout": str, "stderr": str, "passed": bool}.
  Never treat the run_tests dict as text or call string methods on it; check
  result["passed"] and use result["stdout"]/result["stderr"] for feedback
- Do not import subprocess/os.system or call other APIs
- Imports are restricted to anthropic, json, and os. The only allowed os access is
  os.environ.get, os.getenv, and pure path construction with os.path.join
- Never call open, exec, eval, compile, __import__, getattr, setattr, globals, or vars;
  all task file access must go through the provided tools
- Never write to test_solution.py or any file other than solution.py inside work_dir
  (the scorer restores all other files and marks the run as cheating, scoring 0)
- The file must be self-contained Python importable as a module (imports: anthropic, json, os only)

What you MAY change: the system prompt, the user prompt, step budget allocation,
retry logic, what context is shown to the model, ordering of actions (e.g. run tests
first to see failures before reading code), stop conditions."""
GENERATOR_TIMEOUT_SECONDS = 300.0


def _preserve_raw_response(
    family_dir: Path, kind: str, attempt: int, text: str
) -> Path:
    """Keep generator output outside score/checkpoint paths for later diagnosis."""
    repo_root = (
        family_dir.parents[1]
        if family_dir.parent.name == "harnesses"
        else family_dir.parent
    )
    raw_dir = (
        repo_root / "results" / "generator_raw" / "proposer" / family_dir.name
    )
    raw_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    path = raw_dir / f"{stamp}-{kind}-attempt{attempt + 1}.txt"
    path.write_text(text)
    return path


def gather_history(family_dir: Path, max_trace_chars: int = 3000) -> str:
    sections = []
    versions = sorted([d for d in family_dir.iterdir() if d.is_dir() and d.name.startswith("v")])
    for v_dir in versions:
        section = f"\n{'=' * 60}\n## {v_dir.name}\n{'=' * 60}\n"
        harness_file = v_dir / "harness.py"
        if harness_file.exists():
            section += f"\n### harness.py\n```python\n{harness_file.read_text()}\n```\n"

        summary_file = v_dir / "train_summary.json"
        if summary_file.exists():
            section += f"\n### training scores\n{summary_file.read_text()}\n"

        traces_dir = v_dir / "train_results"
        if traces_dir.exists():
            for tf in sorted(traces_dir.glob("*.rep0.json")):
                t = json.loads(tf.read_text())
                if t.get("passed"):
                    continue
                compact = {
                    "task": t.get("task"), "passed": False,
                    "tampered": t.get("tampered"), "steps": t.get("steps"),
                    "error": t.get("error"),
                    "test_output": (t.get("test_output") or "")[-1200:],
                    "last_messages": json.dumps(t.get("trace", [])[-4:], ensure_ascii=False, default=str)[-max_trace_chars:],
                }
                section += f"\n### FAILED: {t.get('task')}\n```json\n{json.dumps(compact, indent=1, ensure_ascii=False)}\n```\n"
        sections.append(section)
    return "\n".join(sections)


def propose(family_dir: str, family_desc: str) -> tuple[str, str]:
    """Returns (new_harness_code, mechanism_tag)."""
    config.load_env()
    family_dir = Path(family_dir)
    history = gather_history(family_dir)

    prompt = f"""You are improving an agent harness (the workflow wrapper around a fixed LLM) for this task family:

{family_desc}

Below is the complete lineage: every harness version, its code, training scores, and traces of failed tasks.

{history}

Your job:
1. Diagnose each failed task: did the workflow fail to show the model key information? Run out of steps? Use a bad strategy order? Crash?
2. Write an improved harness.py targeting the SPECIFIC failures you observed.

{CONSTRAINTS}

Output format — exactly two blocks:
MECHANISM: <one sentence: what this version changes and why>
```python
<complete harness.py content>
```"""

    client = anthropic.Anthropic(
        timeout=GENERATOR_TIMEOUT_SECONDS,
        max_retries=0,
    )
    messages = [{"role": "user", "content": prompt}]
    for attempt in range(3):
        response = client.messages.create(
            model=config.PROPOSER_MODEL,
            max_tokens=8192,
            messages=messages,
        )
        text = response.content[0].text
        _preserve_raw_response(family_dir, "proposal", attempt, text)
        try:
            return parse_generated_harness(text)
        except InvalidHarness as exc:
            if attempt == 2:
                raise
            messages.extend([
                {"role": "assistant", "content": text},
                {
                    "role": "user",
                    "content": (
                        f"The generated harness is invalid: {exc}. Repair only "
                        "this contract error. Do not change the mechanism based "
                        "on new benchmark information. Return the same two-block "
                        "format with a corrected complete harness."
                    ),
                },
            ])
    raise RuntimeError("unreachable")


def repair_candidate(
    family_dir: str, candidate_text: str, contract_error: str
) -> tuple[str, str, str]:
    """Repair one rejected candidate using only that candidate and its error."""
    config.load_env()
    family_path = Path(family_dir)
    messages = [{
        "role": "user",
        "content": (
            "Repair the generated harness below using only the candidate and the "
            "contract error. Do not use or infer any new benchmark information, "
            "scores, or traces.\n\n"
            f"CONTRACT ERROR:\n{contract_error}\n\n"
            f"CANDIDATE:\n{candidate_text}\n\n"
            "Return the same two-block format with a corrected complete harness."
        ),
    }]
    client = anthropic.Anthropic(
        timeout=GENERATOR_TIMEOUT_SECONDS,
        max_retries=0,
    )
    for attempt in range(3):
        response = client.messages.create(
            model=config.PROPOSER_MODEL,
            max_tokens=8192,
            messages=messages,
        )
        text = response.content[0].text
        _preserve_raw_response(family_path, "contract-repair", attempt, text)
        try:
            code, mechanism = parse_generated_harness(text)
            return code, mechanism, text
        except InvalidHarness as exc:
            if attempt == 2:
                raise
            messages.extend([
                {"role": "assistant", "content": text},
                {
                    "role": "user",
                    "content": (
                        f"The repaired harness is still invalid: {exc}. Repair "
                        "only this contract error, using no benchmark information. "
                        "Return the same two-block format."
                    ),
                },
            ])
    raise RuntimeError("unreachable")
