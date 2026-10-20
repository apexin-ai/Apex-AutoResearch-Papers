# monitor training progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260526T065144_result.json`
- **Structured JSON:** [`1a03c9268bd9965d9002.json`](../../sessions/1a/1a03c9268bd9965d9002.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_097: step=85K/105K, fps=10.0, ETA=~33min, 状态=running
  最新 eval_return=77.4 (step 85K), ve_ratio=0.34
exp_100: step=80K/105K, fps=10.7, ETA=~39min, 状态=running
  最新 eval_return=687.0 (step 75K), ve_ratio=0.30
```

备注：
- 两个 PID 存活（显示为 bash 父进程，0% CPU 正常——实际计算在 GPU 上）
- exp_097 的 eval_return 从 192.5 (75K) 跌到 77.4 (85K)，gate 锁死在 dt=2（gate_dt_2_frac=1.0，entropy=0），值得关注
- exp_100 walker 表现稳定，train_return 在 600-680 区间，eval 687.0
- 两个实验的 gate 均未激活多步预测（dt 全为 2，empirical entropy=0）

---
