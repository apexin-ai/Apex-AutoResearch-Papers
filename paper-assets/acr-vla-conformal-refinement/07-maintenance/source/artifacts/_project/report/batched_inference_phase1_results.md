# D067 Phase 1: Batched VLA Inference Results

**Server**: bjb2-40593
**Worker**: worker_code_batched-inference-phase1_20260519T074634
**Duration**: ~31 min

## Code Change
Added `generate_k_samples_batched()` method (~48 lines) to `src/smolvla_wrapper.py`.
Both `get_obs_features_and_samples` and `get_obs_features_and_samples_batch` now call the batched method.
Original `generate_k_samples` preserved for reference.

Key mechanism: `repeat_interleave(K, dim=0)` on KV cache + prefix_pad_masks, single denoising loop over B*K samples.

## Numerical Verification

| Metric | Value |
|---|---|
| Action magnitude | mean=0.28, max=1.02 |
| Max absolute diff | 3.21e-3 |
| Mean absolute diff | 4.47e-4 |
| Mean relative diff | 2.2% |
| Sequential self-consistency | 0.00 (bitwise identical) |

Diff is expected bfloat16 floating point noise from batched vs unbatched CUDA matmul.

## Latency Benchmark (B=1, GPU under contention with 3 eval jobs)

| K | Sequential | Batched | Speedup |
|---|---|---|---|
| 5 | 1579 ± 46 ms | 320 ± 13 ms | **4.94x** |
| 10 | 3167 ± 62 ms | 314 ± 13 ms | **10.10x** |
| 20 | 6375 ± 278 ms | 312 ± 5 ms | **20.41x** |

Batched latency ~314ms regardless of K (all samples parallelized in one forward pass).

## Side fix
Updated `smolvla_libero/config.json` to use local VLM path to avoid HF network dependency.
