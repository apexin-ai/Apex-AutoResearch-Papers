# ssh env setup and data

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_env-setup-and-data_20260514T163452_result.json`
- **Structured JSON:** [`f1aaac9649df62bfebb7.json`](../../sessions/f1/f1aaac9649df62bfebb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇报

### 1. GPU 状态
- **型号**: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB)
- **显存**: 0 MiB / 97887 MiB — 已完全释放

### 2. 环境
| 组件 | 版本 |
|------|------|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.10.0+cu128 |
| CUDA | 可用, 1 GPU |
| vLLM | 0.18.1 |
| transformers | 4.57.6 |
| datasets | 4.8.4 |
| accelerate | 1.13.0 |
| scipy/matplotlib/seaborn/wandb | 已装 |

### 3. 磁盘
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| 根分区 / | 30G | 22G | 9.0G |
| 数据盘 /root/autodl-tmp | 250G | 220G | 31G |

### 4. Few-NERD 数据
- 已下载（supervised config），test set 37648 条
- **66 types, 96902 span-level instances**
- **所有 type 均 >= 20 instances**（最少的 art-painting = 58）
- Top 3: location-GPE (20409), person-other (8767), organization-other (4476)
- 统计文件: `/root/schema-dag-extraction/data/few_nerd_type_stats.json`
- Type definitions: `/root/schema-dag-extraction/configs/few_nerd_types.json` (66 types)

### 5. 模型下载 — BLOCKER
**Qwen3-27B 不存在**（HuggingFace 和 ModelScope 均无此模型）。

可用 Qwen3 模型：
- **Qwen3-32B** — 最接近的 dense 模型，但 ~64GB FP16，数据盘仅剩 31GB，**装不下**
- **Qwen3-14B** — 可装下（~28GB）
- **Qwen3-30B-A3B** — MoE，active 参数仅 3B
- **Qwen3-8B** — 可装下

另外 AutoDL 代理导致 HuggingFace API 返回 401，需要用 ModelScope 下载或清理磁盘空间后用 HF 镜像。

**需要你确认用哪个模型**，以及是否需要清理磁盘空间。

---
