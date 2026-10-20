# ssh check deepseek training progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_deepseek_training_progress_20260515T141138_result.json`
- **Structured JSON:** [`c764c8676876acae99b0.json`](../../sessions/c7/c764c8676876acae99b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

| | deepseek_exception_only_seed42 | deepseek_full_trace_seed42 |
|---|---|---|
| **GPU** | cuda:1 | cuda:0 |
| **当前 step** | 224 / 444 (50%) | 68 / 444 (15%) |
| **当前 epoch** | Epoch 2 (step 76/148) | Epoch 1 (step 68/148) |
| **速度** | ~14 s/step | ~36.5 s/step |
| **预估剩余** | ~51 min | ~3h49m |
| **GPU 利用率** | 100% | 100% |
| **显存占用** | 22.4 GB / 98 GB | 94.0 GB / 98 GB |

两个实验都在正常跑。full_trace 因为输入序列更长，每步慢 2.6 倍且显存占用高很多（94GB vs 22GB）。exception_only 预计约 1 小时内完成，full_trace 还需要约 4 小时。

---
