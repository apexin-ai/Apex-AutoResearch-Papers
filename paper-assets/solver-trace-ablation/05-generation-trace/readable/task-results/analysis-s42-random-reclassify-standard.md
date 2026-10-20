# analysis s42 random reclassify standard

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s42-random-reclassify-standard_20260515T180652_result.json`
- **Structured JSON:** [`247b6d04c0e45b646826.json`](../../sessions/24/247b6d04c0e45b646826.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**s42 random (plan018-additive-random-b01-s42) classify_h7 标准分类结果**

| 指标 | 值 | 旧值 |
|------|---|------|
| Proved | 79 | 79 |
| H7 (tautology) | 0 (0%) | 0 |
| H1 (conclusion in premises) | 58 (73.4%) | 56 (exact) + 8 (near) |
| H8 (conjunction collapse) | 4 (5.1%) | 3 |
| **Genuine** | **18 (22.8%)** | 12 (strict) / 23 (exact_h1 only) |

关键差异：当前 classify_h7 将 2 个原 H1-near 重新分类为 H1，多识别 1 个 H8。有 1 个 H1∩H8 重叠样本，genuine = 79 − |H7∪H1∪H8| = 79 − 61 = 18。

JSON 分类详情保存在 `/root/autodl-tmp/outputs/h7_classification/plan018_additive_random_b01_s42_h7.json`。

---
