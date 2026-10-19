# ops latency measurement

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_latency-measurement_20260519T021351_result.json`
- **Structured JSON:** [`1f8ff7dfc8ff8e686721.json`](../../sessions/1f/1f8ff7dfc8ff8e686721.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process exited cleanly. Here are the results:

## SmolVLA + CRM Latency Breakdown (K=10)

**GPU: NVIDIA GeForce RTX 4090** | CUDA 12.8, PyTorch 2.10.0

| Component | Mean (ms) | Std (ms) | Trials |
|---|---|---|---|
| SmolVLA encode_prefix | 38.16 | 6.84 | 100 |
| SmolVLA generate K=1 (cached KV) | 177.09 | 13.48 | 100 |
| SmolVLA generate K=10 (cached KV) | 1763.94 | 41.26 | 100 |
| **SmolVLA single forward (K=1, e2e)** | **209.42** | 8.17 | 100 |
| **SmolVLA K=10 forward (e2e)** | **1820.39** | 98.14 | 100 |
| CGS compute_features | 8.52 | 0.74 | 100 |
| Argmin selection | 0.28 | 0.02 | 100 |
| CRM single inference | 0.32 | 0.02 | 100 |
| **Total pipeline (K=10, e2e)** | **1778.06** | 84.82 | 100 |
| | | | |
| VLA-only baseline (K=1) | 209.42 | 8.17 | 100 |
| **Overhead ratio (pipeline/VLA K=1)** | **8.49x** | | |

### Key takeaways

- **Flow-matching denoising dominates**: 10 steps per sample, 10 samples = 100 denoising steps total. Generation is ~97% of total time.
- **CRM + CGS + argmin overhead is negligible**: only 9.12 ms combined (0.5% of total pipeline).
- **Encode prefix (VLM forward) is shared**: 38ms, amortized across all K samples.
- **K=10 VLA / K=1 VLA = 8.69x** (not 10x due to shared prefix encoding).
- **No anomalies**: no OOM, no CUDA errors. GPU 2 used ~5.8GB VRAM.

---
