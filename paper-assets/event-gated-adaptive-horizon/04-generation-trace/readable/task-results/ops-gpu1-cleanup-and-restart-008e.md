# ops gpu1 cleanup and restart 008e

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1_cleanup_and_restart_008e_20260514T042546_result.json`
- **Structured JSON:** [`5574eec922535e22e987.json`](../../sessions/55/5574eec922535e22e987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. 进程清理
- PID 123820、123422（008f_dryrun）**已自行退出**，无需 kill
- 无其他重复进程

### 2. logdir 清理
- `exp_008e_subsample_on_fixed_dt1_h15` 为空目录，已 `rmdir` 删除

### 3. 008e 重启
- **exp_id**: `exp_008e_v2_subsample_on_dt1_h15`
- **tmux session PID**: 124955
- **python 进程 PID**: 124960
- **GPU**: cuda:1（CUDA_VISIBLE_DEVICES=1）
- **logdir**: `logdir/exp_008e_v2_subsample_on_dt1_h15`

### 4. GPU 状态确认
| GPU | 进程 | 实验 |
|-----|------|------|
| 0 | PID 106947 (4158MiB) | exp_008a_fixed_dt2_no_subsample |
| 0 | PID 109524 (2744MiB) | exp_008d_subsample_on_h8 |
| 1 | PID 124960 (刚启动，加载中) | exp_008e_v2_subsample_on_dt1_h15 |

GPU 1 上仅有 1 个新进程，无重复。

---
