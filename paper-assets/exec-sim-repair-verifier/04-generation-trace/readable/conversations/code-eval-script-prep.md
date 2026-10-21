# code eval script prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_code_eval-script-prep_20260512T222025.jsonl`
- **Structured JSON:** [`2b9704131856a90efaf1.json`](../../sessions/2b/2b9704131856a90efaf1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-12T22:25:55.767091+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T22:25:55.767437+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T22:25:55.767592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls /home/sonny/exec-sim-repair-verifier/*.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls /home/sonny/exec-sim-repair-verifier/*.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T22:25:55.767749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/home/sonny/exec-sim-repair-verifier/analysis_5paired_bootstrap.py\\n/home/sonny/exec-sim-repair-verifier/analysis_8b_scaling_bootstrap.py\\n/home/sonny/exec-sim-repair-verifier/analysis_error_overlap.py\\n/home/sonny/exec-sim-repair-verifier/analyze_p2p_regression.py\\n/home/sonny/exec-sim-repair-verifier/block_corr_from_predictions.py\\n/home/sonny/exec-sim-repair-verifier/build_cwm_data.py\\n/home/sonny/exec-sim-repair-verifier/build_data.py\\n/home/sonny/exec-sim-repair-verifier/build_swebench_data.py\\n/home/sonny/exec-sim-repair-verifier/build_trace_data.py\\n/home/sonny/exec-sim-repair-verifier/build_traj_data.py\\n/home/sonny/exec-sim-repair-verifier/eval_cwm_baseline.py\\n/home/sonny/exec-sim-repair-verifier/eval_majority_voting.py\\n/home/sonny/exec-sim-repair-verifier/eval_pertest_diagnostic.py\\n/home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py\\n/home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py\\n/home/sonny/exec-sim-repair-verifier/eval_trace_judge.py\\n/home/sonny/exec-sim-repair-verifier/eval_traj_verifier.py\\n/home/sonny/exec-sim-repair-verifier/eval_verifier.py\\n/home/sonny/exec-sim-repair-verifier/extract_cls_seed0.py\\n/home/sonny/exec-sim-repair-verifier/extract_predictions_generic.py\\n/home/sonny/exec-sim-repair-verifier/llm_judge_zeroshot.py\\n/home/sonny/exec-sim-repair-verifier/measure_inference_cost.py\\n/home/sonny/exec-sim-repair-verifier/mvp_a_oracle_sim.py\\n/home/sonny/exec-sim-repair-verifier/mvp_a_real_f2p_sim.py\\n/home/sonny/exec-sim-repair-verifier/mvp_a_sensitivity.py\\n/home/sonny/exec-sim-repair-verifier/mvp_a_total_sim.py\\n/home/sonny/exec-sim-repair-verifier/paired_bootstrap_repo.py\\n/home/sonny/exec-sim-repair-verifier/split_swebench_data.py\\n/home/sonny/exec-sim-repair-verifier/swebench_test_dist.py\\n/home/sonny/exec-sim-repair-verifier/train_cwm_baseline.py\\n/home/sonny/exec-sim-repair-verifier/train_repo_cwm.py\\n/home/sonny/exec-sim-repair-verif
…[truncated 312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T22:25:55.767990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T22:25:55.768280+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# eval_repo_verifier.py — Evaluate repo-level LoRA verifier on SWE-bench test set\\n# Input: data/swebench_full/swebench_test.jsonl + LoRA checkpoint\\n# Output: Formatted report to stdout + JSON to --output\\n# Adapted from eval_verifier.py: reads swebench_test.jsonl, repo-level prompt\\n#\\n# [Added] Truncation-aware evaluation: detects samples truncated at max_seq_length,\\n#   reports separate metrics for truncated vs non-truncated subsets and truncation rate.\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nfrom collections import Counter\\n\\nimport torch\\nfrom peft import PeftModel\\nfrom sklearn.metrics import (\\n    accuracy_score,\\n    confusion_matrix,\\n    f1_score,\\n    precision_score,\\n    recall_score,\\n)\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlog = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are a code verifier. Given a code patch (git diff) and a test name, \\\"\\n    \\\"predict whether the test will pass or fail when run against the patched code.\\\"\\n)\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f]\\n\\n\\ndef detect_thinking_support(tokenizer):\\n    try:\\n        tokenizer.apply_chat_template(\\n            [{\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"hi\\\"}],\\n            tokenize=False,\\n            enable_thinking=False,\\n        )\\n        return {\\\"enable_thinking\\\": False}\\n    except TypeError:\\n        return {}\\n\\n\\ndef build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):\\n    user_msg = f\\\"## Patch (git diff)\\\\n{code}\\\\n\\\\n## Test\\\\n{test}\\\\n\\\\nWill this test pass or fail?\\\"\\n    msgs = [\\n        {\\\"role\\\": \\\"system\\\", \\\"content\\\": SYSTEM_PROMPT},\\n        {\\\"role\\\": \\\"user\\\", \\\"con
…[truncated 7395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T22:25:55.768460+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T22:25:55.768591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat /home/sonny/exec-sim-repair-verifier/paired_bootstrap_repo.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat /home/sonny/exec-sim-repair-verifier/paired_bootstrap_repo.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T22:25:55.768900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# eval_repo_cwm.py — Evaluate repo-level CWM generation on SWE-bench test set\\n# Input: data/swebench_full/swebench_test.jsonl + LoRA checkpoint\\n# Output: Formatted report to stdout + JSON to --output\\n# Adapted from eval_cwm_baseline.py: reads swebench_test.jsonl, repo-level prompt,\\n#   uses execution_output as ground truth target\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport statistics\\nfrom collections import Counter, defaultdict\\n\\nimport torch\\nfrom peft import PeftModel\\nfrom sklearn.metrics import (\\n    accuracy_score,\\n    confusion_matrix,\\n    f1_score,\\n    precision_score,\\n    recall_score,\\n)\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlog = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are a code execution simulator. Given a code patch (git diff) and a test name, \\\"\\n    \\\"predict the execution result when the test is run against the patched code.\\\"\\n)\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f]\\n\\n\\ndef detect_thinking_support(tokenizer):\\n    try:\\n        tokenizer.apply_chat_template(\\n            [{\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"hi\\\"}],\\n            tokenize=False,\\n            enable_thinking=False,\\n        )\\n        return {\\\"enable_thinking\\\": False}\\n    except TypeError:\\n        return {}\\n\\n\\ndef build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):\\n    user_msg = f\\\"## Patch (git diff)\\\\n{code}\\\\n\\\\n## Test\\\\n{test}\\\\n\\\\nWhat is the execution result?\\\"\\n    msgs = [\\n        {\\\"role\\\": \\\"system\\\", \\\"content\\\": SYSTEM_PROMPT},\\n        {\\\"role\\\": \\\"user\\\", \\\"content\\\": user_msg},\\n    ]\\n    ids = tokenizer.apply_chat_template(\\n
…[truncated 7395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T22:25:55.769190+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# paired_bootstrap_repo.py — Paired bootstrap test for CLS vs CWM repo-level eval\\n# Usage:\\n#   python paired_bootstrap_repo.py \\\\\\n#     --cls_preds eval_repo_cls_predictions.jsonl \\\\\\n#     --cwm_preds eval_repo_cwm_predictions.jsonl \\\\\\n#     --output paired_bootstrap_repo_results.json\\n\\nimport argparse\\nimport json\\nimport sys\\n\\nimport numpy as np\\n\\n\\ndef load_predictions(path):\\n    preds = {}\\n    with open(path) as f:\\n        for line in f:\\n            rec = json.loads(line)\\n            key = (rec[\\\"index\\\"], rec.get(\\\"problem_id\\\", \\\"\\\"))\\n            preds[key] = rec\\n    return preds\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser(description=\\\"Paired bootstrap: CLS vs CWM repo-level\\\")\\n    p.add_argument(\\\"--cls_preds\\\", required=True, help=\\\"CLS predictions JSONL\\\")\\n    p.add_argument(\\\"--cwm_preds\\\", required=True, help=\\\"CWM predictions JSONL\\\")\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--output\\\", default=\\\"paired_bootstrap_repo_results.json\\\")\\n    args = p.parse_args()\\n\\n    cls_preds = load_predictions(args.cls_preds)\\n    cwm_preds = load_predictions(args.cwm_preds)\\n\\n    shared_keys = sorted(set(cls_preds.keys()) & set(cwm_preds.keys()))\\n    if not shared_keys:\\n        print(\\\"ERROR: No shared instances between CLS and CWM predictions.\\\", file=sys.stderr)\\n        sys.exit(1)\\n\\n    n = len(shared_keys)\\n    cls_only = len(cls_preds) - n\\n    cwm_only = len(cwm_preds) - n\\n    if cls_only or cwm_only:\\n        print(f\\\"WARNING: {cls_only} CLS-only, {cwm_only} CWM-only instances excluded. Using {n} shared.\\\", file=sys.stderr)\\n\\n    cls_correct = np.zeros(n, dtype=np.int32)\\n    cwm_correct = np.zeros(n, dtype=np.int32)\\n    labels = np.zeros(n, dtype=np.int32)\\n\\n    fo
…[truncated 4957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T22:25:55.769401+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "head -5 /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "head -5 /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T22:25:55.769650+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"code\\\": \\\"diff --git a/xarray/core/dataset.py b/xarray/core/dataset.py\\\\n--- a/xarray/core/dataset.py\\\\n+++ b/xarray/core/dataset.py\\\\n@@ -4026,10 +4026,11 @@ def set_index(\\\\n         dim_coords = either_dict_or_kwargs(indexes, indexes_kwargs, \\\\\\\"set_index\\\\\\\")\\\\n \\\\n         new_indexes: dict[Hashable, Index] = {}\\\\n-        new_variables: dict[Hashable, IndexVariable] = {}\\\\n-        maybe_drop_indexes: list[Hashable] = []\\\\n-        drop_variables: list[Hashable] = []\\\\n+        new_variables: dict[Hashable, Variable] = {}\\\\n+        drop_indexes: set[Hashable] = set()\\\\n+        drop_variables: set[Hashable] = set()\\\\n         replace_dims: dict[Hashable, Hashable] = {}\\\\n+        all_var_names: set[Hashable] = set()\\\\n \\\\n         for dim, _var_names in dim_coords.items():\\\\n             if isinstance(_var_names, str) or not isinstance(_var_names, Sequence):\\\\n@@ -4044,16 +4045,19 @@ def set_index(\\\\n                     + \\\\\\\" variable(s) do not exist\\\\\\\"\\\\n                 )\\\\n \\\\n-            current_coord_names = self.xindexes.get_all_coords(dim, errors=\\\\\\\"ignore\\\\\\\")\\\\n+            all_var_names.update(var_names)\\\\n+            drop_variables.update(var_names)\\\\n \\\\n-            # drop any pre-existing index involved\\\\n-            maybe_drop_indexes += list(current_coord_names) + var_names\\\\n+            # drop any pre-existing index involved and its corresponding coordinates\\\\n+            index_coord_names = self.xindexes.get_all_coords(dim, errors=\\\\\\\"ignore\\\\\\\")\\\\n+            all_index_coord_names = set(index_coord_names)\\\\n             for k in var_names:\\\\n-                maybe_drop_indexes += list(\\\\n+                all_index_coord_names.update(\\\\n                     self.xindexes.get_all_coords(k, errors=\\\\\\\"ignore\\\\\\\")\\\\n                 )\\\\n \\\\n-            drop_
…[truncated 6956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T22:25:55.769831+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "grep -n \"per_sample\" /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "grep -n \"per_sample\" /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T22:25:55.769976+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"155:    y_true, y_pred, per_sample = [], [], []\\n197:            per_sample.append({\\n295:            for rec in per_sample:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T22:25:55.770102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "grep -n \"per_sample\" /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "grep -n \"per_sample\" /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T22:25:55.770227+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"148:    per_sample = []\\n196:            per_sample.append({\\n281:            for rec in per_sample:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T22:25:55.770381+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "sed -n '140,210p' /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "sed -n '140,210p' /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T22:25:55.770508+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T22:25:55.770625+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "sed -n '140,210p' /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "sed -n '140,210p' /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T22:25:55.770742+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T22:25:55.770880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "wc -l /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "wc -l /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T22:25:55.771003+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"9784 /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T22:25:55.771119+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "grep -n \"per_sample.append\" /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "grep -n \"per_sample.append\" /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T22:25:55.771270+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"197:            per_sample.append({\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T22:25:55.771388+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "grep -n \"per_sample.append\" /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "grep -n \"per_sample.append\" /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T22:25:55.771506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"196:            per_sample.append({\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T22:25:55.771625+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "tail -n +190 /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "tail -n +190 /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T22:25:55.771879+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                n_unparseable += 1\\n                pred = majority_class\\n\\n            y_true.append(batch_labels[j])\\n            y_pred.append(pred)\\n            truncated_flags.append(batch_truncated[j])\\n            pid = ex.get(\\\"problem_id\\\", ex.get(\\\"metadata\\\", {}).get(\\\"instance_id\\\", \\\"\\\"))\\n            per_sample.append({\\n                \\\"index\\\": i + j,\\n                \\\"problem_id\\\": pid,\\n                \\\"label\\\": batch_labels[j],\\n                \\\"pred\\\": pred,\\n                \\\"correct\\\": int(pred == batch_labels[j]),\\n                \\\"truncated\\\": batch_truncated[j],\\n            })\\n\\n        done = min(i + args.batch_size, total)\\n        if done % (args.batch_size * 10) == 0 or done == total:\\n            log.info(f\\\"Progress: {done}/{total}\\\")\\n\\n    # --- Overall metrics ---\\n    acc = accuracy_score(y_true, y_pred)\\n    gap = acc - majority_baseline\\n    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1])\\n    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1])\\n    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1])\\n    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])\\n\\n    # --- Truncation subset metrics ---\\n    n_truncated = sum(truncated_flags)\\n    truncation_rate = n_truncated / total if total > 0 else 0.0\\n\\n    yt_notrunc = [y for y, t in zip(y_true, truncated_flags) if not t]\\n    yp_notrunc = [y for y, t in zip(y_pred, truncated_flags) if not t]\\n    yt_trunc = [y for y, t in zip(y_true, truncated_flags) if t]\\n    yp_trunc = [y for y, t in zip(y_pred, truncated_flags) if t]\\n\\n    metrics_non_truncated = compute_subset_metrics(yt_notrunc, yp_notrunc)\\n    metrics_truncated = compute_subset_metrics(yt_trunc, yp_trunc)\\n\\n    results = {\\n        \\\"test_set_size\\\": total,\\n        \\\"class_balance\\\": {\\\"pass\\\": n_pass, \\\"fail\\\": n
…[truncated 4255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T22:25:55.772039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "tail -n +190 /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "tail -n +190 /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T22:25:55.772238+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            y_true.append(batch_labels[j])\\n            y_pred.append(pred)\\n\\n            if pred == batch_labels[j]:\\n                error_type_stats[etype][\\\"pf_correct\\\"] += 1\\n            pid = ex.get(\\\"problem_id\\\", ex.get(\\\"metadata\\\", {}).get(\\\"instance_id\\\", \\\"\\\"))\\n            per_sample.append({\\n                \\\"index\\\": i + j,\\n                \\\"problem_id\\\": pid,\\n                \\\"label\\\": batch_labels[j],\\n                \\\"pred\\\": pred,\\n                \\\"gen_text\\\": gen_text,\\n                \\\"exact_match\\\": is_exact,\\n            })\\n\\n        done = min(i + args.batch_size, total)\\n        if done % (args.batch_size * 10) == 0 or done == total:\\n            log.info(f\\\"Progress: {done}/{total}\\\")\\n\\n    acc = accuracy_score(y_true, y_pred)\\n    gap = acc - majority_baseline\\n    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1])\\n    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1])\\n    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1])\\n    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])\\n    exact_match_rate = n_exact / total if total else 0\\n\\n    error_type_results = {}\\n    for etype, st in error_type_stats.items():\\n        t = st[\\\"total\\\"]\\n        error_type_results[etype] = {\\n            \\\"total\\\": t,\\n            \\\"exact_match_rate\\\": round(st[\\\"exact\\\"] / t * 100, 1) if t else 0,\\n            \\\"pass_fail_accuracy\\\": round(st[\\\"pf_correct\\\"] / t * 100, 1) if t else 0,\\n        }\\n\\n    gen_len_mean = statistics.mean(gen_lengths) if gen_lengths else 0\\n    gen_len_median = statistics.median(gen_lengths) if gen_lengths else 0\\n    gen_len_max = max(gen_lengths) if gen_lengths else 0\\n\\n    results = {\\n        \\\"test_set_size\\\": total,\\n        \\\"class_balance\\\": {\\\"pass\\\": n_pass, \\\"fail\\\": n_fail, \\\"pas
…[truncated 3622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T22:25:55.772420+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "head -190 /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "head -190 /home/sonny/exec-sim-repair-verifier/eval_repo_verifier.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T22:25:55.772651+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# eval_repo_verifier.py — Evaluate repo-level LoRA verifier on SWE-bench test set\\n# Input: data/swebench_full/swebench_test.jsonl + LoRA checkpoint\\n# Output: Formatted report to stdout + JSON to --output\\n# Adapted from eval_verifier.py: reads swebench_test.jsonl, repo-level prompt\\n#\\n# [Added] Truncation-aware evaluation: detects samples truncated at max_seq_length,\\n#   reports separate metrics for truncated vs non-truncated subsets and truncation rate.\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nfrom collections import Counter\\n\\nimport torch\\nfrom peft import PeftModel\\nfrom sklearn.metrics import (\\n    accuracy_score,\\n    confusion_matrix,\\n    f1_score,\\n    precision_score,\\n    recall_score,\\n)\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlog = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are a code verifier. Given a code patch (git diff) and a test name, \\\"\\n    \\\"predict whether the test will pass or fail when run against the patched code.\\\"\\n)\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f]\\n\\n\\ndef detect_thinking_support(tokenizer):\\n    try:\\n        tokenizer.apply_chat_template(\\n            [{\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"hi\\\"}],\\n            tokenize=False,\\n            enable_thinking=False,\\n        )\\n        return {\\\"enable_thinking\\\": False}\\n    except TypeError:\\n        return {}\\n\\n\\ndef build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):\\n    user_msg = f\\\"## Patch (git diff)\\\\n{code}\\\\n\\\\n## Test\\\\n{test}\\\\n\\\\nWill this test pass or fail?\\\"\\n    msgs = [\\n        {\\\"role\\\": \\\"system\\\", \\\"content\\\": SYSTEM_PROMPT},\\n        {\\\"role\\\": \\\"user\\\", \\\"con
…[truncated 5816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T22:25:55.772970+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat > /home/sonny/exec-sim-repair-verifier/eval_repo_level.py << 'ENDOFSCRIPT'\n# eval_repo_level.py — Unified repo-level CLS vs CWM evaluation + paired bootstrap on F1\n# Input:\n#   Mode 1 (inference): --cls_checkpoint + --cwm_checkpoint + test JSONL\n#   Mode 2 (predictions only): --cls_preds + --cwm_preds (skip inference)\n# Output: JSON results + human-readable summary with D008 Go/No-Go decision\n# Dependencies: torch, transformers, peft, sklearn, numpy\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport gc\nfrom collections import Counter\n\nimport numpy as np\nimport torch\nfrom sklearn.metrics import (\n    accuracy_score,\n    confusion_matrix,\n    f1_score,\n    precision_score,\n    recall_score,\n)\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlog = logging.getLogger(__name__)\n\n# ── Prompts ──────────────────────────────────────────────────────────────────\n\nCLS_SYSTEM = (\n    \"You are a code verifier. Given a code patch (git diff) and a test name, \"\n    \"predict whether the test will pass or fail when run against the patched code.\"\n)\nCLS_USER_TEMPLATE = \"## Patch (git diff)\\n{code}\\n\\n## Test\\n{test}\\n\\nWill this test pass or fail?\"\n\nCWM_SYSTEM = (\n    \"You are a code execution simulator. Given a code patch (git diff) and a test name, \"\n    \"predict the execution result when the test is run against the patched code.\"\n)\nCWM_USER_TEMPLATE = \"## Patch (git diff)\\n{code}\\n\\n## Test\\n{test}\\n\\nWhat is the execution result?\"\n\n\n# ── Data / Tokenizer Helpers ─────────────────────────────────────────────────\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef detect_thinking_support(tokenizer):\n    try:\n        tokenizer.apply_chat_template(\n            [{\"role\": \"user\", \"content\": \"hi\"}],\n            tokenize=False,\n            enable_thinking=False,\n        )\n        return {\"enable_thinking\": False}\n    except TypeError:\n        return {}\n\n\ndef build_prompt_ids(tokenizer, code, test, system_prompt, user_template, tmpl_kw, max_len):\n    user_msg = user_template.format(code=code, test=test)\n    msgs = [\n        {\"role\": \"system\", \"content\": system_prompt},\n        {\"role\": \"user\", \"content\": user_msg},\n    ]\n    ids = tokenizer.apply_chat_template(\n        msgs, tokenize=True, add_generation_prompt=True, **tmpl_kw,\n    )\n    if hasattr(ids, \"input_ids\"):\n        ids = ids.input_ids\n    if not isinstance(ids, list):\n        ids = list(ids)\n    was_truncated = len(ids) >= max_len\n    if len(ids) > max_len:\n        ids = ids[:max_len]\n    return ids, was_truncated\n\n\n# ── Prediction Parsing ───────────────────────────────────────────────────────\n\ndef parse_cls_prediction(text):\n    if \"&lt;/think>\" in text:\n        text = text.split(\"&lt;/think>\")[-1]\n    text = text.strip().lower()\n    if text.startswith(\"pass\"):\n        return 1\n    if text.startswith(\"fail\"):\n        return 0\n    if \"pass\" in text and \"fail\" not in text:\n        return 1\n    if \"fail\" in text and \"pass\" not in text:\n        return 0\n    return -1\n\n\ndef parse_cwm_prediction(text):\n    if \"&lt;/think>\" in text:\n        text = text.split(\"&lt;/think>\")[-1]\n    text_lower = text.strip().lower()\n    if text_lower.startswith(\"pass\"):\n        return 1\n    if text_lower.startswith(\"fail\"):\n        return 0\n    fail_kw = [\"error\", \"assert\", \"traceback\", \"exception\", \"fail\"]\n    pass_kw = [\"pass\", \"success\", \"completed\"]\n    has_fail = any(p in text_lower for p in fail_kw)\n    has_pass = any(p in text_lower for p in pass_kw)\n    if has_fail and not has_pass:\n        return 0\n    if has_pass and not has_fail:\n        return 1\n    return 0  # default fail for CWM\n\n\n# ── Model Loading / Unloading ────────────────────────────────────────────────\n\ndef load_model(checkpoint_dir, base_model_name):\n    from peft import PeftModel\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    tokenizer = AutoTokenizer.from_pretrained(\n        checkpoint_dir, trust_remote_code=True, padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    try:\n        import flash_attn  # noqa: F401\n        attn_impl = \"flash_attention_2\"\n    except ImportError:\n        attn_impl = \"sdpa\"\n\n    base_model = AutoModelForCausalLM.from_pretrained(\n        base_model_name,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        attn_implementation=attn_impl,\n    )\n    model = PeftModel.from_pretrained(base_model, checkpoint_dir)\n    model.eval()\n    model = model.cuda()\n    return model, tokenizer\n\n\ndef unload_model(model):\n    del model\n    gc.collect()\n    torch.cuda.empty_cache()\n\n\n# ── Batched Inference ────────────────────────────────────────────────────────\n\ndef run_inference(model, tokenizer, test_data, mode, batch_size, max_seq_length):\n    \"\"\"Run inference. mode='cls' or 'cwm'. Returns list of dicts with index/problem_id/label/pred.\"\"\"\n    if mode == \"cls\":\n        sys_prompt, user_tmpl = CLS_SYSTEM, CLS_USER_TEMPLATE\n        parse_fn = parse_cls_prediction\n        max_new_tokens = 8\n    else:\n        sys_prompt, user_tmpl = CWM_SYSTEM, CWM_USER_TEMPLATE\n        parse_fn = parse_cwm_prediction\n        max_new_tokens = 64\n\n    tmpl_kw = detect_thinking_support(tokenizer)\n    total = len(test_data)\n    label_counts = Counter(ex[\"label\"] for ex in test_data)\n    majority_class = 1 if label_counts.get(1, 0) >= label_counts.get(0, 0) else 0\n\n    results = []\n    n_unparseable = 0\n\n    for i in range(0, total, batch_size):\n        batch = test_data[i : i + batch_size]\n        batch_labels = [ex[\"label\"] for ex in batch]\n\n        batch_built = [\n            build_prompt_ids(tokenizer, ex[\"code\"], ex[\"test\"],\n                             sys_prompt, user_tmpl, tmpl_kw, max_seq_length)\n            for ex in batch\n        ]\n        batch_ids = [r[0] for r in batch_built]\n        batch_truncated = [r[1] for r in batch_built]\n\n        max_len = max(len(ids) for ids in batch_ids)\n        padded = [[tokenizer.pad_token_id] * (max_len - len(ids)) + ids for ids in batch_ids]\n        attn_mask = [[0] * (max_len - len(ids)) + [1] * len(ids) for ids in batch_ids]\n\n        input_ids = torch.tensor(padded, device=\"cuda\")\n        attention_mask = torch.tensor(attn_mask, device=\"cuda\")\n\n        with torch.no_grad():\n            out = model.generate(\n                input_ids=input_ids,\n                attention_mask=attention_mask,\n                max_new_tokens=max_new_tokens,\n                do_sample=False,\n                pad_token_id=tokenizer.pad_token_id,\n            )\n\n        for j, ex in enumerate(batch):\n            gen_ids = out[j][len(padded[j]):]\n            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)\n            pred = parse_fn(gen_text)\n            if pred == -1:\n                n_unparseable += 1\n                pred = majority_class\n\n            pid = ex.get(\"problem_id\", ex.get(\"metadata\", {}).get(\"instance_id\", \"\"))\n            results.append({\n                \"index\": i + j,\n                \"problem_id\": pid,\n                \"label\": batch_labels[j],\n                \"pred\": pred,\n                \"correct\": int(pred == batch_labels[j]),\n                \"truncated\": batch_truncated[j],\n            })\n\n        done = min(i + batch_size, total)\n        if done % (batch_size * 10) == 0 or done == total:\n            log.info(f\"[{mode.upper()}] Progress: {done}/{total}\")\n\n    if n_unparseable:\n        log.warning(f\"[{mode.upper()}] {n_unparseable} unparseable predictions (majority fallback)\")\n    return results\n\n\n# ── Metrics ──────────────────────────────────────────────────────────────────\n\ndef compute_metrics(y_true, y_pred):\n    acc = accuracy_score(y_true, y_pred)\n    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)\n    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)\n    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)\n    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])\n    return {\n        \"accuracy\": round(acc * 100, 2),\n        \"f1_fail\": round(float(f1[0]) * 100, 2),\n        \"f1_pass\": round(float(f1[1]) * 100, 2),\n        \"f1_macro\": round(float(f1.mean()) * 100, 2),\n        \"precision_fail\": round(float(prec[0]) * 100, 2),\n        \"precision_pass\": round(float(prec[1]) * 100, 2),\n        \"recall_fail\": round(float(rec[0]) * 100, 2),\n        \"recall_pass\": round(float(rec[1]) * 100, 2),\n        \"confusion_matrix\": {\n            \"tn\": int(cm[0][0]), \"fp\": int(cm[0][1]),\n            \"fn\": int(cm[1][0]), \"tp\": int(cm[1][1]),\n        },\n    }\n\n\n# ── Paired Bootstrap on F1 ──────────────────────────────────────────────────\n\ndef paired_bootstrap_f1(labels, cls_preds, cwm_preds, n_bootstrap=10000, seed=42):\n    \"\"\"Paired bootstrap comparing CLS vs CWM on multiple metrics.\n\n    Returns dict with observed gaps, CIs, and p-values for f1_fail, f1_pass,\n    f1_macro, and accuracy.\n    \"\"\"\n    n = len(labels)\n    labels = np.array(labels, dtype=np.int32)\n    cls_preds = np.array(cls_preds, dtype=np.int32)\n    cwm_preds = np.array(cwm_preds, dtype=np.int32)\n\n    # Precompute per-sample binary masks for fast bootstrap\n    cls_tp0 = (labels == 0) & (cls_preds == 0)\n    cls_fp0 = (labels == 1) & (cls_preds == 0)\n    cls_fn0 = (labels == 0) & (cls_preds == 1)\n    cls_tp1 = (labels == 1) & (cls_preds == 1)\n    cls_fp1 = (labels == 0) & (cls_preds == 1)\n    cls_fn1 = (labels == 1) & (cls_preds == 0)\n\n    cwm_tp0 = (labels == 0) & (cwm_preds == 0)\n    cwm_fp0 = (labels == 1) & (cwm_preds == 0)\n    cwm_fn0 = (labels == 0) & (cwm_preds == 1)\n    cwm_tp1 = (labels == 1) & (cwm_preds == 1)\n    cwm_fp1 = (labels == 0) & (cwm_preds == 1)\n    cwm_fn1 = (labels == 1) & (cwm_preds == 0)\n\n    cls_correct = (cls_preds == labels)\n    cwm_correct = (cwm_preds == labels)\n\n    def f1_from_counts(tp, fp, fn):\n        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n        return 2 * prec * rec / (prec + rec) * 100 if (prec + rec) > 0 else 0.0\n\n    def compute_all(idx):\n        c_tp0 = cls_tp0[idx].sum(); c_fp0 = cls_fp0[idx].sum(); c_fn0 = cls_fn0[idx].sum()\n        c_tp1 = cls_tp1[idx].sum(); c_fp1 = cls_fp1[idx].sum(); c_fn1 = cls_fn1[idx].sum()\n        w_tp0 = cwm_tp0[idx].sum(); w_fp0 = cwm_fp0[idx].sum(); w_fn0 = cwm_fn0[idx].sum()\n        w_tp1 = cwm_tp1[idx].sum(); w_fp1 = cwm_fp1[idx].sum(); w_fn1 = cwm_fn1[idx].sum()\n\n        cls_f1_0 = f1_from_counts(c_tp0, c_fp0, c_fn0)\n        cls_f1_1 = f1_from_counts(c_tp1, c_fp1, c_fn1)\n        cwm_f1_0 = f1_from_counts(w_tp0, w_fp0, w_fn0)\n        cwm_f1_1 = f1_from_counts(w_tp1, w_fp1, w_fn1)\n\n        cls_acc = cls_correct[idx].mean() * 100\n        cwm_acc = cwm_correct[idx].mean() * 100\n\n        return {\n            \"f1_fail\": cls_f1_0 - cwm_f1_0,\n            \"f1_pass\": cls_f1_1 - cwm_f1_1,\n            \"f1_macro\": (cls_f1_0 + cls_f1_1) / 2 - (cwm_f1_0 + cwm_f1_1) / 2,\n            \"accuracy\": cls_acc - cwm_acc,\n        }\n\n    # Observed gaps\n    obs = compute_all(np.arange(n))\n\n    # Bootstrap\n    rng = np.random.RandomState(seed)\n    boot = {k: np.zeros(n_bootstrap) for k in obs}\n\n    for b in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        gaps = compute_all(idx)\n        for k in obs:\n            boot[k][b] = gaps[k]\n\n    results = {}\n    for k in obs:\n        ci_lo, ci_hi = np.percentile(boot[k], [2.5, 97.5])\n        p_val = float((boot[k] <= 0).mean())\n        results[k] = {\n            \"observed_gap_pp\": round(obs[k], 2),\n            \"ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n            \"p_value_one_sided\": round(p_val, 4),\n        }\n\n    # Disagreement analysis\n    both_right = int(((cls_correct) & (cwm_correct)).sum())\n    both_wrong = int(((~cls_correct) & (~cwm_correct)).sum())\n    cls_only = int(((cls_correct) & (~cwm_correct)).sum())\n    cwm_only = int(((~cls_correct) & (cwm_correct)).sum())\n    results[\"disagreement\"] = {\n        \"both_correct\": both_right,\n        \"both_wrong\": both_wrong,\n        \"cls_only_correct\": cls_only,\n        \"cwm_only_correct\": cwm_only,\n    }\n\n    return results\n\n\n# ── D008 Decision ────────────────────────────────────────────────────────────\n\ndef d008_decision(gap_pp, p_value):\n    \"\"\"Apply D008 Go/No-Go criteria based on F1 macro gap.\"\"\"\n    if gap_pp >= 3.0 and p_value < 0.05:\n        return \"GO_EMNLP_MAIN\", \"F1 gap >= 3pp + p<0.05 → full push EMNLP Main\"\n    elif gap_pp >= 1.0:\n        return \"ADD_SEEDS\", \"1pp <= F1 gap < 3pp (or p>=0.05) → add seeds/data for power\"\n    else:\n        return \"KILL_C1\", \"F1 gap < 1pp → kill C1 hypothesis, pivot Plan B\"\n\n\n# ── Report ───────────────────────────────────────────────────────────────────\n\ndef print_report(cls_metrics, cwm_metrics, bootstrap, decision, decision_msg, n_instances):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"REPO-LEVEL EVALUATION: CLS vs CWM (Paired Bootstrap on F1)\")\n    print(\"=\" * 70)\n\n    print(f\"\\nInstances: {n_instances}\")\n\n    for name, m in [(\"CLS (verifier)\", cls_metrics), (\"CWM (generation)\", cwm_metrics)]:\n        print(f\"\\n--- {name} ---\")\n        print(f\"  Accuracy: {m['accuracy']:.2f}%\")\n        print(f\"  F1 macro: {m['f1_macro']:.2f}%\")\n        print(f\"  F1  fail={m['f1_fail']:.2f}%  pass={m['f1_pass']:.2f}%\")\n        print(f\"  Prec fail={m['precision_fail']:.2f}%  pass={m['precision_pass']:.2f}%\")\n        print(f\"  Rec  fail={m['recall_fail']:.2f}%  pass={m['recall_pass']:.2f}%\")\n\n    print(f\"\\n{'─' * 70}\")\n    print(\"PAIRED BOOTSTRAP (10000 resamples)\")\n    print(f\"{'─' * 70}\")\n    for metric_name in [\"f1_macro\", \"f1_fail\", \"f1_pass\", \"accuracy\"]:\n        b = bootstrap[metric_name]\n        sig = \"***\" if b[\"p_value_one_sided\"] < 0.001 else \"**\" if b[\"p_value_one_sided\"] < 0.01 else \"*\" if b[\"p_value_one_sided\"] < 0.05 else \"ns\"\n        print(f\"  {metric_name:<12} gap={b['observed_gap_pp']:+.2f}pp  \"\n              f\"CI95=[{b['ci_95'][0]:+.2f}, {b['ci_95'][1]:+.2f}]  \"\n              f\"p={b['p_value_one_sided']:.4f} {sig}\")\n\n    d = bootstrap[\"disagreement\"]\n    print(f\"\\n  Disagreement: both_ok={d['both_correct']}  both_wrong={d['both_wrong']}  \"\n          f\"cls_only={d['cls_only_correct']}  cwm_only={d['cwm_only_correct']}\")\n\n    print(f\"\\n{'─' * 70}\")\n    print(\"D008 GO/NO-GO (based on F1 macro)\")\n    print(f\"{'─' * 70}\")\n    gap = bootstrap[\"f1_macro\"][\"observed_gap_pp\"]\n    p = bootstrap[\"f1_macro\"][\"p_value_one_sided\"]\n    print(f\"  F1 macro gap: {gap:+.2f}pp  p={p:.4f}\")\n    print(f\"  Decision: {decision}\")\n    print(f\"  {decision_msg}\")\n    print(\"=\" * 70)\n\n\n# ── Main ─────────────────────────────────────────────────────────────────────\n\ndef main():\n    p = argparse.ArgumentParser(\n        description=\"Unified repo-level CLS vs CWM evaluation with paired bootstrap on F1\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"Examples:\n  # Full inference + bootstrap:\n  python eval_repo_level.py --cls_checkpoint /path/to/cls --cwm_checkpoint /path/to/cwm\n\n  # Bootstrap from existing predictions:\n  python eval_repo_level.py --cls_preds cls_predictions.jsonl --cwm_preds cwm_predictions.jsonl\n\n  # Dry-run (test data loading only):\n  python eval_repo_level.py --dry_run\n\"\"\")\n\n    # Inference mode args\n    p.add_argument(\"--cls_checkpoint\", help=\"CLS LoRA checkpoint dir (inference mode)\")\n    p.add_argument(\"--cwm_checkpoint\", help=\"CWM LoRA checkpoint dir (inference mode)\")\n    p.add_argument(\"--model_name\", default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B\",\n                   help=\"Base model path\")\n\n    # Predictions mode args\n    p.add_argument(\"--cls_preds\", help=\"Existing CLS predictions JSONL (skip inference)\")\n    p.add_argument(\"--cwm_preds\", help=\"Existing CWM predictions JSONL (skip inference)\")\n\n    # Common args\n    p.add_argument(\"--data_dir\", default=\"/home/sonny/exec-sim-repair-verifier/data/swebench_full\")\n    p.add_argument(\"--output\", default=\"eval_repo_level_results.json\")\n    p.add_argument(\"--batch_size\", type=int, default=16)\n    p.add_argument(\"--max_seq_length\", type=int, default=2048)\n    p.add_argument(\"--device\", default=\"cuda:0\")\n    p.add_argument(\"--n_bootstrap\", type=int, default=10000)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--save_predictions\", action=\"store_true\",\n                   help=\"Save per-instance prediction JSONL files\")\n    p.add_argument(\"--dry_run\", action=\"store_true\",\n                   help=\"Only test data loading and arg parsing, no model inference\")\n\n    args = p.parse_args()\n\n    # Validate args\n    inference_mode = args.cls_checkpoint and args.cwm_checkpoint\n    preds_mode = args.cls_preds and args.cwm_preds\n\n    if args.dry_run:\n        test_data = load_jsonl(os.path.join(args.data_dir, \"swebench_test.jsonl\"))\n        label_counts = Counter(ex[\"label\"] for ex in test_data)\n        print(f\"Dry run OK. Test set: {len(test_data)} examples. \"\n              f\"Labels: pass={label_counts.get(1,0)} fail={label_counts.get(0,0)}\")\n        print(f\"Data fields: {list(test_data[0].keys())}\")\n        print(f\"Args: {vars(args)}\")\n        return\n\n    if not inference_mode and not preds_mode:\n        p.error(\"Provide either (--cls_checkpoint + --cwm_checkpoint) or (--cls_preds + --cwm_preds)\")\n\n    # ── Obtain predictions ───────────────────────────────────────────────\n    if inference_mode:\n        os.environ[\"CUDA_VISIBLE_DEVICES\"] = args.device.replace(\"cuda:\", \"\")\n        test_data = load_jsonl(os.path.join(args.data_dir, \"swebench_test.jsonl\"))\n        log.info(f\"Test set: {len(test_data)} examples\")\n\n        # CLS inference\n        log.info(\"=== CLS Inference ===\")\n        cls_model, cls_tok = load_model(args.cls_checkpoint, args.model_name)\n        cls_results = run_inference(cls_model, cls_tok, test_data, \"cls\",\n                                    args.batch_size, args.max_seq_length)\n        unload_model(cls_model)\n        del cls_tok\n        log.info(\"CLS model unloaded, GPU memory freed\")\n\n        # CWM inference\n        log.info(\"=== CWM Inference ===\")\n        cwm_model, cwm_tok = load_model(args.cwm_checkpoint, args.model_name)\n        cwm_results = run_inference(cwm_model, cwm_tok, test_data, \"cwm\",\n                                    args.batch_size, args.max_seq_length)\n        unload_model(cwm_model)\n        del cwm_tok\n        log.info(\"CWM model unloaded\")\n\n    else:  # predictions mode\n        log.info(f\"Loading CLS predictions: {args.cls_preds}\")\n        cls_results = [json.loads(l) for l in open(args.cls_preds)]\n        log.info(f\"Loading CWM predictions: {args.cwm_preds}\")\n        cwm_results = [json.loads(l) for l in open(args.cwm_preds)]\n\n    # ── Align predictions by (index, problem_id) ────────────────────────\n    cls_by_key = {(r[\"index\"], r.get(\"problem_id\", \"\")): r for r in cls_results}\n    cwm_by_key = {(r[\"index\"], r.get(\"problem_id\", \"\")): r for r in cwm_results}\n    shared_keys = sorted(set(cls_by_key) & set(cwm_by_key))\n\n    if not shared_keys:\n        log.error(\"No shared instances between CLS and CWM predictions\")\n        sys.exit(1)\n\n    n_cls_only = len(cls_by_key) - len(shared_keys)\n    n_cwm_only = len(cwm_by_key) - len(shared_keys)\n    if n_cls_only or n_cwm_only:\n        log.warning(f\"{n_cls_only} CLS-only, {n_cwm_only} CWM-only instances excluded. \"\n                     f\"Using {len(shared_keys)} shared.\")\n\n    labels = [cls_by_key[k][\"label\"] for k in shared_keys]\n    cls_preds = [cls_by_key[k][\"pred\"] for k in shared_keys]\n    cwm_preds = [cwm_by_key[k][\"pred\"] for k in shared_keys]\n\n    # ── Compute per-model metrics ────────────────────────────────────────\n    cls_metrics = compute_metrics(labels, cls_preds)\n    cwm_metrics = compute_metrics(labels, cwm_preds)\n\n    # ── Paired bootstrap ─────────────────────────────────────────────────\n    log.info(f\"Running paired bootstrap ({args.n_bootstrap} resamples) ...\")\n    bootstrap = paired_bootstrap_f1(labels, cls_preds, cwm_preds,\n                                     n_bootstrap=args.n_bootstrap, seed=args.seed)\n\n    # ── D008 decision ────────────────────────────────────────────────────\n    f1_gap = bootstrap[\"f1_macro\"][\"observed_gap_pp\"]\n    f1_p = bootstrap[\"f1_macro\"][\"p_value_one_sided\"]\n    decision, decision_msg = d008_decision(f1_gap, f1_p)\n\n    # ── Report ───────────────────────────────────────────────────────────\n    print_report(cls_metrics, cwm_metrics, bootstrap, decision, decision_msg, len(shared_keys))\n\n    # ── Save JSON ────────────────────────────────────────────────────────\n    output = {\n        \"n_instances\": len(shared_keys),\n        \"cls_metrics\": cls_metrics,\n        \"cwm_metrics\": cwm_metrics,\n        \"bootstrap\": bootstrap,\n        \"d008_decision\": decision,\n        \"d008_decision_msg\": decision_msg,\n        \"config\": {\n            \"n_bootstrap\": args.n_bootstrap,\n            \"seed\": args.seed,\n            \"max_seq_length\": args.max_seq_length,\n        },\n    }\n\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    log.info(f\"Results saved to {args.output}\")\n\n    # ── Save predictions ─────────────────────────────────────────────────\n    if args.save_predictions and inference_mode:\n        stem = os.path.splitext(args.output)[0]\n        for name, preds in [(\"cls\", cls_results), (\"cwm\", cwm_results)]:\n            path = f\"{stem}_{name}_predictions.jsonl\"\n            with open(path, \"w\") as f:\n                for r in preds:\n                    f.write(json.dumps(r) + \"\\n\")\n            log.info(f\"{name.upper()} predictions saved to {path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nENDOFSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat > /home/sonny/exec-sim-repair-verifier/eval_repo_level.py << 'ENDOFSCRIPT'\n# eval_repo_level.py — Unified repo-level CLS vs CWM evaluation + paired bootstrap on F1\n# Input:\n#   Mode 1 (inference): --cls_checkpoint + --cwm_checkpoint + test JSONL\n#   Mode 2 (predictions only): --cls_preds + --cwm_preds (skip inference)\n# Output: JSON results + human-readable summary with D008 Go/No-Go decision\n# Dependencies: torch, transformers, peft, sklearn, numpy\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport gc\nfrom collections import Counter\n\nimport numpy as np\nimport torch\nfrom sklearn.metrics import (\n    accuracy_score,\n    confusion_matrix,\n    f1_score,\n    precision_score,\n    recall_score,\n)\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlog = logging.getLogger(__name__)\n\n# ── Prompts ──────────────────────────────────────────────────────────────────\n\nCLS_SYSTEM = (\n    \"You are a code verifier. Given a code patch (git diff) and a test name, \"\n    \"predict whether the test will pass or fail when run against the patched code.\"\n)\nCLS_USER_TEMPLATE = \"## Patch (git diff)\\n{code}\\n\\n## Test\\n{test}\\n\\nWill this test pass or fail?\"\n\nCWM_SYSTEM = (\n    \"You are a code execution simulator. Given a code patch (git diff) and a test name, \"\n    \"predict the execution result when the test is run against the patched code.\"\n)\nCWM_USER_TEMPLATE = \"## Patch (git diff)\\n{code}\\n\\n## Test\\n{test}\\n\\nWhat is the execution result?\"\n\n\n# ── Data / Tokenizer Helpers ─────────────────────────────────────────────────\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef detect_thinking_support(tokenizer):\n    try:\n        tokenizer.apply_chat_template(\n            [{\"role\": \"user\", \"content\": \"hi\"}],\n            tokenize=False,\n            enable_thinking=False,\n        )\n        return {\"enable_thinking\": False}\n    except TypeError:\n        return {}\n\n\ndef build_prompt_ids(tokenizer, code, test, system_prompt, user_template, tmpl_kw, max_len):\n    user_msg = user_template.format(code=code, test=test)\n    msgs = [\n        {\"role\": \"system\", \"content\": system_prompt},\n        {\"role\": \"user\", \"content\": user_msg},\n    ]\n    ids = tokenizer.apply_chat_template(\n        msgs, tokenize=True, add_generation_prompt=True, **tmpl_kw,\n    )\n    if hasattr(ids, \"input_ids\"):\n        ids = ids.input_ids\n    if not isinstance(ids, list):\n        ids = list(ids)\n    was_truncated = len(ids) >= max_len\n    if len(ids) > max_len:\n        ids = ids[:max_len]\n    return ids, was_truncated\n\n\n# ── Prediction Parsing ───────────────────────────────────────────────────────\n\ndef parse_cls_prediction(text):\n    if \"&lt;/think>\" in text:\n        text = text.split(\"&lt;/think>\")[-1]\n    text = text.strip().lower()\n    if text.startswith(\"pass\"):\n        return 1\n    if text.startswith(\"fail\"):\n        return 0\n    if \"pass\" in text and \"fail\" not in text:\n        return 1\n    if \"fail\" in text and \"pass\" not in text:\n        return 0\n    return -1\n\n\ndef parse_cwm_prediction(text):\n    if \"&lt;/think>\" in text:\n        text = text.split(\"&lt;/think>\")[-1]\n    text_lower = text.strip().lower()\n    if text_lower.startswith(\"pass\"):\n        return 1\n    if text_lower.startswith(\"fail\"):\n        return 0\n    fail_kw = [\"error\", \"assert\", \"traceback\", \"exception\", \"fail\"]\n    pass_kw = [\"pass\", \"success\", \"completed\"]\n    has_fail = any(p in text_lower for p in fail_kw)\n    has_pass = any(p in text_lower for p in pass_kw)\n    if has_fail and not has_pass:\n        return 0\n    if has_pass and not has_fail:\n        return 1\n    return 0  # default fail for CWM\n\n\n# ── Model Loading / Unloading ────────────────────────────────────────────────\n\ndef load_model(checkpoint_dir, base_model_name):\n    from peft import PeftModel\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    tokenizer = AutoTokenizer.from_pretrained(\n        checkpoint_dir, trust_remote_code=True, padding_side=\"left\",\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    try:\n        import flash_attn  # noqa: F401\n        attn_impl = \"flash_attention_2\"\n    except ImportError:\n        attn_impl = \"sdpa\"\n\n    base_model = AutoModelForCausalLM.from_pretrained(\n        base_model_name,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        attn_implementation=attn_impl,\n    )\n    model = PeftModel.from_pretrained(base_model, checkpoint_dir)\n    model.eval()\n    model = model.cuda()\n    return model, tokenizer\n\n\ndef unload_model(model):\n    del model\n    gc.collect()\n    torch.cuda.empty_cache()\n\n\n# ── Batched Inference ────────────────────────────────────────────────────────\n\ndef run_inference(model, tokenizer, test_data, mode, batch_size, max_seq_length):\n    \"\"\"Run inference. mode='cls' or 'cwm'. Returns list of dicts with index/problem_id/label/pred.\"\"\"\n    if mode == \"cls\":\n        sys_prompt, user_tmpl = CLS_SYSTEM, CLS_USER_TEMPLATE\n        parse_fn = parse_cls_prediction\n        max_new_tokens = 8\n    else:\n        sys_prompt, user_tmpl = CWM_SYSTEM, CWM_USER_TEMPLATE\n        parse_fn = parse_cwm_prediction\n        max_new_tokens = 64\n\n    tmpl_kw = detect_thinking_support(tokenizer)\n    total = len(test_data)\n    label_counts = Counter(ex[\"label\"] for ex in test_data)\n    majority_class = 1 if label_counts.get(1, 0) >= label_counts.get(0, 0) else 0\n\n    results = []\n    n_unparseable = 0\n\n    for i in range(0, total, batch_size):\n        batch = test_data[i : i + batch_size]\n        batch_labels = [ex[\"label\"] for ex in batch]\n\n        batch_built = [\n            build_prompt_ids(tokenizer, ex[\"code\"], ex[\"test\"],\n                             sys_prompt, user_tmpl, tmpl_kw, max_seq_length)\n            for ex in batch\n        ]\n        batch_ids = [r[0] for r in batch_built]\n        batch_truncated = [r[1] for r in batch_built]\n\n        max_len = max(len(ids) for ids in batch_ids)\n        padded = [[tokenizer.pad_token_id] * (max_len - len(ids)) + ids for ids in batch_ids]\n        attn_mask = [[0] * (max_len - len(ids)) + [1] * len(ids) for ids in batch_ids]\n\n        input_ids = torch.tensor(padded, device=\"cuda\")\n        attention_mask = torch.tensor(attn_mask, device=\"cuda\")\n\n        with torch.no_grad():\n            out = model.generate(\n                input_ids=input_ids,\n                attention_mask=attention_mask,\n                max_new_tokens=max_new_tokens,\n                do_sample=False,\n                pad_token_id=tokenizer.pad_token_id,\n            )\n\n        for j, ex in enumerate(batch):\n            gen_ids = out[j][len(padded[j]):]\n            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)\n            pred = parse_fn(gen_text)\n            if pred == -1:\n                n_unparseable += 1\n                pred = majority_class\n\n            pid = ex.get(\"problem_id\", ex.get(\"metadata\", {}).get(\"instance_id\", \"\"))\n            results.append({\n                \"index\": i + j,\n                \"problem_id\": pid,\n                \"label\": batch_labels[j],\n                \"pred\": pred,\n                \"correct\": int(pred == batch_labels[j]),\n                \"truncated\": batch_truncated[j],\n            })\n\n        done = min(i + batch_size, total)\n        if done % (batch_size * 10) == 0 or done == total:\n            log.info(f\"[{mode.upper()}] Progress: {done}/{total}\")\n\n    if n_unparseable:\n        log.warning(f\"[{mode.upper()}] {n_unparseable} unparseable predictions (majority fallback)\")\n    return results\n\n\n# ── Metrics ──────────────────────────────────────────────────────────────────\n\ndef compute_metrics(y_true, y_pred):\n    acc = accuracy_score(y_true, y_pred)\n    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)\n    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)\n    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)\n    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])\n    return {\n        \"accuracy\": round(acc * 100, 2),\n        \"f1_fail\": round(float(f1[0]) * 100, 2),\n        \"f1_pass\": round(float(f1[1]) * 100, 2),\n        \"f1_macro\": round(float(f1.mean()) * 100, 2),\n        \"precision_fail\": round(float(prec[0]) * 100, 2),\n        \"precision_pass\": round(float(prec[1]) * 100, 2),\n        \"recall_fail\": round(float(rec[0]) * 100, 2),\n        \"recall_pass\": round(float(rec[1]) * 100, 2),\n        \"confusion_matrix\": {\n            \"tn\": int(cm[0][0]), \"fp\": int(cm[0][1]),\n            \"fn\": int(cm[1][0]), \"tp\": int(cm[1][1]),\n        },\n    }\n\n\n# ── Paired Bootstrap on F1 ──────────────────────────────────────────────────\n\ndef paired_bootstrap_f1(labels, cls_preds, cwm_preds, n_bootstrap=10000, seed=42):\n    \"\"\"Paired bootstrap comparing CLS vs CWM on multiple metrics.\n\n    Returns dict with observed gaps, CIs, and p-values for f1_fail, f1_pass,\n    f1_macro, and accuracy.\n    \"\"\"\n    n = len(labels)\n    labels = np.array(labels, dtype=np.int32)\n    cls_preds = np.array(cls_preds, dtype=np.int32)\n    cwm_preds = np.array(cwm_preds, dtype=np.int32)\n\n    # Precompute per-sample binary masks for fast bootstrap\n    cls_tp0 = (labels == 0) & (cls_preds == 0)\n    cls_fp0 = (labels == 1) & (cls_preds == 0)\n    cls_fn0 = (labels == 0) & (cls_preds == 1)\n    cls_tp1 = (labels == 1) & (cls_preds == 1)\n    cls_fp1 = (labels == 0) & (cls_preds == 1)\n    cls_fn1 = (labels == 1) & (cls_preds == 0)\n\n    cwm_tp0 = (labels == 0) & (cwm_preds == 0)\n    cwm_fp0 = (labels == 1) & (cwm_preds == 0)\n    cwm_fn0 = (labels == 0) & (cwm_preds == 1)\n    cwm_tp1 = (labels == 1) & (cwm_preds == 1)\n    cwm_fp1 = (labels == 0) & (cwm_preds == 1)\n    cwm_fn1 = (labels == 1) & (cwm_preds == 0)\n\n    cls_correct = (cls_preds == labels)\n    cwm_correct = (cwm_preds == labels)\n\n    def f1_from_counts(tp, fp, fn):\n        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n        return 2 * prec * rec / (prec + rec) * 100 if (prec + rec) > 0 else 0.0\n\n    def compute_all(idx):\n        c_tp0 = cls_tp0[idx].sum(); c_fp0 = cls_fp0[idx].sum(); c_fn0 = cls_fn0[idx].sum()\n        c_tp1 = cls_tp1[idx].sum(); c_fp1 = cls_fp1[idx].sum(); c_fn1 = cls_fn1[idx].sum()\n        w_tp0 = cwm_tp0[idx].sum(); w_fp0 = cwm_fp0[idx].sum(); w_fn0 = cwm_fn0[idx].sum()\n        w_tp1 = cwm_tp1[idx].sum(); w_fp1 = cwm_fp1[idx].sum(); w_fn1 = cwm_fn1[idx].sum()\n\n        cls_f1_0 = f1_from_counts(c_tp0, c_fp0, c_fn0)\n        cls_f1_1 = f1_from_counts(c_tp1, c_fp1, c_fn1)\n        cwm_f1_0 = f1_from_counts(w_tp0, w_fp0, w_fn0)\n        cwm_f1_1 = f1_from_counts(w_tp1, w_fp1, w_fn1)\n\n        cls_acc = cls_correct[idx].mean() * 100\n        cwm_acc = cwm_correct[idx].mean() * 100\n\n        return {\n            \"f1_fail\": cls_f1_0 - cwm_f1_0,\n            \"f1_pass\": cls_f1_1 - cwm_f1_1,\n            \"f1_macro\": (cls_f1_0 + cls_f1_1) / 2 - (cwm_f1_0 + cwm_f1_1) / 2,\n            \"accuracy\": cls_acc - cwm_acc,\n        }\n\n    # Observed gaps\n    obs = compute_all(np.arange(n))\n\n    # Bootstrap\n    rng = np.random.RandomState(seed)\n    boot = {k: np.zeros(n_bootstrap) for k in obs}\n\n    for b in range(n_bootstrap):\n        idx = rng.randint(0, n, size=n)\n        gaps = compute_all(idx)\n        for k in obs:\n            boot[k][b] = gaps[k]\n\n    results = {}\n    for k in obs:\n        ci_lo, ci_hi = np.percentile(boot[k], [2.5, 97.5])\n        p_val = float((boot[k] <= 0).mean())\n        results[k] = {\n            \"observed_gap_pp\": round(obs[k], 2),\n            \"ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n            \"p_value_one_sided\": round(p_val, 4),\n        }\n\n    # Disagreement analysis\n    both_right = int(((cls_correct) & (cwm_correct)).sum())\n    both_wrong = int(((~cls_correct) & (~cwm_correct)).sum())\n    cls_only = int(((cls_correct) & (~cwm_correct)).sum())\n    cwm_only = int(((~cls_correct) & (cwm_correct)).sum())\n    results[\"disagreement\"] = {\n        \"both_correct\": both_right,\n        \"both_wrong\": both_wrong,\n        \"cls_only_correct\": cls_only,\n        \"cwm_only_correct\": cwm_only,\n    }\n\n    return results\n\n\n# ── D008 Decision ────────────────────────────────────────────────────────────\n\ndef d008_decision(gap_pp, p_value):\n    \"\"\"Apply D008 Go/No-Go criteria based on F1 macro gap.\"\"\"\n    if gap_pp >= 3.0 and p_value < 0.05:\n        return \"GO_EMNLP_MAIN\", \"F1 gap >= 3pp + p<0.05 → full push EMNLP Main\"\n    elif gap_pp >= 1.0:\n        return \"ADD_SEEDS\", \"1pp <= F1 gap < 3pp (or p>=0.05) → add seeds/data for power\"\n    else:\n        return \"KILL_C1\", \"F1 gap < 1pp → kill C1 hypothesis, pivot Plan B\"\n\n\n# ── Report ───────────────────────────────────────────────────────────────────\n\ndef print_report(cls_metrics, cwm_metrics, bootstrap, decision, decision_msg, n_instances):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"REPO-LEVEL EVALUATION: CLS vs CWM (Paired Bootstrap on F1)\")\n    print(\"=\" * 70)\n\n    print(f\"\\nInstances: {n_instances}\")\n\n    for name, m in [(\"CLS (verifier)\", cls_metrics), (\"CWM (generation)\", cwm_metrics)]:\n        print(f\"\\n--- {name} ---\")\n        print(f\"  Accuracy: {m['accuracy']:.2f}%\")\n        print(f\"  F1 macro: {m['f1_macro']:.2f}%\")\n        print(f\"  F1  fail={m['f1_fail']:.2f}%  pass={m['f1_pass']:.2f}%\")\n        print(f\"  Prec fail={m['precision_fail']:.2f}%  pass={m['precision_pass']:.2f}%\")\n        print(f\"  Rec  fail={m['recall_fail']:.2f}%  pass={m['recall_pass']:.2f}%\")\n\n    print(f\"\\n{'─' * 70}\")\n    print(\"PAIRED BOOTSTRAP (10000 resamples)\")\n    print(f\"{'─' * 70}\")\n    for metric_name in [\"f1_macro\", \"f1_fail\", \"f1_pass\", \"accuracy\"]:\n        b = bootstrap[metric_name]\n        sig = \"***\" if b[\"p_value_one_sided\"] < 0.001 else \"**\" if b[\"p_value_one_sided\"] < 0.01 else \"*\" if b[\"p_value_one_sided\"] < 0.05 else \"ns\"\n        print(f\"  {metric_name:<12} gap={b['observed_gap_pp']:+.2f}pp  \"\n              f\"CI95=[{b['ci_95'][0]:+.2f}, {b['ci_95'][1]:+.2f}]  \"\n              f\"p={b['p_value_one_sided']:.4f} {sig}\")\n\n    d = bootstrap[\"disagreement\"]\n    print(f\"\\n  Disagreement: both_ok={d['both_correct']}  both_wrong={d['both_wrong']}  \"\n          f\"cls_only={d['cls_only_correct']}  cwm_only={d['cwm_only_correct']}\")\n\n    print(f\"\\n{'─' * 70}\")\n    print(\"D008 GO/NO-GO (based on F1 macro)\")\n    print(f\"{'─' * 70}\")\n    gap = bootstrap[\"f1_macro\"][\"observed_gap_pp\"]\n    p = bootstrap[\"f1_macro\"][\"p_value_one_sided\"]\n    print(f\"  F1 macro gap: {gap:+.2f}pp  p={p:.4f}\")\n    print(f\"  Decision: {decision}\")\n    print(f\"  {decision_msg}\")\n    print(\"=\" * 70)\n\n\n# ── Main ─────────────────────────────────────────────────────────────────────\n\ndef main():\n    p = argparse.ArgumentParser(\n        description=\"Unified repo-level CLS vs CWM evaluation with paired bootstrap on F1\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"Examples:\n  # Full inference + bootstrap:\n  python eval_repo_level.py --cls_checkpoint /path/to/cls --cwm_checkpoint /path/to/cwm\n\n  # Bootstrap from existing predictions:\n  python eval_repo_level.py --cls_preds cls_predictions.jsonl --cwm_preds cwm_predictions.jsonl\n\n  # Dry-run (test data loading only):\n  python eval_repo_level.py --dry_run\n\"\"\")\n\n    # Inference mode args\n    p.add_argument(\"--cls_checkpoint\", help=\"CLS LoRA checkpoint dir (inference mode)\")\n    p.add_argument(\"--cwm_checkpoint\", help=\"CWM LoRA checkpoint dir (inference mode)\")\n    p.add_argument(\"--model_name\", default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B\",\n                   help=\"Base model path\")\n\n    # Predictions mode args\n    p.add_argument(\"--cls_preds\", help=\"Existing CLS predictions JSONL (skip inference)\")\n    p.add_argument(\"--cwm_preds\", help=\"Existing CWM predictions JSONL (skip inference)\")\n\n    # Common args\n    p.add_argument(\"--data_dir\", default=\"/home/sonny/exec-sim-repair-verifier/data/swebench_full\")\n    p.add_argument(\"--output\", default=\"eval_repo_level_results.json\")\n    p.add_argument(\"--batch_size\", type=int, default=16)\n    p.add_argument(\"--max_seq_length\", type=int, default=2048)\n    p.add_argument(\"--device\", default=\"cuda:0\")\n    p.add_argument(\"--n_bootstrap\", type=int, default=10000)\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--save_predictions\", action=\"store_true\",\n                   help=\"Save per-instance prediction JSONL files\")\n    p.add_argument(\"--dry_run\", action=\"store_true\",\n                   help=\"Only test data loading and arg parsing, no model inference\")\n\n    args = p.parse_args()\n\n    # Validate args\n    inference_mode = args.cls_checkpoint and args.cwm_checkpoint\n    preds_mode = args.cls_preds and args.cwm_preds\n\n    if args.dry_run:\n        test_data = load_jsonl(os.path.join(args.data_dir, \"swebench_test.jsonl\"))\n        label_counts = Counter(ex[\"label\"] for ex in test_data)\n        print(f\"Dry run OK. Test set: {len(test_data)} examples. \"\n              f\"Labels: pass={label_counts.get(1,0)} fail={label_counts.get(0,0)}\")\n        print(f\"Data fields: {list(test_data[0].keys())}\")\n        print(f\"Args: {vars(args)}\")\n        return\n\n    if not inference_mode and not preds_mode:\n        p.error(\"Provide either (--cls_checkpoint + --cwm_checkpoint) or (--cls_preds + --cwm_preds)\")\n\n    # ── Obtain predictions ───────────────────────────────────────────────\n    if inference_mode:\n        os.environ[\"CUDA_VISIBLE_DEVICES\"] = args.device.replace(\"cuda:\", \"\")\n        test_data = load_jsonl(os.path.join(args.data_dir, \"swebench_test.jsonl\"))\n        log.info(f\"Test set: {len(test_data)} examples\")\n\n        # CLS inference\n        log.info(\"=== CLS Inference ===\")\n        cls_model, cls_tok = load_model(args.cls_checkpoint, args.model_name)\n        cls_results = run_inference(cls_model, cls_tok, test_data, \"cls\",\n                                    args.batch_size, args.max_seq_length)\n        unload_model(cls_model)\n        del cls_tok\n        log.info(\"CLS model unloaded, GPU memory freed\")\n\n        # CWM inference\n        log.info(\"=== CWM Inference ===\")\n        cwm_model, cwm_tok = load_model(args.cwm_checkpoint, args.model_name)\n        cwm_results = run_inference(cwm_model, cwm_tok, test_data, \"cwm\",\n                                    args.batch_size, args.max_seq_length)\n        unload_model(cwm_model)\n        del cwm_tok\n        log.info(\"CWM model unloaded\")\n\n    else:  # predictions mode\n        log.info(f\"Loading CLS predictions: {args.cls_preds}\")\n        cls_results = [json.loads(l) for l in open(args.cls_preds)]\n        log.info(f\"Loading CWM predictions: {args.cwm_preds}\")\n        cwm_results = [json.loads(l) for l in open(args.cwm_preds)]\n\n    # ── Align predictions by (index, problem_id) ────────────────────────\n    cls_by_key = {(r[\"index\"], r.get(\"problem_id\", \"\")): r for r in cls_results}\n    cwm_by_key = {(r[\"index\"], r.get(\"problem_id\", \"\")): r for r in cwm_results}\n    shared_keys = sorted(set(cls_by_key) & set(cwm_by_key))\n\n    if not shared_keys:\n        log.error(\"No shared instances between CLS and CWM predictions\")\n        sys.exit(1)\n\n    n_cls_only = len(cls_by_key) - len(shared_keys)\n    n_cwm_only = len(cwm_by_key) - len(shared_keys)\n    if n_cls_only or n_cwm_only:\n        log.warning(f\"{n_cls_only} CLS-only, {n_cwm_only} CWM-only instances excluded. \"\n                     f\"Using {len(shared_keys)} shared.\")\n\n    labels = [cls_by_key[k][\"label\"] for k in shared_keys]\n    cls_preds = [cls_by_key[k][\"pred\"] for k in shared_keys]\n    cwm_preds = [cwm_by_key[k][\"pred\"] for k in shared_keys]\n\n    # ── Compute per-model metrics ────────────────────────────────────────\n    cls_metrics = compute_metrics(labels, cls_preds)\n    cwm_metrics = compute_metrics(labels, cwm_preds)\n\n    # ── Paired bootstrap ─────────────────────────────────────────────────\n    log.info(f\"Running paired bootstrap ({args.n_bootstrap} resamples) ...\")\n    bootstrap = paired_bootstrap_f1(labels, cls_preds, cwm_preds,\n                                     n_bootstrap=args.n_bootstrap, seed=args.seed)\n\n    # ── D008 decision ────────────────────────────────────────────────────\n    f1_gap = bootstrap[\"f1_macro\"][\"observed_gap_pp\"]\n    f1_p = bootstrap[\"f1_macro\"][\"p_value_one_sided\"]\n    decision, decision_msg = d008_decision(f1_gap, f1_p)\n\n    # ── Report ───────────────────────────────────────────────────────────\n    print_report(cls_metrics, cwm_metrics, bootstrap, decision, decision_msg, len(shared_keys))\n\n    # ── Save JSON ────────────────────────────────────────────────────────\n    output = {\n        \"n_instances\": len(shared_keys),\n        \"cls_metrics\": cls_metrics,\n        \"cwm_metrics\": cwm_metrics,\n        \"bootstrap\": bootstrap,\n        \"d008_decision\": decision,\n        \"d008_decision_msg\": decision_msg,\n        \"config\": {\n            \"n_bootstrap\": args.n_bootstrap,\n            \"seed\": args.seed,\n            \"max_seq_length\": args.max_seq_length,\n        },\n    }\n\n    with open(args.output, \"w\") as f:\n        json.dump(output, f, indent=2)\n    log.info(f\"Results saved to {args.output}\")\n\n    # ── Save predictions ─────────────────────────────────────────────────\n    if args.save_predictions and inference_mode:\n        stem = os.path.splitext(args.output)[0]\n        for name, preds in [(\"cls\", cls_results), (\"cwm\", cwm_results)]:\n            path = f\"{stem}_{name}_predictions.jsonl\"\n            with open(path, \"w\") as f:\n                for r in preds:\n                    f.write(json.dumps(r) + \"\\n\")\n            log.info(f\"{name.upper()} predictions saved to {path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nENDOFSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T22:25:55.773359+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T22:25:55.773513+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_repo_level.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_repo_level.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T22:25:55.773667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: eval_repo_level.py [-h] [--cls_checkpoint CLS_CHECKPOINT]\\n                          [--cwm_checkpoint CWM_CHECKPOINT]\\n                          [--model_name MODEL_NAME] [--cls_preds CLS_PREDS]\\n                          [--cwm_preds CWM_PREDS] [--data_dir DATA_DIR]\\n                          [--output OUTPUT] [--batch_size BATCH_SIZE]\\n                          [--max_seq_length MAX_SEQ_LENGTH] [--device DEVICE]\\n                          [--n_bootstrap N_BOOTSTRAP] [--seed SEED]\\n                          [--save_predictions] [--dry_run]\\n\\nUnified repo-level CLS vs CWM evaluation with paired bootstrap on F1\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --cls_checkpoint CLS_CHECKPOINT\\n                        CLS LoRA checkpoint dir (inference mode)\\n  --cwm_checkpoint CWM_CHECKPOINT\\n                        CWM LoRA checkpoint dir (inference mode)\\n  --model_name MODEL_NAME\\n                        Base model path\\n  --cls_preds CLS_PREDS\\n                        Existing CLS predictions JSONL (skip inference)\\n  --cwm_preds CWM_PREDS\\n                        Existing CWM predictions JSONL (skip inference)\\n  --data_dir DATA_DIR\\n  --output OUTPUT\\n  --batch_size BATCH_SIZE\\n  --max_seq_length MAX_SEQ_LENGTH\\n  --device DEVICE\\n  --n_bootstrap N_BOOTSTRAP\\n  --seed SEED\\n  --save_predictions    Save per-instance prediction JSONL files\\n  --dry_run             Only test data loading and arg parsing, no model\\n                        inference\\n\\nExamples:\\n  # Full inference + bootstrap:\\n  python eval_repo_level.py --cls_checkpoint /path/to/cls --cwm_checkpoint /path/to/cwm\\n\\n  # Bootstrap from existing predictions:\\n  python eval_repo_level.py --cls_preds cls_predictions.jsonl --cwm_preds cwm_predictions.jsonl\\n\\n  # Dry-run (test data loading only):\\n  python eval_repo_level.py --dry_run\\n\", \"stderr\": \"\", \"return_code\": 0
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-12T22:25:55.773854+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_repo_level.py --dry_run",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_repo_level.py --dry_run",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T22:25:55.774028+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Dry run OK. Test set: 9784 examples. Labels: pass=7138 fail=2646\\nData fields: ['code', 'test', 'label', 'source', 'problem_id', 'mutation_type', 'error_message', 'execution_output', 'metadata']\\nArgs: {'cls_checkpoint': None, 'cwm_checkpoint': None, 'model_name': '/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B', 'cls_preds': None, 'cwm_preds': None, 'data_dir': '/home/sonny/exec-sim-repair-verifier/data/swebench_full', 'output': 'eval_repo_level_results.json', 'batch_size': 16, 'max_seq_length': 2048, 'device': 'cuda:0', 'n_bootstrap': 10000, 'seed': 42, 'save_predictions': False, 'dry_run': True}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T22:25:55.774178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T22:25:55.774305+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B/config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-12T22:25:55.774434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "ls /root/autodl-tmp/checkpoints_repo_cwm_v9/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "ls /root/autodl-tmp/checkpoints_repo_cwm_v9/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T22:25:55.774555+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoint-100\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-12T22:25:55.774704+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, tempfile, os\n\n# Create synthetic predictions: CLS slightly better than CWM\nn = 200\ncls_preds, cwm_preds = [], []\nfor i in range(n):\n    label = 0 if i < 80 else 1  # 80 fail, 120 pass\n    # CLS: 85% accuracy\n    cls_correct = (i % 20 != 0)\n    cls_pred = label if cls_correct else (1 - label)\n    # CWM: 78% accuracy\n    cwm_correct = (i % 9 != 0)\n    cwm_pred = label if cwm_correct else (1 - label)\n\n    cls_preds.append({'index': i, 'problem_id': f'p{i}', 'label': label, 'pred': cls_pred})\n    cwm_preds.append({'index': i, 'problem_id': f'p{i}', 'label': label, 'pred': cwm_pred})\n\n# Write temp files\nwith open('/tmp/test_cls.jsonl', 'w') as f:\n    for r in cls_preds:\n        f.write(json.dumps(r) + '\\n')\nwith open('/tmp/test_cwm.jsonl', 'w') as f:\n    for r in cwm_preds:\n        f.write(json.dumps(r) + '\\n')\nprint('Synthetic data written')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, tempfile, os\n\n# Create synthetic predictions: CLS slightly better than CWM\nn = 200\ncls_preds, cwm_preds = [], []\nfor i in range(n):\n    label = 0 if i < 80 else 1  # 80 fail, 120 pass\n    # CLS: 85% accuracy\n    cls_correct = (i % 20 != 0)\n    cls_pred = label if cls_correct else (1 - label)\n    # CWM: 78% accuracy\n    cwm_correct = (i % 9 != 0)\n    cwm_pred = label if cwm_correct else (1 - label)\n\n    cls_preds.append({'index': i, 'problem_id': f'p{i}', 'label': label, 'pred': cls_pred})\n    cwm_preds.append({'index': i, 'problem_id': f'p{i}', 'label': label, 'pred': cwm_pred})\n\n# Write temp files\nwith open('/tmp/test_cls.jsonl', 'w') as f:\n    for r in cls_preds:\n        f.write(json.dumps(r) + '\\n')\nwith open('/tmp/test_cwm.jsonl', 'w') as f:\n    for r in cwm_preds:\n        f.write(json.dumps(r) + '\\n')\nprint('Synthetic data written')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T22:25:55.774863+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Synthetic data written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-12T22:25:55.774988+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_repo_level.py --cls_preds /tmp/test_cls.jsonl --cwm_preds /tmp/test_cwm.jsonl --output /tmp/test_bootstrap.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_repo_level.py --cls_preds /tmp/test_cls.jsonl --cwm_preds /tmp/test_cwm.jsonl --output /tmp/test_bootstrap.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T22:25:55.775137+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n======================================================================\\nREPO-LEVEL EVALUATION: CLS vs CWM (Paired Bootstrap on F1)\\n======================================================================\\n\\nInstances: 200\\n\\n--- CLS (verifier) ---\\n  Accuracy: 95.00%\\n  F1 macro: 94.81%\\n  F1  fail=93.83%  pass=95.80%\\n  Prec fail=92.68%  pass=96.61%\\n  Rec  fail=95.00%  pass=95.00%\\n\\n--- CWM (generation) ---\\n  Accuracy: 88.50%\\n  F1 macro: 88.14%\\n  F1  fail=86.06%  pass=90.21%\\n  Prec fail=83.53%  pass=92.17%\\n  Rec  fail=88.75%  pass=88.33%\\n\\n──────────────────────────────────────────────────────────────────────\\nPAIRED BOOTSTRAP (10000 resamples)\\n──────────────────────────────────────────────────────────────────────\\n  f1_macro     gap=+6.68pp  CI95=[+1.48, +12.17]  p=0.0069 **\\n  f1_fail      gap=+7.77pp  CI95=[+1.59, +14.34]  p=0.0069 **\\n  f1_pass      gap=+5.59pp  CI95=[+1.16, +10.34]  p=0.0072 **\\n  accuracy     gap=+6.50pp  CI95=[+1.50, +12.00]  p=0.0088 **\\n\\n  Disagreement: both_ok=169  both_wrong=2  cls_only=21  cwm_only=8\\n\\n──────────────────────────────────────────────────────────────────────\\nD008 GO/NO-GO (based on F1 macro)\\n──────────────────────────────────────────────────────────────────────\\n  F1 macro gap: +6.68pp  p=0.0069\\n  Decision: GO_EMNLP_MAIN\\n  F1 gap >= 3pp + p<0.05 → full push EMNLP Main\\n======================================================================\\n\", \"stderr\": \"2026-05-13 06:25:33,402 INFO Loading CLS predictions: /tmp/test_cls.jsonl\\n2026-05-13 06:25:33,402 INFO Loading CWM predictions: /tmp/test_cwm.jsonl\\n2026-05-13 06:25:33,412 INFO Running paired bootstrap (10000 resamples) ...\\n2026-05-13 06:25:33,759 INFO Results saved to /tmp/test_bootstrap.json\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-12T22:25:55.775331+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "rm /tmp/test_cls.jsonl /tmp/test_cwm.jsonl /tmp/test_bootstrap.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "rm /tmp/test_cls.jsonl /tmp/test_cwm.jsonl /tmp/test_bootstrap.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T22:25:55.775461+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_eval-script-prep_20260512T222025",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-12T22:25:55.775622+00:00_

---

**`eval_repo_level.py`** 已部署到 `/home/sonny/exec-sim-repair-verifier/`，dry-run 和 bootstrap 逻辑验证通过。

### 用法

**训练完成后，全量推理 + bootstrap：**
```bash
python eval_repo_level.py \
  --cls_checkpoint /path/to/cls_best_ckpt \
  --cwm_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v9/checkpoint-XXX \
  --device cuda:0 --save_predictions --output eval_repo_level_results.json
```

**如果已有预测文件（用现有 eval_repo_verifier.py / eval_repo_cwm.py 分别跑过）：**
```bash
python eval_repo_level.py \
  --cls_preds eval_repo_cls_results_predictions.jsonl \
  --cwm_preds eval_repo_cwm_results_predictions.jsonl
```

### 与现有脚本的关系
- `eval_repo_verifier.py` / `eval_repo_cwm.py`：单模型 eval，保持不变
- `paired_bootstrap_repo.py`：旧版 bootstrap（用 accuracy），现在 `eval_repo_level.py` 用 **F1 macro** 做 bootstrap，符合 D008 标准
- 两种模式互补：可以用新脚本一站式跑，也可以先分别跑单模型 eval 再喂预测文件给新脚本

### 注意事项
- CLS v4 checkpoint 在 home-1x5090 上，eval 前需要 scp 到 seetacloud，或在 home 上运行单模型 eval 导出预测文件再传过来用 predictions 模式
- base model 路径默认 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`（已验证存在）
- 推理时两个模型顺序加载、释放 GPU 显存，单卡即可

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_eval-script-prep_20260512T222025"
}
```

</details>

---
