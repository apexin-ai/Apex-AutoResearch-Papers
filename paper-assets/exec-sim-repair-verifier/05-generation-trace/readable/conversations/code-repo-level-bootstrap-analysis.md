# code repo level bootstrap analysis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_code_repo-level-bootstrap-analysis_20260514T172708.jsonl`
- **Structured JSON:** [`aa83158d007aa81a8490.json`](../../sessions/aa/aa83158d007aa81a8490.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T17:28:17.361732+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T17:28:17.362162+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T17:28:17.362379+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls -la /home/sonny/exec-sim-repair-verifier/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls -la /home/sonny/exec-sim-repair-verifier/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T17:28:17.362546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 72\\ndrwxr-xr-x  8 root root 4096 May 14 11:08 .\\ndrwxr-xr-x 19 root root 4096 May 15 00:31 ..\\n-rw-r--r--  1 root root 9629 May 14 11:45 eval_8b_ckpt400.log\\n-rw-r--r--  1 root root 9628 May 14 11:45 eval_8b_ckpt600.log\\n-rw-r--r--  1 root root 9745 May 14 10:30 eval_cls_8b_conda.log\\n-rw-r--r--  1 root root 5726 May 14 10:20 eval_cls_v5_conda.log\\n-rw-r--r--  1 root root 5731 May 14 11:07 eval_cls_v5_conda_ckpt400.log\\n-rw-r--r--  1 root root 5731 May 14 11:07 eval_cls_v5_conda_ckpt600.log\\ndrwxr-xr-x  2 root root   83 May 14 11:45 repo_cls_8b_conda_ckpt400\\ndrwxr-xr-x  2 root root   83 May 14 11:45 repo_cls_8b_conda_ckpt600\\ndrwxr-xr-x  2 root root   83 May 14 10:30 repo_cls_8b_conda_eval\\ndrwxr-xr-x  2 root root   83 May 14 11:07 repo_cls_v5_conda_ckpt400\\ndrwxr-xr-x  2 root root   83 May 14 11:07 repo_cls_v5_conda_ckpt600\\ndrwxr-xr-x  2 root root   83 May 14 10:20 repo_cls_v5_conda_eval\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T17:28:17.362686+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls -la /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls -la /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T17:28:17.362852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1492\\ndrwxr-xr-x 2 root root      83 May 14 10:20 .\\ndrwxr-xr-x 8 root root    4096 May 14 11:08 ..\\n-rw-r--r-- 1 root root     733 May 14 10:20 eval_repo_cls.json\\n-rw-r--r-- 1 root root 1519213 May 14 10:20 eval_repo_cls_predictions.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T17:28:17.363038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls -la /home/sonny/exec-sim-repair-verifier/results/repo_cls_8b_conda_eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls -la /home/sonny/exec-sim-repair-verifier/results/repo_cls_8b_conda_eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T17:28:17.363209+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1492\\ndrwxr-xr-x 2 root root      83 May 14 10:30 .\\ndrwxr-xr-x 8 root root    4096 May 14 11:08 ..\\n-rw-r--r-- 1 root root     731 May 14 10:30 eval_repo_cls.json\\n-rw-r--r-- 1 root root 1519261 May 14 10:30 eval_repo_cls_predictions.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T17:28:17.363355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "head -3 /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "head -3 /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T17:28:17.363502+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"index\\\": 0, \\\"problem_id\\\": \\\"pydata__xarray-6992\\\", \\\"label\\\": 1, \\\"pred\\\": 0, \\\"correct\\\": 0, \\\"truncated\\\": false, \\\"gen_text\\\": \\\"fail\\\", \\\"unparseable\\\": false}\\n{\\\"index\\\": 1, \\\"problem_id\\\": \\\"django__django-14315\\\", \\\"label\\\": 1, \\\"pred\\\": 0, \\\"correct\\\": 0, \\\"truncated\\\": false, \\\"gen_text\\\": \\\"fail\\\", \\\"unparseable\\\": false}\\n{\\\"index\\\": 2, \\\"problem_id\\\": \\\"pytest-dev__pytest-7490\\\", \\\"label\\\": 0, \\\"pred\\\": 0, \\\"correct\\\": 1, \\\"truncated\\\": true, \\\"gen_text\\\": \\\"# If the test failed, and\\\", \\\"unparseable\\\": false}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T17:28:17.363632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T17:28:17.363779+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"CLS\\\",\\n  \\\"checkpoint\\\": \\\"/root/autodl-tmp/checkpoints_repo_cls_v5_conda/checkpoint-200\\\",\\n  \\\"n_instances\\\": 9784,\\n  \\\"n_cls_unparseable\\\": 132,\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 52.96,\\n    \\\"majority_baseline\\\": 72.96,\\n    \\\"gap_vs_majority_pp\\\": -19.99,\\n    \\\"f1_fail\\\": 51.02,\\n    \\\"f1_pass\\\": 54.76,\\n    \\\"f1_macro\\\": 52.89,\\n    \\\"precision_fail\\\": 35.51,\\n    \\\"precision_pass\\\": 91.79,\\n    \\\"recall_fail\\\": 90.59,\\n    \\\"recall_pass\\\": 39.02,\\n    \\\"confusion_matrix\\\": {\\n      \\\"tn\\\": 2397,\\n      \\\"fp\\\": 249,\\n      \\\"fn\\\": 4353,\\n      \\\"tp\\\": 2785\\n    },\\n    \\\"support\\\": {\\n      \\\"fail\\\": 2646,\\n      \\\"pass\\\": 7138\\n    }\\n  },\\n  \\\"config\\\": {\\n    \\\"model_name\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B\\\",\\n    \\\"max_seq_length\\\": 2048,\\n    \\\"batch_size\\\": 16\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T17:28:17.364009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "wc -l /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "wc -l /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T17:28:17.364148+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"9784 /home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T17:28:17.364281+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T17:28:17.364399+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T17:28:17.364529+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat > /home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py << 'SCRIPT_EOF'\n\"\"\"Repo-level paired bootstrap: CLS vs CWM accuracy comparison.\n\nReads two prediction JSONL files (CLS and CWM), pairs by problem_id,\ncomputes accuracy gap with bootstrap 95% CI and one-sided p-value.\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nimport numpy as np\nfrom pathlib import Path\n\n\ndef load_predictions(path: str) -> dict[str, int]:\n    \"\"\"Load JSONL predictions, return {problem_id: correct}.\"\"\"\n    preds = {}\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            preds[row[\"problem_id\"]] = row[\"correct\"]\n    return preds\n\n\ndef paired_bootstrap(cls_correct: np.ndarray, cwm_correct: np.ndarray,\n                     n_bootstrap: int = 10000, seed: int = 42) -> dict:\n    \"\"\"Paired bootstrap comparing CLS vs CWM accuracy.\n    \n    H0: CLS accuracy <= CWM accuracy (one-sided test).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    n = len(cls_correct)\n    \n    cls_acc = cls_correct.mean()\n    cwm_acc = cwm_correct.mean()\n    observed_gap = cls_acc - cwm_acc\n    \n    gaps = np.empty(n_bootstrap)\n    for i in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        gaps[i] = cls_correct[idx].mean() - cwm_correct[idx].mean()\n    \n    ci_lower = float(np.percentile(gaps, 2.5))\n    ci_upper = float(np.percentile(gaps, 97.5))\n    \n    # one-sided p-value: P(gap <= 0) under bootstrap distribution\n    p_value = float((gaps <= 0).mean())\n    \n    return {\n        \"cls_accuracy\": round(float(cls_acc) * 100, 2),\n        \"cwm_accuracy\": round(float(cwm_acc) * 100, 2),\n        \"gap_pp\": round(float(observed_gap) * 100, 2),\n        \"ci_lower_pp\": round(ci_lower * 100, 2),\n        \"ci_upper_pp\": round(ci_upper * 100, 2),\n        \"p_value\": round(p_value, 6),\n        \"n_samples\": int(n),\n        \"n_bootstrap\": n_bootstrap,\n        \"significant_at_005\": p_value < 0.05,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Paired bootstrap: CLS vs CWM repo-level accuracy comparison\")\n    parser.add_argument(\"--cls_pred\", required=True,\n                        help=\"Path to CLS prediction JSONL\")\n    parser.add_argument(\"--cwm_pred\", required=True,\n                        help=\"Path to CWM prediction JSONL\")\n    parser.add_argument(\"--n_bootstrap\", type=int, default=10000,\n                        help=\"Number of bootstrap resamples (default: 10000)\")\n    parser.add_argument(\"--seed\", type=int, default=42,\n                        help=\"Random seed (default: 42)\")\n    parser.add_argument(\"--output\", type=str, default=None,\n                        help=\"Output JSON file path (default: stdout)\")\n    args = parser.parse_args()\n\n    cls_preds = load_predictions(args.cls_pred)\n    cwm_preds = load_predictions(args.cwm_pred)\n\n    common_ids = sorted(set(cls_preds.keys()) & set(cwm_preds.keys()))\n    cls_only = set(cls_preds.keys()) - set(cwm_preds.keys())\n    cwm_only = set(cwm_preds.keys()) - set(cls_preds.keys())\n\n    if cls_only or cwm_only:\n        print(f\"WARNING: {len(cls_only)} CLS-only, {len(cwm_only)} CWM-only instances (excluded)\",\n              file=sys.stderr)\n\n    if not common_ids:\n        print(\"ERROR: No common problem_ids between CLS and CWM predictions\", file=sys.stderr)\n        sys.exit(1)\n\n    cls_correct = np.array([cls_preds[pid] for pid in common_ids])\n    cwm_correct = np.array([cwm_preds[pid] for pid in common_ids])\n\n    result = paired_bootstrap(cls_correct, cwm_correct,\n                              n_bootstrap=args.n_bootstrap, seed=args.seed)\n    result[\"cls_pred_file\"] = args.cls_pred\n    result[\"cwm_pred_file\"] = args.cwm_pred\n\n    output_json = json.dumps(result, indent=2)\n\n    if args.output:\n        Path(args.output).write_text(output_json + \"\\n\")\n        print(f\"Results written to {args.output}\", file=sys.stderr)\n    \n    print(output_json)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat > /home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py << 'SCRIPT_EOF'\n\"\"\"Repo-level paired bootstrap: CLS vs CWM accuracy comparison.\n\nReads two prediction JSONL files (CLS and CWM), pairs by problem_id,\ncomputes accuracy gap with bootstrap 95% CI and one-sided p-value.\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nimport numpy as np\nfrom pathlib import Path\n\n\ndef load_predictions(path: str) -> dict[str, int]:\n    \"\"\"Load JSONL predictions, return {problem_id: correct}.\"\"\"\n    preds = {}\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            preds[row[\"problem_id\"]] = row[\"correct\"]\n    return preds\n\n\ndef paired_bootstrap(cls_correct: np.ndarray, cwm_correct: np.ndarray,\n                     n_bootstrap: int = 10000, seed: int = 42) -> dict:\n    \"\"\"Paired bootstrap comparing CLS vs CWM accuracy.\n    \n    H0: CLS accuracy <= CWM accuracy (one-sided test).\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    n = len(cls_correct)\n    \n    cls_acc = cls_correct.mean()\n    cwm_acc = cwm_correct.mean()\n    observed_gap = cls_acc - cwm_acc\n    \n    gaps = np.empty(n_bootstrap)\n    for i in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        gaps[i] = cls_correct[idx].mean() - cwm_correct[idx].mean()\n    \n    ci_lower = float(np.percentile(gaps, 2.5))\n    ci_upper = float(np.percentile(gaps, 97.5))\n    \n    # one-sided p-value: P(gap <= 0) under bootstrap distribution\n    p_value = float((gaps <= 0).mean())\n    \n    return {\n        \"cls_accuracy\": round(float(cls_acc) * 100, 2),\n        \"cwm_accuracy\": round(float(cwm_acc) * 100, 2),\n        \"gap_pp\": round(float(observed_gap) * 100, 2),\n        \"ci_lower_pp\": round(ci_lower * 100, 2),\n        \"ci_upper_pp\": round(ci_upper * 100, 2),\n        \"p_value\": round(p_value, 6),\n        \"n_samples\": int(n),\n        \"n_bootstrap\": n_bootstrap,\n        \"significant_at_005\": p_value < 0.05,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Paired bootstrap: CLS vs CWM repo-level accuracy comparison\")\n    parser.add_argument(\"--cls_pred\", required=True,\n                        help=\"Path to CLS prediction JSONL\")\n    parser.add_argument(\"--cwm_pred\", required=True,\n                        help=\"Path to CWM prediction JSONL\")\n    parser.add_argument(\"--n_bootstrap\", type=int, default=10000,\n                        help=\"Number of bootstrap resamples (default: 10000)\")\n    parser.add_argument(\"--seed\", type=int, default=42,\n                        help=\"Random seed (default: 42)\")\n    parser.add_argument(\"--output\", type=str, default=None,\n                        help=\"Output JSON file path (default: stdout)\")\n    args = parser.parse_args()\n\n    cls_preds = load_predictions(args.cls_pred)\n    cwm_preds = load_predictions(args.cwm_pred)\n\n    common_ids = sorted(set(cls_preds.keys()) & set(cwm_preds.keys()))\n    cls_only = set(cls_preds.keys()) - set(cwm_preds.keys())\n    cwm_only = set(cwm_preds.keys()) - set(cls_preds.keys())\n\n    if cls_only or cwm_only:\n        print(f\"WARNING: {len(cls_only)} CLS-only, {len(cwm_only)} CWM-only instances (excluded)\",\n              file=sys.stderr)\n\n    if not common_ids:\n        print(\"ERROR: No common problem_ids between CLS and CWM predictions\", file=sys.stderr)\n        sys.exit(1)\n\n    cls_correct = np.array([cls_preds[pid] for pid in common_ids])\n    cwm_correct = np.array([cwm_preds[pid] for pid in common_ids])\n\n    result = paired_bootstrap(cls_correct, cwm_correct,\n                              n_bootstrap=args.n_bootstrap, seed=args.seed)\n    result[\"cls_pred_file\"] = args.cls_pred\n    result[\"cwm_pred_file\"] = args.cwm_pred\n\n    output_json = json.dumps(result, indent=2)\n\n    if args.output:\n        Path(args.output).write_text(output_json + \"\\n\")\n        print(f\"Results written to {args.output}\", file=sys.stderr)\n    \n    print(output_json)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T17:28:17.364690+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T17:28:17.364848+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "python3 /home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "python3 /home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T17:28:17.364978+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python script execution not allowed; use -c for inline expressions only. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T17:28:17.365167+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T17:28:17.365317+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: repo_level_bootstrap.py [-h] --cls_pred CLS_PRED --cwm_pred CWM_PRED\\n                               [--n_bootstrap N_BOOTSTRAP] [--seed SEED]\\n                               [--output OUTPUT]\\n\\nPaired bootstrap: CLS vs CWM repo-level accuracy comparison\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --cls_pred CLS_PRED   Path to CLS prediction JSONL\\n  --cwm_pred CWM_PRED   Path to CWM prediction JSONL\\n  --n_bootstrap N_BOOTSTRAP\\n                        Number of bootstrap resamples (default: 10000)\\n  --seed SEED           Random seed (default: 42)\\n  --output OUTPUT       Output JSON file path (default: stdout)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T17:28:17.365486+00:00_

脚本已部署到 westd `/home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py`，dry-run 通过。

用法示例（CWM eval 完成后）：
```bash
python repo_level_bootstrap.py \
  --cls_pred results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl \
  --cwm_pred results/&lt;cwm_dir>/eval_repo_cls_predictions.jsonl \
  --output results/bootstrap_cls_vs_cwm.json
```

输出 JSON 包含：`cls_accuracy`, `cwm_accuracy`, `gap_pp`（百分点差）, `ci_lower_pp`, `ci_upper_pp`（95% CI）, `p_value`（单侧 H0: CLS ≤ CWM）, `n_samples`, `significant_at_005`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_repo-level-bootstrap-analysis_20260514T172708"
}
```

</details>

---
