"""Phase 3 v3: Strong-model disambiguation experiment.

Changes from v2:
  - Default model: anthropic/claude-sonnet-4 (via OpenRouter proxy)
  - Configurable via REPAIR_MODEL env var or --repair-model flag
  - API read timeout increased to 180s (Claude responses may be slower)
  - All 14 Tier 1 instances as default (not just 4)
  - Checkpoint: phase3_v3_checkpoint.json, CSV: phase3_v3_results.csv
  - More robust diff extraction (handles Claude markdown wrapping)
  - Startup banner logs model, instance count, condition count

Input: pipeline_output/phase3_instances.json, phase2 scores, trace data
Output: pipeline_output/phase3_v3_checkpoint.json, phase3_v3_results.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

from dtd_types import TraceEvent, TraceSegment, ScoredSegment, estimate_tokens
from mvp_pipeline import TRACE_SECTION_TEMPLATE, MVPPipeline
from run_phase2_scoring import load_segments, get_buggy_code, INSTANCE_DESCRIPTIONS
from bugsinpy_setup import BugsInPySetup

logger = logging.getLogger(__name__)

PIPELINE_OUTPUT = "/root/trace_distill_repair/pipeline_output"
WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]

# All 14 Tier 1 instances from phase3_instances.json
TARGET_INSTANCES = [
    "black_1", "cookiecutter_1", "cookiecutter_2", "cookiecutter_3",
    "fastapi_2", "httpie_2", "luigi_5", "sanic_2",
    "scrapy_2", "scrapy_7", "tornado_2",
    "youtube-dl_1", "youtube-dl_5", "youtube-dl_20",
]

DIFF_REPAIR_PROMPT = """\
You are a bug repair expert. Given the buggy source code and diagnostic information, generate a unified diff patch to fix the bug.

## Bug Report
{issue_description}

## Buggy Source Files
{buggy_files_section}
{trace_section}
## Task
Generate a unified diff patch that fixes the bug described above.

Output ONLY the unified diff in this exact format:
--- a/path/to/file.py
+++ b/path/to/file.py
@@ -line,count +line,count @@
 context line
-removed line
+added line
 context line

Rules:
- Output ONLY the diff, no explanation before or after
- Include at least 3 context lines around each change for unambiguous patch application
- The diff must be applicable with `patch -p1`
- Fix ONLY the bug, do not refactor or change unrelated code
- If multiple files need changes, include all of them in one diff
"""

CSV_FIELDS = [
    "instance_id", "condition", "test_pass", "diff_apply_success",
    "eval_method", "tokens_input", "tokens_output",
    "llm_judge_score", "llm_judge_reasoning",
    "raw_diff", "test_stdout_snippet", "test_stderr_snippet",
]


# ---------------------------------------------------------------------------
# Reuse helpers from v2
# ---------------------------------------------------------------------------

def count_tokens(text: str) -> int:
    return len(text.split())


def truncate_trace(trace_text: str, max_tokens: int = 16000) -> Tuple[str, int, int]:
    tokens = trace_text.split()
    original_count = len(tokens)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
    return ' '.join(tokens), original_count, len(tokens)


def load_phase2_scores(mode: str) -> Dict[str, list]:
    path = os.path.join(PIPELINE_OUTPUT, f"phase2_{mode}_scores.json")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"{path} not found")
    with open(path) as f:
        data = json.load(f)
    return {
        key: inst.get("scores", [])
        for key, inst in data.get("results", {}).items()
    }


def load_trace_events(instance_key: str) -> List[TraceEvent]:
    path = os.path.join(PIPELINE_OUTPUT, f"{instance_key}_trace.json")
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        raw = json.load(f)
    events = []
    for e in raw:
        exc_info = None
        ei = e.get("exception_info")
        if ei:
            if isinstance(ei, dict):
                exc_info = (ei.get("type", ""), ei.get("value", ""), ei.get("traceback", ""))
            elif isinstance(ei, (list, tuple)):
                exc_info = tuple(ei)
        events.append(TraceEvent(
            event_type=e["event_type"],
            function_name=e["function_name"],
            filename=e["filename"],
            lineno=e["lineno"],
            locals_snapshot=e.get("locals_snapshot", {}),
            call_depth=e["call_depth"],
            timestamp=e.get("timestamp", 0.0),
            return_value=e.get("return_value"),
            exception_info=exc_info,
        ))
    return events


def build_keep_segments(instance_key: str, mode: str, scores: list) -> List[ScoredSegment]:
    segments = load_segments(instance_key, mode)
    if not segments or not scores:
        return []
    seg_map = {(s.segment_type, s.start_idx, s.end_idx): s for s in segments}
    result = []
    for sc in scores:
        if sc.get("label") != "keep":
            continue
        key = (sc["segment_type"], sc["start_idx"], sc["end_idx"])
        seg = seg_map.get(key)
        if seg:
            result.append(ScoredSegment(
                segment=seg, label="keep",
                confidence=sc.get("confidence", 0.0),
                reasoning=sc.get("reasoning", ""),
            ))
    return result


_PHASE3_INSTANCES_CACHE = None

def load_phase3_instances() -> Dict[str, dict]:
    global _PHASE3_INSTANCES_CACHE
    if _PHASE3_INSTANCES_CACHE is not None:
        return _PHASE3_INSTANCES_CACHE
    path = os.path.join(PIPELINE_OUTPUT, "phase3_instances.json")
    with open(path) as f:
        instances = json.load(f)
    _PHASE3_INSTANCES_CACHE = {inst["instance_id"]: inst for inst in instances}
    return _PHASE3_INSTANCES_CACHE


# ---------------------------------------------------------------------------
# Parse target files from ground_truth_patch
# ---------------------------------------------------------------------------

def parse_patch_files(patch_text: str) -> List[str]:
    """Extract file paths from a unified diff's '--- a/...' lines."""
    files = []
    for line in patch_text.splitlines():
        if line.startswith("--- a/"):
            f = line[len("--- a/"):]
            if f not in files:
                files.append(f)
    return files


