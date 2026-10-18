# ops check gpu status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-status_20260514T224529_result.json`
- **Structured JSON:** [`e5b2acf4e38cfea7b7f7.json`](../../sessions/e5/e5b2acf4e38cfea7b7f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 进程 1: gemma2_hires_bf16_2bitonly (PID 268242, cuda:0)
- **状态**: 🟢 运行中 (Rl, 已运行 41:24)
- **GPU**: GPU 0 @ 100% util, 513W, 72°C, 32.2GB VRAM
- **进度**: 141/336 heads (42%), ETA ~57 min
- **关键指标**:
  - Baseline PPL: **7.3200**
  - delta 范围: -0.008 ~ 0.190 (L0H1 离群值 0.19)

### 进程 2: llama_c4_hires_crossdataset (wrapper PID 271984, python 271994, cuda:1)
- **状态**: 🟢 运行中 (Ss+, 已运行 02:36)
- **GPU**: GPU 1 @ 100% util, 499W, 75°C, 23.5GB VRAM
- **进度**: Phase 1 C4 hires profiling 128/256 heads (50%), ETA ~2.3 min for phase 1
- **关键指标**:
  - C4 hires baseline PPL: **7.2203**
  - 64 seq × 2048 tok bf16 profiling

两个实验都健康运行，无需干预。Gemma2 还需 ~1 小时，Llama_c4 Phase 1 即将完成进入后续阶段。

---
