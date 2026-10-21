# diagnose westd41074 gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd41074_gpu_check_20260525T084609_result.json`
- **Structured JSON:** [`e03a0607e5f08bfd38b5.json`](../../sessions/e0/e03a0607e5f08bfd38b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments are still running on both servers. The alert was a false alarm.

## westd-41074 诊断结果

| GPU | exp_id | 状态 | GPU利用率 | 显存 | 运行时间 |
|-----|--------|------|-----------|------|----------|
| 0 | eval_openvla_random_k09_goal_seed42 | **running** | 68% | 16.0/95.6 GB | 2h59m |
| 1 | eval_openvla_random_k09_spatial_seed42 | **running** | 36% | 15.7/95.6 GB | 2h59m |
| 2 | eval_openvla_l2norm_k05_object_seed42_v4 | **running** | 80% | 15.6/95.6 GB | 2h54m |
| 3 | eval_openvla_prune_random_k03_seed42 | **running** | 61% | 15.7/95.6 GB | 2h54m |

cuda:1 (36%) 和 cuda:2 (80%) 利用率正常，0% 报告是瞬时波动导致的误报。LIBERO 评估在 episode 间隔时 GPU 利用率会短暂降至 0%（环境 reset、渲染等），超过 5 分钟窗口刚好被捕获。

所有 4 个 PID 存活，registry 状态均为 RUNNING，无需任何操作。

## westd-38929 诊断结果

| GPU | exp_id | 状态 | GPU利用率 | 运行时间 |
|-----|--------|------|-----------|----------|
| 0 | eval_openvla_attn_k09_long_seed42_v3 | **running** | 68% | 4h16m |
| 1 | eval_openvla_attn_k085_long_seed42_v3 | **running** | 65% | 4h16m |
| 2 | eval_openvla_random_k09_long_seed42_v3 | **running** | 68% | 4h16m |
| 3 | eval_openvla_l2norm_k09_long_seed42_v3 | **running** | 91% | 4h16m |

Registry 已有全部 4 个实验，状态正确，无需修复。

**空闲 GPU：无。** 两台服务器 8 张卡全部在跑实验。

---
