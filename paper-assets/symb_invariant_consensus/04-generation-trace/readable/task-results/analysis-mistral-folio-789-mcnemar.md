# analysis mistral folio 789 mcnemar

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral-folio-789-mcnemar_20260522T130518_result.json`
- **Structured JSON:** [`1b62ee9fee57b3f5438f.json`](../../sessions/1b/1b62ee9fee57b3f5438f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral FOLIO seed=789 McNemar exact test 结果：

| 指标 | 值 |
|------|-----|
| n | 204 |
| both_correct | 112 |
| **b (SC✓ SICA✗)** | **9** |
| **c (SC✗ SICA✓)** | **4** |
| both_wrong | 79 |
| Discordant pairs | 13 |
| **McNemar exact p** | **0.2668** |
| Direction | SC > SICA by 5 discordant pairs |

差异不显著（p=0.267），仅 13 个 discordant pairs，样本量不足以检测 2.45pp 的差异。

---
