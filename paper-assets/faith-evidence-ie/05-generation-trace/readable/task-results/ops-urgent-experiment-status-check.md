# ops urgent experiment status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-experiment-status-check_20260516T011848_result.json`
- **Structured JSON:** [`97807133fd1c0ef92ba4.json`](../../sessions/97/97807133fd1c0ef92ba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验进程存活且正在运行中。各实验实际运行时间远不到 12 小时。逐一报告：

---

### 1. eval_flat_nli_s44 (PID 270462, GPU 0)
- **状态**: alive, 运行 1h51m
- **进度**: 155/247 batches (63%)，~45s/batch
- **预计剩余**: ~69 min
- **GPU**: 11091/32607 MiB, 48% util

### 2. eval_flat_nli_seed45 (PID 272164, GPU 3)
- **状态**: alive, 运行 1h34m
- **进度**: 122/247 batches (49%)，~50s/batch
- **预计剩余**: ~104 min
- **GPU**: 11095/32607 MiB, 51% util

### 3. rsft_ced_s43_train_r3 (PID 277310, GPU 1)
- **状态**: alive, 运行 58 min
- **进度**: 日志可见到 340/510 steps (67%)，~5.5s/step，含中间 eval。epoch 2.35, loss ~0.61
- **预计剩余**: ~15 min
- **GPU**: 28679/32607 MiB, 34% util

### 4. rsft_ced_s45_train_r4 (PID 279531, GPU 2)
- **状态**: alive, 运行 44 min
- **进度**: 464/510 steps (91%)，~6s/step，epoch ~2.35, loss ~0.61
- **预计剩余**: ~5 min
- **GPU**: 28341/32607 MiB, 99% util

---

**结论**: 4 个实验全部正常运行中，没有卡住或失败。实际提交时间在 ~2 小时内，并非 12 小时前。cron 未触发是因为它们尚未结束。

- rsft_ced_s45_train_r4 约 5 分钟后完成
- rsft_ced_s43_train_r3 约 15 分钟后完成
- eval_flat_nli_s44 约 1h 后完成
- eval_flat_nli_seed45 约 1h40m 后完成

---
