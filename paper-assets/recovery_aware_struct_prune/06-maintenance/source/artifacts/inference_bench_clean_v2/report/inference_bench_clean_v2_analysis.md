# inference_bench_clean_v2 Results

## Setup
- Server: westd-29022 cuda:3 (isolated)
- 50 prompts from GSM8K test set, max_new_tokens=256
- 3 warmup passes before benchmark

## Results

| Model | Params | TPS | Speedup | First-token (ms) | Per-token (ms) | Total tokens |
|---|---|---|---|---|---|---|
| Dense (original) | 7.62B | 72.0 | 1.00x | 20.1 | 13.9 | 12,733 |
| CKA-only 20% | 6.16B | 58.3 | 0.81x | 16.4 | 16.7 | 7,610 |
| Standard 20% | 6.16B | 58.2 | 0.81x | 16.4 | 16.7 | 7,081 |

## Key Findings

1. **No speedup from pruning**: Both pruned models are 19% SLOWER in TPS despite 19% parameter reduction.
2. **Prefill is faster**: First-token latency drops 18% (20.1→16.4ms), confirming smaller model helps prefill.
3. **Per-token generation is slower**: 13.9→16.7ms (+20%), the non-uniform MLP intermediate_size [8128, 18944] causes irregular tensor shapes that hurt GPU utilization.
4. **CKA-only ≈ Standard in speed**: 58.28 vs 58.25 TPS, no meaningful difference.
5. **Pruned models generate fewer tokens**: 7.6K/7.1K vs 12.7K (pruned models hit EOS earlier on GSM8K).

## Implications for Paper
- Cannot claim inference speedup with naive HuggingFace inference on non-uniform pruned models.
- Structured pruning speedup requires uniform layer sizes or custom kernels (e.g., sparse GEMM).
- The parameter reduction (19%) and memory savings are real; latency improvement requires engineering.