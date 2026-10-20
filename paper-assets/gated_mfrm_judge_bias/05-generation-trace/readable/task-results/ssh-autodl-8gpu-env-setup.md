# ssh autodl 8gpu env setup

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_8gpu_env_setup_20260522T091826_result.json`
- **Structured JSON:** [`e21398bea563e1e639fe.json`](../../sessions/e2/e21398bea563e1e639fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搭建完成。汇总：

---

## autodl-8gpu 环境状态

### GPU
| GPU | 型号 | VRAM |
|-----|------|------|
| 0-3 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 96GB x 4 |

**注意：实际 4 GPU，不是 8。** 名字 autodl-8gpu 具有误导性。

### 版本
- **Python**: 3.12.3 (conda base)
- **CUDA**: 12.8 (nvcc), Driver 580.95.05
- **PyTorch**: 2.11.0+cu130, CUDA 可用
- **JAX**: 0.10.1
- **NumPyro**: 0.21.0
- **Transformers**: 5.9.0
- **vLLM**: 0.21.0
- **其他**: accelerate, datasets, openai, httpx, aiohttp, einops, scipy, pandas 均已安装

### 磁盘
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| 根 `/` | 30GB | 1.2GB | 29GB |
| 数据盘 `/root/autodl-tmp` | 250GB | 76GB | 175GB |

### AutoDL 专项配置
- `network_turbo` ✓
- `HF_HOME=/root/autodl-tmp/.hf_cache` ✓
- `HF_HUB_DISABLE_XET=1` ✓
- SSL 证书环境变量 ✓

### SSH
- rtx6000-4x → autodl-8gpu: SSH key 免密 ✓
- 本地控制机 → autodl-8gpu: SSH key 免密 ✓
- resources.yaml 已更新（env_activate, work_dir, GPU 信息）

### 代码同步
- `/root/gated_mfrm_judge_bias/` 已从 rtx6000-4x rsync 完成 ✓

### 无阻塞项

---
