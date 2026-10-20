# launch seed123 eval move westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_seed123_eval_move_westd2_20260522T123552_result.json`
- **Structured JSON:** [`eb19e9f31778f163b689.json`](../../sessions/eb/eb19e9f31778f163b689.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移完成。

### 结果

| 项目 | 值 |
|------|-----|
| 旧 PID (GPU:3) | 41541 — 已 kill |
| 新 PID (GPU:2) | 46229 (python 子进程，父 bash PID 46224) |
| GPU:2 显存 | 9215MiB / 97887MiB，正在推理 |
| GPU:3 | 只剩 depth-first (PID 40073, 16483MiB)，不再拥挤 |

### nvidia-smi 摘要
- GPU:0 — 29137MiB, 99% util (PID 43755)
- GPU:1 — 17651MiB, 92% util (PID 5241)
- **GPU:2 — 9215MiB, 11% util (PID 46229, seed123 eval)** ← 新
- GPU:3 — 16483MiB, 91% util (PID 40073, depth-first only)

### 日志
模型已加载到 cuda:0 (映射为物理 GPU:2)，GSM8K 1319 samples 评估已开始，`Evaluating: 0%`。

---
