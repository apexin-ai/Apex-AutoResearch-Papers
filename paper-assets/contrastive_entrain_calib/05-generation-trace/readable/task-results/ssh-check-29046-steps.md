# ssh check 29046 steps

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-29046-steps_20260522T163927_result.json`
- **Structured JSON:** [`079e68bca4ad5d7b8c08.json`](../../sessions/07/079e68bca4ad5d7b8c08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp-003-gs8:  step 72/8000, PID=516691, step_time=~65s/step, ETA=~143h (6天)
exp-004-s2-v2: step 4290/8000, PID=494017, step_time=~9.3s/step, ETA=~9.5h

GPU0: 55140/97887 MiB, 100%
GPU1: 40222/97887 MiB, 100%
```

**注意：两张卡上各有一个 eval 任务在抢资源**
- GPU0: exp-003-gs8 训练 + exp003-s2-ckpt7500 eval (PID 517336)
- GPU1: exp-004-s2 训练 + exp003-s2-ckpt8000 eval (PID 517417)

exp-003-gs8 每步 65s 极慢，很可能是 eval 争 GPU 导致的。eval 跑完后速度应该会恢复。

---
