# code sparse inference benchmark

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sparse-inference-benchmark_20260519T113305_result.json`
- **Structured JSON:** [`d56f5433842d2709d15f.json`](../../sessions/d5/d56f5433842d2709d15f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Benchmark complete. Summary of results:

**Key findings on RTX PRO 6000 Blackwell, LLaMA-3.1-8B, 30% sparsity:**

| Config | Prefill (ms) | Decode (ms/tok) | Speedup |
|--------|-------------|-----------------|---------|
| Dense bs=1 | 116.6 | 14.48 | 1.000x |
| Sparse 30% bs=1 | 125.1 | 15.23 | 0.932x / 0.950x |
| Dense bs=8 | 1034.2 | 18.51 | 1.000x |
| Sparse 30% bs=8 | 1105.3 | 19.31 | 0.936x / 0.959x |

**Predictor overhead:** 2.5% of prefill, 6-8% of decode (very lightweight).

**Why no speedup:** Zero-masking zeroes neurons but all matmuls still run full-size. The 5-7% slowdown is entirely predictor overhead. Gather-scatter (Python `index_select`) was tested but is 40% slower due to weight-copy overhead.

**Theoretical with sparse CUDA kernels:** ~1.17x prefill, ~1.13x decode speedup possible (30% FFN reduction minus predictor overhead).

Results JSON saved to `results/speedup_benchmark/speedup_results.json` on westd-41718, artifact registered as `art_20260519_10c6a7`.

---
