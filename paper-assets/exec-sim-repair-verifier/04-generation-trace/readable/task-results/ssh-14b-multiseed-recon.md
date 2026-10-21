# ssh 14b multiseed recon

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-multiseed-recon_20260523T041432_result.json`
- **Structured JSON:** [`6186a72f0f9904b08f09.json`](../../sessions/61/6186a72f0f9904b08f09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

---

## 服务器探测结果汇总

### 1. GPU 状态 — 全部空闲

| GPU | 型号 | 总显存 | 已用 | 利用率 |
|-----|------|--------|------|--------|
| 0 | RTX 5090 | 32 GB | 0 MB | 0% |
| 1 | RTX 5090 | 32 GB | 0 MB | 0% |
| 2 | RTX 5090 | 32 GB | 0 MB | 0% |
| 3 | RTX 5090 | 32 GB | 0 MB | 0% |

**4 块 GPU 全部空闲，可同时跑 4 个独立训练任务。**

### 2. Qwen3-14B 模型

模型位于 `/dev/shm/Qwen3-14B`（内存盘，~28GB）。已就绪，无需重新下载。

### 3. 已有 14B s42 训练配置（从 adapter_config + trainer_state 提取）

| 参数 | CLS 14B (s42_v2) | CWM 14B (s42) |
|------|-------------------|---------------|
| LoRA rank | 16 | 16 |
| LoRA alpha | 32 | 32 |
| LoRA dropout | 0.05 | 0.05 |
| target_modules | q/k/v/o_proj | q/k/v/o_proj |
| quantize | 4bit (QLoRA) | 4bit (QLoRA) |
| batch_size | 1 | 1 |
| grad_accumulation | （推断 ~32） | （推断 ~32） |
| lr | ~5e-5 peak (cosine) | ~5e-5 peak |
| epochs | 3 | 3 |
| max_seq_length | 2048 | 2048 |
| warmup_ratio | 0.05 | 0.05 |
| total steps | 1434 | 1434 |
| best checkpoint | step 956 (epoch 2) | step 956 |

从 `train_14b_cwm_pilot.sh` 确认完整命令参数：`--lr 2e-4 --batch_size 1 --grad_accumulation 32 --lora_rank 16 --lora_alpha 32 --epochs 3 --max_seq_length 2048 --warmup_ratio 0.05 --weight_decay 0.01`

### 4. 训练数据

| 文件 | 行数 |
|------|------|
| `data/train.jsonl` (CLS) | 15,290 |
| `data/val.jsonl` (CLS) | 1,896 |
| `data/cwm_train.jsonl` | 15,290 |
| `data/cwm_val.jsonl` | 1,896 |

### 5. 磁盘空间

| 分区 | 总量 | 已用 | 剩余 |
|------|------|------|------|
| `/root/autodl-tmp` | 250 GB | 201 GB | **50 GB** |
| `/dev/shm` (内存盘) | 180 GB | 28 GB | 153 GB |
| `/` (根分区) | 30 GB | 22 GB | 8.5 GB |

已有 14B checkpoint 每个 ~600MB（LoRA adapter 含 optimizer state）。4 个新 checkpoint（每个最终 ~600MB × save_total_limit 3 = ~1.8GB）总计 ~7.2GB。**50GB 余量充足。**

### 6. 已有 14B checkpoint

- `checkpoints_cls14b_func_s42_v2/` — 607MB，含 checkpoint-956（best）、checkpoint-1434
- `checkpoints_cwm14b_func_s42/` — 607MB，含 checkpoint-956（best）、checkpoint-1434
- `checkpoints_cls14b/` — 空目录

### 结论

**可以立即启动 4 路并行 14B multi-seed 训练：**
- 4x RTX 5090 全部空闲，每 GPU 跑一个 seed（QLoRA 14B 单卡 ~14-16GB 显存）
- 模型已在 `/dev/shm/Qwen3-14B`
- 磁盘余量 50GB，够存 4 组新 checkpoint
- 复制 s42 配置，只需改 `--seed` 和 `--output_dir`

---
