# code test execution eval — Part 2 of 2

**trace distill repair** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-test-execution-eval.md) · [Structured JSON](../../../sessions/99/990c968e613e605edfa7.json)

## Before a recorded user message

### Tool result

_source line 210 · 2026-05-15T12:59:45.495Z_

<details><summary>↩ Tool result · `toolu_01WopXWmH4SLwwtTeXKxRbiZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/run_test_evaluation.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "844f9a40-0f43-4857-9d6d-9baec8789ec6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/run_test_evaluation.py",
    "oldString": "def get_test_injection_diff(instance_key: str, bug_info: dict) -> Optional[str]:\n    \"\"\"If the test function doesn't exist in buggy version, generate a diff\n    that adds the test-file changes from the fixed commit.\"\"\"\n    buggy_dir = get_buggy_dir(instance_key)\n    if not os.path.isdir(os.path.join(buggy_dir, \".git\")):\n        return None\n\n    buggy_commit = bug_info.get(\"buggy_commit_id\", \"\")\n    fixed_commit = bug_info.get(\"fixed_commit_id\", \"\")\n    test_file = bug_info.get(\"test_file\", \"\")\n\n    if not (buggy_commit and fixed_commit and test_file):\n        return None\n\n    try:\n        proc = subprocess.run(\n            [\"git\", \"diff\", buggy_commit, fixed_commit, \"--\", test_file],\n            capture_output=True, text=True, timeout=30, cwd=buggy_dir,\n        )\n        if proc.returncode == 0 and proc.stdout.strip():\n            return proc.stdout\n    except Exception as e:\n        logger.warning(\"Failed to get test injection diff for %s: %s\", instance_key, e)\n\n    return None",
    "newString": "def get_test_injection_diff(instance_key: str, bug_info: dict) -> Optional[str]:\n    \"\"\"If the test function doesn't exist in buggy version, generate a diff\n    that adds the test-file changes from the fixed commit.\"\"\"\n    buggy_dir = get_buggy_dir(instance_key)\n    if not os.path.isdir(os.path.join(buggy_dir, \".git\")):\n        return None\n\n    buggy_commit = bug_info.get(\"buggy_commit_id\", \"\")\n    fixed_commit = bug_info.get(\"fixed_commit_id\", \"\")\n    test_file = bug_info.get(\"test_file\", \"\")\n\n    if not (buggy_commit and fixed_commit and test_file):\n        return None\n\n    # Ensure fixed commit is available (may need fetch)\n    try:\n        check = subprocess.run(\n            [\"git\", \"cat-file\", \"-t\", fixed_commit],\n            capture_output=True, text=True, timeout=10, cwd=buggy_dir,\n        )\n        if check.returncode != 0:\n            logger.info(\"  Fetching fixed commit %s for %s...\", fixed_commit[:8], instance_key)\n            subprocess.run(\n                [\"git\", \"fetch\", \"origin\", fixed_commit],\n                capture_output=True, text=True, timeout=60, cwd=buggy_dir,\n            )\n    except Exception:\n        pass\n\n    try:\n        proc = subprocess.run(\n            [\"git\", \"diff\", buggy_commit, fixed_commit, \"--\", test_file],\n            capture_output=True, text=True, timeout=30, cwd=buggy_dir,\n        )\n        if proc.returncode == 0 and proc.stdout.strip():\n            return proc.stdout\n        if proc.returncode != 0:\n            logger.warning(\"git diff failed for %s: %s\", instance_key, proc.stderr[:200])\n    except Exception as e:\n        logger.warning(\"Failed to get test injection diff for %s: %s\", instance_key, e)\n\n    return None",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Phase 3 v2 test execution evaluator.\n\nFor each repair output (unified diff), applies the diff to the buggy version,\nruns the BugsInPy test, and records pass/fail.\n\nHandles:\n  - Test injection: if the test function doesn't exist in the buggy version,\n    extracts test-file changes from the fixed commit and injects them.\n  - Ground truth baseline: applies bug_patch.txt to verify test env works.\n  - Per-project conda/env isolation via PYTHONPATH.\n  - Timeout control (default 60s per test).\n  - Full revert after each evaluation to avoid cross-contamination.\n\nInput:  pipeline_output/phase3_v2_checkpoint.json\nOutput: pipeline_output/test_eval_results.json\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport shutil\nimport subprocess\nimport sys\nimport time\nfrom collections import defaultdict\nfrom typing import Any, Dict, List, Optional, Tuple\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s %(levelname)s %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlogger = logging.getLogger(__name__)\n\nBASE_DIR = \"/root/trace_distill_repair\"\nWORKSPACE = os.path.join(BASE_DIR, \"bugsinpy_workspace\")\nBUGSINPY_DIR = os.path.join(WORKSPACE, \"BugsInPy\")\nPIPELINE_OUTPUT = os.path.join(BASE_DIR, \"pipeline_output\")\n\nCONDITIONS = [\"no_trace\", \"full_trace\", \"structural_filtered\", \"line_filtered\"]\n\nTIER1_INSTANCES = [\n    \"black_1\", \"cookiecutter_1\", \"cookiecutter_2\", \"cookiecutter_3\",\n    \"fastapi_2\", \"httpie_2\", \"luigi_5\", \"sanic_2\",\n    \"scrapy_2\", \"scrapy_7\", \"tornado_2\",\n    \"youtube-dl_1\", \"youtube-dl_2\", \"youtube-dl_5\", \"youtube-dl_20\",\n]\n\nCONDA_ACTIVATE = \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\"\n\n\n# ---------------------------------------------------------------------------\n# BugsInPy metadata helpers\n# ---------------------------------------------------------------------------\n\ndef parse_instance_key(key: str) -> Tuple[str, int]:\n    parts = key.rsplit(\"_\", 1)\n    return parts[0], int(parts[1])\n\n\ndef get_bug_dir(project: str, bug_id: int) -> str:\n    return os.path.join(BUGSINPY_DIR, \"projects\", project, \"bugs\", str(bug_id))\n\n\ndef read_bug_info(project: str, bug_id: int) -> dict:\n    bug_dir = get_bug_dir(project, bug_id)\n    info = {}\n\n    info_file = os.path.join(bug_dir, \"bug.info\")\n    if os.path.isfile(info_file):\n        with open(info_file) as f:\n            for line in f:\n                line = line.strip()\n                if \"=\" in line:\n                    key, _, value = line.partition(\"=\")\n                    info[key.strip().lower().replace(\" \", \"_\")] = value.strip().strip('\"')\n\n    patch_file = os.path.join(bug_dir, \"bug_patch.txt\")\n    if os.path.isfile(patch_file):\n        with open(patch_file) as f:\n            info[\"patch\"] = f.read()\n\n    run_test_sh = os.path.join(bug_dir, \"run_test.sh\")\n    if os.path.isfile(run_test_sh):\n        with open(run_test_sh) as f:\n            lines = [\n                l.strip() for l in f\n                if l.strip() and not l.strip().startswith(\"#\") and not l.strip().startswith(\"!\")\n            ]\n        cmds = []\n        for line in lines:\n            cmd = line\n            if cmd.startswith(\"tox \"):\n                cmd = \"python -m pytest \" + cmd[4:]\n            cmds.append(cmd)\n        if cmds:\n            info[\"test_command\"] = \" && \".join(cmds)\n\n    return info\n\n\ndef get_buggy_dir(instance_key: str) -> str:\n    return os.path.join(WORKSPACE, \"instances\", instance_key, \"buggy\")\n\n\n# ---------------------------------------------------------------------------\n# Test injection: extract test-file diffs from fixed commit\n# ---------------------------------------------------------------------------\n\ndef get_test_injection_diff(instance_key: str, bug_info: dict) -> Optional[str]:\n    \"\"\"If the test function doesn't exist in buggy version, generate a diff\n    that adds the test-file changes from the fixed commit.\"\"\"\n    buggy_dir = get_buggy_dir(instance_key)\n    if not os.path.isdir(os.path.join(buggy_dir, \".git\")):\n        return None\n\n    buggy_commit = bug_info.get(\"buggy_commit_id\", \"\")\n    fixed_commit = bug_info.get(\"fixed_commit_id\", \"\")\n    test_file = bug_info.get(\"test_file\", \"\")\n\n    if not (buggy_commit and fixed_commit and test_file):\n        return None\n\n    try:\n        proc = subprocess.run(\n            [\"git\", \"diff\", buggy_commit, fixed_commit, \"--\", test_file],\n            capture_output=True, text=True, timeout=30, cwd=buggy_dir,\n        )\n        if proc.returncode == 0 and proc.stdout.strip():\n            return proc.stdout\n    except Exception as e:\n        logger.warning(\"Failed to get test injection diff for %s: %s\", instance_key, e)\n\n    return None\n\n\ndef needs_test_injection(instance_key: str, bug_info: dict) -> bool:\n    \"\"\"Check if the test function specified in run_test.sh exists in the buggy version.\"\"\"\n    test_cmd = bug_info.get(\"test_command\", \"\")\n    test_file = bug_info.get(\"test_file\", \"\")\n    buggy_dir = get_buggy_dir(instance_key)\n\n    if not test_cmd or not test_file:\n        return False\n\n    # Extract test function name from command\n    # Patterns: \"python -m unittest -q tests.test_black.BlackTestCase.test_foo\"\n    #           \"pytest tests/test_foo.py::test_bar\"\n    func_name = None\n    if \"::\" in test_cmd:\n        func_name = test_cmd.split(\"::\")[-1]\n    elif \".\" in test_cmd:\n        parts = test_cmd.split()\n        for p in parts:\n            if \".\" in p and not p.startswith(\"-\"):\n                func_name = p.rsplit(\".\", 1)[-1]\n                break\n\n    if not func_name:\n        return False\n\n    test_path = os.path.join(buggy_dir, test_file)\n    if not os.path.isfile(test_path):\n        return True\n\n    try:\n        with open(test_path) as f:\n            content = f.read()\n        return func_name not in content\n    except Exception:\n        return True\n\n\n# ---------------------------------------------------------------------------\n# Diff application\n# ---------------------------------------------------------------------------\n\ndef apply_diff(diff_text: str, work_dir: str, dry_run: bool = False) -> Tuple[bool, str]:\n    cmd = [\"patch\", \"-p1\", \"--no-backup-if-mismatch\", \"--fuzz=3\"]\n    if dry_run:\n        cmd.append(\"--dry-run\")\n    try:\n        proc = subprocess.run(\n            cmd, input=diff_text, capture_output=True, text=True,\n            cwd=work_dir, timeout=30,\n        )\n        ok = proc.returncode == 0\n        msg = (proc.stdout + proc.stderr)[:500]\n        return ok, msg\n    except Exception as e:\n        return False, str(e)[:300]\n\n\ndef revert_diff(diff_text: str, work_dir: str) -> Tuple[bool, str]:\n    try:\n        proc = subprocess.run(\n            [\"patch\", \"-R\", \"-p1\", \"--no-backup-if-mismatch\", \"--fuzz=3\"],\n            input=diff_text, capture_output=True, text=True,\n            cwd=work_dir, timeout=30,\n        )\n        return proc.returncode == 0, (proc.stdout + proc.stderr)[:300]\n    except Exception as e:\n        return False, str(e)[:300]\n\n\ndef git_restore_dir(work_dir: str):\n    \"\"\"Hard restore via git checkout -- . as a safety net.\"\"\"\n    try:\n        subprocess.run(\n            [\"git\", \"checkout\", \"--\", \".\"],\n            capture_output=True, text=True, cwd=work_dir, timeout=30,\n        )\n    except Exception:\n        pass\n\n\n# ---------------------------------------------------------------------------\n# Test execution\n# ---------------------------------------------------------------------------\n\ndef sanitize_pytest_cmd(cmd: str) -> str:\n    \"\"\"Strip pytest addopts that require unavailable plugins (e.g. pytest-cov).\"\"\"\n    if \"pytest\" not in cmd:\n        return cmd\n    parts = cmd.split(\" && \")\n    sanitized = []\n    for part in parts:\n        if \"pytest\" in part:\n            part = re.sub(r\"-o\\s+'addopts=[^']*'\", \"\", part)\n            part += \" -o 'addopts='\"\n        sanitized.append(part)\n    return \" && \".join(sanitized)\n\n\ndef build_test_command(test_cmd: str, work_dir: str, project: str) -> str:\n    \"\"\"Build the full shell command with env activation.\"\"\"\n    env_vars = \"\"\n    if project == \"fastapi\":\n        env_vars = \"PYTHONPATH=. \"\n    test_cmd = sanitize_pytest_cmd(test_cmd)\n    return (\n        f\"{CONDA_ACTIVATE} && \"\n        f\"cd {work_dir} && \"\n        f\"{env_vars}{test_cmd}\"\n    )\n\n\ndef run_test(test_cmd: str, work_dir: str, project: str,\n             timeout: int = 60) -> dict:\n    full_cmd = build_test_command(test_cmd, work_dir, project)\n    try:\n        proc = subprocess.run(\n            [\"bash\", \"-c\", full_cmd],\n            capture_output=True, text=True, timeout=timeout,\n        )\n        return {\n            \"passed\": proc.returncode == 0,\n            \"returncode\": proc.returncode,\n            \"stdout\": proc.stdout[-2000:] if proc.stdout else \"\",\n            \"stderr\": proc.stderr[-2000:] if proc.stderr else \"\",\n        }\n    except subprocess.TimeoutExpired:\n        return {\"passed\": False, \"returncode\": -1, \"stdout\": \"\", \"stderr\": \"TIMEOUT\"}\n    except Exception as e:\n        return {\"passed\": False, \"returncode\": -2, \"stdout\": \"\", \"stderr\": str(e)[:500]}\n\n\n# ---------------------------------------------------------------------------\n# Evaluate one instance × one condition\n# ---------------------------------------------------------------------------\n\ndef evaluate_single(\n    instance_key: str,\n    condition: str,\n    repair_diff: str,\n    bug_info: dict,\n    test_injection_diff: Optional[str],\n    timeout: int = 60,\n) -> dict:\n    \"\"\"Apply repair diff, run test, revert. Returns result dict.\"\"\"\n    project, bug_id = parse_instance_key(instance_key)\n    buggy_dir = get_buggy_dir(instance_key)\n    test_cmd = bug_info.get(\"test_command\", \"\")\n\n    result = {\n        \"instance_id\": instance_key,\n        \"condition\": condition,\n        \"test_pass\": False,\n        \"diff_apply_success\": False,\n        \"test_injection_applied\": False,\n        \"eval_method\": \"unknown\",\n        \"returncode\": None,\n        \"stdout_snippet\": \"\",\n        \"stderr_snippet\": \"\",\n    }\n\n    if not test_cmd:\n        result[\"eval_method\"] = \"no_test_command\"\n        return result\n\n    if not os.path.isdir(buggy_dir):\n        result[\"eval_method\"] = \"no_buggy_dir\"\n        return result\n\n    if not repair_diff or not repair_diff.strip():\n        result[\"eval_method\"] = \"empty_diff\"\n        return result\n\n    # Step 1: Inject test if needed\n    if test_injection_diff:\n        ok, msg = apply_diff(test_injection_diff, buggy_dir)\n        if ok:\n            result[\"test_injection_applied\"] = True\n        else:\n            logger.warning(\"Test injection failed for %s: %s\", instance_key, msg)\n\n    # Step 2: Apply repair diff\n    ok, msg = apply_diff(repair_diff, buggy_dir)\n    if not ok:\n        result[\"eval_method\"] = \"diff_apply_failed\"\n        result[\"stderr_snippet\"] = msg\n        # Revert test injection if applied\n        if result[\"test_injection_applied\"]:\n            revert_diff(test_injection_diff, buggy_dir)\n        git_restore_dir(buggy_dir)\n        return result\n\n    result[\"diff_apply_success\"] = True\n\n    # Step 3: Run test\n    test_result = run_test(test_cmd, buggy_dir, project, timeout)\n    result[\"test_pass\"] = test_result[\"passed\"]\n    result[\"returncode\"] = test_result[\"returncode\"]\n    result[\"stdout_snippet\"] = test_result[\"stdout\"][-500:]\n    result[\"stderr_snippet\"] = test_result[\"stderr\"][-500:]\n    result[\"eval_method\"] = \"test_execution\"\n    if test_result[\"returncode\"] == -1:\n        result[\"eval_method\"] = \"test_timeout\"\n\n    # Step 4: Revert everything\n    revert_diff(repair_diff, buggy_dir)\n    if result[\"test_injection_applied\"]:\n        revert_diff(test_injection_diff, buggy_dir)\n    git_restore_dir(buggy_dir)\n\n    return result\n\n\n# ---------------------------------------------------------------------------\n# Ground truth baseline\n# ---------------------------------------------------------------------------\n\ndef evaluate_ground_truth(\n    instance_key: str,\n    bug_info: dict,\n    test_injection_diff: Optional[str],\n    timeout: int = 60,\n) -> dict:\n    \"\"\"Apply the official bug_patch.txt and run test. Must pass for valid env.\"\"\"\n    gt_patch = bug_info.get(\"patch\", \"\")\n    return evaluate_single(\n        instance_key, \"ground_truth\", gt_patch, bug_info,\n        test_injection_diff, timeout,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Load Phase 3 v2 checkpoint\n# ---------------------------------------------------------------------------\n\ndef load_checkpoint(path: str) -> dict:\n    if not os.path.isfile(path):\n        return {}\n    with open(path) as f:\n        return json.load(f)\n\n\ndef extract_diffs_from_checkpoint(checkpoint: dict) -> Dict[str, Dict[str, str]]:\n    \"\"\"Extract {instance_key: {condition: raw_diff}} from checkpoint.\"\"\"\n    result = {}\n    for key, rows in checkpoint.items():\n        result[key] = {}\n        for row in rows:\n            cond = row.get(\"condition\", \"\")\n            diff = row.get(\"raw_diff\", \"\")\n            if cond and diff:\n                result[key][cond] = diff\n    return result\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation loop\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(\n    instances: List[str],\n    conditions: List[str],\n    checkpoint_path: str,\n    output_path: str,\n    timeout: int = 60,\n    ground_truth_only: bool = False,\n    skip_ground_truth: bool = False,\n) -> dict:\n    checkpoint = load_checkpoint(checkpoint_path)\n    diffs = extract_diffs_from_checkpoint(checkpoint)\n\n    # Load existing results for resume\n    existing_results = {}\n    if os.path.isfile(output_path):\n        with open(output_path) as f:\n            existing_results = json.load(f)\n\n    all_results = existing_results.copy()\n\n    for instance_key in instances:\n        project, bug_id = parse_instance_key(instance_key)\n        bug_info = read_bug_info(project, bug_id)\n        buggy_dir = get_buggy_dir(instance_key)\n\n        if not os.path.isdir(buggy_dir):\n            logger.warning(\"Skipping %s: buggy dir not found\", instance_key)\n            continue\n\n        logger.info(\"=\" * 50)\n        logger.info(\"Evaluating %s\", instance_key)\n        test_cmd = bug_info.get(\"test_command\", \"\")\n        logger.info(\"  test_command: %s\", test_cmd)\n\n        # Determine if test injection is needed\n        test_inj_diff = None\n        if needs_test_injection(instance_key, bug_info):\n            test_inj_diff = get_test_injection_diff(instance_key, bug_info)\n            if test_inj_diff:\n                logger.info(\"  Test injection needed and available (%d bytes)\",\n                            len(test_inj_diff))\n            else:\n                logger.warning(\"  Test injection needed but diff unavailable\")\n\n        inst_results = all_results.get(instance_key, {})\n\n        # Ground truth baseline\n        if not skip_ground_truth and \"ground_truth\" not in inst_results:\n            logger.info(\"  [GT] Running ground truth baseline...\")\n            gt_result = evaluate_ground_truth(\n                instance_key, bug_info, test_inj_diff, timeout,\n            )\n            gt_pass = gt_result[\"test_pass\"]\n            logger.info(\"  [GT] passed=%s method=%s\", gt_pass, gt_result[\"eval_method\"])\n            if not gt_pass:\n                logger.warning(\"  [GT] stderr: %s\", gt_result[\"stderr_snippet\"][:200])\n            inst_results[\"ground_truth\"] = gt_result\n\n        if ground_truth_only:\n            all_results[instance_key] = inst_results\n            save_results(output_path, all_results)\n            continue\n\n        # Per-condition evaluation\n        inst_diffs = diffs.get(instance_key, {})\n        for cond in conditions:\n            result_key = cond\n            if result_key in inst_results:\n                logger.info(\"  [%s] already evaluated, skipping\", cond)\n                continue\n\n            repair_diff = inst_diffs.get(cond, \"\")\n            if not repair_diff:\n                logger.info(\"  [%s] no repair diff found in checkpoint\", cond)\n                inst_results[result_key] = {\n                    \"instance_id\": instance_key,\n                    \"condition\": cond,\n                    \"test_pass\": False,\n                    \"diff_apply_success\": False,\n                    \"eval_method\": \"no_repair_output\",\n                }\n                continue\n\n            logger.info(\"  [%s] Evaluating (diff=%d bytes)...\", cond, len(repair_diff))\n            result = evaluate_single(\n                instance_key, cond, repair_diff, bug_info,\n                test_inj_diff, timeout,\n            )\n            logger.info(\"  [%s] passed=%s method=%s\",\n                        cond, result[\"test_pass\"], result[\"eval_method\"])\n            inst_results[result_key] = result\n\n        all_results[instance_key] = inst_results\n        save_results(output_path, all_results)\n\n    return all_results\n\n\ndef save_results(path: str, results: dict):\n    os.makedirs(os.path.dirname(path), exist_ok=True)\n    with open(path, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n\n\n# ---------------------------------------------------------------------------\n# Summary / reporting\n# ---------------------------------------------------------------------------\n\ndef print_summary(results: dict, conditions: List[str]):\n    print(f\"\\n{'='*70}\")\n    print(\"TEST EVALUATION SUMMARY\")\n    print(f\"{'='*70}\")\n\n    # Per-instance detail\n    print(f\"\\n{'Instance':<20} {'Condition':<25} {'Pass':<6} {'Method':<25} {'RC'}\")\n    print(\"-\" * 80)\n\n    for key in sorted(results.keys()):\n        inst = results[key]\n        gt = inst.get(\"ground_truth\", {})\n        gt_pass = \"Y\" if gt.get(\"test_pass\") else \"N\"\n        gt_method = gt.get(\"eval_method\", \"n/a\")[:25]\n        gt_rc = gt.get(\"returncode\", \"n/a\")\n        print(f\"{key:<20} {'ground_truth':<25} {gt_pass:<6} {gt_method:<25} {gt_rc}\")\n\n        for cond in conditions:\n            cr = inst.get(cond, {})\n            if not cr:\n                continue\n            p = \"Y\" if cr.get(\"test_pass\") else \"N\"\n            m = cr.get(\"eval_method\", \"\")[:25]\n            rc = cr.get(\"returncode\", \"n/a\")\n            print(f\"{'':<20} {cond:<25} {p:<6} {m:<25} {rc}\")\n        print()\n\n    # Aggregates\n    print(f\"\\n{'='*70}\")\n    print(\"AGGREGATE PASS RATES\")\n    print(f\"{'='*70}\")\n\n    all_instances = sorted(results.keys())\n    n = len(all_instances)\n\n    gt_passes = sum(\n        1 for k in all_instances\n        if results[k].get(\"ground_truth\", {}).get(\"test_pass\")\n    )\n    print(f\"  {'ground_truth':<25} {gt_passes}/{n}\")\n\n    for cond in conditions:\n        passes = sum(\n            1 for k in all_instances\n            if results[k].get(cond, {}).get(\"test_pass\")\n        )\n        diff_ok = sum(\n            1 for k in all_instances\n            if results[k].get(cond, {}).get(\"diff_apply_success\")\n        )\n        evaluated = sum(\n            1 for k in all_instances\n            if cond in results[k]\n        )\n        print(f\"  {cond:<25} {passes}/{evaluated} pass, {diff_ok}/{evaluated} diff_apply\")\n\n    # Tier 1 subset\n    tier1_in_results = [k for k in all_instances if k in TIER1_INSTANCES]\n    if tier1_in_results and len(tier1_in_results) < n:\n        print(f\"\\n  Tier 1 subset ({len(tier1_in_results)} instances):\")\n        for cond in conditions:\n            passes = sum(\n                1 for k in tier1_in_results\n                if results[k].get(cond, {}).get(\"test_pass\")\n            )\n            print(f\"    {cond:<25} {passes}/{len(tier1_in_results)}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Evaluate Phase 3 v2 repair outputs via test execution\",\n    )\n    parser.add_argument(\n        \"--instances\", nargs=\"*\", default=None,\n        help=\"Instance keys to evaluate (default: Tier 1 instances)\",\n    )\n    parser.add_argument(\n        \"--conditions\", nargs=\"*\", default=CONDITIONS,\n        help=f\"Conditions to evaluate (default: {CONDITIONS})\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=os.path.join(PIPELINE_OUTPUT, \"phase3_v2_checkpoint.json\"),\n        help=\"Path to Phase 3 v2 checkpoint JSON\",\n    )\n    parser.add_argument(\n        \"--output\", default=os.path.join(PIPELINE_OUTPUT, \"test_eval_results.json\"),\n        help=\"Output path for evaluation results JSON\",\n    )\n    parser.add_argument(\n        \"--timeout\", type=int, default=60,\n        help=\"Test timeout in seconds (default: 60)\",\n    )\n    parser.add_argument(\n        \"--ground-truth-only\", action=\"store_true\",\n        help=\"Only run ground truth baseline, skip repair evaluation\",\n    )\n    parser.add_argument(\n        \"--skip-ground-truth\", action=\"store_true\",\n        help=\"Skip ground truth baseline, only evaluate repairs\",\n    )\n    parser.add_argument(\n        \"--instance-filter\", choices=[\"tier1\", \"all\"], default=\"tier1\",\n        help=\"Instance filter when --instances is not specified\",\n    )\n    parser.add_argument(\n        \"--resume\", action=\"store_true\",\n        help=\"Resume from existing results file (skip already-evaluated)\",\n    )\n    parser.add_argument(\n        \"--clean\", action=\"store_true\",\n        help=\"Git-restore all instance buggy dirs before starting\",\n    )\n    args = parser.parse_args()\n\n    if args.instances:\n        instances = args.instances\n    elif args.instance_filter == \"tier1\":\n        instances = TIER1_INSTANCES\n    else:\n        instance_dir = os.path.join(WORKSPACE, \"instances\")\n        if os.path.isdir(instance_dir):\n            instances = sorted(os.listdir(instance_dir))\n        else:\n            instances = TIER1_INSTANCES\n\n    if not args.resume and os.path.isfile(args.output) and not args.ground_truth_only:\n        logger.info(\"Existing results file found. Use --resume to continue or delete %s\", args.output)\n\n    if args.clean:\n        logger.info(\"Cleaning all buggy dirs via git restore...\")\n        for key in instances:\n            buggy_dir = get_buggy_dir(key)\n            if os.path.isdir(buggy_dir):\n                git_restore_dir(buggy_dir)\n        logger.info(\"Clean complete\")\n\n    logger.info(\"Evaluating %d instances × %d conditions\", len(instances), len(args.conditions))\n    logger.info(\"Checkpoint: %s\", args.checkpoint)\n    logger.info(\"Output: %s\", args.output)\n\n    results = run_evaluation(\n        instances=instances,\n        conditions=args.conditions,\n        checkpoint_path=args.checkpoint,\n        output_path=args.output,\n        timeout=args.timeout,\n        ground_truth_only=args.ground_truth_only,\n        skip_ground_truth=args.skip_ground_truth,\n    )\n\n    print_summary(results, args.conditions)\n\n    print(f\"\\nResults saved to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 125,
        "oldLines": 13,
        "newStart": 125,
        "newLines": 30,
        "lines": [
          "     if not (buggy_commit and fixed_commit and test_file):",
          "         return None",
          " ",
          "+    # Ensure fixed commit is available (may need fetch)",
          "     try:",
          "+        check = subprocess.run(",
          "+            [\"git\", \"cat-file\", \"-t\", fixed_commit],",
          "+            capture_output=True, text=True, timeout=10, cwd=buggy_dir,",
          "+        )",
          "+        if check.returncode != 0:",
          "+            logger.info(\"  Fetching fixed commit %s for %s...\", fixed_commit[:8], instance_key)",
          "+            subprocess.run(",
          "+                [\"git\", \"fetch\", \"origin\", fixed_commit],",
          "+                capture_output=True, text=True, timeout=60, cwd=buggy_dir,",
          "+            )",
          "+    except Exception:",
          "+        pass",
          "+",
          "+    try:",
          "         proc = subprocess.run(",
          "             [\"git\", \"diff\", buggy_commit, fixed_commit, \"--\", test_file],",
          "             capture_output=True, text=True, timeout=30, cwd=buggy_dir,",
          "         )",
          "         if proc.returncode == 0 and proc.stdout.strip():",
          "             return proc.stdout",
          "+        if proc.returncode != 0:",
          "+            logger.warning(\"git diff failed for %s: %s\", instance_key, proc.stderr[:200])",
          "     except Exception as e:",
          "         logger.warning(\"Failed to get test injection diff for %s: %s\", instance_key, e)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 211_

Now add the `import re` (it's already imported at the top). Let me verify the file is consistent, then re-upload.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "05b1ca76-f14b-44e9-b8ca-2d7031f9468a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2Gd2XvVK6QkvoBYBVQWZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 119296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 212_

<details open><summary>🔧 Tool call — Bash · `toolu_01FcbY9Q2VchKB5evffj24NG`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/run_test_evaluation.py').read()); print('Syntax OK')\"",
  "description": "Check Python syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "d725cd3e-d009-49ed-a7c4-2b8ed77c0aaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E2Gd2XvVK6QkvoBYBVQWZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 119296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-15T12:59:50.401Z_

<details><summary>↩ Tool result · `toolu_01FcbY9Q2VchKB5evffj24NG`</summary>

```text
Syntax OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "08977a02-d8f5-4c42-a955-193fa9c7f658",
  "tool_use_result": {
    "stdout": "Syntax OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 214_

<details open><summary>🔧 Tool call — Read · `toolu_01SvBNNbNBQJ5b7HrEUvtx8D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/run_test_evaluation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "4f71d0d4-570a-4121-9ea5-9b6e44b824f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C3QFdX66tpqNBN3XnaoC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 120330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 176
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-15T12:59:54.676Z_

<details><summary>↩ Tool result · `toolu_01SvBNNbNBQJ5b7HrEUvtx8D`</summary>

```text
1	#!/usr/bin/env python3
2	"""Phase 3 v2 test execution evaluator.
3	
4	For each repair output (unified diff), applies the diff to the buggy version,
5	runs the BugsInPy test, and records pass/fail.
6	
7	Handles:
8	  - Test injection: if the test function doesn't exist in the buggy version,
9	    extracts test-file changes from the fixed commit and injects them.
10	  - Ground truth baseline: applies bug_patch.txt to verify test env works.
11	  - Per-project conda/env isolation via PYTHONPATH.
12	  - Timeout control (default 60s per test).
13	  - Full revert after each evaluation to avoid cross-contamination.
14	
15	Input:  pipeline_output/phase3_v2_checkpoint.json
16	Output: pipeline_output/test_eval_results.json
17	"""
18	from __future__ import annotations
19	
20	import argparse
21	import json
22	import logging
23	import os
24	import re
25	import shutil
26	import subprocess
27	import sys
28	import time
29	from collections import defaultdict
30	from typing import Any, Dict, List, Optional, Tuple
31	
32	logging.basicConfig(
33	    level=logging.INFO,
34	    format="%(asctime)s %(levelname)s %(message)s",
35	    datefmt="%H:%M:%S",
36	)
37	logger = logging.getLogger(__name__)
38	
39	BASE_DIR = "/root/trace_distill_repair"
40	WORKSPACE = os.path.join(BASE_DIR, "bugsinpy_workspace")
41	BUGSINPY_DIR = os.path.join(WORKSPACE, "BugsInPy")
42	PIPELINE_OUTPUT = os.path.join(BASE_DIR, "pipeline_output")
43	
44	CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]
45	
46	TIER1_INSTANCES = [
47	    "black_1", "cookiecutter_1", "cookiecutter_2", "cookiecutter_3",
48	    "fastapi_2", "httpie_2", "luigi_5", "sanic_2",
49	    "scrapy_2", "scrapy_7", "tornado_2",
50	    "youtube-dl_1", "youtube-dl_2", "youtube-dl_5", "youtube-dl_20",
51	]
52	
53	CONDA_ACTIVATE = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base"
54	
55	
56	# ---------------------------------------------------------------------------
57	# BugsInPy metadata helpers
58	# ---------------------------------------------------------------------------
59	
60	def parse_instance_key(key: str) -> Tuple[str, int]:
61	    parts = key.rsplit("_", 1)
62	    return parts[0], int(parts[1])
63	
64	
65	def get_bug_dir(project: str, bug_id: int) -> str:
66	    return os.path.join(BUGSINPY_DIR, "projects", project, "bugs", str(bug_id))
67	
68	
69	def read_bug_info(project: str, bug_id: int) -> dict:
70	    bug_dir = get_bug_dir(project, bug_id)
71	    info = {}
72	
73	    info_file = os.path.join(bug_dir, "bug.info")
74	    if os.path.isfile(info_file):
75	        with open(info_file) as f:
76	            for line in f:
77	                line = line.strip()
78	                if "=" in line:
79	                    key, _, value = line.partition("=")
80	                    info[key.strip().lower().replace(" ", "_")] = value.strip().strip('"')
81	
82	    patch_file = os.path.join(bug_dir, "bug_patch.txt")
83	    if os.path.isfile(patch_file):
84	        with open(patch_file) as f:
85	            info["patch"] = f.read()
86	
87	    run_test_sh = os.path.join(bug_dir, "run_test.sh")
88	    if os.path.isfile(run_test_sh):
89	        with open(run_test_sh) as f:
90	            lines = [
91	                l.strip() for l in f
92	                if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("!")
93	            ]
94	        cmds = []
95	        for line in lines:
96	            cmd = line
97	            if cmd.startswith("tox "):
98	                cmd = "python -m pytest " + cmd[4:]
99	            cmds.append(cmd)
100	        if cmds:
101	            info["test_command"] = " && ".join(cmds)
102	
103	    return info
104	
105	
106	def get_buggy_dir(instance_key: str) -> str:
107	    return os.path.join(WORKSPACE, "instances", instance_key, "buggy")
108	
109	
110	# ---------------------------------------------------------------------------
111	# Test injection: extract test-file diffs from fixed commit
112	# ---------------------------------------------------------------------------
113	
114	def get_test_injection_diff(instance_key: str, bug_info: dict) -> Optional[str]:
115	    """If the test function doesn't exist in buggy version, generate a diff
116	    that adds the test-file changes from the fixed commit."""
117	    buggy_dir = get_buggy_dir(instance_key)
118	    if not os.path.isdir(os.path.join(buggy_dir, ".git")):
119	        return None
120	
121	    buggy_commit = bug_info.get("buggy_commit_id", "")
122	    fixed_commit = bug_info.get("fixed_commit_id", "")
123	    test_file = bug_info.get("test_file", "")
124	
125	    if not (buggy_commit and fixed_commit and test_file):
126	        return None
127	
128	    # Ensure fixed commit is available (may need fetch)
129	    try:
130	        check = subprocess.run(
131	            ["git", "cat-file", "-t", fixed_commit],
132	            capture_output=True, text=True, timeout=10, cwd=buggy_dir,
133	        )
134	        if check.returncode != 0:
135	            logger.info("  Fetching fixed commit %s for %s...", fixed_commit[:8], instance_key)
136	            subprocess.run(
137	                ["git", "fetch", "origin", fixed_commit],
138	                capture_output=True, text=True, timeout=60, cwd=buggy_dir,
139	            )
140	    except Exception:
141	        pass
142	
143	    try:
144	        proc = subprocess.run(
145	            ["git", "diff", buggy_commit, fixed_commit, "--", test_file],
146	            capture_output=True, text=True, timeout=30, cwd=buggy_dir,
147	        )
148	        if proc.returncode == 0 and proc.stdout.strip():
149	            return proc.stdout
150	        if proc.returncode != 0:
151	            logger.warning("git diff failed for %s: %s", instance_key, proc.stderr[:200])
152	    except Exception as e:
153	        logger.warning("Failed to get test injection diff for %s: %s", instance_key, e)
154	
155	    return None
156	
157	
158	def needs_test_injection(instance_key: str, bug_info: dict) -> bool:
159	    """Check if the test function specified in run_test.sh exists in the buggy version."""
160	    test_cmd = bug_info.get("test_command", "")
161	    test_file = bug_info.get("test_file", "")
162	    buggy_dir = get_buggy_dir(instance_key)
163	
164	    if not test_cmd or not test_file:
165	        return False
166	
167	    # Extract test function name from command
168	    # Patterns: "python -m unittest -q tests.test_black.BlackTestCase.test_foo"
169	    #           "pytest tests/test_foo.py::test_bar"
170	    func_name = None
171	    if "::" in test_cmd:
172	        func_name = test_cmd.split("::")[-1]
173	    elif "." in test_cmd:
174	        parts = test_cmd.split()
175	        for p in parts:
176	            if "." in p and not p.startswith("-"):
177	                func_name = p.rsplit(".", 1)[-1]
178	                break
179	
180	    if not func_name:
181	        return False
182	
183	    test_path = os.path.join(buggy_dir, test_file)
184	    if not os.path.isfile(test_path):
185	        return True
186	
187	    try:
188	        with open(test_path) as f:
189	            content = f.read()
190	        return func_name not in content
191	    except Exception:
192	        return True
193	
194	
195	# ---------------------------------------------------------------------------
196	# Diff application
197	# ---------------------------------------------------------------------------
198	
199	def apply_diff(diff_text: str, work_dir: str, dry_run: bool = False) -> Tuple[bool, str]:
200	    cmd = ["patch", "-p1", "--no-backup-if-mismatch", "--fuzz=3"]
201	    if dry_run:
202	        cmd.append("--dry-run")
203	    try:
204	        proc = subprocess.run(
205	            cmd, input=diff_text, capture_output=True, text=True,
206	            cwd=work_dir, timeout=30,
207	        )
208	        ok = proc.returncode == 0
209	        msg = (proc.stdout + proc.stderr)[:500]
210	        return ok, msg
211	    except Exception as e:
212	        return False, str(e)[:300]
213	
214	
215	def revert_diff(diff_text: str, work_dir: str) -> Tuple[bool, str]:
216	    try:
217	        proc = subprocess.run(
218	            ["patch", "-R", "-p1", "--no-backup-if-mismatch", "--fuzz=3"],
219	            input=diff_text, capture_output=True, text=True,
220	            cwd=work_dir, timeout=30,
221	        )
222	        return proc.returncode == 0, (proc.stdout + proc.stderr)[:300]
223	    except Exception as e:
224	        return False, str(e)[:300]
225	
226	
227	def git_restore_dir(work_dir: str):
228	    """Hard restore via git checkout -- . as a safety net."""
229	    try:
230	        subprocess.run(
231	            ["git", "checkout", "--", "."],
232	            capture_output=True, text=True, cwd=work_dir, timeout=30,
233	        )
234	    except Exception:
235	        pass
236	
237	
238	# ---------------------------------------------------------------------------
239	# Test execution
240	# ---------------------------------------------------------------------------
241	
242	def sanitize_pytest_cmd(cmd: str) -> str:
243	    """Strip pytest addopts that require unavailable plugins (e.g. pytest-cov)."""
244	    if "pytest" not in cmd:
245	        return cmd
246	    parts = cmd.split(" && ")
247	    sanitized = []
248	    for part in parts:
249	        if "pytest" in part:
250	            part = re.sub(r"-o\s+'addopts=[^']*'", "", part)
251	            part += " -o 'addopts='"
252	        sanitized.append(part)
253	    return " && ".join(sanitized)
254	
255	
256	def build_test_command(test_cmd: str, work_dir: str, project: str) -> str:
257	    """Build the full shell command with env activation."""
258	    env_vars = ""
259	    if project == "fastapi":
260	        env_vars = "PYTHONPATH=. "
261	    test_cmd = sanitize_pytest_cmd(test_cmd)
262	    return (
263	        f"{CONDA_ACTIVATE} && "
264	        f"cd {work_dir} && "
265	        f"{env_vars}{test_cmd}"
266	    )
267	
268	
269	def run_test(test_cmd: str, work_dir: str, project: str,
270	             timeout: int = 60) -> dict:
271	    full_cmd = build_test_command(test_cmd, work_dir, project)
272	    try:
273	        proc = subprocess.run(
274	            ["bash", "-c", full_cmd],
275	            capture_output=True, text=True, timeout=timeout,
276	        )
277	        return {
278	            "passed": proc.returncode == 0,
279	            "returncode": proc.returncode,
280	            "stdout": proc.stdout[-2000:] if proc.stdout else "",
281	            "stderr": proc.stderr[-2000:] if proc.stderr else "",
282	        }
283	    except subprocess.TimeoutExpired:
284	        return {"passed": False, "returncode": -1, "stdout": "", "stderr": "TIMEOUT"}
285	    except Exception as e:
286	        return {"passed": False, "returncode": -2, "stdout": "", "stderr": str(e)[:500]}
287	
288	
289	# ---------------------------------------------------------------------------
290	# Evaluate one instance × one condition
291	# ---------------------------------------------------------------------------
292	
293	def evaluate_single(
294	    instance_key: str,
295	    condition: str,
296	    repair_diff: str,
297	    bug_info: dict,
298	    test_injection_diff: Optional[str],
299	    timeout: int = 60,
300	) -> dict:
301	    """Apply repair diff, run test, revert. Returns result dict."""
302	    project, bug_id = parse_instance_key(instance_key)
303	    buggy_dir = get_buggy_dir(instance_key)
304	    test_cmd = bug_info.get("test_command", "")
305	
306	    result = {
307	        "instance_id": instance_key,
308	        "condition": condition,
309	        "test_pass": False,
310	        "diff_apply_success": False,
311	        "test_injection_applied": False,
312	        "eval_method": "unknown",
313	        "returncode": None,
314	        "stdout_snippet": "",
315	        "stderr_snippet": "",
316	    }
317	
318	    if not test_cmd:
319	        result["eval_method"] = "no_test_command"
320	        return result
321	
322	    if not os.path.isdir(buggy_dir):
323	        result["eval_method"] = "no_buggy_dir"
324	        return result
325	
326	    if not repair_diff or not repair_diff.strip():
327	        result["eval_method"] = "empty_diff"
328	        return result
329	
330	    # Step 1: Inject test if needed
331	    if test_injection_diff:
332	        ok, msg = apply_diff(test_injection_diff, buggy_dir)
333	        if ok:
334	            result["test_injection_applied"] = True
335	        else:
336	            logger.warning("Test injection failed for %s: %s", instance_key, msg)
337	
338	    # Step 2: Apply repair diff
339	    ok, msg = apply_diff(repair_diff, buggy_dir)
340	    if not ok:
341	        result["eval_method"] = "diff_apply_failed"
342	        result["stderr_snippet"] = msg
343	        # Revert test injection if applied
344	        if result["test_injection_applied"]:
345	            revert_diff(test_injection_diff, buggy_dir)
346	        git_restore_dir(buggy_dir)
347	        return result
348	
349	    result["diff_apply_success"] = True
350	
351	    # Step 3: Run test
352	    test_result = run_test(test_cmd, buggy_dir, project, timeout)
353	    result["test_pass"] = test_result["passed"]
354	    result["returncode"] = test_result["returncode"]
355	    result["stdout_snippet"] = test_result["stdout"][-500:]
356	    result["stderr_snippet"] = test_result["stderr"][-500:]
357	    result["eval_method"] = "test_execution"
358	    if test_result["returncode"] == -1:
359	        result["eval_method"] = "test_timeout"
360	
361	    # Step 4: Revert everything
362	    revert_diff(repair_diff, buggy_dir)
363	    if result["test_injection_applied"]:
364	        revert_diff(test_injection_diff, buggy_dir)
365	    git_restore_dir(buggy_dir)
366	
367	    return result
368	
369	
370	# ---------------------------------------------------------------------------
371	# Ground truth baseline
372	# ---------------------------------------------------------------------------
373	
374	def evaluate_ground_truth(
375	    instance_key: str,
376	    bug_info: dict,
377	    test_injection_diff: Optional[str],
378	    timeout: int = 60,
379	) -> dict:
380	    """Apply the official bug_patch.txt and run test. Must pass for valid env."""
381	    gt_patch = bug_info.get("patch", "")
382	    return evaluate_single(
383	        instance_key, "ground_truth", gt_patch, bug_info,
384	        test_injection_diff, timeout,
385	    )
386	
387	
388	# ---------------------------------------------------------------------------
389	# Load Phase 3 v2 checkpoint
390	# ---------------------------------------------------------------------------
391	
392	def load_checkpoint(path: str) -> dict:
393	    if not os.path.isfile(path):
394	        return {}
395	    with open(path) as f:
396	        return json.load(f)
397	
398	
399	def extract_diffs_from_checkpoint(checkpoint: dict) -> Dict[str, Dict[str, str]]:
400	    """Extract {instance_key: {condition: raw_diff}} from checkpoint."""
401	    result = {}
402	    for key, rows in checkpoint.items():
403	        result[key] = {}
404	        for row in rows:
405	            cond = row.get("condition", "")
406	            diff = row.get("raw_diff", "")
407	            if cond and diff:
408	                result[key][cond] = diff
409	    return result
410	
411	
412	# ---------------------------------------------------------------------------
413	# Main evaluation loop
414	# ---------------------------------------------------------------------------
415	
416	def run_evaluation(
417	    instances: List[str],
418	    conditions: List[str],
419	    checkpoint_path: str,
420	    output_path: str,
421	    timeout: int = 60,
422	    ground_truth_only: bool = False,
423	    skip_ground_truth: bool = False,
424	) -> dict:
425	    checkpoint = load_checkpoint(checkpoint_path)
426	    diffs = extract_diffs_from_checkpoint(checkpoint)
427	
428	    # Load existing results for resume
429	    existing_results = {}
430	    if os.path.isfile(output_path):
431	        with open(output_path) as f:
432	            existing_results = json.load(f)
433	
434	    all_results = existing_results.copy()
435	
436	    for instance_key in instances:
437	        project, bug_id = parse_instance_key(instance_key)
438	        bug_info = read_bug_info(project, bug_id)
439	        buggy_dir = get_buggy_dir(instance_key)
440	
441	        if not os.path.isdir(buggy_dir):
442	            logger.warning("Skipping %s: buggy dir not found", instance_key)
443	            continue
444	
445	        logger.info("=" * 50)
446	        logger.info("Evaluating %s", instance_key)
447	        test_cmd = bug_info.get("test_command", "")
448	        logger.info("  test_command: %s", test_cmd)
449	
450	        # Determine if test injection is needed
451	        test_inj_diff = None
452	        if needs_test_injection(instance_key, bug_info):
453	            test_inj_diff = get_test_injection_diff(instance_key, bug_info)
454	            if test_inj_diff:
455	                logger.info("  Test injection needed and available (%d bytes)",
456	                            len(test_inj_diff))
457	            else:
458	                logger.warning("  Test injection needed but diff unavailable")
459	
460	        inst_results = all_results.get(instance_key, {})
461	
462	        # Ground truth baseline
463	        if not skip_ground_truth and "ground_truth" not in inst_results:
464	            logger.info("  [GT] Running ground truth baseline...")
465	            gt_result = evaluate_ground_truth(
466	                instance_key, bug_info, test_inj_diff, timeout,
467	            )
468	            gt_pass = gt_result["test_pass"]
469	            logger.info("  [GT] passed=%s method=%s", gt_pass, gt_result["eval_method"])
470	            if not gt_pass:
471	                logger.warning("  [GT] stderr: %s", gt_result["stderr_snippet"][:200])
472	            inst_results["ground_truth"] = gt_result
473	
474	        if ground_truth_only:
475	            all_results[instance_key] = inst_results
476	            save_results(output_path, all_results)
477	            continue
478	
479	        # Per-condition evaluation
480	        inst_diffs = diffs.get(instance_key, {})
481	        for cond in conditions:
482	            result_key = cond
483	            if result_key in inst_results:
484	                logger.info("  [%s] already evaluated, skipping", cond)
485	                continue
486	
487	            repair_diff = inst_diffs.get(cond, "")
488	            if not repair_diff:
489	                logger.info("  [%s] no repair diff found in checkpoint", cond)
490	                inst_results[result_key] = {
491	                    "instance_id": instance_key,
492	                    "condition": cond,
493	                    "test_pass": False,
494	                    "diff_apply_success": False,
495	                    "eval_method": "no_repair_output",
496	                }
497	                continue
498	
499	            logger.info("  [%s] Evaluating (diff=%d bytes)...", cond, len(repair_diff))
500	            result = evaluate_single(
501	                instance_key, cond, repair_diff, bug_info,
502	                test_inj_diff, timeout,
503	            )
504	            logger.info("  [%s] passed=%s method=%s",
505	                        cond, result["test_pass"], result["eval_method"])
506	            inst_results[result_key] = result
507	
508	        all_results[instance_key] = inst_results
509	        save_results(output_path, all_results)
510	
511	    return all_results
512	
513	
514	def save_results(path: str, results: dict):
515	    os.makedirs(os.path.dirname(path), exist_ok=True)
516	    with open(path, "w") as f:
517	        json.dump(results, f, indent=2, default=str)
518	
519	
520	# ---------------------------------------------------------------------------
521	# Summary / reporting
522	# ---------------------------------------------------------------------------
523	
524	def print_summary(results: dict, conditions: List[str]):
525	    print(f"\n{'='*70}")
526	    print("TEST EVALUATION SUMMARY")
527	    print(f"{'='*70}")
528	
529	    # Per-instance detail
530	    print(f"\n{'Instance':<20} {'Condition':<25} {'Pass':<6} {'Method':<25} {'RC'}")
531	    print("-" * 80)
532	
533	    for key in sorted(results.keys()):
534	        inst = results[key]
535	        gt = inst.get("ground_truth", {})
536	        gt_pass = "Y" if gt.get("test_pass") else "N"
537	        gt_method = gt.get("eval_method", "n/a")[:25]
538	        gt_rc = gt.get("returncode", "n/a")
539	        print(f"{key:<20} {'ground_truth':<25} {gt_pass:<6} {gt_method:<25} {gt_rc}")
540	
541	        for cond in conditions:
542	            cr = inst.get(cond, {})
543	            if not cr:
544	                continue
545	            p = "Y" if cr.get("test_pass") else "N"
546	            m = cr.get("eval_method", "")[:25]
547	            rc = cr.get("returncode", "n/a")
548	            print(f"{'':<20} {cond:<25} {p:<6} {m:<25} {rc}")
549	        print()
550	
551	    # Aggregates
552	    print(f"\n{'='*70}")
553	    print("AGGREGATE PASS RATES")
554	    print(f"{'='*70}")
555	
556	    all_instances = sorted(results.keys())
557	    n = len(all_instances)
558	
559	    gt_passes = sum(
560	        1 for k in all_instances
561	        if results[k].get("ground_truth", {}).get("test_pass")
562	    )
563	    print(f"  {'ground_truth':<25} {gt_passes}/{n}")
564	
565	    for cond in conditions:
566	        passes = sum(
567	            1 for k in all_instances
568	            if results[k].get(cond, {}).get("test_pass")
569	        )
570	        diff_ok = sum(
571	            1 for k in all_instances
572	            if results[k].get(cond, {}).get("diff_apply_success")
573	        )
574	        evaluated = sum(
575	            1 for k in all_instances
576	            if cond in results[k]
577	        )
578	        print(f"  {cond:<25} {passes}/{evaluated} pass, {diff_ok}/{evaluated} diff_apply")
579	
580	    # Tier 1 subset
581	    tier1_in_results = [k for k in all_instances if k in TIER1_INSTANCES]
582	    if tier1_in_results and len(tier1_in_results) < n:
583	        print(f"\n  Tier 1 subset ({len(tier1_in_results)} instances):")
584	        for cond in conditions:
585	            passes = sum(
586	                1 for k in tier1_in_results
587	                if results[k].get(cond, {}).get("test_pass")
588	            )
589	            print(f"    {cond:<25} {passes}/{len(tier1_in_results)}")
590	
591	
592	# ---------------------------------------------------------------------------
593	# CLI
594	# ---------------------------------------------------------------------------
595	
596	def main():
597	    parser = argparse.ArgumentParser(
598	        description="Evaluate Phase 3 v2 repair outputs via test execution",
599	    )
600	    parser.add_argument(
601	        "--instances", nargs="*", default=None,
602	        help="Instance keys to evaluate (default: Tier 1 instances)",
603	    )
604	    parser.add_argument(
605	        "--conditions", nargs="*", default=CONDITIONS,
606	        help=f"Conditions to evaluate (default: {CONDITIONS})",
607	    )
608	    parser.add_argument(
609	        "--checkpoint", default=os.path.join(PIPELINE_OUTPUT, "phase3_v2_checkpoint.json"),
610	        help="Path to Phase 3 v2 checkpoint JSON",
611	    )
612	    parser.add_argument(
613	        "--output", default=os.path.join(PIPELINE_OUTPUT, "test_eval_results.json"),
614	        help="Output path for evaluation results JSON",
615	    )
616	    parser.add_argument(
617	        "--timeout", type=int, default=60,
618	        help="Test timeout in seconds (default: 60)",
619	    )
620	    parser.add_argument(
621	        "--ground-truth-only", action="store_true",
622	        help="Only run ground truth baseline, skip repair evaluation",
623	    )
624	    parser.add_argument(
625	        "--skip-ground-truth", action="store_true",
626	        help="Skip ground truth baseline, only evaluate repairs",
627	    )
628	    parser.add_argument(
629	        "--instance-filter", choices=["tier1", "all"], default="tier1",
630	        help="Instance filter when --instances is not specified",
631	    )
632	    parser.add_argument(
633	        "--resume", action="store_true",
634	        help="Resume from existing results file (skip already-evaluated)",
635	    )
636	    parser.add_argument(
637	        "--clean", action="store_true",
638	        help="Git-restore all instance buggy dirs before starting",
639	    )
640	    args = parser.parse_args()
641	
642	    if args.instances:
643	        instances = args.instances
644	    elif args.instance_filter == "tier1":
645	        instances = TIER1_INSTANCES
646	    else:
647	        instance_dir = os.path.join(WORKSPACE, "instances")
648	        if os.path.isdir(instance_dir):
649	            instances = sorted(os.listdir(instance_dir))
650	        else:
651	            instances = TIER1_INSTANCES
652	
653	    if not args.resume and os.path.isfile(args.output) and not args.ground_truth_only:
654	        logger.info("Existing results file found. Use --resume to continue or delete %s", args.output)
655	
656	    if args.clean:
657	        logger.info("Cleaning all buggy dirs via git restore...")
658	        for key in instances:
659	            buggy_dir = get_buggy_dir(key)
660	            if os.path.isdir(buggy_dir):
661	                git_restore_dir(buggy_dir)
662	        logger.info("Clean complete")
663	
664	    logger.info("Evaluating %d instances × %d conditions", len(instances), len(args.conditions))
665	    logger.info("Checkpoint: %s", args.checkpoint)
666	    logger.info("Output: %s", args.output)
667	
668	    results = run_evaluation(
669	        instances=instances,
670	        conditions=args.conditions,
671	        checkpoint_path=args.checkpoint,
672	        output_path=args.output,
673	        timeout=args.timeout,
674	        ground_truth_only=args.ground_truth_only,
675	        skip_ground_truth=args.skip_ground_truth,
676	    )
677	
678	    print_summary(results, args.conditions)
679	
680	    print(f"\nResults saved to {args.output}")
681	
682	
683	if __name__ == "__main__":
684	    main()
685	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "cd7f5b36-759a-44df-8de0-aa85266e224b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/run_test_evaluation.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Phase 3 v2 test execution evaluator.\n\nFor each repair output (unified diff), applies the diff to the buggy version,\nruns the BugsInPy test, and records pass/fail.\n\nHandles:\n  - Test injection: if the test function doesn't exist in the buggy version,\n    extracts test-file changes from the fixed commit and injects them.\n  - Ground truth baseline: applies bug_patch.txt to verify test env works.\n  - Per-project conda/env isolation via PYTHONPATH.\n  - Timeout control (default 60s per test).\n  - Full revert after each evaluation to avoid cross-contamination.\n\nInput:  pipeline_output/phase3_v2_checkpoint.json\nOutput: pipeline_output/test_eval_results.json\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport re\nimport shutil\nimport subprocess\nimport sys\nimport time\nfrom collections import defaultdict\nfrom typing import Any, Dict, List, Optional, Tuple\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s %(levelname)s %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlogger = logging.getLogger(__name__)\n\nBASE_DIR = \"/root/trace_distill_repair\"\nWORKSPACE = os.path.join(BASE_DIR, \"bugsinpy_workspace\")\nBUGSINPY_DIR = os.path.join(WORKSPACE, \"BugsInPy\")\nPIPELINE_OUTPUT = os.path.join(BASE_DIR, \"pipeline_output\")\n\nCONDITIONS = [\"no_trace\", \"full_trace\", \"structural_filtered\", \"line_filtered\"]\n\nTIER1_INSTANCES = [\n    \"black_1\", \"cookiecutter_1\", \"cookiecutter_2\", \"cookiecutter_3\",\n    \"fastapi_2\", \"httpie_2\", \"luigi_5\", \"sanic_2\",\n    \"scrapy_2\", \"scrapy_7\", \"tornado_2\",\n    \"youtube-dl_1\", \"youtube-dl_2\", \"youtube-dl_5\", \"youtube-dl_20\",\n]\n\nCONDA_ACTIVATE = \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\"\n\n\n# ---------------------------------------------------------------------------\n# BugsInPy metadata helpers\n# ---------------------------------------------------------------------------\n\ndef parse_instance_key(key: str) -> Tuple[str, int]:\n    parts = key.rsplit(\"_\", 1)\n    return parts[0], int(parts[1])\n\n\ndef get_bug_dir(project: str, bug_id: int) -> str:\n    return os.path.join(BUGSINPY_DIR, \"projects\", project, \"bugs\", str(bug_id))\n\n\ndef read_bug_info(project: str, bug_id: int) -> dict:\n    bug_dir = get_bug_dir(project, bug_id)\n    info = {}\n\n    info_file = os.path.join(bug_dir, \"bug.info\")\n    if os.path.isfile(info_file):\n        with open(info_file) as f:\n            for line in f:\n                line = line.strip()\n                if \"=\" in line:\n                    key, _, value = line.partition(\"=\")\n                    info[key.strip().lower().replace(\" \", \"_\")] = value.strip().strip('\"')\n\n    patch_file = os.path.join(bug_dir, \"bug_patch.txt\")\n    if os.path.isfile(patch_file):\n        with open(patch_file) as f:\n            info[\"patch\"] = f.read()\n\n    run_test_sh = os.path.join(bug_dir, \"run_test.sh\")\n    if os.path.isfile(run_test_sh):\n        with open(run_test_sh) as f:\n            lines = [\n                l.strip() for l in f\n                if l.strip() and not l.strip().startswith(\"#\") and not l.strip().startswith(\"!\")\n            ]\n        cmds = []\n        for line in lines:\n            cmd = line\n            if cmd.startswith(\"tox \"):\n                cmd = \"python -m pytest \" + cmd[4:]\n            cmds.append(cmd)\n        if cmds:\n            info[\"test_command\"] = \" && \".join(cmds)\n\n    return info\n\n\ndef get_buggy_dir(instance_key: str) -> str:\n    return os.path.join(WORKSPACE, \"instances\", instance_key, \"buggy\")\n\n\n# ---------------------------------------------------------------------------\n# Test injection: extract test-file diffs from fixed commit\n# ---------------------------------------------------------------------------\n\ndef get_test_injection_diff(instance_key: str, bug_info: dict) -> Optional[str]:\n    \"\"\"If the test function doesn't exist in buggy version, generate a diff\n    that adds the test-file changes from the fixed commit.\"\"\"\n    buggy_dir = get_buggy_dir(instance_key)\n    if not os.path.isdir(os.path.join(buggy_dir, \".git\")):\n        return None\n\n    buggy_commit = bug_info.get(\"buggy_commit_id\", \"\")\n    fixed_commit = bug_info.get(\"fixed_commit_id\", \"\")\n    test_file = bug_info.get(\"test_file\", \"\")\n\n    if not (buggy_commit and fixed_commit and test_file):\n        return None\n\n    # Ensure fixed commit is available (may need fetch)\n    try:\n        check = subprocess.run(\n            [\"git\", \"cat-file\", \"-t\", fixed_commit],\n            capture_output=True, text=True, timeout=10, cwd=buggy_dir,\n        )\n        if check.returncode != 0:\n            logger.info(\"  Fetching fixed commit %s for %s...\", fixed_commit[:8], instance_key)\n            subprocess.run(\n                [\"git\", \"fetch\", \"origin\", fixed_commit],\n                capture_output=True, text=True, timeout=60, cwd=buggy_dir,\n            )\n    except Exception:\n        pass\n\n    try:\n        proc = subprocess.run(\n            [\"git\", \"diff\", buggy_commit, fixed_commit, \"--\", test_file],\n            capture_output=True, text=True, timeout=30, cwd=buggy_dir,\n        )\n        if proc.returncode == 0 and proc.stdout.strip():\n            return proc.stdout\n        if proc.returncode != 0:\n            logger.warning(\"git diff failed for %s: %s\", instance_key, proc.stderr[:200])\n    except Exception as e:\n        logger.warning(\"Failed to get test injection diff for %s: %s\", instance_key, e)\n\n    return None\n\n\ndef needs_test_injection(instance_key: str, bug_info: dict) -> bool:\n    \"\"\"Check if the test function specified in run_test.sh exists in the buggy version.\"\"\"\n    test_cmd = bug_info.get(\"test_command\", \"\")\n    test_file = bug_info.get(\"test_file\", \"\")\n    buggy_dir = get_buggy_dir(instance_key)\n\n    if not test_cmd or not test_file:\n        return False\n\n    # Extract test function name from command\n    # Patterns: \"python -m unittest -q tests.test_black.BlackTestCase.test_foo\"\n    #           \"pytest tests/test_foo.py::test_bar\"\n    func_name = None\n    if \"::\" in test_cmd:\n        func_name = test_cmd.split(\"::\")[-1]\n    elif \".\" in test_cmd:\n        parts = test_cmd.split()\n        for p in parts:\n            if \".\" in p and not p.startswith(\"-\"):\n                func_name = p.rsplit(\".\", 1)[-1]\n                break\n\n    if not func_name:\n        return False\n\n    test_path = os.path.join(buggy_dir, test_file)\n    if not os.path.isfile(test_path):\n        return True\n\n    try:\n        with open(test_path) as f:\n            content = f.read()\n        return func_name not in content\n    except Exception:\n        return True\n\n\n# ---------------------------------------------------------------------------\n# Diff application\n# ---------------------------------------------------------------------------\n\ndef apply_diff(diff_text: str, work_dir: str, dry_run: bool = False) -> Tuple[bool, str]:\n    cmd = [\"patch\", \"-p1\", \"--no-backup-if-mismatch\", \"--fuzz=3\"]\n    if dry_run:\n        cmd.append(\"--dry-run\")\n    try:\n        proc = subprocess.run(\n            cmd, input=diff_text, capture_output=True, text=True,\n            cwd=work_dir, timeout=30,\n        )\n        ok = proc.returncode == 0\n        msg = (proc.stdout + proc.stderr)[:500]\n        return ok, msg\n    except Exception as e:\n        return False, str(e)[:300]\n\n\ndef revert_diff(diff_text: str, work_dir: str) -> Tuple[bool, str]:\n    try:\n        proc = subprocess.run(\n            [\"patch\", \"-R\", \"-p1\", \"--no-backup-if-mismatch\", \"--fuzz=3\"],\n            input=diff_text, capture_output=True, text=True,\n            cwd=work_dir, timeout=30,\n        )\n        return proc.returncode == 0, (proc.stdout + proc.stderr)[:300]\n    except Exception as e:\n        return False, str(e)[:300]\n\n\ndef git_restore_dir(work_dir: str):\n    \"\"\"Hard restore via git checkout -- . as a safety net.\"\"\"\n    try:\n        subprocess.run(\n            [\"git\", \"checkout\", \"--\", \".\"],\n            capture_output=True, text=True, cwd=work_dir, timeout=30,\n        )\n    except Exception:\n        pass\n\n\n# ---------------------------------------------------------------------------\n# Test execution\n# ---------------------------------------------------------------------------\n\ndef sanitize_pytest_cmd(cmd: str) -> str:\n    \"\"\"Strip pytest addopts that require unavailable plugins (e.g. pytest-cov).\"\"\"\n    if \"pytest\" not in cmd:\n        return cmd\n    parts = cmd.split(\" && \")\n    sanitized = []\n    for part in parts:\n        if \"pytest\" in part:\n            part = re.sub(r\"-o\\s+'addopts=[^']*'\", \"\", part)\n            part += \" -o 'addopts='\"\n        sanitized.append(part)\n    return \" && \".join(sanitized)\n\n\ndef build_test_command(test_cmd: str, work_dir: str, project: str) -> str:\n    \"\"\"Build the full shell command with env activation.\"\"\"\n    env_vars = \"\"\n    if project == \"fastapi\":\n        env_vars = \"PYTHONPATH=. \"\n    test_cmd = sanitize_pytest_cmd(test_cmd)\n    return (\n        f\"{CONDA_ACTIVATE} && \"\n        f\"cd {work_dir} && \"\n        f\"{env_vars}{test_cmd}\"\n    )\n\n\ndef run_test(test_cmd: str, work_dir: str, project: str,\n             timeout: int = 60) -> dict:\n    full_cmd = build_test_command(test_cmd, work_dir, project)\n    try:\n        proc = subprocess.run(\n            [\"bash\", \"-c\", full_cmd],\n            capture_output=True, text=True, timeout=timeout,\n        )\n        return {\n            \"passed\": proc.returncode == 0,\n            \"returncode\": proc.returncode,\n            \"stdout\": proc.stdout[-2000:] if proc.stdout else \"\",\n            \"stderr\": proc.stderr[-2000:] if proc.stderr else \"\",\n        }\n    except subprocess.TimeoutExpired:\n        return {\"passed\": False, \"returncode\": -1, \"stdout\": \"\", \"stderr\": \"TIMEOUT\"}\n    except Exception as e:\n        return {\"passed\": False, \"returncode\": -2, \"stdout\": \"\", \"stderr\": str(e)[:500]}\n\n\n# ---------------------------------------------------------------------------\n# Evaluate one instance × one condition\n# ---------------------------------------------------------------------------\n\ndef evaluate_single(\n    instance_key: str,\n    condition: str,\n    repair_diff: str,\n    bug_info: dict,\n    test_injection_diff: Optional[str],\n    timeout: int = 60,\n) -> dict:\n    \"\"\"Apply repair diff, run test, revert. Returns result dict.\"\"\"\n    project, bug_id = parse_instance_key(instance_key)\n    buggy_dir = get_buggy_dir(instance_key)\n    test_cmd = bug_info.get(\"test_command\", \"\")\n\n    result = {\n        \"instance_id\": instance_key,\n        \"condition\": condition,\n        \"test_pass\": False,\n        \"diff_apply_success\": False,\n        \"test_injection_applied\": False,\n        \"eval_method\": \"unknown\",\n        \"returncode\": None,\n        \"stdout_snippet\": \"\",\n        \"stderr_snippet\": \"\",\n    }\n\n    if not test_cmd:\n        result[\"eval_method\"] = \"no_test_command\"\n        return result\n\n    if not os.path.isdir(buggy_dir):\n        result[\"eval_method\"] = \"no_buggy_dir\"\n        return result\n\n    if not repair_diff or not repair_diff.strip():\n        result[\"eval_method\"] = \"empty_diff\"\n        return result\n\n    # Step 1: Inject test if needed\n    if test_injection_diff:\n        ok, msg = apply_diff(test_injection_diff, buggy_dir)\n        if ok:\n            result[\"test_injection_applied\"] = True\n        else:\n            logger.warning(\"Test injection failed for %s: %s\", instance_key, msg)\n\n    # Step 2: Apply repair diff\n    ok, msg = apply_diff(repair_diff, buggy_dir)\n    if not ok:\n        result[\"eval_method\"] = \"diff_apply_failed\"\n        result[\"stderr_snippet\"] = msg\n        # Revert test injection if applied\n        if result[\"test_injection_applied\"]:\n            revert_diff(test_injection_diff, buggy_dir)\n        git_restore_dir(buggy_dir)\n        return result\n\n    result[\"diff_apply_success\"] = True\n\n    # Step 3: Run test\n    test_result = run_test(test_cmd, buggy_dir, project, timeout)\n    result[\"test_pass\"] = test_result[\"passed\"]\n    result[\"returncode\"] = test_result[\"returncode\"]\n    result[\"stdout_snippet\"] = test_result[\"stdout\"][-500:]\n    result[\"stderr_snippet\"] = test_result[\"stderr\"][-500:]\n    result[\"eval_method\"] = \"test_execution\"\n    if test_result[\"returncode\"] == -1:\n        result[\"eval_method\"] = \"test_timeout\"\n\n    # Step 4: Revert everything\n    revert_diff(repair_diff, buggy_dir)\n    if result[\"test_injection_applied\"]:\n        revert_diff(test_injection_diff, buggy_dir)\n    git_restore_dir(buggy_dir)\n\n    return result\n\n\n# ---------------------------------------------------------------------------\n# Ground truth baseline\n# ---------------------------------------------------------------------------\n\ndef evaluate_ground_truth(\n    instance_key: str,\n    bug_info: dict,\n    test_injection_diff: Optional[str],\n    timeout: int = 60,\n) -> dict:\n    \"\"\"Apply the official bug_patch.txt and run test. Must pass for valid env.\"\"\"\n    gt_patch = bug_info.get(\"patch\", \"\")\n    return evaluate_single(\n        instance_key, \"ground_truth\", gt_patch, bug_info,\n        test_injection_diff, timeout,\n    )\n\n\n# ---------------------------------------------------------------------------\n# Load Phase 3 v2 checkpoint\n# ---------------------------------------------------------------------------\n\ndef load_checkpoint(path: str) -> dict:\n    if not os.path.isfile(path):\n        return {}\n    with open(path) as f:\n        return json.load(f)\n\n\ndef extract_diffs_from_checkpoint(checkpoint: dict) -> Dict[str, Dict[str, str]]:\n    \"\"\"Extract {instance_key: {condition: raw_diff}} from checkpoint.\"\"\"\n    result = {}\n    for key, rows in checkpoint.items():\n        result[key] = {}\n        for row in rows:\n            cond = row.get(\"condition\", \"\")\n            diff = row.get(\"raw_diff\", \"\")\n            if cond and diff:\n                result[key][cond] = diff\n    return result\n\n\n# ---------------------------------------------------------------------------\n# Main evaluation loop\n# ---------------------------------------------------------------------------\n\ndef run_evaluation(\n    instances: List[str],\n    conditions: List[str],\n    checkpoint_path: str,\n    output_path: str,\n    timeout: int = 60,\n    ground_truth_only: bool = False,\n    skip_ground_truth: bool = False,\n) -> dict:\n    checkpoint = load_checkpoint(checkpoint_path)\n    diffs = extract_diffs_from_checkpoint(checkpoint)\n\n    # Load existing results for resume\n    existing_results = {}\n    if os.path.isfile(output_path):\n        with open(output_path) as f:\n            existing_results = json.load(f)\n\n    all_results = existing_results.copy()\n\n    for instance_key in instances:\n        project, bug_id = parse_instance_key(instance_key)\n        bug_info = read_bug_info(project, bug_id)\n        buggy_dir = get_buggy_dir(instance_key)\n\n        if not os.path.isdir(buggy_dir):\n            logger.warning(\"Skipping %s: buggy dir not found\", instance_key)\n            continue\n\n        logger.info(\"=\" * 50)\n        logger.info(\"Evaluating %s\", instance_key)\n        test_cmd = bug_info.get(\"test_command\", \"\")\n        logger.info(\"  test_command: %s\", test_cmd)\n\n        # Determine if test injection is needed\n        test_inj_diff = None\n        if needs_test_injection(instance_key, bug_info):\n            test_inj_diff = get_test_injection_diff(instance_key, bug_info)\n            if test_inj_diff:\n                logger.info(\"  Test injection needed and available (%d bytes)\",\n                            len(test_inj_diff))\n            else:\n                logger.warning(\"  Test injection needed but diff unavailable\")\n\n        inst_results = all_results.get(instance_key, {})\n\n        # Ground truth baseline\n        if not skip_ground_truth and \"ground_truth\" not in inst_results:\n            logger.info(\"  [GT] Running ground truth baseline...\")\n            gt_result = evaluate_ground_truth(\n                instance_key, bug_info, test_inj_diff, timeout,\n            )\n            gt_pass = gt_result[\"test_pass\"]\n            logger.info(\"  [GT] passed=%s method=%s\", gt_pass, gt_result[\"eval_method\"])\n            if not gt_pass:\n                logger.warning(\"  [GT] stderr: %s\", gt_result[\"stderr_snippet\"][:200])\n            inst_results[\"ground_truth\"] = gt_result\n\n        if ground_truth_only:\n            all_results[instance_key] = inst_results\n            save_results(output_path, all_results)\n            continue\n\n        # Per-condition evaluation\n        inst_diffs = diffs.get(instance_key, {})\n        for cond in conditions:\n            result_key = cond\n            if result_key in inst_results:\n                logger.info(\"  [%s] already evaluated, skipping\", cond)\n                continue\n\n            repair_diff = inst_diffs.get(cond, \"\")\n            if not repair_diff:\n                logger.info(\"  [%s] no repair diff found in checkpoint\", cond)\n                inst_results[result_key] = {\n                    \"instance_id\": instance_key,\n                    \"condition\": cond,\n                    \"test_pass\": False,\n                    \"diff_apply_success\": False,\n                    \"eval_method\": \"no_repair_output\",\n                }\n                continue\n\n            logger.info(\"  [%s] Evaluating (diff=%d bytes)...\", cond, len(repair_diff))\n            result = evaluate_single(\n                instance_key, cond, repair_diff, bug_info,\n                test_inj_diff, timeout,\n            )\n            logger.info(\"  [%s] passed=%s method=%s\",\n                        cond, result[\"test_pass\"], result[\"eval_method\"])\n            inst_results[result_key] = result\n\n        all_results[instance_key] = inst_results\n        save_results(output_path, all_results)\n\n    return all_results\n\n\ndef save_results(path: str, results: dict):\n    os.makedirs(os.path.dirname(path), exist_ok=True)\n    with open(path, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n\n\n# ---------------------------------------------------------------------------\n# Summary / reporting\n# ---------------------------------------------------------------------------\n\ndef print_summary(results: dict, conditions: List[str]):\n    print(f\"\\n{'='*70}\")\n    print(\"TEST EVALUATION SUMMARY\")\n    print(f\"{'='*70}\")\n\n    # Per-instance detail\n    print(f\"\\n{'Instance':<20} {'Condition':<25} {'Pass':<6} {'Method':<25} {'RC'}\")\n    print(\"-\" * 80)\n\n    for key in sorted(results.keys()):\n        inst = results[key]\n        gt = inst.get(\"ground_truth\", {})\n        gt_pass = \"Y\" if gt.get(\"test_pass\") else \"N\"\n        gt_method = gt.get(\"eval_method\", \"n/a\")[:25]\n        gt_rc = gt.get(\"returncode\", \"n/a\")\n        print(f\"{key:<20} {'ground_truth':<25} {gt_pass:<6} {gt_method:<25} {gt_rc}\")\n\n        for cond in conditions:\n            cr = inst.get(cond, {})\n            if not cr:\n                continue\n            p = \"Y\" if cr.get(\"test_pass\") else \"N\"\n            m = cr.get(\"eval_method\", \"\")[:25]\n            rc = cr.get(\"returncode\", \"n/a\")\n            print(f\"{'':<20} {cond:<25} {p:<6} {m:<25} {rc}\")\n        print()\n\n    # Aggregates\n    print(f\"\\n{'='*70}\")\n    print(\"AGGREGATE PASS RATES\")\n    print(f\"{'='*70}\")\n\n    all_instances = sorted(results.keys())\n    n = len(all_instances)\n\n    gt_passes = sum(\n        1 for k in all_instances\n        if results[k].get(\"ground_truth\", {}).get(\"test_pass\")\n    )\n    print(f\"  {'ground_truth':<25} {gt_passes}/{n}\")\n\n    for cond in conditions:\n        passes = sum(\n            1 for k in all_instances\n            if results[k].get(cond, {}).get(\"test_pass\")\n        )\n        diff_ok = sum(\n            1 for k in all_instances\n            if results[k].get(cond, {}).get(\"diff_apply_success\")\n        )\n        evaluated = sum(\n            1 for k in all_instances\n            if cond in results[k]\n        )\n        print(f\"  {cond:<25} {passes}/{evaluated} pass, {diff_ok}/{evaluated} diff_apply\")\n\n    # Tier 1 subset\n    tier1_in_results = [k for k in all_instances if k in TIER1_INSTANCES]\n    if tier1_in_results and len(tier1_in_results) < n:\n        print(f\"\\n  Tier 1 subset ({len(tier1_in_results)} instances):\")\n        for cond in conditions:\n            passes = sum(\n                1 for k in tier1_in_results\n                if results[k].get(cond, {}).get(\"test_pass\")\n            )\n            print(f\"    {cond:<25} {passes}/{len(tier1_in_results)}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Evaluate Phase 3 v2 repair outputs via test execution\",\n    )\n    parser.add_argument(\n        \"--instances\", nargs=\"*\", default=None,\n        help=\"Instance keys to evaluate (default: Tier 1 instances)\",\n    )\n    parser.add_argument(\n        \"--conditions\", nargs=\"*\", default=CONDITIONS,\n        help=f\"Conditions to evaluate (default: {CONDITIONS})\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=os.path.join(PIPELINE_OUTPUT, \"phase3_v2_checkpoint.json\"),\n        help=\"Path to Phase 3 v2 checkpoint JSON\",\n    )\n    parser.add_argument(\n        \"--output\", default=os.path.join(PIPELINE_OUTPUT, \"test_eval_results.json\"),\n        help=\"Output path for evaluation results JSON\",\n    )\n    parser.add_argument(\n        \"--timeout\", type=int, default=60,\n        help=\"Test timeout in seconds (default: 60)\",\n    )\n    parser.add_argument(\n        \"--ground-truth-only\", action=\"store_true\",\n        help=\"Only run ground truth baseline, skip repair evaluation\",\n    )\n    parser.add_argument(\n        \"--skip-ground-truth\", action=\"store_true\",\n        help=\"Skip ground truth baseline, only evaluate repairs\",\n    )\n    parser.add_argument(\n        \"--instance-filter\", choices=[\"tier1\", \"all\"], default=\"tier1\",\n        help=\"Instance filter when --instances is not specified\",\n    )\n    parser.add_argument(\n        \"--resume\", action=\"store_true\",\n        help=\"Resume from existing results file (skip already-evaluated)\",\n    )\n    parser.add_argument(\n        \"--clean\", action=\"store_true\",\n        help=\"Git-restore all instance buggy dirs before starting\",\n    )\n    args = parser.parse_args()\n\n    if args.instances:\n        instances = args.instances\n    elif args.instance_filter == \"tier1\":\n        instances = TIER1_INSTANCES\n    else:\n        instance_dir = os.path.join(WORKSPACE, \"instances\")\n        if os.path.isdir(instance_dir):\n            instances = sorted(os.listdir(instance_dir))\n        else:\n            instances = TIER1_INSTANCES\n\n    if not args.resume and os.path.isfile(args.output) and not args.ground_truth_only:\n        logger.info(\"Existing results file found. Use --resume to continue or delete %s\", args.output)\n\n    if args.clean:\n        logger.info(\"Cleaning all buggy dirs via git restore...\")\n        for key in instances:\n            buggy_dir = get_buggy_dir(key)\n            if os.path.isdir(buggy_dir):\n                git_restore_dir(buggy_dir)\n        logger.info(\"Clean complete\")\n\n    logger.info(\"Evaluating %d instances × %d conditions\", len(instances), len(args.conditions))\n    logger.info(\"Checkpoint: %s\", args.checkpoint)\n    logger.info(\"Output: %s\", args.output)\n\n    results = run_evaluation(\n        instances=instances,\n        conditions=args.conditions,\n        checkpoint_path=args.checkpoint,\n        output_path=args.output,\n        timeout=args.timeout,\n        ground_truth_only=args.ground_truth_only,\n        skip_ground_truth=args.skip_ground_truth,\n    )\n\n    print_summary(results, args.conditions)\n\n    print(f\"\\nResults saved to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 685,
      "startLine": 1,
      "totalLines": 685
    }
  }
}
```

</details>

---


### Assistant

_source line 216_

Good - file looks clean. Let me re-upload and re-test with the fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d1beb84a-a3d1-4df0-8935-261ab58b3407",
  "uuid": "8f142ffe-0f56-4b07-82ef-adeadb47d87d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3tvjCTdPDWGoJum3nmooX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8461,
      "cache_read_input_tokens": 120506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8461
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
