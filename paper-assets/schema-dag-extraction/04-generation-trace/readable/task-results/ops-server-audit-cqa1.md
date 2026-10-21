# ops server audit cqa1

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-audit-cqa1_20260523T195517_result.json`
- **Structured JSON:** [`93306d9481dfc49b60e8.json`](../../sessions/93/93306d9481dfc49b60e8.json)

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
| 当前占用 | 0 MiB / 0% 利用率 |

### 运行中进程
**无 python/torch/vllm 进程。** GPU 完全空闲。

活跃的后台服务：
- JupyterLab（系统自带）
- autopanel / supervisord（AutoDL 管理进程）
- http.server on port 18765（May 18 启动）
- tmux session: `exp_unconstrained_decoding_ablation`（May 18 创建，bash idle）

### vLLM 服务
未运行。

### 项目目录
| 目录 | 大小 |
|------|------|
| `/root/schema-dag-extraction/` 总计 | **1.6 GB** |
| `artifacts/` | 1.4 GB |
| `data/` | 212 MB |

### 数据文件
- **JSON 文件**: 200+（输出截断，覆盖 65 个实验子目录）
- **PT 文件**: 22 个（sim_matrix、type_embeddings、relation_sim_matrix 等）
- **Safetensors**: 0 个

主要实验目录（65 个子目录），涵盖：exp004-exp017、fewrel 系列、maven 系列、bcs 系列、schema_intervention、unconstrained_decoding_ablation 等。

### 模型缓存 (`/root/autodl-tmp/`)
| 内容 | 大小 |
|------|------|
| autodl-tmp 总计 | **213 GB** |
| llama-3.3-70b-instruct-fp8 | 68 GB |
| qwen3-32b-fp8 | 32 GB |
| sentence-transformers/all-MiniLM-L6-v2 | ~27 MB |
| datasets (few-nerd) | 有缓存 |

### 磁盘使用率
| 分区 | 总容量 | 已用 | 可用 | 使用率 |
|------|--------|------|------|--------|
| `/`（根分区） | 30 GB | 22 GB | 8.8 GB | **71%** ⚠️ |
| 数据盘 (NVMe) | 1.8 TB | 21 GB | 1.7 TB | 2% |

**⚠️ 根分区 71% 已用**，剩余 8.8 GB。autodl-tmp 的 213 GB 在数据盘上，空间充足。

---
