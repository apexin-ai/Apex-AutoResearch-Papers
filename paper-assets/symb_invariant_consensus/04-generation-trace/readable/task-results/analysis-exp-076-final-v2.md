# analysis exp 076 final v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-076-final-v2_20260519T203752_result.json`
- **Structured JSON:** [`d3b46fe38e9071bb30ab.json`](../../sessions/d3/d3b46fe38e9071bb30ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-076 已完成，全部 204 个样本处理完毕。

| 指标 | 值 |
|------|-----|
| n_samples | **204/204** |
| SC accuracy | **0.5686 (56.86%)** |
| Debate accuracy | **0.3824 (38.24%)** |
| Delta (Debate − SC) | **−0.1863** |
| Wall time | 186.4 min |
| Fallbacks | 10/204 |
| Total debate constraints | 3,677 |

Debate 在 FOLIO 上显著低于 SC baseline（−18.6 个百分点），Mistral 在这个形式逻辑数据集上 debate 框架反而损害了准确率。

---
