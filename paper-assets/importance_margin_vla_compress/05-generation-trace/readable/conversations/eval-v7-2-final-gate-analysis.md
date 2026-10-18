# eval v7 2 final gate analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_eval_v7_2-final-gate-analysis_20260515T230441.jsonl`
- **Structured JSON:** [`8cfe1ccd1173f08c8b2e.json`](../../sessions/8c/8cfe1ccd1173f08c8b2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-15T23:05:31.044887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T23:05:31.045252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:05:31.045437+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_imm_v7_2_final.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_imm_v7_2_final.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T23:05:31.045569+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'mvp_imm_anchor_v7'}",
  "project": "importance_margin_vla_compress",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'mvp_imm_anchor_v7'}",
    "project": "importance_margin_vla_compress",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T23:05:31.045784+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eps0.0_pruneFalse\\\": {\\n    \\\"action_loss\\\": 0.013010345310205593,\\n    \\\"margin_mean\\\": 0.9435573816299438,\\n    \\\"margin_median\\\": 0.6627011299133301,\\n    \\\"margin_std\\\": 0.881189227104187,\\n    \\\"margin_min\\\": 0.0002582073211669922,\\n    \\\"margin_max\\\": 6.517972946166992,\\n    \\\"preservation_rate\\\": 1.0,\\n    \\\"kendall_tau\\\": 1.0,\\n    \\\"certified_bound_mean\\\": 0.3068249225616455,\\n    \\\"certified_bound_max\\\": 1.0,\\n    \\\"l_eps_delta_ratio_mean\\\": 1.074245572090149,\\n    \\\"l_eps_delta_ratio_median\\\": 0.16381829977035522\\n  },\\n  \\\"eps0.0_pruneTrue\\\": {\\n    \\\"action_loss\\\": 0.01463813268346712,\\n    \\\"margin_mean\\\": 0.9544364809989929,\\n    \\\"margin_median\\\": 0.680659294128418,\\n    \\\"margin_std\\\": 0.8860161304473877,\\n    \\\"margin_min\\\": 0.00040149688720703125,\\n    \\\"margin_max\\\": 6.60963249206543,\\n    \\\"preservation_rate\\\": 1.0,\\n    \\\"kendall_tau\\\": 1.0,\\n    \\\"certified_bound_mean\\\": 0.29706352949142456,\\n    \\\"certified_bound_max\\\": 1.0,\\n    \\\"l_eps_delta_ratio_mean\\\": 0.9499572515487671,\\n    \\\"l_eps_delta_ratio_median\\\": 0.15915440022945404\\n  },\\n  \\\"eps0.01_pruneFalse\\\": {\\n    \\\"action_loss\\\": 0.01240322061488405,\\n    \\\"margin_mean\\\": 0.9652565717697144,\\n    \\\"margin_median\\\": 0.670074462890625,\\n    \\\"margin_std\\\": 0.887263834476471,\\n    \\\"margin_min\\\": 0.00012540817260742188,\\n    \\\"margin_max\\\": 5.5614118576049805,\\n    \\\"preservation_rate\\\": 0.9253029227256775,\\n    \\\"kendall_tau\\\": 0.7795423865318298,\\n    \\\"certified_bound_mean\\\": 0.2970312833786011,\\n    \\\"certified_bound_max\\\": 1.0,\\n    \\\"l_eps_delta_ratio_mean\\\": 1.6824694871902466,\\n    \\\"l_eps_delta_ratio_median\\\": 0.16196206212043762\\n  },\\n  \\\"eps0.01_pruneTrue\\\": {\\n    \\\"action_loss\\\": 0.014826250161626376,\\n    \
…[truncated 3600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:05:31.045940+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0313}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:05:31.046098+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "limit": "10",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "limit": "10",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:05:31.046460+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"mvp_imm_anchor_v7_2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:18:02.766Z\", \"updated_at\": \"2026-05-15T23:05:05.010Z\", \"hypothesis\": \"v7.1 重跑 (metrics.py eval mode leak 修复后): lambda_margin=0.2, grad_clip=30.0\", \"parent\": null, \"spec\": {\"checkpoint_path\": \"checkpoints/imm_anchor_v7_1/step_029999\", \"log_path\": \"/tmp/imm_anchor_v7_2.log\"}, \"notes\": \"v7.2 final eval (fixed soft forward + temperature): G1 PASS 64.25x, G2 PASS +47.46pp, G3 FAIL 3.19x (vs v7's 3.28x — barely better despite lambda 0.5→0.2), G4 PASS 0.323. Bypass-ACIS diagnostic: G3=1.91x >> 1.10 → 权重受损确认，不是 selection mechanism overhead。IMM 梯度回传通过 LoRA 污染了 VLM backbone。附注: pruneTrue 条件下 v7.2 远优于 baseline (0.24x ratio)，说明 IMM 训练确实提升了 token importance 鲁棒性，但代价是 clean performance。\", \"metrics\": {\"eval_500batch_soft\": {\"clean_action_loss\": 0.013, \"clean_margin_median\": 0.6627, \"clean_preservation\": 1, \"eps001_preservation\": 0.9253, \"eps002_preservation\": 0.8482, \"eps005_preservation\": 0.6597, \"eps001_led_median\": 0.162, \"eps002_led_median\": 0.3232, \"eps005_led_median\": 0.7656, \"lipschitz_empirical\": 0.3393, \"lipschitz_spectral\": 1.0672}, \"bypass_acis\": {\"clean_action_loss\": 0.0078, \"g3_ratio\": 1.91, \"conclusion\": \"weights_damaged\"}, \"gate_v7_2\": {\"G1_margin_ratio\": 64.25, \"G1_pass\": true, \"G2_preservation_diff_pp\": 47.46, \"G2_pass\": true, \"G3_action_loss_ratio\": 3.19, \"G3_pass\": false, \"G4_led_median\": 0.323, \"G4_pass\": true, \"overall\": \"FAIL\"}, \"source\": \"eval_results/eval_imm_v7_2_final.json + eval_results/eval_imm_v7_2_bypass_acis.json\"}, \"conclusion\": \"negative\"}, \"mvp_baseline_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:36:06.963Z\", \"updated_at\": \"2026-05-15T22:21:59.760Z\", \"spec\": {\"server\": \"westd-27271\", \"gpu\": \"cuda:0\", \"pid\": 31871, \"command\": \"CUDA_VISIBLE_D
…[truncated 12283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:05:31.046623+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --baseline eval_results/eval_baseline_v5_final.json --imm eval_results/eval_imm_v7_2_final.json --output eval_results/gate_report_v7_2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --baseline eval_results/eval_baseline_v5_final.json --imm eval_results/eval_imm_v7_2_final.json --output eval_results/gate_report_v7_2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:05:31.046770+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --baseline eval_results/eval_baseline_v5_final.json --imm eval_results/eval_imm_v7_2_final.json --output eval_results/gate_report_v7_2.json'\\n\\nExit code: 1\\n\\nStdout:\\n\\n  [FAIL] G3: Clean action loss ratio ≤ 1.10\\n         value=3.1912  threshold=≤ 1.10\\n  [PASS] G4: LED ratio median < 1.0 (certified bound)\\n         value=0.3232  threshold=< 1.0\\n\\n================================================================\\n  OVERALL VERDICT: FAIL\\n================================================================\\n\\nDetailed results saved to eval_results/gate_report_v7_2.json\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:05:31.046937+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/gate_report_v7_2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/gate_report_v7_2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:05:31.047106+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conditions_evaluated\\\": [\\n    \\\"eps0.01_pruneFalse\\\",\\n    \\\"eps0.02_pruneFalse\\\",\\n    \\\"eps0.05_pruneFalse\\\"\\n  ],\\n  \\\"per_condition\\\": {\\n    \\\"eps0.01_pruneFalse\\\": {\\n      \\\"margin_ratio\\\": 64.87381845461366,\\n      \\\"bl_margin_median\\\": 0.010328888893127441,\\n      \\\"imm_margin_median\\\": 0.670074462890625,\\n      \\\"pres_diff\\\": 0.5900704264640808,\\n      \\\"bl_preservation\\\": 0.3352324962615967,\\n      \\\"imm_preservation\\\": 0.9253029227256775,\\n      \\\"imm_led_median\\\": 0.16196206212043762\\n    },\\n    \\\"eps0.02_pruneFalse\\\": {\\n      \\\"margin_ratio\\\": 63.20752896835635,\\n      \\\"bl_margin_median\\\": 0.010627388954162598,\\n      \\\"imm_margin_median\\\": 0.6717309951782227,\\n      \\\"pres_diff\\\": 0.5120221078395844,\\n      \\\"bl_preservation\\\": 0.3362119495868683,\\n      \\\"imm_preservation\\\": 0.8482340574264526,\\n      \\\"imm_led_median\\\": 0.32316556572914124\\n    },\\n    \\\"eps0.05_pruneFalse\\\": {\\n      \\\"margin_ratio\\\": 64.66915761609603,\\n      \\\"bl_margin_median\\\": 0.010943293571472168,\\n      \\\"imm_margin_median\\\": 0.7076935768127441,\\n      \\\"pres_diff\\\": 0.3216330409049988,\\n      \\\"bl_preservation\\\": 0.3380565047264099,\\n      \\\"imm_preservation\\\": 0.6596895456314087,\\n      \\\"imm_led_median\\\": 0.765597403049469\\n    }\\n  },\\n  \\\"gate\\\": {\\n    \\\"G1_margin_median_ratio\\\": {\\n      \\\"value\\\": 64.25016834635535,\\n      \\\"threshold\\\": \\\"\\\\u2265 2.0\\\",\\n      \\\"pass\\\": true\\n    },\\n    \\\"G2_preservation_rate_diff\\\": {\\n      \\\"value\\\": 0.4745751917362213,\\n      \\\"threshold\\\": \\\"\\\\u2265 0.10\\\",\\n      \\\"pass\\\": true\\n    },\\n    \\\"G3_clean_action_loss_ratio\\\": {\\n      \\\"value\\\": 3.191162079988599,\\n      \\\"threshold\\\": \\\"\\\\u2264 1.10\\\",\\n      \\\"bl_loss\\\": 0.00407699
…[truncated 401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T23:05:31.047315+00:00_

Gate 报告已读取。Registry 中 `mvp_imm_anchor_v7_2` 已有 metrics 字段（含 eval_500batch_soft、bypass_acis、gate_v7_2），内容与本次分析一致，无需再更新。

## Gate Report v7.2 完整结果

### Per-condition 详情

| Condition | Margin Ratio | BL Margin | IMM Margin | Pres Diff | BL Pres | IMM Pres | LED Median |
|---|---|---|---|---|---|---|---|
| eps0.01 | 64.87x | 0.0103 | 0.6701 | +59.00pp | 0.3352 | 0.9253 | 0.162 |
| eps0.02 | 63.21x | 0.0106 | 0.6717 | +51.20pp | 0.3362 | 0.8482 | 0.323 |
| eps0.05 | 64.67x | 0.0109 | 0.7077 | +32.16pp | 0.3381 | 0.6597 | 0.766 |

### Gate 判定

| Gate | Metric | Value | Threshold | Result |
|---|---|---|---|---|
| **G1** | Margin median ratio | **64.25x** | ≥ 2.0 | **PASS** |
| **G2** | Preservation diff | **+47.46pp** | ≥ +10pp | **PASS** |
| **G3** | Clean action loss ratio | **3.19x** | ≤ 1.10 | **FAIL** |
| **G4** | LED median | **0.323** | < 1.0 | **PASS** |

### **OVERALL: FAIL**

G3 失败：clean action loss 0.01301 vs baseline 0.00408，比值 3.19x（阈值 ≤ 1.10）。与 v7 的 3.28x 相比仅微幅改善，lambda 从 0.5 降到 0.2 未能实质解决 clean performance 退化问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_v7_2-final-gate-analysis_20260515T230441"
}
```

</details>

---
