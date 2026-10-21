# analysis bench dense results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bench_dense_results_20260516T061410_result.json`
- **Structured JSON:** [`1c6d517e54135e8535b2.json`](../../sessions/1c/1c6d517e54135e8535b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## bench_dense 完整指标 — Llama-3.1-8B Dense Baseline

| Benchmark | Metric | Value | Stderr |
|-----------|--------|-------|--------|
| **WikiText-2** | PPL | **6.1173** | — |
| **ARC-Challenge** (25-shot) | acc | 0.5478 | ±0.0145 |
| | acc_norm | **0.5828** | ±0.0144 |
| **WinoGrande** (5-shot) | acc | **0.7806** | ±0.0116 |
| **MMLU** (5-shot) | acc | **0.6527** | ±0.0038 |
| **GSM8K** (8-shot) | exact_match (flexible) | **0.4875** | ±0.0138 |
| | exact_match (strict) | 0.4860 | ±0.0138 |

所有 5 项 benchmark 正常完成，EXIT_CODE=0。Results JSON 已保存在 `/root/distill_sparse_swiglu/results/benchmark/bench_dense/results.json`。

---
