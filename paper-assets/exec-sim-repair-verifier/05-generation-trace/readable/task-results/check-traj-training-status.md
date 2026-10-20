# check traj training status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_traj-training-status_20260517T134306_result.json`
- **Structured JSON:** [`25e3efb9e9dc42ae5d94.json`](../../sessions/25/25e3efb9e9dc42ae5d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

**状态**: 正常运行中

| 项目 | 值 |
|------|------|
| 服务器 | home-1x5090 (RTX 5090) |
| tmux session | `qwen3-8b-traj-func-s42` (创建于 06:20) |
| GPU 占用 | 22705 / 32607 MiB, 利用率 94%, 77°C |
| 总 steps | 756 (3 epochs) |
| 当前进度 | **step 359/756 (47%)**, epoch 2 进行中 |
| 训练速度 | ~3.7 s/it |
| Epoch 1 eval loss | **0.0952** |
| Checkpoint | `checkpoint-252` 已保存 (epoch 1 结束) |
| 运行时间 | ~23 分钟 |
| 预估剩余 | ~25 分钟 (约 06:49 完成 epoch 2 eval, 总计约 50 分钟完成全部 3 epochs) |

训练健康，loss 很低 (0.095)，速度稳定。预计约 **06:50 UTC** 完成全部训练。

---
