# analysis full experiment tables

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_analysis_full-experiment-tables_20260516T051338.jsonl`
- **Structured JSON:** [`896d1ab1506b21d81cce.json`](../../sessions/89/896d1ab1506b21d81cce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-16T05:16:55.128802+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T05:16:55.129255+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T05:16:55.129492+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "provenance_weight_training",
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "provenance_weight_training",
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T05:16:55.132409+00:00_

Error: result (116,305 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T05:16:55.132732+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract experiment metrics from registry JSON",
  "prompt": "I need to extract experiment metrics from a large JSON file at:\n/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need you to extract the following information for each experiment:\n- exp_id\n- metrics (especially eval_ppl or any PPL-related metric)\n- status\n- conclusion\n\nSpecifically, I need PPL values for these experiments:\n1. uniform_seed42, uniform_seed123, uniform_seed456\n2. adaptive_fix_seed42, adaptive_fix_seed123, adaptive_fix_seed456\n3. grid_b0_3_seed42\n4. grid_b0_5_seed123, grid_b0_5_seed456\n5. ess_only_seed42, ess_only_seed123, ess_only_seed456\n6. contamination_60_uniform_seed42\n7. contamination_60_seed42_r2\n8. contamination_60_grid_b0_5_seed42\n9. contamination_60_ess_only_seed42\n10. nmin1_seed42, adaptive_seed42, nmin4_seed42\n11. tau_05_seed42, tau_06_seed42, tau_07_seed42, tau_09_seed42, tau_095_seed42\n12. bs8_nmin2_seed42_r2\n13. golden_ratio_seed42\n14. grid_b_seed42_batch (this one may have multiple b values in its metrics)\n15. grid_b0_1_seed42\n16. detect_remove_baseline_seed42\n\nUse jq or python to parse the file. First probe structure, then extract all exp_ids and their metrics. Return a clean listing of exp_id -> PPL value for all experiments found. If an experiment has conclusion field, include that too."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract experiment metrics from registry JSON",
    "prompt": "I need to extract experiment metrics from a large JSON file at:\n/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need you to extract the following information for each experiment:\n- exp_id\n- metrics (especially eval_ppl or any PPL-related metric)\n- status\n- conclusion\n\nSpecifically, I need PPL values for these experiments:\n1. uniform_seed42, uniform_seed123, uniform_seed456\n2. adaptive_fix_seed42, adaptive_fix_seed123, adaptive_fix_seed456\n3. grid_b0_3_seed42\n4. grid_b0_5_seed123, grid_b0_5_seed456\n5. ess_only_seed42, ess_only_seed123, ess_only_seed456\n6. contamination_60_uniform_seed42\n7. contamination_60_seed42_r2\n8. contamination_60_grid_b0_5_seed42\n9. contamination_60_ess_only_seed42\n10. nmin1_seed42, adaptive_seed42, nmin4_seed42\n11. tau_05_seed42, tau_06_seed42, tau_07_seed42, tau_09_seed42, tau_095_seed42\n12. bs8_nmin2_seed42_r2\n13. golden_ratio_seed42\n14. grid_b_seed42_batch (this one may have multiple b values in its metrics)\n15. grid_b0_1_seed42\n16. detect_remove_baseline_seed42\n\nUse jq or python to parse the file. First probe structure, then extract all exp_ids and their metrics. Return a clean listing of exp_id -> PPL value for all experiments found. If an experiment has conclusion field, include that too."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T05:16:55.133031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T05:16:55.133209+00:00_

File content (48875 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T05:16:55.133383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T05:16:55.133540+00:00_

File content (48875 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T05:16:55.133722+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt\"",
  "description": "Probe beginning of the JSON file to understand structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt\"",
    "description": "Probe beginning of the JSON file to understand structure"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T05:16:55.135964+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"grid_b0_3_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:26:45.815Z\", \"updated_at\": \"2026-05-16T05:03:15.767Z\", \"hypothesis\": \"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\", \"parent\": \"grid_b_seed42_batch\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"pid\": 274304, \"log_path\": \"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\", \"submitted_at\": \"2026-05-16T01:13:08.506Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\", \"wall_clock_seconds\": 13807.3, \"gpu_hours\": 3.84}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:57:12.423Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:57:14.788065+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:03:15.767Z\"}, \"contamination_60_ess_only_seed42\": {\"status\": \"DONE\", \"r

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T05:16:55.136243+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = json.load(f)\n\n# The result field is a JSON string\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Target experiments\ntargets = [\n    'uniform_seed42', 'uniform_seed123', 'uniform_seed456',\n    'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n    'grid_b0_3_seed42',\n    'grid_b0_5_seed123', 'grid_b0_5_seed456',\n    'ess_only_seed42', 'ess_only_seed123', 'ess_only_seed456',\n    'contamination_60_uniform_seed42',\n    'contamination_60_seed42_r2',\n    'contamination_60_grid_b0_5_seed42',\n    'contamination_60_ess_only_seed42',\n    'nmin1_seed42', 'adaptive_seed42', 'nmin4_seed42',\n    'tau_05_seed42', 'tau_06_seed42', 'tau_07_seed42', 'tau_09_seed42', 'tau_095_seed42',\n    'bs8_nmin2_seed42_r2',\n    'golden_ratio_seed42',\n    'grid_b_seed42_batch',\n    'grid_b0_1_seed42',\n    'detect_remove_baseline_seed42',\n]\n\nprint(f\"Total experiments in registry: {len(experiments)}\")\nprint(f\"All exp_ids: {sorted(experiments.keys())}\")\nprint(\"\\n\" + \"=\"*80)\nprint(\"DETAILED EXTRACTION\")\nprint(\"=\"*80)\n\nfor exp_id in targets:\n    print(f\"\\n--- {exp_id} ---\")\n    if exp_id not in experiments:\n        print(\"  NOT FOUND in registry\")\n        continue\n    exp = experiments[exp_id]\n    print(f\"  status: {exp.get('status', 'N/A')}\")\n    metrics = exp.get('metrics', {})\n    if metrics:\n        # Print all PPL-related metrics\n        ppl_keys = [k for k in metrics if 'ppl' in k.lower() or 'perplexity' in k.lower()]\n        for k in ppl_keys:\n            print(f\"  {k}: {metrics[k]}\")\n        # Also print eval_loss if available\n        loss_keys = [k for k in metrics if 'eval_loss' in k.lower()]\n        for k in loss_keys:\n            print(f\"  {k}: {metrics[k]}\")\n        # Print all metrics for grid_b_seed42_batch since it may have multiple b values\n        if exp_id == 'grid_b_seed42_batch':\n            print(f\"  ALL METRICS: {json.dumps(metrics, indent=4)}\")\n    else:\n        print(\"  metrics: NONE\")\n    conclusion = exp.get('conclusion', 'N/A')\n    print(f\"  conclusion: {conclusion}\")\n\nEOF",
  "description": "Parse the JSON file and extract experiment metrics",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a87ce64d-ab6a-42f5-b69a-c04b815fd7b1/tool-results/mcp-agent-ml-research-read_registry-1778908435947.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = json.load(f)\n\n# The result field is a JSON string\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Target experiments\ntargets = [\n    'uniform_seed42', 'uniform_seed123', 'uniform_seed456',\n    'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n    'grid_b0_3_seed42',\n    'grid_b0_5_seed123', 'grid_b0_5_seed456',\n    'ess_only_seed42', 'ess_only_seed123', 'ess_only_seed456',\n    'contamination_60_uniform_seed42',\n    'contamination_60_seed42_r2',\n    'contamination_60_grid_b0_5_seed42',\n    'contamination_60_ess_only_seed42',\n    'nmin1_seed42', 'adaptive_seed42', 'nmin4_seed42',\n    'tau_05_seed42', 'tau_06_seed42', 'tau_07_seed42', 'tau_09_seed42', 'tau_095_seed42',\n    'bs8_nmin2_seed42_r2',\n    'golden_ratio_seed42',\n    'grid_b_seed42_batch',\n    'grid_b0_1_seed42',\n    'detect_remove_baseline_seed42',\n]\n\nprint(f\"Total experiments in registry: {len(experiments)}\")\nprint(f\"All exp_ids: {sorted(experiments.keys())}\")\nprint(\"\\n\" + \"=\"*80)\nprint(\"DETAILED EXTRACTION\")\nprint(\"=\"*80)\n\nfor exp_id in targets:\n    print(f\"\\n--- {exp_id} ---\")\n    if exp_id not in experiments:\n        print(\"  NOT FOUND in registry\")\n        continue\n    exp = experiments[exp_id]\n    print(f\"  status: {exp.get('status', 'N/A')}\")\n    metrics = exp.get('metrics', {})\n    if metrics:\n        # Print all PPL-related metrics\n        ppl_keys = [k for k in metrics if 'ppl' in k.lower() or 'perplexity' in k.lower()]\n        for k in ppl_keys:\n            print(f\"  {k}: {metrics[k]}\")\n        # Also print eval_loss if available\n        loss_keys = [k for k in metrics if 'eval_loss' in k.lower()]\n        for k in loss_keys:\n            print(f\"  {k}: {metrics[k]}\")\n        # Print all metrics for grid_b_seed42_batch since it may have multiple b values\n        if exp_id == 'grid_b_seed42_batch':\n            print(f\"  ALL METRICS: {json.dumps(metrics, indent=4)}\")\n    else:\n        print(\"  metrics: NONE\")\n    conclusion = exp.get('conclusion', 'N/A')\n    print(f\"  conclusion: {conclusion}\")\n\nEOF",
    "description": "Parse the JSON file and extract experiment metrics",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T05:16:55.136476+00:00_

Total experiments in registry: 62
All exp_ids: ['adaptive_fix_seed123', 'adaptive_fix_seed42', 'adaptive_fix_seed456', 'adaptive_seed123', 'adaptive_seed42', 'adaptive_seed456', 'adaptive_v2_seed123', 'adaptive_v2_seed42', 'adaptive_v2_seed456', 'baseline_qwen3_0.6b', 'bs8_nmin2_seed42', 'bs8_nmin2_seed42_r2', 'bs8_seed42', 'contamination_60_ess_only_seed42', 'contamination_60_grid_b0_5_seed42', 'contamination_60_seed42', 'contamination_60_seed42_r2', 'contamination_60_uniform_seed42', 'datagen_synthetic_4gpu', 'detector_modernbert', 'detector_tfidf_lr', 'diagnostic_contamination100', 'ess_only_seed123', 'ess_only_seed42', 'ess_only_seed456', 'golden_ratio_seed42', 'grid_b0_3_seed42', 'grid_b0_5_seed123', 'grid_b0_5_seed456', 'grid_b1_0_seed123', 'grid_b1_0_seed456', 'grid_b1_5_seed123', 'grid_b1_5_seed456', 'grid_b2_0_seed123', 'grid_b2_0_seed456', 'grid_b3_0_seed123', 'grid_b3_0_seed456', 'grid_b5_0_seed123', 'grid_b5_0_seed456', 'grid_b_low_seed42', 'grid_b_low_seed42_r2', 'grid_b_low_seed42_r3', 'grid_b_low_serial_seed42', 'grid_b_seed42_batch', 'nmin1_seed42', 'nmin4_seed42', 'nmin5_seed42', 'p0_contamination_60_datagen', 'tau_0.6_seed42', 'tau_05_nmin2_seed42', 'tau_05_seed42', 'tau_06_nmin2_seed42', 'tau_06_seed42', 'tau_07_nmin2_seed42', 'tau_07_seed42', 'tau_095_nmin2_seed42', 'tau_095_seed42', 'tau_09_nmin2_seed42', 'tau_09_seed42', 'uniform_seed123', 'uniform_seed42', 'uniform_seed456']

================================================================================
DETAILED EXTRACTION
================================================================================

--- uniform_seed42 ---
  status: DONE
  eval_ppl_holdout: 17.6939
  eval_loss_holdout: 2.8732
  conclusion: success

--- uniform_seed123 ---
  status: DONE
  eval_ppl_holdout: 17.6861
  eval_loss_holdout: 2.8728
  conclusion: success

--- uniform_seed456 ---
  status: DONE
  eval_ppl_holdout: 17.7015
  eval_loss_holdout: 2.8737
  conclusion: success

--- adaptive_fix_seed42 ---
  status: DONE
…[truncated 4524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T05:16:55.136766+00:00_

Here is the complete extraction:

## Experiment PPL Results

### Uniform Weighting (baseline)
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| uniform_seed42 | 17.6939 | DONE | success |
| uniform_seed123 | 17.6861 | DONE | success |
| uniform_seed456 | 17.7015 | DONE | success |

### Adaptive Fix
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| adaptive_fix_seed42 | 17.6527 | DONE | success |
| adaptive_fix_seed123 | 17.6432 | DONE | success |
| adaptive_fix_seed456 | 17.6566 | DONE | success |

### Grid b=0.3
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| grid_b0_3_seed42 | 17.64 | DONE | success |

### Grid b=0.5
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| grid_b0_5_seed123 | 17.638 | DONE | success |
| grid_b0_5_seed456 | 17.65 | DONE | success |

### ESS-Only
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| ess_only_seed42 | 17.73 | DONE | success |
| ess_only_seed123 | 17.72 | DONE | success |
| ess_only_seed456 | 17.719 | DONE | success |

### Contamination 60%
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| contamination_60_uniform_seed42 | 17.766 | DONE | success |
| contamination_60_seed42_r2 | 17.74 | DONE | success |
| contamination_60_grid_b0_5_seed42 | 17.704 | DONE | success |
| contamination_60_ess_only_seed42 | 17.77 | DONE | success |

### n_min Ablation
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| nmin1_seed42 | 17.789 | DONE | success |
| adaptive_seed42 | 17.644 | DONE | success |
| nmin4_seed42 | 17.6947 | DONE | success |

### Tau Ablation
| exp_id | eval_ppl | status | conclusion |
|--------|----------|--------|------------|
| tau_05_seed42 | 17.688 | DONE | success |
| tau_06_seed42 | 17.6805 | DONE | success |
| tau_07_seed42 | 17.6793 | DONE | su
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T05:16:55.137070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables",
  "description": "Create tables output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables",
    "description": "Create tables output directory"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T05:16:55.137261+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T05:16:55.137438+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.csv",
  "content": "Method,rho,PPL,Delta_vs_uniform,Seeds\nUniform,0.4,17.694±0.008,0.000,42/123/456\nAdaptive (dual-constraint),0.4,17.651±0.007,-0.043,42/123/456\nGrid-best (b=0.3),0.4,17.640,-0.054,42\nESS-only,0.4,17.723±0.006,+0.029,42/123/456\nUniform,0.6,17.766,0.000,42\nAdaptive (τ=0.8),0.6,17.740,-0.026,42\nGrid (b=0.5),0.6,17.704,-0.062,42\nESS-only,0.6,17.770,+0.004,42\nAdaptive (τ=0.6),0.6,RUNNING,,42\nAdaptive (τ=0.7),0.6,RUNNING,,42\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.csv",
    "content": "Method,rho,PPL,Delta_vs_uniform,Seeds\nUniform,0.4,17.694±0.008,0.000,42/123/456\nAdaptive (dual-constraint),0.4,17.651±0.007,-0.043,42/123/456\nGrid-best (b=0.3),0.4,17.640,-0.054,42\nESS-only,0.4,17.723±0.006,+0.029,42/123/456\nUniform,0.6,17.766,0.000,42\nAdaptive (τ=0.8),0.6,17.740,-0.026,42\nGrid (b=0.5),0.6,17.704,-0.062,42\nESS-only,0.6,17.770,+0.004,42\nAdaptive (τ=0.6),0.6,RUNNING,,42\nAdaptive (τ=0.7),0.6,RUNNING,,42\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T05:16:55.137610+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T05:16:55.137780+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.md",
  "content": "## Table 1: Main Results\n\n| Method | ρ | PPL (mean±std) | Δ vs uniform | Seeds |\n|--------|---|----------------|--------------|-------|\n| Uniform | 0.4 | 17.694±0.008 | 0.000 | 42/123/456 |\n| Adaptive (dual-constraint) | 0.4 | 17.651±0.007 | -0.043 | 42/123/456 |\n| Grid-best (b=0.3) | 0.4 | 17.640 | -0.054 | 42 |\n| ESS-only | 0.4 | 17.723±0.006 | +0.029 | 42/123/456 |\n| Uniform | 0.6 | 17.766 | 0.000 | 42 |\n| Adaptive (τ=0.8) | 0.6 | 17.740 | -0.026 | 42 |\n| Grid (b=0.5) | 0.6 | 17.704 | -0.062 | 42 |\n| ESS-only | 0.6 | 17.770 | +0.004 | 42 |\n| Adaptive (τ=0.6) | 0.6 | RUNNING | — | 42 |\n| Adaptive (τ=0.7) | 0.6 | RUNNING | — | 42 |\n\n**Notes:**\n- ρ=0.4: 3-seed mean±std for uniform, adaptive, ESS-only; grid-best only has seed42\n- ρ=0.6: single seed42; adaptive τ=0.6/0.7 still running\n- Negative Δ = better than uniform\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.md",
    "content": "## Table 1: Main Results\n\n| Method | ρ | PPL (mean±std) | Δ vs uniform | Seeds |\n|--------|---|----------------|--------------|-------|\n| Uniform | 0.4 | 17.694±0.008 | 0.000 | 42/123/456 |\n| Adaptive (dual-constraint) | 0.4 | 17.651±0.007 | -0.043 | 42/123/456 |\n| Grid-best (b=0.3) | 0.4 | 17.640 | -0.054 | 42 |\n| ESS-only | 0.4 | 17.723±0.006 | +0.029 | 42/123/456 |\n| Uniform | 0.6 | 17.766 | 0.000 | 42 |\n| Adaptive (τ=0.8) | 0.6 | 17.740 | -0.026 | 42 |\n| Grid (b=0.5) | 0.6 | 17.704 | -0.062 | 42 |\n| ESS-only | 0.6 | 17.770 | +0.004 | 42 |\n| Adaptive (τ=0.6) | 0.6 | RUNNING | — | 42 |\n| Adaptive (τ=0.7) | 0.6 | RUNNING | — | 42 |\n\n**Notes:**\n- ρ=0.4: 3-seed mean±std for uniform, adaptive, ESS-only; grid-best only has seed42\n- ρ=0.6: single seed42; adaptive τ=0.6/0.7 still running\n- Negative Δ = better than uniform\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T05:16:55.140040+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T05:16:55.140304+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.csv",
  "content": "Ablation,Setting,PPL,Delta_vs_default,Notes\nn_min sweep,n_min=1,17.789,+0.136,nmin1_seed42\nn_min sweep,n_min=2 (default),17.653,0.000,adaptive_fix_seed42\nn_min sweep,n_min=3,17.644,-0.009,adaptive_seed42\nn_min sweep,n_min=4,17.695,+0.042,nmin4_seed42\nτ sweep,τ=0.5,17.688,+0.035,tau_05_seed42\nτ sweep,τ=0.6,17.681,+0.028,tau_06_seed42\nτ sweep,τ=0.7,17.679,+0.027,tau_07_seed42\nτ sweep,τ=0.8 (default),17.653,0.000,adaptive_fix_seed42\nτ sweep,τ=0.9,17.712,+0.059,tau_09_seed42; NEGATIVE\nτ sweep,τ=0.95,17.723,+0.070,tau_095_seed42; NEGATIVE\nbatch_size,bs=8,17.730,+0.077,bs8_nmin2_seed42_r2; NEGATIVE\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.csv",
    "content": "Ablation,Setting,PPL,Delta_vs_default,Notes\nn_min sweep,n_min=1,17.789,+0.136,nmin1_seed42\nn_min sweep,n_min=2 (default),17.653,0.000,adaptive_fix_seed42\nn_min sweep,n_min=3,17.644,-0.009,adaptive_seed42\nn_min sweep,n_min=4,17.695,+0.042,nmin4_seed42\nτ sweep,τ=0.5,17.688,+0.035,tau_05_seed42\nτ sweep,τ=0.6,17.681,+0.028,tau_06_seed42\nτ sweep,τ=0.7,17.679,+0.027,tau_07_seed42\nτ sweep,τ=0.8 (default),17.653,0.000,adaptive_fix_seed42\nτ sweep,τ=0.9,17.712,+0.059,tau_09_seed42; NEGATIVE\nτ sweep,τ=0.95,17.723,+0.070,tau_095_seed42; NEGATIVE\nbatch_size,bs=8,17.730,+0.077,bs8_nmin2_seed42_r2; NEGATIVE\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:16:55.140510+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T05:16:55.140694+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.md",
  "content": "## Table 2: Ablations (ρ=0.4, seed42)\n\n### n_min Sweep\n\n| Setting | PPL | Δ vs default | Notes |\n|---------|-----|--------------|-------|\n| n_min=1 | 17.789 | +0.136 | nmin1_seed42 |\n| n_min=2 (default) | 17.653 | 0.000 | adaptive_fix_seed42 |\n| n_min=3 | 17.644 | -0.009 | adaptive_seed42 |\n| n_min=4 | 17.695 | +0.042 | nmin4_seed42 |\n\n### τ Sweep\n\n| Setting | PPL | Δ vs default | Notes |\n|---------|-----|--------------|-------|\n| τ=0.5 | 17.688 | +0.035 | tau_05_seed42 |\n| τ=0.6 | 17.681 | +0.028 | tau_06_seed42 |\n| τ=0.7 | 17.679 | +0.027 | tau_07_seed42 |\n| τ=0.8 (default) | 17.653 | 0.000 | adaptive_fix_seed42 |\n| τ=0.9 | 17.712 | +0.059 | tau_09_seed42; **NEGATIVE** |\n| τ=0.95 | 17.723 | +0.070 | tau_095_seed42; **NEGATIVE** |\n\n### Batch Size\n\n| Setting | PPL | Δ vs default | Notes |\n|---------|-----|--------------|-------|\n| bs=8 | 17.730 | +0.077 | bs8_nmin2_seed42_r2; **NEGATIVE** |\n\n**Notes:**\n- Default = adaptive_fix_seed42 (n_min=2, τ=0.8, bs=4), PPL=17.653\n- Negative Δ = better than default\n- NEGATIVE = conclusion marked negative in registry\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.md",
    "content": "## Table 2: Ablations (ρ=0.4, seed42)\n\n### n_min Sweep\n\n| Setting | PPL | Δ vs default | Notes |\n|---------|-----|--------------|-------|\n| n_min=1 | 17.789 | +0.136 | nmin1_seed42 |\n| n_min=2 (default) | 17.653 | 0.000 | adaptive_fix_seed42 |\n| n_min=3 | 17.644 | -0.009 | adaptive_seed42 |\n| n_min=4 | 17.695 | +0.042 | nmin4_seed42 |\n\n### τ Sweep\n\n| Setting | PPL | Δ vs default | Notes |\n|---------|-----|--------------|-------|\n| τ=0.5 | 17.688 | +0.035 | tau_05_seed42 |\n| τ=0.6 | 17.681 | +0.028 | tau_06_seed42 |\n| τ=0.7 | 17.679 | +0.027 | tau_07_seed42 |\n| τ=0.8 (default) | 17.653 | 0.000 | adaptive_fix_seed42 |\n| τ=0.9 | 17.712 | +0.059 | tau_09_seed42; **NEGATIVE** |\n| τ=0.95 | 17.723 | +0.070 | tau_095_seed42; **NEGATIVE** |\n\n### Batch Size\n\n| Setting | PPL | Δ vs default | Notes |\n|---------|-----|--------------|-------|\n| bs=8 | 17.730 | +0.077 | bs8_nmin2_seed42_r2; **NEGATIVE** |\n\n**Notes:**\n- Default = adaptive_fix_seed42 (n_min=2, τ=0.8, bs=4), PPL=17.653\n- Negative Δ = better than default\n- NEGATIVE = conclusion marked negative in registry\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T05:16:55.140890+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T05:16:55.141054+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.csv",
  "content": "Method_or_b,PPL,Delta_vs_uniform,Notes\ngolden_ratio,17.654,-0.040,golden_ratio_seed42\ndetect_remove,RUNNING,,detect_remove_baseline_seed42; RUNNING\nb=0.1,RUNNING,,grid_b0_1_seed42; RUNNING\nb=0.3,17.640,-0.054,grid_b0_3_seed42 (independent run)\nb=0.5,17.651,-0.043,grid_b_seed42_batch\nb=1.0,17.692,-0.002,grid_b_seed42_batch\nb=1.5,17.718,+0.024,grid_b_seed42_batch\nb=2.0,17.741,+0.047,grid_b_seed42_batch\nb=3.0,17.774,+0.080,grid_b_seed42_batch\nb=5.0,17.818,+0.124,grid_b_seed42_batch\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.csv",
    "content": "Method_or_b,PPL,Delta_vs_uniform,Notes\ngolden_ratio,17.654,-0.040,golden_ratio_seed42\ndetect_remove,RUNNING,,detect_remove_baseline_seed42; RUNNING\nb=0.1,RUNNING,,grid_b0_1_seed42; RUNNING\nb=0.3,17.640,-0.054,grid_b0_3_seed42 (independent run)\nb=0.5,17.651,-0.043,grid_b_seed42_batch\nb=1.0,17.692,-0.002,grid_b_seed42_batch\nb=1.5,17.718,+0.024,grid_b_seed42_batch\nb=2.0,17.741,+0.047,grid_b_seed42_batch\nb=3.0,17.774,+0.080,grid_b_seed42_batch\nb=5.0,17.818,+0.124,grid_b_seed42_batch\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T05:16:55.141227+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T05:16:55.141397+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.md",
  "content": "## Table 3: Baselines & Grid Sweep (ρ=0.4, seed42)\n\n### Baselines\n\n| Method | PPL | Δ vs uniform | Notes |\n|--------|-----|--------------|-------|\n| Golden ratio | 17.654 | -0.040 | golden_ratio_seed42 |\n| Detect & remove | RUNNING | — | RUNNING |\n\n### Grid b Sweep\n\n| b | PPL | Δ vs uniform | Notes |\n|---|-----|--------------|-------|\n| 0.1 | RUNNING | — | RUNNING |\n| 0.3 | 17.640 | -0.054 | Independent run (grid_b0_3_seed42) |\n| 0.5 | 17.651 | -0.043 | grid_b_seed42_batch |\n| 1.0 | 17.692 | -0.002 | grid_b_seed42_batch |\n| 1.5 | 17.718 | +0.024 | grid_b_seed42_batch |\n| 2.0 | 17.741 | +0.047 | grid_b_seed42_batch |\n| 3.0 | 17.774 | +0.080 | grid_b_seed42_batch |\n| 5.0 | 17.818 | +0.124 | grid_b_seed42_batch |\n\n**Notes:**\n- Uniform baseline (seed42): PPL = 17.694\n- Negative Δ = better than uniform\n- Best grid point: b=0.3 (PPL=17.640, Δ=-0.054)\n- Monotonic degradation as b increases past 0.5\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.md",
    "content": "## Table 3: Baselines & Grid Sweep (ρ=0.4, seed42)\n\n### Baselines\n\n| Method | PPL | Δ vs uniform | Notes |\n|--------|-----|--------------|-------|\n| Golden ratio | 17.654 | -0.040 | golden_ratio_seed42 |\n| Detect & remove | RUNNING | — | RUNNING |\n\n### Grid b Sweep\n\n| b | PPL | Δ vs uniform | Notes |\n|---|-----|--------------|-------|\n| 0.1 | RUNNING | — | RUNNING |\n| 0.3 | 17.640 | -0.054 | Independent run (grid_b0_3_seed42) |\n| 0.5 | 17.651 | -0.043 | grid_b_seed42_batch |\n| 1.0 | 17.692 | -0.002 | grid_b_seed42_batch |\n| 1.5 | 17.718 | +0.024 | grid_b_seed42_batch |\n| 2.0 | 17.741 | +0.047 | grid_b_seed42_batch |\n| 3.0 | 17.774 | +0.080 | grid_b_seed42_batch |\n| 5.0 | 17.818 | +0.124 | grid_b_seed42_batch |\n\n**Notes:**\n- Uniform baseline (seed42): PPL = 17.694\n- Negative Δ = better than uniform\n- Best grid point: b=0.3 (PPL=17.640, Δ=-0.054)\n- Monotonic degradation as b increases past 0.5\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T05:16:55.141586+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T05:16:55.141781+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 1: Main Results",
  "type": "data",
  "description": "Main results table comparing uniform vs adaptive vs grid-best vs ESS-only at ρ=0.4 and ρ=0.6 (CSV)",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.csv",
  "tags": "['results', 'table', 'main']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 1: Main Results",
    "type": "data",
    "description": "Main results table comparing uniform vs adaptive vs grid-best vs ESS-only at ρ=0.4 and ρ=0.6 (CSV)",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.csv",
    "tags": "['results', 'table', 'main']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T05:16:55.144073+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_342ab0\", \"name\": \"Table 1: Main Results\", \"type\": \"data\", \"description\": \"Main results table comparing uniform vs adaptive vs grid-best vs ESS-only at ρ=0.4 and ρ=0.6 (CSV)\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/table1_main.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:16:35.760460+00:00\", \"tags\": [\"results\", \"table\", \"main\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T05:16:55.144269+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 1: Main Results (Markdown)",
  "type": "report",
  "description": "Main results table in Markdown format with notes",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.md",
  "tags": "['results', 'table', 'main']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 1: Main Results (Markdown)",
    "type": "report",
    "description": "Main results table in Markdown format with notes",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table1_main.md",
    "tags": "['results', 'table', 'main']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T05:16:55.144449+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_35813d\", \"name\": \"Table 1: Main Results (Markdown)\", \"type\": \"report\", \"description\": \"Main results table in Markdown format with notes\", \"path\": \"projects/provenance_weight_training/artifacts/_project/report/table1_main.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:16:37.726726+00:00\", \"tags\": [\"results\", \"table\", \"main\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T05:16:55.144632+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 2: Ablations",
  "type": "data",
  "description": "Ablation results: n_min sweep, τ sweep, batch_size (CSV)",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.csv",
  "tags": "['results', 'table', 'ablation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 2: Ablations",
    "type": "data",
    "description": "Ablation results: n_min sweep, τ sweep, batch_size (CSV)",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.csv",
    "tags": "['results', 'table', 'ablation']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T05:16:55.144841+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_2e994b\", \"name\": \"Table 2: Ablations\", \"type\": \"data\", \"description\": \"Ablation results: n_min sweep, τ sweep, batch_size (CSV)\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/table2_ablations.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:16:39.585045+00:00\", \"tags\": [\"results\", \"table\", \"ablation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T05:16:55.145052+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 2: Ablations (Markdown)",
  "type": "report",
  "description": "Ablation results in Markdown format with n_min, τ, batch_size sections",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.md",
  "tags": "['results', 'table', 'ablation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 2: Ablations (Markdown)",
    "type": "report",
    "description": "Ablation results in Markdown format with n_min, τ, batch_size sections",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table2_ablations.md",
    "tags": "['results', 'table', 'ablation']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T05:16:55.145250+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c70b38\", \"name\": \"Table 2: Ablations (Markdown)\", \"type\": \"report\", \"description\": \"Ablation results in Markdown format with n_min, τ, batch_size sections\", \"path\": \"projects/provenance_weight_training/artifacts/_project/report/table2_ablations.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:16:41.017737+00:00\", \"tags\": [\"results\", \"table\", \"ablation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T05:16:55.145427+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 3: Baselines & Grid Sweep",
  "type": "data",
  "description": "Baselines (golden ratio, detect-remove) and grid b sweep results (CSV)",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.csv",
  "tags": "['results', 'table', 'grid', 'baseline']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 3: Baselines & Grid Sweep",
    "type": "data",
    "description": "Baselines (golden ratio, detect-remove) and grid b sweep results (CSV)",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.csv",
    "tags": "['results', 'table', 'grid', 'baseline']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T05:16:55.145621+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_ddb394\", \"name\": \"Table 3: Baselines & Grid Sweep\", \"type\": \"data\", \"description\": \"Baselines (golden ratio, detect-remove) and grid b sweep results (CSV)\", \"path\": \"projects/provenance_weight_training/artifacts/_project/data/table3_baselines.csv\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:16:42.875508+00:00\", \"tags\": [\"results\", \"table\", \"grid\", \"baseline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T05:16:55.145817+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Table 3: Baselines & Grid Sweep (Markdown)",
  "type": "report",
  "description": "Baselines and grid b sweep in Markdown format with notes",
  "project": "provenance_weight_training",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.md",
  "tags": "['results', 'table', 'grid', 'baseline']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Table 3: Baselines & Grid Sweep (Markdown)",
    "type": "report",
    "description": "Baselines and grid b sweep in Markdown format with notes",
    "project": "provenance_weight_training",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/tables/table3_baselines.md",
    "tags": "['results', 'table', 'grid', 'baseline']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T05:16:55.148173+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_a0df33\", \"name\": \"Table 3: Baselines & Grid Sweep (Markdown)\", \"type\": \"report\", \"description\": \"Baselines and grid b sweep in Markdown format with notes\", \"path\": \"projects/provenance_weight_training/artifacts/_project/report/table3_baselines.md\", \"url\": null, \"project\": \"provenance_weight_training\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T05:16:44.818331+00:00\", \"tags\": [\"results\", \"table\", \"grid\", \"baseline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_full-experiment-tables_20260516T051338",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 2
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T05:16:55.148399+00:00_

6 files已生成并注册，位于 `artifacts/tables/`。

关键结果摘要：

**Table 1** — Adaptive (dual-constraint) 在 ρ=0.4 下 PPL=17.651±0.007，比 uniform (17.694±0.008) 低 0.043；ρ=0.6 下 grid b=0.5 最优 (17.704, Δ=-0.062)。

**Table 2** — 最佳消融配置为 n_min=3 (PPL=17.644)，τ=0.8 是最优 τ 值；bs=8 和高 τ (≥0.9) 均为 NEGATIVE。

**Table 3** — Grid sweep 中 b=0.3 最优 (17.640, Δ=-0.054)，PPL 随 b 增大单调恶化；golden_ratio 接近 adaptive (17.654)。

仍在跑的实验：contamination_60 的 τ=0.6/0.7、grid_b0_1、detect_remove_baseline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_full-experiment-tables_20260516T051338"
}
```

</details>

---
