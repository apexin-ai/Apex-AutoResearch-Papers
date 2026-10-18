# research westd 27271 c4ext feasibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_westd_27271_c4ext_feasibility_20260519T170422_result.json`
- **Structured JSON:** [`be2aadfc83415e3ffeb3.json`](../../sessions/be/be2aadfc83415e3ffeb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## westd-27271 就绪度报告

### 1. GPU 状态
| GPU | 型号 | 显存 | 已用 | 利用率 |
|-----|------|------|------|--------|
| 0 | RTX PRO 6000 Blackwell Server Edition | 94 GB | 0 MB | 0% |
| 1 | RTX PRO 6000 Blackwell Server Edition | 94 GB | 0 MB | 0% |

**完全空闲，无任何进程占用。**

### 2. PyTorch / CUDA
| 项目 | 版本 |
|------|------|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.8.0+cu128 |
| CUDA | 可用，2 GPU 均检测到 |
| transformers | 5.8.1 |
| accelerate | 1.13.0 |
| einops | 0.8.2 |
| lerobot | 0.5.1 |
| timm | 0.9.16 |
| wandb | 0.24.2 |
| flash_attn | **未安装** |

### 3. OpenVLA fine-tuned model
- **路径**: `/root/autodl-tmp/openvla-libero-object/`
- **大小**: 15 GB（4 个 safetensors 分片）
- **架构**: `OpenVLAForActionPrediction`（基于 Llama-2-7b + DINOv2-SigLIP 双视觉编码器）
- **微调数据**: libero_object（454 trajectories, 66984 transitions）

### 4. 项目代码完整性
- 项目目录 `/root/autodl-tmp/importance_margin_vla_compress/` **存在**，含大量 .py 文件
- `smart_compress_module.py` 在服务器上（SmolVLA 版本）
- **缺失的 OpenVLA 适配代码**（服务器上不存在，本地 `artifacts/` 有）:
  - `openvla_vtc_adapter.py` — OpenVLA VTC 适配器
  - `train_openvla_smart_compress.py` — OpenVLA 训练脚本
  - `eval_openvla_smart_compress.py` — OpenVLA 评估脚本

### 5. 磁盘
- `/root/autodl-tmp/`: 250GB 总量，207GB 已用，**44GB 可用**（够用）

### 6. 缺少什么
| 项 | 紧迫度 | 说明 |
|----|--------|------|
| 同步 3 个 OpenVLA 适配文件到服务器 | **必须** | openvla_vtc_adapter.py, train_openvla_smart_compress.py, eval_openvla_smart_compress.py |
| flash_attn | 可选 | 没有不影响正确性，但 7B 模型训练可能需要以节省显存 |
| nvcc 不在 PATH | 低 | torch 自带 CUDA runtime，编译 flash_attn 才需要 |

### 结论：可以在 30 分钟内开始训练

**需要的步骤**：
1. **同步适配代码**（~2 min）：将本地 `artifacts/` 下的 3 个 OpenVLA 文件 scp/rsync 到服务器 `/root/autodl-tmp/importance_margin_vla_compress/`
2. **检查适配代码依赖**（~5 min）：确认 `openvla_vtc_adapter.py` 的 import 在服务器环境中全部可用
3. **（可选）安装 flash_attn**（~10-15 min）：如果显存紧张可装，94GB×2 跑 7B 可能不需要
4. **启动训练**：配置好 accelerate 后直接跑

环境基本就绪，主要阻塞项是同步 3 个适配文件。

---