def read_buggy_file(instance_key: str, relpath: str) -> str:
    """Read a file from the buggy workspace directory."""
    path = os.path.join(WORKSPACE, "instances", instance_key, "buggy", relpath)
    if not os.path.isfile(path):
        return ""
    with open(path) as f:
        return f.read()


def build_buggy_files_section(instance_key: str, file_paths: List[str]) -> str:
    """Build prompt section showing all relevant buggy files."""
    sections = []
    for fp in file_paths:
        code = read_buggy_file(instance_key, fp)
        if not code:
            continue
        lines = code.splitlines()
        if len(lines) > 4000:
            code = "\n".join(lines[:4000]) + f"\n... ({len(lines) - 4000} more lines truncated)"
        sections.append(f"### {fp}\n```python\n{code}\n```")
    return "\n\n".join(sections) if sections else "(no source files found)"


# ---------------------------------------------------------------------------
# Diff application and testing
# ---------------------------------------------------------------------------

def recount_diff_hunks(diff_text: str) -> str:
    """Recalculate @@ line counts from actual hunk body."""
    lines = diff_text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^@@ -(\d+),\d+ \+(\d+),\d+ @@(.*)', lines[i])
        if m:
            old_start, new_start, rest = int(m.group(1)), int(m.group(2)), m.group(3)
            hunk_lines = []
            j = i + 1
            while j < len(lines):
                if lines[j].startswith('@@') or lines[j].startswith('--- ') or lines[j].startswith('+++ '):
                    break
                hunk_lines.append(lines[j])
                j += 1
            while hunk_lines and hunk_lines[-1] == '':
                hunk_lines.pop()
            old_count = sum(1 for l in hunk_lines if not l.startswith('+'))
            new_count = sum(1 for l in hunk_lines if not l.startswith('-'))
            result.append(f'@@ -{old_start},{old_count} +{new_start},{new_count} @@{rest}')
            result.extend(hunk_lines)
            i = j
        else:
            result.append(lines[i])
            i += 1
    return '\n'.join(result) + '\n'


def apply_diff_in_dir(diff_text: str, work_dir: str, dry_run: bool = False) -> Tuple[bool, str]:
    """Apply a unified diff in work_dir using patch -p1. Returns (success, message)."""
    diff_text = recount_diff_hunks(diff_text)
    cmd = ["patch", "-p1", "--no-backup-if-mismatch"]
    if dry_run:
        cmd.append("--dry-run")
    proc = subprocess.run(
        cmd, input=diff_text, capture_output=True, text=True, cwd=work_dir,
    )
    ok = proc.returncode == 0
    msg = proc.stdout[:500] if ok else proc.stderr[:500]
    return ok, msg


def revert_diff_in_dir(diff_text: str, work_dir: str) -> Tuple[bool, str]:
    """Revert a previously applied diff."""
    proc = subprocess.run(
        ["patch", "-R", "-p1", "--no-backup-if-mismatch"],
        input=diff_text, capture_output=True, text=True, cwd=work_dir,
    )
    return proc.returncode == 0, proc.stderr[:300]


