# analysis g final check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-final-check_20260520T132527_result.json`
- **Structured JSON:** [`153da6a192e459e0f347.json`](../../sessions/15/153da6a192e459e0f347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行，conservative 策略正在执行。**

| 指标 | 值 |
|------|-----|
| 进度 | **180/204** (88%) |
| 当前 acc | **55.0%** (99/180) |
| 速度 | 0.02 prob/s |
| ETA | ~1500s (**约 25 分钟**) |
| avg truncation | 4.2% |
| trace match rate | 98% |

注意：results.json 里现在只有 standard 策略的 3 题（看起来是 dry-run），conservative 的完整结果要等跑完才会写入。

当前 55.0% vs SC baseline 54.41%，差距极小（+0.6pp），最终结果可能不显著。

---
