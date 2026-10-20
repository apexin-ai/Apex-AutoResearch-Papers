# exp-015 Neural Probe: OLMo Rerun Results

## Setup
- **Model**: OLMo-1B-hf (frozen, last hidden state avg-pool → 2048-dim)
- **Classifier**: MLP (2048→512→256→6), 5-fold GroupKFold CV
- **Data**: `data/exp_olmo1b_c4_rerun/` (5000 samples × 6 depths = 30,000)
- **Device**: RTX 4090 D (cuda:2), embed_batch_size=8
- **Peak VRAM**: 3450 MB (embedding), 107 MB (MLP training)
- **Runtime**: ~4 min total (3.25 min embedding + 0.5 min MLP + 0.5 min bootstrap/permutation)

## Results: Adjacent Pairwise AUC

| Pair | Neural Probe AUC | 95% CI | p-value | LightGBM AUC (rerun) |
|------|----------------:|--------|---------|---------------------:|
| 0v1  | **0.9773** | [0.9747, 0.9795] | <0.002 | 0.986 |
| 1v2  | 0.5054 | [0.4954, 0.5148] | 0.176 | 0.508 |
| 2v3  | 0.5056 | [0.4966, 0.5157] | 0.142 | 0.497 |
| 3v4  | 0.5032 | [0.4941, 0.5133] | 0.262 | 0.502 |
| 4v5  | 0.4999 | [0.4913, 0.5073] | 0.514 | 0.494 |

- **K\* (neural probe) = 1** (threshold=0.60)
- **K\* (LightGBM rerun) = 1**
- Classification accuracy: 0.3087 (near 1/6 = 0.167 random baseline for the binary 0-vs-rest)

## Per-Fold Stability

| Pair | Mean±Std | Folds |
|------|----------|-------|
| 0v1 | 0.9777±0.003 | [0.983, 0.978, 0.975, 0.974, 0.978] |
| 1v2 | 0.505±0.011 | [0.521, 0.492, 0.513, 0.498, 0.500] |
| 2v3 | 0.505±0.008 | [0.513, 0.501, 0.516, 0.502, 0.494] |
| 3v4 | 0.505±0.007 | [0.518, 0.505, 0.495, 0.501, 0.504] |
| 4v5 | 0.499±0.010 | [0.498, 0.506, 0.479, 0.506, 0.504] |

## Key Finding

**K\*=1 is model-intrinsic, not a feature limitation.**

The 2048-dim OLMo hidden states (via MLP probe) yield identical K\*=1 as the 15D hand-crafted features (via LightGBM). For all depth pairs ≥1v2, the neural probe AUC is indistinguishable from random chance (0.50), with all 95% CIs straddling 0.50 and all permutation test p-values far above 0.05.

This means OLMo-1B's greedy-decoded iterative generations reach a fixed point after depth 1: the model's internal representations contain no signal to distinguish gen-1 from gen-2+ text. The K\*=1 boundary is a property of the data/model pair, not an artifact of feature engineering.

## Comparison with Other Models

For reference, the original exp-015 (Qwen2.5-1.5B-Instruct) found K\*=2 with neural probe, consistent with K\*=2 from LightGBM on Qwen data. This model-specific difference in K\* is itself an interesting finding: Qwen maintains distinguishable generational structure one depth further than OLMo before convergence.

## Output Location
- Server: `results/exp015_olmo_rerun/neural_probe_results.json`
