# analysis exp 058 ddr causality

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_exp_058_ddr_causality_20260520T075058.jsonl`
- **Structured JSON:** [`aa278e0d4f87e792c4ef.json`](../../sessions/aa/aa278e0d4f87e792c4ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-20T07:52:42.187966+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T07:52:42.188264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T07:52:42.188422+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "cat /root/gen-depth-fingerprint/results/ddr_causal_permutation.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "cat /root/gen-depth-fingerprint/results/ddr_causal_permutation.json"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T07:52:42.188656+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"permutation\\\": {\\n    \\\"hapax_ratio\\\": {\\n      \\\"mean_importance\\\": 0.235,\\n      \\\"std_importance\\\": 0.0543,\\n      \\\"per_fold\\\": {\\n        \\\"llama-3.2-3b\\\": 0.2492,\\n        \\\"mistral-7b-v0.3\\\": 0.1098,\\n        \\\"olmo-2-1b\\\": 0.2573,\\n        \\\"pythia-1b\\\": 0.2842,\\n        \\\"pythia-2.8b\\\": 0.2545,\\n        \\\"qwen3-0.6b\\\": 0.2786,\\n        \\\"qwen3-1.7b\\\": 0.2567,\\n        \\\"qwen3-8b\\\": 0.19\\n      }\\n    },\\n    \\\"ttr\\\": {\\n      \\\"mean_importance\\\": 0.1564,\\n      \\\"std_importance\\\": 0.0531,\\n      \\\"per_fold\\\": {\\n        \\\"llama-3.2-3b\\\": 0.1411,\\n        \\\"mistral-7b-v0.3\\\": 0.0396,\\n        \\\"olmo-2-1b\\\": 0.1777,\\n        \\\"pythia-1b\\\": 0.2162,\\n        \\\"pythia-2.8b\\\": 0.1956,\\n        \\\"qwen3-0.6b\\\": 0.1812,\\n        \\\"qwen3-1.7b\\\": 0.1849,\\n        \\\"qwen3-8b\\\": 0.1151\\n      }\\n    },\\n    \\\"entropy_mean\\\": {\\n      \\\"mean_importance\\\": 0.1698,\\n      \\\"std_importance\\\": 0.0384,\\n      \\\"per_fold\\\": {\\n        \\\"llama-3.2-3b\\\": 0.165,\\n        \\\"mistral-7b-v0.3\\\": 0.0903,\\n        \\\"olmo-2-1b\\\": 0.1891,\\n        \\\"pythia-1b\\\": 0.224,\\n        \\\"pythia-2.8b\\\": 0.194,\\n        \\\"qwen3-0.6b\\\": 0.1955,\\n        \\\"qwen3-1.7b\\\": 0.1589,\\n        \\\"qwen3-8b\\\": 0.1412\\n      }\\n    },\\n    \\\"entropy_std\\\": {\\n      \\\"mean_importance\\\": 0.0566,\\n      \\\"std_importance\\\": 0.0128,\\n      \\\"per_fold\\\": {\\n        \\\"llama-3.2-3b\\\": 0.0665,\\n        \\\"mistral-7b-v0.3\\\": 0.0441,\\n        \\\"olmo-2-1b\\\": 0.047,\\n        \\\"pythia-1b\\\": 0.0784,\\n        \\\"pythia-2.8b\\\": 0.0728,\\n        \\\"qwen3-0.6b\\\": 0.0499,\\n        \\\"qwen3-1.7b\\\": 0.0473,\\n        \\\"qwen3-8b\\\": 0.0466\\n      }\\n    },\\n    \\\"entropy_min\\\": {\\n      \\\"mean_importance\\\": 0.0186,\\n 
…[truncated 2161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T07:52:42.188832+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "cat /root/gen-depth-fingerprint/results/ddr_causal_granger.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "cat /root/gen-depth-fingerprint/results/ddr_causal_granger.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T07:52:42.189174+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"granger\\\": {\\n    \\\"hapax_ratio\\\": {\\n      \\\"F_stat\\\": 270.5989,\\n      \\\"p_value\\\": 0.0,\\n      \\\"p_value_str\\\": \\\"0.00e+00\\\",\\n      \\\"r2_restricted\\\": 0.3817,\\n      \\\"r2_full\\\": 0.3874,\\n      \\\"delta_r2\\\": 0.0057,\\n      \\\"significant_005\\\": true,\\n      \\\"depth_coefficient\\\": 0.019137,\\n      \\\"n_obs\\\": 29095\\n    },\\n    \\\"ttr\\\": {\\n      \\\"F_stat\\\": 515.9977,\\n      \\\"p_value\\\": 0.0,\\n      \\\"p_value_str\\\": \\\"0.00e+00\\\",\\n      \\\"r2_restricted\\\": 0.4808,\\n      \\\"r2_full\\\": 0.4899,\\n      \\\"delta_r2\\\": 0.009,\\n      \\\"significant_005\\\": true,\\n      \\\"depth_coefficient\\\": 0.024931,\\n      \\\"n_obs\\\": 29095\\n    },\\n    \\\"entropy_mean\\\": {\\n      \\\"F_stat\\\": 399.6411,\\n      \\\"p_value\\\": 0.0,\\n      \\\"p_value_str\\\": \\\"0.00e+00\\\",\\n      \\\"r2_restricted\\\": 0.4373,\\n      \\\"r2_full\\\": 0.4449,\\n      \\\"delta_r2\\\": 0.0076,\\n      \\\"significant_005\\\": true,\\n      \\\"depth_coefficient\\\": -0.088874,\\n      \\\"n_obs\\\": 29095\\n    },\\n    \\\"entropy_std\\\": {\\n      \\\"F_stat\\\": 1338.3466,\\n      \\\"p_value\\\": 0.0,\\n      \\\"p_value_str\\\": \\\"0.00e+00\\\",\\n      \\\"r2_restricted\\\": 0.2952,\\n      \\\"r2_full\\\": 0.3262,\\n      \\\"delta_r2\\\": 0.031,\\n      \\\"significant_005\\\": true,\\n      \\\"depth_coefficient\\\": -0.041391,\\n      \\\"n_obs\\\": 29095\\n    },\\n    \\\"entropy_min\\\": {\\n      \\\"F_stat\\\": 0.3788,\\n      \\\"p_value\\\": 0.5382264300966464,\\n      \\\"p_value_str\\\": \\\"5.38e-01\\\",\\n      \\\"r2_restricted\\\": 0.0107,\\n      \\\"r2_full\\\": 0.0107,\\n      \\\"delta_r2\\\": 0.0,\\n      \\\"significant_005\\\": false,\\n      \\\"depth_coefficient\\\": -0.000974,\\n      \\\"n_obs\\\": 29095\\n    },\\n    \\\"entropy_max\\\": {\\n      \\\"F_stat\\\": 22.9668,\\n      \\\
…[truncated 8370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T07:52:42.189345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "cat /root/gen-depth-fingerprint/results/ddr_causal_intervention.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "cat /root/gen-depth-fingerprint/results/ddr_causal_intervention.json"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T07:52:42.189476+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-18868",
  "command": "tail -50 /root/runs/gen-depth-fingerprint/exp_058_ddr_causality.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-18868",
    "command": "tail -50 /root/runs/gen-depth-fingerprint/exp_058_ddr_causality.log"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T07:52:42.189636+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"intervention\\\": {\\n    \\\"hapax_ratio\\\": {\\n      \\\"mean_f1_drop\\\": 0.0062,\\n      \\\"std_f1_drop\\\": 0.0009\\n    },\\n    \\\"ttr\\\": {\\n      \\\"mean_f1_drop\\\": 0.0073,\\n      \\\"std_f1_drop\\\": 0.0008\\n    },\\n    \\\"entropy_mean\\\": {\\n      \\\"mean_f1_drop\\\": 0.0112,\\n      \\\"std_f1_drop\\\": 0.0007\\n    },\\n    \\\"entropy_std\\\": {\\n      \\\"mean_f1_drop\\\": 0.0095,\\n      \\\"std_f1_drop\\\": 0.0008\\n    },\\n    \\\"entropy_min\\\": {\\n      \\\"mean_f1_drop\\\": 0.0061,\\n      \\\"std_f1_drop\\\": 0.0009\\n    },\\n    \\\"entropy_max\\\": {\\n      \\\"mean_f1_drop\\\": 0.0203,\\n      \\\"std_f1_drop\\\": 0.0011\\n    },\\n    \\\"tail_decay\\\": {\\n      \\\"mean_f1_drop\\\": 0.0069,\\n      \\\"std_f1_drop\\\": 0.0009\\n    },\\n    \\\"_baseline_avg_f1\\\": 0.7714\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T07:52:42.189807+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Depths: [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4)]\\nFeatures: ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay']\\n\\n\\n=== Granger Causality ===\\n  WARNING: Depth chains have only T=5 points per seed.\\n  Per-seed Granger tests have negligible statistical power.\\n  Primary results use pooled panel regression across seeds.\\n\\n  Panel: 29095 obs from 7963 seed chains\\n  Requested max_lag=2, but using lag=1 (T=5 constraint)\\n\\n  Feature             F-stat      p-value  R2_full  R2_rest      dR2   Sig\\n  ----------------------------------------------------------------------\\n  hapax_ratio         270.60     0.00e+00   0.3874   0.3817   0.0057   ***\\n  ttr                 516.00     0.00e+00   0.4899   0.4808   0.0090   ***\\n  entropy_mean        399.64     0.00e+00   0.4449   0.4373   0.0076   ***\\n  entropy_std        1338.35     0.00e+00   0.3262   0.2952   0.0310   ***\\n  entropy_min           0.38     5.38e-01   0.0107   0.0107   0.0000      \\n  entropy_max          22.97     1.66e-06   0.0220   0.0212   0.0008   ***\\n  tail_decay           17.81     2.44e-05   0.4891   0.4888   0.0003   ***\\n\\n  Per-generator pooled Granger (lag=1):\\n\\n  Fisher's combined p-values across 8 generators:\\n    hapax_ratio      chi2= 1594.53  p=0.00e+00  ***\\n    ttr              chi2= 5624.71  p=0.00e+00  ***\\n    entropy_mean     chi2= 6951.35  p=0.00e+00  ***\\n    entropy_std      chi2=11052.41  p=0.00e+00  ***\\n    entropy_min      chi2=   17.16  p=3.75e-01  \\n    entropy_max      chi2=   75.91  p=9.02e-10  ***\\n    tail_decay       chi2=   92.52  p=8.57e-13  ***\\n\\nSaved: results/ddr_causal_granger.json\\nLoaded 37058 rows, 8 generators\\nDepths: [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4)]\\nFeatures: ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay']\\n\\n===
…[truncated 543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T07:52:42.190002+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T07:52:42.190127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T07:52:42.190245+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T07:52:42.190384+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md\", \"content\": \"# Memory — gen-depth-fingerprint\\n\\n## 独立种子控制实验 (2026-05-18)\\n- exp_051: 完全不共享种子的 cross-generator 评估 F1=0.680，与 shared-seed LOGO 0.694 差 -1.4pp\\n- 两方向: Pythia→OLMo 0.695, OLMo→Pythia 0.666\\n- 与 seed demeaning (F1=0.701) 形成收敛证据：depth signal 非 topic artifact\\n- 0.680 略低于 LOGO 合理：独立种子 = strict cross-generator transfer，比 LOGO 更严格\\n\\n## 温度曲线关键约束 (2026-05-17)\\n- autodl-5090 容器只有 1 张可见 GPU（非 4 张），所有 GPU 实验必须串行\\n- top_p 必须固定为 0.9（与主实验一致），不同温度下不能改 top_p\\n\\n## 模型版本确认 (2026-05-17)\\n- Qwen3 系列: Qwen/Qwen3-0.6B, Qwen/Qwen3-1.7B, Qwen/Qwen3-8B（HuggingFace 上可用）\\n- 主实验用 8 个 base model generators: Pythia-1B, Pythia-2.8B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, Llama-3.2-3B, Mistral-7B\\n\\n## Downstream utility 负面结果 (2026-05-16)\\n- plan-004-v2: depth-aware curation 不优于随机抽样（all > size_matched > depth01 ≈ binary_filtered >> depth0_only）\\n- 已 reframe 为 diagnostic-not-curative（D009 决策）\\n- 跨 seed 方差极小 (<0.002)，结论稳健\\n\\n## 竞品实验参考\\n- 暂无直接竞品（depth classification 是新任务）\\n- 最近的 baseline: FastDetectGPT, Binoculars, LD-Score（均为 binary detection，非 depth）\\n\", \"total_chars\": 1019, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T07:52:42.190525+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "filters": "{'exp_id': 'exp_058_ddr_causality'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "filters": "{'exp_id': 'exp_058_ddr_causality'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T07:52:42.190672+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.159}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T07:52:42.190838+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "memory.md",
  "content": "# Memory — gen-depth-fingerprint\n\n## DDR 因果性分析 (2026-05-20, exp_058)\n- **Permutation importance**: drifting 组均值 0.158 vs stationary 组 0.030（5.3x），hapax_ratio 最强 (0.235)，tail_decay 最弱 (0.014)\n- **Granger causality**: 6/7 特征显著（panel N=29095, lag=1）；entropy_min 唯一不显著（pooled p=0.538, Fisher p=0.375）；最大 ΔR²=entropy_std 0.031；方向: hapax_ratio/ttr 随 depth 递增，entropy 系列递减\n- **Intervention**: 所有 7 特征干预后 F1 下降 0.6–2.0pp；entropy_max 最大（2.0pp），entropy_min 最小（0.6pp）\n- **结论**: hypothesis 成立（success）——DDR 特征对 depth 有因果预测力，超越相关性\n- **注意**: entropy_min 是最弱特征（Granger 不显著、permutation 最低），但仍有干预效果；T=5 限制导致只能用 lag=1\n\n## 独立种子控制实验 (2026-05-18)\n- exp_051: 完全不共享种子的 cross-generator 评估 F1=0.680，与 shared-seed LOGO 0.694 差 -1.4pp\n- 两方向: Pythia→OLMo 0.695, OLMo→Pythia 0.666\n- 与 seed demeaning (F1=0.701) 形成收敛证据：depth signal 非 topic artifact\n- 0.680 略低于 LOGO 合理：独立种子 = strict cross-generator transfer，比 LOGO 更严格\n\n## 温度曲线关键约束 (2026-05-17)\n- autodl-5090 容器只有 1 张可见 GPU（非 4 张），所有 GPU 实验必须串行\n- top_p 必须固定为 0.9（与主实验一致），不同温度下不能改 top_p\n\n## 模型版本确认 (2026-05-17)\n- Qwen3 系列: Qwen/Qwen3-0.6B, Qwen/Qwen3-1.7B, Qwen/Qwen3-8B（HuggingFace 上可用）\n- 主实验用 8 个 base model generators: Pythia-1B, Pythia-2.8B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, Llama-3.2-3B, Mistral-7B\n\n## Downstream utility 负面结果 (2026-05-16)\n- plan-004-v2: depth-aware curation 不优于随机抽样（all > size_matched > depth01 ≈ binary_filtered >> depth0_only）\n- 已 reframe 为 diagnostic-not-curative（D009 决策）\n- 跨 seed 方差极小 (<0.002)，结论稳健\n\n## 竞品实验参考\n- 暂无直接竞品（depth classification 是新任务）\n- 最近的 baseline: FastDetectGPT, Binoculars, LD-Score（均为 binary detection，非 depth）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "memory.md",
    "content": "# Memory — gen-depth-fingerprint\n\n## DDR 因果性分析 (2026-05-20, exp_058)\n- **Permutation importance**: drifting 组均值 0.158 vs stationary 组 0.030（5.3x），hapax_ratio 最强 (0.235)，tail_decay 最弱 (0.014)\n- **Granger causality**: 6/7 特征显著（panel N=29095, lag=1）；entropy_min 唯一不显著（pooled p=0.538, Fisher p=0.375）；最大 ΔR²=entropy_std 0.031；方向: hapax_ratio/ttr 随 depth 递增，entropy 系列递减\n- **Intervention**: 所有 7 特征干预后 F1 下降 0.6–2.0pp；entropy_max 最大（2.0pp），entropy_min 最小（0.6pp）\n- **结论**: hypothesis 成立（success）——DDR 特征对 depth 有因果预测力，超越相关性\n- **注意**: entropy_min 是最弱特征（Granger 不显著、permutation 最低），但仍有干预效果；T=5 限制导致只能用 lag=1\n\n## 独立种子控制实验 (2026-05-18)\n- exp_051: 完全不共享种子的 cross-generator 评估 F1=0.680，与 shared-seed LOGO 0.694 差 -1.4pp\n- 两方向: Pythia→OLMo 0.695, OLMo→Pythia 0.666\n- 与 seed demeaning (F1=0.701) 形成收敛证据：depth signal 非 topic artifact\n- 0.680 略低于 LOGO 合理：独立种子 = strict cross-generator transfer，比 LOGO 更严格\n\n## 温度曲线关键约束 (2026-05-17)\n- autodl-5090 容器只有 1 张可见 GPU（非 4 张），所有 GPU 实验必须串行\n- top_p 必须固定为 0.9（与主实验一致），不同温度下不能改 top_p\n\n## 模型版本确认 (2026-05-17)\n- Qwen3 系列: Qwen/Qwen3-0.6B, Qwen/Qwen3-1.7B, Qwen/Qwen3-8B（HuggingFace 上可用）\n- 主实验用 8 个 base model generators: Pythia-1B, Pythia-2.8B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, Llama-3.2-3B, Mistral-7B\n\n## Downstream utility 负面结果 (2026-05-16)\n- plan-004-v2: depth-aware curation 不优于随机抽样（all > size_matched > depth01 ≈ binary_filtered >> depth0_only）\n- 已 reframe 为 diagnostic-not-curative（D009 决策）\n- 跨 seed 方差极小 (<0.002)，结论稳健\n\n## 竞品实验参考\n- 暂无直接竞品（depth classification 是新任务）\n- 最近的 baseline: FastDetectGPT, Binoculars, LD-Score（均为 binary detection，非 depth）\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T07:52:42.191038+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T07:52:42.191180+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_058_ddr_causality",
  "field": "conclusion",
  "value": "success",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_058_ddr_causality",
    "field": "conclusion",
    "value": "success",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T07:52:42.191350+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_058_ddr_causality\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:05:46.902Z\", \"updated_at\": \"2026-05-20T07:52:16.040Z\", \"hypothesis\": \"DDR features have causal predictive power for depth beyond correlation: permutation importance confirms each feature group (drifting/stationary) contributes independently, and Granger causality tests show depth-t features predict depth-(t+1) features beyond autoregressive baseline, establishing temporal causal direction in the generation chain\", \"notes\": \"脚本 444 行，3 模块（permutation/granger/intervention）已实现并 dry-run 验证。全部 CPU-bound，不需要 GPU。数据: features_8gen.csv 37058 行。预估: Granger ~2min, Permutation ~15min, Intervention ~45min，可并行。\", \"server\": \"bjb2-18868\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python3 scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 --output results/ddr_causal_permutation.json && python3 scripts/ddr_causal_analysis.py --module granger --output results/ddr_causal_granger.json && python3 scripts/ddr_causal_analysis.py --module intervention --n-repeats 30 --output results/ddr_causal_intervention.json\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:1\"], \"pid\": \"179978\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_058_ddr_causality.log\", \"submitted_at\": \"2026-05-20T07:33:06.935Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"179978\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_058_ddr_causality.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python3 scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 --output results/ddr_causal_permutation.json && pyt
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T07:52:42.191504+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_058_ddr_causality",
  "field": "metrics",
  "value": "{'permutation_baseline_f1': 0.7714, 'drifting_avg_importance': 0.1578, 'stationary_avg_importance': 0.0297, 'drifting_stationary_ratio': 5.31, 'granger_significant_features': '6/7', 'granger_max_delta_r2': 0.031, 'granger_max_delta_r2_feature': 'entropy_std', 'granger_nonsig_feature': 'entropy_min', 'granger_panel_n': 29095, 'intervention_max_f1_drop': 0.0203, 'intervention_max_feature': 'entropy_max', 'intervention_min_f1_drop': 0.0061}",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_058_ddr_causality",
    "field": "metrics",
    "value": "{'permutation_baseline_f1': 0.7714, 'drifting_avg_importance': 0.1578, 'stationary_avg_importance': 0.0297, 'drifting_stationary_ratio': 5.31, 'granger_significant_features': '6/7', 'granger_max_delta_r2': 0.031, 'granger_max_delta_r2_feature': 'entropy_std', 'granger_nonsig_feature': 'entropy_min', 'granger_panel_n': 29095, 'intervention_max_f1_drop': 0.0203, 'intervention_max_feature': 'entropy_max', 'intervention_min_f1_drop': 0.0061}",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T07:52:42.191731+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_058_ddr_causality\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:05:46.902Z\", \"updated_at\": \"2026-05-20T07:52:22.652Z\", \"hypothesis\": \"DDR features have causal predictive power for depth beyond correlation: permutation importance confirms each feature group (drifting/stationary) contributes independently, and Granger causality tests show depth-t features predict depth-(t+1) features beyond autoregressive baseline, establishing temporal causal direction in the generation chain\", \"notes\": \"脚本 444 行，3 模块（permutation/granger/intervention）已实现并 dry-run 验证。全部 CPU-bound，不需要 GPU。数据: features_8gen.csv 37058 行。预估: Granger ~2min, Permutation ~15min, Intervention ~45min，可并行。\", \"server\": \"bjb2-18868\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python3 scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 --output results/ddr_causal_permutation.json && python3 scripts/ddr_causal_analysis.py --module granger --output results/ddr_causal_granger.json && python3 scripts/ddr_causal_analysis.py --module intervention --n-repeats 30 --output results/ddr_causal_intervention.json\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:1\"], \"pid\": \"179978\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_058_ddr_causality.log\", \"submitted_at\": \"2026-05-20T07:33:06.935Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"179978\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_058_ddr_causality.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python3 scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 --output results/ddr_causal_permutation.json && pyt
…[truncated 987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T07:52:42.191887+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_058_ddr_causality",
  "field": "checkpoint_path",
  "value": "results/ddr_causal_permutation.json, results/ddr_causal_granger.json, results/ddr_causal_intervention.json",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_058_ddr_causality",
    "field": "checkpoint_path",
    "value": "results/ddr_causal_permutation.json, results/ddr_causal_granger.json, results/ddr_causal_intervention.json",
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T07:52:42.192065+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_058_ddr_causality\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:05:46.902Z\", \"updated_at\": \"2026-05-20T07:52:23.365Z\", \"hypothesis\": \"DDR features have causal predictive power for depth beyond correlation: permutation importance confirms each feature group (drifting/stationary) contributes independently, and Granger causality tests show depth-t features predict depth-(t+1) features beyond autoregressive baseline, establishing temporal causal direction in the generation chain\", \"notes\": \"脚本 444 行，3 模块（permutation/granger/intervention）已实现并 dry-run 验证。全部 CPU-bound，不需要 GPU。数据: features_8gen.csv 37058 行。预估: Granger ~2min, Permutation ~15min, Intervention ~45min，可并行。\", \"server\": \"bjb2-18868\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python3 scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 --output results/ddr_causal_permutation.json && python3 scripts/ddr_causal_analysis.py --module granger --output results/ddr_causal_granger.json && python3 scripts/ddr_causal_analysis.py --module intervention --n-repeats 30 --output results/ddr_causal_intervention.json\\\"\", \"server\": \"bjb2-18868\", \"gpu\": [\"cuda:1\"], \"pid\": \"179978\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_058_ddr_causality.log\", \"submitted_at\": \"2026-05-20T07:33:06.935Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"179978\", \"log_path\": \"~/runs/gen-depth-fingerprint/exp_058_ddr_causality.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-fingerprint && python3 scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 --output results/ddr_causal_permutation.json && pyt
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T07:52:42.192249+00:00_

所有更新完成。

---

## exp_058_ddr_causality 分析摘要

**结论: SUCCESS** — Hypothesis 成立，DDR 特征对 depth 有因果预测力，超越相关性。

### 1. Permutation Importance
- Baseline F1 = 0.7714
- **Drifting 组** avg importance = 0.158，**Stationary 组** = 0.030（**5.3x 差距**）
- 排序: hapax_ratio (0.235) > entropy_mean (0.170) > ttr (0.156) > entropy_max (0.070) > entropy_std (0.057) > entropy_min (0.019) > tail_decay (0.014)
- 两组均独立贡献，drifting 主导

### 2. Granger Causality (panel N=29,095, lag=1)
- **6/7 特征显著** (p < 0.05)，唯一例外 entropy_min (p=0.538)
- 最大效应: entropy_std ΔR²=0.031 (F=1338)
- 方向一致: hapax_ratio/ttr 随 depth **递增**，entropy 系列 **递减**
- Fisher combined 跨 8 generator 验证: 6/7 显著，entropy_min 仍不显著 (p=0.375)

### 3. Intervention
- 所有 7 特征干预后 F1 均下降（0.6–2.0pp）
- 最大: entropy_max (−2.0pp)，其次 entropy_mean (−1.1pp)，entropy_std (−0.95pp)
- entropy_max 干预效果最大但 permutation importance 仅排第 4，说明其因果贡献具有特异性

### 注意事项
- entropy_min 是最弱特征：Granger 不显著、permutation 最低（0.019），但仍有干预效果（0.6pp）
- T=5 depth chain 限制只能用 lag=1，per-seed Granger 不可行，结果依赖 pooled panel regression
- Mistral-7B 的 per-generator Granger 在 hapax_ratio/ttr 上不显著（p>0.4），但 Fisher combined 仍显著——表明这两个特征的 Granger 信号不是所有 generator 均匀贡献的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_058_ddr_causality_20260520T075058"
}
```

</details>

---
