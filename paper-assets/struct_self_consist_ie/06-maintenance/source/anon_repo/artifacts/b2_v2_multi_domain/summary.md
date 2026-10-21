# B2-v2: Multi-Domain Joint Training Entity Verifier

**Date**: 2026-05-20 19:46
**Total entities**: 86246 across 9 configs

## Leave-One-Dataset-Out Results

| Fold | Train | Test | LGB AUC | XGB AUC | LGB ECE | Greedy F1 | Best PathA F1 | Δ vs Greedy |
|------|-------|------|---------|---------|---------|-----------|---------------|-------------|
| 1 | scierc+fewnerd | conll | 0.9378 | 0.9391 | 0.0304 | 0.9121 | 0.9121 | +0.0000 |
| 2 | conll+fewnerd | scierc | 0.8006 | 0.7910 | 0.1274 | 0.6655 | 0.6709 | +0.0054 |
| 3 | conll+scierc | fewnerd | 0.8477 | 0.8603 | 0.1357 | 0.7937 | 0.7861 | -0.0076 |
| 4 | ALL | random CV | 0.9313±0.0012 | 0.9325±0.0012 | 0.0072 | - | - | - |

## Comparison with B2 Original (Fold 3)

| Metric | B2 Original | B2-v2 | Δ |
|--------|-------------|-------|---|
| LGB AUC | 0.8335 | 0.8477 | +0.0142 |
| XGB AUC | 0.8282 | 0.8603 | +0.0321 |

## Feature Stability (Point-Biserial Correlation with Label)

| Feature | CoNLL | SciERC | FewNERD | Cross-Domain Std |
|---------|-------|--------|---------|------------------|
| agreement_count | 0.8570 | 0.5597 | 0.6881 | 0.1217 |
| vc | 0.8550 | 0.5518 | 0.6823 | 0.1242 |
| lp_token | 0.2757 | nan | 0.2484 | 0.0136 |
| lp_span | 0.3112 | nan | 0.3365 | 0.0127 |
| sample_mean_lp | 0.4670 | 0.2479 | 0.4216 | 0.0944 |
| sj | 0.7360 | 0.4047 | 0.5089 | 0.1383 |
| entity_type_enc | 0.1785 | -0.0643 | 0.0753 | 0.0995 |
| entity_length | -0.0123 | -0.0870 | -0.1749 | 0.0665 |
| entity_char_length | 0.0351 | -0.0528 | -0.1560 | 0.0781 |
| entity_position | -0.0110 | -0.0302 | -0.0047 | 0.0108 |
| model_size_log | nan | nan | nan | nan |
| dataset_enc | nan | nan | nan | nan |
| regime_enc | nan | nan | nan | nan |

## Key Findings

1. **Cross-domain gap**: Fold 3 (train CoNLL+SciERC → test FewNERD) vs B2 original
   - B2-v2 LGB AUC: 0.8477 vs B2 orig: 0.8335
2. **Joint training upper bound**: Fold 4 (all-data CV) gives the IID performance ceiling
   - LGB AUC: 0.9313±0.0012
3. **Feature stability**: Features with low cross-domain std are most transferable