def run_test_in_dir(test_command: str, work_dir: str, timeout: int = 120) -> dict:
    """Run test command and return result dict."""
    try:
        proc = subprocess.run(
            test_command, shell=True,
            capture_output=True, text=True,
            timeout=timeout, cwd=work_dir,
        )
        return {
            "pass": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout_snippet": proc.stdout[:500] if proc.stdout else "",
            "stderr_snippet": proc.stderr[:500] if proc.stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"pass": False, "returncode": -1, "stdout_snippet": "", "stderr_snippet": "TIMEOUT"}
    except Exception as e:
        return {"pass": False, "returncode": -1, "stdout_snippet": "", "stderr_snippet": str(e)[:300]}


def apply_diff_and_test(
    diff_text: str, buggy_dir: str, test_command: str,
    conda_env: str = "bugsinpy",
) -> dict:
    """Apply diff, run test, revert. Returns result dict."""
    full_cmd = (
        f"source /root/miniconda3/etc/profile.d/conda.sh && "
        f"conda activate {conda_env} && "
        f"cd {buggy_dir} && "
        f"{test_command}"
    )

    ok, msg = apply_diff_in_dir(diff_text, buggy_dir)
    if not ok:
        return {
            "test_pass": False,
            "diff_apply_success": False,
            "eval_method": "diff_apply_failed",
            "stdout_snippet": "",
            "stderr_snippet": msg,
        }

    try:
        proc = subprocess.run(
            ["bash", "-c", full_cmd],
            capture_output=True, text=True, timeout=120,
        )
        result = {
            "test_pass": proc.returncode == 0,
            "diff_apply_success": True,
            "eval_method": "test_execution",
            "stdout_snippet": proc.stdout[-500:] if proc.stdout else "",
            "stderr_snippet": proc.stderr[-500:] if proc.stderr else "",
        }
    except subprocess.TimeoutExpired:
        result = {
            "test_pass": False,
            "diff_apply_success": True,
            "eval_method": "test_timeout",
            "stdout_snippet": "",
            "stderr_snippet": "TIMEOUT",
        }
    except Exception as e:
        result = {
            "test_pass": False,
            "diff_apply_success": True,
            "eval_method": "test_error",
            "stdout_snippet": "",
            "stderr_snippet": str(e)[:300],
        }

    rev_ok, rev_msg = revert_diff_in_dir(diff_text, buggy_dir)
    if not rev_ok:
        logger.warning("Failed to revert diff in %s: %s", buggy_dir, rev_msg)

    return result


# ---------------------------------------------------------------------------
# LLM interaction
# ---------------------------------------------------------------------------

def extract_diff_from_response(text: str) -> str:
    """Extract unified diff from LLM response, handling various markdown wrappings."""
    text = text.strip()
    if text.startswith("```diff"):
        text = text[len("```diff"):].strip()
    elif text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    # Claude sometimes adds explanatory text before/after the diff
    # Try to extract just the diff portion
    lines = text.split('\n')
    diff_start = None
    diff_end = None
    for i, line in enumerate(lines):
        if line.startswith('--- ') and diff_start is None:
            diff_start = i
        if diff_start is not None and (line.startswith('--- ') or line.startswith('+++ ') or
                                        line.startswith('@@') or line.startswith(' ') or
                                        line.startswith('+') or line.startswith('-') or
                                        line.strip() == ''):
            diff_end = i
    if diff_start is not None:
        return '\n'.join(lines[diff_start:diff_end + 1]).strip()
    return text


def call_repair_llm_v3(client, model: str, prompt: str) -> Tuple[str, int, int]:
    """Call repair LLM using standalone client."""
    logger.info("  API call: prompt_tokens~%d, model=%s", count_tokens(prompt), model)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=8192,
        timeout=180,
    )
    raw = response.choices[0].message.content
    text = extract_diff_from_response(raw) if raw else ""
    usage = response.usage
    tokens_in = getattr(usage, "prompt_tokens", 0) if usage else 0
    tokens_out = getattr(usage, "completion_tokens", 0) if usage else 0
    if not tokens_in:
        tokens_in = estimate_tokens(prompt)
    if not tokens_out:
        tokens_out = estimate_tokens(text)
    return text, tokens_in, tokens_out


