# infra westd 48478 explore

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-48478-explore_20260512T185902_result.json`
- **Structured JSON:** [`000031dcf0d5b7578812.json`](../../sessions/00/000031dcf0d5b7578812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-48478 (seetacloud-westd-4x5090) 探测报告

### GPU
| 项目 | 值 |
|------|-----|
| 型号 | NVIDIA GeForce RTX 5090 |
| 数量 | 4 张 |
| 单卡显存 | 32 GB |
| 总显存 | 128 GB |
| 驱动 | 580.105.08 |
| 当前 GPU 进程 | **无**（全部空闲） |

### 系统
| 项目 | 值 |
|------|-----|
| CPU | Intel Xeon Platinum 8470Q, 208 线程 (2x52c HT) |
| RAM | 754 GB（已用 20 GB，可用 723 GB） |
| 根分区 | 30 GB（已用 20 GB，剩余 11 GB，**64% 占用**） |
| /home | 与根分区同一 overlay |

### Python / CUDA 环境
| 项目 | 版本 |
|------|------|
| Python | 3.10.12 |
| CUDA Toolkit | 12.8 |
| PyTorch | 2.11.0+cu128 |
| Transformers | 5.8.0 |
| PEFT | 0.19.1 |
| Accelerate | 1.13.0 |
| TRL | **未安装** |
| flash-attn | **未安装** |

### 项目代码与数据
- 项目目录 `/home/sonny/exec-sim-repair-verifier/` **已就绪**，4.5 GB
- 数据目录 `data/` 1.2 GB，含 train/val/test + cwm/trace/traj 全套 JSONL
- `train.jsonl` 15,290 行，`cwm_train.jsonl` 15,290 行
- 已有多轮训练 checkpoints（cls8b/cwm8b/seed 变体），共 ~3.4 GB
- `checkpoints_repo_cls` 和 `checkpoints_repo_cwm` **为空**（repo-level 训练未开始）
- 训练脚本 `train_repo_cwm.py` 和 `train_repo_verifier.py` 已存在
- 无 Qwen 模型缓存（需首次下载）

### 能否跑 repo-level 训练（Qwen3-4B LoRA, 70k samples, max_seq_len=4096）

**可以跑**，硬件绰绰有余。分配的 cuda:2 + cuda:3 = 64 GB 显存，跑 Qwen3-4B LoRA 完全够用（单卡 32 GB 就够 4B LoRA + 4096 seq_len）。

**需要补装/配置的：**

1. **下载 Qwen3-4B 模型** — 服务器无缓存，需下载 ~8 GB。注意根分区只剩 11 GB，模型必须放到项目目录或找到数据盘
2. **安装 TRL** — `pip install trl`
3. **安装 flash-attn**（可选但推荐）— `pip install flash-attn --no-build-isolation`，可显著加速 4096 seq_len 训练
4. **磁盘风险** — 根分区仅剩 11 GB，需确认是否有数据盘挂载点用于存放模型和新 checkpoints。当前项目+checkpoints 已占 4.5 GB，再加模型 + 新 checkpoints 可能撑满根分区

---
