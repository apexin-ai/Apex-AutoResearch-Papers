# code env setup

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_env-setup_20260518T053533_result.json`
- **Structured JSON:** [`d3d38819facd7b205b2c.json`](../../sessions/d3/d3d38819facd7b205b2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。

**汇总：**

| 项目 | 值 |
|---|---|
| Python | 3.12.3 |
| PyTorch | 2.8.0+cu128 |
| CUDA | 12.8 |
| transformers | 5.8.1 |
| flash-linear-attention | 0.5.0 (GatedDeltaNetForCausalLM 可用) |
| triton | 3.4.0 |
| causal-conv1d | 1.6.2.post1 |
| accelerate | 1.13.0 |
| GPU | NVIDIA RTX PRO 6000 Blackwell (94GB) |

**磁盘：**
- 根分区：30G（已用 3.1G，剩余 27G）— 放 16 个 340M 模型（~5.5GB）没问题
- 数据盘：`/root/autodl-tmp` 250G（几乎全空）— 建议大文件（模型、数据集）存这里

**模型最佳存放路径：** `/root/autodl-tmp/models`（数据盘更大更安全），项目目录下的 `models/` 可软链过去。

**环境激活命令：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PATH=/usr/local/cuda/bin:$PATH
```

---
