# code sf7 timing benchmark

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sf7-timing-benchmark_20260523T182038_result.json`
- **Structured JSON:** [`259af6ee212c40f125c3.json`](../../sessions/25/259af6ee212c40f125c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results summary:

| Step | Time (s) |
|---|---|
| Single DIM estimate | 0.002 ± 0.001 |
| HB Centered EB (optimization) | 0.002 ± 0.000 |
| HB Gibbs MCMC (4 chains × 6k iter) | 4.662 ± 0.114 |
| EC-HTE full pipeline (DIM + EB + inversion) | 0.003 ± 0.000 |
| Bootstrap SE (B=100) | 0.346 ± 0.018 (0.0035/rep) |

Key takeaways:
- The EC-HTE pipeline with centered EB is extremely fast (~3ms) — the optimization-based EB replaces MCMC and runs ~2000x faster than the Gibbs sampler (4.7s)
- Bootstrap SE with B=100 takes ~0.35s total (3.5ms per replicate), since each replicate only re-estimates the EB CM on resampled expert data
- The Gibbs MCMC sampler (4 chains × 2000 warmup + 4000 post-warmup) is the only computationally expensive step at ~4.7s

Saved to `artifacts/timing_benchmark.csv`. Machine: Intel Xeon Platinum 8259CL @ 2.50GHz, 2 cores, 7.6GB RAM.

---
