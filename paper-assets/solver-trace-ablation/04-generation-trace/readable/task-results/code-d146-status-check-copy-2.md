# code d146 status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-status-check_20260519T173947_result.json`
- **Structured JSON:** [`c2380b9cc2a0d7bd3aa2.json`](../../sessions/c2/c2380b9cc2a0d7bd3aa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 Pipeline 状态报告

### 1. Pipeline 在运行
- tmux session `d146-pipeline` 存活，训练进程活跃（CPU 98%）

### 2. 当前实验：`d146_pf_exec_s43`
- **进度：427/500 steps (85%)**，预计剩余 ~16 分钟
- 当前 reward ≈ 0.5–1.0，ISR ≈ 0.16–0.24，parse_rate = 1.0
- 已保存 checkpoint-400

### 3. 已完成实验
- **`d146_pf_exec_s42`** — 500/500 steps 完成 ✓
  - 最终：reward=1.0, prove_rate=1.0, ISR=0.0, parse_rate=1.0
  - 模型权重已保存（4 shard safetensors + checkpoint-500）

### 4. GPU / 磁盘

| 资源 | 使用 | 总量 | 占比 |
|------|------|------|------|
| GPU 显存 | 85.4 GB | 97.9 GB | 87% |
| 根分区 | 9.1 GB | 30 GB | 31% |
| 数据盘 | 97 GB | 250 GB | 39% |

磁盘和 GPU 状态健康，s43 预计约 16 分钟内完成。

---
