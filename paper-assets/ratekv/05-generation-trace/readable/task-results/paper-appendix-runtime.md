# paper appendix runtime

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-runtime_20260514T193142_result.json`
- **Structured JSON:** [`04070cd7f562e4f1a5b2.json`](../../sessions/04/04070cd7f562e4f1a5b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Appendix section added at `appendix.tex:50-78`. It includes:

- **Table** (`\ref{tab:runtime}`): 3 conditions × 3 metrics with caption noting PyTorch-level simulation
- **Analysis paragraph**: MCKP +8.5% over uniform due to mixed-precision dispatch; solver itself is 5ms; same 4x compression as uniform
- **Caveat paragraph**: explicitly states these are not optimized CUDA kernels, production engines with fused kernels would narrow the gap, and the conclusion's "no real-kernel latency benchmarks" limitation still holds

The `\label{sec:runtime}` is in place for cross-referencing from the main text.

---
