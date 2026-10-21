# Plan 006: Training-Free Baseline Re-Evaluation

## Root Cause
`_global_topk_masks` performed raw global top-K on activation scores without per-layer
normalization. Activation magnitudes vary 50-100x across layers (Layer 0 mean=0.0027,
Layer 31 mean=0.178), causing early layers to be pruned to near-zero while late layers
keep everything.

## Fix Applied
1. **`_global_topk_masks` (evaluate.py:133)**: Added per-layer mean normalization before
   global top-K. Each layer's scores are divided by their mean, making cross-layer
   comparison fair.
2. **`teal_activation_magnitude_masks` (evaluate.py:173)**: Added `dense_mse` normalization
   to the per-layer error curves, dividing reconstruction MSE by the dense output MSE.
3. **`_layer_error_curve` (baselines.py:44)**: Same `dense_mse` normalization fix.

## Results at 50% Sparsity (LLaMA 3.1 8B, WikiText-2, 141 eval samples)

| Method | Before Fix | After Fix | Status |
|--------|-----------|-----------|--------|
| Dense | 6.12 | 6.12 | Reference |
| Uniform 50% | — | 23.90 | Sanity check |
| Vanilla TEAL (global) | 58,032 | **23.31** | FIXED |
| WINA (global) | 82,567 | **27.93** | FIXED |
| TEAL Greedy (baselines.py) | — | **33.47** | FIXED |
| TEAL Greedy (evaluate.py) | 50,035 | 164.76 | Partial fix — Layer 1 still over-pruned |
| R-Sparse (global) | 74,929 | 151.20 | Mean norm insufficient for SVD-weighted scores |
| WINA Greedy | — | 2,126 | Inverted allocation — separate bug |

## Remaining Issues

### R-Sparse (PPL 151.2)
SVD-weighted scores have much higher cross-layer variance than activation-only scores.
Per-layer mean normalization is insufficient because the score distribution shape varies.
Needs percentile-based or max normalization.

### TEAL Greedy evaluate.py (PPL 164.8)
Layer 1 gets fully pruned (keep_ratio=0.000). The baselines.py version (PPL 33.47)
handles this better. Recommend using baselines.py version.

### WINA Greedy (PPL 2126)
Inverted allocation: early layers at 90% keep, late layers at 0% keep. The WINA-weighted
reconstruction error grows with layer depth, so greedy over-prunes late layers.

## Validated Methods (Ready for Use)
- **Vanilla TEAL (global, normalized)**: 23.31
- **WINA (global, normalized)**: 27.93
- **TEAL Greedy (baselines.py)**: 33.47