LLM_JUDGE_PROMPT = """\
Given the following bug fix evaluation:

## Ground truth fix (as diff):
```
{ground_truth}
```

## Generated fix (as diff):
```
{generated}
```

Rate the semantic correctness of the generated fix on a scale of 1-5.
1=completely wrong, 2=partially addresses the issue, 3=correct approach but implementation errors, 4=mostly correct with minor differences, 5=functionally identical to ground truth.
Output ONLY a JSON object: {{"score": N, "reasoning": "..."}}
"""

def llm_judge_evaluate(client, model: str, generated_diff: str, gt_patch: str) -> Tuple[int, str]:
    if not generated_diff or not gt_patch:
        return 0, "empty input"
    prompt = LLM_JUDGE_PROMPT.format(
        ground_truth=gt_patch[:3000], generated=generated_diff[:3000],
    )
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=256,
        )
        raw = response.choices[0].message.content
        text = raw.strip() if raw else ""
        match = re.search(r'\{[^}]+\}', text)
        if match:
            data = json.loads(match.group())
            return int(data.get("score", 0)), data.get("reasoning", "")[:500]
        return 0, f"parse_error: {text[:200]}"
    except Exception as e:
        return 0, f"error: {str(e)[:200]}"


# ---------------------------------------------------------------------------
# Build prompt for one instance+condition
# ---------------------------------------------------------------------------

def build_repair_prompt(
    instance_key: str,
    issue: str,
    buggy_files_section: str,
    trace_context: str,
    condition: str,
) -> str:
    trace_section = ""
    if trace_context:
        trace_section = TRACE_SECTION_TEMPLATE.format(
            condition=condition, trace_context=trace_context,
        )
    return DIFF_REPAIR_PROMPT.format(
        issue_description=issue,
        buggy_files_section=buggy_files_section,
        trace_section=trace_section,
    )


# ---------------------------------------------------------------------------
# Instance-level get_instance_info
# ---------------------------------------------------------------------------

def get_instance_info(instance_key: str) -> dict:
    parts = instance_key.rsplit("_", 1)
    project, bug_id = parts[0], int(parts[1])
    setup = BugsInPySetup(WORKSPACE)
    try:
        return setup.setup_instance(project, bug_id)
    except Exception as e:
        logger.warning("setup_instance failed for %s: %s", instance_key, e)
        buggy_dir = os.path.join(WORKSPACE, "instances", instance_key, "buggy")
        return {
            "project": project,
            "bug_id": bug_id,
            "buggy_dir": buggy_dir if os.path.isdir(buggy_dir) else "",
            "test_command": "",
            "issue_description": INSTANCE_DESCRIPTIONS.get(instance_key, f"{project} bug #{bug_id}"),
            "bug_info": {},
        }


# ---------------------------------------------------------------------------
# Oracle baseline
# ---------------------------------------------------------------------------

def run_oracle_baseline(instances: Dict[str, dict], instance_keys: List[str]) -> Dict[str, dict]:
    """Apply ground_truth_patch directly and run test for each instance."""
    results = {}
    for key in instance_keys:
        inst = instances.get(key)
        if not inst:
            results[key] = {"pass": False, "reason": "instance not found"}
            continue
        gt_patch = inst.get("ground_truth_patch", "")
        if not gt_patch:
            results[key] = {"pass": False, "reason": "no ground_truth_patch"}
            continue
        buggy_dir = os.path.join(WORKSPACE, "instances", key, "buggy")
        test_cmd = inst.get("test_command", "")
        if not test_cmd:
            results[key] = {"pass": False, "reason": "no test_command"}
            continue

        logger.info("Oracle baseline: %s", key)
        result = apply_diff_and_test(gt_patch, buggy_dir, test_cmd)
        results[key] = result
        logger.info("  %s: pass=%s method=%s", key, result["test_pass"], result["eval_method"])
    return results


# ---------------------------------------------------------------------------
# Run one instance across all conditions
# ---------------------------------------------------------------------------

