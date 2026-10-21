# check hopper phase1 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hopper-phase1-progress_20260527T032456_result.json`
- **Structured JSON:** [`f424e280dbbe99e8c04d.json`](../../sessions/f4/f424e280dbbe99e8c04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_hopper_baseline:    step 16K/105K (15.2%)
exp_hopper_trained_s0:  step 16K/105K (15.2%)
GPU 0: util 21%, mem 53858/97887 MiB
GPU 1: util 36%, mem 3276/97887 MiB
```

两个实验都在 step 16K，进度同步。GPU 利用率偏低（21%/36%），可能处于 environment rollout 阶段而非 gradient update。

按 15.2% 进度推算，若已运行约 X 小时，预计还需 ~5.6 倍当前已用时间完成。需要知道启动时间才能给出具体 ETA——要我查一下进程启动时间吗？

---
