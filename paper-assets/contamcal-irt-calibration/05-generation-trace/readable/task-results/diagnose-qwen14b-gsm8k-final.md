# diagnose qwen14b gsm8k final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen14b-gsm8k-final_20260520T074816_result.json`
- **Structured JSON:** [`f7dde58fba951f2f7825.json`](../../sessions/f7/f7dde58fba951f2f7825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**Qwen-14B GSM8K eval 结果 (s42)**

| Dosage | Accuracy | Correct/Total |
|--------|----------|---------------|
| d000 (clean) | **60.80%** | 802/1319 |
| d100 (contaminated) | **81.27%** | 1072/1319 |
| **Delta** | **+20.47pp** | +270 items |

与 MMLU 上的 U-collapse（−9.37pp）不同，Qwen-14B 在 GSM8K 上呈现强正向 contamination effect：d100 比 d000 高 20.47pp，说明 contamination 在 generative math benchmark 上的迁移方向与 MCQ benchmark 截然相反。

---
