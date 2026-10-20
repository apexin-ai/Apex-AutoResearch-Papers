# submit medium uncurated cuda0

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_medium_uncurated_cuda0_20260513T190117_result.json`
- **Structured JSON:** [`6b5ec1d22f7842c6b6aa.json`](../../sessions/6b/6b5ec1d22f7842c6b6aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在运行：

- **medium_uncurated** (PID 283798): gpt2-medium, seed=42, gpu_ids=0 — 已启动，正在加载模型/数据（还未上 GPU）
- **seed456_methods** (PID 262538): gpt2, seed=456, cuda:1 — 正常运行中

**汇总**：

| 项目 | 状态 |
|------|------|
| cuda:0 | 49GB orphan 显存（已知），无活跃计算进程 → 可用 |
| medium_uncurated | 已启动，PID 283798，tmux session 存在，模型加载中 |
| seed456_methods | 正常运行，cuda:1，PID 262538 |

实验已成功启动。模型加载完成后日志会开始输出训练进度。

---
