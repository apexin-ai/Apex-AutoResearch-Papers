# eval wallclock speedup 30 50

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_wallclock_speedup_30_50_20260517T152859_result.json`
- **Structured JSON:** [`4d911ed70e36a5cb1cb4.json`](../../sessions/4d/4d911ed70e36a5cb1cb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Profiling complete. Registry and artifacts updated.

**Summary:**

- **No wall-clock speedup** with either approach tested:
  - **Mask-based** (current implementation): 0.87-0.94x — slower due to predictor overhead, all matmuls still execute fully
  - **Structured skip** (weight subsetting): 0.45-0.74x — GPU gather overhead far exceeds compute savings

- **Theoretical FLOPs reduction is real**, requiring custom sparse kernels to realize:
  - 30% sparsity: 1.36x (28% actual mean sparsity, 8.27 vs 11.27 GFLOP/token)
  - 50% sparsity: 2.45x (60.5% actual mean sparsity, 4.61 vs 11.27 GFLOP/token)

- **Predictor overhead is small**: ~1 ms decode, ~2 ms prefill (all 32 layers)

For the paper, report **theoretical FLOPs reduction** (1.36x / 2.45x), not wall-clock speedup. Wall-clock speedup requires sparse kernels (triton semi-structured, 2:4 sparsity hardware support, or custom gather-scatter kernels) which are outside scope.

---
