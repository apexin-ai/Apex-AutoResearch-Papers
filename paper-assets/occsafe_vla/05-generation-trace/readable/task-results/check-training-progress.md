# check training progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_progress_20260529T100620_result.json`
- **Structured JSON:** [`1df4dd2f411873b57dde.json`](../../sessions/1d/1df4dd2f411873b57dde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
实验 1: random_occ_v2_s0_r4 @westd-10894
- 进程状态：alive（持续输出中）
- 当前 step: 38532 / 50005 (77.1%)
- 已运行时间：10h 57m
- 预估剩余：~3h 12m（tqdm 估计）
- 预估完成时间：~14:08 UTC（约北京时间 22:08）
- 最新 loss (step 38500): occ=0.0408, action=0.0732

实验 2: full_occ_bn_v2_s2_r5 @westd-34685
- 进程状态：alive（持续输出中）
- 当前 step: 38560 / 50005 (77.1%)
- 已运行时间：10h 57m
- 预估剩余：~3h 12m（tqdm 估计）
- 预估完成时间：~14:08 UTC（约北京时间 22:08）
- 最新 loss (step 38500): occ=0.0096, action=0.1011
```

两个实验进度基本同步，速度稳定在 ~1.01 s/step。DDL (05-28 12:00 UTC) 已过，但实验仍在正常运行中。

---
