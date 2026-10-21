# analyze cwm seed456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cwm-seed456_20260512T125008_result.json`
- **Structured JSON:** [`d1109c449714dbb0f0ee.json`](../../sessions/d1/d1109c449714dbb0f0ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。结果汇总：

**cwm-seed456 结果**

| 指标 | seed=456 | baseline (seed=42) | 差异 |
|------|----------|-------------------|------|
| accuracy | 86.98% | 87.51% | -0.53pp |
| pass_f1 | 86.66% | 87.31% | -0.65pp |
| fail_f1 | 87.29% | 87.71% | -0.42pp |
| exact_match | 84.02% | 84.02% | 0 |
| train_loss | 0.2525 | — | — |
| eval_loss (best) | 0.0551 | — | — |

**一致性分析**：seed=456 的 accuracy (86.98%) 与 cwm8b-seed123 (86.98%) 完全一致，两个非默认 seed 均低于 seed=42 (87.51%)，说明 seed=42 略偏高。4B CWM 真实水平约 87.0–87.5%。

**cls-cwm gap**：cls-baseline=88.36%，CWM 三 seed 均值≈87.16%，gap ~1.2pp，在不同 seed 下稳定存在。

---
