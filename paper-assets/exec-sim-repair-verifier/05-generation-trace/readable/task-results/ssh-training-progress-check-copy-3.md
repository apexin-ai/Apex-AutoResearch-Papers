# ssh training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-progress-check_20260520T004607_result.json`
- **Structured JSON:** [`9f08c47c47cfda44c10e.json`](../../sessions/9f/9f08c47c47cfda44c10e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### 1. qwen3-8b-cwm-repo-s123-train-v2 (GPU 0, pid 881318)
- **状态**: 存活，已运行 8 分钟
- **当前 step**: 10 / 6633（注意：实际总步数 6633，非 13266。70748 samples / 32 grad_accum = 2211 steps/epoch × 3 = 6633）
- **进度**: **0.15%**
- **速度**: ~11.8 s/step
- **预估剩余**: ~21.7 小时
- **GPU 利用率**: 74%, 显存 21251/32607 MiB

### 2. deepseek-cwm-repo-s42-e3-seq4096-eval (GPU 2, pid 833667)
- **状态**: 存活，已运行 12 小时 7 分
- **当前进度**: 9400 / 9784 samples
- **进度**: **96.1%**
- **running_acc**: 61.4%
- **速度**: ~19 s/batch (batch_size=4)
- **预估剩余**: ~30 分钟
- **GPU 利用率**: 67%, 显存 29615/32607 MiB

### 3. qwen3-8b-cwm-repo-s456-train (GPU 3, pid 881460)
- **状态**: 存活，已运行 8 分钟
- **当前 step**: 9 / 6633
- **进度**: **0.14%**
- **速度**: ~12.2 s/step
- **预估剩余**: ~22.4 小时
- **GPU 利用率**: 98%, 显存 31257/32607 MiB

---

Eval 任务即将完成（~30 min），两个训练任务刚启动，预计明早完成。GPU 1 未被这三个实验使用（0 MiB 显存占用）。

---
