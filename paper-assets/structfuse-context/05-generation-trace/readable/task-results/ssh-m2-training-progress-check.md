# ssh m2 training progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m2_training_progress_check_20260513T223404_result.json`
- **Structured JSON:** [`b50cb16893c5126df1a7.json`](../../sessions/b5/b50cb16893c5126df1a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M2 Full Training 进度报告

### Qwen (cuda:0, PID 73544) — 运行 4h55m
| 指标 | 值 |
|------|-----|
| 当前 | Epoch 1, step 1200 / 1414 |
| 最新 loss | 0.3260 (step 1200) |
| eval@500 | val_loss=0.4869, R@1=53.3%, R@5=95.4%, R@10=100% |
| eval@1000 | val_loss=0.4651, R@1=55.3%, R@5=95.9%, R@10=100% |

Loss 从 0.67 持续下降到 0.33，eval 指标 step 1000 比 500 全面提升。即将完成 Epoch 1（还剩 ~214 步），预计很快进入 Epoch 2。尚未进入 random_s43（当前仍在 s42 Epoch 1/3）。

### StarCoder (cuda:1, PID 76627) — 运行 4h04m
| 指标 | 值 |
|------|-----|
| 当前 | Epoch 1, step 750 / 1414 |
| 最新 loss | 0.5464 (step 750) |
| eval@500 | val_loss=0.6194, R@1=43.5%, R@5=90.5%, R@10=100% |

Loss 从 0.85 下降到 0.55，训练正常。比 Qwen 慢约 450 步（StarCoder 启动晚 ~50 min）。

### GPU 状态
| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| 0 (Qwen) | 100% | 51.6 / 97.9 GB | 68°C |
| 1 (StarCoder) | 100% | 55.2 / 97.9 GB | 71°C |

两个进程均存活，无报错，GPU 满载运行。

---
