# analysis median audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 0
- **Tool calls:** 45
- **Original source:** `logs/chats/worker_analysis_median_audit_20260514T182536.jsonl`
- **Structured JSON:** [`cb1e93c89de88308124c.json`](../../sessions/cb/cb1e93c89de88308124c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

91 recorded events

### Tool call

_source line 1 · 2026-05-14T18:29:40.920614+00:00_

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
  "session": "worker_analysis_median_audit_20260514T182536",
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

_source line 2 · 2026-05-14T18:29:40.921140+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T18:29:40.921363+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/profiling -name 'profiling_results.json' -ls 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/profiling -name 'profiling_results.json' -ls 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T18:29:40.921641+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T18:29:40.921801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -la /root/autodl-tmp/pacs/profiling/results_n500_deepseek/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -la /root/autodl-tmp/pacs/profiling/results_n500_deepseek/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T18:29:40.921934+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T18:29:40.922058+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/profiling -maxdepth 1 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/profiling -maxdepth 1 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T18:29:40.922179+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/analysis_output/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/analysis_output/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T18:29:40.922304+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling\\n/root/autodl-tmp/pacs/profiling/__pycache__\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:29:40.922454+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:29:40.922630+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/ -path '*c5b*' -name '*.json' -ls 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/ -path '*c5b*' -name '*.json' -ls 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:29:40.922773+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T18:29:40.922914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/profiling -type f -name '*.json'",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/profiling -type f -name '*.json'",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T18:29:40.923040+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T18:29:40.923156+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -maxdepth 2 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -maxdepth 2 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T18:29:40.923340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs\\n/root/autodl-tmp/pacs/data\\n/root/autodl-tmp/pacs/output\\n/root/autodl-tmp/pacs/checkpoints\\n/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B\\n/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct-cache\\n/root/autodl-tmp/pacs/logs\\n/root/autodl-tmp/pacs/profiling\\n/root/autodl-tmp/pacs/profiling/__pycache__\\n/root/autodl-tmp/pacs/utils\\n/root/autodl-tmp/pacs/utils/__pycache__\\n/root/autodl-tmp/pacs/paper\\n/root/autodl-tmp/pacs/paper/figures\\n/root/autodl-tmp/pacs/paper/_pdf_images\\n/root/autodl-tmp/pacs/profiling_output\\n/root/autodl-tmp/pacs/pacs\\n/root/autodl-tmp/pacs/pacs/profiling\\n/root/autodl-tmp/pacs/pacs/utils\\n/root/autodl-tmp/pacs/pacs/compound\\n/root/autodl-tmp/pacs/pacs/__pycache__\\n/root/autodl-tmp/pacs/pacs/analysis\\n/root/autodl-tmp/pacs/__pycache__\\n/root/autodl-tmp/pacs/profiling_output_v2\\n/root/autodl-tmp/pacs/compound\\n/root/autodl-tmp/pacs/compound/__pycache__\\n/root/autodl-tmp/pacs/profiling_output_v3\\n/root/autodl-tmp/pacs/profiling_output_v4a\\n/root/autodl-tmp/pacs/profiling_output_v4b\\n/root/autodl-tmp/pacs/profiling_output_v4c\\n/root/autodl-tmp/pacs/profiling_output_v4d\\n/root/autodl-tmp/pacs/profiling_output_v4a_r2\\n/root/autodl-tmp/pacs/profiling_output_v4b_r2\\n/root/autodl-tmp/pacs/profiling_output_v4c_r2\\n/root/autodl-tmp/pacs/profiling_output_v4_random_r2\\n/root/autodl-tmp/pacs/profiling_output_qwen_dryrun\\n/root/autodl-tmp/pacs/profiling_output_v4_s025\\n/root/autodl-tmp/pacs/profiling_output_v4_s035\\n/root/autodl-tmp/pacs/profiling_output_v4_s040\\n/root/autodl-tmp/pacs/profiling_output_float32_s030\\n/root/autodl-tmp/pacs/.git\\n/root/autodl-tmp/pacs/.git/branches\\n/root/autodl-tmp/pacs/.git/hooks\\n/root/autodl-tmp/pacs/.git/info\\n/root/autodl-tmp/pacs/.git/refs\\n/root/autodl-tmp/pacs/.git/objects\\n/root/autodl-tmp/pacs/.git/logs\\n/root/autodl-tmp/pacs/profiling_output_v5_s020\\n/root/autodl-tmp/pacs/profiling_output_
…[truncated 4626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T18:29:40.923562+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/analysis_output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/analysis_output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T18:29:40.923727+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_n500_deepseek_dryrun.json\\nanalyze_n500_qwen_dryrun.json\\nbf16_qw_rand_s015\\nbf16_qw_rand_s020\\nbf16_qw_rand_s025\\nbf16_qw_rand_s030\\nc2_n500_report_dryrun.md\\nc2_n500_results_dryrun.json\\nc3_llama_cohens_d.json\\nc3_llama_report.md\\nc3_llama_results.json\\ncohens_d_bf16.json\\ncohens_d_bf16_qwen.json\\ncohens_d_n500_dryrun.json\\ncohens_d_paired_b10000.json\\ncohens_d_paired_b10000_6point.json\\ncohens_d_paired_dz_6point.json\\ncross_model_analysis.json\\nexperiment_summary_table.json\\npermutation_test_results.json\\nrebootstrap_b10000_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T18:29:40.923915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -name '*c5b*' -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -name '*c5b*' -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T18:29:40.924050+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/logs/c5b_pilot_full.log\\n/root/autodl-tmp/pacs/logs/c5b_pilot_s025.log\\n/root/autodl-tmp/pacs/logs/c5b_pilot_s030.log\\n/root/autodl-tmp/pacs/logs/c5b_pilot_gpu3.log\\n/root/autodl-tmp/pacs/run_c5b_pilot.py\\n/root/autodl-tmp/pacs/run_c5b_pilot.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T18:29:40.924203+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T18:29:40.924330+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T18:29:40.924501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -100 /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -100 /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T18:29:40.924797+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conditions\\\": {\\n    \\\"s015\\\": {\\n      \\\"sparsity_label\\\": \\\"s015\\\",\\n      \\\"sparsity_key\\\": \\\"0.15\\\",\\n      \\\"imp_vs_rand\\\": {\\n        \\\"d_z\\\": 0.19225138846763962,\\n        \\\"d_z_ci\\\": [\\n          -0.08617740273835006,\\n          0.49603215305542003\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"negligible\\\",\\n        \\\"median_diff\\\": 0.020257102834024265,\\n        \\\"median_diff_ci\\\": [\\n          0.0016488482019793027,\\n          0.04347908904179021\\n        ],\\n        \\\"ci_crosses_zero\\\": false,\\n        \\\"mean_diff\\\": 0.021268112473844396,\\n        \\\"std_diff\\\": 0.11062657410884871,\\n        \\\"wilcoxon_stat\\\": 774.0,\\n        \\\"wilcoxon_p\\\": 0.05487489561739345,\\n        \\\"wilcoxon_p_bonferroni\\\": 0.2194995824695738,\\n        \\\"significant_bonferroni\\\": false,\\n        \\\"n_valid\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      },\\n      \\\"phase_gradient_importance\\\": {\\n        \\\"d_z\\\": 1.0079201236023063,\\n        \\\"d_z_ci\\\": [\\n          0.5930227488814525,\\n          1.7024933729406215\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"large\\\",\\n        \\\"mean_diff\\\": 0.05441382480766818,\\n        \\\"std_diff\\\": 0.05398624705814305,\\n        \\\"n\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      },\\n      \\\"phase_gradient_random\\\": {\\n        \\\"d_z\\\": 0.3497305202096621,\\n        \\\"d_z_ci\\\": [\\n          0.06654450841272631,\\n          0.6916419318996692\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"small\\\",\\n        \\\"mean_diff\\\": 0.03314571233382378,\\n        \\\"std_diff\\\": 0.09477500652203032,\\n        \\\"n\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      }\\n    },\\n    \\\"s020\\\": {\\n      \\\"sparsity_label\\\": \\\"s020\\\",\\n      \\\"sparsity_key\\\": \\\"0.2\\\",\\n      \\\"imp_vs_rand\\\": {\\n        
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T18:29:40.924994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -100 /root/autodl-tmp/pacs/analysis_output/c2_n500_results_dryrun.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -100 /root/autodl-tmp/pacs/analysis_output/c2_n500_results_dryrun.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T18:29:40.925257+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -100 /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -100 /root/autodl-tmp/pacs/analysis_output/cross_model_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T18:29:40.925489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conditions\\\": {\\n    \\\"ds_imp_s015\\\": {\\n      \\\"n_total\\\": 50,\\n      \\\"n_valid\\\": 49,\\n      \\\"n_skipped\\\": 1,\\n      \\\"phase_gradient\\\": {\\n        \\\"d_z\\\": 0.441634,\\n        \\\"d_z_ci\\\": [\\n          0.3548,\\n          0.7836\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"small\\\",\\n        \\\"d_z_ci_crosses_zero\\\": false\\n      },\\n      \\\"median_diff\\\": {\\n        \\\"value\\\": 0.350757,\\n        \\\"ci\\\": [\\n          0.249,\\n          0.4443\\n        ],\\n        \\\"ci_crosses_zero\\\": false\\n      },\\n      \\\"mean_diff\\\": {\\n        \\\"value\\\": 0.756804,\\n        \\\"ci\\\": [\\n          0.3469,\\n          1.2972\\n        ],\\n        \\\"std\\\": 1.713645\\n      },\\n      \\\"wilcoxon\\\": {\\n        \\\"statistic\\\": 1095.0,\\n        \\\"p_value\\\": 9.601204276066255e-08,\\n        \\\"significant_005\\\": true\\n      },\\n      \\\"phase_stats\\\": {\\n        \\\"high\\\": {\\n          \\\"n\\\": 49,\\n          \\\"mean\\\": -0.013404601606581582,\\n          \\\"median\\\": 0.00011950714612435354,\\n          \\\"std\\\": 0.07929679239821659\\n        },\\n        \\\"mid\\\": {\\n          \\\"n\\\": 40,\\n          \\\"mean\\\": 0.30862102587006696,\\n          \\\"median\\\": 0.10711428023182856,\\n          \\\"std\\\": 0.6989788444027193\\n        },\\n        \\\"low\\\": {\\n          \\\"n\\\": 50,\\n          \\\"mean\\\": 0.7255037511215768,\\n          \\\"median\\\": 0.3155165357061468,\\n          \\\"std\\\": 1.7486310767151996\\n        }\\n      },\\n      \\\"dirname\\\": \\\"profiling_output_bf16_ds_imp_s015\\\",\\n      \\\"model\\\": \\\"deepseek\\\",\\n      \\\"masking\\\": \\\"imp\\\",\\n      \\\"sparsity\\\": \\\"s015\\\"\\n    },\\n    \\\"ds_imp_s020\\\": {\\n      \\\"n_total\\\": 50,\\n      \\\"n_valid\\\": 49,\\n      \\\"n_skipped\\\": 1,\\n      \\\"phase_gradient\\
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:29:40.925715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Cross-model analysis: concordance of compound interaction severity across DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct\\\",\\n  \\\"note\\\": \\\"cross-model (shared Qwen2ForCausalLM architecture), not cross-architecture\\\",\\n  \\\"importance_median_diffs\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"s015\\\": 0.392539,\\n      \\\"s020\\\": 1.481741,\\n      \\\"s025\\\": 7.163595,\\n      \\\"s030\\\": 14.586064\\n    },\\n    \\\"qwen\\\": {\\n      \\\"s015\\\": 0.038565,\\n      \\\"s020\\\": 0.234979,\\n      \\\"s025\\\": 1.267732,\\n      \\\"s030\\\": 2.943093\\n    }\\n  },\\n  \\\"random_median_diffs\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"s015\\\": 0.009572,\\n      \\\"s020\\\": -0.01555,\\n      \\\"s025\\\": 0.544512,\\n      \\\"s030\\\": 1.538314\\n    },\\n    \\\"qwen\\\": {\\n      \\\"s015\\\": 0.04971,\\n      \\\"s020\\\": 0.128948,\\n      \\\"s025\\\": 0.659798,\\n      \\\"s030\\\": 2.418272\\n    }\\n  },\\n  \\\"cohens_d_trend\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"s015\\\": 0.4416,\\n      \\\"s020\\\": 0.5195,\\n      \\\"s025\\\": 0.6831,\\n      \\\"s030\\\": 0.8031\\n    },\\n    \\\"qwen\\\": {\\n      \\\"s015\\\": 0.2811,\\n      \\\"s020\\\": 0.5494,\\n      \\\"s025\\\": 0.8894,\\n      \\\"s030\\\": 1.022\\n    },\\n    \\\"deepseek_monotonic\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    },\\n    \\\"qwen_monotonic\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    },\\n    \\\"spearman_rho\\\": 1.0,\\n    \\\"spearman_p\\\": 0.0\\n  },\\n  \\\"importance_monotonicity\\\": {\\n    \\\"deepseek\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    },\\n    \\\"qwen\\\": {\\n      \\\"monotonic_increasing\\\": true,\\n      \\\"strictly_increasing\\\": true\\n    }\\n  },\\n  \\\"ra
…[truncated 1242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T18:29:40.926272+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -maxdepth 1 -name 'analyze_*.py' -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -maxdepth 1 -name 'analyze_*.py' -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T18:29:40.926477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/analyze_v4_comparison.py\\n/root/autodl-tmp/pacs/analyze_c2_n500.py\\n/root/autodl-tmp/pacs/analyze_c3_llama.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T18:29:40.926666+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T18:29:40.926982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T18:29:40.927161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -80 /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -80 /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T18:29:40.927345+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 500,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 230984,\\n      \\\"n_segments\\\": 4527\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 290009,\\n      \\\"n_segments\\\": 4123\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 177399,\\n      \\\"n_segments\\\": 2420\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1827,\\n        \\\"attn\\\": 408.8502,\\n        \\\"kv\\\": 3.0552,\\n        \\\"both\\\": 46.8159\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2217,\\n        \\\"attn\\\": 236196.4937,\\n        \\\"kv\\\": 3.6981,\\n        \\\"both\\\": 3548.4445\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2304,\\n        \\\"attn\\\": 357.5725,\\n        \\\"kv\\\": 3.2159,\\n        \\\"both\\\": 53.5013\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": -259.341152,\\n        \\\"ci_low\\\": -698.594777,\\n        \\\"ci_high\\\": -21.446168,\\n        \\\"median\\\": 0.10302,\\n        \\\"median_ci_low\\\": 0.089985,\\n        \\\"median_ci_high\\\": 0.114715,\\n        \\\"winsorized_mean\\\": 0.305852,\\n        \\\"skewness\\\": -65.9675,\\n        \\\"outlier_count\\\": 4\\n      }\\n    },\\n    \\\"low_sparsi
…[truncated 514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T18:29:40.927545+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -80 /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -80 /root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T18:29:40.927731+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 21086,\\n      \\\"n_segments\\\": 387\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 27748,\\n      \\\"n_segments\\\": 397\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 13306,\\n      \\\"n_segments\\\": 191\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1687,\\n        \\\"attn\\\": 3.5947,\\n        \\\"kv\\\": 2.9239,\\n        \\\"both\\\": 5.7569\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2284,\\n        \\\"attn\\\": 11.3419,\\n        \\\"kv\\\": 3.6161,\\n        \\\"both\\\": 6.2886\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.2269,\\n        \\\"attn\\\": 297.7957,\\n        \\\"kv\\\": 2.915,\\n        \\\"both\\\": 11.3156\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": 0.220767,\\n        \\\"ci_low\\\": -1.009098,\\n        \\\"ci_high\\\": 1.524347,\\n        \\\"median\\\": 0.093076,\\n        \\\"winsorized_mean\\\": 0.316098,\\n        \\\"skewness\\\": -5.4014,\\n        \\\"outlier_count\\\": 4,\\n        \\\"median_ci_low\\\": 0.002436,\\n        \\\"median_ci_high\\\": 0.151457\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.1
…[truncated 475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T18:29:40.927912+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median\\|np.mean\\|np.median\\|nanmean\\|nanmedian' /root/autodl-tmp/pacs/analyze_c2_n500.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median\\|np.mean\\|np.median\\|nanmean\\|nanmedian' /root/autodl-tmp/pacs/analyze_c2_n500.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T18:29:40.928055+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T18:29:40.928183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median\\|np.mean\\|np.median\\|nanmean\\|nanmedian' /root/autodl-tmp/pacs/analyze_c3_llama.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median\\|np.mean\\|np.median\\|nanmean\\|nanmedian' /root/autodl-tmp/pacs/analyze_c3_llama.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T18:29:40.928307+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T18:29:40.928485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c2_n500.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c2_n500.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T18:29:40.928618+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T18:29:40.928736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c3_llama.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c3_llama.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T18:29:40.928854+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T18:29:40.928970+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii' /root/autodl-tmp/pacs/profiling/run_profiling.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii' /root/autodl-tmp/pacs/profiling/run_profiling.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T18:29:40.929093+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T18:29:40.929211+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii' /root/autodl-tmp/pacs/pacs/profiling/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii' /root/autodl-tmp/pacs/pacs/profiling/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T18:29:40.929325+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T18:29:40.929455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -100 /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -100 /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T18:29:40.929633+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        \\\"ii_high\\\": 0.039099327603677514,\\n        \\\"n_segments_high\\\": 9,\\n        \\\"ii_mid\\\": 0.10114905413459341,\\n        \\\"n_segments_mid\\\": 3,\\n        \\\"ii_low\\\": 0.1573013722849681,\\n        \\\"n_segments_low\\\": 2\\n      },\\n      {\\n        \\\"problem_idx\\\": 491,\\n        \\\"problem_id\\\": \\\"test/prealgebra/1128.json\\\",\\n        \\\"ii_high\\\": 0.1506054606658731,\\n        \\\"n_segments_high\\\": 15,\\n        \\\"ii_mid\\\": 0.05386426202182104,\\n        \\\"n_segments_mid\\\": 5,\\n        \\\"ii_low\\\": -0.010269485153518332,\\n        \\\"n_segments_low\\\": 7\\n      },\\n      {\\n        \\\"problem_idx\\\": 492,\\n        \\\"problem_id\\\": \\\"test/precalculus/356.json\\\",\\n        \\\"ii_high\\\": 0.2123657008212826,\\n        \\\"n_segments_high\\\": 8,\\n        \\\"ii_mid\\\": -0.007715007811213925,\\n        \\\"n_segments_mid\\\": 2,\\n        \\\"ii_low\\\": -0.2536642751386089,\\n        \\\"n_segments_low\\\": 9\\n      },\\n      {\\n        \\\"problem_idx\\\": 493,\\n        \\\"problem_id\\\": \\\"test/algebra/2779.json\\\",\\n        \\\"ii_high\\\": 0.3280502955118816,\\n        \\\"n_segments_high\\\": 11,\\n        \\\"ii_mid\\\": 0.3526705173790614,\\n        \\\"n_segments_mid\\\": 10,\\n        \\\"ii_low\\\": 0.6987636801439289,\\n        \\\"n_segments_low\\\": 10\\n      },\\n      {\\n        \\\"problem_idx\\\": 494,\\n        \\\"problem_id\\\": \\\"test/intermediate_algebra/1930.json\\\",\\n        \\\"ii_high\\\": -17.59721852076872,\\n        \\\"n_segments_high\\\": 19,\\n        \\\"ii_mid\\\": -154.04805732212182,\\n        \\\"n_segments_mid\\\": 7,\\n        \\\"ii_low\\\": -133.06556539695356,\\n        \\\"n_segments_low\\\": 15\\n      },\\n      {\\n        \\\"problem_idx\\\": 495,\\n        \\\"problem_id\\\": \\\"test/intermediate_algebra/1981.json\\\",\\n        \\\"ii_high\\\": 0.9547416887785263,\\n 
…[truncated 1853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T18:29:40.929813+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c2_n500.py | head -50",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c2_n500.py | head -50",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T18:29:40.929999+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"76:    return float(np.mean(diffs) / s)\\n86:        boot[i] = sample.mean() / s if s > 0 else np.nan\\n93:def bootstrap_ci_median(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):\\n96:    boot = np.array([np.median(diffs[rng.randint(0, n, size=n)]) for _ in range(B)])\\n100:def bootstrap_ci_mean(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):\\n103:    boot = np.array([np.mean(diffs[rng.randint(0, n, size=n)]) for _ in range(B)])\\n139:    med = float(np.median(diffs))\\n140:    med_ci_lo, med_ci_hi = bootstrap_ci_median(diffs)\\n141:    mean_val = float(np.mean(diffs))\\n142:    mean_ci_lo, mean_ci_hi = bootstrap_ci_mean(diffs)\\n153:                \\\"mean\\\": float(np.mean(arr)),\\n154:                \\\"median\\\": float(np.median(arr)),\\n158:    median_ci_crosses_zero = (med_ci_lo <= 0 <= med_ci_hi)\\n171:        \\\"median_diff\\\": {\\n174:            \\\"ci_crosses_zero\\\": median_ci_crosses_zero,\\n176:        \\\"mean_diff\\\": {\\n177:            \\\"value\\\": round(mean_val, 6),\\n178:            \\\"ci\\\": [round(mean_ci_lo, 4), round(mean_ci_hi, 4)],\\n199:    med50 = r50[\\\"median_diff\\\"]\\n200:    med500 = r500[\\\"median_diff\\\"]\\n211:        \\\"median_ci_width_n50\\\": round(med_ci50_width, 4),\\n212:        \\\"median_ci_width_n500\\\": round(med_ci500_width, 4),\\n213:        \\\"median_ci_reduction_pct\\\": round((1 - med_ci500_width / med_ci50_width) * 100, 1) if med_ci50_width > 0 else None,\\n228:        lines.append(f\\\"- Qwen s015 median diff CI: [{qw_s015.get('median_ci_lo', '?')}, {qw_s015.get('median_ci_hi', '?')}]\\\")\\n248:                md = r[\\\"median_diff\\\"]\\n270:                md = r[\\\"median_diff\\\"]\\n283:        lines.append(f\\\"## {model_name.title()} — Compound Interaction Severity (II_low median)\\\")\\n285:        lines.append(\\\"| Sparsity | Imp median | Imp mean | Rand median | Rand mean | Imp/Rand ratio |\\\")\\n294:            imp_med = ps_i.g
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T18:29:40.930147+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii\\|II.*=\\|ppl_both\\|ppl_attn\\|ppl_kv' /root/autodl-tmp/pacs/profiling/run_profiling.py | head -40",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii\\|II.*=\\|ppl_both\\|ppl_attn\\|ppl_kv' /root/autodl-tmp/pacs/profiling/run_profiling.py | head -40",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T18:29:40.930283+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"39:from .interaction_index import InteractionIndexCalculator, _HeadMaskHook, bootstrap_interaction_index\\n105:    ppl_attn = ii_calc.forward_with_sparse_config(\\n109:    ppl_kv = ii_calc.forward_with_sparse_config(\\n113:    ppl_both = ii_calc.forward_with_sparse_config(\\n118:    return {\\\"dense\\\": ppl_dense, \\\"attn\\\": ppl_attn, \\\"kv\\\": ppl_kv, \\\"both\\\": ppl_both}\\n167:                sign_detail = f\\\"{p1} II{'>' if sign1 == 'pos' else '<'}0, {p2} II{'>' if sign2 == 'pos' else '<'}0 at {level_str}\\\"\\n410:                mean, ci_low, ci_high = bootstrap_interaction_index(\\n452:        \\\"interaction_index\\\": ii_out,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T18:29:40.930433+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii\\|II.*=' /root/autodl-tmp/pacs/pacs/ | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -rn 'interaction_index\\|compute_ii\\|def.*_ii\\|II.*=' /root/autodl-tmp/pacs/pacs/ | head -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T18:29:40.930620+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:4:# II = R_both - R_attn - R_kv + 1\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:8:# II = 0 → independent\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:51:            f\\\"II={self.ii_value:+.4f} ({tag})  \\\"\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:377:            logging.getLogger('interaction_index').warning(\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:399:    def compute_interaction_index(\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:409:        II = R_both - R_attn - R_kv + 1, where R_x = ppl_x / ppl_dense.\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:464:    def compute_per_phase_ii(\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:482:            result = self.compute_interaction_index(\\n/root/autodl-tmp/pacs/pacs/profiling/interaction_index.py:497:def bootstrap_interaction_index(\\n/root/autodl-tmp/pacs/pacs/profiling/run_profiling.py:40:from .interaction_index import InteractionIndexCalculator, _HeadMaskHook, bootstrap_interaction_index\\n/root/autodl-tmp/pacs/pacs/profiling/run_profiling.py:172:                sign_detail = f\\\"{p1} II{'>' if sign1 == 'pos' else '<'}0, {p2} II{'>' if sign2 == 'pos' else '<'}0 at {level_str}\\\"\\n/root/autodl-tmp/pacs/pacs/profiling/run_profiling.py:449:                boot = bootstrap_interaction_index(\\n/root/autodl-tmp/pacs/pacs/profiling/run_profiling.py:508:        \\\"interaction_index\\\": ii_out,\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_results.py:28:def build_ii_table(data: dict) -> List[dict]:\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_results.py:30:    ii = data[\\\"interaction_index\\\"]\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_results.py:52:def print_ii_table(rows: List[dict]) -> None:\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_results.py:70:    ii = data[\\\"interaction_
…[truncated 1534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T18:29:40.930768+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint(f'Total problems: {len(per_problem)}')\n\n# Collect all II values per phase\nfor phase in ['ii_low', 'ii_mid', 'ii_high']:\n    vals = [p[phase] for p in per_problem if phase in p]\n    arr = np.array(vals)\n    print(f'\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\n    print(f'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}')\n    # find outliers beyond 3 IQR\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(i, v) for i, v in enumerate(vals) if v < lo or v > hi]\n    print(f'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}')\n    if outliers:\n        outliers.sort(key=lambda x: x[0])\n        for idx, val in outliers[:10]:\n            prob = per_problem[idx]\n            print(f'    problem_idx={prob[\\\"problem_idx\\\"]}, {phase}={val:.2f}, id={prob[\\\"problem_id\\\"]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint(f'Total problems: {len(per_problem)}')\n\n# Collect all II values per phase\nfor phase in ['ii_low', 'ii_mid', 'ii_high']:\n    vals = [p[phase] for p in per_problem if phase in p]\n    arr = np.array(vals)\n    print(f'\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\n    print(f'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}')\n    # find outliers beyond 3 IQR\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(i, v) for i, v in enumerate(vals) if v < lo or v > hi]\n    print(f'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}')\n    if outliers:\n        outliers.sort(key=lambda x: x[0])\n        for idx, val in outliers[:10]:\n            prob = per_problem[idx]\n            print(f'    problem_idx={prob[\\\"problem_idx\\\"]}, {phase}={val:.2f}, id={prob[\\\"problem_id\\\"]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T18:29:40.930936+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/pacs && python3 -c \\\"\\\\nimport json, numpy as np\\\\n\\\\nwith open(\\\\'profiling_output_n500_bf16_ds_rand_s015/profiling_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\n\\\\nper_problem = d.get(\\\\'per_problem_ii\\\\', {}).get(\\\\'0.15\\\\', [])\\\\nprint(f\\\\'Total problems: {len(per_problem)}\\\\')\\\\n\\\\n# Collect all II values per phase\\\\nfor phase in [\\\\'ii_low\\\\', \\\\'ii_mid\\\\', \\\\'ii_high\\\\']:\\\\n    vals = [p[phase] for p in per_problem if phase in p]\\\\n    arr = np.array(vals)\\\\n    print(f\\\\'\\\\\\\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}\\\\')\\\\n    print(f\\\\'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}\\\\')\\\\n    # find outliers beyond 3 IQR\\\\n    q1, q3 = np.percentile(arr, [25, 75])\\\\n    iqr = q3 - q1\\\\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\\\\n    outliers = [(i, v) for i, v in enumerate(vals) if v < lo or v > hi]\\\\n    print(f\\\\'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}\\\\')\\\\n    if outliers:\\\\n        outliers.sort(key=lambda x: x[0])\\\\n        for idx, val in outliers[:10]:\\\\n            prob = per_problem[idx]\\\\n            print(f\\\\'    problem_idx={prob[\\\\\\\\\\\"problem_idx\\\\\\\\\\\"]}, {phase}={val:.2f}, id={prob[\\\\\\\\\\\"problem_id\\\\\\\\\\\"]}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 2, in &lt;module>\\nModuleNotFoundError: No module named 'numpy'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T18:29:40.931099+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -30 /root/autodl-tmp/pacs/pacs/profiling/interaction_index.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -30 /root/autodl-tmp/pacs/pacs/profiling/interaction_index.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T18:29:40.931243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Interaction Index (II) calculator for measuring super/sub-additivity\\n# of compound sparsity (attention head pruning + KV cache eviction).\\n#\\n# II = R_both - R_attn - R_kv + 1\\n# where R_x = ppl_x / ppl_dense (relative degradation ratio).\\n# II > 0 → super-additive degradation (compound sparsity hurts more than sum of parts)\\n# II < 0 → sub-additive degradation\\n# II = 0 → independent\\n\\nfrom __future__ import annotations\\n\\nimport math\\nfrom dataclasses import dataclass, field\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nimport torch\\nimport torch.nn.functional as F\\n\\nfrom ..utils.metrics import compute_perplexity\\n\\ntry:\\n    from .phase_segmentation import Phase\\nexcept ImportError:\\n    Phase = None  # will be resolved when phase_segmentation is created\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data classes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T18:29:40.931387+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint(f'Total problems: {len(per_problem)}')\n\nfor phase in ['ii_low', 'ii_mid', 'ii_high']:\n    vals = [p[phase] for p in per_problem if phase in p]\n    arr = np.array(vals)\n    print(f'\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\n    print(f'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}')\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(i, v) for i, v in enumerate(vals) if v < lo or v > hi]\n    print(f'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}')\n    if outliers:\n        outliers.sort(key=lambda x: x[1])\n        for idx, val in outliers[:10]:\n            prob = per_problem[idx]\n            print(f'    problem_idx={prob[\\\"problem_idx\\\"]}, {phase}={val:.2f}, id={prob[\\\"problem_id\\\"]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint(f'Total problems: {len(per_problem)}')\n\nfor phase in ['ii_low', 'ii_mid', 'ii_high']:\n    vals = [p[phase] for p in per_problem if phase in p]\n    arr = np.array(vals)\n    print(f'\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\n    print(f'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}')\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(i, v) for i, v in enumerate(vals) if v < lo or v > hi]\n    print(f'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}')\n    if outliers:\n        outliers.sort(key=lambda x: x[1])\n        for idx, val in outliers[:10]:\n            prob = per_problem[idx]\n            print(f'    problem_idx={prob[\\\"problem_idx\\\"]}, {phase}={val:.2f}, id={prob[\\\"problem_id\\\"]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T18:29:40.931580+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \\\"\\\\nimport json, numpy as np\\\\n\\\\nwith open(\\\\'profiling_output_n500_bf16_ds_rand_s015/profiling_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\n\\\\nper_problem = d.get(\\\\'per_problem_ii\\\\', {}).get(\\\\'0.15\\\\', [])\\\\nprint(f\\\\'Total problems: {len(per_problem)}\\\\')\\\\n\\\\nfor phase in [\\\\'ii_low\\\\', \\\\'ii_mid\\\\', \\\\'ii_high\\\\']:\\\\n    vals = [p[phase] for p in per_problem if phase in p]\\\\n    arr = np.array(vals)\\\\n    print(f\\\\'\\\\\\\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}\\\\')\\\\n    print(f\\\\'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}\\\\')\\\\n    q1, q3 = np.percentile(arr, [25, 75])\\\\n    iqr = q3 - q1\\\\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\\\\n    outliers = [(i, v) for i, v in enumerate(vals) if v < lo or v > hi]\\\\n    print(f\\\\'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}\\\\')\\\\n    if outliers:\\\\n        outliers.sort(key=lambda x: x[1])\\\\n        for idx, val in outliers[:10]:\\\\n            prob = per_problem[idx]\\\\n            print(f\\\\'    problem_idx={prob[\\\\\\\\\\\"problem_idx\\\\\\\\\\\"]}, {phase}={val:.2f}, id={prob[\\\\\\\\\\\"problem_id\\\\\\\\\\\"]}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n    problem_idx=392, ii_low=-4325437.55, id=test/precalculus/902.json\\n    problem_idx=75, ii_low=-6858.83, id=test/counting_and_probability/1114.json\\n    problem_idx=26, ii_low=-5578.73, id=test/counting_and_probability/525.json\\n    problem_idx=462, ii_low=-1526.80, id=test/number_theory/679.json\\n    problem_idx=97, ii_low=-407.82, id=test/prealgebra/105.json\\n    problem_idx=320, ii_low=-364.32, id=test/geometry/947.json\\n    problem_idx=463, ii_lo
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T18:29:40.931768+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint(f'Total problems: {len(per_problem)}')\n\nfor phase in ['ii_low', 'ii_mid', 'ii_high']:\n    vals = [(i, p[phase]) for i, p in enumerate(per_problem) if phase in p and p[phase] is not None]\n    arr = np.array([v for _, v in vals])\n    print(f'\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\n    print(f'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}')\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(idx, val) for idx, val in vals if val < lo or val > hi]\n    print(f'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}')\n    outliers.sort(key=lambda x: x[1])\n    for idx, val in outliers[:5]:\n        prob = per_problem[idx]\n        print(f'    problem_idx={prob[\\\"problem_idx\\\"]}, {phase}={val:.2f}, id={prob[\\\"problem_id\\\"]}')\n    # None count\n    none_ct = sum(1 for p in per_problem if phase in p and p[phase] is None)\n    missing_ct = sum(1 for p in per_problem if phase not in p)\n    print(f'  None count: {none_ct}, missing: {missing_ct}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint(f'Total problems: {len(per_problem)}')\n\nfor phase in ['ii_low', 'ii_mid', 'ii_high']:\n    vals = [(i, p[phase]) for i, p in enumerate(per_problem) if phase in p and p[phase] is not None]\n    arr = np.array([v for _, v in vals])\n    print(f'\\n{phase}: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\n    print(f'  min={arr.min():.2f}, max={arr.max():.2f}, std={arr.std():.2f}')\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(idx, val) for idx, val in vals if val < lo or val > hi]\n    print(f'  IQR={iqr:.4f}, 3-IQR bounds=[{lo:.4f}, {hi:.4f}], outliers={len(outliers)}')\n    outliers.sort(key=lambda x: x[1])\n    for idx, val in outliers[:5]:\n        prob = per_problem[idx]\n        print(f'    problem_idx={prob[\\\"problem_idx\\\"]}, {phase}={val:.2f}, id={prob[\\\"problem_id\\\"]}')\n    # None count\n    none_ct = sum(1 for p in per_problem if phase in p and p[phase] is None)\n    missing_ct = sum(1 for p in per_problem if phase not in p)\n    print(f'  None count: {none_ct}, missing: {missing_ct}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T18:29:40.931973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total problems: 500\\n\\nii_low: n=500, mean=-8681.2511, median=0.0889\\n  min=-4325437.55, max=65.60, std=193244.97\\n  IQR=0.3461, 3-IQR bounds=[-1.0582, 1.3647], outliers=71\\n    problem_idx=392, ii_low=-4325437.55, id=test/precalculus/902.json\\n    problem_idx=75, ii_low=-6858.83, id=test/counting_and_probability/1114.json\\n    problem_idx=26, ii_low=-5578.73, id=test/counting_and_probability/525.json\\n    problem_idx=462, ii_low=-1526.80, id=test/number_theory/679.json\\n    problem_idx=97, ii_low=-407.82, id=test/prealgebra/105.json\\n  None count: 0, missing: 0\\n\\nii_mid: n=449, mean=-2.6126, median=0.1050\\n  min=-720.51, max=319.09, std=43.44\\n  IQR=0.2825, 3-IQR bounds=[-0.8513, 1.1261], outliers=73\\n    problem_idx=26, ii_mid=-720.51, id=test/counting_and_probability/525.json\\n    problem_idx=37, ii_mid=-394.60, id=test/geometry/967.json\\n    problem_idx=494, ii_mid=-154.05, id=test/intermediate_algebra/1930.json\\n    problem_idx=97, ii_mid=-120.74, id=test/prealgebra/105.json\\n    problem_idx=75, ii_mid=-116.62, id=test/counting_and_probability/1114.json\\n  None count: 51, missing: 0\\n\\nii_high: n=496, mean=-1.5965, median=0.0833\\n  min=-355.29, max=52.21, std=21.43\\n  IQR=0.3162, 3-IQR bounds=[-0.9818, 1.2313], outliers=72\\n    problem_idx=37, ii_high=-355.29, id=test/geometry/967.json\\n    problem_idx=94, ii_high=-210.63, id=test/prealgebra/1646.json\\n    problem_idx=392, ii_high=-170.81, id=test/precalculus/902.json\\n    problem_idx=26, ii_high=-152.88, id=test/counting_and_probability/525.json\\n    problem_idx=289, ii_high=-28.74, id=test/intermediate_algebra/1300.json\\n  None count: 4, missing: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T18:29:40.932152+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# Check the perplexity values for worst outlier (problem 392)\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nppl = d.get('per_problem_ppl', {}).get('0.15', [])\nprint(f'Per-problem ppl entries: {len(ppl)}')\n\n# Check structure\nif ppl:\n    print('Keys in first entry:', list(ppl[0].keys())[:20])\n    \n# If no per_problem_ppl, check what keys exist\nprint('\\nTop-level keys:', list(d.keys()))\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint('Per-problem II keys:', list(per_problem[0].keys()) if per_problem else 'empty')\n\n# The II formula is: II = R_both - R_attn - R_kv + 1\n# where R_x = ppl_x / ppl_dense\n# When ppl_dense is very close to 1.0, a small denominator amplifies everything\n# Let's check if there's per-problem ppl data anywhere\nfor k in d:\n    if 'ppl' in k.lower() or 'perplexity' in k.lower():\n        print(f'  Key with ppl: {k}, type={type(d[k]).__name__}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# Check the perplexity values for worst outlier (problem 392)\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nppl = d.get('per_problem_ppl', {}).get('0.15', [])\nprint(f'Per-problem ppl entries: {len(ppl)}')\n\n# Check structure\nif ppl:\n    print('Keys in first entry:', list(ppl[0].keys())[:20])\n    \n# If no per_problem_ppl, check what keys exist\nprint('\\nTop-level keys:', list(d.keys()))\n\nper_problem = d.get('per_problem_ii', {}).get('0.15', [])\nprint('Per-problem II keys:', list(per_problem[0].keys()) if per_problem else 'empty')\n\n# The II formula is: II = R_both - R_attn - R_kv + 1\n# where R_x = ppl_x / ppl_dense\n# When ppl_dense is very close to 1.0, a small denominator amplifies everything\n# Let's check if there's per-problem ppl data anywhere\nfor k in d:\n    if 'ppl' in k.lower() or 'perplexity' in k.lower():\n        print(f'  Key with ppl: {k}, type={type(d[k]).__name__}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T18:29:40.932365+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Per-problem ppl entries: 0\\n\\nTop-level keys: ['config', 'phase_stats', 'perplexity', 'interaction_index', 'pass_fail', 'warnings', 'diagnostics', 'per_problem_ii']\\nPer-problem II keys: ['problem_idx', 'problem_id', 'ii_high', 'n_segments_high', 'ii_mid', 'n_segments_mid', 'ii_low', 'n_segments_low']\\n  Key with ppl: perplexity, type=dict\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T18:29:40.932616+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\n# Check n_segments for the worst outliers in rand_s015\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\nper = d['per_problem_ii']['0.15']\n\n# Problem 392 - the -4.3M outlier\nfor idx in [392, 75, 26, 462, 97]:\n    p = next((x for x in per if x['problem_idx'] == idx), None)\n    if p:\n        print(f'problem {idx} ({p[\\\"problem_id\\\"]}):')\n        print(f'  ii_low={p[\\\"ii_low\\\"]:.2f}, n_seg_low={p[\\\"n_segments_low\\\"]}')\n        print(f'  ii_mid={p.get(\\\"ii_mid\\\", \\\"N/A\\\")}, n_seg_mid={p[\\\"n_segments_mid\\\"]}')\n        print(f'  ii_high={p[\\\"ii_high\\\"]:.2f}, n_seg_high={p[\\\"n_segments_high\\\"]}')\n\n# Now check importance-based for same problems\nprint('\\n--- Importance-based (same problems) ---')\nwith open('profiling_output_n500_bf16_ds_imp_s015/profiling_results.json') as f:\n    d2 = json.load(f)\nper2 = d2['per_problem_ii']['0.15']\nfor idx in [392, 75, 26, 462, 97]:\n    p = next((x for x in per2 if x['problem_idx'] == idx), None)\n    if p:\n        print(f'problem {idx}: ii_low={p[\\\"ii_low\\\"]:.4f}, ii_high={p[\\\"ii_high\\\"]:.4f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\n# Check n_segments for the worst outliers in rand_s015\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\nper = d['per_problem_ii']['0.15']\n\n# Problem 392 - the -4.3M outlier\nfor idx in [392, 75, 26, 462, 97]:\n    p = next((x for x in per if x['problem_idx'] == idx), None)\n    if p:\n        print(f'problem {idx} ({p[\\\"problem_id\\\"]}):')\n        print(f'  ii_low={p[\\\"ii_low\\\"]:.2f}, n_seg_low={p[\\\"n_segments_low\\\"]}')\n        print(f'  ii_mid={p.get(\\\"ii_mid\\\", \\\"N/A\\\")}, n_seg_mid={p[\\\"n_segments_mid\\\"]}')\n        print(f'  ii_high={p[\\\"ii_high\\\"]:.2f}, n_seg_high={p[\\\"n_segments_high\\\"]}')\n\n# Now check importance-based for same problems\nprint('\\n--- Importance-based (same problems) ---')\nwith open('profiling_output_n500_bf16_ds_imp_s015/profiling_results.json') as f:\n    d2 = json.load(f)\nper2 = d2['per_problem_ii']['0.15']\nfor idx in [392, 75, 26, 462, 97]:\n    p = next((x for x in per2 if x['problem_idx'] == idx), None)\n    if p:\n        print(f'problem {idx}: ii_low={p[\\\"ii_low\\\"]:.4f}, ii_high={p[\\\"ii_high\\\"]:.4f}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T18:29:40.932809+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \\\"\\\\nimport json, numpy as np\\\\n\\\\n# Check n_segments for the worst outliers in rand_s015\\\\nwith open(\\\\'profiling_output_n500_bf16_ds_rand_s015/profiling_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\nper = d[\\\\'per_problem_ii\\\\'][\\\\'0.15\\\\']\\\\n\\\\n# Problem 392 - the -4.3M outlier\\\\nfor idx in [392, 75, 26, 462, 97]:\\\\n    p = next((x for x in per if x[\\\\'problem_idx\\\\'] == idx), None)\\\\n    if p:\\\\n        print(f\\\\'problem {idx} ({p[\\\\\\\\\\\"problem_id\\\\\\\\\\\"]}):\\\\')\\\\n        print(f\\\\'  ii_low={p[\\\\\\\\\\\"ii_low\\\\\\\\\\\"]:.2f}, n_seg_low={p[\\\\\\\\\\\"n_segments_low\\\\\\\\\\\"]}\\\\')\\\\n        print(f\\\\'  ii_mid={p.get(\\\\\\\\\\\"ii_mid\\\\\\\\\\\", \\\\\\\\\\\"N/A\\\\\\\\\\\")}, n_seg_mid={p[\\\\\\\\\\\"n_segments_mid\\\\\\\\\\\"]}\\\\')\\\\n        print(f\\\\'  ii_high={p[\\\\\\\\\\\"ii_high\\\\\\\\\\\"]:.2f}, n_seg_high={p[\\\\\\\\\\\"n_segments_high\\\\\\\\\\\"]}\\\\')\\\\n\\\\n# Now check importance-based for same problems\\\\nprint(\\\\'\\\\\\\\n--- Importance-based (same problems) ---\\\\')\\\\nwith open(\\\\'profiling_output_n500_bf16_ds_imp_s015/profiling_results.json\\\\') as f:\\\\n    d2 = json.load(f)\\\\nper2 = d2[\\\\'per_problem_ii\\\\'][\\\\'0.15\\\\']\\\\nfor idx in [392, 75, 26, 462, 97]:\\\\n    p = next((x for x in per2 if x[\\\\'problem_idx\\\\'] == idx), None)\\\\n    if p:\\\\n        print(f\\\\'problem {idx}: ii_low={p[\\\\\\\\\\\"ii_low\\\\\\\\\\\"]:.4f}, ii_high={p[\\\\\\\\\\\"ii_high\\\\\\\\\\\"]:.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\nproblem 462 (test/number_theory/679.json):\\n  ii_low=-1526.80, n_seg_low=12\\n  ii_mid=-4.056569417317709, n_seg_mid=5\\n  ii_high=0.04, n_seg_high=12\\nproblem 97 (test/prealgebra/105.j
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T18:29:40.932964+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\n# Check importance-based outlier distribution\nwith open('profiling_output_n500_bf16_ds_imp_s015/profiling_results.json') as f:\n    d = json.load(f)\nper = d['per_problem_ii']['0.15']\nvals = [p['ii_low'] for p in per if p['ii_low'] is not None]\narr = np.array(vals)\nprint(f'IMP ii_low: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\nprint(f'  min={arr.min():.2f}, max={arr.max():.2f}')\nq1, q3 = np.percentile(arr, [25, 75])\niqr = q3 - q1\nlo, hi = q1 - 3*iqr, q3 + 3*iqr\noutliers = [(p['problem_idx'], p['ii_low']) for p in per if p['ii_low'] is not None and (p['ii_low'] < lo or p['ii_low'] > hi)]\nprint(f'  Outliers: {len(outliers)}')\noutliers.sort(key=lambda x: x[1])\nfor idx, val in outliers[:5]:\n    print(f'    problem_idx={idx}, ii_low={val:.2f}')\n\n# Also check aggregate II\nii = d['interaction_index']\nfor phase in ii:\n    for sp in ii[phase]:\n        entry = ii[phase][sp]\n        print(f'\\nIMP {phase} {sp}: mean={entry[\\\"mean\\\"]:.4f}, median={entry[\\\"median\\\"]:.4f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\n# Check importance-based outlier distribution\nwith open('profiling_output_n500_bf16_ds_imp_s015/profiling_results.json') as f:\n    d = json.load(f)\nper = d['per_problem_ii']['0.15']\nvals = [p['ii_low'] for p in per if p['ii_low'] is not None]\narr = np.array(vals)\nprint(f'IMP ii_low: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}')\nprint(f'  min={arr.min():.2f}, max={arr.max():.2f}')\nq1, q3 = np.percentile(arr, [25, 75])\niqr = q3 - q1\nlo, hi = q1 - 3*iqr, q3 + 3*iqr\noutliers = [(p['problem_idx'], p['ii_low']) for p in per if p['ii_low'] is not None and (p['ii_low'] < lo or p['ii_low'] > hi)]\nprint(f'  Outliers: {len(outliers)}')\noutliers.sort(key=lambda x: x[1])\nfor idx, val in outliers[:5]:\n    print(f'    problem_idx={idx}, ii_low={val:.2f}')\n\n# Also check aggregate II\nii = d['interaction_index']\nfor phase in ii:\n    for sp in ii[phase]:\n        entry = ii[phase][sp]\n        print(f'\\nIMP {phase} {sp}: mean={entry[\\\"mean\\\"]:.4f}, median={entry[\\\"median\\\"]:.4f}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-14T18:29:40.933114+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c2_n500.py | head -60",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c2_n500.py | head -60",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-14T18:29:40.933264+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \\\"\\\\nimport json, numpy as np\\\\n\\\\n# Check importance-based outlier distribution\\\\nwith open(\\\\'profiling_output_n500_bf16_ds_imp_s015/profiling_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\nper = d[\\\\'per_problem_ii\\\\'][\\\\'0.15\\\\']\\\\nvals = [p[\\\\'ii_low\\\\'] for p in per if p[\\\\'ii_low\\\\'] is not None]\\\\narr = np.array(vals)\\\\nprint(f\\\\'IMP ii_low: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}\\\\')\\\\nprint(f\\\\'  min={arr.min():.2f}, max={arr.max():.2f}\\\\')\\\\nq1, q3 = np.percentile(arr, [25, 75])\\\\niqr = q3 - q1\\\\nlo, hi = q1 - 3*iqr, q3 + 3*iqr\\\\noutliers = [(p[\\\\'problem_idx\\\\'], p[\\\\'ii_low\\\\']) for p in per if p[\\\\'ii_low\\\\'] is not None and (p[\\\\'ii_low\\\\'] < lo or p[\\\\'ii_low\\\\'] > hi)]\\\\nprint(f\\\\'  Outliers: {len(outliers)}\\\\')\\\\noutliers.sort(key=lambda x: x[1])\\\\nfor idx, val in outliers[:5]:\\\\n    print(f\\\\'    problem_idx={idx}, ii_low={val:.2f}\\\\')\\\\n\\\\n# Also check aggregate II\\\\nii = d[\\\\'interaction_index\\\\']\\\\nfor phase in ii:\\\\n    for sp in ii[phase]:\\\\n        entry = ii[phase][sp]\\\\n        print(f\\\\'\\\\\\\\nIMP {phase} {sp}: mean={entry[\\\\\\\\\\\"mean\\\\\\\\\\\"]:.4f}, median={entry[\\\\\\\\\\\"median\\\\\\\\\\\"]:.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 5, in &lt;module>\\nFileNotFoundError: [Errno 2] No such file or directory: 'profiling_output_n500_bf16_ds_imp_s015/profiling_results.json'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.24}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T18:29:40.933477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"76:    return float(np.mean(diffs) / s)\\n86:        boot[i] = sample.mean() / s if s > 0 else np.nan\\n93:def bootstrap_ci_median(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):\\n96:    boot = np.array([np.median(diffs[rng.randint(0, n, size=n)]) for _ in range(B)])\\n100:def bootstrap_ci_mean(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):\\n103:    boot = np.array([np.mean(diffs[rng.randint(0, n, size=n)]) for _ in range(B)])\\n139:    med = float(np.median(diffs))\\n140:    med_ci_lo, med_ci_hi = bootstrap_ci_median(diffs)\\n141:    mean_val = float(np.mean(diffs))\\n142:    mean_ci_lo, mean_ci_hi = bootstrap_ci_mean(diffs)\\n153:                \\\"mean\\\": float(np.mean(arr)),\\n154:                \\\"median\\\": float(np.median(arr)),\\n158:    median_ci_crosses_zero = (med_ci_lo <= 0 <= med_ci_hi)\\n171:        \\\"median_diff\\\": {\\n174:            \\\"ci_crosses_zero\\\": median_ci_crosses_zero,\\n176:        \\\"mean_diff\\\": {\\n177:            \\\"value\\\": round(mean_val, 6),\\n178:            \\\"ci\\\": [round(mean_ci_lo, 4), round(mean_ci_hi, 4)],\\n199:    med50 = r50[\\\"median_diff\\\"]\\n200:    med500 = r500[\\\"median_diff\\\"]\\n211:        \\\"median_ci_width_n50\\\": round(med_ci50_width, 4),\\n212:        \\\"median_ci_width_n500\\\": round(med_ci500_width, 4),\\n213:        \\\"median_ci_reduction_pct\\\": round((1 - med_ci500_width / med_ci50_width) * 100, 1) if med_ci50_width > 0 else None,\\n228:        lines.append(f\\\"- Qwen s015 median diff CI: [{qw_s015.get('median_ci_lo', '?')}, {qw_s015.get('median_ci_hi', '?')}]\\\")\\n248:                md = r[\\\"median_diff\\\"]\\n270:                md = r[\\\"median_diff\\\"]\\n283:        lines.append(f\\\"## {model_name.title()} — Compound Interaction Severity (II_low median)\\\")\\n285:        lines.append(\\\"| Sparsity | Imp median | Imp mean | Rand median | Rand mean | Imp/Rand ratio |\\\")\\n294:            imp_med = ps_i.g
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T18:29:40.933674+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -d /root/autodl-tmp/pacs/profiling_output_n500_*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -d /root/autodl-tmp/pacs/profiling_output_n500_*/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T18:29:40.933815+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015/\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s020/\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_imp_s015/\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_imp_s020/\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_rand_s015/\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_rand_s020/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T18:29:40.933942+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/pacs/profiling/interaction_index.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/pacs/profiling/interaction_index.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T18:29:40.934509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Interaction Index (II) calculator for measuring super/sub-additivity\\n# of compound sparsity (attention head pruning + KV cache eviction).\\n#\\n# II = R_both - R_attn - R_kv + 1\\n# where R_x = ppl_x / ppl_dense (relative degradation ratio).\\n# II > 0 → super-additive degradation (compound sparsity hurts more than sum of parts)\\n# II < 0 → sub-additive degradation\\n# II = 0 → independent\\n\\nfrom __future__ import annotations\\n\\nimport math\\nfrom dataclasses import dataclass, field\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nimport torch\\nimport torch.nn.functional as F\\n\\nfrom ..utils.metrics import compute_perplexity\\n\\ntry:\\n    from .phase_segmentation import Phase\\nexcept ImportError:\\n    Phase = None  # will be resolved when phase_segmentation is created\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data classes\\n# ---------------------------------------------------------------------------\\n\\n@dataclass\\nclass InteractionResult:\\n    ii_value: float\\n    ppl_dense: float\\n    ppl_attn_sparse: float\\n    ppl_kv_sparse: float\\n    ppl_both_sparse: float\\n    r_attn: float          # ppl_attn / ppl_dense\\n    r_kv: float            # ppl_kv / ppl_dense\\n    r_both: float          # ppl_both / ppl_dense\\n    is_super_additive: bool  # II > 0 → compound sparsity degrades more than sum of parts\\n    sparsity_level: float = 0.0\\n    phase_name: Optional[str] = None\\n    num_tokens: int = 0\\n\\n    def summary(self) -> str:\\n        tag = \\\"super-additive\\\" if self.is_super_additive else \\\"sub-additive\\\"\\n        return (\\n            f\\\"II={self.ii_value:+.4f} ({tag})  \\\"\\n            f\\\"R_attn={self.r_attn:.4f}  R_kv={self.r_kv:.4f}  R_both={self.r_both:.4f}  \\\"\\n            f\\\"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  \\\"\\n            f\\\"kv={self.ppl_k
…[truncated 6859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T18:29:40.934767+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\n# n500 imp s015\nwith open('profiling_output_n500_bf16_ds_imp_s015/profiling_results.json') as f:\n    d = json.load(f)\nii = d['interaction_index']\nfor phase in ii:\n    for sp in ii[phase]:\n        e = ii[phase][sp]\n        print(f'IMP {phase} {sp}: mean={e[\\\"mean\\\"]:.4f}, median={e[\\\"median\\\"]:.4f}, outlier_count={e.get(\\\"outlier_count\\\", \\\"N/A\\\")}')\n        print(f'  skewness={e.get(\\\"skewness\\\", \\\"N/A\\\")}')\n\n# Check per-problem outliers\nper = d.get('per_problem_ii', {}).get('0.15', [])\nif per:\n    vals = [p['ii_low'] for p in per if p['ii_low'] is not None]\n    arr = np.array(vals)\n    print(f'\\nIMP ii_low: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}, min={arr.min():.2f}, max={arr.max():.2f}')\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(p['problem_idx'], p['ii_low']) for p in per if p['ii_low'] is not None and (p['ii_low'] < lo or p['ii_low'] > hi)]\n    outliers.sort(key=lambda x: x[1])\n    print(f'  Outliers: {len(outliers)}')\n    for idx, val in outliers[:5]:\n        print(f'    problem_idx={idx}, ii_low={val:.2f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json, numpy as np\n\n# n500 imp s015\nwith open('profiling_output_n500_bf16_ds_imp_s015/profiling_results.json') as f:\n    d = json.load(f)\nii = d['interaction_index']\nfor phase in ii:\n    for sp in ii[phase]:\n        e = ii[phase][sp]\n        print(f'IMP {phase} {sp}: mean={e[\\\"mean\\\"]:.4f}, median={e[\\\"median\\\"]:.4f}, outlier_count={e.get(\\\"outlier_count\\\", \\\"N/A\\\")}')\n        print(f'  skewness={e.get(\\\"skewness\\\", \\\"N/A\\\")}')\n\n# Check per-problem outliers\nper = d.get('per_problem_ii', {}).get('0.15', [])\nif per:\n    vals = [p['ii_low'] for p in per if p['ii_low'] is not None]\n    arr = np.array(vals)\n    print(f'\\nIMP ii_low: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}, min={arr.min():.2f}, max={arr.max():.2f}')\n    q1, q3 = np.percentile(arr, [25, 75])\n    iqr = q3 - q1\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\n    outliers = [(p['problem_idx'], p['ii_low']) for p in per if p['ii_low'] is not None and (p['ii_low'] < lo or p['ii_low'] > hi)]\n    outliers.sort(key=lambda x: x[1])\n    print(f'  Outliers: {len(outliers)}')\n    for idx, val in outliers[:5]:\n        print(f'    problem_idx={idx}, ii_low={val:.2f}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T18:29:40.934955+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \\\"\\\\nimport json, numpy as np\\\\n\\\\n# n500 imp s015\\\\nwith open(\\\\'profiling_output_n500_bf16_ds_imp_s015/profiling_results.json\\\\') as f:\\\\n    d = json.load(f)\\\\nii = d[\\\\'interaction_index\\\\']\\\\nfor phase in ii:\\\\n    for sp in ii[phase]:\\\\n        e = ii[phase][sp]\\\\n        print(f\\\\'IMP {phase} {sp}: mean={e[\\\\\\\\\\\"mean\\\\\\\\\\\"]:.4f}, median={e[\\\\\\\\\\\"median\\\\\\\\\\\"]:.4f}, outlier_count={e.get(\\\\\\\\\\\"outlier_count\\\\\\\\\\\", \\\\\\\\\\\"N/A\\\\\\\\\\\")}\\\\')\\\\n        print(f\\\\'  skewness={e.get(\\\\\\\\\\\"skewness\\\\\\\\\\\", \\\\\\\\\\\"N/A\\\\\\\\\\\")}\\\\')\\\\n\\\\n# Check per-problem outliers\\\\nper = d.get(\\\\'per_problem_ii\\\\', {}).get(\\\\'0.15\\\\', [])\\\\nif per:\\\\n    vals = [p[\\\\'ii_low\\\\'] for p in per if p[\\\\'ii_low\\\\'] is not None]\\\\n    arr = np.array(vals)\\\\n    print(f\\\\'\\\\\\\\nIMP ii_low: n={len(arr)}, mean={arr.mean():.4f}, median={np.median(arr):.4f}, min={arr.min():.2f}, max={arr.max():.2f}\\\\')\\\\n    q1, q3 = np.percentile(arr, [25, 75])\\\\n    iqr = q3 - q1\\\\n    lo, hi = q1 - 3*iqr, q3 + 3*iqr\\\\n    outliers = [(p[\\\\'problem_idx\\\\'], p[\\\\'ii_low\\\\']) for p in per if p[\\\\'ii_low\\\\'] is not None and (p[\\\\'ii_low\\\\'] < lo or p[\\\\'ii_low\\\\'] > hi)]\\\\n    outliers.sort(key=lambda x: x[1])\\\\n    print(f\\\\'  Outliers: {len(outliers)}\\\\')\\\\n    for idx, val in outliers[:5]:\\\\n        print(f\\\\'    problem_idx={idx}, ii_low={val:.2f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 5, in &lt;module>\\nFileNotFoundError: [Errno 2] No such file or directory: 'profiling_output_n500_bf16_ds_imp_s015/profiling_re
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T18:29:40.935125+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# Check perplexity for the aggregate phases in rand s015\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nppl = d['perplexity']\nfor phase in ppl:\n    for sp in ppl[phase]:\n        e = ppl[phase][sp]\n        print(f'RAND {phase} {sp}: dense={e[\\\"dense\\\"]:.4f}, attn={e[\\\"attn\\\"]:.4f}, kv={e[\\\"kv\\\"]:.4f}, both={e[\\\"both\\\"]:.4f}')\n\n# The key insight: when ppl_dense ~1.0, R_x = ppl_x / ppl_dense\n# If ppl_both explodes to 236196 but ppl_attn=408 and ppl_kv=3.05:\n# R_both = 236196/1.22 = 193603, R_attn = 408/1.22 = 334, R_kv = 3.05/1.22 = 2.5\n# II = 193603 - 334 - 2.5 + 1 = 193267 — but wait, the mean is NEGATIVE?\n# That means the per-segment aggregation is driving it negative somehow.\nprint()\nprint('--- Diagnostics ---')\ndiag = d.get('diagnostics', {})\nprint(json.dumps(diag, indent=2)[:2000] if diag else 'No diagnostics')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# Check perplexity for the aggregate phases in rand s015\nwith open('profiling_output_n500_bf16_ds_rand_s015/profiling_results.json') as f:\n    d = json.load(f)\n\nppl = d['perplexity']\nfor phase in ppl:\n    for sp in ppl[phase]:\n        e = ppl[phase][sp]\n        print(f'RAND {phase} {sp}: dense={e[\\\"dense\\\"]:.4f}, attn={e[\\\"attn\\\"]:.4f}, kv={e[\\\"kv\\\"]:.4f}, both={e[\\\"both\\\"]:.4f}')\n\n# The key insight: when ppl_dense ~1.0, R_x = ppl_x / ppl_dense\n# If ppl_both explodes to 236196 but ppl_attn=408 and ppl_kv=3.05:\n# R_both = 236196/1.22 = 193603, R_attn = 408/1.22 = 334, R_kv = 3.05/1.22 = 2.5\n# II = 193603 - 334 - 2.5 + 1 = 193267 — but wait, the mean is NEGATIVE?\n# That means the per-segment aggregation is driving it negative somehow.\nprint()\nprint('--- Diagnostics ---')\ndiag = d.get('diagnostics', {})\nprint(json.dumps(diag, indent=2)[:2000] if diag else 'No diagnostics')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-14T18:29:40.935273+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c3_llama.py | head -50",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "grep -n 'mean\\|median' /root/autodl-tmp/pacs/analyze_c3_llama.py | head -50",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T18:29:40.935447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"RAND high_sparsity 0.15: dense=1.1827, attn=408.8502, kv=3.0552, both=46.8159\\nRAND low_sparsity 0.15: dense=1.2217, attn=236196.4937, kv=3.6981, both=3548.4445\\nRAND mid_sparsity 0.15: dense=1.2304, attn=357.5725, kv=3.2159, both=53.5013\\n\\n--- Diagnostics ---\\n{\\n  \\\"per_problem_sparsity\\\": [\\n    {\\n      \\\"problem_id\\\": \\\"test/precalculus/807.json\\\",\\n      \\\"sparsity_values\\\": [\\n        0.3392857313156128,\\n        0.4214285910129547,\\n        0.474567174911499,\\n        0.42803841829299927,\\n        0.4406512975692749,\\n        0.3690476715564728,\\n        0.4454081952571869,\\n        0.2957746684551239,\\n        0.3353174924850464,\\n        0.4011741876602173,\\n        0.40347492694854736,\\n        0.35380953550338745,\\n        0.3594925105571747,\\n        0.3214285969734192,\\n        0.3392857313156128,\\n        0.3173598647117615,\\n        0.35803571343421936,\\n        0.2843915820121765,\\n        0.37979093194007874,\\n        0.31454387307167053,\\n        0.46641162037849426,\\n        0.278151273727417,\\n        0.335132896900177,\\n        0.3050082325935364,\\n        0.30965912342071533,\\n        0.26565009355545044,\\n        0.2984127402305603,\\n        0.34183675050735474,\\n        0.3299689292907715,\\n        0.31182795763015747,\\n        0.38981762528419495,\\n        0.3432331383228302,\\n        0.3887649178504944,\\n        0.35382917523384094,\\n        0.38265305757522583,\\n        0.3845599293708801,\\n        0.31035715341567993,\\n        0.35254594683647156,\\n        0.27976194024086,\\n        0.35852986574172974,\\n        0.38255494832992554,\\n        0.36122453212738037,\\n        0.30087605118751526,\\n        0.33744993805885315,\\n        0.341269850730896,\\n        0.3741808831691742,\\n        0.38181817531585693,\\n        0.488095223903656,\\n        0.4218750298023224,\\n        0.4175094664096832,\\n        0.44204
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-14T18:29:40.935625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"66:    return float(np.mean(diffs) / s)\\n77:        boot[i] = sample.mean() / s if s > 0 else np.nan\\n84:def bootstrap_ci_median(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):\\n90:        boot[i] = np.median(diffs[idx])\\n94:def bootstrap_paired_dz_and_median(imp_diffs, rand_diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):\\n102:    boot_median = np.empty(B)\\n107:        boot_dz[i] = sample.mean() / s if s > 0 else np.nan\\n108:        boot_median[i] = np.median(sample)\\n113:    med_ci = (float(np.percentile(boot_median, 100 * alpha / 2)),\\n114:              float(np.percentile(boot_median, 100 * (1 - alpha / 2))))\\n186:    dz_ci, median_ci = bootstrap_paired_dz_and_median(imp_pg, rand_pg, B=B_BOOTSTRAP, seed=SEED)\\n189:    median_diff = float(np.median(paired_D))\\n195:        \\\"median_diff\\\": median_diff,\\n196:        \\\"median_diff_ci\\\": list(median_ci),\\n197:        \\\"ci_crosses_zero\\\": bool(median_ci[0] <= 0 <= median_ci[1]),\\n198:        \\\"mean_diff\\\": float(np.mean(paired_D)),\\n216:        \\\"mean_diff\\\": float(np.mean(imp_pg)),\\n230:        \\\"mean_diff\\\": float(np.mean(rand_pg)),\\n282:        mci = ivr[\\\"median_diff_ci\\\"]\\n283:        lines.append(f\\\"| {sl} | {ivr['median_diff']:.6f} | [{mci[0]:.6f}, {mci[1]:.6f}] | {ivr['ci_crosses_zero']} |\\\")\\n423:        print(f\\\"  Median diff={ivr['median_diff']:.6f} CI=[{ivr['median_diff_ci'][0]:.6f}, {ivr['median_diff_ci'][1]:.6f}]\\\")\\n439:            \\\"mean_diff\\\": pg[\\\"mean_diff\\\"],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-14T18:29:40.935780+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-14T18:29:40.935964+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-14T18:29:40.936097+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# Check what n500 results we actually have with profiling_results.json\nimport os, glob\ndirs = sorted(glob.glob('profiling_output_n500_*/'))\nfor d in dirs:\n    f = os.path.join(d, 'profiling_results.json')\n    exists = os.path.exists(f)\n    print(f'{d}: profiling_results.json = {exists}')\n    if exists:\n        with open(f) as fh:\n            data = json.load(fh)\n        ii = data.get('interaction_index', {})\n        for phase in ['low_sparsity']:\n            for sp in ii.get(phase, {}):\n                e = ii[phase][sp]\n                print(f'  {phase} {sp}: mean={e[\\\"mean\\\"]:.4f}, median={e[\\\"median\\\"]:.4f}, skew={e.get(\\\"skewness\\\",\\\"N/A\\\")}, outliers={e.get(\\\"outlier_count\\\",\\\"N/A\\\")}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# Check what n500 results we actually have with profiling_results.json\nimport os, glob\ndirs = sorted(glob.glob('profiling_output_n500_*/'))\nfor d in dirs:\n    f = os.path.join(d, 'profiling_results.json')\n    exists = os.path.exists(f)\n    print(f'{d}: profiling_results.json = {exists}')\n    if exists:\n        with open(f) as fh:\n            data = json.load(fh)\n        ii = data.get('interaction_index', {})\n        for phase in ['low_sparsity']:\n            for sp in ii.get(phase, {}):\n                e = ii[phase][sp]\n                print(f'  {phase} {sp}: mean={e[\\\"mean\\\"]:.4f}, median={e[\\\"median\\\"]:.4f}, skew={e.get(\\\"skewness\\\",\\\"N/A\\\")}, outliers={e.get(\\\"outlier_count\\\",\\\"N/A\\\")}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-14T18:29:40.936238+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_output_n500_bf16_ds_imp_s015/: profiling_results.json = False\\nprofiling_output_n500_bf16_ds_rand_s015/: profiling_results.json = True\\n  low_sparsity 0.15: mean=-185738.2737, median=0.1178, skew=-45.6929, outliers=7\\nprofiling_output_n500_bf16_ds_rand_s020/: profiling_results.json = False\\nprofiling_output_n500_bf16_qw_imp_s015/: profiling_results.json = False\\nprofiling_output_n500_bf16_qw_imp_s020/: profiling_results.json = False\\nprofiling_output_n500_bf16_qw_rand_s015/: profiling_results.json = False\\nprofiling_output_n500_bf16_qw_rand_s020/: profiling_results.json = False\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-14T18:29:40.936399+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# n=50 bf16 results - check mean vs median discrepancy\nfor name in ['profiling_output_bf16_ds_rand_s015', 'profiling_output_bf16_ds_imp_s015',\n             'profiling_output_bf16_qw_rand_s015', 'profiling_output_bf16_qw_imp_s015']:\n    try:\n        with open(f'{name}/profiling_results.json') as f:\n            d = json.load(f)\n        ii = d['interaction_index']\n        for phase in ['low_sparsity', 'high_sparsity']:\n            for sp in ii.get(phase, {}):\n                e = ii[phase][sp]\n                print(f'{name.replace(\\\"profiling_output_bf16_\\\",\\\"\\\")} {phase} {sp}: mean={e[\\\"mean\\\"]:.4f}, median={e[\\\"median\\\"]:.4f}, skew={e.get(\\\"skewness\\\",\\\"N/A\\\")}, outliers={e.get(\\\"outlier_count\\\",\\\"N/A\\\")}')\n    except FileNotFoundError:\n        print(f'{name}: NOT FOUND')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\n\n# n=50 bf16 results - check mean vs median discrepancy\nfor name in ['profiling_output_bf16_ds_rand_s015', 'profiling_output_bf16_ds_imp_s015',\n             'profiling_output_bf16_qw_rand_s015', 'profiling_output_bf16_qw_imp_s015']:\n    try:\n        with open(f'{name}/profiling_results.json') as f:\n            d = json.load(f)\n        ii = d['interaction_index']\n        for phase in ['low_sparsity', 'high_sparsity']:\n            for sp in ii.get(phase, {}):\n                e = ii[phase][sp]\n                print(f'{name.replace(\\\"profiling_output_bf16_\\\",\\\"\\\")} {phase} {sp}: mean={e[\\\"mean\\\"]:.4f}, median={e[\\\"median\\\"]:.4f}, skew={e.get(\\\"skewness\\\",\\\"N/A\\\")}, outliers={e.get(\\\"outlier_count\\\",\\\"N/A\\\")}')\n    except FileNotFoundError:\n        print(f'{name}: NOT FOUND')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-14T18:29:40.936570+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ds_rand_s015 low_sparsity 0.15: mean=-1.8952, median=0.1026, skew=-11.5715, outliers=4\\nds_rand_s015 high_sparsity 0.15: mean=0.2208, median=0.0931, skew=-5.4014, outliers=4\\nds_imp_s015 low_sparsity 0.15: mean=2.4058, median=0.3983, skew=9.5402, outliers=5\\nds_imp_s015 high_sparsity 0.15: mean=-0.1502, median=0.0058, skew=-14.9912, outliers=2\\nqw_rand_s015 low_sparsity 0.15: mean=1.4082, median=0.1878, skew=7.1113, outliers=5\\nqw_rand_s015 high_sparsity 0.15: mean=1.6652, median=0.1381, skew=7.1842, outliers=6\\nqw_imp_s015 low_sparsity 0.15: mean=0.0344, median=0.0394, skew=4.7585, outliers=4\\nqw_imp_s015 high_sparsity 0.15: mean=-0.0828, median=0.0009, skew=-4.5327, outliers=7\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-14T18:29:40.936706+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s025/ && head -60 /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s025/profiling_results.json 2>/dev/null; ls /root/autodl-tmp/pacs/profiling_output_c5b_all_s025/ && head -60 /root/autodl-tmp/pacs/profiling_output_c5b_all_s025/profiling_results.json 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s025/ && head -60 /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s025/profiling_results.json 2>/dev/null; ls /root/autodl-tmp/pacs/profiling_output_c5b_all_s025/ && head -60 /root/autodl-tmp/pacs/profiling_output_c5b_all_s025/profiling_results.json 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-14T18:29:40.936840+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'ls /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s025/ && head -60 /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s025/profiling_results.json 2>/dev/null; ls /root/autodl-tmp/pacs/profiling_output_c5b_all_s025/ && head -60 /root/autodl-tmp/pacs/profiling_output_c5b_all_s025/profiling_results.json 2>/dev/null'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_median_audit_20260514T182536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 91 · 2026-05-14T18:29:40.937044+00:00_

调查完成。汇报如下：

---

## 1. Median 字段已存在

**所有 profiling_results.json** 的 `interaction_index` 区块已包含：
- `median`, `median_ci_low`, `median_ci_high` — 由 `bootstrap_interaction_index()` 计算
- 同时有 `mean`, `winsorized_mean`, `skewness`, `outlier_count`

**分析输出**（c2_n500, c3_llama, cross_model_analysis）也已同时报告 `median_diff` 和 `mean_diff`。`cross_model_analysis.json` 主指标即 `importance_median_diffs` / `random_median_diffs`。

**结论：不需要重跑实验，median 数据已齐全。**

## 2. Raw Data 结构

`per_problem_ii` 存储每个 problem 的 `ii_high/ii_mid/ii_low` + segment 数，可事后重算任意统计量。**不存储 per-problem perplexity**（只有聚合 ppl）。

## 3. Outlier 调查

### n500 rand s015 ii_low 统计

| 指标 | 值 |
|------|-----|
| n | 500 |
| mean | **-8,681.25** |
| median | **0.0889** |
| std | 193,244.97 |
| min | **-4,325,437.55** |
| max | 65.60 |
| 3×IQR outliers | 71 (14.2%) |

### 前 5 极端 outlier

| problem_idx | ii_low | problem_id |
|-------------|--------|------------|
| 392 | -4,325,437.55 | test/precalculus/902.json |
| 75 | -6,858.83 | test/counting_and_probability/1114.json |
| 26 | -5,578.73 | test/counting_and_probability/525.json |
| 462 | -1,526.80 | test/number_theory/679.json |
| 97 | -407.82 | test/prealgebra/105.json |

### Outlier 根源

**不是分母为零的问题。** Dense ppl 始终 ≈ 1.2，分母安全。

根源是 **II 公式 `II = R_both - R_attn - R_kv + 1`** 中，random pruning 对某些 problem 造成了灾难性失败：
- 聚合 ppl 可见端倪：low_sparsity 的 `attn_ppl = 236,196`（正常应为个位数）
- 单个 problem（#392）的 random head masking 恰好破坏了关键 attention 路径，导致 ppl_attn 爆炸到数百万级别，`R_attn` 远大于 `R_both`，II 变成巨大负数
- Importance-based 条件下同一问题不出现此现象（importance 保留关键 head，避免灾难性失败）

**n=50 vs n=500 对比：** n=50 时 mean=-1.90 / median=0.103（偏差已有但可控），n=500 采样到更多极端 problem 后 mean 彻底崩溃到 -185,738。

## 4. 分析脚本 Mean/Median 使用

**analyze_c2_n500.py** 和 **analyze_c3_llama.py** 都已同时计算 median 和 mean：
- `bootstrap_ci_median()` + `bootstrap_ci_mean()` 并行
- 输出中 `median_diff` 和 `mean_diff` 双轨
- 报告表同时展示 median 和 mean 列

**但 Cohen's d_z 仍用 mean-based 公式**（`mean(D)/SD(D)`，`analyze_c2_n500.py:76`），同样会被 outlier 摧毁。如果要全面切 median，d_z 需替换为 robust 效应量（如基于 median 的非参数替代）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_median_audit_20260514T182536"
}
```

</details>

---
