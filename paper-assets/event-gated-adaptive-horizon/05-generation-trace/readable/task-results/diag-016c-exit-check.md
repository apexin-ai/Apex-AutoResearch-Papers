# diag 016c exit check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_016c_exit_check_20260515T192605_result.json`
- **Structured JSON:** [`69ac258b7f971dc90e53.json`](../../sessions/69/69ac258b7f971dc90e53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 016c 诊断结果

**训练进度**：到达 step 5000（目标 105000），完成了第一次 eval（eval_return=31.0），刚开始 training loop 就被杀。

**退出原因**：`EXIT_CODE=137` — SIGKILL（128+9），典型的 **OOM Killer**。日志最后一行：
```
bash: line 1: 523540 Killed    timeout 21600 env bash -c ...
```
不是 timeout（6h 远未到），不是代码错误，不是 eval hang，是系统级 OOM kill。

**GPU 1 当前状态**：空闲，无任何进程。

**Checkpoint**：logdir 中 **没有模型 checkpoint**（只有 tfevents、metrics.jsonl、train_eps/eval_eps），重试需从头开始。

**可重试**：可以。GPU 1 已释放。但需注意 OOM 根因——step 5000 的 training 刚启动就被杀，可能是 replay buffer + 模型 + eval 同时驻留内存导致峰值超限。建议排查：
- 是 GPU OOM 还是 CPU/RAM OOM（137 通常是系统 RAM OOM killer）
- 如果是 RAM，考虑减小 replay buffer 或 prefill 数据量

---
