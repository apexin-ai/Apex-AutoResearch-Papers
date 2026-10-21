# ops preflight exp 008

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_preflight_exp_008_20260514T013938_result.json`
- **Structured JSON:** [`67d2980fd9a869261ec1.json`](../../sessions/67/67d2980fd9a869261ec1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pre-flight 检查结果

**exp_008a 和 exp_008c 已经在运行中，无需再次提交。**

### GPU 状态
| GPU | 型号 | 显存占用 | 进程 |
|-----|------|---------|------|
| cuda:0 | RTX PRO 6000 Blackwell (96GB) | 803 MiB / 97887 MiB | PID 106947 — **exp_008a** |
| cuda:1 | RTX PRO 6000 Blackwell (96GB) | 803 MiB / 97887 MiB | PID 107026 — **exp_008c** |

### 训练进度
- **exp_008a** (`exp_008a_fixed_dt2_no_subsample`): step 5000 / 105000，运行 ~2 分钟
- **exp_008c** (`exp_008c_fixed_dt2_no_subsample_h8`): step 5000 / 105000，运行 ~2 分钟
- 两者刚启动不久，GPU 利用率还在 0%（正在预热/prefill 阶段）

### 训练命令
- **008a**: `python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1`
- **008c**: 同上 + `--imag_horizon 8`，logdir `exp_008c_fixed_dt2_no_subsample_h8`，device cuda:0（注意两者都声明 cuda:0，但实际分别在两块 GPU 上）

### 其他
- **磁盘**: 246G 可用 / 250G (2%)，充足
- **logdir**: 两个目录已创建，各含 tfevents、metrics.jsonl、train_eps、eval_eps

### 阻塞项
**无。** 两个实验已在运行中，不需要再提交。

---
