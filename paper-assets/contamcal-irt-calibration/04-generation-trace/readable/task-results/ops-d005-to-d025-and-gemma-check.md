# ops d005 to d025 and gemma check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d005-to-d025-and-gemma-check_20260518T132619_result.json`
- **Structured JSON:** [`bfd044482aabc660d1a6.json`](../../sessions/bf/bfd044482aabc660d1a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1：d005 → d025
- **d005 完成**：train_loss=0.9299, mean_token_accuracy=0.7896, 3177 steps, 1h30m, checkpoint 639MB, lora_alpha=32 ✓
- **d025 已启动**：cuda:0, PID 30306, 54133 样本, 正在 tokenizing（很快进入训练）
  - 参数：lora_r=16, lora_alpha=32, lr=5e-5, batch=2, grad_accum=8, epochs=1

### 任务 2：Gemma
- **下载未完成**：5/8 safetensors 已下载（001, 002, 005, 007, 008），缺 003, 004, 006
- 下载进程 PID 6380 活跃，6/18 files (33%)，已跑 5h21m
- .cache 中有 12GB 部分数据，按当前速率（~2-3h/shard）预计还需 6-9 小时
- cuda:3 无法启动训练，需等下载完成

### 全卡状态
| GPU | 状态 | 任务 |
|-----|------|------|
| cuda:0 | 550MiB, 加载中 | d025 s42 (PID 30306) |
| cuda:1 | 17.7GB, 91% | 训练中 (PID 25326) |
| cuda:2 | 64.8GB, 92% | 训练中 (PID 28900) |
| cuda:3 | 0MiB, 100% util | 空闲（残留 util 状态），等待 Gemma |

另有 OLMo-2 (PID 19571)、Phi-4 (PID 19608)、Qwen2.5-14B (PID 28640) 在后台下载中。

---
