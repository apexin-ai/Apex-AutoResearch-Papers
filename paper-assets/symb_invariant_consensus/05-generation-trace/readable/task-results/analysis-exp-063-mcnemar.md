# analysis exp 063 mcnemar

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-063-mcnemar_20260519T120101_result.json`
- **Structured JSON:** [`27ed35959b10c28094fa.json`](../../sessions/27/27ed35959b10c28094fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**2x2 Contingency Table (exp-063, LLaMA-3.1-8B, FOLIO-204)**

|  | SICA correct | SICA wrong |
|--|--|--|
| **SC correct** | a = 119 | b = 16 |
| **SC wrong** | c = 7 | d = 62 |

- **Discordant pairs**: b=16, c=7 (total=23)
- **SC accuracy**: 66.18% (135/204) ✓
- **SICA accuracy**: 61.76% (126/204) ✓
- **Δ**: -4.41pp ✓
- **McNemar exact test p-value**: **0.0931**
- **Significant (p<0.05)**: **No**

SC 比 SICA 高 4.41pp，但差异不显著 (p=0.0931)。在 23 个 discordant pairs 中，16 个 SC 对而 SICA 错，7 个反过来，比例偏向 SC 但未达到 0.05 显著性门槛。

---
