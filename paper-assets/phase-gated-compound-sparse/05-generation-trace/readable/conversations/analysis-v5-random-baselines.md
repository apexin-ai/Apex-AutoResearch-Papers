# analysis v5 random baselines

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_v5-random-baselines_20260514T025924.jsonl`
- **Structured JSON:** [`e2a0df744d121a39b7b8.json`](../../sessions/e2/e2a0df744d121a39b7b8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-14T03:01:15.869778+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T03:01:15.870383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T03:01:15.870702+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_v5_random_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_v5_random_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T03:01:15.870915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_v5_random_s025/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_v5_random_s025/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T03:01:15.877563+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 25862,\\n      \\\"n_segments\\\": 511\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32349,\\n      \\\"n_segments\\\": 454\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 27996,\\n      \\\"n_segments\\\": 391\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1462,\\n        \\\"attn\\\": 1.5625,\\n        \\\"kv\\\": 3.14,\\n        \\\"both\\\": 3.9177\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1105,\\n        \\\"attn\\\": 1.3939,\\n        \\\"kv\\\": 3.6093,\\n        \\\"both\\\": 4.7109\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1226,\\n        \\\"attn\\\": 1.4107,\\n        \\\"kv\\\": 2.9051,\\n        \\\"both\\\": 4.1376\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": 0.456308,\\n        \\\"ci_low\\\": 0.118563,\\n        \\\"ci_high\\\": 0.767261,\\n        \\\"median\\\": 0.160628,\\n        \\\"winsorized_mean\\\": 0.537753,\\n        \\\"skewness\\\": -2.0645,\\n        \\\"outlier_count\\\": 2\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": 0.477465,\\n        \\\"ci_low\\\": 0.284644,\\n        \\\"
…[truncated 7718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T03:01:15.878422+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.25\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 25862,\\n      \\\"n_segments\\\": 511\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32349,\\n      \\\"n_segments\\\": 454\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 27996,\\n      \\\"n_segments\\\": 391\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.1462,\\n        \\\"attn\\\": 8.6611,\\n        \\\"kv\\\": 6.3908,\\n        \\\"both\\\": 17.0646\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.1105,\\n        \\\"attn\\\": 5.1508,\\n        \\\"kv\\\": 9.0665,\\n        \\\"both\\\": 29.3192\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.1226,\\n        \\\"attn\\\": 2.6223,\\n        \\\"kv\\\": 6.1113,\\n        \\\"both\\\": 15.3841\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"mean\\\": 3.905197,\\n        \\\"ci_low\\\": 0.979625,\\n        \\\"ci_high\\\": 6.339257,\\n        \\\"median\\\": 3.002378,\\n        \\\"winsorized_mean\\\": 4.707617,\\n        \\\"skewness\\\": -4.7643,\\n        \\\"outlier_count\\\": 2\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"mean\\\": 3.911394,\\n        \\\"ci_low\\\": 2.706653,\\n       
…[truncated 7718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T03:01:15.878851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -20 /root/runs/phase-gated-compound-sparse/mvp_v5_random_s015.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -20 /root/runs/phase-gated-compound-sparse/mvp_v5_random_s015.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T03:01:15.879126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 10:57:11,453 [INFO] run_profiling: [50/50] Processing problem test/algebra/892.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 10:58:05,775 [INFO] run_profiling:   -> 29 phases, boundaries at [339, 368, 408, 444, 479, 785, 957, 1109, 1179, 1444, 1512, 1563, 1597, 1616, 1650, 1683, 1709, 1742, 1755, 1780, 1793, 1808, 1832, 1861, 1895, 1913, 1972, 1989]\\n2026-05-14 10:58:05,857 [INFO] run_profiling: Results saved to /root/autodl-tmp/pacs/profiling_output_v5_random_s015/profiling_results.json\\n\\n============================================================\\nPACS Profiling Complete — 50 problems\\n============================================================\\n  high_sparsity: 25862 tokens, 511 segments\\n  low_sparsity: 32349 tokens, 454 segments\\n  mid_sparsity: 27996 tokens, 391 segments\\n\\n  II[high_sparsity, 0.15]: mean=+0.4563  95%CI=[+0.1186, +0.7673]\\n  II[low_sparsity, 0.15]: mean=+0.4775  95%CI=[+0.2846, +0.7010]\\n  II[mid_sparsity, 0.15]: mean=+0.5134  95%CI=[+0.3366, +0.7408]\\n\\nVerdict: FAIL\\n============================================================\\n\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T03:01:15.879366+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "tail -20 /root/runs/phase-gated-compound-sparse/mvp_v5_random_s025.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "tail -20 /root/runs/phase-gated-compound-sparse/mvp_v5_random_s025.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T03:01:15.885956+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 10:56:59,785 [INFO] run_profiling: [50/50] Processing problem test/algebra/892.json\\nSetting `pad_token_id` to `eos_token_id`:151643 for open-end generation.\\n2026-05-14 10:57:53,949 [INFO] run_profiling:   -> 29 phases, boundaries at [339, 368, 408, 444, 479, 785, 957, 1109, 1179, 1444, 1512, 1563, 1597, 1616, 1650, 1683, 1709, 1742, 1755, 1780, 1793, 1808, 1832, 1861, 1895, 1913, 1972, 1989]\\n2026-05-14 10:57:54,031 [INFO] run_profiling: Results saved to /root/autodl-tmp/pacs/profiling_output_v5_random_s025/profiling_results.json\\n\\n============================================================\\nPACS Profiling Complete — 50 problems\\n============================================================\\n  high_sparsity: 25862 tokens, 511 segments\\n  low_sparsity: 32349 tokens, 454 segments\\n  mid_sparsity: 27996 tokens, 391 segments\\n\\n  II[high_sparsity, 0.25]: mean=+3.9052  95%CI=[+0.9796, +6.3393]\\n  II[low_sparsity, 0.25]: mean=+3.9114  95%CI=[+2.7067, +5.2360]\\n  II[mid_sparsity, 0.25]: mean=+7.9491  95%CI=[+4.6697, +11.8672]\\n\\nVerdict: FAIL\\n============================================================\\n\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_v5-random-baselines_20260514T025924",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T03:01:15.886444+00:00_

两个实验均完成（50/50 problems, EXIT_CODE=0, 无 NaN/Inf warnings）。

## 提取结果

### mvp_v5_random_s015 (random, s=0.15)

| Phase | II mean | 95% CI | II median | II winsorized | kv_ppl | attn_ppl | both_ppl | dense_ppl |
|-------|---------|--------|-----------|---------------|--------|----------|----------|-----------|
| high | +0.456 | [+0.119, +0.767] | 0.161 | 0.538 | 3.14 | 1.56 | 3.92 | 1.15 |
| mid | +0.513 | [+0.337, +0.741] | 0.252 | 0.509 | 2.91 | 1.41 | 4.14 | 1.12 |
| low | +0.477 | [+0.285, +0.701] | 0.183 | 0.428 | 3.61 | 1.39 | 4.71 | 1.11 |

Segments: high=511, mid=391, low=454. No warnings.

### mvp_v5_random_s025 (random, s=0.25)

| Phase | II mean | 95% CI | II median | II winsorized | kv_ppl | attn_ppl | both_ppl | dense_ppl |
|-------|---------|--------|-----------|---------------|--------|----------|----------|-----------|
| high | +3.905 | [+0.980, +6.339] | 3.002 | 4.708 | 6.39 | 8.66 | 17.06 | 1.15 |
| mid | +7.949 | [+4.670, +11.867] | 2.985 | 6.353 | 6.11 | 2.62 | 15.38 | 1.12 |
| low | +3.911 | [+2.707, +5.236] | 2.915 | 3.858 | 9.07 | 5.15 | 29.32 | 1.11 |

Segments: high=511, mid=391, low=454. No warnings.

---

## Random vs Importance 对比

### s=0.15

| Metric | Importance | Random | Delta |
|--------|-----------|--------|-------|
| ii_high | +0.306 | **+0.456** | random 高 49% |
| ii_mid | +1.274 | **+0.513** | random 低 60% |
| ii_low | **+8.786** | +0.477 | random 低 95% |
| kv_ppl_high | **1.21** | 3.14 | importance 低 61% |
| kv_ppl_mid | **2.13** | 2.91 | importance 低 27% |
| kv_ppl_low | 6.75 | **3.61** | random 低 47% |

### s=0.25

| Metric | Importance | Random | Delta |
|--------|-----------|--------|-------|
| ii_high | +0.851 | **+3.905** | random 高 4.6x |
| ii_mid | +9.306 | +7.949 | ~相当 |
| ii_low | **+96.715** | +3.911 | importance 高 24.7x |
| kv_ppl_high | **1.31** | 6.39 | importance 低 4.9x |
| kv_ppl_mid | 6.18 | 6.11 | ~相当 |
| kv_ppl_low | 23.89 | **9.07** | random 低 2.6x |

---

## 分析

### 1. II 符号
**两组全部为正（super-additive）**，无 sign reversal。Pivot hypothesis 预期 importance → negative II 未实现。

### 2. II 幅度分布模式
- **Random II 跨 phase 非常均匀**：s=0.15 时三个 phase 在 0.46~0.51 范围；s=0.25 时在 3.9~7.9 范围
- **Importance II 极度不均匀**：low-sparsity phase 暴涨（s=0.15: 8.79; s=0.25: 96.7），说明 importance metric 在 high natural sparsity 区域造成了极端的 super-additive 干扰

### 3. KV PPL
- Importance 在 **high-sparsity phase 更优**（heads 激活度高 → importance 排序可靠）
- Random 在 **low-sparsity phase 反而更优**（importance metric 在 high natural sparsity 区域失效，eviction 决策比随机还差）
- Mid phase 两者接近

### 4. Both PPL
s=0.25 差异显著：random both_ppl (15~29) 远低于 importance 在 low phase 暗示的水平（importance kv_ppl_low=23.89 本身已经很高）

---

## 结论：**Negative — importance metric 可能无效甚至有害**

- **Sign reversal 不成立**：两种策略 II 符号相同（全正），strategy-dependent reversal 假说被否定
- **Importance masking 不是"更智能"的 eviction**：在 low-sparsity phases，importance 的 kv_ppl 和 II 都远差于 random，说明当 attention 本身就稀疏时，importance metric 的排序几乎没有信号
- **Importance 唯一优势在 high-sparsity phase**（ii_high 和 kv_ppl_high 更低），但 low phase 的灾难性表现（II=96.7 at s=0.25）抵消了收益

---

## 结构化 JSON

```json
{
  "mvp_v5_random_s015": {
    "status": "completed",
    "n_problems": 50,
    "masking_method": "random",
    "sparsity": 0.15,
    "warnings": [],
    "segments": {"high": 511, "mid": 391, "low": 454},
    "ii": {
      "high": {"mean": 0.456, "ci": [0.119, 0.767], "median": 0.161, "winsorized": 0.538},
      "mid": {"mean": 0.513, "ci": [0.337, 0.741], "median": 0.252, "winsorized": 0.509},
      "low": {"mean": 0.477, "ci": [0.285, 0.701], "median": 0.183, "winsorized": 0.428}
    },
    "ppl": {
      "high": {"dense": 1.15, "attn": 1.56, "kv": 3.14, "both": 3.92},
      "mid": {"dense": 1.12, "attn": 1.41, "kv": 2.91, "both": 4.14},
      "low": {"dense": 1.11, "attn": 1.39, "kv": 3.61, "both": 4.71}
    },
    "verdict": "FAIL"
  },
  "mvp_v5_random_s025": {
    "status": "completed",
    "n_problems": 50,
    "masking_method": "random",
    "sparsity": 0.25,
    "warnings": [],
    "segments": {"high": 511, "mid": 391, "low": 454},
    "ii": {
      "high": {"mean": 3.905, "ci": [0.980, 6.339], "median": 3.002, "winsorized": 4.708},
      "mid": {"mean": 7.949, "ci": [4.670, 11.867], "median": 2.985, "winsorized": 6.353},
      "low": {"mean": 3.911, "ci": [2.707, 5.236], "median": 2.915, "winsorized": 3.858}
    },
    "ppl": {
      "high": {"dense": 1.15, "attn": 8.66, "kv": 6.39, "both": 17.06},
      "mid": {"dense": 1.12, "attn": 2.62, "kv": 6.11, "both": 15.38},
      "low": {"dense": 1.11, "attn": 5.15, "kv": 9.07, "both": 29.32}
    },
    "verdict": "FAIL"
  },
  "comparison_conclusion": {
    "sign_reversal": false,
    "importance_vs_random": "importance worse in low-sparsity phases, better in high-sparsity phases only",
    "overall": "negative — importance metric ineffective, no strategy-dependent II reversal"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_v5-random-baselines_20260514T025924"
}
```

</details>

---
