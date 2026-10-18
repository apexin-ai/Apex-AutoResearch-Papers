# analysis betastd trajectory

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_betastd-trajectory_20260524T192235_result.json`
- **Structured JSON:** [`718cbcc86e202e6e225f.json`](../../sessions/71/718cbcc86e202e6e225f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**输出文件：**
- `betastd_trajectory.json` — 完整 β_std 数据 + p-values + shift evidence
- `fig_betastd_trajectory.pdf` — 轨迹图（mean ± SD + 散点）
- `fig_betastd_pvalue_dist.pdf` — Bootstrap p-value violin 图（按 K 分面）

**核心结果：**

| K | β_std(K_eff) | β_std(η_max) | K_eff sig | η_max sig |
|---|---|---|---|---|
| 3 | 0.349 ± 0.183 | 0.266 ± 0.179 | 7/12 | 5/12 |
| 5 | 0.437 ± 0.293 | 0.101 ± 0.327 | 8/12 | 5/12 |
| 7 | 0.401 ± 0.222 | 0.084 ± 0.284 | 9/12 | 3/12 |

Predictor shift 得到连续 effect size 证据支持：β_std(K_eff) 从 0.35 上升到 ~0.40，β_std(η_max) 从 0.27 下降到 0.08，且 K_eff 显著条件数从 7→8→9/12 递增，η_max 从 5→5→3/12 递减。

---
