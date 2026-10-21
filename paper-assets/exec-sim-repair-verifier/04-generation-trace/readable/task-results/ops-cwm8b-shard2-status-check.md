# ops cwm8b shard2 status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-shard2-status-check_20260516T023528_result.json`
- **Structured JSON:** [`35c4a4c60ddb716c5a58.json`](../../sessions/35/35c4a4c60ddb716c5a58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### shard2 (cuda:1) — 运行中
- **PID 448094** 活着，`--start_idx 7680`，输出到 `cwm_8b_ckpt400_test_shard2/`
- **进度**: 608 / 2104 samples (**28.9%**)，当前处理到 idx ~8287
- GPU 1: 21133 MiB, 88% 利用率

### v3 主跑 (cuda:3) — 运行中
- **PID 443221** 活着，已运行 ~1h49m
- **进度**: 6216 / 9784 samples (**63.5%**)
- GPU 3: 21133 MiB, 88% 利用率

### GPU 空闲情况
| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 0 MiB | 0% | **空闲** |
| 1 | 21133 MiB | 88% | shard2 |
| 2 | 0 MiB | 0% | **空闲** |
| 3 | 21133 MiB | 88% | v3 主跑 |

另外发现 PID 194398 是一个 `eval_cwm_seed123`（4B 模型，CUDA_VISIBLE_DEVICES=0）的 tmux session，但 GPU 0 显存为 0，可能已完成或未实际占用 GPU。

---
