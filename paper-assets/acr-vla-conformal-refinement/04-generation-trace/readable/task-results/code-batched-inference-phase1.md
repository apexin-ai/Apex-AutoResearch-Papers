# code batched inference phase1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batched-inference-phase1_20260519T074634_result.json`
- **Structured JSON:** [`7f4d02585c80c64bef0b.json`](../../sessions/7f/7f4d02585c80c64bef0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D067 Phase 1 complete. Here's the summary:

## Diff

Added `generate_k_samples_batched()` method (~48 lines) to `src/smolvla_wrapper.py`. Both `get_obs_features_and_samples` and `get_obs_features_and_samples_batch` now call the batched method. Original `generate_k_samples` preserved for reference.

Key mechanism: `repeat_interleave(K, dim=0)` on KV cache dict `{layer_idx: {"key_states", "value_states"}}` and `prefix_pad_masks`, then single denoising loop over `B*K` samples.

## Numerical Verification

| Metric | Value |
|---|---|
| Action magnitude | mean=0.28, max=1.02 |
| Max absolute diff | 3.21e-3 |
| Mean absolute diff | 4.47e-4 |
| Mean relative diff | 2.2% |
| Sequential self-consistency | 0.00 (bitwise identical) |

Diff is expected bfloat16 floating point noise from batched vs unbatched CUDA matmul — not a correctness bug.

## Latency Benchmark (B=1, GPU under contention with 3 eval jobs)

| K | Sequential | Batched | Speedup |
|---|---|---|---|
| 5 | 1579 ± 46 ms | 320 ± 13 ms | **4.94x** |
| 10 | 3167 ± 62 ms | 314 ± 13 ms | **10.10x** |
| 20 | 6375 ± 278 ms | 312 ± 5 ms | **20.41x** |

Batched latency is ~314ms regardless of K (all samples parallelized in one forward pass). Sequential scales linearly with K.

## Side fix
Updated `smolvla_libero/config.json` to use local VLM path (`/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct`) with `load_vlm_weights: false` to avoid HF network dependency (all weights are in `model.safetensors`).

---
