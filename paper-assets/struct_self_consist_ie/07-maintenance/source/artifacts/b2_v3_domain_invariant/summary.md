# B2-v3: Domain-Invariant Features Only Entity Verifier

**Date**: 2026-05-20 19:52
**Features** (9): agreement_count, vc, lp_token, lp_span, sample_mean_lp, sj, entity_length, entity_char_length, entity_position
**Removed**: entity_type_enc, model_size_log, dataset_enc, regime_enc
**Total entities**: 86246 across 9 configs

## Leave-One-Dataset-Out Results

| Fold | Train | Test | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Greedy F1 | Best F1 | Δ Greedy |
|------|-------|------|---------|---------|---------|---------|-----------|---------|----------|
| 1 | scierc+fewnerd | conll | 0.9386 | 0.9368 | 0.0234 | 0.0197 | 0.9121 | 0.9151 | +0.0030 |
| 2 | conll+fewnerd | scierc | 0.8163 | 0.8152 | 0.1521 | 0.1439 | 0.6655 | 0.6745 | +0.0090 |
| 3 | conll+scierc | fewnerd | 0.8518 | 0.8562 | 0.1643 | 0.1373 | 0.7937 | 0.7835 | -0.0102 |

## Comparison: v3 vs v2 vs Original (Fold 3: FewNERD)

| Version | Features | XGB AUC | LGB AUC | XGB ECE | LGB ECE |
|---------|----------|---------|---------|---------|---------|
| B2 orig | 13 (all) | 0.8282 | 0.8335 | - | - |
| B2-v2   | 13 (all) | 0.8603 | 0.8477 | 0.1556 | 0.1357 |
| **B2-v3** | **9 (invariant)** | **0.8518** | **0.8562** | **0.1643** | **0.1373** |

### AUC Delta (v3 - v2)

| Fold | XGB Δ | LGB Δ | ECE XGB Δ | ECE LGB Δ |
|------|-------|-------|-----------|-----------|
| conll | -0.0005 | -0.0010 | -0.0070 | -0.0107 |
| scierc | +0.0253 | +0.0146 | +0.0071 | +0.0165 |
| fewnerd | -0.0085 | +0.0085 | +0.0087 | +0.0016 |

## Feature Importance (XGB Gain, avg across folds)

| Feature | Avg Gain | Rank |
|---------|----------|------|
| agreement_count | 0.5843 | 1 |
| vc | 0.3029 | 2 |
| lp_span | 0.0207 | 3 |
| sample_mean_lp | 0.0201 | 4 |
| lp_token | 0.0146 | 5 |
| entity_position | 0.0145 | 6 |
| entity_length | 0.0144 | 7 |
| sj | 0.0143 | 8 |
| entity_char_length | 0.0142 | 9 |

## Feature Stability (Point-Biserial Correlation)

| Feature | CoNLL | SciERC | FewNERD | Cross-Domain Std |
|---------|-------|--------|---------|------------------|
| agreement_count | 0.8570 | 0.5597 | 0.6881 | 0.1217 |
| vc | 0.8550 | 0.5518 | 0.6823 | 0.1242 |
| lp_token | 0.2757 | nan | 0.2484 | 0.0136 |
| lp_span | 0.3112 | nan | 0.3365 | 0.0127 |
| sample_mean_lp | 0.4670 | 0.2479 | 0.4216 | 0.0944 |
| sj | 0.7360 | 0.4047 | 0.5089 | 0.1383 |
| entity_length | -0.0123 | -0.0870 | -0.1749 | 0.0665 |
| entity_char_length | 0.0351 | -0.0528 | -0.1560 | 0.0781 |
| entity_position | -0.0110 | -0.0302 | -0.0047 | 0.0108 |

## Key Findings

1. **Cross-domain generalization**: Does removing domain features improve transfer?
   - YES: Fold 3 LGB AUC improved by +0.0085
2. **Calibration**: ECE changes — +0.0016 (LGB), +0.0087 (XGB)
3. **Top features without domain info**: agreement_count, vc, lp_span