def run_instance(
    pipeline: MVPPipeline,
    client,
    model: str,
    instance_key: str,
    instance_data: dict,
    structural_scores: list,
    line_scores: list,
    conditions: List[str],
) -> List[dict]:
    """Run diff-based repair for one instance across conditions."""
    logger.info("Processing %s", instance_key)
    t0 = time.time()

    info = get_instance_info(instance_key)
    issue = info.get("issue_description", "") or INSTANCE_DESCRIPTIONS.get(instance_key, "")
    buggy_dir = os.path.join(WORKSPACE, "instances", instance_key, "buggy")
    test_cmd = instance_data.get("test_command", "") or info.get("test_command", "")
    gt_patch = instance_data.get("ground_truth_patch", "")

    target_files = parse_patch_files(gt_patch) if gt_patch else instance_data.get("changed_files", [])
    if not target_files:
        target_files = instance_data.get("changed_files", [])

    buggy_files_section = build_buggy_files_section(instance_key, target_files)

    events = load_trace_events(instance_key)
    if events:
        full_trace_text, _ = pipeline._format_full_trace(events, max_tokens=16000)
    else:
        full_trace_text = ""
    full_trace_text, _, _ = truncate_trace(full_trace_text, max_tokens=16000)

    structural_keep = build_keep_segments(instance_key, "structural", structural_scores)
    line_keep = build_keep_segments(instance_key, "line", line_scores)
    structural_trace = pipeline._format_filtered_trace(structural_keep) if structural_keep else ""
    line_trace = pipeline._format_filtered_trace(line_keep) if line_keep else ""

    trace_map = {
        "no_trace": "",
        "full_trace": full_trace_text,
        "structural_filtered": structural_trace,
        "line_filtered": line_trace,
    }

    rows = []
    for condition in conditions:
        trace_ctx = trace_map.get(condition, "")
        prompt = build_repair_prompt(
            instance_key, issue, buggy_files_section, trace_ctx, condition,
        )

        time.sleep(2)

        try:
            generated_diff, tokens_in, tokens_out = call_repair_llm_v3(client, model, prompt)
        except Exception as e:
            logger.error("%s/%s LLM error: %s", instance_key, condition, e)
            generated_diff = ""
            tokens_in = estimate_tokens(prompt)
            tokens_out = 0

        if not generated_diff:
            test_result = {
                "test_pass": False,
                "diff_apply_success": False,
                "eval_method": "empty_response",
                "stdout_snippet": "",
                "stderr_snippet": "",
            }
        else:
            test_result = apply_diff_and_test(generated_diff, buggy_dir, test_cmd)

        judge_score, judge_reasoning = llm_judge_evaluate(
            client, model, generated_diff, gt_patch,
        ) if generated_diff else (0, "empty_response")

        rows.append({
            "instance_id": instance_key,
            "condition": condition,
            "test_pass": test_result["test_pass"],
            "diff_apply_success": test_result.get("diff_apply_success", False),
            "eval_method": test_result.get("eval_method", "none"),
            "tokens_input": tokens_in,
            "tokens_output": tokens_out,
            "llm_judge_score": judge_score,
            "llm_judge_reasoning": judge_reasoning[:500],
            "raw_diff": generated_diff[:5000],
            "test_stdout_snippet": test_result.get("stdout_snippet", "")[:300],
            "test_stderr_snippet": test_result.get("stderr_snippet", "")[:300],
        })
        logger.info("  %s/%s: test_pass=%s diff_apply=%s judge=%d tokens=%d+%d",
                     instance_key, condition, test_result["test_pass"],
                     test_result.get("diff_apply_success"), judge_score,
                     tokens_in, tokens_out)

    logger.info("Done %s (%.1fs)", instance_key, time.time() - t0)
    return rows


# ---------------------------------------------------------------------------
# Checkpoint management
# ---------------------------------------------------------------------------

def load_checkpoint(path: str) -> dict:
    if not os.path.isfile(path):
        return {}
    with open(path) as f:
        return json.load(f)


