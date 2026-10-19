# Plan 007: WikiText-2 PPL Validation Results
Llama-3.1-8B, 50% SwiGLU Sparsity

| Condition | Mode | WikiText-2 PPL |
|-----------|------|----------------|
| Dense | dense | 6.48 |
| KL-Distill | predictor | 9.65 |
| STE | predictor | 8.18 |
| SPON | spon | 9.41 |
| BCE | predictor | 28.37 |
| BCE+Comp | predictor_comp | 25.34 |
| TEAL | static_mask | 48715 |
| WINA | static_mask | 2126 |
| R-Sparse | static_mask | 151.20 |

## Key Finding
Learned contextual sparsity predictors (KL, STE, SPON) maintain near-dense quality (PPL 8-10 vs dense 6.48), while all static mask baselines degrade catastrophically at 50% SwiGLU sparsity (PPL 151-48715).

## Notes
- TEAL uses greedy per-layer allocation (not global top-k)
- WINA uses WINA-weighted greedy per-layer allocation
- R-Sparse uses global top-k magnitude masks
- C4 PPL and downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) pending dataset pre-caching
- Server results at /root/distill_sparse_swiglu/results/plan_007/consolidated/