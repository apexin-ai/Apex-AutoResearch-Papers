# ops check multiseed progress

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_multiseed_progress_20260516T085017_result.json`
- **Structured JSON:** [`2700704774ae6c5d3b0a.json`](../../sessions/27/2700704774ae6c5d3b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Multi-seed PPL 实验状态

| | Llama-3.1-8B (cuda:0) | Mistral-7B-v0.3 (cuda:1) |
|---|---|---|
| **GPU 利用率** | 100%, 42.8GB / 97.9GB VRAM | 100%, 41.3GB / 97.9GB VRAM |
| **已完成** | seed 42 ✅ (PPL=8.4701) | seed 42 ✅ (PPL=7.1348) |
| **当前 seed** | **seed 123** (第 2/3 个) | **seed 123** (第 2/3 个) |
| **剩余** | seed 123 剩余 + seed 456 | seed 123 剩余 + seed 456 |

### 时间估算

每个 seed 耗时 ~2h 57min（profiling ~10,594s + solve/eval ~34s）。

**Llama (PID 399383, 已运行 5h13m)**
- seed 42 完成于 14:36，seed 123 已跑 ~2h15m
- seed 123 剩余 ~42 min，seed 456 需 ~3h
- **预计完成：~20:30 UTC**

**Mistral (PID 401157, 已运行 4h49m)**
- seed 42 完成于 15:00，seed 123 已跑 ~1h51m
- seed 123 剩余 ~1h06m，seed 456 需 ~3h
- **预计完成：~21:00 UTC**

### Seed 42 初步结果

| 模型 | Constrained PPL | Baseline PPL | Δ | 2-bit heads |
|---|---|---|---|---|
| Llama-3.1-8B | 8.4701 | 6.1221 | +2.35 | 0/256 |
| Mistral-7B-v0.3 | 7.1348 | 5.8031 | +1.33 | 2/256 |

---
