# ssh env probe

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_env-probe_20260515T101035_result.json`
- **Structured JSON:** [`bc761d279eaa85c4c227.json`](../../sessions/bc/bc761d279eaa85c4c227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探测完成，汇总如下：

## westd-34887 环境探测结果

| 项目 | 详情 |
|------|------|
| **GPU** | 2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 每卡 94GB |
| **驱动** | 580.95.05 |
| **CUDA** | 12.8（torch cu128 编译） |
| **PyTorch** | 2.8.0+cu128, CUDA 可用 |
| **Python** | 3.12（conda base） |
| **根分区** | 30G 总 / 20G 可用（34% 已用） |
| **数据盘** | `/root/autodl-tmp` 250G 总 / 241G 可用 |
| **环境激活** | `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` |
| **项目目录** | `/root/distill_sparse_swiglu/{src,data,checkpoints,logs}` ✅ 已创建 |
| **预置镜像** | 未检测到 aml-train 镜像（无 `.aml_image.json`），但 conda + ML 包已齐全 |

**已安装 ML 包**：accelerate 1.13.0, datasets 4.8.5, einops 0.8.2, modelscope 1.36.3, transformers 5.8.1, wandb 0.27.0 — 所有项目依赖均已就位，无需额外安装。

---
