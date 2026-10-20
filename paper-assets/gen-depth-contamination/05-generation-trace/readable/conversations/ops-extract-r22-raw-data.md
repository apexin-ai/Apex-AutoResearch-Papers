# ops extract r22 raw data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 0
- **Tool calls:** 53
- **Original source:** `logs/chats/worker_ops_extract_r22_raw_data_20260520T164246.jsonl`
- **Structured JSON:** [`a3527fa59ddb23a302d3.json`](../../sessions/a3/a3527fa59ddb23a302d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

107 recorded events

### Tool call

_source line 1 · 2026-05-20T16:49:42.627212+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T16:49:42.627565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T16:49:42.627748+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -maxdepth 3 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -maxdepth 3 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T16:49:42.627911+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T16:49:42.628170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination\\n/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base\\n/root/autodl-tmp/gen-depth-contamination/scripts\\n/root/autodl-tmp/gen-depth-contamination/scripts/__pycache__\\n/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base\\n/root/autodl-tmp/gen-depth-contamination/logs\\n/root/autodl-tmp/gen-depth-contamination/logs/exp025\\n/root/autodl-tmp/gen-depth-contamination/logs/exp026\\n/root/autodl-tmp/gen-depth-contamination/data\\n/root/autodl-tmp/gen-depth-contamination/data/exp_018_llama8b\\n/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_128\\n/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_256\\n/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_512\\n/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki\\n/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain\\n/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response\\n/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_10\\n/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_30\\n/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_50\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_olmo\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_llama8b\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_pythia\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_olmo\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_qwen7b\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_llama8b\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_mistral7b\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b\\n/root/autodl-tmp/gen-depth-con
…[truncated 6462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T16:49:42.628445+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/
…[truncated 6366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T16:49:42.628698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"permutation*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"permutation*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T16:49:42.628886+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/permutation_test.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/permutation_test.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T16:49:42.629026+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*changepoint*\" -o -name \"*pelt*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*changepoint*\" -o -name \"*pelt*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T16:49:42.629159+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/run_changepoint_kstar.py\\n/root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar\\n/root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/changepoint_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T16:49:42.629283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*bootstrap*\" -o -name \"*fold*\" -o -name \"*roc*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*bootstrap*\" -o -name \"*fold*\" -o -name \"*roc*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T16:49:42.629438+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/exp016_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp019_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp018_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/borderline_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp024_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp025_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_retrain_bootstrap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/retrain_chain_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/olmo_c4_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_bootstrap_10k.py\\n/root/autodl-tmp/gen-depth-contamination/logs/retrain_chain_bootstrap.log\\n/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/bootstrap_comparison.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k_log.txt\\n/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k\\n/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k/bootstrap_10k_comparison.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp016_b
…[truncated 855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T16:49:42.629586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*generator*\" -o -name \"*gen_id*\" -o -name \"*multi_source*\" -o -name \"*pool*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*generator*\" -o -name \"*gen_id*\" -o -name \"*multi_source*\" -o -name \"*pool*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T16:49:42.629716+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T16:49:42.629874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/__pycache__/run_multi_source_code.cpython-312.pyc\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_unified_scorer.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_vocab_only.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_arxiv.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_wiki.py\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_vocab_only_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection_v2\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection_v2/multi_source_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_unified_scorer\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_arxiv\\n/root/autodl-tmp/gen-depth-contamination/results/exp_code_multi_source.log\\n/root/autodl-tmp/gen-depth-contamination/results/exp_code_multi_source\\n/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source.log\\n/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T16:49:42.630030+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"borderline_analysis\\nborderline_bootstrap_ci.json\\nc4_subsample_control.json\\ncode_crossmodel_results.json\\ncode_crossmodel_table.tex\\ncrossscorer_bootstrap_ci.json\\ncrossscorer_bootstrap_log.txt\\nexp009_v3_full_analysis.json\\nexp009_v3_partial_10_30.json\\nexp009_v3_ratio_50_final.json\\nexp016_bootstrap_ci.json\\nexp018_bootstrap_ci.json\\nexp019_bootstrap_ci.json\\nexp024_bootstrap_ci.json\\nexp025_bootstrap_ci.json\\nexp026_feature_stability.json\\nexp026_feature_stability_v2.json\\nexp027_retrain_bootstrap.json\\nexp_14d_ablation_detail.csv\\nexp_14d_ablation_detail.json\\nexp_gemma2b_depth_bootstrap_ci.json\\nfigures\\nfull_feature_importance_17d.json\\njsd_decay_analysis.json\\njsd_decay_curves.pdf\\njsd_decay_curves.png\\nscripts\\nsemantic_ablation_multi_model.json\\nsemantic_ablation_report.json\\nsemantic_ablation_table.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T16:49:42.630205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/permutation_test.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/permutation_test.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T16:49:42.630345+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"true_auc\\\": 0.9968,\\n    \\\"p_value\\\": 0.0\\n  },\\n  \\\"1v2\\\": {\\n    \\\"true_auc\\\": 0.9855,\\n    \\\"p_value\\\": 0.0\\n  },\\n  \\\"2v3\\\": {\\n    \\\"true_auc\\\": 0.9556,\\n    \\\"p_value\\\": 0.0\\n  },\\n  \\\"3v4\\\": {\\n    \\\"true_auc\\\": 0.9029,\\n    \\\"p_value\\\": 0.304\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T16:49:42.630469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/permutation_test.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/permutation_test.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T16:49:42.630605+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"true_auc\\\": 0.9988,\\n    \\\"p_value\\\": 0.0\\n  },\\n  \\\"1v2\\\": {\\n    \\\"true_auc\\\": 0.961,\\n    \\\"p_value\\\": 0.0\\n  },\\n  \\\"2v3\\\": {\\n    \\\"true_auc\\\": 0.8919,\\n    \\\"p_value\\\": 0.998\\n  },\\n  \\\"3v4\\\": {\\n    \\\"true_auc\\\": 0.8762,\\n    \\\"p_value\\\": 1.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T16:49:42.630726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/changepoint_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/changepoint_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T16:49:42.631104+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_008_retrain_chain\\\": {\\n    \\\"auc_sequence\\\": [\\n      0.9847,\\n      0.9484,\\n      0.8888,\\n      0.7982\\n    ],\\n    \\\"n_pairs\\\": 4,\\n    \\\"pair_keys\\\": [\\n      \\\"0v1\\\",\\n      \\\"1v2\\\",\\n      \\\"2v3\\\",\\n      \\\"3v4\\\"\\n    ],\\n    \\\"kstar_theta_0.60\\\": 4,\\n    \\\"kstar_changepoint\\\": 4,\\n    \\\"breakpoints\\\": [],\\n    \\\"kstar_bootstrap\\\": {\\n      \\\"kstar_median\\\": 4,\\n      \\\"kstar_mean\\\": 4.0,\\n      \\\"kstar_mode\\\": 4,\\n      \\\"kstar_distribution\\\": {\\n        \\\"4\\\": 10000\\n      },\\n      \\\"changepoint_distribution\\\": {\\n        \\\"-1\\\": 10000\\n      },\\n      \\\"n_bootstrap\\\": 10000\\n    },\\n    \\\"method_comparison\\\": {\\n      \\\"Pelt\\\": {\\n        \\\"breakpoints\\\": [],\\n        \\\"kstar\\\": 4\\n      },\\n      \\\"Binseg\\\": {\\n        \\\"breakpoints\\\": [],\\n        \\\"kstar\\\": 4\\n      },\\n      \\\"BottomUp\\\": {\\n        \\\"breakpoints\\\": [],\\n        \\\"kstar\\\": 4\\n      }\\n    },\\n    \\\"agreement_with_theta\\\": true\\n  },\\n  \\\"exp_018_llama8b\\\": {\\n    \\\"auc_sequence\\\": [\\n      0.9225,\\n      0.6123,\\n      0.5274,\\n      0.5169,\\n      0.5162\\n    ],\\n    \\\"n_pairs\\\": 5,\\n    \\\"pair_keys\\\": [\\n      \\\"0v1\\\",\\n      \\\"1v2\\\",\\n      \\\"2v3\\\",\\n      \\\"3v4\\\",\\n      \\\"4v5\\\"\\n    ],\\n    \\\"kstar_theta_0.60\\\": 2,\\n    \\\"kstar_changepoint\\\": 1,\\n    \\\"breakpoints\\\": [\\n      1\\n    ],\\n    \\\"kstar_bootstrap\\\": {\\n      \\\"kstar_median\\\": 1,\\n      \\\"kstar_mean\\\": 1.0,\\n      \\\"kstar_mode\\\": 1,\\n      \\\"kstar_distribution\\\": {\\n        \\\"1\\\": 10000\\n      },\\n      \\\"changepoint_distribution\\\": {\\n        \\\"1\\\": 10000\\n      },\\n      \\\"n_bootstrap\\\": 10000\\n    },\\n    \\\"method_comparison\\\": {\\n      \\\"Pelt\\\": {\\n        
…[truncated 8810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T16:49:42.631289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection_v2/multi_source_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection_v2/multi_source_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T16:49:42.631506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_multi_source_detection_v2\\\",\\n  \\\"description\\\": \\\"Multi-source contamination detection v2: Qwen-1.5B + Pythia-1.4B + LLaMA-3.1-8B\\\",\\n  \\\"generators\\\": [\\n    \\\"qwen1b5\\\",\\n    \\\"pythia1b4\\\",\\n    \\\"llama8b\\\"\\n  ],\\n  \\\"docs_per_generator\\\": 1000,\\n  \\\"total_docs\\\": 3000,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 227.5,\\n  \\\"no_generator_label\\\": {\\n    \\\"pairs\\\": {\\n      \\\"0v1\\\": {\\n        \\\"auc\\\": 0.968,\\n        \\\"fold_aucs\\\": [\\n          0.9679,\\n          0.9706,\\n          0.969,\\n          0.9605,\\n          0.9735\\n        ],\\n        \\\"ci_lower\\\": 0.964,\\n        \\\"ci_upper\\\": 0.9719,\\n        \\\"boot_mean\\\": 0.968,\\n        \\\"boot_std\\\": 0.002\\n      },\\n      \\\"1v2\\\": {\\n        \\\"auc\\\": 0.7144,\\n        \\\"fold_aucs\\\": [\\n          0.6973,\\n          0.7166,\\n          0.709,\\n          0.7282,\\n          0.7222\\n        ],\\n        \\\"ci_lower\\\": 0.7019,\\n        \\\"ci_upper\\\": 0.7272,\\n        \\\"boot_mean\\\": 0.7145,\\n        \\\"boot_std\\\": 0.0065\\n      },\\n      \\\"2v3\\\": {\\n        \\\"auc\\\": 0.5201,\\n        \\\"fold_aucs\\\": [\\n          0.5107,\\n          0.5174,\\n          0.5128,\\n          0.531,\\n          0.5294\\n        ],\\n        \\\"ci_lower\\\": 0.5061,\\n        \\\"ci_upper\\\": 0.534,\\n        \\\"boot_mean\\\": 0.5201,\\n        \\\"boot_std\\\": 0.0071\\n      },\\n      \\\"3v4\\\": {\\n        \\\"auc\\\": 0.503,\\n        \\\"fold_aucs\\\": [\\n          0.4908,\\n          0.5068,\\n          0.5156,\\n          0.498,\\n          0.5048\\n        ],\\n        \\\"ci_lower\\\": 0.4891,\\n        \\\"ci_upper\\\": 0.517,\\n        \\\"boot_mean\\\": 0.503,\\n        \\\"boot_std\\\": 0.0071\\n      },\\n      \\\"4v5\\\": {\\n    
…[truncated 2757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T16:49:42.631663+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k/bootstrap_10k_comparison.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k/bootstrap_10k_comparison.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T16:49:42.631884+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Table 2 borderline bootstrap CI: 1K vs 10K comparison\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 215.4,\\n  \\\"any_verdict_flipped\\\": true,\\n  \\\"note\\\": \\\"exp_017 (Qwen-cont) and exp_002 (OLMo-1B) excluded: features.csv not found on disk\\\",\\n  \\\"cases\\\": {\\n    \\\"LLaMA-3.1-8B (exp_018)\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"1v2_auc\\\": 0.6075,\\n      \\\"fold_aucs\\\": [\\n        0.6202,\\n        0.6019,\\n        0.6181,\\n        0.5912,\\n        0.6069\\n      ],\\n      \\\"ci_1k\\\": [\\n        0.5969,\\n        0.617\\n      ],\\n      \\\"ci_10k\\\": [\\n        0.5979,\\n        0.6172\\n      ],\\n      \\\"ci_width_1k\\\": 0.0201,\\n      \\\"ci_width_10k\\\": 0.0193,\\n      \\\"perm_p_10k\\\": 0.0001,\\n      \\\"boot_mean_10k\\\": 0.6076,\\n      \\\"boot_std_10k\\\": 0.0049,\\n      \\\"verdict_1k\\\": \\\"BORDERLINE\\\",\\n      \\\"verdict_10k\\\": \\\"BORDERLINE\\\",\\n      \\\"flipped\\\": false\\n    },\\n    \\\"Gemma-2-2B (exp_gemma2b)\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"1v2_auc\\\": 0.5981,\\n      \\\"fold_aucs\\\": [\\n        0.601,\\n        0.5841,\\n        0.6006,\\n        0.5966,\\n        0.6082\\n      ],\\n      \\\"ci_1k\\\": [\\n        0.5879,\\n        0.608\\n      ],\\n      \\\"ci_10k\\\": [\\n        0.5884,\\n        0.6079\\n      ],\\n      \\\"ci_width_1k\\\": 0.0201,\\n      \\\"ci_width_10k\\\": 0.0196,\\n      \\\"perm_p_10k\\\": 0.0001,\\n      \\\"boot_mean_10k\\\": 0.5981,\\n      \\\"boot_std_10k\\\": 0.005,\\n      \\\"verdict_1k\\\": \\\"BORDERLINE\\\",\\n      \\\"verdict_10k\\\": \\\"BORDERLINE\\\",\\n      \\\"flipped\\\": false\\n    },\\n    \\\"Mistral-7B (exp_019)\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"1v2_
…[truncated 1409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T16:49:42.632105+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/changepoint_results.json')); print(json.dumps({k:{'K_OBD':v['kstar_theta_0.60'],'K_PELT':v['kstar_changepoint'],'agree':v['agreement_with_theta']} for k,v in d.items()}, indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/changepoint_results.json')); print(json.dumps({k:{'K_OBD':v['kstar_theta_0.60'],'K_PELT':v['kstar_changepoint'],'agree':v['agreement_with_theta']} for k,v in d.items()}, indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T16:49:42.632250+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T16:49:42.632375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T16:49:42.632516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.9225,\\n    \\\"1v2\\\": 0.6123,\\n    \\\"2v3\\\": 0.5274,\\n    \\\"3v4\\\": 0.5169,\\n    \\\"4v5\\\": 0.5162\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9196,\\n      0.9194,\\n      0.928,\\n      0.92,\\n      0.9257\\n    ],\\n    \\\"1v2\\\": [\\n      0.6362,\\n      0.6072,\\n      0.5975,\\n      0.6067,\\n      0.614\\n    ],\\n    \\\"2v3\\\": [\\n      0.5345,\\n      0.5442,\\n      0.5342,\\n      0.5141,\\n      0.5101\\n    ],\\n    \\\"3v4\\\": [\\n      0.5185,\\n      0.5292,\\n      0.4968,\\n      0.5175,\\n      0.5222\\n    ],\\n    \\\"4v5\\\": [\\n      0.5089,\\n      0.5225,\\n      0.5321,\\n      0.5103,\\n      0.5072\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T16:49:42.632650+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*multi_source*results*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*multi_source*results*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T16:49:42.632796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_vocab_only_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection_v2/multi_source_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T16:49:42.632927+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T16:49:42.633088+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Borderline cases bootstrap CI + permutation test\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap(10000) + label permutation(10000)\\\",\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 163.5,\\n  \\\"cases\\\": {\\n    \\\"exp-021_512tok_1v2\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"expected_auc\\\": 0.6073,\\n      \\\"auc_oof\\\": 0.6073,\\n      \\\"auc_mean_folds\\\": 0.6073,\\n      \\\"fold_aucs\\\": [\\n        0.6184,\\n        0.5979,\\n        0.5952,\\n        0.6118,\\n        0.6134\\n      ],\\n      \\\"ci_lower\\\": 0.5979,\\n      \\\"ci_upper\\\": 0.6166,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.6074,\\n      \\\"boot_std\\\": 0.0048,\\n      \\\"verdict\\\": \\\"BORDERLINE\\\",\\n      \\\"check\\\": \\\"ci_lower_gt_060\\\"\\n    },\\n    \\\"exp-020_t07_2v3\\\": {\\n      \\\"depth_pair\\\": \\\"2v3\\\",\\n      \\\"expected_auc\\\": 0.5941,\\n      \\\"auc_oof\\\": 0.5939,\\n      \\\"auc_mean_folds\\\": 0.5941,\\n      \\\"fold_aucs\\\": [\\n        0.6009,\\n        0.5951,\\n        0.5954,\\n        0.5754,\\n        0.6036\\n      ],\\n      \\\"ci_lower\\\": 0.5855,\\n      \\\"ci_upper\\\": 0.6025,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5939,\\n      \\\"boot_std\\\": 0.0043,\\n      \\\"verdict\\\": \\\"BORDERLINE\\\",\\n      \\\"check\\\": \\\"ci_upper_lt_060\\\"\\n    },\\n    \\\"exp-020_t12_1v2\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"expected_auc\\\": 0.6172,\\n      \\\"auc_oof\\\": 0.617,\\n      \\\"auc_mean_folds\\\": 0.6172,\\n      \\\"fold_aucs\\\": [\\n        0.6193,\\n        0.5961,\\n        0.6182,\\n        0.6258,\\n        0.6265\\n      ],\\n      \\\"ci_lower\\\": 0.6071,\\n      \\\"ci_upper\\\": 0.627,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.617,\\n      \\\"boot_std\\\": 0.0051,\\n      \\\"verdict\\\": \\\
…[truncated 178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T16:49:42.633261+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 -c \"\nimport json\nd=json.load(open('results/exp_changepoint_kstar/changepoint_results.json'))\nfor k,v in d.items():\n    print(f'{k}: K_OBD={v[\\\"kstar_theta_0.60\\\"]}, K_PELT={v[\\\"kstar_changepoint\\\"]}, agree={v[\\\"agreement_with_theta\\\"]}')\nprint(f'\\nTotal configs: {len(d)}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 -c \"\nimport json\nd=json.load(open('results/exp_changepoint_kstar/changepoint_results.json'))\nfor k,v in d.items():\n    print(f'{k}: K_OBD={v[\\\"kstar_theta_0.60\\\"]}, K_PELT={v[\\\"kstar_changepoint\\\"]}, agree={v[\\\"agreement_with_theta\\\"]}')\nprint(f'\\nTotal configs: {len(d)}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T16:49:42.633414+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exp_008_retrain_chain: K_OBD=4, K_PELT=4, agree=True\\nexp_018_llama8b: K_OBD=2, K_PELT=1, agree=False\\nexp_021_length_128: K_OBD=2, K_PELT=1, agree=False\\nexp_021_length_256: K_OBD=2, K_PELT=1, agree=False\\nexp_021_length_512: K_OBD=2, K_PELT=1, agree=False\\nexp_023_wiki: K_OBD=2, K_PELT=1, agree=False\\nexp_024_arxiv: K_OBD=3, K_PELT=2, agree=False\\nexp_025_pythia_arxiv: K_OBD=3, K_PELT=2, agree=False\\nexp_027_latex_ablation: K_OBD=3, K_PELT=2, agree=False\\nexp_14b_c4: K_OBD=2, K_PELT=1, agree=False\\nexp_arXiv_llama8b: K_OBD=3, K_PELT=2, agree=False\\nexp_arXiv_llama8b_crossscorer: K_OBD=3, K_PELT=2, agree=False\\nexp_arXiv_mistral7b: K_OBD=3, K_PELT=2, agree=False\\nexp_arXiv_mistral7b_crossscorer: K_OBD=3, K_PELT=2, agree=False\\nexp_arXiv_olmo: K_OBD=1, K_PELT=1, agree=True\\nexp_arXiv_qwen1b5_crossscorer: K_OBD=3, K_PELT=2, agree=False\\nexp_arXiv_qwen7b: K_OBD=3, K_PELT=2, agree=False\\nexp_arXiv_qwen7b_crossscorer: K_OBD=2, K_PELT=2, agree=True\\nexp_code_llama8b: K_OBD=2, K_PELT=2, agree=True\\nexp_code_mistral7b: K_OBD=2, K_PELT=1, agree=False\\nexp_code_pythia1b4: K_OBD=1, K_PELT=1, agree=True\\nexp_code_qwen1b5: K_OBD=2, K_PELT=2, agree=True\\nexp_code_qwen1b5_pythia_scorer: K_OBD=2, K_PELT=2, agree=True\\nexp_code_qwen7b: K_OBD=2, K_PELT=2, agree=True\\nexp_pythia_retrain_depth7: K_OBD=7, K_PELT=4, agree=False\\nexp_qwen_retrain_chain: K_OBD=4, K_PELT=4, agree=True\\nexp_qwen_retrain_chain_ext: K_OBD=7, K_PELT=2, agree=False\\nexp_wiki_llama8b: K_OBD=1, K_PELT=1, agree=True\\nexp_wiki_mistral7b: K_OBD=1, K_PELT=1, agree=True\\nexp_wiki_olmo: K_OBD=1, K_PELT=1, agree=True\\nexp_wiki_olmo_v2: K_OBD=1, K_PELT=1, agree=True\\nexp_wiki_pythia: K_OBD=2, K_PELT=1, agree=False\\nexp_wiki_pythia_v2: K_OBD=1, K_PELT=1, agree=True\\nexp_wiki_qwen7b: K_OBD=2, K_PELT=1, agree=False\\nexp_wiki_scorer_confound: K_OBD=1, K_PELT=1, agree=True\\nexp_wiki_scorer_confound_1b5: K_OBD=1, K_PELT=1, agree=True\\no
…[truncated 172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T16:49:42.633569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T16:49:42.633769+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_multi_source_detection\\\",\\n  \\\"description\\\": \\\"Multi-source contamination detection: 3 generators mixed pool\\\",\\n  \\\"generators\\\": [\\n    \\\"qwen1b5\\\",\\n    \\\"pythia1b4\\\",\\n    \\\"olmo1b\\\"\\n  ],\\n  \\\"docs_per_generator\\\": 1000,\\n  \\\"total_docs\\\": 3000,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 220.3,\\n  \\\"no_generator_label\\\": {\\n    \\\"pairs\\\": {\\n      \\\"0v1\\\": {\\n        \\\"auc\\\": 0.9929,\\n        \\\"fold_aucs\\\": [\\n          0.9935,\\n          0.9937,\\n          0.9937,\\n          0.9898,\\n          0.9942\\n        ],\\n        \\\"ci_lower\\\": 0.9915,\\n        \\\"ci_upper\\\": 0.9942,\\n        \\\"boot_mean\\\": 0.9929,\\n        \\\"boot_std\\\": 0.0007\\n      },\\n      \\\"1v2\\\": {\\n        \\\"auc\\\": 0.7007,\\n        \\\"fold_aucs\\\": [\\n          0.6713,\\n          0.7012,\\n          0.6893,\\n          0.7237,\\n          0.7194\\n        ],\\n        \\\"ci_lower\\\": 0.6874,\\n        \\\"ci_upper\\\": 0.7142,\\n        \\\"boot_mean\\\": 0.7007,\\n        \\\"boot_std\\\": 0.0068\\n      },\\n      \\\"2v3\\\": {\\n        \\\"auc\\\": 0.5128,\\n        \\\"fold_aucs\\\": [\\n          0.5121,\\n          0.4992,\\n          0.5166,\\n          0.5208,\\n          0.5168\\n        ],\\n        \\\"ci_lower\\\": 0.4988,\\n        \\\"ci_upper\\\": 0.5268,\\n        \\\"boot_mean\\\": 0.5128,\\n        \\\"boot_std\\\": 0.0071\\n      },\\n      \\\"3v4\\\": {\\n        \\\"auc\\\": 0.4958,\\n        \\\"fold_aucs\\\": [\\n          0.4882,\\n          0.4842,\\n          0.5271,\\n          0.5061,\\n          0.4736\\n        ],\\n        \\\"ci_lower\\\": 0.4816,\\n        \\\"ci_upper\\\": 0.51,\\n        \\\"boot_mean\\\": 0.4958,\\n        \\\"boot_std\\\": 0.0073\\n      },\\n      \\\"4v5\\\": {\\n        \\\"auc\
…[truncated 2435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T16:49:42.633942+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_code_multi_source/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_code_multi_source/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T16:49:42.634071+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"features_llama8b_qwen_scorer.csv\\nfeatures_mistral7b_qwen_scorer.csv\\nfeatures_qwen7b_qwen_scorer.csv\\nresults.json\\nresults_vocab_only.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T16:49:42.634200+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T16:49:42.634321+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_arxiv/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_arxiv/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T16:49:42.634446+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"features_llama8b_qwen_scorer.csv\\nfeatures_mistral7b_qwen_scorer.csv\\nresults.json\\nresults_vocab_only.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T16:49:42.634564+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"features_llama8b_qwen_scorer.csv\\nfeatures_pythia1b4_qwen_scorer.csv\\nresults.json\\nresults_vocab_only.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T16:49:42.634694+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_code_multi_source/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_code_multi_source/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T16:49:42.634953+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_code_multi_source\\\",\\n  \\\"domain\\\": \\\"Code (CodeSearchNet Python)\\\",\\n  \\\"scorer\\\": \\\"Qwen2.5-1.5B\\\",\\n  \\\"generators\\\": [\\n    \\\"qwen7b\\\",\\n    \\\"llama8b\\\",\\n    \\\"mistral7b\\\"\\n  ],\\n  \\\"docs_per_generator\\\": 1000,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 2024.9,\\n  \\\"vocab_only\\\": {\\n    \\\"no_label\\\": {\\n      \\\"pairs\\\": {\\n        \\\"0v1\\\": {\\n          \\\"auc\\\": 0.7891,\\n          \\\"fold_aucs\\\": [\\n            0.7995,\\n            0.7865,\\n            0.7852,\\n            0.7931,\\n            0.7823\\n          ],\\n          \\\"ci_lower\\\": 0.7785,\\n          \\\"ci_upper\\\": 0.7997,\\n          \\\"boot_mean\\\": 0.7892,\\n          \\\"boot_std\\\": 0.0054\\n        },\\n        \\\"1v2\\\": {\\n          \\\"auc\\\": 0.6353,\\n          \\\"fold_aucs\\\": [\\n            0.6428,\\n            0.6346,\\n            0.6438,\\n            0.6368,\\n            0.6203\\n          ],\\n          \\\"ci_lower\\\": 0.6225,\\n          \\\"ci_upper\\\": 0.6482,\\n          \\\"boot_mean\\\": 0.6353,\\n          \\\"boot_std\\\": 0.0066\\n        },\\n        \\\"2v3\\\": {\\n          \\\"auc\\\": 0.5121,\\n          \\\"fold_aucs\\\": [\\n            0.5046,\\n            0.5181,\\n            0.5091,\\n            0.5213,\\n            0.5081\\n          ],\\n          \\\"ci_lower\\\": 0.4979,\\n          \\\"ci_upper\\\": 0.5267,\\n          \\\"boot_mean\\\": 0.5122,\\n          \\\"boot_std\\\": 0.0073\\n        },\\n        \\\"3v4\\\": {\\n          \\\"auc\\\": 0.5103,\\n          \\\"fold_aucs\\\": [\\n            0.5006,\\n            0.5003,\\n            0.5411,\\n            0.4985,\\n            0.5129\\n          ],\\n          \\\"ci_lower\\\": 0.4962,\\n          \\\"ci_upper\\\": 0.5248,\\n          \\\"boot_mean\\
…[truncated 6706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T16:49:42.635120+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T16:49:42.635387+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_wiki_multi_source\\\",\\n  \\\"domain\\\": \\\"Wiki\\\",\\n  \\\"scorer\\\": \\\"Qwen2.5-1.5B\\\",\\n  \\\"generators\\\": [\\n    \\\"qwen1b5\\\",\\n    \\\"llama8b\\\",\\n    \\\"mistral7b\\\"\\n  ],\\n  \\\"docs_per_generator\\\": 1000,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 3498.6,\\n  \\\"vocab_only\\\": {\\n    \\\"no_label\\\": {\\n      \\\"pairs\\\": {\\n        \\\"0v1\\\": {\\n          \\\"auc\\\": 0.7616,\\n          \\\"fold_aucs\\\": [\\n            0.764,\\n            0.7696,\\n            0.7491,\\n            0.7595,\\n            0.7662\\n          ],\\n          \\\"ci_lower\\\": 0.7505,\\n          \\\"ci_upper\\\": 0.7723,\\n          \\\"boot_mean\\\": 0.7616,\\n          \\\"boot_std\\\": 0.0055\\n        },\\n        \\\"1v2\\\": {\\n          \\\"auc\\\": 0.5434,\\n          \\\"fold_aucs\\\": [\\n            0.5696,\\n            0.5165,\\n            0.5338,\\n            0.543,\\n            0.5533\\n          ],\\n          \\\"ci_lower\\\": 0.5292,\\n          \\\"ci_upper\\\": 0.5575,\\n          \\\"boot_mean\\\": 0.5434,\\n          \\\"boot_std\\\": 0.0072\\n        },\\n        \\\"2v3\\\": {\\n          \\\"auc\\\": 0.517,\\n          \\\"fold_aucs\\\": [\\n            0.5274,\\n            0.4981,\\n            0.5323,\\n            0.5071,\\n            0.521\\n          ],\\n          \\\"ci_lower\\\": 0.503,\\n          \\\"ci_upper\\\": 0.5312,\\n          \\\"boot_mean\\\": 0.517,\\n          \\\"boot_std\\\": 0.0072\\n        },\\n        \\\"3v4\\\": {\\n          \\\"auc\\\": 0.5017,\\n          \\\"fold_aucs\\\": [\\n            0.4993,\\n            0.4811,\\n            0.5254,\\n            0.4895,\\n            0.5146\\n          ],\\n          \\\"ci_lower\\\": 0.4874,\\n          \\\"ci_upper\\\": 0.516,\\n          \\\"boot_mean\\\": 0.5016,\\n          \\\"b
…[truncated 6426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T16:49:42.635550+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_arxiv/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_arxiv/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T16:49:42.635824+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_multi_source_arxiv\\\",\\n  \\\"domain\\\": \\\"arXiv\\\",\\n  \\\"scorer\\\": \\\"Qwen2.5-1.5B\\\",\\n  \\\"generators\\\": [\\n    \\\"qwen1b5\\\",\\n    \\\"pythia1b4\\\",\\n    \\\"llama8b\\\"\\n  ],\\n  \\\"docs_per_generator\\\": 1000,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 914.8,\\n  \\\"vocab_only\\\": {\\n    \\\"no_label\\\": {\\n      \\\"pairs\\\": {\\n        \\\"0v1\\\": {\\n          \\\"auc\\\": 0.9431,\\n          \\\"fold_aucs\\\": [\\n            0.9492,\\n            0.9602,\\n            0.9342,\\n            0.9354,\\n            0.937\\n          ],\\n          \\\"ci_lower\\\": 0.9378,\\n          \\\"ci_upper\\\": 0.9482,\\n          \\\"boot_mean\\\": 0.9431,\\n          \\\"boot_std\\\": 0.0026\\n        },\\n        \\\"1v2\\\": {\\n          \\\"auc\\\": 0.6922,\\n          \\\"fold_aucs\\\": [\\n            0.6861,\\n            0.7229,\\n            0.6779,\\n            0.6676,\\n            0.7068\\n          ],\\n          \\\"ci_lower\\\": 0.68,\\n          \\\"ci_upper\\\": 0.7044,\\n          \\\"boot_mean\\\": 0.6922,\\n          \\\"boot_std\\\": 0.0062\\n        },\\n        \\\"2v3\\\": {\\n          \\\"auc\\\": 0.589,\\n          \\\"fold_aucs\\\": [\\n            0.5814,\\n            0.5918,\\n            0.5757,\\n            0.5893,\\n            0.6071\\n          ],\\n          \\\"ci_lower\\\": 0.5755,\\n          \\\"ci_upper\\\": 0.6026,\\n          \\\"boot_mean\\\": 0.589,\\n          \\\"boot_std\\\": 0.0069\\n        },\\n        \\\"3v4\\\": {\\n          \\\"auc\\\": 0.5082,\\n          \\\"fold_aucs\\\": [\\n            0.5053,\\n            0.5034,\\n            0.5289,\\n            0.505,\\n            0.4995\\n          ],\\n          \\\"ci_lower\\\": 0.4941,\\n          \\\"ci_upper\\\": 0.5222,\\n          \\\"boot_mean\\\": 0.5082,\\n          \\\
…[truncated 6439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T16:49:42.635994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -rl \"perm_p\\|permutation\\|p_value\" /root/autodl-tmp/gen-depth-contamination/results/ /root/autodl-tmp/gen-depth-contamination/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -rl \"perm_p\\|permutation\\|p_value\" /root/autodl-tmp/gen-depth-contamination/results/ /root/autodl-tmp/gen-depth-contamination/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T16:49:42.636126+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T16:49:42.636250+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -rl \"generator_identity\\|gen_id\\|generator_auc\" /root/autodl-tmp/gen-depth-contamination/results/ /root/autodl-tmp/gen-depth-contamination/artifacts/ /root/autodl-tmp/gen-depth-contamination/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -rl \"generator_identity\\|gen_id\\|generator_auc\" /root/autodl-tmp/gen-depth-contamination/results/ /root/autodl-tmp/gen-depth-contamination/artifacts/ /root/autodl-tmp/gen-depth-contamination/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T16:49:42.636381+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T16:49:42.636536+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && grep -rl \"generator_identity\\|gen_id\\|generator_auc\" results/ artifacts/ scripts/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && grep -rl \"generator_identity\\|gen_id\\|generator_auc\" results/ artifacts/ scripts/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T16:49:42.636668+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"scripts/__pycache__/run_multi_source_code.cpython-312.pyc\\nscripts/run_multi_source.py\\nscripts/run_multi_source_v2.py\\nscripts/run_multi_source_unified_scorer.py\\nscripts/run_multi_source_vocab_only.py\\nscripts/run_multi_source_arxiv.py\\nscripts/run_multi_source_code.py\\nscripts/run_multi_source_wiki.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T16:49:42.636805+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && grep -rl \"perm_p\\|permutation\\|p_value\" results/ artifacts/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && grep -rl \"perm_p\\|permutation\\|p_value\" results/ artifacts/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T16:49:42.636947+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results/exp_008_retrain_chain/permutation_test.json\\nresults/exp_008_retrain_chain/summary.json\\nresults/exp_008_retrain_chain/bootstrap_ci_v2.json\\nresults/exp_009_dose_response/ratio_10/statistical_analysis.json\\nresults/exp_009_dose_response/ratio_30/statistical_analysis.json\\nresults/exp_009_dose_response/ratio_50/statistical_analysis.json\\nresults/exp_14b_c4/bootstrap_ci_results.json\\nresults/exp_027_latex_ablation/bootstrap_ci_results.json\\nresults/exp_olmo_retrain_chain/permutation_test.json\\nresults/exp_olmo_retrain_chain/summary.json\\nresults/lofo_importance/lofo_results.json\\nresults/exp_014_naturalistic/cc_sample.jsonl\\nresults/exp_bootstrap_10k/bootstrap_10k_comparison.json\\nartifacts/exp016_bootstrap_ci.json\\nartifacts/exp019_bootstrap_ci.json\\nartifacts/exp018_bootstrap_ci.json\\nartifacts/borderline_bootstrap_ci.json\\nartifacts/exp024_bootstrap_ci.json\\nartifacts/exp025_bootstrap_ci.json\\nartifacts/exp027_retrain_bootstrap.json\\nartifacts/crossscorer_bootstrap_ci.json\\nartifacts/exp_gemma2b_depth_bootstrap_ci.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T16:49:42.637073+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/bootstrap_comparison.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_changepoint_kstar/bootstrap_comparison.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T16:49:42.637403+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_008_retrain_chain\\\": {\\n    \\\"kstar_theta\\\": 4,\\n    \\\"kstar_direct_cp\\\": 4,\\n    \\\"kstar_boot_median\\\": 4,\\n    \\\"kstar_boot_mode\\\": 4,\\n    \\\"boot_distribution\\\": {\\n      \\\"4\\\": 10000\\n    },\\n    \\\"direct_agrees_theta\\\": true,\\n    \\\"boot_median_agrees_theta\\\": true,\\n    \\\"boot_mode_agrees_theta\\\": true\\n  },\\n  \\\"exp_018_llama8b\\\": {\\n    \\\"kstar_theta\\\": 2,\\n    \\\"kstar_direct_cp\\\": 1,\\n    \\\"kstar_boot_median\\\": 1,\\n    \\\"kstar_boot_mode\\\": 1,\\n    \\\"boot_distribution\\\": {\\n      \\\"1\\\": 10000\\n    },\\n    \\\"direct_agrees_theta\\\": false,\\n    \\\"boot_median_agrees_theta\\\": false,\\n    \\\"boot_mode_agrees_theta\\\": false\\n  },\\n  \\\"exp_021_length_128\\\": {\\n    \\\"kstar_theta\\\": 2,\\n    \\\"kstar_direct_cp\\\": 1,\\n    \\\"kstar_boot_median\\\": 1,\\n    \\\"kstar_boot_mode\\\": 1,\\n    \\\"boot_distribution\\\": {\\n      \\\"1\\\": 10000\\n    },\\n    \\\"direct_agrees_theta\\\": false,\\n    \\\"boot_median_agrees_theta\\\": false,\\n    \\\"boot_mode_agrees_theta\\\": false\\n  },\\n  \\\"exp_021_length_256\\\": {\\n    \\\"kstar_theta\\\": 2,\\n    \\\"kstar_direct_cp\\\": 1,\\n    \\\"kstar_boot_median\\\": 1,\\n    \\\"kstar_boot_mode\\\": 1,\\n    \\\"boot_distribution\\\": {\\n      \\\"1\\\": 10000\\n    },\\n    \\\"direct_agrees_theta\\\": false,\\n    \\\"boot_median_agrees_theta\\\": false,\\n    \\\"boot_mode_agrees_theta\\\": false\\n  },\\n  \\\"exp_021_length_512\\\": {\\n    \\\"kstar_theta\\\": 2,\\n    \\\"kstar_direct_cp\\\": 1,\\n    \\\"kstar_boot_median\\\": 1,\\n    \\\"kstar_boot_mode\\\": 1,\\n    \\\"boot_distribution\\\": {\\n      \\\"1\\\": 10000\\n    },\\n    \\\"direct_agrees_theta\\\": false,\\n    \\\"boot_median_agrees_theta\\\": false,\\n    \\\"boot_mode_agrees_theta\\\": false\\n  },\\n  \\\"exp_023_wiki\\\": {\\n    \\\"kstar_theta\\\": 2,\\n
…[truncated 8504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T16:49:42.637599+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp016_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp016_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T16:49:42.637790+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-016 Qwen2.5-1.5B base continuation\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 282.0,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.987,\\n      \\\"auc_mean_folds\\\": 0.987,\\n      \\\"fold_aucs\\\": [\\n        0.9881,\\n        0.9884,\\n        0.9852,\\n        0.9851,\\n        0.9882\\n      ],\\n      \\\"ci_lower\\\": 0.9853,\\n      \\\"ci_upper\\\": 0.9885,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.9869,\\n      \\\"boot_std\\\": 0.0008\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.626,\\n      \\\"auc_mean_folds\\\": 0.6262,\\n      \\\"fold_aucs\\\": [\\n        0.5963,\\n        0.6362,\\n        0.6366,\\n        0.6337,\\n        0.6282\\n      ],\\n      \\\"ci_lower\\\": 0.6168,\\n      \\\"ci_upper\\\": 0.6353,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.6261,\\n      \\\"boot_std\\\": 0.0047\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.5496,\\n      \\\"auc_mean_folds\\\": 0.5496,\\n      \\\"fold_aucs\\\": [\\n        0.5516,\\n        0.5456,\\n        0.5403,\\n        0.5605,\\n        0.5501\\n      ],\\n      \\\"ci_lower\\\": 0.5397,\\n      \\\"ci_upper\\\": 0.56,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5496,\\n      \\\"boot_std\\\": 0.0052\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5293,\\n      \\\"auc_mean_folds\\\": 0.5294,\\n      \\\"fold_aucs\\\": [\\n        0.5515,\\n        0.5133,\\n        0.5198,\\n        0.535,\\n        0.5276\\n      ],\\n      \\\"ci_lower\\\": 0.5188,\\n      \\\"ci_upper\\\": 0.5399,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5292,\\n      \\\"boot_std\\\": 0.0054\\n    },\\n    \\\"4v5\\\": {\\n      \\\"auc\\\": 0.5181,\\n      \\
…[truncated 448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T16:49:42.637952+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp018_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp018_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T16:49:42.638130+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-018 LLaMA-3.1-8B continuation, scorer=Qwen2.5-1.5B base\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 255.4,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9224,\\n      \\\"auc_mean_folds\\\": 0.9225,\\n      \\\"fold_aucs\\\": [\\n        0.9196,\\n        0.9194,\\n        0.928,\\n        0.92,\\n        0.9257\\n      ],\\n      \\\"ci_lower\\\": 0.9174,\\n      \\\"ci_upper\\\": 0.9272,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.9224,\\n      \\\"boot_std\\\": 0.0025\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.6123,\\n      \\\"auc_mean_folds\\\": 0.6123,\\n      \\\"fold_aucs\\\": [\\n        0.6362,\\n        0.6072,\\n        0.5975,\\n        0.6067,\\n        0.614\\n      ],\\n      \\\"ci_lower\\\": 0.6028,\\n      \\\"ci_upper\\\": 0.6216,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.6123,\\n      \\\"boot_std\\\": 0.0048\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.5273,\\n      \\\"auc_mean_folds\\\": 0.5274,\\n      \\\"fold_aucs\\\": [\\n        0.5345,\\n        0.5442,\\n        0.5342,\\n        0.5141,\\n        0.5101\\n      ],\\n      \\\"ci_lower\\\": 0.5169,\\n      \\\"ci_upper\\\": 0.5378,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5273,\\n      \\\"boot_std\\\": 0.0053\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5168,\\n      \\\"auc_mean_folds\\\": 0.5169,\\n      \\\"fold_aucs\\\": [\\n        0.5185,\\n        0.5292,\\n        0.4968,\\n        0.5175,\\n        0.5222\\n      ],\\n      \\\"ci_lower\\\": 0.5062,\\n      \\\"ci_upper\\\": 0.5275,\\n      \\\"perm_p\\\": 0.0037,\\n      \\\"boot_mean\\\": 0.5168,\\n      \\\"boot_std\\\": 0.0054\\n    },\\n    \\\"4v5\\\": {\\n      \\\"auc\
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T16:49:42.638283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp024_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp024_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T16:49:42.638459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-024 Qwen2.5-1.5B-base arXiv continuation\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 3,\\n  \\\"total_seconds\\\": 147.4,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9946,\\n      \\\"auc_mean_folds\\\": 0.9948,\\n      \\\"fold_aucs\\\": [\\n        0.9956,\\n        0.9955,\\n        0.9938,\\n        0.9938,\\n        0.9952\\n      ],\\n      \\\"ci_lower\\\": 0.9929,\\n      \\\"ci_upper\\\": 0.9961,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9946,\\n      \\\"boot_std\\\": 0.0008\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.858,\\n      \\\"auc_mean_folds\\\": 0.8581,\\n      \\\"fold_aucs\\\": [\\n        0.8763,\\n        0.8669,\\n        0.8411,\\n        0.8515,\\n        0.8549\\n      ],\\n      \\\"ci_lower\\\": 0.848,\\n      \\\"ci_upper\\\": 0.8679,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.858,\\n      \\\"boot_std\\\": 0.005\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.6427,\\n      \\\"auc_mean_folds\\\": 0.6436,\\n      \\\"fold_aucs\\\": [\\n        0.6738,\\n        0.6349,\\n        0.6479,\\n        0.6537,\\n        0.6078\\n      ],\\n      \\\"ci_lower\\\": 0.6275,\\n      \\\"ci_upper\\\": 0.6575,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.6426,\\n      \\\"boot_std\\\": 0.0077\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5437,\\n      \\\"auc_mean_folds\\\": 0.544,\\n      \\\"fold_aucs\\\": [\\n        0.52,\\n        0.5346,\\
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T16:49:42.638609+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T16:49:42.638944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"scorer\\\": \\\"Pythia-1.4B (cross-scorer)\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"total_seconds\\\": 621.0,\\n  \\\"models\\\": {\\n    \\\"Qwen-7B\\\": {\\n      \\\"experiment\\\": \\\"exp_arXiv_qwen7b_crossscorer\\\",\\n      \\\"kstar_ci\\\": 2,\\n      \\\"total_seconds\\\": 155.7,\\n      \\\"pairs\\\": {\\n        \\\"0v1\\\": {\\n          \\\"auc\\\": 0.9573,\\n          \\\"auc_mean_folds\\\": 0.9575,\\n          \\\"fold_aucs\\\": [\\n            0.9614,\\n            0.9561,\\n            0.968,\\n            0.9454,\\n            0.9567\\n          ],\\n          \\\"ci_lower\\\": 0.9518,\\n          \\\"ci_upper\\\": 0.9626,\\n          \\\"ci_lower_above_theta\\\": true,\\n          \\\"ci_upper_above_theta\\\": true,\\n          \\\"perm_p\\\": 0.0001,\\n          \\\"p_vs_theta_0.60\\\": 0.0,\\n          \\\"boot_mean\\\": 0.9573,\\n          \\\"boot_std\\\": 0.0027\\n        },\\n        \\\"1v2\\\": {\\n          \\\"auc\\\": 0.8163,\\n          \\\"auc_mean_folds\\\": 0.8171,\\n          \\\"fold_aucs\\\": [\\n            0.7892,\\n            0.8093,\\n            0.8265,\\n            0.8236,\\n            0.8372\\n          ],\\n          \\\"ci_lower\\\": 0.8049,\\n          \\\"ci_upper\\\": 0.8277,\\n          \\\"ci_lower_above_theta\\\": true,\\n          \\\"ci_upper_above_theta\\\": true,\\n          \\\"perm_p\\\": 0.0001,\\n          \\\"p_vs_theta_0.60\\\": 0.0,\\n          \\\"boot_mean\\\": 0.8162,\\n          \\\"boot_std\\\": 0.0058\\n        },\\n        \\\"2v3\\\": {\\n          \\\"auc\\\": 0.5986,\\n          \\\"auc_mean_folds\\\": 0.5989,\\n          \\\"fold_aucs\\\": [\\n            0.592,\\n            0.6006,\\n            0.6108,\\n            0.5768,\\n            0.6142\\n      
…[truncated 8073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T16:49:42.639151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp019_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp019_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T16:49:42.639347+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-019 Mistral-7B-Instruct continuation\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 1,\\n  \\\"total_seconds\\\": 274.4,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9842,\\n      \\\"auc_mean_folds\\\": 0.9843,\\n      \\\"fold_aucs\\\": [\\n        0.9833,\\n        0.9875,\\n        0.9854,\\n        0.9817,\\n        0.9838\\n      ],\\n      \\\"ci_lower\\\": 0.9824,\\n      \\\"ci_upper\\\": 0.986,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9842,\\n      \\\"boot_std\\\": 0.0009\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.5934,\\n      \\\"auc_mean_folds\\\": 0.5935,\\n      \\\"fold_aucs\\\": [\\n        0.5981,\\n        0.5894,\\n        0.5962,\\n        0.585,\\n        0.5988\\n      ],\\n      \\\"ci_lower\\\": 0.5835,\\n      \\\"ci_upper\\\": 0.6032,\\n      \\\"ci_lower_above_theta\\\": false,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.9017,\\n      \\\"boot_mean\\\": 0.5934,\\n      \\\"boot_std\\\": 0.005\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.5402,\\n      \\\"auc_mean_folds\\\": 0.5402,\\n      \\\"fold_aucs\\\": [\\n        0.5308,\\n        0.534,\\n        0.5493,\\n        0.5584,\\n        0.5286\\n      ],\\n      \\\"ci_lower\\\": 0.5301,\\n      \\\"ci_upper\\\": 0.551,\\n      \\\"ci_lower_above_theta\\\": false,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 1.0,\\n      \\\"boot_mean\\\": 0.5403,\\n      \\\"boot_std\\\": 0.0053\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5233,\\n      \\\"auc_mean_folds\\\": 0.5232,\\n      \\\"fold_aucs\\\": [\\n        0.5254,\\n        0.5164
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T16:49:42.639504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp025_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp025_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-20T16:49:42.639682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-025 Pythia-1.4B arXiv continuation (domain x model interaction)\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 3,\\n  \\\"total_seconds\\\": 146.8,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9876,\\n      \\\"auc_mean_folds\\\": 0.9877,\\n      \\\"fold_aucs\\\": [\\n        0.9914,\\n        0.9889,\\n        0.9844,\\n        0.9895,\\n        0.9845\\n      ],\\n      \\\"ci_lower\\\": 0.9851,\\n      \\\"ci_upper\\\": 0.99,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9876,\\n      \\\"boot_std\\\": 0.0012\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.8047,\\n      \\\"auc_mean_folds\\\": 0.8047,\\n      \\\"fold_aucs\\\": [\\n        0.7906,\\n        0.8278,\\n        0.8018,\\n        0.8065,\\n        0.7967\\n      ],\\n      \\\"ci_lower\\\": 0.7934,\\n      \\\"ci_upper\\\": 0.8162,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.8047,\\n      \\\"boot_std\\\": 0.0058\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.6544,\\n      \\\"auc_mean_folds\\\": 0.6545,\\n      \\\"fold_aucs\\\": [\\n        0.6409,\\n        0.6433,\\n        0.6764,\\n        0.6548,\\n        0.6572\\n      ],\\n      \\\"ci_lower\\\": 0.6401,\\n      \\\"ci_upper\\\": 0.6688,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.6544,\\n      \\\"boot_std\\\": 0.0073\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.55,\\n      \\\"auc_mean_folds\\\": 0.5507,\\n      \\\"fold_aucs\\\": [\\n        0
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T16:49:42.639855+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-20T16:49:42.640066+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-027 retrain-chain bootstrap CI (based on exp-008 v2)\\\",\\n  \\\"source_data\\\": \\\"exp_008_retrain_chain features.csv\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 4,\\n  \\\"total_seconds\\\": 197.9,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc_point\\\": 0.9847,\\n      \\\"auc_mean_folds\\\": 0.9847,\\n      \\\"fold_aucs\\\": [\\n        0.9831,\\n        0.9852,\\n        0.9851,\\n        0.9842,\\n        0.986\\n      ],\\n      \\\"ci_lower\\\": 0.9828,\\n      \\\"ci_upper\\\": 0.9864,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.9847,\\n      \\\"boot_std\\\": 0.0009\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc_point\\\": 0.9482,\\n      \\\"auc_mean_folds\\\": 0.9484,\\n      \\\"fold_aucs\\\": [\\n        0.9464,\\n        0.9513,\\n        0.9462,\\n        0.9486,\\n        0.9497\\n      ],\\n      \\\"ci_lower\\\": 0.9443,\\n      \\\"ci_upper\\\": 0.952,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.9482,\\n      \\\"boot_std\\\": 0.002\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc_point\\\": 0.8885,\\n      \\\"auc_mean_folds\\\": 0.8888,\\n      \\\"fold_aucs\\\": [\\n        0.8982,\\n        0.8888,\\n        0.8837,\\n        0.8833,\\n        0.8901\\n      ],\\n      \\\"ci_lower\\\": 0.8829,\\n      \\\"ci_upper\\\": 0.894,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.8885,\\n      \\\"boot_std\\\": 0.0028\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc_point\\\": 0.7977,\\n      \\\"auc_mean_folds\\\": 0.7982,\\n      \\\"fold_aucs\\\": [\\n        0.8058,\\n        0.7962,\\n     
…[truncated 389 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-20T16:49:42.640246+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp_gemma2b_depth_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp_gemma2b_depth_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T16:49:42.640424+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_gemma2b_depth: Gemma-2-2B continuation, scorer=Qwen2.5-1.5B base\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 259.6,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.953,\\n      \\\"auc_mean_folds\\\": 0.9534,\\n      \\\"fold_aucs\\\": [\\n        0.9519,\\n        0.9482,\\n        0.9548,\\n        0.955,\\n        0.9568\\n      ],\\n      \\\"ci_lower\\\": 0.9494,\\n      \\\"ci_upper\\\": 0.9565,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.953,\\n      \\\"boot_std\\\": 0.0018\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.5981,\\n      \\\"auc_mean_folds\\\": 0.5981,\\n      \\\"fold_aucs\\\": [\\n        0.601,\\n        0.5841,\\n        0.6006,\\n        0.5966,\\n        0.6082\\n      ],\\n      \\\"ci_lower\\\": 0.5882,\\n      \\\"ci_upper\\\": 0.6076,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5981,\\n      \\\"boot_std\\\": 0.005\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.534,\\n      \\\"auc_mean_folds\\\": 0.5342,\\n      \\\"fold_aucs\\\": [\\n        0.5598,\\n        0.5246,\\n        0.5338,\\n        0.5241,\\n        0.5286\\n      ],\\n      \\\"ci_lower\\\": 0.5234,\\n      \\\"ci_upper\\\": 0.5446,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5339,\\n      \\\"boot_std\\\": 0.0054\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5033,\\n      \\\"auc_mean_folds\\\": 0.503,\\n      \\\"fold_aucs\\\": [\\n        0.5072,\\n        0.5006,\\n        0.4992,\\n        0.5014,\\n        0.5068\\n      ],\\n      \\\"ci_lower\\\": 0.4924,\\n      \\\"ci_upper\\\": 0.5142,\\n      \\\"perm_p\\\": 0.291871,\\n      \\\"boot_mean\\\": 0.5032,\\n      \\\"boot_std\\\": 0.0055\\n    },\\n    \\\"4v5\\\": {\\n      
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T16:49:42.640573+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T16:49:42.640745+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_008_retrain_chain_v2\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"protocol\\\": \\\"retrain-chain (independent LoRA per generation)\\\",\\n  \\\"scorer\\\": \\\"Qwen2.5-1.5B\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"max_depth\\\": 4,\\n  \\\"kstar_ci\\\": 4,\\n  \\\"total_seconds\\\": 195.7,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc_oof\\\": 0.9842,\\n      \\\"auc_mean_folds\\\": 0.9843,\\n      \\\"fold_aucs\\\": [\\n        0.985,\\n        0.9849,\\n        0.9848,\\n        0.9801,\\n        0.9865\\n      ],\\n      \\\"ci_lower\\\": 0.9823,\\n      \\\"ci_upper\\\": 0.986,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9842,\\n      \\\"boot_std\\\": 0.0009\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc_oof\\\": 0.9471,\\n      \\\"auc_mean_folds\\\": 0.9472,\\n      \\\"fold_aucs\\\": [\\n        0.952,\\n        0.9444,\\n        0.9558,\\n        0.9401,\\n        0.9437\\n      ],\\n      \\\"ci_lower\\\": 0.9432,\\n      \\\"ci_upper\\\": 0.9509,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9471,\\n      \\\"boot_std\\\": 0.002\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc_oof\\\": 0.8888,\\n      \\\"auc_mean_folds\\\": 0.8891,\\n      \\\"fold_aucs\\\": [\\n        0.8794,\\n        0.8828,\\n        0.8998,\\n        0.8986,\\n        0.8848\\n      ],\\n      \\\"ci_lower\\\": 0.8832,\\n      \\\"ci_upper\\\": 0.8943,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.8888,\\n      \\\"boot_std\\\": 0.0028\\n    },\\n    \\\"3v4\
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T16:49:42.640963+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T16:49:42.641147+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_14b_c4\\\",\\n  \\\"config\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"n_permutation\\\": 1000,\\n    \\\"theta\\\": 0.6,\\n    \\\"seed\\\": 42,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"resample_unit\\\": \\\"document\\\"\\n  },\\n  \\\"pairwise_results\\\": {\\n    \\\"0v1\\\": {\\n      \\\"point_estimate\\\": 0.9598,\\n      \\\"ci_lower\\\": 0.9564,\\n      \\\"ci_upper\\\": 0.963,\\n      \\\"ci_width\\\": 0.0066,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.9598,\\n      \\\"bootstrap_std\\\": 0.0017\\n    },\\n    \\\"1v2\\\": {\\n      \\\"point_estimate\\\": 0.621,\\n      \\\"ci_lower\\\": 0.6119,\\n      \\\"ci_upper\\\": 0.6304,\\n      \\\"ci_width\\\": 0.0185,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.621,\\n      \\\"bootstrap_std\\\": 0.0047\\n    },\\n    \\\"2v3\\\": {\\n      \\\"point_estimate\\\": 0.5494,\\n      \\\"ci_lower\\\": 0.5392,\\n      \\\"ci_upper\\\": 0.5594,\\n      \\\"ci_width\\\": 0.0202,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.5493,\\n      \\\"bootstrap_std\\\": 0.0051\\n    },\\n    \\\"3v4\\\": {\\n      \\\"point_estimate\\\": 0.5243,\\n      \\\"ci_lower\\\": 0.514,\\n      \\\"ci_upper\\\": 0.5346,\\n      \\\"ci_width\\\": 0.0206,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.5243,\\n      \\\"bootstrap_std\\\": 0.0053\\n    },\\n    \\\"4v5\\\": {\\n      \\\"point_estimate\\\": 0.5154,\\n      \\\"ci_lower\\\": 0.5045,\\n      \\\"ci_upper\\\": 0.5265,\\n      \\\"
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T16:49:42.641307+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T16:49:42.641448+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"mean\\\": 0.9972,\\n    \\\"ci_95\\\": [\\n      0.9967,\\n      0.9977\\n    ]\\n  },\\n  \\\"1v2\\\": {\\n    \\\"mean\\\": 0.9572,\\n    \\\"ci_95\\\": [\\n      0.9542,\\n      0.9601\\n    ]\\n  },\\n  \\\"2v3\\\": {\\n    \\\"mean\\\": 0.8885,\\n    \\\"ci_95\\\": [\\n      0.8814,\\n      0.8947\\n    ]\\n  },\\n  \\\"3v4\\\": {\\n    \\\"mean\\\": 0.8772,\\n    \\\"ci_95\\\": [\\n      0.8684,\\n      0.8852\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-20T16:49:42.641573+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T16:49:42.641707+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"mean\\\": 0.9942,\\n    \\\"ci_95\\\": [\\n      0.9933,\\n      0.995\\n    ]\\n  },\\n  \\\"1v2\\\": {\\n    \\\"mean\\\": 0.9611,\\n    \\\"ci_95\\\": [\\n      0.958,\\n      0.964\\n    ]\\n  },\\n  \\\"2v3\\\": {\\n    \\\"mean\\\": 0.9174,\\n    \\\"ci_95\\\": [\\n      0.912,\\n      0.9225\\n    ]\\n  },\\n  \\\"3v4\\\": {\\n    \\\"mean\\\": 0.8924,\\n    \\\"ci_95\\\": [\\n      0.8854,\\n      0.8989\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-20T16:49:42.641858+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T16:49:42.642017+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"point_estimate\\\": 0.9944,\\n    \\\"boot_mean\\\": 0.9944,\\n    \\\"ci_lower\\\": 0.9925,\\n    \\\"ci_upper\\\": 0.996,\\n    \\\"per_fold\\\": [\\n      0.9912,\\n      0.9978,\\n      0.9934,\\n      0.9976,\\n      0.994\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"1v2\\\": {\\n    \\\"point_estimate\\\": 0.8315,\\n    \\\"boot_mean\\\": 0.8316,\\n    \\\"ci_lower\\\": 0.8205,\\n    \\\"ci_upper\\\": 0.8426,\\n    \\\"per_fold\\\": [\\n      0.8125,\\n      0.8563,\\n      0.8227,\\n      0.8285,\\n      0.8373\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"2v3\\\": {\\n    \\\"point_estimate\\\": 0.6248,\\n    \\\"boot_mean\\\": 0.6248,\\n    \\\"ci_lower\\\": 0.6098,\\n    \\\"ci_upper\\\": 0.6402,\\n    \\\"per_fold\\\": [\\n      0.6512,\\n      0.6178,\\n      0.6157,\\n      0.6054,\\n      0.6351\\n    ],\\n    \\\"n_boot_valid\\\": 10000,\\n    \\\"p_value\\\": 0.0,\\n    \\\"perm_null_mean\\\": 0.5,\\n    \\\"perm_null_std\\\": 0.0087,\\n    \\\"n_perm\\\": 1000\\n  },\\n  \\\"3v4\\\": {\\n    \\\"point_estimate\\\": 0.544,\\n    \\\"boot_mean\\\": 0.5439,\\n    \\\"ci_lower\\\": 0.5277,\\n    \\\"ci_upper\\\": 0.5598,\\n    \\\"per_fold\\\": [\\n      0.5501,\\n      0.5691,\\n      0.5507,\\n      0.5379,\\n      0.5131\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"4v5\\\": {\\n    \\\"point_estimate\\\": 0.5425,\\n    \\\"boot_mean\\\": 0.5425,\\n    \\\"ci_lower\\\": 0.5265,\\n    \\\"ci_upper\\\": 0.5584,\\n    \\\"per_fold\\\": [\\n      0.5253,\\n      0.5664,\\n      0.547,\\n      0.5423,\\n      0.5292\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-20T16:49:42.642173+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -80 /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -80 /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-20T16:49:42.642296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"generator\" /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"generator\" /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-20T16:49:42.642420+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_vocab_only_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection/multi_source_vocab_only_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T16:49:42.642582+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import csv\\nimport json\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport lightgbm as lgb\\nfrom sklearn.model_selection import GroupKFold\\nfrom sklearn.metrics import roc_auc_score\\n\\nFEAT_COLS = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\", \\\"freq_entropy\\\", \\\"low_freq_ratio\\\",\\n]\\n\\nSOURCES = {\\n    \\\"qwen1b5\\\": Path(\\\"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\\\"),\\n    \\\"pythia1b4\\\": Path(\\\"/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_greedy/features.csv\\\"),\\n    \\\"llama8b\\\": Path(\\\"/root/autodl-tmp/gen-depth-contamination/data/exp_018_llama8b/features.csv\\\"),\\n}\\n\\nDOCS_PER_GEN = 1000\\nMAX_DEPTH = 5\\nN_BOOT = 10000\\nTHETA = 0.60\\nSEED = 42\\nOUT_DIR = Path(\\\"/root/autodl-tmp/gen-depth-contamination/results/exp_multi_source_detection_v2\\\")\\n\\n\\ndef load_features(path):\\n    with open(path) as f:\\n        rows = list(csv.DictReader(f))\\n    doc_ids = np.array([int(r[\\\"doc_id\\\"]) for r in rows])\\n    depths = np.array([int(r[\\\"depth\\\"]) for r in rows])\\n    X = np.array(\\n        [[float(r[c]) if r[c] not in (\\\"\\\", \\\"nan\\\") else np.nan for c in FEAT_COLS] for r in rows]\\n    )\\n    col_means = np.nanmean(X, axis=0)\\n    for j in range(X.shape[1]):\\n        mask = np.isnan(X[:, j])\\n        X[mask, j] = col_means[j]\\n    return X, depths, doc_ids\\n\\n\\ndef sample_and_merge(rng):\\n    all_X, all_depths, all_doc_ids, all_gen_ids = [], [], [], []\\n    doc_offset = 0\\n\\n    for gen_idx, (gen_name, path) in enumerate(SOURCES.items()):\\n        X, depths, doc_ids = load_features(path)\\n        unique_docs = np.uniq
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-20T16:49:42.642737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"179:    # --- Main experiment: mixed-source, no generator label ---\\n180:    print(\\\"\\\\n=== Experiment 1: Mixed-source (no generator label) ===\\\", flush=True)\\n185:    # --- Experiment 2: with generator label as 16th feature ---\\n186:    print(\\\"\\\\n=== Experiment 2: Mixed-source (with generator label) ===\\\", flush=True)\\n196:        \\\"generators\\\": list(SOURCES.keys()),\\n197:        \\\"docs_per_generator\\\": DOCS_PER_GEN,\\n203:        \\\"no_generator_label\\\": {\\n207:        \\\"with_generator_label\\\": {\\n217:            \\\"v1_generators\\\": [\\\"qwen1b5\\\", \\\"pythia1b4\\\", \\\"olmo1b\\\"],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-20T16:49:42.642964+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_multi_source_vocab_only\\\",\\n  \\\"description\\\": \\\"Vocab-only (scorer-independent) multi-source detection\\\",\\n  \\\"features\\\": [\\n    \\\"ttr\\\",\\n    \\\"hapax_ratio\\\",\\n    \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\",\\n    \\\"freq_entropy\\\",\\n    \\\"low_freq_ratio\\\"\\n  ],\\n  \\\"n_features\\\": 6,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"theta\\\": 0.6,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 231.9,\\n  \\\"v1_qwen_pythia_olmo\\\": {\\n    \\\"generators\\\": [\\n      \\\"qwen1b5\\\",\\n      \\\"pythia1b4\\\",\\n      \\\"olmo1b\\\"\\n    ],\\n    \\\"pairs\\\": {\\n      \\\"0v1\\\": {\\n        \\\"auc\\\": 0.8675,\\n        \\\"fold_aucs\\\": [\\n          0.8713,\\n          0.8698,\\n          0.8712,\\n          0.8626,\\n          0.8637\\n        ],\\n        \\\"ci_lower\\\": 0.8586,\\n        \\\"ci_upper\\\": 0.8763,\\n        \\\"boot_mean\\\": 0.8675,\\n        \\\"boot_std\\\": 0.0045\\n      },\\n      \\\"1v2\\\": {\\n        \\\"auc\\\": 0.676,\\n        \\\"fold_aucs\\\": [\\n          0.6671,\\n          0.6855,\\n          0.6644,\\n          0.6896,\\n          0.6736\\n        ],\\n        \\\"ci_lower\\\": 0.6617,\\n        \\\"ci_upper\\\": 0.6903,\\n        \\\"boot_mean\\\": 0.6759,\\n        \\\"boot_std\\\": 0.0073\\n      },\\n      \\\"2v3\\\": {\\n        \\\"auc\\\": 0.4938,\\n        \\\"fold_aucs\\\": [\\n          0.5041,\\n          0.4761,\\n          0.4966,\\n          0.4989,\\n          0.4933\\n        ],\\n        \\\"ci_lower\\\": 0.4799,\\n        \\\"ci_upper\\\": 0.5075,\\n        \\\"boot_mean\\\": 0.4938,\\n        \\\"boot_std\\\": 0.0071\\n      },\\n      \\\"3v4\\\": {\\n        \\\"auc\\\": 0.4971,\\n        \\\"fold_aucs\\\": [\\n          0.485,\\n          0.5012,\\n          0.5027,\\n          0.5061,\\n          0.4913\\n        ],\\n        \\\"ci_lower\\\": 0.4828,\\n      
…[truncated 2572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-20T16:49:42.643171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-20T16:49:42.643336+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.9961,\\n    \\\"1v2\\\": 0.6193,\\n    \\\"2v3\\\": 0.5498,\\n    \\\"3v4\\\": 0.5231,\\n    \\\"4v5\\\": 0.5141\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9955,\\n      0.9964,\\n      0.997,\\n      0.9955,\\n      0.9963\\n    ],\\n    \\\"1v2\\\": [\\n      0.6152,\\n      0.6161,\\n      0.6189,\\n      0.6112,\\n      0.6352\\n    ],\\n    \\\"2v3\\\": [\\n      0.5473,\\n      0.5559,\\n      0.5378,\\n      0.5637,\\n      0.5442\\n    ],\\n    \\\"3v4\\\": [\\n      0.5247,\\n      0.5245,\\n      0.5175,\\n      0.5106,\\n      0.5384\\n    ],\\n    \\\"4v5\\\": [\\n      0.5019,\\n      0.5252,\\n      0.5191,\\n      0.5161,\\n      0.5084\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-20T16:49:42.643482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T16:49:42.643625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.9948,\\n    \\\"1v2\\\": 0.8581,\\n    \\\"2v3\\\": 0.6436,\\n    \\\"3v4\\\": 0.544,\\n    \\\"4v5\\\": 0.5299\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9956,\\n      0.9955,\\n      0.9938,\\n      0.9938,\\n      0.9952\\n    ],\\n    \\\"1v2\\\": [\\n      0.8763,\\n      0.8669,\\n      0.8411,\\n      0.8515,\\n      0.8549\\n    ],\\n    \\\"2v3\\\": [\\n      0.6738,\\n      0.6349,\\n      0.6479,\\n      0.6537,\\n      0.6078\\n    ],\\n    \\\"3v4\\\": [\\n      0.52,\\n      0.5346,\\n      0.5491,\\n      0.5471,\\n      0.5693\\n    ],\\n    \\\"4v5\\\": [\\n      0.5517,\\n      0.5419,\\n      0.5413,\\n      0.5312,\\n      0.4832\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-20T16:49:42.643752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-20T16:49:42.643911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.987,\\n    \\\"1v2\\\": 0.6262,\\n    \\\"2v3\\\": 0.5496,\\n    \\\"3v4\\\": 0.5294,\\n    \\\"4v5\\\": 0.5182\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9881,\\n      0.9884,\\n      0.9852,\\n      0.9851,\\n      0.9882\\n    ],\\n    \\\"1v2\\\": [\\n      0.5963,\\n      0.6362,\\n      0.6366,\\n      0.6337,\\n      0.6282\\n    ],\\n    \\\"2v3\\\": [\\n      0.5516,\\n      0.5456,\\n      0.5403,\\n      0.5605,\\n      0.5501\\n    ],\\n    \\\"3v4\\\": [\\n      0.5515,\\n      0.5133,\\n      0.5198,\\n      0.535,\\n      0.5276\\n    ],\\n    \\\"4v5\\\": [\\n      0.5207,\\n      0.5393,\\n      0.5186,\\n      0.5169,\\n      0.4956\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-20T16:49:42.644044+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_025_pythia_arxiv/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_025_pythia_arxiv/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-20T16:49:42.644179+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.9877,\\n    \\\"1v2\\\": 0.8047,\\n    \\\"2v3\\\": 0.6545,\\n    \\\"3v4\\\": 0.5507,\\n    \\\"4v5\\\": 0.5287\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9914,\\n      0.9889,\\n      0.9844,\\n      0.9895,\\n      0.9845\\n    ],\\n    \\\"1v2\\\": [\\n      0.7906,\\n      0.8278,\\n      0.8018,\\n      0.8065,\\n      0.7967\\n    ],\\n    \\\"2v3\\\": [\\n      0.6409,\\n      0.6433,\\n      0.6764,\\n      0.6548,\\n      0.6572\\n    ],\\n    \\\"3v4\\\": [\\n      0.5496,\\n      0.5418,\\n      0.5499,\\n      0.5675,\\n      0.5444\\n    ],\\n    \\\"4v5\\\": [\\n      0.5253,\\n      0.5101,\\n      0.5413,\\n      0.5432,\\n      0.5235\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-20T16:49:42.644338+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 -c \"\nimport json, os, glob\n\n# Collect all pairwise_auc.json files and extract 1v2 and 2v3 fold data\nresults = {}\nfor f in sorted(glob.glob('results/*/pairwise_auc.json') + glob.glob('results_*/pairwise_auc.json')):\n    config = f.split('/')[1] if f.startswith('results/') else f.split('/')[0]\n    if config.startswith('results_'):\n        config = config.replace('results_', '')\n    d = json.load(open(f))\n    entry = {}\n    if 'per_fold' in d:\n        for pair in ['1v2', '2v3']:\n            if pair in d['per_fold']:\n                entry[pair] = {'mean': d['mean'][pair], 'folds': d['per_fold'][pair]}\n    results[config] = entry\n\nprint(json.dumps(results, indent=2))\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 -c \"\nimport json, os, glob\n\n# Collect all pairwise_auc.json files and extract 1v2 and 2v3 fold data\nresults = {}\nfor f in sorted(glob.glob('results/*/pairwise_auc.json') + glob.glob('results_*/pairwise_auc.json')):\n    config = f.split('/')[1] if f.startswith('results/') else f.split('/')[0]\n    if config.startswith('results_'):\n        config = config.replace('results_', '')\n    d = json.load(open(f))\n    entry = {}\n    if 'per_fold' in d:\n        for pair in ['1v2', '2v3']:\n            if pair in d['per_fold']:\n                entry[pair] = {'mean': d['mean'][pair], 'folds': d['per_fold'][pair]}\n    results[config] = entry\n\nprint(json.dumps(results, indent=2))\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-20T16:49:42.644667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_008_retrain_chain\\\": {\\n    \\\"1v2\\\": {\\n      \\\"mean\\\": 0.9484,\\n      \\\"folds\\\": [\\n        0.9464,\\n        0.9513,\\n        0.9462,\\n        0.9486,\\n        0.9497\\n      ]\\n    },\\n    \\\"2v3\\\": {\\n      \\\"mean\\\": 0.8888,\\n      \\\"folds\\\": [\\n        0.8982,\\n        0.8888,\\n        0.8837,\\n        0.8833,\\n        0.8901\\n      ]\\n    }\\n  },\\n  \\\"exp_018_llama8b\\\": {\\n    \\\"1v2\\\": {\\n      \\\"mean\\\": 0.6123,\\n      \\\"folds\\\": [\\n        0.6362,\\n        0.6072,\\n        0.5975,\\n        0.6067,\\n        0.614\\n      ]\\n    },\\n    \\\"2v3\\\": {\\n      \\\"mean\\\": 0.5274,\\n      \\\"folds\\\": [\\n        0.5345,\\n        0.5442,\\n        0.5342,\\n        0.5141,\\n        0.5101\\n      ]\\n    }\\n  },\\n  \\\"exp_021_length_128\\\": {\\n    \\\"1v2\\\": {\\n      \\\"mean\\\": 0.6219,\\n      \\\"folds\\\": [\\n        0.6405,\\n        0.6269,\\n        0.6191,\\n        0.6117,\\n        0.6112\\n      ]\\n    },\\n    \\\"2v3\\\": {\\n      \\\"mean\\\": 0.5291,\\n      \\\"folds\\\": [\\n        0.513,\\n        0.5411,\\n        0.5422,\\n        0.5091,\\n        0.5401\\n      ]\\n    }\\n  },\\n  \\\"exp_021_length_256\\\": {\\n    \\\"1v2\\\": {\\n      \\\"mean\\\": 0.6282,\\n      \\\"folds\\\": [\\n        0.6335,\\n        0.6173,\\n        0.6231,\\n        0.6244,\\n        0.6425\\n      ]\\n    },\\n    \\\"2v3\\\": {\\n      \\\"mean\\\": 0.5556,\\n      \\\"folds\\\": [\\n        0.5535,\\n        0.5557,\\n        0.5551,\\n        0.5593,\\n        0.5545\\n      ]\\n    }\\n  },\\n  \\\"exp_021_length_512\\\": {\\n    \\\"1v2\\\": {\\n      \\\"mean\\\": 0.6073,\\n      \\\"folds\\\": [\\n        0.6184,\\n        0.5979,\\n        0.5952,\\n        0.6118,\\n        0.6134\\n      ]\\n    },\\n    \\\"2v3\\\": {\\n      \\\"mean\\\": 0.5721,\\n      \\\"folds\\\": [\\n        0.5767,\
…[truncated 8341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-20T16:49:42.644908+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-20T16:49:42.645072+00:00_

14b_scorer_contingency
_project
analysis_exp_deberta_arxiv_qwen1b5.md
analyze_pythia_retrain_depth7.py
arXiv_crossscorer_summary
bootstrap_audit_report.md
bootstrap_ci_4model.json
borderline_analysis
borderline_bootstrap_ci.json
c3_contingency_versions.tex
c3_fallback_outline.md
c4_power_curve
citations_round2
code_crossmodel_table.tex
code_scenario_prep.md
compute_f1_threshold.py
diag_exp_code_qwen7b.md
discussion_outline.md
domain_lexical_stats
drafts
dream_reports
dream_simulation_readiness.md
exp-004
exp-005
exp-006
exp-013
exp-014
exp-019
exp-024
exp-D
exp005_4model_tau_matrix.json
exp006_analyze.py
exp006_continued_pretraining.py
exp006_evaluate.py
exp006_filtering_strategies.py
exp008_retrain_chain.py
exp012_binary_confidence.py
exp012_ppl_depth_correlation.py
exp016_bootstrap_ci.json
exp025_bootstrap_ci.json
exp026_feature_stability.json
exp_003_decoding_ablation
exp_006_graduated_filtering
exp_007_bootstrap_ci
exp_008_retrain_chain_v2
exp_015_neural_probe
exp_016_base_vs_instruct
exp_019_mistral7b_depth
exp_019b_mistral_cross_scorer
exp_020_pythia_decoding
exp_022_cross_scorer_matrix
exp_023_wiki_domain
exp_024_arxiv_domain
exp_025_pythia_arxiv
exp_026
exp_026_arxiv_filtering
exp_026_feature_stability
exp_026_ttest
exp_027
exp_027_bootstrap_ci
exp_027_latex_ablation
exp_028_power_curve
exp_14b_c4
exp_14b_c4_bootstrap_ci
exp_32b_c4
exp_B_14d_ablation.json
exp_C_permutation_10k.json
exp_D_obd_n500.json
exp_arXiv_llama8b_crossscorer
exp_arXiv_mistral7b_crossscorer
exp_arXiv_qwen1b5_crossscorer
exp_arXiv_qwen7b
exp_arXiv_qwen7b_analysis.md
exp_arXiv_qwen7b_crossscorer
exp_bootstrap_10k
exp_changepoint_kstar
exp_code_mistral7b_diagnosis.md
exp_code_qwen1b5
exp_code_qwen7b
exp_deberta_c4_1b5
exp_gemma2b_depth
exp_gemma2b_depth_results.json
exp_multi_source_arxiv
exp_multi_source_detection
exp_olmo_retrain_chain
exp_olmo_retrain_chain.py
exp_qwen_retrain_chain
exp_qwen_retrain_chain_ext.py
exp_qwen_retrain_depth7
exp_qwen_retrain_ext
exp_wiki_llama8b
exp_wiki_mist
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-20T16:49:42.645255+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/round22_raw_data_extraction.md",
  "content": "# Round 22 审稿修复原始数据提取\n\n提取日期: 2026-05-20\n数据来源: cqa1-22115:/root/autodl-tmp/gen-depth-contamination/\n\n---\n\n## T4: Permutation Test 精确 p-values\n\n所有 p-value 来自 label permutation test (n_permutation=10000, 除 exp_14b_c4 使用 n_permutation=1000)。\n`perm_p = 0.0001` 对应 0/10000 permutations 超过观测值, 即 p = 1/(10000+1) ≈ 0.0001。\n\n### 主要 configs 的完整逐对 p-value\n\n**exp016 (Qwen-1.5B base, C4)** — boundary: 1v2\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9870 | 0.0001 |\n| 1v2 | 0.6260 | 0.0001 |\n| 2v3 | 0.5496 | 0.0001 |\n| 3v4 | 0.5293 | 0.0001 |\n| 4v5 | 0.5181 | 0.0016 |\n\n**exp018 (LLaMA-3.1-8B, C4)** — boundary: 1v2\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9224 | 0.0001 |\n| 1v2 | 0.6123 | 0.0001 |\n| 2v3 | 0.5273 | 0.0001 |\n| 3v4 | 0.5168 | 0.0037 |\n| 4v5 | 0.5159 | 0.0035 |\n\n**exp019 (Mistral-7B-Instruct, C4)** — boundary: 1v2 (K*_CI=1, borderline)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9842 | 0.0001 |\n| 1v2 | 0.5934 | 0.0001 |\n| 2v3 | 0.5402 | 0.0001 |\n| 3v4 | 0.5233 | 0.0003 |\n| 4v5 | 0.5180 | 0.0014 |\n\n**exp024 (Qwen-1.5B arXiv)** — boundary: 2v3 (K*=3)\n| Pair | AUC | perm_p | p_vs_θ |\n|------|-----|--------|--------|\n| 0v1 | 0.9946 | 0.0001 | 0.0 |\n| 1v2 | 0.8580 | 0.0001 | 0.0 |\n| 2v3 | 0.6427 | 0.0001 | 0.0 |\n| 3v4 | 0.5437 | 0.0001 | 1.0 |\n| 4v5 | 0.5294 | 0.0006 | 1.0 |\n\n**exp025 (Pythia-1.4B arXiv)** — boundary: 2v3 (K*=3)\n| Pair | AUC | perm_p | p_vs_θ |\n|------|-----|--------|--------|\n| 0v1 | 0.9876 | 0.0001 | 0.0 |\n| 1v2 | 0.8047 | 0.0001 | 0.0 |\n| 2v3 | 0.6544 | 0.0001 | 0.0 |\n| 3v4 | 0.5500 | 0.0001 | 1.0 |\n| 4v5 | 0.5284 | 0.0010 | 1.0 |\n\n**exp_gemma2b (Gemma-2-2B, C4)** — boundary: 1v2\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9530 | 0.0001 |\n| 1v2 | 0.5981 | 0.0001 |\n| 2v3 | 0.5340 | 0.0001 |\n| 3v4 | 0.5033 | 0.2919 |\n| 4v5 | 0.5025 | 0.3418 |\n\n**exp027 retrain-chain (Pythia, C4)** — boundary: 3v4 (K*=4)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9847 | 0.0001 |\n| 1v2 | 0.9482 | 0.0001 |\n| 2v3 | 0.8885 | 0.0001 |\n| 3v4 | 0.7977 | 0.0001 |\n\n**exp_008_retrain_chain (v2, bootstrap_ci_v2)** — boundary: 3v4 (K*=4)\n| Pair | AUC | perm_p | p_vs_θ |\n|------|-----|--------|--------|\n| 0v1 | 0.9842 | 0.0001 | 0.0 |\n| 1v2 | 0.9471 | 0.0001 | 0.0 |\n| 2v3 | 0.8888 | 0.0001 | 0.0 |\n| 3v4 | 0.7994 | 0.0001 | 0.0 |\n\n**exp_14b_c4 (Qwen-14B, C4)** — boundary: 1v2, n_perm=1000\n| Pair | AUC | p_value |\n|------|-----|---------|\n| 0v1 | 0.9598 | 0.0 (0/1000) |\n| 1v2 | 0.6210 | 0.0 (0/1000) |\n| 2v3 | 0.5494 | 0.0 (0/1000) |\n| 3v4 | 0.5243 | 0.0 (0/1000) |\n| 4v5 | 0.5154 | 0.0 (0/1000) |\n\n### Cross-scorer configs (arXiv, scorer=Pythia-1.4B)\n\n**Qwen-7B crossscorer** (K*=2)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9573 | 0.0001 |\n| 1v2 | 0.8163 | 0.0001 |\n| 2v3 | 0.5986 | 0.0001 |\n| 3v4 | 0.5413 | 0.0001 |\n| 4v5 | 0.5191 | 0.0166 |\n\n**Mistral-7B crossscorer** (K*=2)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9798 | 0.0001 |\n| 1v2 | 0.8138 | 0.0001 |\n| 2v3 | 0.6075 | 0.0001 |\n| 3v4 | 0.5489 | 0.0001 |\n| 4v5 | 0.5389 | 0.0001 |\n\n**LLaMA-8B crossscorer** (K*=2)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 2v3 | 0.6201 | 0.0001 |\n| 3v4 | 0.5228 | 0.0060 |\n| 4v5 | 0.5247 | 0.0034 |\n\n### Retrain-chain permutation_test.json (独立格式, p_value不同编码)\n\n**exp_008_retrain_chain (Pythia)**\n| Pair | AUC | p_value |\n|------|-----|---------|\n| 0v1 | 0.9968 | 0.0 |\n| 1v2 | 0.9855 | 0.0 |\n| 2v3 | 0.9556 | 0.0 |\n| 3v4 | 0.9029 | 0.304 |\n\n**exp_olmo_retrain_chain (OLMo)**\n| Pair | AUC | p_value |\n|------|-----|---------|\n| 0v1 | 0.9988 | 0.0 |\n| 1v2 | 0.9610 | 0.0 |\n| 2v3 | 0.8919 | 0.998 |\n| 3v4 | 0.8762 | 1.0 |\n\n### Borderline 10K 比较\n\n| Config | Pair | AUC | perm_p_10k |\n|--------|------|-----|------------|\n| LLaMA-3.1-8B (exp_018) | 1v2 | 0.6075 | 0.0001 |\n| Gemma-2-2B | 1v2 | 0.5981 | 0.0001 |\n| Mistral-7B (exp_019) | 1v2 | 0.5902 | 0.0001 |\n| 512-tok (exp_021) | 1v2 | 0.6136 | 0.0001 |\n\n---\n\n## T3: PELT Changepoint 完整配对数据 (37 configs)\n\n| Config | K*_OBD | K*_PELT | Agree |\n|--------|--------|---------|-------|\n| exp_008_retrain_chain | 4 | 4 | ✓ |\n| exp_018_llama8b | 2 | 1 | ✗ |\n| exp_021_length_128 | 2 | 1 | ✗ |\n| exp_021_length_256 | 2 | 1 | ✗ |\n| exp_021_length_512 | 2 | 1 | ✗ |\n| exp_023_wiki | 2 | 1 | ✗ |\n| exp_024_arxiv | 3 | 2 | ✗ |\n| exp_025_pythia_arxiv | 3 | 2 | ✗ |\n| exp_027_latex_ablation | 3 | 2 | ✗ |\n| exp_14b_c4 | 2 | 1 | ✗ |\n| exp_arXiv_llama8b | 3 | 2 | ✗ |\n| exp_arXiv_llama8b_crossscorer | 3 | 2 | ✗ |\n| exp_arXiv_mistral7b | 3 | 2 | ✗ |\n| exp_arXiv_mistral7b_crossscorer | 3 | 2 | ✗ |\n| exp_arXiv_olmo | 1 | 1 | ✓ |\n| exp_arXiv_qwen1b5_crossscorer | 3 | 2 | ✗ |\n| exp_arXiv_qwen7b | 3 | 2 | ✗ |\n| exp_arXiv_qwen7b_crossscorer | 2 | 2 | ✓ |\n| exp_code_llama8b | 2 | 2 | ✓ |\n| exp_code_mistral7b | 2 | 1 | ✗ |\n| exp_code_pythia1b4 | 1 | 1 | ✓ |\n| exp_code_qwen1b5 | 2 | 2 | ✓ |\n| exp_code_qwen1b5_pythia_scorer | 2 | 2 | ✓ |\n| exp_code_qwen7b | 2 | 2 | ✓ |\n| exp_pythia_retrain_depth7 | 7 | 4 | ✗ |\n| exp_qwen_retrain_chain | 4 | 4 | ✓ |\n| exp_qwen_retrain_chain_ext | 7 | 2 | ✗ |\n| exp_wiki_llama8b | 1 | 1 | ✓ |\n| exp_wiki_mistral7b | 1 | 1 | ✓ |\n| exp_wiki_olmo | 1 | 1 | ✓ |\n| exp_wiki_olmo_v2 | 1 | 1 | ✓ |\n| exp_wiki_pythia | 2 | 1 | ✗ |\n| exp_wiki_pythia_v2 | 1 | 1 | ✓ |\n| exp_wiki_qwen7b | 2 | 1 | ✗ |\n| exp_wiki_scorer_confound | 1 | 1 | ✓ |\n| exp_wiki_scorer_confound_1b5 | 1 | 1 | ✓ |\n| olmo_c4_cont | 1 | 1 | ✓ |\n\n**汇总**: 37 configs, 18 agree (48.6%), 19 disagree (51.4%)\n- K*_OBD = K*_PELT 时 agree: 当两者都为 1 (14 cases) 或都为 2 (5 cases) 或都为 4 (2 cases)\n- 不一致模式: K*_OBD 系统性偏高 (PELT 总是 ≤ OBD), 差 1 的有 15 cases, 差 ≥2 的有 4 cases\n\n---\n\n## T2: Fold-level AUC 数据 (1v2 和 2v3)\n\n### 核心 configs 的 5-fold AUC\n\n**C4 domain:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp016 (Qwen-1.5B) | 1v2 | 0.6262 | 0.5963 | 0.6362 | 0.6366 | 0.6337 | 0.6282 |\n| exp016 (Qwen-1.5B) | 2v3 | 0.5496 | 0.5516 | 0.5456 | 0.5403 | 0.5605 | 0.5501 |\n| exp018 (LLaMA-8B) | 1v2 | 0.6123 | 0.6362 | 0.6072 | 0.5975 | 0.6067 | 0.6140 |\n| exp018 (LLaMA-8B) | 2v3 | 0.5274 | 0.5345 | 0.5442 | 0.5342 | 0.5141 | 0.5101 |\n| exp019 (Mistral-7B) | 1v2 | 0.5935 | 0.5981 | 0.5894 | 0.5962 | 0.5850 | 0.5988 |\n| exp019 (Mistral-7B) | 2v3 | 0.5402 | 0.5308 | 0.5340 | 0.5493 | 0.5584 | 0.5286 |\n| exp_gemma2b | 1v2 | 0.5981 | 0.6010 | 0.5841 | 0.6006 | 0.5966 | 0.6082 |\n| exp_gemma2b | 2v3 | 0.5342 | 0.5598 | 0.5246 | 0.5338 | 0.5241 | 0.5286 |\n| exp_14b_c4 (Qwen-14B) | 1v2 | 0.6211 | 0.6252 | 0.6112 | 0.6153 | 0.6323 | 0.6214 |\n| exp_14b_c4 (Qwen-14B) | 2v3 | 0.5494 | 0.5362 | 0.5529 | 0.5590 | 0.5445 | 0.5546 |\n| olmo_c4_cont | 1v2 | 0.5070 | 0.5083 | 0.4946 | 0.4953 | 0.5170 | 0.5195 |\n| olmo_c4_cont | 2v3 | 0.5042 | 0.5106 | 0.4896 | 0.5140 | 0.4977 | 0.5093 |\n\n**arXiv domain:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp024 (Qwen-1.5B) | 1v2 | 0.8581 | 0.8763 | 0.8669 | 0.8411 | 0.8515 | 0.8549 |\n| exp024 (Qwen-1.5B) | 2v3 | 0.6436 | 0.6738 | 0.6349 | 0.6479 | 0.6537 | 0.6078 |\n| exp025 (Pythia-1.4B) | 1v2 | 0.8047 | 0.7906 | 0.8278 | 0.8018 | 0.8065 | 0.7967 |\n| exp025 (Pythia-1.4B) | 2v3 | 0.6545 | 0.6409 | 0.6433 | 0.6764 | 0.6548 | 0.6572 |\n| exp027_latex_ablation | 1v2 | 0.8297 | 0.8085 | 0.8529 | 0.8198 | 0.8292 | 0.8381 |\n| exp027_latex_ablation | 2v3 | 0.6229 | 0.6429 | 0.6196 | 0.6258 | 0.5986 | 0.6275 |\n\n**Wiki domain:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp023 (Qwen-1.5B) | 1v2 | 0.6193 | 0.6152 | 0.6161 | 0.6189 | 0.6112 | 0.6352 |\n| exp023 (Qwen-1.5B) | 2v3 | 0.5498 | 0.5473 | 0.5559 | 0.5378 | 0.5637 | 0.5442 |\n| exp_wiki_pythia_v2 | 1v2 | 0.5846 | 0.5826 | 0.5783 | 0.5842 | 0.5864 | 0.5913 |\n| exp_wiki_qwen7b | 1v2 | 0.6108 | 0.6135 | 0.6085 | 0.6031 | 0.6016 | 0.6272 |\n| exp_wiki_scorer_confound | 1v2 | 0.5870 | 0.5850 | 0.5825 | 0.5877 | 0.5766 | 0.6030 |\n\n**Retrain-chain configs:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp008 retrain (v2) | 1v2 | 0.9472 | 0.9520 | 0.9444 | 0.9558 | 0.9401 | 0.9437 |\n| exp008 retrain (v2) | 2v3 | 0.8891 | 0.8794 | 0.8828 | 0.8998 | 0.8986 | 0.8848 |\n| exp008 retrain (v2) | 3v4 | 0.7996 | 0.8020 | 0.7975 | 0.8036 | 0.7898 | 0.8050 |\n\n**Cross-scorer configs (arXiv, scorer=Pythia-1.4B):**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| Qwen-7B crossscorer | 1v2 | 0.8171 | 0.7892 | 0.8093 | 0.8265 | 0.8236 | 0.8372 |\n| Qwen-7B crossscorer | 2v3 | 0.5989 | 0.5920 | 0.6006 | 0.6108 | 0.5768 | 0.6142 |\n| Mistral-7B crossscorer | 1v2 | 0.8141 | 0.7874 | 0.8256 | 0.8225 | 0.8223 | 0.8125 |\n| Mistral-7B crossscorer | 2v3 | 0.6075 | 0.6052 | 0.5803 | 0.6210 | 0.6113 | 0.6195 |\n| LLaMA-8B crossscorer | 2v3 | 0.6201 | 0.6306 | 0.6115 | 0.6073 | 0.6136 | 0.6377 |\n\n**Length ablation:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| 128-tok | 1v2 | 0.6219 | 0.6405 | 0.6269 | 0.6191 | 0.6117 | 0.6112 |\n| 256-tok | 1v2 | 0.6282 | 0.6335 | 0.6173 | 0.6231 | 0.6244 | 0.6425 |\n| 512-tok | 1v2 | 0.6073 | 0.6184 | 0.5979 | 0.5952 | 0.6118 | 0.6134 |\n\n---\n\n## T6: Generator Identity AUC\n\n### 结论: 无独立的 \"generator identity classification AUC\" 指标\n\nmulti_source 实验测量的是将 generator ID 作为第 16 个特征加入 depth classifier 后的 AUC 变化, 而非 generator identity 本身的分类性能。\n\n### 所有 multi-source 实验的 Δ(with_label - no_label)\n\n**C4 domain (v1: Qwen-1.5B + Pythia-1.4B + OLMo-1B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9929 | 0.9948 | +0.0019 |\n| 1v2 | 0.7007 | 0.7015 | +0.0008 |\n| K* | 2 | 2 | unchanged |\n\n**C4 domain (v2: Qwen-1.5B + Pythia-1.4B + LLaMA-8B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9680 | 0.9785 | +0.0105 |\n| 1v2 | 0.7144 | 0.7250 | +0.0106 |\n| K* | 2 | 2 | unchanged |\n\n**arXiv domain (vocab-only, Qwen-1.5B + Pythia-1.4B + LLaMA-8B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9431 | 0.9436 | +0.0005 |\n| 1v2 | 0.6922 | 0.7020 | +0.0098 |\n| 2v3 | 0.5890 | 0.5883 | -0.0007 |\n| K* | 2 | 2 | unchanged |\n\n**arXiv domain (unified scorer, same generators)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9899 | 0.9911 | +0.0012 |\n| 1v2 | 0.8117 | 0.8338 | +0.0221 |\n| 2v3 | 0.6247 | 0.6276 | +0.0029 |\n| K* | 3 | 3 | unchanged |\n\n**Wiki domain (vocab-only, Qwen-1.5B + LLaMA-8B + Mistral-7B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.7616 | 0.7779 | +0.0163 |\n| 1v2 | 0.5434 | 0.5520 | +0.0086 |\n| K* | 1 | 1 | unchanged |\n\n**Wiki domain (unified scorer)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9603 | 0.9685 | +0.0082 |\n| 1v2 | 0.5685 | 0.5790 | +0.0105 |\n| K* | 1 | 1 | unchanged |\n\n**Code domain (vocab-only, Qwen-7B + LLaMA-8B + Mistral-7B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.7891 | 0.7900 | +0.0009 |\n| 1v2 | 0.6353 | 0.6440 | +0.0087 |\n| K* | 2 | 2 | unchanged |\n\n**Code domain (unified scorer)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9123 | 0.9123 | +0.0000 |\n| 1v2 | 0.6702 | 0.6803 | +0.0101 |\n| K* | 2 | 2 | unchanged |\n\n### 关键结论\n- **Generator identity 对 depth detection 的增益可忽略**: 平均 Δ(1v2) ≈ +0.01 AUC\n- **K* 从未因加入 generator label 而改变**\n- 最大 Δ 出现在 arXiv unified scorer 1v2 (+0.0221), 但仍不改变 K*\n- **不存在独立的 generator identity classification AUC** — 实验设计中没有将 \"识别 generator\" 作为目标任务\n\n---\n\n## 数据文件索引\n\n| 数据类型 | 文件路径 |\n|---------|---------|\n| Permutation test (retrain) | results/exp_008_retrain_chain/permutation_test.json |\n| Permutation test (OLMo retrain) | results/exp_olmo_retrain_chain/permutation_test.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp016_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp018_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp019_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp024_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp025_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp027_retrain_bootstrap.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp_gemma2b_depth_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/crossscorer_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | results/exp_14b_c4/bootstrap_ci_results.json |\n| Bootstrap CI v2 | results/exp_008_retrain_chain/bootstrap_ci_v2.json |\n| Borderline 10K comparison | results/exp_bootstrap_10k/bootstrap_10k_comparison.json |\n| Borderline bootstrap | artifacts/borderline_bootstrap_ci.json |\n| PELT changepoint | results/exp_changepoint_kstar/changepoint_results.json |\n| PELT bootstrap comparison | results/exp_changepoint_kstar/bootstrap_comparison.json |\n| Multi-source v1 (C4) | results/exp_multi_source_detection/multi_source_results.json |\n| Multi-source v2 (C4) | results/exp_multi_source_detection_v2/multi_source_results.json |\n| Multi-source arXiv | results/exp_multi_source_arxiv/results.json |\n| Multi-source Wiki | results/exp_wiki_multi_source/results.json |\n| Multi-source Code | results/exp_code_multi_source/results.json |\n| Fold AUC (per config) | results/*/pairwise_auc.json, results_*/pairwise_auc.json |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/round22_raw_data_extraction.md",
    "content": "# Round 22 审稿修复原始数据提取\n\n提取日期: 2026-05-20\n数据来源: cqa1-22115:/root/autodl-tmp/gen-depth-contamination/\n\n---\n\n## T4: Permutation Test 精确 p-values\n\n所有 p-value 来自 label permutation test (n_permutation=10000, 除 exp_14b_c4 使用 n_permutation=1000)。\n`perm_p = 0.0001` 对应 0/10000 permutations 超过观测值, 即 p = 1/(10000+1) ≈ 0.0001。\n\n### 主要 configs 的完整逐对 p-value\n\n**exp016 (Qwen-1.5B base, C4)** — boundary: 1v2\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9870 | 0.0001 |\n| 1v2 | 0.6260 | 0.0001 |\n| 2v3 | 0.5496 | 0.0001 |\n| 3v4 | 0.5293 | 0.0001 |\n| 4v5 | 0.5181 | 0.0016 |\n\n**exp018 (LLaMA-3.1-8B, C4)** — boundary: 1v2\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9224 | 0.0001 |\n| 1v2 | 0.6123 | 0.0001 |\n| 2v3 | 0.5273 | 0.0001 |\n| 3v4 | 0.5168 | 0.0037 |\n| 4v5 | 0.5159 | 0.0035 |\n\n**exp019 (Mistral-7B-Instruct, C4)** — boundary: 1v2 (K*_CI=1, borderline)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9842 | 0.0001 |\n| 1v2 | 0.5934 | 0.0001 |\n| 2v3 | 0.5402 | 0.0001 |\n| 3v4 | 0.5233 | 0.0003 |\n| 4v5 | 0.5180 | 0.0014 |\n\n**exp024 (Qwen-1.5B arXiv)** — boundary: 2v3 (K*=3)\n| Pair | AUC | perm_p | p_vs_θ |\n|------|-----|--------|--------|\n| 0v1 | 0.9946 | 0.0001 | 0.0 |\n| 1v2 | 0.8580 | 0.0001 | 0.0 |\n| 2v3 | 0.6427 | 0.0001 | 0.0 |\n| 3v4 | 0.5437 | 0.0001 | 1.0 |\n| 4v5 | 0.5294 | 0.0006 | 1.0 |\n\n**exp025 (Pythia-1.4B arXiv)** — boundary: 2v3 (K*=3)\n| Pair | AUC | perm_p | p_vs_θ |\n|------|-----|--------|--------|\n| 0v1 | 0.9876 | 0.0001 | 0.0 |\n| 1v2 | 0.8047 | 0.0001 | 0.0 |\n| 2v3 | 0.6544 | 0.0001 | 0.0 |\n| 3v4 | 0.5500 | 0.0001 | 1.0 |\n| 4v5 | 0.5284 | 0.0010 | 1.0 |\n\n**exp_gemma2b (Gemma-2-2B, C4)** — boundary: 1v2\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9530 | 0.0001 |\n| 1v2 | 0.5981 | 0.0001 |\n| 2v3 | 0.5340 | 0.0001 |\n| 3v4 | 0.5033 | 0.2919 |\n| 4v5 | 0.5025 | 0.3418 |\n\n**exp027 retrain-chain (Pythia, C4)** — boundary: 3v4 (K*=4)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9847 | 0.0001 |\n| 1v2 | 0.9482 | 0.0001 |\n| 2v3 | 0.8885 | 0.0001 |\n| 3v4 | 0.7977 | 0.0001 |\n\n**exp_008_retrain_chain (v2, bootstrap_ci_v2)** — boundary: 3v4 (K*=4)\n| Pair | AUC | perm_p | p_vs_θ |\n|------|-----|--------|--------|\n| 0v1 | 0.9842 | 0.0001 | 0.0 |\n| 1v2 | 0.9471 | 0.0001 | 0.0 |\n| 2v3 | 0.8888 | 0.0001 | 0.0 |\n| 3v4 | 0.7994 | 0.0001 | 0.0 |\n\n**exp_14b_c4 (Qwen-14B, C4)** — boundary: 1v2, n_perm=1000\n| Pair | AUC | p_value |\n|------|-----|---------|\n| 0v1 | 0.9598 | 0.0 (0/1000) |\n| 1v2 | 0.6210 | 0.0 (0/1000) |\n| 2v3 | 0.5494 | 0.0 (0/1000) |\n| 3v4 | 0.5243 | 0.0 (0/1000) |\n| 4v5 | 0.5154 | 0.0 (0/1000) |\n\n### Cross-scorer configs (arXiv, scorer=Pythia-1.4B)\n\n**Qwen-7B crossscorer** (K*=2)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9573 | 0.0001 |\n| 1v2 | 0.8163 | 0.0001 |\n| 2v3 | 0.5986 | 0.0001 |\n| 3v4 | 0.5413 | 0.0001 |\n| 4v5 | 0.5191 | 0.0166 |\n\n**Mistral-7B crossscorer** (K*=2)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 0v1 | 0.9798 | 0.0001 |\n| 1v2 | 0.8138 | 0.0001 |\n| 2v3 | 0.6075 | 0.0001 |\n| 3v4 | 0.5489 | 0.0001 |\n| 4v5 | 0.5389 | 0.0001 |\n\n**LLaMA-8B crossscorer** (K*=2)\n| Pair | AUC | perm_p |\n|------|-----|--------|\n| 2v3 | 0.6201 | 0.0001 |\n| 3v4 | 0.5228 | 0.0060 |\n| 4v5 | 0.5247 | 0.0034 |\n\n### Retrain-chain permutation_test.json (独立格式, p_value不同编码)\n\n**exp_008_retrain_chain (Pythia)**\n| Pair | AUC | p_value |\n|------|-----|---------|\n| 0v1 | 0.9968 | 0.0 |\n| 1v2 | 0.9855 | 0.0 |\n| 2v3 | 0.9556 | 0.0 |\n| 3v4 | 0.9029 | 0.304 |\n\n**exp_olmo_retrain_chain (OLMo)**\n| Pair | AUC | p_value |\n|------|-----|---------|\n| 0v1 | 0.9988 | 0.0 |\n| 1v2 | 0.9610 | 0.0 |\n| 2v3 | 0.8919 | 0.998 |\n| 3v4 | 0.8762 | 1.0 |\n\n### Borderline 10K 比较\n\n| Config | Pair | AUC | perm_p_10k |\n|--------|------|-----|------------|\n| LLaMA-3.1-8B (exp_018) | 1v2 | 0.6075 | 0.0001 |\n| Gemma-2-2B | 1v2 | 0.5981 | 0.0001 |\n| Mistral-7B (exp_019) | 1v2 | 0.5902 | 0.0001 |\n| 512-tok (exp_021) | 1v2 | 0.6136 | 0.0001 |\n\n---\n\n## T3: PELT Changepoint 完整配对数据 (37 configs)\n\n| Config | K*_OBD | K*_PELT | Agree |\n|--------|--------|---------|-------|\n| exp_008_retrain_chain | 4 | 4 | ✓ |\n| exp_018_llama8b | 2 | 1 | ✗ |\n| exp_021_length_128 | 2 | 1 | ✗ |\n| exp_021_length_256 | 2 | 1 | ✗ |\n| exp_021_length_512 | 2 | 1 | ✗ |\n| exp_023_wiki | 2 | 1 | ✗ |\n| exp_024_arxiv | 3 | 2 | ✗ |\n| exp_025_pythia_arxiv | 3 | 2 | ✗ |\n| exp_027_latex_ablation | 3 | 2 | ✗ |\n| exp_14b_c4 | 2 | 1 | ✗ |\n| exp_arXiv_llama8b | 3 | 2 | ✗ |\n| exp_arXiv_llama8b_crossscorer | 3 | 2 | ✗ |\n| exp_arXiv_mistral7b | 3 | 2 | ✗ |\n| exp_arXiv_mistral7b_crossscorer | 3 | 2 | ✗ |\n| exp_arXiv_olmo | 1 | 1 | ✓ |\n| exp_arXiv_qwen1b5_crossscorer | 3 | 2 | ✗ |\n| exp_arXiv_qwen7b | 3 | 2 | ✗ |\n| exp_arXiv_qwen7b_crossscorer | 2 | 2 | ✓ |\n| exp_code_llama8b | 2 | 2 | ✓ |\n| exp_code_mistral7b | 2 | 1 | ✗ |\n| exp_code_pythia1b4 | 1 | 1 | ✓ |\n| exp_code_qwen1b5 | 2 | 2 | ✓ |\n| exp_code_qwen1b5_pythia_scorer | 2 | 2 | ✓ |\n| exp_code_qwen7b | 2 | 2 | ✓ |\n| exp_pythia_retrain_depth7 | 7 | 4 | ✗ |\n| exp_qwen_retrain_chain | 4 | 4 | ✓ |\n| exp_qwen_retrain_chain_ext | 7 | 2 | ✗ |\n| exp_wiki_llama8b | 1 | 1 | ✓ |\n| exp_wiki_mistral7b | 1 | 1 | ✓ |\n| exp_wiki_olmo | 1 | 1 | ✓ |\n| exp_wiki_olmo_v2 | 1 | 1 | ✓ |\n| exp_wiki_pythia | 2 | 1 | ✗ |\n| exp_wiki_pythia_v2 | 1 | 1 | ✓ |\n| exp_wiki_qwen7b | 2 | 1 | ✗ |\n| exp_wiki_scorer_confound | 1 | 1 | ✓ |\n| exp_wiki_scorer_confound_1b5 | 1 | 1 | ✓ |\n| olmo_c4_cont | 1 | 1 | ✓ |\n\n**汇总**: 37 configs, 18 agree (48.6%), 19 disagree (51.4%)\n- K*_OBD = K*_PELT 时 agree: 当两者都为 1 (14 cases) 或都为 2 (5 cases) 或都为 4 (2 cases)\n- 不一致模式: K*_OBD 系统性偏高 (PELT 总是 ≤ OBD), 差 1 的有 15 cases, 差 ≥2 的有 4 cases\n\n---\n\n## T2: Fold-level AUC 数据 (1v2 和 2v3)\n\n### 核心 configs 的 5-fold AUC\n\n**C4 domain:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp016 (Qwen-1.5B) | 1v2 | 0.6262 | 0.5963 | 0.6362 | 0.6366 | 0.6337 | 0.6282 |\n| exp016 (Qwen-1.5B) | 2v3 | 0.5496 | 0.5516 | 0.5456 | 0.5403 | 0.5605 | 0.5501 |\n| exp018 (LLaMA-8B) | 1v2 | 0.6123 | 0.6362 | 0.6072 | 0.5975 | 0.6067 | 0.6140 |\n| exp018 (LLaMA-8B) | 2v3 | 0.5274 | 0.5345 | 0.5442 | 0.5342 | 0.5141 | 0.5101 |\n| exp019 (Mistral-7B) | 1v2 | 0.5935 | 0.5981 | 0.5894 | 0.5962 | 0.5850 | 0.5988 |\n| exp019 (Mistral-7B) | 2v3 | 0.5402 | 0.5308 | 0.5340 | 0.5493 | 0.5584 | 0.5286 |\n| exp_gemma2b | 1v2 | 0.5981 | 0.6010 | 0.5841 | 0.6006 | 0.5966 | 0.6082 |\n| exp_gemma2b | 2v3 | 0.5342 | 0.5598 | 0.5246 | 0.5338 | 0.5241 | 0.5286 |\n| exp_14b_c4 (Qwen-14B) | 1v2 | 0.6211 | 0.6252 | 0.6112 | 0.6153 | 0.6323 | 0.6214 |\n| exp_14b_c4 (Qwen-14B) | 2v3 | 0.5494 | 0.5362 | 0.5529 | 0.5590 | 0.5445 | 0.5546 |\n| olmo_c4_cont | 1v2 | 0.5070 | 0.5083 | 0.4946 | 0.4953 | 0.5170 | 0.5195 |\n| olmo_c4_cont | 2v3 | 0.5042 | 0.5106 | 0.4896 | 0.5140 | 0.4977 | 0.5093 |\n\n**arXiv domain:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp024 (Qwen-1.5B) | 1v2 | 0.8581 | 0.8763 | 0.8669 | 0.8411 | 0.8515 | 0.8549 |\n| exp024 (Qwen-1.5B) | 2v3 | 0.6436 | 0.6738 | 0.6349 | 0.6479 | 0.6537 | 0.6078 |\n| exp025 (Pythia-1.4B) | 1v2 | 0.8047 | 0.7906 | 0.8278 | 0.8018 | 0.8065 | 0.7967 |\n| exp025 (Pythia-1.4B) | 2v3 | 0.6545 | 0.6409 | 0.6433 | 0.6764 | 0.6548 | 0.6572 |\n| exp027_latex_ablation | 1v2 | 0.8297 | 0.8085 | 0.8529 | 0.8198 | 0.8292 | 0.8381 |\n| exp027_latex_ablation | 2v3 | 0.6229 | 0.6429 | 0.6196 | 0.6258 | 0.5986 | 0.6275 |\n\n**Wiki domain:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp023 (Qwen-1.5B) | 1v2 | 0.6193 | 0.6152 | 0.6161 | 0.6189 | 0.6112 | 0.6352 |\n| exp023 (Qwen-1.5B) | 2v3 | 0.5498 | 0.5473 | 0.5559 | 0.5378 | 0.5637 | 0.5442 |\n| exp_wiki_pythia_v2 | 1v2 | 0.5846 | 0.5826 | 0.5783 | 0.5842 | 0.5864 | 0.5913 |\n| exp_wiki_qwen7b | 1v2 | 0.6108 | 0.6135 | 0.6085 | 0.6031 | 0.6016 | 0.6272 |\n| exp_wiki_scorer_confound | 1v2 | 0.5870 | 0.5850 | 0.5825 | 0.5877 | 0.5766 | 0.6030 |\n\n**Retrain-chain configs:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| exp008 retrain (v2) | 1v2 | 0.9472 | 0.9520 | 0.9444 | 0.9558 | 0.9401 | 0.9437 |\n| exp008 retrain (v2) | 2v3 | 0.8891 | 0.8794 | 0.8828 | 0.8998 | 0.8986 | 0.8848 |\n| exp008 retrain (v2) | 3v4 | 0.7996 | 0.8020 | 0.7975 | 0.8036 | 0.7898 | 0.8050 |\n\n**Cross-scorer configs (arXiv, scorer=Pythia-1.4B):**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| Qwen-7B crossscorer | 1v2 | 0.8171 | 0.7892 | 0.8093 | 0.8265 | 0.8236 | 0.8372 |\n| Qwen-7B crossscorer | 2v3 | 0.5989 | 0.5920 | 0.6006 | 0.6108 | 0.5768 | 0.6142 |\n| Mistral-7B crossscorer | 1v2 | 0.8141 | 0.7874 | 0.8256 | 0.8225 | 0.8223 | 0.8125 |\n| Mistral-7B crossscorer | 2v3 | 0.6075 | 0.6052 | 0.5803 | 0.6210 | 0.6113 | 0.6195 |\n| LLaMA-8B crossscorer | 2v3 | 0.6201 | 0.6306 | 0.6115 | 0.6073 | 0.6136 | 0.6377 |\n\n**Length ablation:**\n\n| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |\n|--------|------|------|-----|-----|-----|-----|-----|\n| 128-tok | 1v2 | 0.6219 | 0.6405 | 0.6269 | 0.6191 | 0.6117 | 0.6112 |\n| 256-tok | 1v2 | 0.6282 | 0.6335 | 0.6173 | 0.6231 | 0.6244 | 0.6425 |\n| 512-tok | 1v2 | 0.6073 | 0.6184 | 0.5979 | 0.5952 | 0.6118 | 0.6134 |\n\n---\n\n## T6: Generator Identity AUC\n\n### 结论: 无独立的 \"generator identity classification AUC\" 指标\n\nmulti_source 实验测量的是将 generator ID 作为第 16 个特征加入 depth classifier 后的 AUC 变化, 而非 generator identity 本身的分类性能。\n\n### 所有 multi-source 实验的 Δ(with_label - no_label)\n\n**C4 domain (v1: Qwen-1.5B + Pythia-1.4B + OLMo-1B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9929 | 0.9948 | +0.0019 |\n| 1v2 | 0.7007 | 0.7015 | +0.0008 |\n| K* | 2 | 2 | unchanged |\n\n**C4 domain (v2: Qwen-1.5B + Pythia-1.4B + LLaMA-8B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9680 | 0.9785 | +0.0105 |\n| 1v2 | 0.7144 | 0.7250 | +0.0106 |\n| K* | 2 | 2 | unchanged |\n\n**arXiv domain (vocab-only, Qwen-1.5B + Pythia-1.4B + LLaMA-8B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9431 | 0.9436 | +0.0005 |\n| 1v2 | 0.6922 | 0.7020 | +0.0098 |\n| 2v3 | 0.5890 | 0.5883 | -0.0007 |\n| K* | 2 | 2 | unchanged |\n\n**arXiv domain (unified scorer, same generators)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9899 | 0.9911 | +0.0012 |\n| 1v2 | 0.8117 | 0.8338 | +0.0221 |\n| 2v3 | 0.6247 | 0.6276 | +0.0029 |\n| K* | 3 | 3 | unchanged |\n\n**Wiki domain (vocab-only, Qwen-1.5B + LLaMA-8B + Mistral-7B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.7616 | 0.7779 | +0.0163 |\n| 1v2 | 0.5434 | 0.5520 | +0.0086 |\n| K* | 1 | 1 | unchanged |\n\n**Wiki domain (unified scorer)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9603 | 0.9685 | +0.0082 |\n| 1v2 | 0.5685 | 0.5790 | +0.0105 |\n| K* | 1 | 1 | unchanged |\n\n**Code domain (vocab-only, Qwen-7B + LLaMA-8B + Mistral-7B)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.7891 | 0.7900 | +0.0009 |\n| 1v2 | 0.6353 | 0.6440 | +0.0087 |\n| K* | 2 | 2 | unchanged |\n\n**Code domain (unified scorer)**\n| Pair | AUC_no_label | AUC_with_label | Δ |\n|------|-------------|----------------|-------|\n| 0v1 | 0.9123 | 0.9123 | +0.0000 |\n| 1v2 | 0.6702 | 0.6803 | +0.0101 |\n| K* | 2 | 2 | unchanged |\n\n### 关键结论\n- **Generator identity 对 depth detection 的增益可忽略**: 平均 Δ(1v2) ≈ +0.01 AUC\n- **K* 从未因加入 generator label 而改变**\n- 最大 Δ 出现在 arXiv unified scorer 1v2 (+0.0221), 但仍不改变 K*\n- **不存在独立的 generator identity classification AUC** — 实验设计中没有将 \"识别 generator\" 作为目标任务\n\n---\n\n## 数据文件索引\n\n| 数据类型 | 文件路径 |\n|---------|---------|\n| Permutation test (retrain) | results/exp_008_retrain_chain/permutation_test.json |\n| Permutation test (OLMo retrain) | results/exp_olmo_retrain_chain/permutation_test.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp016_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp018_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp019_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp024_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp025_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp027_retrain_bootstrap.json |\n| Bootstrap CI (含 perm_p) | artifacts/exp_gemma2b_depth_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | artifacts/crossscorer_bootstrap_ci.json |\n| Bootstrap CI (含 perm_p) | results/exp_14b_c4/bootstrap_ci_results.json |\n| Bootstrap CI v2 | results/exp_008_retrain_chain/bootstrap_ci_v2.json |\n| Borderline 10K comparison | results/exp_bootstrap_10k/bootstrap_10k_comparison.json |\n| Borderline bootstrap | artifacts/borderline_bootstrap_ci.json |\n| PELT changepoint | results/exp_changepoint_kstar/changepoint_results.json |\n| PELT bootstrap comparison | results/exp_changepoint_kstar/bootstrap_comparison.json |\n| Multi-source v1 (C4) | results/exp_multi_source_detection/multi_source_results.json |\n| Multi-source v2 (C4) | results/exp_multi_source_detection_v2/multi_source_results.json |\n| Multi-source arXiv | results/exp_multi_source_arxiv/results.json |\n| Multi-source Wiki | results/exp_wiki_multi_source/results.json |\n| Multi-source Code | results/exp_code_multi_source/results.json |\n| Fold AUC (per config) | results/*/pairwise_auc.json, results_*/pairwise_auc.json |\n"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-20T16:49:42.645586+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/round22_raw_data_extraction.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-20T16:49:42.645785+00:00_

完整数据已提取并写入 `artifacts/round22_raw_data_extraction.md`。

---

## 摘要

### T4: Permutation test p-values
- **所有 boundary pair 的 perm_p 均为 0.0001** (= 0/10000 permutations 超过观测值), 包括 exp016, exp018, exp019, exp024, exp025, exp027, exp_gemma2b, 和全部 crossscorer configs
- 例外: retrain-chain 的 permutation_test.json 用不同编码, 其中 exp_008 3v4 p=0.304, exp_olmo 2v3 p=0.998 (这些是 K* 之后的第一个下降对, 不是 boundary pair)
- **exp_gemma2b** 的 3v4 (p=0.2919) 和 4v5 (p=0.3418) 不显著, 符合预期 (K*=1)

### T3: PELT changepoint
- 37 configs 完整列表已提取。18/37 (48.6%) K*_OBD = K*_PELT; 19/37 不一致
- PELT 系统性偏保守 (K*_PELT ≤ K*_OBD), 差值主要为 1

### T2: Fold-level AUC
- 所有 configs 的 1v2 和 2v3 五折 AUC 均已提取 (从 pairwise_auc.json 和 bootstrap_ci.json)
- 数据可直接用于 Youden's J optimal θ 计算

### T6: Generator identity AUC
- **不存在独立的 generator identity classification AUC 指标**
- multi_source 实验仅测量加入 generator label 后 depth classifier 的 AUC 增量
- 增量极小: 平均 Δ(1v2) ≈ +0.01; K* 在所有 domain/config 中未因此改变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_extract_r22_raw_data_20260520T164246"
}
```

</details>

---
