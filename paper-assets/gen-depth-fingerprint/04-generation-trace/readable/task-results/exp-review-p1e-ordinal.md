# exp review p1e ordinal

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p1e-ordinal_20260515T134136_result.json`
- **Structured JSON:** [`bafe762482c732b1c1d2.json`](../../sessions/ba/bafe762482c732b1c1d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P1-E 实验完成。结果汇总：

### 3-class LOGO (gen-0 / gen-1 / gen-2+)

| 方法 | F1 | 95% CI |
|---|---|---|
| **XGBoost multiclass** | 0.7888 | [0.7843, 0.7933] |
| **CORAL ordinal** | 0.7711 | [0.7662, 0.7760] |
| **Frank-Hall ordinal** | **0.7931** | [0.7885, 0.7975] |

Ordinal consistency (concordance): XGBoost 0.821, CORAL 0.810, Frank-Hall **0.825**

### Binary LOGO (gen-1 vs gen-2+)

| 方法 | F1 | 95% CI |
|---|---|---|
| XGBoost binary | 0.7213 | [0.7150, 0.7275] |
| CORAL binary | 0.7275 | [0.7217, 0.7339] |

### 结论
三种方法 CI 高度重叠，ordinal structure 对 3-class 任务收益极小。Frank-Hall 略优但差异不显著（+0.004），CORAL 反而略差（-0.018）。符合预期——3 个有序类太少，ordinal 结构信息有限。

---
