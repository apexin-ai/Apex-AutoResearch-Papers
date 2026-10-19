# ssh eval progress check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-progress-check_20260517T172241_result.json`
- **Structured JSON:** [`52302cf7982eff153051.json`](../../sessions/52/52302cf7982eff153051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
进程状态: PID 40598 [运行中], PID 44022 [运行中]
GPU 状态: GPU 0 (PID 40598) 3546MiB, GPU 1 (PID 44022) 3524MiB, 均 1% util

α=0.0 (GPU 0):
  spatial: 59.4% ✅ (500 ep, 112.8 min)
  object: 进行中, 26/50 ep (当前 task), running SR=57.7%
  goal: 未开始
  libero_10: 未开始

α=1.0 (GPU 1):
  spatial: 61.0% ✅ (500 ep, 113.3 min)
  object: 进行中, 15/50 ep (当前 task), running SR=73.3%
  goal: 未开始
  libero_10: 未开始
```

时间估算：每个 suite 约 113 min。object 从 ~23:25 开始已跑约 2h，接近完成。剩余 goal + libero_10 还需约 3.5-4h，预计全部完成时间约 05:00-05:30 (May 18)。

---
