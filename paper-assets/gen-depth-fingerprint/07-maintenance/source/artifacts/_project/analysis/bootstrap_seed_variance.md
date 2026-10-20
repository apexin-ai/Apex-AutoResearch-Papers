# Bootstrap Seed Variance: 8-gen Binary LOGO

**Date:** 2026-05-17  
**Task:** 5-seed stability check for binary (gen-1 vs gen-2+) LOGO evaluation  
**Data:** features_8gen.csv, 29,095 rows (gen-0 excluded), 8 generators

## Summary

| Metric | Value |
|--------|-------|
| Mean binary F1 (5 seeds) | **0.7006** |
| Std across seeds | **0.0009** |
| Range | [0.6992, 0.7017] |

Cross-seed variance is negligible (std < 0.001). Results are highly stable.

## Per-Generator Results

| Generator | Mean F1 | Std | Min | Max |
|-----------|---------|-----|-----|-----|
| pythia-1b | 0.7899 | 0.0035 | 0.7848 | 0.7955 |
| qwen3-1.7b | 0.7549 | 0.0041 | 0.7479 | 0.7597 |
| qwen3-0.6b | 0.7512 | 0.0048 | 0.7453 | 0.7573 |
| pythia-2.8b | 0.7391 | 0.0028 | 0.7338 | 0.7414 |
| olmo-2-1b | 0.6923 | 0.0023 | 0.6898 | 0.6952 |
| llama-3.2-3b | 0.6863 | 0.0033 | 0.6834 | 0.6926 |
| qwen3-8b | 0.6506 | 0.0015 | 0.6480 | 0.6523 |
| mistral-7b-v0.3 | 0.5404 | 0.0043 | 0.5345 | 0.5476 |

## Key Observations

1. **Overall stability:** std=0.0009 across seeds confirms the LOGO evaluation is robust to random seed choice
2. **Per-generator stability:** all generators have std < 0.005, max std is qwen3-0.6b at 0.0048
3. **Performance ranking is invariant across seeds:** pythia-1b always best, mistral-7b-v0.3 always worst
4. **Implication for paper:** reporting single-seed F1 values is justified; seed variance is an order of magnitude smaller than inter-generator differences

## Configuration

- Seeds: [42, 123, 456, 789, 1024]
- Classifier: XGBClassifier(n_estimators=200, max_depth=6, lr=0.1, tree_method="hist")
- Evaluation: LOGO (leave-one-generator-out), class-balanced downsampling per fold
- Features: entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio
- Server results: `/root/gen-depth-fingerprint/results/bootstrap_seed_variance.json`
