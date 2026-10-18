# ops check multiseed status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_multiseed_status_20260516T052517_result.json`
- **Structured JSON:** [`d8703d9e8cbaca712860.json`](../../sessions/d8/d8703d9e8cbaca712860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 实验进度 — 都在运行中

**Llama multi-seed** (GPU 0, 42782 MiB, 100% util):
- Uniform 4-bit PPL 已完成: **8.4701**
- 当前: Seed 42 (1/3) profiling 阶段，已到 150/256 heads
- 还需完成: seed 42 profiling 剩余 + constrained eval, 然后 seed 2/3, seed 3/3

**Mistral multi-seed v2** (GPU 1, 41290 MiB, 100% util):
- Uniform 4-bit PPL 已完成: **7.1308**
- 当前: Seed 42 (1/3) profiling 阶段，已到 120/256 heads
- 进度与 Llama 类似

两个实验都还在 seed 1/3 的 profiling 阶段，距离完成还需跑完 3 个 seed 各自的 profiling + constrained eval。结果文件尚未生成。

### Yi 8K spotcheck — max_2bit 已修复

`run_yi15_8k_spotcheck.py` 第 25 行: `max_2bit = 2` — 值正确，无需修改。

---
