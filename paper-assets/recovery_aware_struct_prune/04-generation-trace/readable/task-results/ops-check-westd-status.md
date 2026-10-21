# ops check westd status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd-status_20260516T022051_result.json`
- **Structured JSON:** [`7ae8ed02850999876fbb.json`](../../sessions/7a/7ae8ed02850999876fbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 实验状态摘要

### eval_sft_unpruned_full — RUNNING
- **PID**: 74129 → 子进程 74134 占 GPU-0 (17654 MiB)
- **进度**: 894/1319 (67.8%)，已跑 42 分钟
- **当前 accuracy**: **81.76%** (截至 850 样本)，eos_rate=99.76%
- **预计剩余**: ~18 分钟（约 2.5s/样本）

### grpo_unpruned_v2 — RUNNING, 无冲突
- **PID 75381**: 已死
- **PID 77647**: 存活 → 子进程 77652 占 GPU-1 (91018 MiB)
- **进度**: **31/100 steps** (31%)，从 checkpoint-20 恢复，~34s/step
- **Checkpoints**: checkpoint-20, checkpoint-25, checkpoint-30
- **预计剩余**: ~39 分钟

### 磁盘
- `/root/autodl-tmp/`: 205G / 250G used，**46G 可用** (82%)

---
