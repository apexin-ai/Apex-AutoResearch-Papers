# analysis plan 005 stratified

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 39
- **Original source:** `logs/chats/worker_analysis_plan_005_stratified_20260514T201443.jsonl`
- **Structured JSON:** [`22d74a283293e41a2e97.json`](../../sessions/22/22d74a283293e41a2e97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-14T20:25:40.105271+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T20:25:40.105744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:25:40.105929+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:25:40.106069+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:25:40.106194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -name \"analyze_stratified*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse -name \"analyze_stratified*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T20:25:40.106320+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T20:25:40.106438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:25:40.106559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"random_s42\\nrandom_s43\\nrandom_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T20:25:40.106768+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -name \"analyze_stratified*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse -name \"analyze_stratified*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:25:40.106910+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T20:25:40.107027+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -name \"*stratif*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse -name \"*stratif*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T20:25:40.107142+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T20:25:40.107285+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/structfuse/scripts/"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T20:25:40.107419+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_bm25_overlap_stratified.py\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench_e2e.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nmigrate_m1_data.sh\\nmine_bm25_negatives.py\\nplot_neg_difficulty.py\\nprepare_m1_rerun.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_full_bm25_qwen.sh\\nrun_m2_full_bm25_starcoder.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T20:25:40.107538+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/evaluation/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/structfuse/evaluation/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:25:40.107682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_stratified.py\\neval_repobench.py\\neval_retrieval.py\\neval_swebench.py\\neval_swebench.py.bak\\nlinear_proxy.py\\nlinear_proxy_results.json\\nplot_neg_difficulty.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:25:40.107803+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/structfuse/"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T20:25:40.107930+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\nartifacts\\nauto_start_dataflow.sh\\nconfigs\\neval_checkpoint.py\\nevaluation\\nextraction\\nmvp_phase1.py\\nmvp_phase1.py.bak\\nrequirements.txt\\nresults\\nrun_m2_bm25_qwen_s42.sh\\nrun_m2_early_pilot.sh\\nrun_m2_embed_verify.sh\\nrun_m2_embed_verify_continuation.sh\\nrun_m2_full_qwen.sh\\nrun_m2_full_starcoder.sh\\nrun_m2_full_starcoder_resume.sh\\nrun_m2_full_starcoder_s43plus.sh\\nrun_m2_s42_supplement.sh\\nrun_plan013_dataflow_retry.sh\\nrun_plan013_starcoder.sh\\nrun_plan014_temp_ablation.sh\\nrun_plan014_temp_ablation.sh.bak\\nrun_plan014_temp_cuda0.sh\\nrun_plan014_temp_cuda1.sh\\nrun_starcoder_data_build.sh\\nscripts\\ntea_debug.log\\ntraining\\nwandb\\nwatch_and_chain_qwen_s42.sh\\nwatch_and_chain_starcoder_s42.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T20:25:40.108093+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T20:25:40.108359+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unkno
…[truncated 7282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T20:25:40.108519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/scripts/analyze_bm25_overlap_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "cat /root/structfuse/scripts/analyze_bm25_overlap_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T20:25:40.108737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Stratified BM25 overlap analysis: compares BM25 top-k negatives against\\n# other mining strategies (random, embedding_distance, dataflow_aware),\\n# stratified by repo size (unique file count).\\n#\\n# Input:  /root/autodl-tmp/structfuse/full_m2_training_data/train_{strategy}_s42.jsonl\\n# Output: /root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\n\\nimport json\\nimport os\\nfrom collections import defaultdict\\n\\nimport numpy as np\\n\\nDATA_DIR = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\nOUT_PATH = \\\"/root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\\"\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEED = 42\\nK = 7\\nTIERS = {\\n    \\\"small_lt50\\\": (0, 50),\\n    \\\"medium_50_200\\\": (50, 201),\\n    \\\"large_200plus\\\": (201, float(\\\"inf\\\")),\\n}\\n\\n\\ndef extract_repo(query_id: str) -> str:\\n    iid = query_id.split(\\\"::\\\")[0]\\n    return iid.split(\\\".\\\")[0]\\n\\n\\ndef extract_filepath(full_id: str) -> str:\\n    return full_id.split(\\\"::\\\", 1)[1]\\n\\n\\ndef jaccard(a: set, b: set) -> float:\\n    if not a and not b:\\n        return 1.0\\n    union = a | b\\n    if not union:\\n        return 0.0\\n    return len(a & b) / len(union)\\n\\n\\ndef load_strategy(name: str) -> dict:\\n    path = os.path.join(DATA_DIR, f\\\"train_{name}_s{SEED}.jsonl\\\")\\n    data = {}\\n    with open(path) as f:\\n        for line in f:\\n            d = json.loads(line)\\n            data[d[\\\"query_id\\\"]] = d[\\\"neg_candidates\\\"]\\n    return data\\n\\n\\ndef main():\\n    # 1. Load all strategies\\n    bm25_data = load_strategy(\\\"bm25\\\")\\n    other_data = {s: load_strategy(s) for s in STRATEGIES}\\n\\n    # 2. Build repo file count (union of all file paths across all strategies)\\n    repo_files = defaultdict(set)\\n    for qid, negs in bm25_data.items():\\n        repo = extract_rep
…[truncated 4192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T20:25:40.108933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "wc -l /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "wc -l /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T20:25:40.109061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -250 /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "head -250 /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T20:25:40.109183+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"781 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T20:25:40.109448+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unkno
…[truncated 7397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T20:25:40.109625+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "tail -n +250 /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "tail -n +250 /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T20:25:40.109884+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\ndef mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n
…[truncated 7081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T20:25:40.110075+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "sed -n '370,530p' /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "sed -n '370,530p' /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T20:25:40.110206+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T20:25:40.110326+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "sed -n '530,650p' /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "sed -n '530,650p' /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T20:25:40.110443+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T20:25:40.110559+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \\|argparse\\|add_argument\\|structural\\|dataflow\\|neg_difficulty\\|quartile\\|has_dataflow\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def \\|argparse\\|add_argument\\|structural\\|dataflow\\|neg_difficulty\\|quartile\\|has_dataflow\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T20:25:40.110698+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T20:25:40.110813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \\|add_argument\\|structural\\|dataflow\\|neg_difficulty\\|quartile\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def \\|add_argument\\|structural\\|dataflow\\|neg_difficulty\\|quartile\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T20:25:40.110929+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T20:25:40.111047+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"def \" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T20:25:40.111173+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"56:def _bin_value(value, bins):\\n65:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n85:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n126:def text_similarity(a: str, b: str) -> float:\\n137:def reeval_checkpoint(\\n176:            def _encode(text):\\n213:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n251:def mock_predictions(\\n283:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n296:def _metric_fn(results, metric_name):\\n301:def bootstrap_ci(\\n328:def assign_strata(\\n344:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n353:def run_stratified_analysis(\\n402:def make_plots(\\n560:def write_summary_csv(\\n617:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T20:25:40.111364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"add_argument\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"add_argument\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T20:25:40.111545+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"621:    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n623:    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n625:    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n627:    parser.add_argument(\\\"--m1-data\\\", required=True,\\n629:    parser.add_argument(\\\"--output-dir\\\", required=True)\\n630:    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n632:    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n634:    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n635:    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n636:    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n637:    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n639:    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n641:    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T20:25:40.111790+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"dataflow\\|structural\\|neg_difficulty\\|quartile\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"dataflow\\|structural\\|neg_difficulty\\|quartile\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T20:25:40.111934+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T20:25:40.112137+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"dataflow\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"dataflow\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T20:25:40.112308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"32:STRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\n33:STRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\n34:STRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n385:        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n531:                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n591:            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T20:25:40.112452+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"neg_difficulty\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"neg_difficulty\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T20:25:40.112648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"quartile\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"quartile\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T20:25:40.112812+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T20:25:40.112934+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T20:25:40.113049+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"structural\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "grep -n \"structural\" /root/structfuse/evaluation/analyze_stratified.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T20:25:40.113165+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T20:25:40.113323+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/structfuse/results/"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T20:25:40.113448+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"full_z_percent_stats.json\\npilot_results.json\\npilot_results_summary.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T20:25:40.113563+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse/results -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/structfuse/results -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T20:25:40.113761+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/results/pilot_results.json\\n/root/structfuse/results/full_z_percent_stats.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T20:25:40.113891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/full_m2_training_data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/autodl-tmp/structfuse/full_m2_training_data/"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T20:25:40.114020+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dataflow_graph.json\\ntrain_bm25_s42.jsonl\\ntrain_bm25_s43.jsonl\\ntrain_bm25_s44.jsonl\\ntrain_dataflow_aware_s42.jsonl\\ntrain_dataflow_aware_s43.jsonl\\ntrain_dataflow_aware_s44.jsonl\\ntrain_embedding_distance_s42.jsonl\\ntrain_embedding_distance_s43.jsonl\\ntrain_embedding_distance_s44.jsonl\\ntrain_random_s42.jsonl\\ntrain_random_s43.jsonl\\ntrain_random_s44.jsonl\\nval_bm25_s42.jsonl\\nval_bm25_s43.jsonl\\nval_bm25_s44.jsonl\\nval_dataflow_aware_s42.jsonl\\nval_dataflow_aware_s43.jsonl\\nval_dataflow_aware_s44.jsonl\\nval_embedding_distance_s42.jsonl\\nval_embedding_distance_s43.jsonl\\nval_embedding_distance_s44.jsonl\\nval_random_s42.jsonl\\nval_random_s43.jsonl\\nval_random_s44.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T20:25:40.114167+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse -name \"per_instance*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp/structfuse -name \"per_instance*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T20:25:40.114284+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse -name \"eval_results*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp/structfuse -name \"eval_results*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T20:25:40.114405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse/checkpoints -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp/structfuse/checkpoints -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T20:25:40.114521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/eval_results/dryrun_verify/per_instance_results.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T20:25:40.114653+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T20:25:40.114803+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer_confi
…[truncated 2949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T20:25:40.114950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T20:25:40.115066+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"m2_full_qwen\\nm2_full_starcoder\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T20:25:40.115183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse/checkpoints -maxdepth 3 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp/structfuse/checkpoints -maxdepth 3 -type d"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T20:25:40.115309+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T20:25:40.115426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T20:25:40.115719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"query_id\\\": \\\"pyparsing__pyparsing.533adf47.combine_file__b756s2rd::pyparsing/helpers.py\\\", \\\"query_tokens\\\": \\\"# helpers.py\\\\nimport html.entities\\\\nimport operator\\\\nimport re\\\\nimport sys\\\\nimport typing\\\\n\\\\nfrom . import __diag__\\\\nfrom .core import *\\\\nfrom .util import (\\\\n    _bslash,\\\\n    _flatten,\\\\n    _escape_regex_range_chars,\\\\n    make_compressed_re,\\\\n    replaced_by_pep8,\\\\n)\\\\n\\\\n\\\\n#\\\\n# global helpers\\\\n#\\\\ndef counted_array(\\\\n    expr: ParserElement,\\\\n    int_expr: typing.Optional[ParserElement] = None,\\\\n    *,\\\\n    intExpr: typing.Optional[ParserElement] = None,\\\\n) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define a counted list of expressions.\\\\n\\\\n    This helper defines a pattern of the form::\\\\n\\\\n        integer expr expr expr...\\\\n\\\\n    where the leading integer tells how many expr expressions follow.\\\\n    The matched tokens returns the array of expr tokens as a list - the\\\\n    leading count token is suppressed.\\\\n\\\\n    If ``int_expr`` is specified, it should be a pyparsing expression\\\\n    that produces an integer value.\\\\n\\\\n    Example::\\\\n\\\\n        counted_array(Word(alphas)).parse_string('2 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # in this parser, the leading integer value is given in binary,\\\\n        # '10' indicating that 2 values are in the array\\\\n        binary_constant = Word('01').set_parse_action(lambda t: int(t[0], 2))\\\\n        counted_array(Word(alphas), int_expr=binary_constant).parse_string('10 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # if other fields must be parsed after the count but before the\\\\n        # list items, give the fields results names and they will\\\\n        # be preserved in the returned ParseResults:\\\\n        count_with_metadata = integer + Word(alphas)(\\\\\\\"type\\\\\\\")\\\\n        typed_arra
…[truncated 7672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T20:25:40.115907+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl').readline()); print(list(d.keys()))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl').readline()); print(list(d.keys()))\""
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T20:25:40.116062+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T20:25:40.116198+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse -name \"all.jsonl\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "find /root/autodl-tmp/structfuse -name \"all.jsonl\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T20:25:40.116322+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T20:25:40.116438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T20:25:40.116556+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2980 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T20:25:40.116698+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.loads(open('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl').readline())\nprint('Keys:', list(d.keys()))\nprint('neg_candidates count:', len(d.get('neg_candidates', [])))\nprint('candidate_tokens count:', len(d.get('candidate_tokens', {})))\nprint('has_dataflow:', d.get('has_dataflow'))\nprint('neg_difficulty:', d.get('neg_difficulty'))\nprint('strategy:', d.get('strategy'))\nprint('margin:', d.get('margin'))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.loads(open('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl').readline())\nprint('Keys:', list(d.keys()))\nprint('neg_candidates count:', len(d.get('neg_candidates', [])))\nprint('candidate_tokens count:', len(d.get('candidate_tokens', {})))\nprint('has_dataflow:', d.get('has_dataflow'))\nprint('neg_difficulty:', d.get('neg_difficulty'))\nprint('strategy:', d.get('strategy'))\nprint('margin:', d.get('margin'))\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T20:25:40.116833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Keys: ['query_id', 'query_tokens', 'pos_id', 'pos_tokens', 'pos_dataflow_distance', 'neg_candidates', 'candidate_tokens']\\nneg_candidates count: 50\\ncandidate_tokens count: 50\\nhas_dataflow: None\\nneg_difficulty: None\\nstrategy: None\\nmargin: None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T20:25:40.116948+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_plan_005_stratified_20260514T201443",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "account": "root",
    "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json"
  }
}
```

</details>

---
