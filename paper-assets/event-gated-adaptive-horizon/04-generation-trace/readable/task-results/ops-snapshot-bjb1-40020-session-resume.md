# ops snapshot bjb1 40020 session resume

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_bjb1_40020_session_resume_20260520T194043_result.json`
- **Structured JSON:** [`43d203cbe1ffaf0a1c01.json`](../../sessions/43/43d203cbe1ffaf0a1c01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_029b: step=80K, eval_return=64.0 (@75K), ve_ratio=1.65 (@75K, alert=1), train_return=49.1, 进程状态=alive
exp_029d: step=5K,  eval_return=31.7 (@5K),  ve_ratio=N/A (尚未报告),          train_return=35.4, 进程状态=alive
GPU状态: cuda:0=12% (3041/24564 MiB)  cuda:1=12% (3043/24564 MiB)
```

补充：
- **exp_029b** eval_return 走势：5K→30.5, 15K→168.4, 25K→159.6, 35K→168.1, 45K→171.5, **55K→177.7**(peak), 65K→106.6, 75K→64.0 — 55K 后持续下降，ve_ratio=1.65 已触发 alert
- **exp_029d** 刚起步（step 5K），gate_dt 固定在 2.0（100% dt=2），尚无 ve_ratio 数据
- 两组 GPU 利用率都偏低(12%)，可能处于环境交互阶段

---