def save_checkpoint(path: str, data: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, default=str)
    os.replace(tmp, path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    default_model = os.environ.get("REPAIR_MODEL", "anthropic/claude-sonnet-4")

    parser = argparse.ArgumentParser(description="Phase 3 v3: strong-model disambiguation (Claude Sonnet 4)")
    parser.add_argument("--repair-model", default=default_model)
    parser.add_argument("--oracle-only", action="store_true", help="Only run oracle baseline")
    parser.add_argument("--conditions", nargs="+", default=CONDITIONS)
    parser.add_argument("--instances", nargs="+", default=TARGET_INSTANCES)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    )

    # --- Startup banner ---
    logger.info("=" * 60)
    logger.info("Phase 3 v3: Strong-model disambiguation")
    logger.info("  Model: %s", args.repair_model)
    logger.info("  Instances: %d (%s)", len(args.instances), ", ".join(args.instances))
    logger.info("  Conditions: %s", ", ".join(args.conditions))
    logger.info("=" * 60)

    instances = load_phase3_instances()
    output_dir = PIPELINE_OUTPUT

    # --- Oracle baseline ---
    logger.info("=== Oracle Baseline ===")
    oracle_results = run_oracle_baseline(instances, args.instances)
    oracle_path = os.path.join(output_dir, "phase3_v3_oracle.json")
    with open(oracle_path, "w") as f:
        json.dump(oracle_results, f, indent=2, default=str)
    oracle_pass = sum(1 for r in oracle_results.values() if r.get("test_pass"))
    logger.info("Oracle: %d/%d pass", oracle_pass, len(oracle_results))
    for key, r in oracle_results.items():
        logger.info("  %s: pass=%s method=%s", key, r.get("test_pass"), r.get("eval_method"))

    if args.oracle_only:
        print(f"\nOracle baseline: {oracle_pass}/{len(oracle_results)} pass")
        for k, r in oracle_results.items():
            print(f"  {k}: {'PASS' if r.get('test_pass') else 'FAIL'} ({r.get('eval_method', '')})")
        return

    # --- Load Phase 2 scores ---
    structural_scores_map = load_phase2_scores("structural")
    line_scores_map = load_phase2_scores("line")

    # --- Checkpoint ---
    checkpoint_path = os.path.join(output_dir, "phase3_v3_checkpoint.json")
    checkpoint = load_checkpoint(checkpoint_path)

    api_key = [REDACTED]"OPENROUTER_API_KEY", "")
    if not api_key:
        print("ERROR: Set OPENROUTER_API_KEY", file=sys.stderr)
        sys.exit(1)

    # --- Create standalone OpenAI client with extended timeout for Claude ---
    from openai import OpenAI
    import httpx
    client = OpenAI(
        api_key=[REDACTED],
        base_url="http://47.94.22.126/v1",
        timeout=httpx.Timeout(connect=30.0, read=180.0, write=30.0, pool=30.0),
        max_retries=3,
    )

    # Pipeline only used for trace formatting helpers
    pipeline = MVPPipeline(
        repair_api_key=[REDACTED],
        repair_model=args.repair_model,
        output_dir=output_dir,
    )

    # --- Run instances ---
    for key in args.instances:
        if key in checkpoint:
            logger.info("Skipping %s (already in checkpoint)", key)
            continue
        inst = instances.get(key)
        if not inst:
            logger.warning("Instance %s not found in phase3_instances.json", key)
            continue

        s_scores = structural_scores_map.get(key, [])
        l_scores = line_scores_map.get(key, [])

        rows = run_instance(
            pipeline, client, args.repair_model,
            key, inst, s_scores, l_scores, args.conditions,
        )
        if rows:
            checkpoint[key] = rows
            save_checkpoint(checkpoint_path, checkpoint)
            logger.info("Checkpoint saved (%d/%d)", len(checkpoint), len(args.instances))

    # --- Collect and output results ---
    all_results = []
    for key in args.instances:
        if key in checkpoint:
            all_results.extend(checkpoint[key])

    # Write CSV
    csv_path = os.path.join(output_dir, "phase3_v3_results.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(all_results)
    logger.info("CSV saved to %s (%d rows)", csv_path, len(all_results))

    # --- Print summary ---
    print(f"\n{'='*60}")
    print(f"Phase 3 v3 Results (model={args.repair_model})")
    print(f"{'='*60}")
    print(f"\nOracle baseline: {oracle_pass}/{len(oracle_results)} pass")

    by_condition = defaultdict(list)
    for r in all_results:
        by_condition[r["condition"]].append(r)

    print(f"\nPer-condition results:")
    for cond in CONDITIONS:
        rows = by_condition.get(cond, [])
        if not rows:
            continue
        n = len(rows)
        test_pass = sum(1 for r in rows if r["test_pass"])
        diff_ok = sum(1 for r in rows if r["diff_apply_success"])
        avg_judge = sum(r.get("llm_judge_score", 0) for r in rows) / max(n, 1)
        print(f"  {cond:25s}: test={test_pass}/{n} diff_apply={diff_ok}/{n} judge={avg_judge:.1f}")

    print(f"\nPer-instance × per-condition:")
    for key in args.instances:
        for r in all_results:
            if r["instance_id"] == key:
                status = "PASS" if r["test_pass"] else "FAIL"
                diff_s = "ok" if r["diff_apply_success"] else "FAIL"
                print(f"  {key:15s} {r['condition']:25s}: {status} (diff={diff_s}, judge={r.get('llm_judge_score', 0)})")


if __name__ == "__main__":
    main()
