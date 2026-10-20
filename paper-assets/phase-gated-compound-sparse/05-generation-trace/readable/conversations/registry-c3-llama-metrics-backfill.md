# registry c3 llama metrics backfill

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_registry_c3_llama_metrics_backfill_20260516T025245.jsonl`
- **Structured JSON:** [`19fa3887619b95f5f22e.json`](../../sessions/19/19fa3887619b95f5f22e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-16T02:54:09.052950+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:54:09.053491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:54:09.053776+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'c3_llama'}",
  "project": "phase-gated-compound-sparse",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'c3_llama'}",
    "project": "phase-gated-compound-sparse",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T02:54:09.053974+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -la /root/autodl-tmp/pacs/analysis_output/c3_llama*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -la /root/autodl-tmp/pacs/analysis_output/c3_llama*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T02:54:09.054168+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0609}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:54:09.054352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1011 May 15 01:55 /root/autodl-tmp/pacs/analysis_output/c3_llama_cohens_d.json\\n-rw-r--r-- 1 root root 1917 May 15 01:55 /root/autodl-tmp/pacs/analysis_output/c3_llama_report.md\\n-rw-r--r-- 1 root root 6102 May 15 01:55 /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:54:09.054609+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis_output/c3_llama_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:54:09.055024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conditions\\\": {\\n    \\\"s015\\\": {\\n      \\\"sparsity_label\\\": \\\"s015\\\",\\n      \\\"sparsity_key\\\": \\\"0.15\\\",\\n      \\\"imp_vs_rand\\\": {\\n        \\\"d_z\\\": 0.19225138846763962,\\n        \\\"d_z_ci\\\": [\\n          -0.08617740273835006,\\n          0.49603215305542003\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"negligible\\\",\\n        \\\"median_diff\\\": 0.020257102834024265,\\n        \\\"median_diff_ci\\\": [\\n          0.0016488482019793027,\\n          0.04347908904179021\\n        ],\\n        \\\"ci_crosses_zero\\\": false,\\n        \\\"mean_diff\\\": 0.021268112473844396,\\n        \\\"std_diff\\\": 0.11062657410884871,\\n        \\\"wilcoxon_stat\\\": 774.0,\\n        \\\"wilcoxon_p\\\": 0.05487489561739345,\\n        \\\"wilcoxon_p_bonferroni\\\": 0.2194995824695738,\\n        \\\"significant_bonferroni\\\": false,\\n        \\\"n_valid\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      },\\n      \\\"phase_gradient_importance\\\": {\\n        \\\"d_z\\\": 1.0079201236023063,\\n        \\\"d_z_ci\\\": [\\n          0.5930227488814525,\\n          1.7024933729406215\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"large\\\",\\n        \\\"mean_diff\\\": 0.05441382480766818,\\n        \\\"std_diff\\\": 0.05398624705814305,\\n        \\\"n\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      },\\n      \\\"phase_gradient_random\\\": {\\n        \\\"d_z\\\": 0.3497305202096621,\\n        \\\"d_z_ci\\\": [\\n          0.06654450841272631,\\n          0.6916419318996692\\n        ],\\n        \\\"d_z_interpretation\\\": \\\"small\\\",\\n        \\\"mean_diff\\\": 0.03314571233382378,\\n        \\\"std_diff\\\": 0.09477500652203032,\\n        \\\"n\\\": 49,\\n        \\\"n_skipped\\\": 1\\n      }\\n    },\\n    \\\"s020\\\": {\\n      \\\"sparsity_label\\\": \\\"s020\\\",\\n      \\\"sparsity_key\\\": \\\"0.2\\\",\\n      \\\"imp_vs_rand\\\": {\\n        
…[truncated 5748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:54:09.055316+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis_output/c3_llama_cohens_d.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis_output/c3_llama_cohens_d.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:54:09.057670+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"s015\\\": {\\n    \\\"d\\\": 1.0079201236023063,\\n    \\\"ci_low\\\": 0.5930227488814525,\\n    \\\"ci_high\\\": 1.7024933729406215,\\n    \\\"n\\\": 49,\\n    \\\"n_skipped\\\": 1,\\n    \\\"mean_diff\\\": 0.05441382480766818,\\n    \\\"std_diff\\\": 0.05398624705814305,\\n    \\\"interpretation\\\": \\\"large\\\"\\n  },\\n  \\\"s020\\\": {\\n    \\\"d\\\": 1.1079945177803487,\\n    \\\"ci_low\\\": 0.8144225776418755,\\n    \\\"ci_high\\\": 1.5698333601725651,\\n    \\\"n\\\": 49,\\n    \\\"n_skipped\\\": 1,\\n    \\\"mean_diff\\\": 0.15684586995077796,\\n    \\\"std_diff\\\": 0.14155834476960058,\\n    \\\"interpretation\\\": \\\"large\\\"\\n  },\\n  \\\"s025\\\": {\\n    \\\"d\\\": 1.1227060736223793,\\n    \\\"ci_low\\\": 0.8734880719992411,\\n    \\\"ci_high\\\": 1.5767998440206223,\\n    \\\"n\\\": 49,\\n    \\\"n_skipped\\\": 1,\\n    \\\"mean_diff\\\": 0.34412922512237787,\\n    \\\"std_diff\\\": 0.3065176480359233,\\n    \\\"interpretation\\\": \\\"large\\\"\\n  },\\n  \\\"s030\\\": {\\n    \\\"d\\\": 1.0038154860504354,\\n    \\\"ci_low\\\": 0.8099192773251124,\\n    \\\"ci_high\\\": 1.3519403830443735,\\n    \\\"n\\\": 49,\\n    \\\"n_skipped\\\": 1,\\n    \\\"mean_diff\\\": 0.6401246217027533,\\n    \\\"std_diff\\\": 0.6376915186090196,\\n    \\\"interpretation\\\": \\\"large\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:54:09.057955+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/analysis_output/c3_llama_report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/analysis_output/c3_llama_report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:54:09.058162+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "fields": "['*']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "fields": "['*']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T02:54:09.058391+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# C3 LLaMA Cross-Architecture Analysis Report\\n\\nModel: DeepSeek-R1-Distill-Llama-8B (n=50)\\nBootstrap: B=10000, seed=42\\nBonferroni correction: k=4\\n\\n## 1. Importance vs Random Paired Comparison\\n\\n| Sparsity | d_z | 95% CI | Interpretation | Wilcoxon p (Bonf.) | Sig. |\\n|----------|-----|--------|----------------|---------------------|------|\\n| s015 | 0.1923 | [-0.0862, 0.4960] | negligible | 0.2195 | No |\\n| s020 | 0.2550 | [-0.0248, 0.5381] | small | 0.2527 | No |\\n| s025 | 0.2902 | [0.0081, 0.6121] | small | 0.0834 | No |\\n| s030 | 0.3352 | [0.0606, 0.6629] | small | 0.0294 | Yes |\\n\\n## 2. Median Difference (Importance - Random Phase Gradient)\\n\\n| Sparsity | Median Diff | 95% CI | Crosses Zero |\\n|----------|-------------|--------|--------------|\\n| s015 | 0.020257 | [0.001649, 0.043479] | False |\\n| s020 | 0.022135 | [-0.090492, 0.187002] | True |\\n| s025 | 0.094734 | [-0.003660, 0.302884] | True |\\n| s030 | 0.356166 | [-0.069057, 0.544225] | True |\\n\\n## 3. Phase Gradient Monotonicity\\n\\nd_z sequence: s015=0.1923, s020=0.2550, s025=0.2902, s030=0.3352\\nMonotonically increasing: **Yes**\\n\\n## 4. Phase Gradient d_z (Importance Condition Only)\\n\\n| Sparsity | d_z | 95% CI | Interpretation |\\n|----------|-----|--------|----------------|\\n| s015 | 1.0079 | [0.5930, 1.7025] | large |\\n| s020 | 1.1080 | [0.8144, 1.5698] | large |\\n| s025 | 1.1227 | [0.8735, 1.5768] | large |\\n| s030 | 1.0038 | [0.8099, 1.3519] | large |\\n\\n## 5. Cross-Architecture Comparison (LLaMA-8B vs DeepSeek-7B)\\n\\n| Sparsity | DeepSeek d_z | DeepSeek CI | LLaMA d_z | LLaMA CI | Delta |\\n|----------|-------------|-------------|-----------|----------|-------|\\n| s015 | 0.4416 | [0.3548, 0.7836] | 1.0079 | [0.5930, 1.7025] | 0.5663 |\\n| s020 | 0.5195 | [0.4319, 0.9011] | 1.1080 | [0.8144, 1.5698] | 0.5885 |\\n| s025 | 0.6831 | [0.5576, 0.8634] | 1.1227 | [0.8735, 1.5768] | 0.4396 |\\n| s030 | 0.
…[truncated 169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:54:09.059375+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"c4_think_validation_math500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:32:40.564Z\", \"updated_at\": \"2026-05-16T02:52:26.822Z\", \"spec\": {\"hypothesis\": \"验证 &lt;think> token 与 PPL-based phase segmentation 的一致性（Cohen's κ ≥ 0.80），回应 Reviewer 'phase segmentation validation' 质疑\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-500 problems 1-50\", \"data_count\": 50, \"server\": \"westd-22162\", \"seed\": 42, \"claims\": [\"C2\", \"C4\"], \"command\": \"python scripts/think_phase_kappa_v3.py\", \"checkpoint_path\": \"artifacts/think_phase_kappa_v3.json\", \"log_path\": \"scripts/think_phase_kappa_v3.py\"}, \"conclusion\": \"success\", \"metrics\": {\"adaptive_kappa\": 0.8804, \"per_problem_kappa_mean\": 0.8466, \"per_problem_kappa_median\": 0.8782, \"per_problem_auc_roc_mean\": 0.9808, \"per_problem_auc_roc_median\": 0.9854, \"pct_problems_kappa_ge_080\": 0.75, \"pct_problems_kappa_ge_060\": 1, \"token_level_accuracy\": 0.942, \"fixed_threshold_kappa\": 0.52, \"think_phase_sparsity\": 0.656, \"exec_phase_sparsity\": 0.763, \"phase_sparsity_cohens_d\": -0.8, \"think_fraction_mean\": 0.46, \"think_fraction_std\": 0.21}, \"completed_at\": \"2026-05-16T02:52:26.822Z\"}, \"c10_lang_switching\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:41:23.965Z\", \"updated_at\": \"2026-05-16T02:41:23.965Z\", \"spec\": {\"hypothesis\": \"检查 MATH-500 DS 各 sparsity 水平的 language switching rate，确认 s030 40% Chinese switching 是否随 sparsity 递增\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"existing MATH-500 evaluation outputs\", \"data_count\": 50, \"server\": \"westd-22162\", \"seed\": 42, \"claims\": [\"C2\"]}}, \"c9_gsm8k_power_analysis\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:41:22.330Z\", \"updated_at\": \"2026-05-16T02:41:22.330Z\", \"spec\": {\"hypothesis\": \"GSM8K ra
…[truncated 29447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:54:09.061587+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "filters": "{'status': 'DONE'}",
  "fields": "['status', 'conclusion', 'metrics']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "filters": "{'status': 'DONE'}",
    "fields": "['status', 'conclusion', 'metrics']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:54:09.062482+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"c9_gsm8k_power_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"c4_think_validation_math500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"adaptive_kappa\": 0.8804, \"per_problem_kappa_mean\": 0.8466, \"per_problem_kappa_median\": 0.8782, \"per_problem_auc_roc_mean\": 0.9808, \"per_problem_auc_roc_median\": 0.9854, \"pct_problems_kappa_ge_080\": 0.75, \"pct_problems_kappa_ge_060\": 1, \"token_level_accuracy\": 0.942, \"fixed_threshold_kappa\": 0.52, \"think_phase_sparsity\": 0.656, \"exec_phase_sparsity\": 0.763, \"phase_sparsity_cohens_d\": -0.8, \"think_fraction_mean\": 0.46, \"think_fraction_std\": 0.21}}, \"acc_ds_s030_8k_v2\": {\"status\": \"DONE\", \"metrics\": {\"accuracy\": 0.04, \"correct\": 2, \"total\": 50, \"truncation_rate\": 0.76, \"truncated_count\": 38, \"extraction_failures\": 3, \"non_truncated_accuracy\": 0.167, \"non_truncated_correct\": 2, \"non_truncated_total\": 12, \"max_new_tokens\": 8192, \"avg_tokens\": 6566.3, \"total_time_seconds\": 7095.1}, \"conclusion\": \"success\"}, \"acc_qw_s030_b1_8k\": {\"status\": \"DONE\", \"metrics\": {\"accuracy\": 0.14, \"correct\": 7, \"total\": 50, \"truncation_rate\": 0.04, \"truncated_count\": 2, \"extraction_failures\": 8, \"max_new_tokens\": 8192, \"total_time_seconds\": 886.7, \"batch\": \"b1_v2 (problems 1-50, 8k tokens)\", \"old_batch1_acc\": 0.14, \"old_batch1_correct\": 7, \"batch2_acc\": 0.24, \"batch2_correct\": 12, \"new_combined_n100_acc\": 0.19, \"new_combined_n100_correct\": 19}, \"conclusion\": \"negative\"}, \"acc_qw_s025_b1_8k\": {\"status\": \"DONE\", \"metrics\": {\"accuracy\": 0.32, \"correct\": 16, \"n_problems\": 50, \"truncation_rate\": 0.04, \"truncated_count\": 2, \"extraction_failures\": 6, \"avg_tokens\": 797.3, \"total_time_seconds\": 831.6}, \"conclusion\": \"negative\"}, \"acc_qw_s015_b1_8k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0
…[truncated 19107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:54:09.062885+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "c3_llama",
  "field": "metrics",
  "value": "{'model': 'DeepSeek-R1-Distill-Llama-8B', 'n_problems': 50, 'n_valid': 49, 'n_skipped': 1, 'conditions_completed': '8/8', 'n_bootstrap': 10000, 'bonferroni_k': 4, 'imp_vs_rand_dz': {'s015': 0.1923, 's020': 0.255, 's025': 0.2902, 's030': 0.3352}, 'imp_vs_rand_dz_ci': {'s015': [-0.0862, 0.496], 's020': [-0.0248, 0.5381], 's025': [0.0081, 0.6121], 's030': [0.0606, 0.6629]}, 'imp_vs_rand_dz_interpretation': {'s015': 'negligible', 's020': 'small', 's025': 'small', 's030': 'small'}, 'imp_vs_rand_dz_monotonic': True, 'phase_gradient_importance_dz': {'s015': 1.0079, 's020': 1.108, 's025': 1.1227, 's030': 1.0038}, 'phase_gradient_importance_dz_ci': {'s015': [0.593, 1.7025], 's020': [0.8144, 1.5698], 's025': [0.8735, 1.5768], 's030': [0.8099, 1.3519]}, 'phase_gradient_importance_interpretation': 'all_large', 'phase_gradient_random_dz': {'s015': 0.3497, 's020': 0.373, 's025': 0.4476, 's030': 0.4385}, 'phase_gradient_random_dz_ci': {'s015': [0.0665, 0.6916], 's020': [0.0868, 0.7335], 's025': [0.1669, 0.7698], 's030': [0.1966, 0.707]}, 'phase_gradient_random_interpretation': 'all_small', 'median_diff': {'s015': 0.0203, 's020': 0.0221, 's025': 0.0947, 's030': 0.3562}, 'median_diff_ci': {'s015': [0.0016, 0.0435], 's020': [-0.0905, 0.187], 's025': [-0.0037, 0.3029], 's030': [-0.0691, 0.5442]}, 'wilcoxon_p': {'s015': 0.0549, 's020': 0.0632, 's025': 0.0209, 's030': 0.0074}, 'wilcoxon_p_bonferroni': {'s015': 0.2195, 's020': 0.2527, 's025': 0.0834, 's030': 0.0294}, 'significant_bonferroni': {'s015': False, 's020': False, 's025': False, 's030': True}, 'cross_arch_comparison': {'deepseek_importance_dz': {'s015': 0.4416, 's020': 0.5195, 's025': 0.6831, 's030': 0.8031}, 'llama_importance_dz': {'s015': 1.0079, 's020': 1.108, 's025': 1.1227, 's030': 1.0038}, 'delta': {'s015': 0.5663, 's020': 0.5885, 's025': 0.4396, 's030': 0.2007}, 'note': 'LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large'}}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "c3_llama",
    "field": "metrics",
    "value": "{'model': 'DeepSeek-R1-Distill-Llama-8B', 'n_problems': 50, 'n_valid': 49, 'n_skipped': 1, 'conditions_completed': '8/8', 'n_bootstrap': 10000, 'bonferroni_k': 4, 'imp_vs_rand_dz': {'s015': 0.1923, 's020': 0.255, 's025': 0.2902, 's030': 0.3352}, 'imp_vs_rand_dz_ci': {'s015': [-0.0862, 0.496], 's020': [-0.0248, 0.5381], 's025': [0.0081, 0.6121], 's030': [0.0606, 0.6629]}, 'imp_vs_rand_dz_interpretation': {'s015': 'negligible', 's020': 'small', 's025': 'small', 's030': 'small'}, 'imp_vs_rand_dz_monotonic': True, 'phase_gradient_importance_dz': {'s015': 1.0079, 's020': 1.108, 's025': 1.1227, 's030': 1.0038}, 'phase_gradient_importance_dz_ci': {'s015': [0.593, 1.7025], 's020': [0.8144, 1.5698], 's025': [0.8735, 1.5768], 's030': [0.8099, 1.3519]}, 'phase_gradient_importance_interpretation': 'all_large', 'phase_gradient_random_dz': {'s015': 0.3497, 's020': 0.373, 's025': 0.4476, 's030': 0.4385}, 'phase_gradient_random_dz_ci': {'s015': [0.0665, 0.6916], 's020': [0.0868, 0.7335], 's025': [0.1669, 0.7698], 's030': [0.1966, 0.707]}, 'phase_gradient_random_interpretation': 'all_small', 'median_diff': {'s015': 0.0203, 's020': 0.0221, 's025': 0.0947, 's030': 0.3562}, 'median_diff_ci': {'s015': [0.0016, 0.0435], 's020': [-0.0905, 0.187], 's025': [-0.0037, 0.3029], 's030': [-0.0691, 0.5442]}, 'wilcoxon_p': {'s015': 0.0549, 's020': 0.0632, 's025': 0.0209, 's030': 0.0074}, 'wilcoxon_p_bonferroni': {'s015': 0.2195, 's020': 0.2527, 's025': 0.0834, 's030': 0.0294}, 'significant_bonferroni': {'s015': False, 's020': False, 's025': False, 's030': True}, 'cross_arch_comparison': {'deepseek_importance_dz': {'s015': 0.4416, 's020': 0.5195, 's025': 0.6831, 's030': 0.8031}, 'llama_importance_dz': {'s015': 1.0079, 's020': 1.108, 's025': 1.1227, 's030': 1.0038}, 'delta': {'s015': 0.5663, 's020': 0.5885, 's025': 0.4396, 's030': 0.2007}, 'note': 'LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large'}}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T02:54:09.063321+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"c3_llama\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:34:06.637Z\", \"updated_at\": \"2026-05-16T02:54:01.512Z\", \"hypothesis\": \"C3: LLaMA 架构验证。用 DeepSeek-R1-Distill-Llama-8B 验证 phase-modulated compound severity 是否跨架构复现（Qwen2ForCausalLM → LlamaForCausalLM），回应审稿人\\\"cross-model ≠ cross-architecture\\\"质疑。\", \"spec\": {\"command\": \"bash run_c3_llama_full.sh\", \"server\": \"westd-22162\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Llama-8B\", \"seed\": null, \"gpu\": \"cuda:2,cuda:3\", \"pid\": \"138393 (parent), 138408 (importance gpu2), 138410 (random gpu3)\", \"note\": \"sp_str bug fixed: bc unavailable → python3. Old s000 output deleted (12/50 incomplete). All 8 conditions restarting from scratch.\", \"pids\": {\"importance_gpu2\": 138408, \"random_gpu3\": 138410, \"parent\": 138398}, \"conditions\": \"importance×{0.15,0.20,0.25,0.30} + random×{0.15,0.20,0.25,0.30}\", \"gpu_allocation\": \"GPU2=importance, GPU3=random\"}, \"notes\": \"8/8 conditions complete. Analysis output: analysis_output/c3_llama_{results,cohens_d,report}.*. Phase gradient d_z monotonically increasing (0.19→0.26→0.29→0.34). Cross-architecture pattern confirmed: LLaMA shows large phase gradient d_z ~1.0 across all sparsity levels, consistent qualitative direction with DeepSeek/Qwen. s030 Wilcoxon significant (p=0.029 Bonferroni). s015 median diff CI [0.002, 0.043] does not cross zero.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_c3_llama_{importance,random}_s{015,020,025,030}\", \"log_path\": \"/root/autodl-tmp/pacs/logs/c3_llama_{importance,random}_s{015,020,025,030}.log\", \"completed_at\": \"2026-05-14T17:57:09.264Z\", \"metrics\": {\"model\": \"DeepSeek-R1-Distill-Llama-8B\", \"n_problems\": 50, \"n_valid\": 49, \"n_skipped\": 1, \"conditions_completed\": \"8/
…[truncated 2048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T02:54:09.063731+00:00_

写入成功。完整 metrics 结构：

| 字段 | 值 |
|------|-----|
| **imp_vs_rand d_z** | s015=0.19, s020=0.26, s025=0.29, s030=0.34（单调递增） |
| **phase_gradient_importance d_z** | 全部 large（1.00–1.12） |
| **phase_gradient_random d_z** | 全部 small（0.35–0.45） |
| **s030 Bonferroni p** | 0.029（显著） |
| **cross_arch delta** | LLaMA d_z 比 DeepSeek 高 0.20–0.59 |

Registry `c3_llama` metrics 字段已更新，包含 imp_vs_rand_dz、phase_gradient_{importance,random}_dz、median_diff、wilcoxon_p（含 Bonferroni 校正）、CI、cross_arch_comparison 等全部结构化数值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_registry_c3_llama_metrics_backfill_20260516T025245"
}
```

</details>

---
