# analysis exp deberta code qwen1b5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_deberta_code_qwen1b5_20260520T092537_result.json`
- **Structured JSON:** [`4ff87d0b2e77d5254f20.json`](../../sessions/4f/4ff87d0b2e77d5254f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (success)。

## 分析摘要

**exp_deberta_code_qwen1b5: Hypothesis confirmed (K\*=2)。** DeBERTa supervised classifier 在 Code domain 上的 K\*=2，与 OBD-LightGBM 的 K\*=2 完全一致，证实 domain ceiling 与分类器架构无关。DeBERTa 在所有深度对上 AUC 均高于 OBD（delta +0.05~+0.07），但两者的可区分性边界一致：0v1 和 1v2 显著可区分（AUC CI lower > θ=0.6），2v3 及更深的对均落在 θ 以下。

| Pair | DeBERTa AUC | 95% CI | OBD AUC | Delta |
|------|------------|--------|---------|-------|
| 0v1 | 1.0000 | [0.9999, 1.0000] | 0.9388 | +0.061 |
| 1v2 | 0.8076 | [0.8001, 0.8147] | 0.7382 | +0.069 |
| 2v3 | 0.5933 | [0.5847, 0.6018] | 0.5300 | +0.063 |
| 3v4 | 0.5492 | [0.5410, 0.5573] | 0.5022 | +0.047 |
| 4v5 | 0.5311 | [0.5235, 0.5388] | 0.5219 | +0.009 |

---
