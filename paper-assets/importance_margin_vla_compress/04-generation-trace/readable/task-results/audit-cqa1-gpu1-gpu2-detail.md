# audit cqa1 gpu1 gpu2 detail

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_gpu1_gpu2_detail_20260526T172804_result.json`
- **Structured JSON:** [`d717f16ed046c60982c3.json`](../../sessions/d7/d717f16ed046c60982c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
CQA1-33015 GPU STATUS (as of ~01:28 Beijing time, May 27):

GPU0: 23% util | 10267/24564 MiB | PID=384775 | pi05 random k=0.85 libero_10 50ep seed42
      PROGRESS: T9 ep10/50 (last task) | ETA: ~01:45 Beijing (~15min)

GPU1: 60% util | 10269/24564 MiB | PID=416018 | pi05 l2norm k=0.85 libero_10 50ep seed42
      PROGRESS: T9 ep20/50 (last task) | ETA: ~01:42 Beijing (~12min)

GPU2: 32% util | 10495/24564 MiB | PID=467731 | pi05 random k=0.7 libero_10 50ep seed42
      PROGRESS: T6 ep10/50 (4 tasks remaining) | ETA: ~02:55 Beijing (~85min)

GPU3: 65% util | 10657/24564 MiB | PID=546287 | pi05 attention k=0.95 libero_10 50ep seed42
      PROGRESS: T1 ep30/50 (started 00:52, 8.5 tasks remaining) | ETA: ~04:15 Beijing (~2.8h)
```

关键发现：
- **GPU0 和 GPU1** 都在跑最后一个 task (T9)，约 15 分钟内完成
- **GPU2** (random k=0.7) 在 T6，约 1.5h 完成
- **GPU3** (attention k=0.95) 刚到 T1，是最新启动的实验，约 2.8h 完成（~04:15 Beijing）

中间结果快照：
- random k=0.85: T8 done → 185/450=41.1%，T9 ep10 → 7/10=70%
- l2norm k=0.85: T8 done → 347/450=77.1%，T9 ep20 → 19/20=95%
- random k=0.7: T5 done → 222/300=74.0%，T6 ep10 → 5/10=50%
- attention k=0.95: T0 done → 44/50=88.0%，T1 ep30 → 29/30=97%

---
