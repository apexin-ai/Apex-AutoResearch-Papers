# infra setup westd 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_setup-westd-41312_20260516T110521_result.json`
- **Structured JSON:** [`8bc65fb808f955d8368d.json`](../../sessions/8b/8bc65fb808f955d8368d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇报如下：

---

## westd-41312 环境就绪

| 项目 | 状态 |
|------|------|
| **GPU** | 4× NVIDIA RTX PRO 6000 Blackwell 94GB, CUDA 可用 |
| **PyTorch** | 2.10.0+cu128 |
| **ML 包** | transformers 4.57.6, accelerate 1.13.0, datasets 4.8.4, einops 0.8.2, wandb 0.26.0 |
| **训练脚本** | `training/pretrain_weighted.py` ✓，`scripts/` 下 46 个 shell 脚本 ✓ |
| **模型** | Llama-3.2-3B (6.4GB) ✓, Qwen3-0.6B (1.5GB) ✓, ModernBERT ✓ |
| **数据** | 11GB 全量同步完成，含 scored_data (ρ=0.2/0.4/0.6)、hybrid、threshold、holdout |
| **磁盘** | 根分区 30G(~24G 可用)，数据盘 250G（数据/模型已放数据盘，软链接到项目目录） |
| **环境激活** | `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` |
| **SSH** | `-p 41312 root@connect.westd.seetacloud.com` |

---
