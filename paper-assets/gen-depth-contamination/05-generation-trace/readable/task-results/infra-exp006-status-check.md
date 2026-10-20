# infra exp006 status check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-status-check_20260514T213157_result.json`
- **Structured JSON:** [`e09e19d44d1149e9cae5.json`](../../sessions/e0/e09e19d44d1149e9cae5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-006 状态报告

| 项目 | 状态 |
|------|------|
| **tmux session** | `exp_006_graduated_filtering` — 存活 |
| **GPU** | 83% 利用率，13.7 / 24.6 GB 显存占用 |
| **已完成 runs** | **33 / 50**（含 base_model） |
| **总 run 目录** | 35（含 1 个 base_model + 1 个正在训练） |
| **当前训练** | `graduated_a0.7_s456` — epoch 0.96, 进度 61% (1715/2814), 速度 1.25 it/s |
| **loss** | ~2.49-2.55，稳定下降中 |

**剩余估算**：当前 run 剩余 ~14 min（1099 steps × 0.8s）。之后还剩 **~17 个 run** 待训练（graduated_a0.7 剩 3 个 seed + graduated_a0.9 × 5 seeds + 可能的其他条件）。按每个 run ~37 min 估算，总剩余约 **10-11 小时**。

---
