# analysis check gpu training progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_gpu_training_progress_20260519T165836_result.json`
- **Structured JSON:** [`ff508a35fe6ccbc76db3.json`](../../sessions/ff/ff508a35fe6ccbc76db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### 实验 1: codellama13b_ae_only_seed42 (GPU 1, PID 512034)

| 项目 | 状态 |
|------|------|
| 进度 | ~432/444 steps（估算，约 97%） |
| 最新 loss | 0.0245 @ step 290（epoch ~1.96） |
| Eval loss | 0.1745 @ step 296（epoch 2.0） |
| 预估剩余 | ~10 分钟（含 epoch 3 结束后的 eval） |
| 状态 | 正常运行，GPU 100% 利用率 |

注：该实验无独立日志文件（stdout 接入 pipe），进度基于 `checkpoint-296/trainer_state.json`（创建于 23:47）和 ~30s/step 速率估算。

---

### 实验 2: codellama13b_loop_only_seed42 (GPU 0, PID 517775)

| 项目 | 状态 |
|------|------|
| 进度 | 236/444 steps（53%） |
| 最新 loss | 0.0699 @ epoch 0.95（end of epoch 1） |
| 速度 | ~29.5s/step |
| 预估剩余 | ~1h42m |
| 状态 | 正常运行，GPU 100% 利用率 |

---

两个实验均正常。ae_only 即将完成，loop_only 还需约 1.7 小时。

---
