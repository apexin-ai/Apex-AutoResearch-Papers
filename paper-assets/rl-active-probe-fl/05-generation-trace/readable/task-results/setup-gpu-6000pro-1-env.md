# setup gpu 6000pro 1 env

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_gpu-6000pro-1-env_20260514T124000_result.json`
- **Structured JSON:** [`ba2efdd2cefc7cddcc21.json`](../../sessions/ba/ba2efdd2cefc7cddcc21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境已完全就绪，无需额外安装。汇报如下：

---

### gpu-6000pro-1 环境状态

| 项目 | 状态 |
|------|------|
| **OS** | Ubuntu 22.04.5 |
| **Python** | 3.12.3 (conda base) |
| **CUDA** | 12.8 (nvcc V12.8.93) |
| **GPU** | 2× RTX PRO 6000 Blackwell 94GB |
| **驱动** | 595.58.03 |

### 关键包版本

| 包 | 版本 |
|---|---|
| torch | 2.10.0+cu128 |
| transformers | 4.57.6 |
| trl | 1.1.0 |
| peft | 0.19.0 |
| accelerate | 1.13.0 |
| datasets | 4.8.4 |
| vllm | 0.18.1 |
| wandb | 0.26.0 |
| flashinfer | 0.6.6 |
| einops | 0.8.2 |

### 代码与模型

- **代码**：`/root/autodl-tmp/diagprobe/` 已同步（含 src/ 全部文件）
- **模型**：Qwen3-8B ✓，Qwen3-30B-A3B ✓（均在 `/root/autodl-tmp/models/Qwen/`）

### 缺什么

无。环境、代码、模型全部就绪，可以直接跑实验。

---
