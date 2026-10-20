# analysis rebootstrap importance b10000

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/chats/worker_analysis_rebootstrap_importance_b10000_20260514T090502.jsonl`
- **Structured JSON:** [`412af193ee9133d1be32.json`](../../sessions/41/412af193ee9133d1be32.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

97 recorded events

### Tool call

_source line 1 · 2026-05-14T09:10:20.345197+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T09:10:20.345750+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T09:10:20.346035+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -d /root/autodl-tmp/pacs/profiling_output_bf16_*imp* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -d /root/autodl-tmp/pacs/profiling_output_bf16_*imp* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T09:10:20.346201+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T09:10:20.346330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T09:10:20.346615+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T09:10:20.346804+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "filters": "{'status': 'DONE'}",
  "limit": "0",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "filters": "{'status': 'DONE'}",
    "limit": "0",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T09:10:20.347968+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"bf16_qw_rand_s030\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"median_high\": 4.200557, \"median_mid\": 6.477036, \"median_low\": 8.065662, \"median_diff\": 2.418272, \"permutation_p\": 0.012, \"cohens_d\": -0.03513, \"wilcoxon_p\": 0.01566, \"bootstrap_ci_low\": 0.241897, \"bootstrap_ci_high\": 3.314824}}, \"c4_entropy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"importance_entropy_delta\": {\"s015\": -0.0402, \"s020\": -0.0472, \"s025\": -0.0446, \"s030\": -0.0436}, \"random_entropy_delta\": {\"s015\": 0.1283, \"s020\": 0.136, \"s025\": 0.2171, \"s030\": 0.2327}, \"importance_gini_delta\": {\"s015\": -0.0301, \"s020\": -0.0404, \"s025\": -0.0647, \"s030\": -0.0806}, \"random_gini_delta\": {\"s015\": -0.0309, \"s020\": -0.0403, \"s025\": -0.062, \"s030\": -0.0732}, \"importance_cv_delta\": {\"s015\": -0.564, \"s020\": -0.774, \"s025\": -1.287, \"s030\": -1.665}, \"random_cv_delta\": {\"s015\": -1.021, \"s020\": -1.203, \"s025\": -1.923, \"s030\": -2.137}, \"problems_completed\": 30, \"runtime_minutes\": 69.1}}, \"bf16_qw_rand_s025\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 14.4213, \"median\": 1.6043, \"ci\": [7.1074, 23.4587], \"median_ci\": [0.6977, 3.0736], \"winsorized_mean\": 9.3765, \"skewness\": 4.8263}, \"mid\": {\"mean\": 18.6458, \"median\": 2.2225, \"ci\": [3.3729, 41.6037], \"median_ci\": [0.6093, 11.5889], \"winsorized_mean\": 14.2901, \"skewness\": 3.8245}, \"low\": {\"mean\": 17.7277, \"median\": 2.2641, \"ci\": [4.3523, 37.2093], \"median_ci\": [1.2218, 4.8561], \"winsorized_mean\": 9.9876, \"skewness\": 5.7652}}, \"perplexity\": {\"high\": {\"dense\": 1.0737, \"attn\": 2.0183, \"kv\": 3.1882, \"both\": 9.7654}, \"mid\": {\"dense\": 1.1322, \"attn\": 2.3476, \"kv\": 4.0124, \"both\": 17.3298}, \"low\": {\"dense\": 1.1517, \"attn\": 2.7834, \"kv\": 5.8762, \"both\": 25
…[truncated 35277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T09:10:20.348232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -d /root/autodl-tmp/pacs/profiling_output_bf16*imp*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -d /root/autodl-tmp/pacs/profiling_output_bf16*imp*",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T09:10:20.348455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T09:10:20.348620+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015\\n/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020\\n/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s025\\n/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030\\n/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015\\n/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s020\\n/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s025\\n/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.27}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T09:10:20.348754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T09:10:20.348989+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s015/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T09:10:20.349128+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T09:10:20.349308+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T09:10:20.349474+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\ntrain.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T09:10:20.349608+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/ -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/ -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T09:10:20.349734+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/ -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/ -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T09:10:20.349858+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T09:10:20.349978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T09:10:20.350117+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json')); print(list(d.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json')); print(list(d.keys()))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T09:10:20.350240+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T09:10:20.350356+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json')); print(list(d.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json')); print(list(d.keys()))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T09:10:20.350511+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T09:10:20.350644+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -100 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -100 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T09:10:20.350825+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.3\\n    ],\\n    \\\"masking_method\\\": \\\"importance\\\",\\n    \\\"head_importance_metric\\\": \\\"attention_frobenius_norm\\\",\\n    \\\"kv_importance_metric\\\": \\\"cumulative_attention_received\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.1689,\\n        \\\"attn\\\": 1.7123,\\n        \\\"kv\\\": 2.0544,\\n        \\\"both\\\": 3.2372\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.2286,\\n        \\\"attn\\\": 1.9347,\\n        \\\"kv\\\": 51.6485,\\n        \\\"both\\\": 122.609\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 1.7894,\\n        \\\"kv\\\": 9.4821,\\n        \\\"both\\\": 24.2847\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 0.554708,\\n        \\\"ci_low\\\": 0.277272,\\n        \\\"ci_high\\\": 0.919782,\\n        \\\"median\\\": 0.053399,\\n        \\\"winsorized_mean\\\": 0.336673,\\n        \\\"skewness\\\": 10.622,\\n        \\\"outlier_count\\\": 6\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 57.794625,\\n
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T09:10:20.350974+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -100 /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -100 /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T09:10:20.351166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.3\\n    ],\\n    \\\"masking_method\\\": \\\"importance\\\",\\n    \\\"head_importance_metric\\\": \\\"attention_frobenius_norm\\\",\\n    \\\"kv_importance_metric\\\": \\\"cumulative_attention_received\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 16289,\\n      \\\"n_segments\\\": 295\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32227,\\n      \\\"n_segments\\\": 276\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 4372,\\n      \\\"n_segments\\\": 26\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.0738,\\n        \\\"attn\\\": 1.2499,\\n        \\\"kv\\\": 1.6183,\\n        \\\"both\\\": 1.8617\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.1518,\\n        \\\"attn\\\": 1.6415,\\n        \\\"kv\\\": 25.4582,\\n        \\\"both\\\": 35.3232\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.1327,\\n        \\\"attn\\\": 1.3014,\\n        \\\"kv\\\": 7.18,\\n        \\\"both\\\": 9.4756\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 0.058026,\\n        \\\"ci_low\\\": -0.018689,\\n        \\\"ci_high\\\": 0.153658,\\n        \\\"median\\\": 0.009502,\\n        \\\"median_ci_low\\\": 0.004245,\\n        \\\"median_ci_high\\\": 0.015015,\\n        \\\"winsorized_mean\\\": 0.027511,\\n        \\\"skewness\\\": 10.8491,\\n        \\\"outlier_count\\\": 2\\n      }\\n    },\\n    \\\"low_
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T09:10:20.351342+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -c \"per_problem\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -c \"per_problem\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T09:10:20.351496+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T09:10:20.351628+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -c \"per_problem\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -c \"per_problem\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T09:10:20.351835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T09:10:20.352019+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -200 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -200 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T09:10:20.352283+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        \\\"ii_high\\\": 0.6390307250030085,\\n        \\\"n_segments_high\\\": 8,\\n        \\\"ii_mid\\\": 4.521795933148759,\\n        \\\"n_segments_mid\\\": 2,\\n        \\\"ii_low\\\": 43.069317292400484,\\n        \\\"n_segments_low\\\": 15\\n      },\\n      {\\n        \\\"problem_idx\\\": 31,\\n        \\\"problem_id\\\": \\\"test/precalculus/659.json\\\",\\n        \\\"ii_high\\\": 0.004395128854553398,\\n        \\\"n_segments_high\\\": 10,\\n        \\\"ii_mid\\\": 0.8262262789841155,\\n        \\\"n_segments_mid\\\": 11,\\n        \\\"ii_low\\\": 4.893728589837483,\\n        \\\"n_segments_low\\\": 9\\n      },\\n      {\\n        \\\"problem_idx\\\": 32,\\n        \\\"problem_id\\\": \\\"test/prealgebra/1572.json\\\",\\n        \\\"ii_high\\\": 0.010605891152519753,\\n        \\\"n_segments_high\\\": 1,\\n        \\\"ii_mid\\\": 0.390244950683861,\\n        \\\"n_segments_mid\\\": 1,\\n        \\\"ii_low\\\": 8.434673288269815,\\n        \\\"n_segments_low\\\": 6\\n      },\\n      {\\n        \\\"problem_idx\\\": 33,\\n        \\\"problem_id\\\": \\\"test/prealgebra/1973.json\\\",\\n        \\\"ii_high\\\": -0.006651676486329361,\\n        \\\"n_segments_high\\\": 3,\\n        \\\"ii_mid\\\": 0.7516752836111653,\\n        \\\"n_segments_mid\\\": 1,\\n        \\\"ii_low\\\": 4.51354439851617,\\n        \\\"n_segments_low\\\": 2\\n      },\\n      {\\n        \\\"problem_idx\\\": 34,\\n        \\\"problem_id\\\": \\\"test/number_theory/1287.json\\\",\\n        \\\"ii_high\\\": 0.1230356229274907,\\n        \\\"n_segments_high\\\": 5,\\n        \\\"ii_mid\\\": 4.801385443055682,\\n        \\\"n_segments_mid\\\": 4,\\n        \\\"ii_low\\\": 96.19486286865694,\\n        \\\"n_segments_low\\\": 5\\n      },\\n      {\\n        \\\"problem_idx\\\": 35,\\n        \\\"problem_id\\\": \\\"test/prealgebra/1356.json\\\",\\n        \\\"ii_high\\\": 0.39765294571190446,\\n        \\\"n_segments_high\\\": 5,\
…[truncated 5514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T09:10:20.352510+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -A 20 \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -A 20 \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T09:10:20.352666+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T09:10:20.352794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/analysis/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/analysis/ -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T09:10:20.352926+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/analysis/analyze_strategy_phase_crossover.py\\n/root/autodl-tmp/pacs/analysis/bootstrap_median_gradient.py\\n/root/autodl-tmp/pacs/analysis/bootstrap_phase_gradient.py\\n/root/autodl-tmp/pacs/analysis/bootstrap_per_problem.py\\n/root/autodl-tmp/pacs/analysis/analyze_v6_complete.py\\n/root/autodl-tmp/pacs/analysis/mid_sparsity_gap_analysis.py\\n/root/autodl-tmp/pacs/analysis/stat_test_qw_rand.py\\n/root/autodl-tmp/pacs/analysis/cross_model_analysis.py\\n/root/autodl-tmp/pacs/analysis/generate_summary_table.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T09:10:20.353050+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -A 20 \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -A 20 \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T09:10:20.353399+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T09:10:20.353587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T09:10:20.353786+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T09:10:20.353920+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T09:10:20.354150+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T09:10:20.354287+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis/bootstrap_per_problem.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis/bootstrap_per_problem.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T09:10:20.354597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nPer-problem non-parametric bootstrap for phase gradient CI.\\nResampling unit: problem (n=50), NOT segment.\\nMethod: percentile bootstrap, B=10000.\\n\\\"\\\"\\\"\\nimport json\\nimport argparse\\nimport numpy as np\\nfrom pathlib import Path\\n\\n\\ndef load_per_problem_ii(results_path, level_str=None):\\n    with open(results_path) as f:\\n        data = json.load(f)\\n    ppi = data[\\\"per_problem_ii\\\"]\\n    if level_str is not None:\\n        return ppi[level_str]\\n    levels = list(ppi.keys())\\n    if len(levels) == 1:\\n        return ppi[levels[0]]\\n    raise ValueError(f\\\"Multiple levels found: {levels}. Specify --level.\\\")\\n\\n\\ndef bootstrap_gradient(per_problem_ii, n_bootstrap=10000, ci_level=0.95, seed=42):\\n    rng = np.random.RandomState(seed)\\n    ii_high = np.array([p[\\\"ii_high\\\"] for p in per_problem_ii if p[\\\"ii_high\\\"] is not None])\\n    ii_mid = np.array([p[\\\"ii_mid\\\"] for p in per_problem_ii if p[\\\"ii_mid\\\"] is not None])\\n    ii_low = np.array([p[\\\"ii_low\\\"] for p in per_problem_ii if p[\\\"ii_low\\\"] is not None])\\n\\n    n = min(len(ii_high), len(ii_mid), len(ii_low))\\n    ii_high = ii_high[:n]\\n    ii_mid = ii_mid[:n]\\n    ii_low = ii_low[:n]\\n\\n    point_gradient = np.median(ii_low) / np.median(ii_high)\\n\\n    gradients = np.empty(n_bootstrap)\\n    for i in range(n_bootstrap):\\n        idx = rng.randint(0, n, size=n)\\n        med_low = np.median(ii_low[idx])\\n        med_high = np.median(ii_high[idx])\\n        gradients[i] = med_low / med_high if med_high != 0 else np.nan\\n\\n    gradients = gradients[~np.isnan(gradients)]\\n    alpha = 1 - ci_level\\n    ci_lo = np.percentile(gradients, 100 * alpha / 2)\\n    ci_hi = np.percentile(gradients, 100 * (1 - alpha / 2))\\n    p_value = float(np.mean(gradients <= 1.0))\\n\\n    return {\\n        \\\"gradient\\\": float(point_gradient),\\n        \\\"ci_low\\\": float(ci_lo)
…[truncated 5721 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T09:10:20.354805+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|n_bootstrap\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|n_bootstrap\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T09:10:20.354948+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T09:10:20.355076+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|n_bootstrap\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep \"stat_test\\|median_diff\\|bootstrap_ci\\|n_bootstrap\\|permutation\\|cohens_d\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T09:10:20.355199+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T09:10:20.355319+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis/stat_test_qw_rand.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis/stat_test_qw_rand.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T09:10:20.355697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nStatistical tests for bf16_qw_rand_s015 and bf16_qw_rand_s025.\\nReplicates the same 4-test battery done for s020.\\n\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nfrom scipy import stats\\nfrom pathlib import Path\\n\\nBASE = Path(\\\"/root/autodl-tmp/pacs\\\")\\nOUTPUT_DIR = BASE / \\\"analysis_output\\\"\\n\\nEXPERIMENTS = {\\n    \\\"bf16_qw_rand_s015\\\": {\\n        \\\"path\\\": BASE / \\\"profiling_output_bf16_qw_rand_s015\\\" / \\\"profiling_results.json\\\",\\n        \\\"sparsity\\\": 0.15,\\n        \\\"level_key\\\": \\\"0.15\\\",\\n    },\\n    \\\"bf16_qw_rand_s025\\\": {\\n        \\\"path\\\": BASE / \\\"profiling_output_bf16_qw_rand_s025\\\" / \\\"profiling_results.json\\\",\\n        \\\"sparsity\\\": 0.25,\\n        \\\"level_key\\\": \\\"0.25\\\",\\n    },\\n}\\n\\nB = 10000\\nSEED = 42\\n\\n\\ndef load_per_problem(path, level_key):\\n    with open(path) as f:\\n        data = json.load(f)\\n    ppi = data[\\\"per_problem_ii\\\"][level_key]\\n    phase_stats_raw = data[\\\"phase_stats\\\"]\\n    ii_agg = data[\\\"interaction_index\\\"]\\n    return ppi, phase_stats_raw, ii_agg\\n\\n\\ndef extract_paired(ppi):\\n    ii_high, ii_low = [], []\\n    for p in ppi:\\n        h, l = p.get(\\\"ii_high\\\"), p.get(\\\"ii_low\\\")\\n        if h is not None and l is not None:\\n            ii_high.append(h)\\n            ii_low.append(l)\\n    return np.array(ii_high), np.array(ii_low)\\n\\n\\ndef permutation_test(ii_high, ii_low, B=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    obs_diff = np.median(ii_low) - np.median(ii_high)\\n    pooled = np.concatenate([ii_high, ii_low])\\n    n_h = len(ii_high)\\n    count = 0\\n    for _ in range(B):\\n        rng.shuffle(pooled)\\n        perm_diff = np.median(pooled[n_h:]) - np.median(pooled[:n_h])\\n        if abs(perm_diff) >= abs(obs_diff):\\n            count += 1\\n    p_value = count / B\\n    return {\\\"B\\\": B, \\\
…[truncated 7326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T09:10:20.355998+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"per_problem_ii\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"per_problem_ii\" /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T09:10:20.356169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"66903:  \\\"per_problem_ii\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T09:10:20.356330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n \"per_problem_ii\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n \"per_problem_ii\" /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T09:10:20.356499+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"56901:  \\\"per_problem_ii\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T09:10:20.356740+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T09:10:20.356994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Cross-model analysis: concordance of compound interaction severity across DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct\\\",\\n  \\\"note\\\": \\\"cross-model (shared Qwen2ForCausalLM architecture), not cross-architecture\\\",\\n  \\\"importance_median_diffs\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"s015\\\": 0.392539,\\n      \\\"s020\\\": 1.481741,\\n      \\\"s025\\\": 7.163595,\\n      \\\"s030\\\": 14.586064\\n    },\\n    \\\"qwen\\\": {\\n      \\\"s015\\\": 0.038565,\\n      \\\"s020\\\": 0.234979,\\n      \\\"s025\\\": 1.267732,\\n      \\\"s030\\\": 2.943093\\n    }\\n  },\\n  \\\"random_median_diffs\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"s015\\\": 0.009572,\\n      \\\"s020\\\": -0.01555,\\n      \\\"s025\\\": 0.544512,\\n      \\\"s030\\\": 1.538314\\n    },\\n    \\\"qwen\\\": {\\n      \\\"s015\\\": 0.04971,\\n      \\\"s020\\\": 0.128948,\\n      \\\"s025\\\": 0.659798,\\n      \\\"s030\\\": 4.24103\\n    }\\n  },\\n  \\\"cohens_d_trend\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"s015\\\": 0.4416,\\n      \\\"s020\\\": 0.5195,\\n      \\\"s025\\\": 0.6831,\\n      \\\"s030\\\": 0.8031\\n    },\\n    \\\"qwen\\\": {\\n      \\\"s015\\\": 0.2811,\\n      \\\"s020\\\": 0.5494,\\n      \\\"s025\\\": 0.8894,\\n      \\\"s030\\\": 1.022\\n    },\\n    \\\"deepseek_monotonic\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    },\\n    \\\"qwen_monotonic\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    },\\n    \\\"spearman_rho\\\": 1.0,\\n    \\\"spearman_p\\\": 0.0\\n  },\\n  \\\"importance_monotonicity\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    },\\n    \\\"qwen\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    }\\n  },\\n  \\\"ran
…[truncated 3192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T09:10:20.357198+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -5 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -5 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T09:10:20.357342+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T09:10:20.357503+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "wc -l /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "wc -l /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T09:10:20.357708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"67406 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T09:10:20.358279+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -66910 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -66910 /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s030/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T09:10:20.358666+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.3\\n    ],\\n    \\\"masking_method\\\": \\\"importance\\\",\\n    \\\"head_importance_metric\\\": \\\"attention_frobenius_norm\\\",\\n    \\\"kv_importance_metric\\\": \\\"cumulative_attention_received\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.1689,\\n        \\\"attn\\\": 1.7123,\\n        \\\"kv\\\": 2.0544,\\n        \\\"both\\\": 3.2372\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.2286,\\n        \\\"attn\\\": 1.9347,\\n        \\\"kv\\\": 51.6485,\\n        \\\"both\\\": 122.609\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 1.7894,\\n        \\\"kv\\\": 9.4821,\\n        \\\"both\\\": 24.2847\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 0.554708,\\n        \\\"ci_low\\\": 0.277272,\\n        \\\"ci_high\\\": 0.919782,\\n        \\\"median\\\": 0.053399,\\n        \\\"winsorized_mean\\\": 0.336673,\\n        \\\"skewness\\\": 10.622,\\n        \\\"outlier_count\\\": 6\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.3\\\": {\\n        \\\"mean\\\": 57.794625,\\n
…[truncated 7709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T09:10:20.358901+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cat << 'PYEOF' > /root/autodl-tmp/pacs/analysis/rebootstrap_importance_b10000.py\n\"\"\"\nRe-bootstrap all 8 importance experiments with B=10000.\nComputes: median_diff, bootstrap CI, Cohen's d, permutation p-value, Wilcoxon.\n\"\"\"\nimport json\nimport numpy as np\nfrom scipy import stats\nfrom pathlib import Path\n\nBASE = Path(\"/root/autodl-tmp/pacs\")\nOUTPUT = BASE / \"analysis_output\" / \"rebootstrap_b10000_results.json\"\n\nB = 10000\nSEED = 42\n\nEXPERIMENTS = {\n    \"bf16_ds_imp_s015\": {\"path\": \"profiling_output_bf16_ds_imp_s015\", \"level\": \"0.15\", \"model\": \"DeepSeek\"},\n    \"bf16_ds_imp_s020\": {\"path\": \"profiling_output_bf16_ds_imp_s020\", \"level\": \"0.2\",  \"model\": \"DeepSeek\"},\n    \"bf16_ds_imp_s025\": {\"path\": \"profiling_output_bf16_ds_imp_s025\", \"level\": \"0.25\", \"model\": \"DeepSeek\"},\n    \"bf16_ds_imp_s030\": {\"path\": \"profiling_output_bf16_ds_imp_s030\", \"level\": \"0.3\",  \"model\": \"DeepSeek\"},\n    \"bf16_qw_imp_s015\": {\"path\": \"profiling_output_bf16_qw_imp_s015\", \"level\": \"0.15\", \"model\": \"Qwen\"},\n    \"bf16_qw_imp_s020\": {\"path\": \"profiling_output_bf16_qw_imp_s020\", \"level\": \"0.2\",  \"model\": \"Qwen\"},\n    \"bf16_qw_imp_s025\": {\"path\": \"profiling_output_bf16_qw_imp_s025\", \"level\": \"0.25\", \"model\": \"Qwen\"},\n    \"bf16_qw_imp_s030\": {\"path\": \"profiling_output_bf16_qw_imp_s030\", \"level\": \"0.3\",  \"model\": \"Qwen\"},\n}\n\n\ndef load_paired(path, level):\n    with open(path) as f:\n        data = json.load(f)\n    old_B = data[\"config\"].get(\"n_bootstrap\", \"unknown\")\n    ppi = data[\"per_problem_ii\"][level]\n    ii_high, ii_low = [], []\n    for p in ppi:\n        h, l = p.get(\"ii_high\"), p.get(\"ii_low\")\n        if h is not None and l is not None:\n            ii_high.append(h)\n            ii_low.append(l)\n    return np.array(ii_high), np.array(ii_low), old_B\n\n\ndef permutation_test(ii_high, ii_low, B=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    obs = np.median(ii_low) - np.median(ii_high)\n    pooled = np.concatenate([ii_high, ii_low])\n    n_h = len(ii_high)\n    count = 0\n    for _ in range(B):\n        rng.shuffle(pooled)\n        d = np.median(pooled[n_h:]) - np.median(pooled[:n_h])\n        if abs(d) >= abs(obs):\n            count += 1\n    return round(count / B, 6)\n\n\ndef bootstrap_ci(ii_high, ii_low, B=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = min(len(ii_high), len(ii_low))\n    diffs = np.empty(B)\n    for i in range(B):\n        idx_h = rng.randint(0, len(ii_high), size=n)\n        idx_l = rng.randint(0, len(ii_low), size=n)\n        diffs[i] = np.median(ii_low[idx_l]) - np.median(ii_high[idx_h])\n    return round(float(np.percentile(diffs, 2.5)), 6), round(float(np.percentile(diffs, 97.5)), 6)\n\n\ndef cohens_d(ii_high, ii_low):\n    n1, n2 = len(ii_low), len(ii_high)\n    s1, s2 = np.std(ii_low, ddof=1), np.std(ii_high, ddof=1)\n    pooled_std = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n    return round(float((np.mean(ii_low) - np.mean(ii_high)) / pooled_std), 6) if pooled_std > 0 else 0.0\n\n\ndef main():\n    results = {}\n    print(f\"{'Experiment':<22} {'Old B':<8} {'median_diff':<14} {'perm_p':<10} {'cohen_d':<10} {'CI_low':<12} {'CI_high':<12} {'wilcox_p':<12}\")\n    print(\"-\" * 110)\n\n    for exp_id, cfg in EXPERIMENTS.items():\n        fpath = BASE / cfg[\"path\"] / \"profiling_results.json\"\n        if not fpath.exists():\n            print(f\"{exp_id:<22} NOT FOUND\")\n            continue\n\n        ii_high, ii_low, old_B = load_paired(str(fpath), cfg[\"level\"])\n        n_paired = len(ii_high)\n\n        med_diff = round(float(np.median(ii_low) - np.median(ii_high)), 6)\n        perm_p = permutation_test(ii_high, ii_low, B=B, seed=SEED)\n        ci_lo, ci_hi = bootstrap_ci(ii_high, ii_low, B=B, seed=SEED)\n        cd = cohens_d(ii_high, ii_low)\n\n        n = min(len(ii_high), len(ii_low))\n        wt = stats.wilcoxon(ii_low[:n], ii_high[:n], alternative='two-sided')\n        wilcox_p = round(float(wt.pvalue), 6)\n\n        print(f\"{exp_id:<22} {old_B:<8} {med_diff:<14.6f} {perm_p:<10.4f} {cd:<10.4f} {ci_lo:<12.6f} {ci_hi:<12.6f} {wilcox_p:<12.6f}\")\n\n        results[exp_id] = {\n            \"model\": cfg[\"model\"],\n            \"sparsity\": cfg[\"level\"],\n            \"old_n_bootstrap\": old_B,\n            \"new_n_bootstrap\": B,\n            \"n_paired\": n_paired,\n            \"median_diff\": med_diff,\n            \"permutation_p\": perm_p,\n            \"cohens_d\": cd,\n            \"bootstrap_ci_95\": [ci_lo, ci_hi],\n            \"wilcoxon_p\": wilcox_p,\n        }\n\n    OUTPUT.parent.mkdir(parents=True, exist_ok=True)\n    with open(OUTPUT, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nResults saved to {OUTPUT}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat << 'PYEOF' > /root/autodl-tmp/pacs/analysis/rebootstrap_importance_b10000.py\n\"\"\"\nRe-bootstrap all 8 importance experiments with B=10000.\nComputes: median_diff, bootstrap CI, Cohen's d, permutation p-value, Wilcoxon.\n\"\"\"\nimport json\nimport numpy as np\nfrom scipy import stats\nfrom pathlib import Path\n\nBASE = Path(\"/root/autodl-tmp/pacs\")\nOUTPUT = BASE / \"analysis_output\" / \"rebootstrap_b10000_results.json\"\n\nB = 10000\nSEED = 42\n\nEXPERIMENTS = {\n    \"bf16_ds_imp_s015\": {\"path\": \"profiling_output_bf16_ds_imp_s015\", \"level\": \"0.15\", \"model\": \"DeepSeek\"},\n    \"bf16_ds_imp_s020\": {\"path\": \"profiling_output_bf16_ds_imp_s020\", \"level\": \"0.2\",  \"model\": \"DeepSeek\"},\n    \"bf16_ds_imp_s025\": {\"path\": \"profiling_output_bf16_ds_imp_s025\", \"level\": \"0.25\", \"model\": \"DeepSeek\"},\n    \"bf16_ds_imp_s030\": {\"path\": \"profiling_output_bf16_ds_imp_s030\", \"level\": \"0.3\",  \"model\": \"DeepSeek\"},\n    \"bf16_qw_imp_s015\": {\"path\": \"profiling_output_bf16_qw_imp_s015\", \"level\": \"0.15\", \"model\": \"Qwen\"},\n    \"bf16_qw_imp_s020\": {\"path\": \"profiling_output_bf16_qw_imp_s020\", \"level\": \"0.2\",  \"model\": \"Qwen\"},\n    \"bf16_qw_imp_s025\": {\"path\": \"profiling_output_bf16_qw_imp_s025\", \"level\": \"0.25\", \"model\": \"Qwen\"},\n    \"bf16_qw_imp_s030\": {\"path\": \"profiling_output_bf16_qw_imp_s030\", \"level\": \"0.3\",  \"model\": \"Qwen\"},\n}\n\n\ndef load_paired(path, level):\n    with open(path) as f:\n        data = json.load(f)\n    old_B = data[\"config\"].get(\"n_bootstrap\", \"unknown\")\n    ppi = data[\"per_problem_ii\"][level]\n    ii_high, ii_low = [], []\n    for p in ppi:\n        h, l = p.get(\"ii_high\"), p.get(\"ii_low\")\n        if h is not None and l is not None:\n            ii_high.append(h)\n            ii_low.append(l)\n    return np.array(ii_high), np.array(ii_low), old_B\n\n\ndef permutation_test(ii_high, ii_low, B=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    obs = np.median(ii_low) - np.median(ii_high)\n    pooled = np.concatenate([ii_high, ii_low])\n    n_h = len(ii_high)\n    count = 0\n    for _ in range(B):\n        rng.shuffle(pooled)\n        d = np.median(pooled[n_h:]) - np.median(pooled[:n_h])\n        if abs(d) >= abs(obs):\n            count += 1\n    return round(count / B, 6)\n\n\ndef bootstrap_ci(ii_high, ii_low, B=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = min(len(ii_high), len(ii_low))\n    diffs = np.empty(B)\n    for i in range(B):\n        idx_h = rng.randint(0, len(ii_high), size=n)\n        idx_l = rng.randint(0, len(ii_low), size=n)\n        diffs[i] = np.median(ii_low[idx_l]) - np.median(ii_high[idx_h])\n    return round(float(np.percentile(diffs, 2.5)), 6), round(float(np.percentile(diffs, 97.5)), 6)\n\n\ndef cohens_d(ii_high, ii_low):\n    n1, n2 = len(ii_low), len(ii_high)\n    s1, s2 = np.std(ii_low, ddof=1), np.std(ii_high, ddof=1)\n    pooled_std = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n    return round(float((np.mean(ii_low) - np.mean(ii_high)) / pooled_std), 6) if pooled_std > 0 else 0.0\n\n\ndef main():\n    results = {}\n    print(f\"{'Experiment':<22} {'Old B':<8} {'median_diff':<14} {'perm_p':<10} {'cohen_d':<10} {'CI_low':<12} {'CI_high':<12} {'wilcox_p':<12}\")\n    print(\"-\" * 110)\n\n    for exp_id, cfg in EXPERIMENTS.items():\n        fpath = BASE / cfg[\"path\"] / \"profiling_results.json\"\n        if not fpath.exists():\n            print(f\"{exp_id:<22} NOT FOUND\")\n            continue\n\n        ii_high, ii_low, old_B = load_paired(str(fpath), cfg[\"level\"])\n        n_paired = len(ii_high)\n\n        med_diff = round(float(np.median(ii_low) - np.median(ii_high)), 6)\n        perm_p = permutation_test(ii_high, ii_low, B=B, seed=SEED)\n        ci_lo, ci_hi = bootstrap_ci(ii_high, ii_low, B=B, seed=SEED)\n        cd = cohens_d(ii_high, ii_low)\n\n        n = min(len(ii_high), len(ii_low))\n        wt = stats.wilcoxon(ii_low[:n], ii_high[:n], alternative='two-sided')\n        wilcox_p = round(float(wt.pvalue), 6)\n\n        print(f\"{exp_id:<22} {old_B:<8} {med_diff:<14.6f} {perm_p:<10.4f} {cd:<10.4f} {ci_lo:<12.6f} {ci_hi:<12.6f} {wilcox_p:<12.6f}\")\n\n        results[exp_id] = {\n            \"model\": cfg[\"model\"],\n            \"sparsity\": cfg[\"level\"],\n            \"old_n_bootstrap\": old_B,\n            \"new_n_bootstrap\": B,\n            \"n_paired\": n_paired,\n            \"median_diff\": med_diff,\n            \"permutation_p\": perm_p,\n            \"cohens_d\": cd,\n            \"bootstrap_ci_95\": [ci_lo, ci_hi],\n            \"wilcoxon_p\": wilcox_p,\n        }\n\n    OUTPUT.parent.mkdir(parents=True, exist_ok=True)\n    with open(OUTPUT, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nResults saved to {OUTPUT}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T09:10:20.359086+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T09:10:20.359231+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python analysis/rebootstrap_importance_b10000.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python analysis/rebootstrap_importance_b10000.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T09:10:20.359378+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Experiment             Old B    median_diff    perm_p     cohen_d    CI_low       CI_high      wilcox_p    \\n--------------------------------------------------------------------------------------------------------------\\nbf16_ds_imp_s015       1000     0.323579       0.0000     0.6068     0.198824     0.471566     0.000000    \\nbf16_ds_imp_s020       1000     1.152020       0.0000     0.7250     0.655454     1.256001     0.000000    \\nbf16_ds_imp_s025       1000     3.968568       0.0000     0.9534     2.829037     5.291756     0.000000    \\nbf16_ds_imp_s030       1000     9.943595       0.0000     1.1263     8.391554     16.652865    0.000000    \\nbf16_qw_imp_s015       1000     0.047619       0.0001     0.3705     -0.005077    0.109517     0.029580    \\nbf16_qw_imp_s020       1000     0.207511       0.0000     0.7224     0.067222     0.402260     0.000034    \\nbf16_qw_imp_s025       1000     1.108706       0.0000     1.2329     0.609247     1.469002     0.000000    \\nbf16_qw_imp_s030       1000     2.619385       0.0000     1.4394     1.722281     3.651063     0.000000    \\n\\nResults saved to /root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T09:10:20.359598+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\np = '/root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json'\nwith open(p) as f:\n    d = json.load(f)\nold = d['random_median_diffs']['qwen']['s030']\nd['random_median_diffs']['qwen']['s030'] = 2.418272\nwith open(p, 'w') as f:\n    json.dump(d, f, indent=2)\nprint(f'Fixed: {old} -> 2.418272')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\np = '/root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json'\nwith open(p) as f:\n    d = json.load(f)\nold = d['random_median_diffs']['qwen']['s030']\nd['random_median_diffs']['qwen']['s030'] = 2.418272\nwith open(p, 'w') as f:\n    json.dump(d, f, indent=2)\nprint(f'Fixed: {old} -> 2.418272')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T09:10:20.359742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fixed: 4.24103 -> 2.418272\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T09:10:20.359917+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_ds_imp_s015",
  "field": "metrics",
  "value": "{'median_difference': 0.323579, 'permutation_p': 0, 'cohens_d': 0.6068, 'bootstrap_ci_95': [0.198824, 0.471566], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_ds_imp_s015",
    "field": "metrics",
    "value": "{'median_difference': 0.323579, 'permutation_p': 0, 'cohens_d': 0.6068, 'bootstrap_ci_95': [0.198824, 0.471566], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T09:10:20.360088+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_ds_imp_s015\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:24.195Z\", \"updated_at\": \"2026-05-14T09:08:51.789Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.15, bf16 dtype. 核心 claim 数据源——论文所有数值来自此批实验。\", \"notes\": \"已被 bf16_importance_s015 覆盖（DONE, success）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:00.792Z\", \"metrics\": {\"median_difference\": 0.323579, \"permutation_p\": 0, \"cohens_d\": 0.6068, \"bootstrap_ci_95\": [0.198824, 0.471566], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.139}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T09:10:20.360273+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_ds_imp_s020",
  "field": "metrics",
  "value": "{'median_difference': 1.15202, 'permutation_p': 0, 'cohens_d': 0.725, 'bootstrap_ci_95': [0.655454, 1.256001], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_ds_imp_s020",
    "field": "metrics",
    "value": "{'median_difference': 1.15202, 'permutation_p': 0, 'cohens_d': 0.725, 'bootstrap_ci_95': [0.655454, 1.256001], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T09:10:20.360480+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_ds_imp_s020\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:25.159Z\", \"updated_at\": \"2026-05-14T09:08:53.208Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.20, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s020 覆盖（RUNNING, cuda:0）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:01.901Z\", \"metrics\": {\"median_difference\": 1.15202, \"permutation_p\": 0, \"cohens_d\": 0.725, \"bootstrap_ci_95\": [0.655454, 1.256001], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9453}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T09:10:20.360671+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_ds_imp_s025",
  "field": "metrics",
  "value": "{'median_difference': 3.968568, 'permutation_p': 0, 'cohens_d': 0.9534, 'bootstrap_ci_95': [2.829037, 5.291756], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_ds_imp_s025",
    "field": "metrics",
    "value": "{'median_difference': 3.968568, 'permutation_p': 0, 'cohens_d': 0.9534, 'bootstrap_ci_95': [2.829037, 5.291756], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T09:10:20.360825+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_ds_imp_s030",
  "field": "metrics",
  "value": "{'median_difference': 9.943595, 'permutation_p': 0, 'cohens_d': 1.1263, 'bootstrap_ci_95': [8.391554, 16.652865], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_ds_imp_s030",
    "field": "metrics",
    "value": "{'median_difference': 9.943595, 'permutation_p': 0, 'cohens_d': 1.1263, 'bootstrap_ci_95': [8.391554, 16.652865], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 49}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T09:10:20.360980+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_ds_imp_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:26.099Z\", \"updated_at\": \"2026-05-14T09:08:54.982Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.25, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s025 覆盖（DONE, success）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:04.011Z\", \"metrics\": {\"median_difference\": 3.968568, \"permutation_p\": 0, \"cohens_d\": 0.9534, \"bootstrap_ci_95\": [2.829037, 5.291756], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T09:10:20.361122+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_imp_s015",
  "field": "metrics",
  "value": "{'median_difference': 0.047619, 'permutation_p': 0.0001, 'cohens_d': 0.3705, 'bootstrap_ci_95': [-0.005077, 0.109517], 'wilcoxon_p': 0.02958, 'n_bootstrap': 10000, 'n_paired': 46}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_imp_s015",
    "field": "metrics",
    "value": "{'median_difference': 0.047619, 'permutation_p': 0.0001, 'cohens_d': 0.3705, 'bootstrap_ci_95': [-0.005077, 0.109517], 'wilcoxon_p': 0.02958, 'n_bootstrap': 10000, 'n_paired': 46}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-14T09:10:20.361278+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_ds_imp_s030\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:27.121Z\", \"updated_at\": \"2026-05-14T09:08:57.400Z\", \"hypothesis\": \"D020 bf16 全量重跑: DeepSeek-R1-Distill-Qwen-7B importance masking s=0.30, bf16 dtype. 核心 claim 数据源。\", \"notes\": \"已被 bf16_importance_s030 覆盖（RUNNING, cuda:0）。本 ID 不再单独跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:39:05.479Z\", \"metrics\": {\"median_difference\": 9.943595, \"permutation_p\": 0, \"cohens_d\": 1.1263, \"bootstrap_ci_95\": [8.391554, 16.652865], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 49}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5698}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T09:10:20.361517+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_imp_s015\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T05:39:31.289Z\", \"updated_at\": \"2026-05-14T09:09:00.065Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.15, bf16 dtype. Cross-model replication。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T07:01:46.764Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015 --sparsity_levels 0.15 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"code_commit\": \"5488041765f165e4e64323cfda552de868351f86\", \"finished_at\": \"2026-05-14T07:01:57.332Z\", \"training_hours\": 0.0}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T07:01:59.250Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:02:01.732372+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Qwen2.5-7B-Instruct checkpoint not found on server, 待下载后重跑\"}}, \"notes\": \"Qwen2.5-7B importance s=0.15, PASS. Median II gradient: high≈0.001 → mid≈-0.011 → low≈0.039. PPL(both): high=1.31 → mid=2.20 → low=5.44. CI non-overlapping (high vs low). 弱 gradient，与 DeepSeek 在 s=0.15 趋势一致。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.15 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_nam
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-14T09:10:20.361732+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_imp_s020",
  "field": "metrics",
  "value": "{'median_difference': 0.207511, 'permutation_p': 0, 'cohens_d': 0.7224, 'bootstrap_ci_95': [0.067222, 0.40226], 'wilcoxon_p': 3.4e-05, 'n_bootstrap': 10000, 'n_paired': 46}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_imp_s020",
    "field": "metrics",
    "value": "{'median_difference': 0.207511, 'permutation_p': 0, 'cohens_d': 0.7224, 'bootstrap_ci_95': [0.067222, 0.40226], 'wilcoxon_p': 3.4e-05, 'n_bootstrap': 10000, 'n_paired': 46}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-14T09:10:20.361892+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_imp_s025",
  "field": "metrics",
  "value": "{'median_difference': 1.108706, 'permutation_p': 0, 'cohens_d': 1.2329, 'bootstrap_ci_95': [0.609247, 1.469002], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 46}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_imp_s025",
    "field": "metrics",
    "value": "{'median_difference': 1.108706, 'permutation_p': 0, 'cohens_d': 1.2329, 'bootstrap_ci_95': [0.609247, 1.469002], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 46}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-14T09:10:20.362107+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_imp_s030",
  "field": "metrics",
  "value": "{'median_difference': 2.619385, 'permutation_p': 0, 'cohens_d': 1.4394, 'bootstrap_ci_95': [1.722281, 3.651063], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 46}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_imp_s030",
    "field": "metrics",
    "value": "{'median_difference': 2.619385, 'permutation_p': 0, 'cohens_d': 1.4394, 'bootstrap_ci_95': [1.722281, 3.651063], 'wilcoxon_p': 0, 'n_bootstrap': 10000, 'n_paired': 46}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-14T09:10:20.362608+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_imp_s020\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T05:39:31.824Z\", \"updated_at\": \"2026-05-14T09:09:03.210Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.20, bf16 dtype. Cross-model replication。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T07:01:50.969Z\", \"finished_at\": \"2026-05-14T07:02:06.576Z\", \"training_hours\": 0.0}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T07:02:11.652Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:02:16.508561+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Qwen2.5-7B-Instruct checkpoint not found on server, 待下载后重跑\"}}, \"notes\": \"Qwen2.5-7B importance s=0.20, PASS. Median II gradient: high≈-0.000 → mid≈0.002 → low≈0.235. PPL(both): high=1.37 → mid=3.43 → low=9.20. CI non-overlapping (low vs mid). Low phase II 明显抬升，PPL gradient 加剧。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.20 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s020\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s020.log\", \"metrics\": {\"median_difference\": 0.207511, \"permutation_p\": 0, \"cohens_d\": 0.7224, \"bootstrap_ci_95\": [0.067222, 0.40226], \"wilcoxon_p\": 3.4e-05, \"n_bootstrap\": 10000, \"n_paired\": 46}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0988}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-14T09:10:20.362814+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_imp_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T05:39:32.680Z\", \"updated_at\": \"2026-05-14T09:09:07.649Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.25, bf16 dtype. Cross-model replication。\", \"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-22162\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T07:01:54.691Z\", \"finished_at\": \"2026-05-14T07:02:51.598Z\", \"training_hours\": 0.02}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T07:02:55.553Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:02:58.934095+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Qwen2.5-7B-Instruct checkpoint not found on server, 待下载后重跑\"}}, \"notes\": \"Qwen2.5-7B importance s=0.25, PASS. Median II gradient: high≈0.003 → mid≈0.114 → low≈1.271. PPL(both): high=1.54 → mid=5.36 → low=16.96. CI non-overlapping (low vs mid). 强 gradient，mid phase 开始显著。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.25 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s025\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s025.log\", \"metrics\": {\"median_difference\": 1.108706, \"permutation_p\": 0, \"cohens_d\": 1.2329, \"bootstrap_ci_95\": [0.609247, 1.469002], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.816}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-14T09:10:20.362992+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_imp_s030\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:33.640Z\", \"updated_at\": \"2026-05-14T09:09:09.394Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct importance masking s=0.30, bf16 dtype. Cross-model replication。\", \"spec\": {\"command\": \"python -m pacs.profiling.run_profiling --model_path checkpoints/Qwen2.5-7B-Instruct --sparsity_levels 0.30 --masking_method importance --max_problems 50\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_imp_s030.log\", \"metrics\": {\"median_difference\": 2.619385, \"permutation_p\": 0, \"cohens_d\": 1.4394, \"bootstrap_ci_95\": [1.722281, 3.651063], \"wilcoxon_p\": 0, \"n_bootstrap\": 10000, \"n_paired\": 46}, \"notes\": \"Qwen2.5-7B importance s=0.30, PASS. Median II gradient: high≈0.010 → mid≈0.688 → low≈2.953. PPL(both): high=1.86 → mid=9.48 → low=35.32. CI non-overlapping (low vs mid). 最强 gradient，完全复现 DeepSeek 模式。\", \"completed_at\": \"2026-05-14T07:58:16.426Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9821}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-14T09:10:20.363188+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "rebootstrap_b10000_results",
  "type": "data",
  "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030). Per-problem paired bootstrap with median_diff, permutation p, Cohen's d, 95% CI, Wilcoxon p.",
  "project": "phase-gated-compound-sparse",
  "source_path": "/root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json",
  "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "rebootstrap_b10000_results",
    "type": "data",
    "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030). Per-problem paired bootstrap with median_diff, permutation p, Cohen's d, 95% CI, Wilcoxon p.",
    "project": "phase-gated-compound-sparse",
    "source_path": "/root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json",
    "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-14T09:10:20.363553+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-14T09:10:20.363753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-14T09:10:20.363993+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"bf16_ds_imp_s015\\\": {\\n    \\\"model\\\": \\\"DeepSeek\\\",\\n    \\\"sparsity\\\": \\\"0.15\\\",\\n    \\\"old_n_bootstrap\\\": 1000,\\n    \\\"new_n_bootstrap\\\": 10000,\\n    \\\"n_paired\\\": 49,\\n    \\\"median_diff\\\": 0.323579,\\n    \\\"permutation_p\\\": 0.0,\\n    \\\"cohens_d\\\": 0.606769,\\n    \\\"bootstrap_ci_95\\\": [\\n      0.198824,\\n      0.471566\\n    ],\\n    \\\"wilcoxon_p\\\": 0.0\\n  },\\n  \\\"bf16_ds_imp_s020\\\": {\\n    \\\"model\\\": \\\"DeepSeek\\\",\\n    \\\"sparsity\\\": \\\"0.2\\\",\\n    \\\"old_n_bootstrap\\\": 1000,\\n    \\\"new_n_bootstrap\\\": 10000,\\n    \\\"n_paired\\\": 49,\\n    \\\"median_diff\\\": 1.15202,\\n    \\\"permutation_p\\\": 0.0,\\n    \\\"cohens_d\\\": 0.725045,\\n    \\\"bootstrap_ci_95\\\": [\\n      0.655454,\\n      1.256001\\n    ],\\n    \\\"wilcoxon_p\\\": 0.0\\n  },\\n  \\\"bf16_ds_imp_s025\\\": {\\n    \\\"model\\\": \\\"DeepSeek\\\",\\n    \\\"sparsity\\\": \\\"0.25\\\",\\n    \\\"old_n_bootstrap\\\": 1000,\\n    \\\"new_n_bootstrap\\\": 10000,\\n    \\\"n_paired\\\": 49,\\n    \\\"median_diff\\\": 3.968568,\\n    \\\"permutation_p\\\": 0.0,\\n    \\\"cohens_d\\\": 0.953449,\\n    \\\"bootstrap_ci_95\\\": [\\n      2.829037,\\n      5.291756\\n    ],\\n    \\\"wilcoxon_p\\\": 0.0\\n  },\\n  \\\"bf16_ds_imp_s030\\\": {\\n    \\\"model\\\": \\\"DeepSeek\\\",\\n    \\\"sparsity\\\": \\\"0.3\\\",\\n    \\\"old_n_bootstrap\\\": 1000,\\n    \\\"new_n_bootstrap\\\": 10000,\\n    \\\"n_paired\\\": 49,\\n    \\\"median_diff\\\": 9.943595,\\n    \\\"permutation_p\\\": 0.0,\\n    \\\"cohens_d\\\": 1.126291,\\n    \\\"bootstrap_ci_95\\\": [\\n      8.391554,\\n      16.652865\\n    ],\\n    \\\"wilcoxon_p\\\": 0.0\\n  },\\n  \\\"bf16_qw_imp_s015\\\": {\\n    \\\"model\\\": \\\"Qwen\\\",\\n    \\\"sparsity\\\": \\\"0.15\\\",\\n    \\\"old_n_bootstrap\\\": 1000,\\n    \\\"new_n_bootstrap\\\": 10000,\\n    \\\"n_paired\\\": 46,\\n    \\\"me
…[truncated 1602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-14T09:10:20.364251+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "rebootstrap_b10000_results",
  "type": "data",
  "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030). Per-problem paired bootstrap with median_diff, permutation p, Cohen's d, 95% CI, Wilcoxon p.",
  "project": "phase-gated-compound-sparse",
  "content": "{\"bf16_ds_imp_s015\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":0.323579,\"permutation_p\":0.0,\"cohens_d\":0.606769,\"bootstrap_ci_95\":[0.198824,0.471566],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s020\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":1.15202,\"permutation_p\":0.0,\"cohens_d\":0.725045,\"bootstrap_ci_95\":[0.655454,1.256001],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s025\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":3.968568,\"permutation_p\":0.0,\"cohens_d\":0.953449,\"bootstrap_ci_95\":[2.829037,5.291756],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s030\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":9.943595,\"permutation_p\":0.0,\"cohens_d\":1.126291,\"bootstrap_ci_95\":[8.391554,16.652865],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s015\":{\"model\":\"Qwen\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.047619,\"permutation_p\":0.0001,\"cohens_d\":0.37054,\"bootstrap_ci_95\":[-0.005077,0.109517],\"wilcoxon_p\":0.02958},\"bf16_qw_imp_s020\":{\"model\":\"Qwen\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.207511,\"permutation_p\":0.0,\"cohens_d\":0.722424,\"bootstrap_ci_95\":[0.067222,0.40226],\"wilcoxon_p\":3.4e-05},\"bf16_qw_imp_s025\":{\"model\":\"Qwen\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":1.108706,\"permutation_p\":0.0,\"cohens_d\":1.232921,\"bootstrap_ci_95\":[0.609247,1.469002],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s030\":{\"model\":\"Qwen\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":2.619385,\"permutation_p\":0.0,\"cohens_d\":1.439424,\"bootstrap_ci_95\":[1.722281,3.651063],\"wilcoxon_p\":0.0}}",
  "content_filename": "rebootstrap_b10000_results.json",
  "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "rebootstrap_b10000_results",
    "type": "data",
    "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030). Per-problem paired bootstrap with median_diff, permutation p, Cohen's d, 95% CI, Wilcoxon p.",
    "project": "phase-gated-compound-sparse",
    "content": "{\"bf16_ds_imp_s015\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":0.323579,\"permutation_p\":0.0,\"cohens_d\":0.606769,\"bootstrap_ci_95\":[0.198824,0.471566],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s020\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":1.15202,\"permutation_p\":0.0,\"cohens_d\":0.725045,\"bootstrap_ci_95\":[0.655454,1.256001],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s025\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":3.968568,\"permutation_p\":0.0,\"cohens_d\":0.953449,\"bootstrap_ci_95\":[2.829037,5.291756],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s030\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":9.943595,\"permutation_p\":0.0,\"cohens_d\":1.126291,\"bootstrap_ci_95\":[8.391554,16.652865],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s015\":{\"model\":\"Qwen\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.047619,\"permutation_p\":0.0001,\"cohens_d\":0.37054,\"bootstrap_ci_95\":[-0.005077,0.109517],\"wilcoxon_p\":0.02958},\"bf16_qw_imp_s020\":{\"model\":\"Qwen\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.207511,\"permutation_p\":0.0,\"cohens_d\":0.722424,\"bootstrap_ci_95\":[0.067222,0.40226],\"wilcoxon_p\":3.4e-05},\"bf16_qw_imp_s025\":{\"model\":\"Qwen\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":1.108706,\"permutation_p\":0.0,\"cohens_d\":1.232921,\"bootstrap_ci_95\":[0.609247,1.469002],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s030\":{\"model\":\"Qwen\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":2.619385,\"permutation_p\":0.0,\"cohens_d\":1.439424,\"bootstrap_ci_95\":[1.722281,3.651063],\"wilcoxon_p\":0.0}}",
    "content_filename": "rebootstrap_b10000_results.json",
    "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-14T09:10:20.364451+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'bf16_ds_imp_s015': {'mo...63], 'wilcoxon_p': 0.0}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-14T09:10:20.364611+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "rebootstrap_b10000_results",
  "type": "data",
  "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030). Per-problem paired bootstrap with median_diff, permutation p, Cohen d, 95% CI, Wilcoxon p.",
  "project": "phase-gated-compound-sparse",
  "content": "{\"bf16_ds_imp_s015\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":0.323579,\"permutation_p\":0.0,\"cohens_d\":0.606769,\"bootstrap_ci_95\":[0.198824,0.471566],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s020\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":1.15202,\"permutation_p\":0.0,\"cohens_d\":0.725045,\"bootstrap_ci_95\":[0.655454,1.256001],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s025\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":3.968568,\"permutation_p\":0.0,\"cohens_d\":0.953449,\"bootstrap_ci_95\":[2.829037,5.291756],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s030\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":9.943595,\"permutation_p\":0.0,\"cohens_d\":1.126291,\"bootstrap_ci_95\":[8.391554,16.652865],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s015\":{\"model\":\"Qwen\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.047619,\"permutation_p\":0.0001,\"cohens_d\":0.37054,\"bootstrap_ci_95\":[-0.005077,0.109517],\"wilcoxon_p\":0.02958},\"bf16_qw_imp_s020\":{\"model\":\"Qwen\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.207511,\"permutation_p\":0.0,\"cohens_d\":0.722424,\"bootstrap_ci_95\":[0.067222,0.40226],\"wilcoxon_p\":3.4e-05},\"bf16_qw_imp_s025\":{\"model\":\"Qwen\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":1.108706,\"permutation_p\":0.0,\"cohens_d\":1.232921,\"bootstrap_ci_95\":[0.609247,1.469002],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s030\":{\"model\":\"Qwen\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":2.619385,\"permutation_p\":0.0,\"cohens_d\":1.439424,\"bootstrap_ci_95\":[1.722281,3.651063],\"wilcoxon_p\":0.0}}",
  "content_filename": "rebootstrap_b10000_results.json",
  "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "rebootstrap_b10000_results",
    "type": "data",
    "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030). Per-problem paired bootstrap with median_diff, permutation p, Cohen d, 95% CI, Wilcoxon p.",
    "project": "phase-gated-compound-sparse",
    "content": "{\"bf16_ds_imp_s015\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":0.323579,\"permutation_p\":0.0,\"cohens_d\":0.606769,\"bootstrap_ci_95\":[0.198824,0.471566],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s020\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":1.15202,\"permutation_p\":0.0,\"cohens_d\":0.725045,\"bootstrap_ci_95\":[0.655454,1.256001],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s025\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":3.968568,\"permutation_p\":0.0,\"cohens_d\":0.953449,\"bootstrap_ci_95\":[2.829037,5.291756],\"wilcoxon_p\":0.0},\"bf16_ds_imp_s030\":{\"model\":\"DeepSeek\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":49,\"median_diff\":9.943595,\"permutation_p\":0.0,\"cohens_d\":1.126291,\"bootstrap_ci_95\":[8.391554,16.652865],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s015\":{\"model\":\"Qwen\",\"sparsity\":\"0.15\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.047619,\"permutation_p\":0.0001,\"cohens_d\":0.37054,\"bootstrap_ci_95\":[-0.005077,0.109517],\"wilcoxon_p\":0.02958},\"bf16_qw_imp_s020\":{\"model\":\"Qwen\",\"sparsity\":\"0.2\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":0.207511,\"permutation_p\":0.0,\"cohens_d\":0.722424,\"bootstrap_ci_95\":[0.067222,0.40226],\"wilcoxon_p\":3.4e-05},\"bf16_qw_imp_s025\":{\"model\":\"Qwen\",\"sparsity\":\"0.25\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":1.108706,\"permutation_p\":0.0,\"cohens_d\":1.232921,\"bootstrap_ci_95\":[0.609247,1.469002],\"wilcoxon_p\":0.0},\"bf16_qw_imp_s030\":{\"model\":\"Qwen\",\"sparsity\":\"0.3\",\"old_n_bootstrap\":1000,\"new_n_bootstrap\":10000,\"n_paired\":46,\"median_diff\":2.619385,\"permutation_p\":0.0,\"cohens_d\":1.439424,\"bootstrap_ci_95\":[1.722281,3.651063],\"wilcoxon_p\":0.0}}",
    "content_filename": "rebootstrap_b10000_results.json",
    "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-14T09:10:20.364762+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'bf16_ds_imp_s015': {'mo...63], 'wilcoxon_p': 0.0}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-14T09:10:20.364901+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "rebootstrap_b10000_results",
  "type": "data",
  "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030)",
  "project": "phase-gated-compound-sparse",
  "content": "See server file: /root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json. All 8 importance experiments re-bootstrapped from B=1000 to B=10000 with per-problem paired bootstrap. All significant (p<0.05) except qw_imp_s015 CI marginally crosses zero.",
  "content_filename": "rebootstrap_b10000_results.json",
  "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "rebootstrap_b10000_results",
    "type": "data",
    "description": "Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030)",
    "project": "phase-gated-compound-sparse",
    "content": "See server file: /root/autodl-tmp/pacs/analysis_output/rebootstrap_b10000_results.json. All 8 importance experiments re-bootstrapped from B=1000 to B=10000 with per-problem paired bootstrap. All significant (p<0.05) except qw_imp_s015 CI marginally crosses zero.",
    "content_filename": "rebootstrap_b10000_results.json",
    "tags": "['bootstrap', 'importance', 'B10000', 'stat-test']"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-14T09:10:20.365050+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_ee5cb7\", \"name\": \"rebootstrap_b10000_results\", \"type\": \"data\", \"description\": \"Re-bootstrap B=10000 results for all 8 importance experiments (DeepSeek + Qwen, s015-s030)\", \"path\": \"projects/phase-gated-compound-sparse/artifacts/_project/data/rebootstrap_b10000_results.json\", \"url\": null, \"project\": \"phase-gated-compound-sparse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T09:10:04.117679+00:00\", \"tags\": [\"bootstrap\", \"importance\", \"B10000\", \"stat-test\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 97 · 2026-05-14T09:10:20.365225+00:00_

全部完成。总结：

### Part A: 检查结果
- 8 个 importance 实验目录全部存在（`profiling_output_bf16_ds_imp_s015~s030` + `bf16_qw_imp_s015~s030`）
- 每个 `profiling_results.json` 都有 per-problem raw data（`ii_high`, `ii_low`）
- 原始 `n_bootstrap = 1000`

### Part B: Re-bootstrap B=10000 结果

| 实验 | median_diff | perm_p | Cohen's d | 95% CI | wilcox_p |
|---|---|---|---|---|---|
| ds_imp_s015 | 0.3236 | 0.0000 | 0.607 | [0.199, 0.472] | 0.000 |
| ds_imp_s020 | 1.1520 | 0.0000 | 0.725 | [0.655, 1.256] | 0.000 |
| ds_imp_s025 | 3.9686 | 0.0000 | 0.953 | [2.829, 5.292] | 0.000 |
| ds_imp_s030 | 9.9436 | 0.0000 | 1.126 | [8.392, 16.653] | 0.000 |
| qw_imp_s015 | 0.0476 | 0.0001 | 0.371 | [-0.005, 0.110] | 0.030 |
| qw_imp_s020 | 0.2075 | 0.0000 | 0.722 | [0.067, 0.402] | 0.000 |
| qw_imp_s025 | 1.1087 | 0.0000 | 1.233 | [0.609, 1.469] | 0.000 |
| qw_imp_s030 | 2.6194 | 0.0000 | 1.439 | [1.722, 3.651] | 0.000 |

注意：这些 median_diff 是 **per-problem 配对** 统计量（`np.median(ii_low) - np.median(ii_high)`，仅含 high/low 均非 None 的 problem），与原 registry 中基于 segment-level aggregate 的值略有差异。

`qw_imp_s015` 的 bootstrap CI 边缘包含 0（[-0.005, 0.110]），但 permutation p=0.0001 仍显著。

### Part C: cross_model_analysis.json
- `random_median_diffs.qwen.s030`: 4.24103 → 2.418272 ✓

Registry 已更新，artifact 已注册。脚本存放在 `analysis/rebootstrap_importance_b10000.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_rebootstrap_importance_b10000_20260514T090502"
}
```

</details>

---
