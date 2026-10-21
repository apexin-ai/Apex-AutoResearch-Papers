# ops server audit cqa1

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-audit-cqa1_20260523T194902_result.json`
- **Structured JSON:** [`c605d7c130f8ea6bbccf.json`](../../sessions/c6/c605d7c130f8ea6bbccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器审计报告 — cqa1-38874

### GPU
| 项目 | 值 |
|------|-----|
| 型号 | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 显存 | 97,887 MiB (~96 GB) |
| 当前使用 | 0 MiB / 0% 利用率 |

### 运行进程
- **无 Python/vLLM/PyTorch 训练进程在跑**
- 后台服务：supervisord、sshd、JupyterLab、HTTP server (port 18765)
- 一个 tmux session `exp_unconstrained_decoding_ablation` 残留（bash idle）

### 项目目录
| 项目 | 值 |
|------|-----|
| 总大小 | **1.6 GB** |
| artifacts/ | 67 个子目录 + 大量 JSON/PT 文件 |
| results/ | 评估结果、分析 JSON、可视化 PNG/PDF |

### 重要数据文件
- **.pt 文件**（22 个）：embedding 矩阵、相似度矩阵（sim_matrix.pt、type_embeddings.pt、bcs_matrix 等）
- **.json 文件**：大量实验配置、预测结果、评估结果（predictions_exp1.json 51MB、predictions_exp2.json 31MB 等）
- **无 .safetensors 文件**

### 模型缓存
| 路径 | 大小 |
|------|------|
| /root/autodl-tmp/ | **213 GB** |
| /root/autodl-tmp/.hf_cache/ | **100 GB** |

缓存内容：
- `llama-3.3-70b-instruct-fp8`
- `qwen3-32b-fp8`
- `sentence-transformers/all-MiniLM-L6-v2`
- `DFKI-SLT/few-nerd` 数据集

/root/autodl-tmp/models/：
- `llama-3.1-8b-instruct`
- `llama-3.1-8b-instruct-ms`

### 磁盘使用
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30 GB | 22 GB | 8.8 GB | **71%** |
| /root/autodl-tmp (数据盘) | 250 GB | 213 GB | 38 GB | **85%** |

### vLLM 服务
**未运行。** GPU 完全空闲。

---
