# code westd kill and grasp sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-kill-and-grasp-sft_20260515T135104_result.json`
- **Structured JSON:** [`b7ce9cc2cb3cb5929dfd.json`](../../sessions/b7/b7ce9cc2cb3cb5929dfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已启动，正在加载模型（模型较大，GPU 显存尚未分配是因为还在 CPU 加载阶段）。

**执行结果：**
- **Killed**: PID 34206 (GraSP full eval), PID 34195 (tmux), PID 37310 (重复 alpha_4.0 eval)
- **GraSP eval 结果文件**：不存在（进程 kill 前未写入磁盘，partial 结果丢失）
- **已提交**: `sft_grasp_20_westd` on GPU 0, PID 38509, 正在加载模型
- **GPU 1**: 空闲可用

---
