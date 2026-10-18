# analysis llama heuristic k2 exit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_heuristic_k2_exit_20260514T120541_result.json`
- **Structured JSON:** [`b8b81a33b0af9ece4494.json`](../../sessions/b8/b8b81a33b0af9ece4494.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **llama_heuristic_k2** 完成，registry 已更新，cron 已清除。

### 结果摘要

| Method | PPL (k=2) | PPL (k=16 旧) |
|--------|-----------|---------------|
| Baseline bf16 | 8.0918 | 8.0918 |
| MCKP | 8.4498 | 8.4498 |
| Uniform 4-bit | 8.4690 | 8.4690 |
| L0-random (mean±std) | 8.625±0.073 | 10.479±1.033 |
| Naive Positional | 8.578 | 9.941 |

### 关键发现

- **MCKP vs L0-random gap**: 0.17 (k=2) vs 2.03 (k=16) — 缩小 12 倍
- **MCKP vs Naive gap**: 0.13 (k=2) vs 1.49 (k=16) — 缩小 11 倍
- **L0-random 方差**: 0.073 (k=2) vs 1.033 (k=16) — 稳定 14 倍
- k=2 是更公平的比较（只有 2 个 2-bit heads），MCKP 优势缩小但仍显著存在，验证 per-head optimization 的价值

---
