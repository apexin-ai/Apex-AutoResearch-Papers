# ops pool50 precheck

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_ops_pool50-precheck_20260515T235517.jsonl`
- **Structured JSON:** [`7558864a4310bb152d3f.json`](../../sessions/75/7558864a4310bb152d3f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-15T23:59:09.464284+00:00_

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
  "session": "worker_ops_pool50-precheck_20260515T235517",
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

_source line 2 · 2026-05-15T23:59:09.464812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:59:09.465100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/ -name \"*pool*50*\" -o -name \"*evaluate_pool*\" -o -name \"*stratified*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/ -name \"*pool*50*\" -o -name \"*evaluate_pool*\" -o -name \"*stratified*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T23:59:09.465307+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:59:09.465484+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/ -name \"*.py\" -path \"*/eval*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/ -name \"*.py\" -path \"*/eval*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:59:09.465692+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:59:09.465865+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"best_by_recall_at_1\" -type d 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"best_by_recall_at_1\" -type d 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:59:09.466036+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:59:09.466208+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -name \"*val*\" -name \"*.jsonl\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -name \"*val*\" -name \"*.jsonl\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:59:09.466378+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:59:09.466539+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/scripts/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/scripts/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:59:09.466758+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T23:59:09.466966+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/ -name \"*pool*50*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/ -name \"*pool*50*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T23:59:09.467139+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/ -name \"*evaluate_pool*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/ -name \"*evaluate_pool*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T23:59:09.467307+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/__pycache__/evaluate_pool50.cpython-312.pyc\\n/root/structfuse/evaluation/evaluate_pool50.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T23:59:09.467472+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/ -name \"*stratified*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/ -name \"*stratified*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T23:59:09.467666+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/__pycache__/evaluate_pool50.cpython-312.pyc\\n/root/structfuse/evaluation/evaluate_pool50.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T23:59:09.467857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/__pycache__/analyze_stratified.cpython-312.pyc\\n/root/structfuse/evaluation/analyze_stratified.py\\n/root/structfuse/evaluation/analyze_stratified.py.bak_v2\\n/root/structfuse/evaluation/analyze_stratified.py.bak\\n/root/structfuse/scripts/analyze_bm25_overlap_stratified.py\\n/root/structfuse/scripts/evaluate_stratified.py\\n/root/structfuse/scripts/analyze_stratified.py\\n/root/structfuse/results/stratified\\n/root/structfuse/results/stratified/stratified_results_dryrun.json\\n/root/structfuse/results/stratified/stratified_results_dryrun.csv\\n/root/structfuse/results/stratified/stratified_repo_size.pdf\\n/root/structfuse/results/stratified/stratified_pool_size.pdf\\n/root/structfuse/results/stratified/stratified_query_pos_similarity.pdf\\n/root/structfuse/results/stratified/stratified_structural_availability.pdf\\n/root/structfuse/results/stratified/stratified_neg_difficulty.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T23:59:09.468043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/ -name \"*.py\" -path \"*eval*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/ -name \"*.py\" -path \"*eval*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T23:59:09.468232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T23:59:09.468422+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/evaluation/linear_proxy.py\\n/root/structfuse/evaluation/eval_swebench.py\\n/root/structfuse/evaluation/eval_retrieval.py\\n/root/structfuse/evaluation/eval_repobench.py\\n/root/structfuse/evaluation/analyze_stratified.py\\n/root/structfuse/evaluation/plot_neg_difficulty.py\\n/root/structfuse/evaluation/evaluate_pool50.py\\n/root/structfuse/scripts/eval_p2b.py\\n/root/structfuse/scripts/eval_p2b_pooled.py\\n/root/structfuse/scripts/eval_swebench_e2e.py\\n/root/structfuse/scripts/evaluate_stratified.py\\n/root/structfuse/scripts/extract_eval_trajectories.py\\n/root/structfuse/eval_checkpoint.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T23:59:09.468657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_bm25_overlap_stratified.py\\nanalyze_confound.py\\nanalyze_m2_stats.py\\nanalyze_stratified.py\\nbootstrap_paired_test.py\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncombine_m1_reextract.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench_e2e.py\\neval_swebench_e2e.py.bak.20260516032207\\nevaluate_stratified.py\\nextract_eval_trajectories.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nm2_statistical_analysis.py\\nmigrate_m1_data.sh\\nmine_bm25_negatives.py\\nplot_neg_difficulty.py\\nplot_overfitting_mechanism.py\\nplot_per_seed_delta.py\\nprepare_m1_rerun.py\\nprepare_stratification_index.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_full_bm25_qwen.sh\\nrun_m2_full_bm25_starcoder.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nrun_plan005_s43.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T23:59:09.468898+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T23:59:09.469232+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n# evaluate_pool50.py — 独立评估脚本，用 pool=50 重新评估 contrastive retrieval checkpoints\\n# \\n# 输入：best checkpoint 目录 + 验证数据 JSONL\\n# 输出：R@1, R@5 (mean ± std over multiple random samplings)\\n# \\n# 用法：\\n#   python evaluate_pool50.py --checkpoint-dir /path/to/best --data-path val.jsonl --base-model Qwen/Qwen2.5-Coder-3B\\n#   python evaluate_pool50.py --checkpoint-dir /path/to/all_checkpoints/ --data-path val.jsonl --base-model Qwen/Qwen2.5-Coder-3B --batch-mode\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nfrom tqdm import tqdm\\nfrom transformers import AutoTokenizer\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\ndef load_val_data(data_path: str):\\n    samples = []\\n    with open(data_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            item = json.loads(line)\\n            samples.append({\\n                \\\"query_id\\\": item[\\\"query_id\\\"],\\n                \\\"query_tokens\\\": item[\\\"query_tokens\\\"],\\n                \\\"pos_tokens\\\": item[\\\"pos_tokens\\\"],\\n            })\\n    return samples\\n\\n\\ndef encode_texts(model, tokenizer, texts, batch_size, max_seq_length, device):\\n    all_embs = []\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\"Encoding\\\", leave=False):\\n        batch_texts = texts[i:i + batch_size]\\n        encoded = tokenizer(\\n            batch_texts, truncation=True, max_length=max_seq_length,\\n            padding=True, return_tensors=\\\"pt\\\",\\n        )\\n        input_ids = encoded[\\\"input_ids\\\"].to(device)\\n        attention_mask = encoded[\\\"attention_mask\\\"].to(device)\\n        with torch.no_grad():\\n            if device.type ==
…[truncated 7161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T23:59:09.469502+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/run_eval_p50.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/scripts/run_eval_p50.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T23:59:09.469799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport CUDA_VISIBLE_DEVICES=4\\n\\ncd /root/structfuse\\n\\nCKPT_BASE=\\\"/root/autodl-tmp/structfuse/checkpoints\\\"\\nRESULTS_DIR=\\\"/root/autodl-tmp/structfuse/eval_results_p50\\\"\\nMODEL=\\\"/root/structfuse-context/models/Qwen/Qwen2.5-Coder-3B\\\"\\nPOOL_SIZE=50\\nmkdir -p $RESULTS_DIR\\n\\neval_checkpoint() {\\n  local ckpt_dir=\\\"$1\\\"\\n  local out_name=\\\"$2\\\"\\n  local LOG=\\\"${RESULTS_DIR}/${out_name}.log\\\"\\n\\n  if [ -f \\\"${RESULTS_DIR}/${out_name}.json\\\" ] && grep -q \\\"recall@1\\\" \\\"${RESULTS_DIR}/${out_name}.json\\\"; then\\n    echo \\\"SKIP $out_name: already evaluated\\\"\\n    return\\n  fi\\n\\n  echo \\\"=== Evaluating $out_name (ckpt: $ckpt_dir, pool_size=$POOL_SIZE) ===\\\"\\n  python scripts/eval_p2b_pooled.py \\\\\\n    --ckpt-dir \\\"$ckpt_dir\\\" \\\\\\n    --model-name \\\"$MODEL\\\" \\\\\\n    --pool-size $POOL_SIZE \\\\\\n    --device cuda:0 \\\\\\n    2>&1 | tee \\\"$LOG\\\"\\n\\n  python3 -c \\\"\\nimport re, json\\nwith open('$LOG') as f:\\n    text = f.read()\\nm = re.search(r'Results:\\\\s*(\\\\{.*\\\\})', text, re.DOTALL)\\nif m:\\n    metrics = json.loads(m.group(1))\\n    metrics['run'] = '$out_name'\\n    metrics['ckpt_dir'] = '$ckpt_dir'\\n    with open('${RESULTS_DIR}/${out_name}.json', 'w') as out:\\n        json.dump(metrics, out, indent=2)\\n    print(f'Saved: ${RESULTS_DIR}/${out_name}.json')\\nelse:\\n    print('WARNING: could not parse metrics from log')\\n\\\"\\n}\\n\\nfor SEED in 42 123 456; do\\n  for STRATEGY in random embedding_distance dataflow_aware; do\\n    RUN_NAME=\\\"p2b_${STRATEGY}_s${SEED}\\\"\\n    RUN_DIR=\\\"${CKPT_BASE}/${RUN_NAME}\\\"\\n\\n    if [ ! -d \\\"$RUN_DIR\\\" ]; then\\n      echo \\\"SKIP $RUN_NAME: directory not found\\\"\\n      continue\\n    fi\\n\\n    # --- Final checkpoint ---\\n    FINAL_CKPT=\\\"${RUN_DIR}/final\\\
…[truncated 2476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T23:59:09.470033+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"best_by_recall_at_1\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/ -name \"best_by_recall_at_1\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T23:59:09.470232+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s42/best_by_recall_at_1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T23:59:09.470418+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -name \"*val*\" -name \"*.jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -name \"*val*\" -name \"*.jsonl\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T23:59:09.470593+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -80 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -80 /root/structfuse/evaluation/analyze_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T23:59:09.470815+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m2_training_data/val_embedding_distance_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_dataflow_aware_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_embedding_distance_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_dataflow_aware_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_embedding_distance_s44.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s44.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_dataflow_aware_s44.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_bm25_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_bm25_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_training_data/val_bm25_s44.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_random_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_dataflow_aware_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_embedding_distance_s42.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_random_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_dataflow_aware_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_embedding_distance_s43.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_random_s44.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_dataflow_aware_s44.jsonl\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/val_embedding_distance_s44.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T23:59:09.471098+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of M2 negative-sampling strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across 5+2 dimensions:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n  - Dataflow availability (edge count from dataflow_graph.json)\\n  - Negative difficulty (pos-neg margin quartiles)\\n  - [NEW] Pool-size controlled comparison: within-bin delta to disentangle\\n    the confound that rich-dataflow instances have larger candidate pools\\n  - [NEW] Dataflow x pool_size cross-tabulation with underpowered flagging\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n  - dataflow_graph.json (optional, for dataflow dimension and cross-analysis)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table (incl. pool_size_controlled and cross sections)\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends,\\n    pool-controlled comparison, dataflow x pool_size heatmaps\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    
…[truncated 1055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T23:59:09.471370+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "wc -l /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "wc -l /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T23:59:09.471558+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"260 /root/structfuse/evaluation/evaluate_pool50.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T23:59:09.471756+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -30 /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -30 /root/structfuse/evaluation/analyze_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T23:59:09.471947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of M2 negative-sampling strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across 5+2 dimensions:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n  - Dataflow availability (edge count from dataflow_graph.json)\\n  - Negative difficulty (pos-neg margin quartiles)\\n  - [NEW] Pool-size controlled comparison: within-bin delta to disentangle\\n    the confound that rich-dataflow instances have larger candidate pools\\n  - [NEW] Dataflow x pool_size cross-tabulation with underpowered flagging\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n  - dataflow_graph.json (optional, for dataflow dimension and cross-analysis)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table (incl. pool_size_controlled and cross sections)\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends,\\n    pool-controlled comparison, dataflow x pool_size heatmaps\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T23:59:09.472130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"argparse\\|add_argument\\|predictions\\|--pred\\|--checkpoint\\|--input\\|--data\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -n \"argparse\\|add_argument\\|predictions\\|--pred\\|--checkpoint\\|--input\\|--data\" /root/structfuse/evaluation/analyze_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T23:59:09.472301+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T23:59:09.472467+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T23:59:09.472728+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"added_tokens.json\\nchat_template.jinja\\nmerges.txt\\nmodel.pt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_config.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T23:59:09.472917+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"def main\\|max.queries\\|max_queries\\|limit\\|num_eval\" /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -n \"def main\\|max.queries\\|max_queries\\|limit\\|num_eval\" /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T23:59:09.473100+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T23:59:09.473288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"add_argument\\|predictions\\|--pred\\|--checkpoint\\|--input\\|--data\\|--m1\\|--val\\|--output\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -n \"add_argument\\|predictions\\|--pred\\|--checkpoint\\|--input\\|--data\\|--m1\\|--val\\|--output\" /root/structfuse/evaluation/analyze_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T23:59:09.473457+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T23:59:09.473639+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"max.queries\\|max_queries\\|limit\\|num_eval\\|def main\" /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -n \"max.queries\\|max_queries\\|limit\\|num_eval\\|def main\" /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T23:59:09.473817+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T23:59:09.473981+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -80 /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "tail -80 /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T23:59:09.474214+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        checkpoints = [args.checkpoint_dir]\\n\\n    print(f\\\"\\\\nLoading data from {args.data_path}...\\\")\\n    samples = load_val_data(args.data_path)\\n    print(f\\\"  {len(samples)} queries\\\")\\n\\n    if args.pool_size > len(samples):\\n        print(f\\\"  pool_size capped: {args.pool_size} -> {len(samples)}\\\")\\n        args.pool_size = len(samples)\\n\\n    query_texts = [s[\\\"query_tokens\\\"] for s in samples]\\n    cand_texts = [s[\\\"pos_tokens\\\"] for s in samples]\\n\\n    all_results = {}\\n\\n    for ckpt_path in checkpoints:\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"Checkpoint: {ckpt_path}\\\")\\n        print(f\\\"{'='*60}\\\")\\n\\n        model, tokenizer, cfg = load_model(ckpt_path, args.base_model, device)\\n\\n        print(\\\"Encoding queries...\\\")\\n        query_embs = encode_texts(model, tokenizer, query_texts,\\n                                  args.batch_size, args.max_seq_length, device)\\n        print(\\\"Encoding candidates...\\\")\\n        cand_embs = encode_texts(model, tokenizer, cand_texts,\\n                                 args.batch_size, args.max_seq_length, device)\\n\\n        print(f\\\"Evaluating pool_size={args.pool_size}, trials={args.num_samples}...\\\")\\n        metrics = evaluate_with_pool(\\n            query_embs, cand_embs, args.pool_size, args.num_samples, args.seed,\\n        )\\n\\n        print(f\\\"  R@1: {metrics['recall@1_mean']:.4f} +/- {metrics['recall@1_std']:.4f}\\\")\\n        print(f\\\"  R@5: {metrics['recall@5_mean']:.4f} +/- {metrics['recall@5_std']:.4f}\\\")\\n\\n        all_results[ckpt_path] = {\\n            \\\"config_model_name\\\": cfg[\\\"model_name\\\"],\\n            \\\"pool_size\\\": args.pool_size,\\n            \\\"num_samples\\\": args.num_samples,\\n            \\\"num_queries\\\": len(samples),\\n            \\\"metrics\\\": {\\n                \\\"recall@1_mean\\\": metrics[\\\"recall@1_me
…[truncated 1592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T23:59:09.474428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T23:59:09.474654+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\",\\n  \\\"train_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/train_random_s42.jsonl\\\",\\n  \\\"val_file\\\": \\\"/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\\",\\n  \\\"output_dir\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\\",\\n  \\\"batch_size\\\": 8,\\n  \\\"learning_rate\\\": 2e-05,\\n  \\\"num_epochs\\\": 3,\\n  \\\"warmup_ratio\\\": 0.1,\\n  \\\"num_negatives\\\": 7,\\n  \\\"hard_negative_strategy\\\": \\\"random\\\",\\n  \\\"hard_negative_ratio\\\": 0.5,\\n  \\\"temperature\\\": 0.07,\\n  \\\"pos_weight_alpha\\\": 1.0,\\n  \\\"use_fusion_head\\\": false,\\n  \\\"use_lora\\\": true,\\n  \\\"lora_r\\\": 16,\\n  \\\"proj_dim\\\": 256,\\n  \\\"gradient_checkpointing\\\": true,\\n  \\\"eval_steps\\\": 500,\\n  \\\"save_steps\\\": 1000,\\n  \\\"max_seq_length\\\": 2048,\\n  \\\"seed\\\": 42,\\n  \\\"wandb_project\\\": \\\"structfuse\\\",\\n  \\\"wandb_run_name\\\": \\\"m2_full_random_s42\\\",\\n  \\\"dataflow_graph_file\\\": null,\\n  \\\"embeddings_file\\\": null,\\n  \\\"dynamic_mining\\\": false,\\n  \\\"candidate_pool_file\\\": null,\\n  \\\"early_stopping_patience\\\": 0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T23:59:09.474861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T23:59:09.475036+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2980 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T23:59:09.475240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "sed -n '95,145p' /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "sed -n '95,145p' /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T23:59:09.475415+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T23:59:09.475579+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"add_argument\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -n \"add_argument\" /root/structfuse/evaluation/analyze_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T23:59:09.475792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1070:    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n1072:    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n1074:    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n1076:    parser.add_argument(\\\"--m1-data\\\", required=True,\\n1078:    parser.add_argument(\\\"--output-dir\\\", required=True)\\n1079:    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n1081:    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n1083:    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n1084:    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n1085:    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n1086:    parser.add_argument(\\\"--batch-size\\\", type=int, default=64,\\n1088:    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n1090:    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n1092:    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n1094:    parser.add_argument(\\\"--dataflow-graph\\\", default=None,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T23:59:09.475969+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T23:59:09.476142+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dataflow_aware_s43\\nembedding_distance_s43\\nembedding_distance_s44\\nrandom_s42\\nrandom_s43\\nrandom_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T23:59:09.476307+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T23:59:09.476473+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"embedding_distance_s42\\nrandom_s42\\nrandom_s43\\nrandom_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T23:59:09.476727+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -170 /root/structfuse/evaluation/evaluate_pool50.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -170 /root/structfuse/evaluation/evaluate_pool50.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T23:59:09.477031+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n# evaluate_pool50.py — 独立评估脚本，用 pool=50 重新评估 contrastive retrieval checkpoints\\n# \\n# 输入：best checkpoint 目录 + 验证数据 JSONL\\n# 输出：R@1, R@5 (mean ± std over multiple random samplings)\\n# \\n# 用法：\\n#   python evaluate_pool50.py --checkpoint-dir /path/to/best --data-path val.jsonl --base-model Qwen/Qwen2.5-Coder-3B\\n#   python evaluate_pool50.py --checkpoint-dir /path/to/all_checkpoints/ --data-path val.jsonl --base-model Qwen/Qwen2.5-Coder-3B --batch-mode\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nfrom tqdm import tqdm\\nfrom transformers import AutoTokenizer\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\ndef load_val_data(data_path: str):\\n    samples = []\\n    with open(data_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            item = json.loads(line)\\n            samples.append({\\n                \\\"query_id\\\": item[\\\"query_id\\\"],\\n                \\\"query_tokens\\\": item[\\\"query_tokens\\\"],\\n                \\\"pos_tokens\\\": item[\\\"pos_tokens\\\"],\\n            })\\n    return samples\\n\\n\\ndef encode_texts(model, tokenizer, texts, batch_size, max_seq_length, device):\\n    all_embs = []\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\"Encoding\\\", leave=False):\\n        batch_texts = texts[i:i + batch_size]\\n        encoded = tokenizer(\\n            batch_texts, truncation=True, max_length=max_seq_length,\\n            padding=True, return_tensors=\\\"pt\\\",\\n        )\\n        input_ids = encoded[\\\"input_ids\\\"].to(device)\\n        attention_mask = encoded[\\\"attention_mask\\\"].to(device)\\n        with torch.no_grad():\\n            if device.type ==
…[truncated 5043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T23:59:09.477260+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -n \"predictions-dir\\|checkpoints-dir\\|--predictions\\|load.*prediction\\|load.*pred\\|re.eval\\|re_eval\" /root/structfuse/evaluation/analyze_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -n \"predictions-dir\\|checkpoints-dir\\|--predictions\\|load.*prediction\\|load.*pred\\|re.eval\\|re_eval\" /root/structfuse/evaluation/analyze_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T23:59:09.477439+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T23:59:09.477623+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/ -name \"best_by_recall_at_1\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/ -name \"best_by_recall_at_1\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T23:59:09.477809+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/embedding_distance_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T23:59:09.477976+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/ -name \"best_by_recall_at_1\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/ -name \"best_by_recall_at_1\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T23:59:09.478152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s42/best_by_recall_at_1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T23:59:09.478367+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T23:59:09.478547+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T23:59:09.478741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 62620 MiB, 97887 MiB, 100 %\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 54787 MiB, 97887 MiB, 100 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T23:59:09.479119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"query_id\\\": \\\"pyparsing__pyparsing.533adf47.combine_file__b756s2rd::pyparsing/helpers.py\\\", \\\"query_tokens\\\": \\\"# helpers.py\\\\nimport html.entities\\\\nimport operator\\\\nimport re\\\\nimport sys\\\\nimport typing\\\\n\\\\nfrom . import __diag__\\\\nfrom .core import *\\\\nfrom .util import (\\\\n    _bslash,\\\\n    _flatten,\\\\n    _escape_regex_range_chars,\\\\n    make_compressed_re,\\\\n    replaced_by_pep8,\\\\n)\\\\n\\\\n\\\\n#\\\\n# global helpers\\\\n#\\\\ndef counted_array(\\\\n    expr: ParserElement,\\\\n    int_expr: typing.Optional[ParserElement] = None,\\\\n    *,\\\\n    intExpr: typing.Optional[ParserElement] = None,\\\\n) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define a counted list of expressions.\\\\n\\\\n    This helper defines a pattern of the form::\\\\n\\\\n        integer expr expr expr...\\\\n\\\\n    where the leading integer tells how many expr expressions follow.\\\\n    The matched tokens returns the array of expr tokens as a list - the\\\\n    leading count token is suppressed.\\\\n\\\\n    If ``int_expr`` is specified, it should be a pyparsing expression\\\\n    that produces an integer value.\\\\n\\\\n    Example::\\\\n\\\\n        counted_array(Word(alphas)).parse_string('2 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # in this parser, the leading integer value is given in binary,\\\\n        # '10' indicating that 2 values are in the array\\\\n        binary_constant = Word('01').set_parse_action(lambda t: int(t[0], 2))\\\\n        counted_array(Word(alphas), int_expr=binary_constant).parse_string('10 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # if other fields must be parsed after the count but before the\\\\n        # list items, give the fields results names and they will\\\\n        # be preserved in the returned ParseResults:\\\\n        count_with_metadata = integer + Word(alphas)(\\\\\\\"type\\\\\\\")\\\\n        typed_arra
…[truncated 7672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T23:59:09.479385+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python -c \"\nfrom evaluation.evaluate_pool50 import load_val_data, load_model, encode_texts, evaluate_with_pool\nprint('All imports OK')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python -c \"\nfrom evaluation.evaluate_pool50 import load_val_data, load_model, encode_texts, evaluate_with_pool\nprint('All imports OK')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-15T23:59:09.479567+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python evaluation/evaluate_pool50.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python evaluation/evaluate_pool50.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T23:59:09.479770+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python evaluation/analyze_stratified.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python evaluation/analyze_stratified.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T23:59:09.479947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"All imports OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-15T23:59:09.480138+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: evaluate_pool50.py [-h] --checkpoint-dir CHECKPOINT_DIR --data-path\\n                          DATA_PATH [--base-model BASE_MODEL]\\n                          [--pool-size POOL_SIZE] [--num-samples NUM_SAMPLES]\\n                          [--seed SEED] [--batch-size BATCH_SIZE]\\n                          [--max-seq-length MAX_SEQ_LENGTH] [--output OUTPUT]\\n                          [--gpu GPU] [--batch-mode]\\n\\nEvaluate contrastive retrieval checkpoints with larger candidate pools\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --checkpoint-dir CHECKPOINT_DIR\\n                        Checkpoint dir (single) or parent dir (--batch-mode)\\n  --data-path DATA_PATH\\n                        Validation JSONL path\\n  --base-model BASE_MODEL\\n                        Override base model path (default: from\\n                        training_config.json)\\n  --pool-size POOL_SIZE\\n  --num-samples NUM_SAMPLES\\n                        Random sampling trials for mean±std\\n  --seed SEED\\n  --batch-size BATCH_SIZE\\n  --max-seq-length MAX_SEQ_LENGTH\\n  --output OUTPUT       Output JSON path\\n  --gpu GPU             GPU index (-1 for CPU)\\n  --batch-mode          Auto-discover best_by_* checkpoints under\\n                        --checkpoint-dir\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T23:59:09.480351+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: analyze_stratified.py [-h] [--predictions-dir PREDICTIONS_DIR]\\n                             [--checkpoints-dir CHECKPOINTS_DIR]\\n                             [--val-data-dir VAL_DATA_DIR] --m1-data M1_DATA\\n                             --output-dir OUTPUT_DIR [--dry-run]\\n                             [--seeds SEEDS] [--device DEVICE]\\n                             [--max-seq-length MAX_SEQ_LENGTH]\\n                             [--n-bootstrap N_BOOTSTRAP]\\n                             [--batch-size BATCH_SIZE]\\n                             [--repo-size-bins REPO_SIZE_BINS]\\n                             [--pool-size-bins POOL_SIZE_BINS]\\n                             [--sim-bins SIM_BINS]\\n                             [--dataflow-graph DATAFLOW_GRAPH]\\n\\nStratified analysis of M2 strategies by data strata\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --predictions-dir PREDICTIONS_DIR\\n                        Dir with per-strategy prediction JSONs (from\\n                        eval_retrieval.py)\\n  --checkpoints-dir CHECKPOINTS_DIR\\n                        Dir containing strategy/seed checkpoint subdirs\\n  --val-data-dir VAL_DATA_DIR\\n                        Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\n  --m1-data M1_DATA     Path to M1 all.jsonl\\n  --output-dir OUTPUT_DIR\\n  --dry-run             Use mock predictions to validate pipeline\\n  --seeds SEEDS         Comma-separated seed list\\n  --device DEVICE\\n  --max-seq-length MAX_SEQ_LENGTH\\n  --n-bootstrap N_BOOTSTRAP\\n  --batch-size BATCH_SIZE\\n                        Batch size for encoding during checkpoint re-\\n                        evaluation\\n  --repo-size-bins REPO_SIZE_BINS\\n                        JSON dict: {\\\"small\\\": [0,50], \\\"medium\\\": [50,200], ...}\\n  --pool-size-bins POOL_SIZE_BINS\\n                        JSON dict for pool size bins\\n  --sim-bins SIM_BINS   JSON di
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T23:59:09.480642+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/results/stratified/stratified_results_dryrun.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/results/stratified/stratified_results_dryrun.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T23:59:09.481097+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"repo_size\\\": {\\n    \\\"bins\\\": {\\n      \\\"small (<50)\\\": \\\"(0, 50)\\\",\\n      \\\"medium (50-200)\\\": \\\"(50, 201)\\\",\\n      \\\"large (200+)\\\": \\\"(201, inf)\\\"\\n    },\\n    \\\"strata\\\": {\\n      \\\"large (200+)\\\": {\\n        \\\"random\\\": {\\n          \\\"mean\\\": 0.382637,\\n          \\\"ci_lower\\\": 0.33119,\\n          \\\"ci_upper\\\": 0.437299,\\n          \\\"n\\\": 311\\n        },\\n        \\\"embedding_distance\\\": {\\n          \\\"mean\\\": 0.446254,\\n          \\\"ci_lower\\\": 0.390879,\\n          \\\"ci_upper\\\": 0.501629,\\n          \\\"n\\\": 307\\n        },\\n        \\\"dataflow_aware\\\": {\\n          \\\"mean\\\": 0.555556,\\n          \\\"ci_lower\\\": 0.499913,\\n          \\\"ci_upper\\\": 0.611111,\\n          \\\"n\\\": 288\\n        },\\n        \\\"delta_embedding_distance_vs_random\\\": 0.063617,\\n        \\\"delta_dataflow_aware_vs_random\\\": 0.172919,\\n        \\\"count\\\": 906\\n      },\\n      \\\"medium (50-200)\\\": {\\n        \\\"random\\\": {\\n          \\\"mean\\\": 0.384106,\\n          \\\"ci_lower\\\": 0.311258,\\n          \\\"ci_upper\\\": 0.463576,\\n          \\\"n\\\": 151\\n        },\\n        \\\"embedding_distance\\\": {\\n          \\\"mean\\\": 0.430556,\\n          \\\"ci_lower\\\": 0.347222,\\n          \\\"ci_upper\\\": 0.513889,\\n          \\\"n\\\": 144\\n        },\\n        \\\"dataflow_aware\\\": {\\n          \\\"mean\\\": 0.514451,\\n          \\\"ci_lower\\\": 0.439306,\\n          \\\"ci_upper\\\": 0.589595,\\n          \\\"n\\\": 173\\n        },\\n        \\\"delta_embedding_distance_vs_random\\\": 0.04645,\\n        \\\"delta_dataflow_aware_vs_random\\\": 0.130345,\\n        \\\"count\\\": 468\\n      },\\n      \\\"small (<50)\\\": {\\n        \\\"random\\\": {\\n          \\\"mean\\\": 0.449904,\\n          \\\"ci_lower\\\": 0.420039,\\n          \\\"ci_upper\\\": 0.480732,\\n 
…[truncated 8289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T23:59:09.481330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -name \"all.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -name \"all.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T23:59:09.481509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T23:59:09.481698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/ -name \"dataflow_graph.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/ -name \"dataflow_graph.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T23:59:09.481870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json\\n/root/autodl-tmp/structfuse/full_m2_starcoder_data/dataflow_graph.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T23:59:09.482038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T23:59:09.482216+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"added_tokens.json\\nchat_template.jinja\\nmerges.txt\\nmodel.pt\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_config.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T23:59:09.482432+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python -c \"\nimport json, torch, sys\nsys.path.insert(0, 'training')\nfrom evaluation.evaluate_pool50 import load_val_data, load_model\n\n# 1. Load val data\nsamples = load_val_data('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl')\nprint(f'Val data: {len(samples)} samples')\nprint(f'Sample keys: {list(samples[0].keys())}')\nprint(f'query_tokens length: {len(samples[0][\\\"query_tokens\\\"])} chars')\n\n# 2. Load model on CPU\nckpt = '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1'\nmodel, tokenizer, cfg = load_model(ckpt, None, torch.device('cpu'))\nprint(f'Model loaded OK: {type(model).__name__}')\nprint(f'Config model_name: {cfg[\\\"model_name\\\"]}')\n\n# 3. Single-sample encode\ntext = samples[0]['query_tokens'][:200]  # truncate for speed\nencoded = tokenizer([text], truncation=True, max_length=128, padding=True, return_tensors='pt')\nwith torch.no_grad():\n    emb = model.encode(encoded['input_ids'], encoded['attention_mask'])\nprint(f'Embedding shape: {emb.shape}')\nprint(f'Embedding norm: {emb.norm().item():.4f}')\nprint('PIPELINE OK')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python -c \"\nimport json, torch, sys\nsys.path.insert(0, 'training')\nfrom evaluation.evaluate_pool50 import load_val_data, load_model\n\n# 1. Load val data\nsamples = load_val_data('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl')\nprint(f'Val data: {len(samples)} samples')\nprint(f'Sample keys: {list(samples[0].keys())}')\nprint(f'query_tokens length: {len(samples[0][\\\"query_tokens\\\"])} chars')\n\n# 2. Load model on CPU\nckpt = '/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1'\nmodel, tokenizer, cfg = load_model(ckpt, None, torch.device('cpu'))\nprint(f'Model loaded OK: {type(model).__name__}')\nprint(f'Config model_name: {cfg[\\\"model_name\\\"]}')\n\n# 3. Single-sample encode\ntext = samples[0]['query_tokens'][:200]  # truncate for speed\nencoded = tokenizer([text], truncation=True, max_length=128, padding=True, return_tensors='pt')\nwith torch.no_grad():\n    emb = model.encode(encoded['input_ids'], encoded['attention_mask'])\nprint(f'Embedding shape: {emb.shape}')\nprint(f'Embedding norm: {emb.norm().item():.4f}')\nprint('PIPELINE OK')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T23:59:09.482659+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Val data: 2980 samples\\nSample keys: ['query_id', 'query_tokens', 'pos_tokens']\\nquery_tokens length: 4096 chars\\nModel loaded OK: StructFuseEncoder\\nConfig model_name: /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\nEmbedding shape: torch.Size([1, 256])\\nEmbedding norm: 1.0000\\nPIPELINE OK\\n\", \"stderr\": \"\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:01<00:01,  1.03s/it]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.83it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.61it/s]\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_pool50-precheck_20260515T235517",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-15T23:59:09.482945+00:00_

Pipeline 验证通过。汇总如下：

---

## 预检结果

### 脚本路径
| 脚本 | 路径 | 用途 |
|------|------|------|
| evaluate_pool50.py | `/root/structfuse/evaluation/evaluate_pool50.py` | 独立 pool=50 R@1/R@5 评估 |
| analyze_stratified.py | `/root/structfuse/evaluation/analyze_stratified.py` | 5+2 维度分层分析 |
| run_eval_p50.sh | `/root/structfuse/scripts/run_eval_p50.sh` | M1 p2b 旧脚本，**不是** M2 用的 |

### 数据路径
- Val 数据: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` (每份 2980 queries)
- M1 元数据: `/root/autodl-tmp/structfuse/full_m1_data/all.jsonl` ✅
- Dataflow 图: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json` ✅

### Checkpoint 状态 (best_by_recall_at_1)

**Qwen — 6/9 完成:**

| Strategy | s42 | s43 | s44 |
|----------|:---:|:---:|:---:|
| random | ✅ | ✅ | ✅ |
| embedding_distance | ❌ | ✅ | ✅ |
| dataflow_aware | ❌ | ✅ | ❌ |

**StarCoder — 4/9 完成:**

| Strategy | s42 | s43 | s44 |
|----------|:---:|:---:|:---:|
| random | ✅ | ✅ | ✅ |
| embedding_distance | ✅ | ❌ | ❌ |
| dataflow_aware | ❌ | ❌ | ❌ |

### Dry-run 验证
- ✅ Import chain 正常
- ✅ 两个脚本 `--help` 正常
- ✅ 模型加载成功 (StructFuseEncoder, base=Qwen2.5-Coder-3B)
- ✅ 单样本编码: shape `(1, 256)`, norm=1.0000
- ✅ Val 数据格式正确 (keys: query_id, query_tokens, pos_tokens)
- ✅ 上游数据全部存在

### 注意事项
1. **两个脚本是独立 pipeline** — analyze_stratified.py 不消费 evaluate_pool50.py 的输出，它自带 `--checkpoints-dir` 模式直接从 checkpoint re-eval
2. **evaluate_pool50.py 没有 `--max-queries` 参数** — 完整跑需要编码 2980 queries，单 GPU 约 2-5 分钟
3. **两块 GPU 当前 100% 占用**（训练中），eval 需等训练完成或使用空闲 GPU
4. **Qwen 缺 3 个 run, StarCoder 缺 5 个 run** — 还在训练中

### 结论
**Pipeline ready.** 脚本、数据、格式全部验证通过。唯一 blocker 是等待剩余 M2 checkpoint 训练完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_pool50-precheck_20260515T235517"
}
```

</details>

---
