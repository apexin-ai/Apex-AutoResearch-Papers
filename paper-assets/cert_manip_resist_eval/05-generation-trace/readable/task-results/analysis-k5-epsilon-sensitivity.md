# analysis k5 epsilon sensitivity

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-epsilon-sensitivity_20260523T140549_result.json`
- **Structured JSON:** [`4370f396bf62ac8c6c41.json`](../../sessions/43/4370f396bf62ac8c6c41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `docs/paper/data/epsilon_sensitivity_k5.json`。

**关键发现：**

**ASR=0 比例** — arc×sycophancy 18.5%, arc×authority_bias 19.7%, arc×verbosity_bias 16.2%，低于任务描述中预期的 23%/32%（可能是之前统计基于不同口径）。

**ε 敏感性结论 — K=5 下 ε 选择确实会影响系数量级，但不改变方向：**

| 指标 | max_coefficient_change |
|------|----------------------|
| K_eff β_std | 105.75% |
| η_max β_std | 55.54% |

- 所有 12 个 condition 下，K_eff 和 η_max 的β系数在三个 ε 值间**方向一致**（全部为正）
- **量级受 ε 影响较大**：ε=1e-3 时系数普遍更大（因为 log 变换压缩了零值附近的分布），ε=1e-9 时系数缩小
- 最敏感的条件是高 ASR=0 比例的 arc 组合（sycophancy、authority_bias），这符合预期——零值越多，ε 对 log 变换影响越大
- **mmlu_position_bias 和 arc_position_bias 完全不受 ε 影响**（无零值面板）
- R² 在 ε=1e-3 时最高，ε=1e-9 时降低，说明更大的 ε 有正则化效果

---
