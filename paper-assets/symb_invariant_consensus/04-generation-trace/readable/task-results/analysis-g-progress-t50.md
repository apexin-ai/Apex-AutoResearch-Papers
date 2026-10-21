# analysis g progress t50

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-progress-t50_20260520T122509_result.json`
- **Structured JSON:** [`60ac48c3771d193427a4.json`](../../sessions/60/60ac48c3771d193427a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## G Decoupling (PID 307169) — westd-16639

| 指标 | 值 |
|------|-----|
| 进程状态 | **alive** (2h29m, 93MB RSS, 1.3% CPU) |
| 策略 | conservative |
| 进度 | **140/204** (68.6%) |
| 当前 accuracy | **55.7%** (78/140) |
| vs SC baseline (54.41%) | **+1.3pp** |
| avg truncation | 4.2%, matched=98% |
| 速度 | 0.02 prob/s (~50s/problem) |
| ETA（从 [140] 起） | ~3972s ≈ **66 min 剩余** |

Accuracy 趋势：从前 10 题 70% 持续下降，100 题时 60.0%，140 题时 55.7%，逐渐趋近 SC baseline。

注意：results/ 目录里的 results.json 是之前 dry-run 的 3 题 standard 结果，不是当前 conservative 运行的输出。最终结果需等进程完成后再读取。

---

## Q (PID 314817) — westd-16639

| 指标 | 值 |
|------|-----|
| 进程状态 | **alive** (1h29m, 2MB RSS) |
| 进度 | **77/204** (37.7%) |
| 速度 | ~65s/problem |
| ETA | 127 题 × 65s ≈ **~2h20m 剩余** (约 23:05 完成) |

Q 的日志活跃（最后请求 20:45:15），正在正常推理中。

---
