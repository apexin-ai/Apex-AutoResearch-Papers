# ops falcon3 d000 gsm8k check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-d000-gsm8k-check_20260523T084332_result.json`
- **Structured JSON:** [`23374570df17c5f71981.json`](../../sessions/23/23374570df17c5f71981.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。Cron 不存在（已被清除或未创建）。

**结果汇总：**

| | GSM8K Accuracy | Correct/Total |
|---|---|---|
| Falcon3-7B d000 (clean) | 74.53% | 983/1319 |
| Falcon3-7B d100 (contaminated) | 75.82% | 1000/1319 |
| **Delta (d100 - d000)** | **+1.29pp** | +17 |

Falcon3-7B 在 GSM8K 上的 contamination effect 很小（+1.29pp），远低于 Qwen2.5-7B 的 GSM8K delta（+11.07pp, 81.65% vs 70.58%）。这与 Falcon3 在 MCQ benchmarks 上 contamination effect 也较小的模式一致。

---
