# ssh exp 001 env setup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp-001-env-setup_20260513T172844_result.json`
- **Structured JSON:** [`d594e7cfa75805c04d56.json`](../../sessions/d5/d594e7cfa75805c04d56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## exp-001 环境搭建完成

### 1. Python/CUDA/Torch
| 项目 | 版本 |
|------|------|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.11.0+cu130 |
| CUDA | True (driver 580.76.05) |
| transformers | 4.57.6 |
| peft | 0.19.0 |
| trl | 1.4.0 |
| accelerate | 1.13.0 |
| lm_eval | 0.4.11 |

### 2. GPU (6× RTX 4090D)
| 设备 | 显存 |
|------|------|
| cuda:0-5 | 6× NVIDIA GeForce RTX 4090 D 23GB |

### 3. 模型下载状态
| 模型 | 大小 | 路径 |
|------|------|------|
| Qwen2.5-0.5B | 954M | `/root/autodl-tmp/models/Qwen/Qwen2___5-0___5B` |
| Qwen2.5-1.5B | 2.9G | `/root/autodl-tmp/models/Qwen/Qwen2___5-1___5B` |
| Qwen2.5-3B | 5.8G | `/root/autodl-tmp/models/Qwen/Qwen2___5-3B` |
| Qwen2.5-7B-Instruct | 15G | `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct` |
| all-MiniLM-L6-v2 | 88M | `/root/autodl-tmp/models/st/` |

### 4. Benchmark 数据集
| 数据集 | 条数 |
|--------|------|
| MMLU (test) | 14,042 |
| GSM8K (test) | 1,319 |
| ARC-Challenge (test) | 1,172 |
| HumanEval (test) | 164 |
| OpenHermes-2.5 (train) | 1,001,551 |

### 5. 磁盘使用
- `/root/autodl-tmp`: 169G 总量, **162G 已用, 7.3G 剩余 (96%)**

### 6. 注意事项
- **磁盘紧张**：autodl-tmp 只剩 7.3G。旧项目模型（Mistral-7B 14G, Qwen2.5-14B 系列 ~27G, DPO-merged ~30G）占用大量空间。如不再需要可清理释放 ~70G
- **ModelScope 路径**：模型目录使用 `___` 替代 `.`（如 `Qwen2___5-0___5B`），加载时注意路径
- **环境激活**：使用 `source /root/contamcal-irt-calibration/env_setup.sh` 一键配置所有环境变量
- **faiss-gpu 未安装**：当前安装的是 faiss-cpu，如需 GPU 加速相似度搜索需另装

---
