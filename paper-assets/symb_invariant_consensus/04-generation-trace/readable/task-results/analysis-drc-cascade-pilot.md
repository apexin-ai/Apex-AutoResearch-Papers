# analysis drc cascade pilot

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_drc-cascade-pilot_20260521T044810_result.json`
- **Structured JSON:** [`15f9cc6950d2bb595ab4.json`](../../sessions/15/15f9cc6950d2bb595ab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DRC cascade pilot 完成。结果：

| τ | Accuracy | NLI Invocation Rate | NLI Invoked |
|---|----------|-------------------|-------------|
| 0.3 | 39.33% | 0% | 0/600 |
| 0.5 | 41.50% | 10.8% | 65/600 |
| **0.7** | **45.33%** | **38.8%** | **233/600** |
| 0.9 | 45.83% | 75.8% | 455/600 |

Baselines: SC-only = 39.33%, Full combo w=3 = 46.0%

关键发现：
- τ=0.3 无效 — 所有题目 agreement > 0.333（12 traces 3 类的理论下限），NLI 从不触发
- **τ=0.7 是甜蜜点**：仅调用 38.8% 的 NLI，就拿到了 45.33% accuracy（full combo 46% 的 ~93% 增益）
- τ=0.9 增加到 75.8% NLI 调用，只多 0.5pp

输出文件在 `/root/symb_invariant_consensus/results/drc_cascade_pilot/`：`results.json`、`pareto_front.pdf`、`agreement_distribution.png`。

---
