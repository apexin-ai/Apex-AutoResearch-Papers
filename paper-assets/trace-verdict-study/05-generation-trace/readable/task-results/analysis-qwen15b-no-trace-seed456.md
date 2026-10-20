# analysis qwen15b no trace seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_no_trace_seed456_20260520T221422_result.json`
- **Structured JSON:** [`f5a8868b911e788f854c.json`](../../sessions/f5/f5a8868b911e788f854c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总如下：

---

## qwen15b_no_trace_seed456 结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **73.87%** (95% CI: [71.3%, 76.2%]) |
| Majority baseline | 71.5% (always predict pass) |
| Lift over majority | +2.4pp |
| pass F1 | 0.82 (P=0.81, R=0.83) |
| fail F1 | 0.53 (P=0.54, R=0.51) |
| eval_loss | 0.7725 |
| train_loss | 0.2226 |

## 3-seed 统计 (Qwen-1.5B no_trace)

| Seed | Accuracy |
|------|----------|
| 42 | 67.31% |
| 123 | 75.88% |
| 456 | 73.87% |
| **Mean** | **72.35%** |
| **Std** | **4.48pp** |

## Outlier 判断

seed42 偏差 = (72.35 - 67.31) / 4.48 = **1.13 std** → **不构成 outlier**（阈值 1.5 std）。

seed42 确实是最低的，但 seed456 (73.87%) 更接近 seed123 (75.88%) 而非 seed42，说明 no_trace 条件的典型表现在 ~73-76% 区间，seed42 偏低但在合理方差范围内。3 个 seed 的 std=4.48pp 反映 no_trace 条件下 1.5B 模型存在中等程度的 seed 敏感性。

---
