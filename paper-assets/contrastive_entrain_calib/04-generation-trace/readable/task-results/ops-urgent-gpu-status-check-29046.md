# ops urgent gpu status check 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-status-check-29046_20260519T110755_result.json`
- **Structured JSON:** [`ea7904049c319134775f.json`](../../sessions/ea/ea7904049c319134775f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: [运行中] PID=172844 显存=66898/97887 MiB  step=1199/8000
GPU 1: [运行中] PID=70649  显存=38152/97887 MiB  step=2282/8000

exp002v2-recalib: 运行中 step 1199/8000 (15%), 已跑 4h27m, 剩余 ~44h40m, 预计 5/21 ~15:50 完成
  reward: combined=0.54, r1=-0.08, r2=-0.07, r3=0.75

exp-003: 运行中 step 2282/8000 (29%), 已跑 18h17m, 剩余 ~44h, 预计 5/21 ~15:10 完成
  reward: combined=0.54 (r3-only), ~27s/step
  ⚠ 每步 WARNING: "d_syc not loaded; returning R3-only rewards" (符合 r3-only 实验设计)
```

两个实验均正常运行，无错误。exp003_restart.log 中有旧的 crash 记录（deberta 加载失败），但当前进程不受影响。

---
