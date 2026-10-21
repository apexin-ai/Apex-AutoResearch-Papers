# diagnosis gpu status 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu-status-28034_20260519T165902_result.json`
- **Structured JSON:** [`515b9d624cfa58463871.json`](../../sessions/51/515b9d624cfa58463871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 实时状态 — westd-28034

### 各 GPU 状态

| GPU | 型号 | 利用率 | 显存占用 | 进程 |
|-----|------|--------|----------|------|
| 0 | RTX 5090 | **0%** | 5 / 32607 MiB | 无 |
| 1 | RTX 5090 | **66%** | 31432 / 32607 MiB | `run_exp008v3_binary_probe_grpo.py --local_rank=0` (PID 104503) |
| 2 | RTX 5090 | **65%** | 30670 / 32607 MiB | `run_exp008v3_binary_probe_grpo.py --local_rank=1` (PID 104504) |
| 3 | RTX 5090 | **0%** | 4 / 32607 MiB | 无 |

### 实验存活状态

| 实验 | 状态 | 说明 |
|------|------|------|
| exp-008v3 训练 (GPU 1+2) | **存活** | DeepSpeed 双卡运行中，tmux session `exp-008v3` 存在，两个 worker 进程正常 |
| exp-004 eval (GPU 0) | **不存在** | GPU 0 空闲，无 tmux session `exp-004` |
| exp-016 re-eval (GPU 3) | **不存在** | GPU 3 空闲，无相关进程 |

### 空闲 GPU

**GPU 0 和 GPU 3** 完全空闲（利用率 0%，无进程），可立即使用。

---
