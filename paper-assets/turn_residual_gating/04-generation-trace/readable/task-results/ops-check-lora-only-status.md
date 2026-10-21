# ops check lora only status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_lora_only_status_20260519T125134_result.json`
- **Structured JSON:** [`49ea651750f686e8dced.json`](../../sessions/49/49ea651750f686e8dced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 wandb 日志。训练进程 stdout 走 pipe，没有直接 log 文件。根据 checkpoint 时间戳推算进度。

**LoRA-only 训练状态 (PID 46085)**

| 项目 | 状态 |
|------|------|
| 进程 | **运行中**，已运行 5h31m，CPU 99.9% |
| GPU | 利用率 98%，显存 91.3 / 97.9 GiB |
| 命令 | `train_phase2.py --gate-type none --epochs 3 --seed 42` |
| 输出目录 | `runs/phase2_lora_only_s42/` |

**Checkpoint 进度：**

| Checkpoint | 保存时间 | 状态 |
|------------|----------|------|
| epoch_0/lora/ | 17:14 | 已保存 (adapter_model.safetensors, 19MB) |
| epoch_1/lora/ | 19:09 | 已保存 |
| epoch_2 | — | **训练中** |

**进度估算：**
- 进程约 ~14:00 启动，epoch 0 耗时 ~3h14m，epoch 1 耗时 ~1h55m
- epoch 1 于 19:09 完成，当前正在跑 epoch 2（最后一个 epoch）
- 按 epoch 1 的耗时推算，epoch 2 预计约 **21:00 前后完成**，剩余约 **1.5 小时**

没有 log 文件和 wandb，无法获取精确 step 级进度。如需实时 step 信息，下次启动时建议将 stdout 重定向到 log 文件。

---
