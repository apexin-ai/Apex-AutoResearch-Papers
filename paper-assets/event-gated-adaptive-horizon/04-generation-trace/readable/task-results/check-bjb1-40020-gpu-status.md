# check bjb1 40020 gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-40020-gpu-status_20260523T034228_result.json`
- **Structured JSON:** [`520d692b9a46d1fc6ca0.json`](../../sessions/52/520d692b9a46d1fc6ca0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

| 实验 | PID | 状态 | 当前步数 | 关键 Metrics |
|------|-----|------|----------|-------------|
| **exp_050** peginsertion_civo_trigger_s0 | 304736 | **ALIVE** | **143,400** | train_return 波动大 (0.5~21.7), eval_return **7.7** @142500, ve_ratio **3.2**, gate_dt 锁定 2.0 (100% dt_2), fps 4.2 |
| **exp_051** stackcube_frozen_dt_emb_s0 | 305974 | **ALIVE** | **144,600** | train_return 稳定 ~25, eval_return **25.3** @142500, ve_ratio **0.2**, gate_dt 锁定 2.0 (100% dt_2), fps 4.4 |

**GPU 占用**：
- PID 304736 (exp_050): GPU-3b54 上 2575 MiB
- PID 305974 (exp_051): GPU-3b54 上 435 MiB + GPU-7205 上 2530 MiB

**注意事项**：
- 两个实验的 gate_dt 都完全锁死在 dt=2（gate_empirical_entropy=0.0），门控没有自适应行为
- exp_050 的 train_return 方差很大（0.2~21.7），eval 仅 7.7，学习不稳定
- exp_051 表现明显更好，train/eval return 都在 ~25 附近，较稳定

---
