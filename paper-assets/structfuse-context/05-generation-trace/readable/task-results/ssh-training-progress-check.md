# ssh training progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training_progress_check_20260513T192824_result.json`
- **Structured JSON:** [`374b76a582f93b590733.json`](../../sessions/37/374b76a582f93b590733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 双卡训练进度

### GPU 状态
| GPU | 型号 | 利用率 | 显存 | 温度 |
|-----|------|--------|------|------|
| 0 (Qwen) | RTX PRO 6000 Blackwell 96GB | 100% | 50.7/95.6 GB (53%) | 72°C |
| 1 (StarCoder) | RTX PRO 6000 Blackwell 96GB | 100% | 55.2/95.6 GB (58%) | 72°C |

### Qwen (cuda:0) — PID 73558
- **当前 run**: `random_s42` (1/9)，启动于 05-14 01:39 CST
- **进度**: Epoch 1, **step 500 / 1414**（35%）
- **最新 loss**: 0.6168, lr=2.00e-05（已到达峰值学习率）
- **eval 指标**: 尚未触发（预计 epoch 结束时 eval）
- **已完成 run**: 0/9，无 best_model checkpoint

### StarCoder (cuda:1) — PID 76627
- **当前 run**: `random_s42` (1/9)，启动于 05-14 02:30 CST
- **进度**: Epoch 1, **step 200 / 1414**（14%）
- **最新 loss**: 0.4387, lr=9.25e-06（还在 warmup 阶段）
- **eval 指标**: 尚未触发
- **已完成 run**: 0/9，无 best_model checkpoint

### 总览
- 两张卡都在跑第 1/9 个 run（`random_s42`），均为 Epoch 1
- Qwen 领先约 50 分钟（更早启动），StarCoder 晚启动因为先跑了数据预处理
- 每个 run 1414 steps/epoch，**还剩 9 个 run × 每 run 多 epoch**，预计还需较长时间
- GPU 满载运行，状态正常

---
