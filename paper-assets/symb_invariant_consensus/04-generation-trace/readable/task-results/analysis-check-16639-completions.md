# analysis check 16639 completions

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-16639-completions_20260519T200109_result.json`
- **Structured JSON:** [`c9b769af066d8afbe1f0.json`](../../sessions/c9/c9b769af066d8afbe1f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-072b 已完成，结论 negative，registry 已更新。**

| 指标 | 值 |
|------|-----|
| SC accuracy | 59.5% |
| SICA accuracy | 58.5% |
| Delta | -1.0pp |
| n_samples | 200 |
| k | 12 |
| Wall time | ~2h |
| Extraction failures | 108/2400 (4.5% JSON parse) |

SICA 在 LLaMA-8B + LogiQA 上未能超过 SC baseline。4.5% 的 JSON 解析失败率可能是一个拖累因素。

---
