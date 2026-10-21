# analysis check exp019 status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-exp019-status_20260517T083138_result.json`
- **Structured JSON:** [`0dbe924b6c9973785f58.json`](../../sessions/0d/0dbe924b6c9973785f58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在来估算速度。实验从 16:18:23 开始，当前已完成约 64 题（16:32 左右），大约 14 分钟完成 64 题。

```
STATUS: RUNNING
PROGRESS: 64/200 (已完成结果写入 64 条，当前正在处理第 65 题)
GPU_UTIL: 100%
GPU_MEM: 88309/97887 MiB (90.2%)

TIMING:
- 开始时间: 16:18:23
- 当前时间: ~16:32:43
- 已用时间: ~14.3 min (64 题)
- 平均每题: ~13.4 sec
- 预估剩余: ~30 min (136 题 × 13.4s)
- 预估完成: ~17:03 CST

中间统计 (基于日志，64 题已完成):
- SICA 正确: 48/64 (75.0%)
- SC 正确: 47/64 (73.4%)
- SICA 领先: +1.6pp (暂时)
```

实验运行正常，GPU 满载。按当前速度约 30 分钟后完成全部 200 题。

---
