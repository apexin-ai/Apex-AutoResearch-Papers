# diagnosis 28034 full status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_28034-full-status_20260520T071500_result.json`
- **Structured JSON:** [`732db656989bd3535d8a.json`](../../sessions/73/732db656989bd3535d8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-28034 全面状态报告

### GPU 状态
| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|---------|
| 0 | RTX 5090 | 0% | 5 MiB / 32607 MiB |
| 1 | RTX 5090 | 100% | 31432 MiB / 32607 MiB |
| 2 | RTX 5090 | 62% | 30668 MiB / 32607 MiB |
| 3 | RTX 5090 | 100% | 4 MiB / 32607 MiB |

**GPU 进程**: PID 200881 占 GPU1 (31422 MiB), PID 200882 占 GPU2 (30658 MiB) — 均为 exp-009 训练进程。

### Llama-3-8B 下载
- **PID 214625**: 存活，已运行 **2h52m**
- **下载速度**: ~400 KB/s（ModelScope）
- **进度**:
  - model-00001-of-00004.safetensors: **97%** (4.51G/4.63G), 剩余 ~5min
  - model-00002-of-00004.safetensors: **98%** (4.56G/4.66G), 剩余 ~4min
  - model-00003-of-00004.safetensors: **99%** (4.55G/4.58G), 剩余 ~1.5min
  - model-00004-of-00004.safetensors: **已完成** (1.17GB, 已落盘到正式目录)
- **config.json**: 已存在于 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3-8B-Instruct/`
- 其余 3 个 shard 仍在 `._____temp/` 临时目录，下载完成后会自动移入正式目录
- **预计 5-10 分钟内全部完成**

### EXP-009 训练
- **PID 200283**: 存活，已运行 **4h08m**
- **进度**: step **714/8000** (9%)，~19.2s/step
- **最新 reward**:
  - r1_mean (格式): 0.57~0.87
  - r2_mean (探针): 0.00
  - r3_mean (校准): 0.47~0.84
  - combined_mean: 0.49~0.85
- **Checkpoint**: checkpoint-500 已保存，含 adapter_model.safetensors (117MB)、tokenizer、DeepSpeed 状态
- **使用 GPU 1,2**，通过 DeepSpeed 启动，master_port=29502
- **r2_mean 持续为 0**，探针 reward 可能存在问题

### 其他进程
- exp-008v3 的 tmux session 仍在，但无活跃 GPU 占用（已完成或已停止）
- GPU 0 和 GPU 3 空闲可用

---
