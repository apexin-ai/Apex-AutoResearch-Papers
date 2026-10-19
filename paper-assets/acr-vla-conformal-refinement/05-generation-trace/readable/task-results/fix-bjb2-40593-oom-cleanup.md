# fix bjb2 40593 oom cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb2-40593-oom-cleanup_20260521T150538_result.json`
- **Structured JSON:** [`498b723469649f529cf8.json`](../../sessions/49/498b723469649f529cf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**清理前后对比：**

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| GPU 进程数 | 2 (PID 872656 + 876717) | 1 (PID 872656) |
| GPU 显存 | 19674MiB / 24564MiB (80%) | 9839MiB / 24564MiB (40%) |
| GPU 功耗 | 119W | 82W |
| GPU 温度 | 41°C | 39°C |

**原始 shard 0 状态：** PID 872656 正常运行，3000/7251 samples，3.35s/sample，预计剩余 ~4h。

---
