#!/usr/bin/env python3
"""Phase 3 v2 test execution evaluator.

For each repair output (unified diff), applies the diff to the buggy version,
runs the BugsInPy test, and records pass/fail.

Handles:
  - Test injection: if the test function doesn't exist in the buggy version,
    extracts test-file changes from the fixed commit and injects them.
  - Ground truth baseline: applies bug_patch.txt to verify test env works.
  - Per-project conda/env isolation via PYTHONPATH.
  - Timeout control (default 60s per test).
  - Full revert after each evaluation to avoid cross-contamination.

Input:  pipeline_output/phase3_v2_checkpoint.json
Output: pipeline_output/test_eval_results.json
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_DIR = "/root/trace_distill_repair"
WORKSPACE = os.path.join(BASE_DIR, "bugsinpy_workspace")
BUGSINPY_DIR = os.path.join(WORKSPACE, "BugsInPy")
PIPELINE_OUTPUT = os.path.join(BASE_DIR, "pipeline_output")

CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]

TIER1_INSTANCES = [
    "black_1", "cookiecutter_1", "cookiecutter_2", "cookiecutter_3",
    "fastapi_2", "httpie_2", "luigi_5", "sanic_2",
    "scrapy_2", "scrapy_7", "tornado_2",
    "youtube-dl_1", "youtube-dl_2", "youtube-dl_5", "youtube-dl_20",
]

CONDA_ACTIVATE = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base"


# ---------------------------------------------------------------------------
# BugsInPy metadata helpers
# ---------------------------------------------------------------------------

def parse_instance_key(key: str) -> Tuple[str, int]:
    parts = key.rsplit("_", 1)
    return parts[0], int(parts[1])


def get_bug_dir(project: str, bug_id: int) -> str:
    return os.path.join(BUGSINPY_DIR, "projects", project, "bugs", str(bug_id))


def read_bug_info(project: str, bug_id: int) -> dict:
    bug_dir = get_bug_dir(project, bug_id)
    info = {}

    info_file = os.path.join(bug_dir, "bug.info")
    if os.path.isfile(info_file):
        with open(info_file) as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    key, _, value = line.partition("=")
                    info[key.strip().lower().replace(" ", "_")] = value.strip().strip('"')

    patch_file = os.path.join(bug_dir, "bug_patch.txt")
    if os.path.isfile(patch_file):
        with open(patch_file) as f:
            info["patch"] = f.read()

    run_test_sh = os.path.join(bug_dir, "run_test.sh")
    if os.path.isfile(run_test_sh):
        with open(run_test_sh) as f:
            lines = [
                l.strip() for l in f
                if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("!")
            ]
        cmds = []
        for line in lines:
            cmd = line
            if cmd.startswith("tox "):
                cmd = "python -m pytest " + cmd[4:]
            cmds.append(cmd)
        if cmds:
            info["test_command"] = " && ".join(cmds)

    return info


def get_buggy_dir(instance_key: str) -> str:
    return os.path.join(WORKSPACE, "instances", instance_key, "buggy")


# ---------------------------------------------------------------------------
# Test injection: extract test-file diffs from fixed commit
# ---------------------------------------------------------------------------

def get_test_injection_diff(instance_key: str, bug_info: dict) -> Optional[str]:
    """If the test function doesn't exist in buggy version, generate a diff
    that adds the test-file changes from the fixed commit."""
    buggy_dir = get_buggy_dir(instance_key)
    if not os.path.isdir(os.path.join(buggy_dir, ".git")):
        return None

    buggy_commit = bug_info.get("buggy_commit_id", "")
    fixed_commit = bug_info.get("fixed_commit_id", "")
    test_file = bug_info.get("test_file", "")

    if not (buggy_commit and fixed_commit and test_file):
        return None

    # Ensure fixed commit is available (may need fetch)
    try:
        check = subprocess.run(
            ["git", "cat-file", "-t", fixed_commit],
            capture_output=True, text=True, timeout=10, cwd=buggy_dir,
        )
        if check.returncode != 0:
            logger.info("  Fetching fixed commit %s for %s...", fixed_commit[:8], instance_key)
            subprocess.run(
                ["git", "fetch", "origin", fixed_commit],
                capture_output=True, text=True, timeout=60, cwd=buggy_dir,
            )
    except Exception:
        pass

    try:
        proc = subprocess.run(
            ["git", "diff", buggy_commit, fixed_commit, "--", test_file],
            capture_output=True, text=True, timeout=30, cwd=buggy_dir,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout
        if proc.returncode != 0:
            logger.warning("git diff failed for %s: %s", instance_key, proc.stderr[:200])
    except Exception as e:
        logger.warning("Failed to get test injection diff for %s: %s", instance_key, e)

    return None


def needs_test_injection(instance_key: str, bug_info: dict) -> bool:
    """Check if the test function specified in run_test.sh exists in the buggy version."""
    test_cmd = bug_info.get("test_command", "")
    test_file = bug_info.get("test_file", "")
    buggy_dir = get_buggy_dir(instance_key)

    if not test_cmd or not test_file:
        return False

    # Extract test function name from command
    # Patterns: "python -m unittest -q tests.test_black.BlackTestCase.test_foo"
    #           "pytest tests/test_foo.py::test_bar"
    func_name = None
    if "::" in test_cmd:
        func_name = test_cmd.split("::")[-1]
    elif "." in test_cmd:
        parts = test_cmd.split()
        for p in parts:
            if "." in p and not p.startswith("-"):
                func_name = p.rsplit(".", 1)[-1]
                break

    if not func_name:
        return False

    test_path = os.path.join(buggy_dir, test_file)
    if not os.path.isfile(test_path):
        return True

    try:
        with open(test_path) as f:
            content = f.read()
        return func_name not in content
    except Exception:
        return True


# ---------------------------------------------------------------------------
# Diff application
# ---------------------------------------------------------------------------

def apply_diff(diff_text: str, work_dir: str, dry_run: bool = False) -> Tuple[bool, str]:
    cmd = ["patch", "-p1", "--no-backup-if-mismatch", "--fuzz=3"]
    if dry_run:
        cmd.append("--dry-run")
    try:
        proc = subprocess.run(
            cmd, input=diff_text, capture_output=True, text=True,
            cwd=work_dir, timeout=30,
        )
        ok = proc.returncode == 0
        msg = (proc.stdout + proc.stderr)[:500]
        return ok, msg
    except Exception as e:
        return False, str(e)[:300]


def revert_diff(diff_text: str, work_dir: str) -> Tuple[bool, str]:
    try:
        proc = subprocess.run(
            ["patch", "-R", "-p1", "--no-backup-if-mismatch", "--fuzz=3"],
            input=diff_text, capture_output=True, text=True,
            cwd=work_dir, timeout=30,
        )
        return proc.returncode == 0, (proc.stdout + proc.stderr)[:300]
    except Exception as e:
        return False, str(e)[:300]


def git_restore_dir(work_dir: str):
    """Hard restore via git checkout -- . as a safety net."""
    try:
        subprocess.run(
            ["git", "checkout", "--", "."],
            capture_output=True, text=True, cwd=work_dir, timeout=30,
        )
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Test execution
# ---------------------------------------------------------------------------

def sanitize_pytest_cmd(cmd: str) -> str:
    """Strip pytest addopts that require unavailable plugins (e.g. pytest-cov)."""
    if "pytest" not in cmd:
        return cmd
    parts = cmd.split(" && ")
    sanitized = []
    for part in parts:
        if "pytest" in part:
            part = re.sub(r"-o\s+'addopts=[^']*'", "", part)
            part += " -o 'addopts='"
        sanitized.append(part)
    return " && ".join(sanitized)


def build_test_command(test_cmd: str, work_dir: str, project: str) -> str:
    """Build the full shell command with env activation."""
    env_vars = ""
    if project == "fastapi":
        env_vars = "PYTHONPATH=. "
    test_cmd = sanitize_pytest_cmd(test_cmd)
    return (
        f"{CONDA_ACTIVATE} && "
        f"cd {work_dir} && "
        f"{env_vars}{test_cmd}"
    )


def run_test(test_cmd: str, work_dir: str, project: str,
             timeout: int = 60) -> dict:
    full_cmd = build_test_command(test_cmd, work_dir, project)
    try:
        proc = subprocess.run(
            ["bash", "-c", full_cmd],
            capture_output=True, text=True, timeout=timeout,
        )
        return {
            "passed": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout": proc.stdout[-2000:] if proc.stdout else "",
            "stderr": proc.stderr[-2000:] if proc.stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"passed": False, "returncode": -1, "stdout": "", "stderr": "TIMEOUT"}
    except Exception as e:
        return {"passed": False, "returncode": -2, "stdout": "", "stderr": str(e)[:500]}


# ---------------------------------------------------------------------------
# Evaluate one instance × one condition
# ---------------------------------------------------------------------------

def evaluate_single(
    instance_key: str,
    condition: str,
    repair_diff: str,
    bug_info: dict,
    test_injection_diff: Optional[str],
    timeout: int = 60,
) -> dict:
    """Apply repair diff, run test, revert. Returns result dict."""
    project, bug_id = parse_instance_key(instance_key)
    buggy_dir = get_buggy_dir(instance_key)
    test_cmd = bug_info.get("test_command", "")

    result = {
        "instance_id": instance_key,
        "condition": condition,
        "test_pass": False,
        "diff_apply_success": False,
        "test_injection_applied": False,
        "eval_method": "unknown",
        "returncode": None,
        "stdout_snippet": "",
        "stderr_snippet": "",
    }

    if not test_cmd:
        result["eval_method"] = "no_test_command"
        return result

    if not os.path.isdir(buggy_dir):
        result["eval_method"] = "no_buggy_dir"
        return result

    if not repair_diff or not repair_diff.strip():
        result["eval_method"] = "empty_diff"
        return result

    # Step 1: Inject test if needed
    if test_injection_diff:
        ok, msg = apply_diff(test_injection_diff, buggy_dir)
        if ok:
            result["test_injection_applied"] = True
        else:
            logger.warning("Test injection failed for %s: %s", instance_key, msg)

    # Step 2: Apply repair diff
    ok, msg = apply_diff(repair_diff, buggy_dir)
    if not ok:
        result["eval_method"] = "diff_apply_failed"
        result["stderr_snippet"] = msg
        # Revert test injection if applied
        if result["test_injection_applied"]:
            revert_diff(test_injection_diff, buggy_dir)
        git_restore_dir(buggy_dir)
        return result

    result["diff_apply_success"] = True

    # Step 3: Run test
    test_result = run_test(test_cmd, buggy_dir, project, timeout)
    result["test_pass"] = test_result["passed"]
    result["returncode"] = test_result["returncode"]
    result["stdout_snippet"] = test_result["stdout"][-500:]
    result["stderr_snippet"] = test_result["stderr"][-500:]
    result["eval_method"] = "test_execution"
    if test_result["returncode"] == -1:
        result["eval_method"] = "test_timeout"

    # Step 4: Revert everything
    revert_diff(repair_diff, buggy_dir)
    if result["test_injection_applied"]:
        revert_diff(test_injection_diff, buggy_dir)
    git_restore_dir(buggy_dir)

    return result


# ---------------------------------------------------------------------------
# Ground truth baseline
# ---------------------------------------------------------------------------

def evaluate_ground_truth(
    instance_key: str,
    bug_info: dict,
    test_injection_diff: Optional[str],
    timeout: int = 60,
) -> dict:
    """Apply the official bug_patch.txt and run test. Must pass for valid env."""
    gt_patch = bug_info.get("patch", "")
    return evaluate_single(
        instance_key, "ground_truth", gt_patch, bug_info,
        test_injection_diff, timeout,
    )


# ---------------------------------------------------------------------------
# Load Phase 3 v2 checkpoint
# ---------------------------------------------------------------------------

def load_checkpoint(path: str) -> dict:
    if not os.path.isfile(path):
        return {}
    with open(path) as f:
        return json.load(f)


def extract_diffs_from_checkpoint(checkpoint: dict) -> Dict[str, Dict[str, str]]:
    """Extract {instance_key: {condition: raw_diff}} from checkpoint."""
    result = {}
    for key, rows in checkpoint.items():
        result[key] = {}
        for row in rows:
            cond = row.get("condition", "")
            diff = row.get("raw_diff", "")
            if cond and diff:
                result[key][cond] = diff
    return result


# ---------------------------------------------------------------------------
# Main evaluation loop
# ---------------------------------------------------------------------------

def run_evaluation(
    instances: List[str],
    conditions: List[str],
    checkpoint_path: str,
    output_path: str,
    timeout: int = 60,
    ground_truth_only: bool = False,
    skip_ground_truth: bool = False,
) -> dict:
    checkpoint = load_checkpoint(checkpoint_path)
    diffs = extract_diffs_from_checkpoint(checkpoint)

    # Load existing results for resume
    existing_results = {}
    if os.path.isfile(output_path):
        with open(output_path) as f:
            existing_results = json.load(f)

    all_results = existing_results.copy()

    for instance_key in instances:
        project, bug_id = parse_instance_key(instance_key)
        bug_info = read_bug_info(project, bug_id)
        buggy_dir = get_buggy_dir(instance_key)

        if not os.path.isdir(buggy_dir):
            logger.warning("Skipping %s: buggy dir not found", instance_key)
            continue

        logger.info("=" * 50)
        logger.info("Evaluating %s", instance_key)
        test_cmd = bug_info.get("test_command", "")
        logger.info("  test_command: %s", test_cmd)

        # Determine if test injection is needed
        test_inj_diff = None
        if needs_test_injection(instance_key, bug_info):
            test_inj_diff = get_test_injection_diff(instance_key, bug_info)
            if test_inj_diff:
                logger.info("  Test injection needed and available (%d bytes)",
                            len(test_inj_diff))
            else:
                logger.warning("  Test injection needed but diff unavailable")

        inst_results = all_results.get(instance_key, {})

        # Ground truth baseline
        if not skip_ground_truth and "ground_truth" not in inst_results:
            logger.info("  [GT] Running ground truth baseline...")
            gt_result = evaluate_ground_truth(
                instance_key, bug_info, test_inj_diff, timeout,
            )
            gt_pass = gt_result["test_pass"]
            logger.info("  [GT] passed=%s method=%s", gt_pass, gt_result["eval_method"])
            if not gt_pass:
                logger.warning("  [GT] stderr: %s", gt_result["stderr_snippet"][:200])
            inst_results["ground_truth"] = gt_result

        if ground_truth_only:
            all_results[instance_key] = inst_results
            save_results(output_path, all_results)
            continue

        # Per-condition evaluation
        inst_diffs = diffs.get(instance_key, {})
        for cond in conditions:
            result_key = cond
            if result_key in inst_results:
                logger.info("  [%s] already evaluated, skipping", cond)
                continue

            repair_diff = inst_diffs.get(cond, "")
            if not repair_diff:
                logger.info("  [%s] no repair diff found in checkpoint", cond)
                inst_results[result_key] = {
                    "instance_id": instance_key,
                    "condition": cond,
                    "test_pass": False,
                    "diff_apply_success": False,
                    "eval_method": "no_repair_output",
                }
                continue

            logger.info("  [%s] Evaluating (diff=%d bytes)...", cond, len(repair_diff))
            result = evaluate_single(
                instance_key, cond, repair_diff, bug_info,
                test_inj_diff, timeout,
            )
            logger.info("  [%s] passed=%s method=%s",
                        cond, result["test_pass"], result["eval_method"])
            inst_results[result_key] = result

        all_results[instance_key] = inst_results
        save_results(output_path, all_results)

    return all_results


def save_results(path: str, results: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2, default=str)


# ---------------------------------------------------------------------------
# Summary / reporting
# ---------------------------------------------------------------------------

def print_summary(results: dict, conditions: List[str]):
    print(f"\n{'='*70}")
    print("TEST EVALUATION SUMMARY")
    print(f"{'='*70}")

    # Per-instance detail
    print(f"\n{'Instance':<20} {'Condition':<25} {'Pass':<6} {'Method':<25} {'RC'}")
    print("-" * 80)

    for key in sorted(results.keys()):
        inst = results[key]
        gt = inst.get("ground_truth", {})
        gt_pass = "Y" if gt.get("test_pass") else "N"
        gt_method = gt.get("eval_method", "n/a")[:25]
        gt_rc = gt.get("returncode", "n/a")
        print(f"{key:<20} {'ground_truth':<25} {gt_pass:<6} {gt_method:<25} {gt_rc}")

        for cond in conditions:
            cr = inst.get(cond, {})
            if not cr:
                continue
            p = "Y" if cr.get("test_pass") else "N"
            m = cr.get("eval_method", "")[:25]
            rc = cr.get("returncode", "n/a")
            print(f"{'':<20} {cond:<25} {p:<6} {m:<25} {rc}")
        print()

    # Aggregates
    print(f"\n{'='*70}")
    print("AGGREGATE PASS RATES")
    print(f"{'='*70}")

    all_instances = sorted(results.keys())
    n = len(all_instances)

    gt_passes = sum(
        1 for k in all_instances
        if results[k].get("ground_truth", {}).get("test_pass")
    )
    print(f"  {'ground_truth':<25} {gt_passes}/{n}")

    for cond in conditions:
        passes = sum(
            1 for k in all_instances
            if results[k].get(cond, {}).get("test_pass")
        )
        diff_ok = sum(
            1 for k in all_instances
            if results[k].get(cond, {}).get("diff_apply_success")
        )
        evaluated = sum(
            1 for k in all_instances
            if cond in results[k]
        )
        print(f"  {cond:<25} {passes}/{evaluated} pass, {diff_ok}/{evaluated} diff_apply")

    # Tier 1 subset
    tier1_in_results = [k for k in all_instances if k in TIER1_INSTANCES]
    if tier1_in_results and len(tier1_in_results) < n:
        print(f"\n  Tier 1 subset ({len(tier1_in_results)} instances):")
        for cond in conditions:
            passes = sum(
                1 for k in tier1_in_results
                if results[k].get(cond, {}).get("test_pass")
            )
            print(f"    {cond:<25} {passes}/{len(tier1_in_results)}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Evaluate Phase 3 v2 repair outputs via test execution",
    )
    parser.add_argument(
        "--instances", nargs="*", default=None,
        help="Instance keys to evaluate (default: Tier 1 instances)",
    )
    parser.add_argument(
        "--conditions", nargs="*", default=CONDITIONS,
        help=f"Conditions to evaluate (default: {CONDITIONS})",
    )
    parser.add_argument(
        "--checkpoint", default=os.path.join(PIPELINE_OUTPUT, "phase3_v2_checkpoint.json"),
        help="Path to Phase 3 v2 checkpoint JSON",
    )
    parser.add_argument(
        "--output", default=os.path.join(PIPELINE_OUTPUT, "test_eval_results.json"),
        help="Output path for evaluation results JSON",
    )
    parser.add_argument(
        "--timeout", type=int, default=60,
        help="Test timeout in seconds (default: 60)",
    )
    parser.add_argument(
        "--ground-truth-only", action="store_true",
        help="Only run ground truth baseline, skip repair evaluation",
    )
    parser.add_argument(
        "--skip-ground-truth", action="store_true",
        help="Skip ground truth baseline, only evaluate repairs",
    )
    parser.add_argument(
        "--instance-filter", choices=["tier1", "all"], default="tier1",
        help="Instance filter when --instances is not specified",
    )
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume from existing results file (skip already-evaluated)",
    )
    parser.add_argument(
        "--clean", action="store_true",
        help="Git-restore all instance buggy dirs before starting",
    )
    args = parser.parse_args()

    if args.instances:
        instances = args.instances
    elif args.instance_filter == "tier1":
        instances = TIER1_INSTANCES
    else:
        instance_dir = os.path.join(WORKSPACE, "instances")
        if os.path.isdir(instance_dir):
            instances = sorted(os.listdir(instance_dir))
        else:
            instances = TIER1_INSTANCES

    if not args.resume and os.path.isfile(args.output) and not args.ground_truth_only:
        logger.info("Existing results file found. Use --resume to continue or delete %s", args.output)

    if args.clean:
        logger.info("Cleaning all buggy dirs via git restore...")
        for key in instances:
            buggy_dir = get_buggy_dir(key)
            if os.path.isdir(buggy_dir):
                git_restore_dir(buggy_dir)
        logger.info("Clean complete")

    logger.info("Evaluating %d instances × %d conditions", len(instances), len(args.conditions))
    logger.info("Checkpoint: %s", args.checkpoint)
    logger.info("Output: %s", args.output)

    results = run_evaluation(
        instances=instances,
        conditions=args.conditions,
        checkpoint_path=args.checkpoint,
        output_path=args.output,
        timeout=args.timeout,
        ground_truth_only=args.ground_truth_only,
        skip_ground_truth=args.skip_ground_truth,
    )

    print_summary(results, args.conditions)

    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
