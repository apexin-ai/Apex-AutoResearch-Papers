# B2-v4: Inverse-Frequency Weighted Entity Verifier

**Date**: 2026-05-20 20:02
**Total entities**: 86246 across 9 configs
**IFW formula**: `feature / log(1 + freq * 1000)` where freq = type_proportion in train

## Variant A: Replace (ac/vc/sj → IFW versions, 13 features)

| Fold | Train | Test | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Greedy F1 | Best F1 | Δ Greedy |
|------|-------|------|---------|---------|---------|---------|-----------|---------|----------|
| 1 | scierc+fewnerd | conll | 0.8243 | 0.8181 | 0.3184 | 0.3220 | 0.9121 | 0.8924 | -0.0197 |
| 2 | conll+fewnerd | scierc | 0.7623 | 0.7530 | 0.1294 | 0.1341 | 0.6655 | 0.6647 | -0.0008 |
| 3 | conll+scierc | fewnerd | 0.8224 | 0.8340 | 0.1964 | 0.2188 | 0.7937 | 0.7810 | -0.0127 |
| 4 | ALL | CV | 0.9326±0.0011 | 0.9313±0.0012 | 0.0089 | 0.0091 | - | - | - |

## Variant B: Augment (original + IFW, 16 features)

| Fold | Train | Test | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Greedy F1 | Best F1 | Δ Greedy |
|------|-------|------|---------|---------|---------|---------|-----------|---------|----------|
| 1 | scierc+fewnerd | conll | 0.9359 | 0.9413 | 0.1047 | 0.1065 | 0.9121 | 0.9151 | +0.0030 |
| 2 | conll+fewnerd | scierc | 0.7857 | 0.7907 | 0.1307 | 0.1192 | 0.6655 | 0.6722 | +0.0067 |
| 3 | conll+scierc | fewnerd | 0.8554 | 0.8541 | 0.1979 | 0.1934 | 0.7937 | 0.7852 | -0.0085 |
| 4 | ALL | CV | 0.9329±0.0016 | 0.9312±0.0014 | 0.0083 | 0.0073 | - | - | - |

## Comparison: Fold 3 (FewNERD, critical cross-domain fold)

| Version | Features | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Best F1 Δ |
|---------|----------|---------|---------|---------|---------|-----------|
| B2 orig | 13 | 0.8282 | 0.8335 | - | - | - |
| B2-v2 | 13 | 0.8603 | 0.8477 | 0.1556 | 0.1357 | - |
| B2-v3 | 9 (invariant) | 0.8518 | 0.8562 | 0.1643 | 0.1373 | - |
| **B2-v4 replace** | 13 (IFW) | 0.8224 | 0.8340 | 0.1964 | 0.2188 | -0.0127 |
| **B2-v4 augment** | 16 (orig+IFW) | 0.8554 | 0.8541 | 0.1979 | 0.1934 | -0.0085 |

## Feature Importance (XGB Gain, Fold 3)


### Replace

| Feature | XGB Gain | LGB Splits |
|---------|----------|------------|
| vc_ifw | 0.3111 | 369 |
| ac_ifw | 0.2867 | 643 |
| dataset_enc | 0.2748 | 91 |
| entity_type_enc | 0.0211 | 437 |
| entity_length | 0.0170 | 211 |
| entity_char_length | 0.0169 | 796 |
| entity_position | 0.0164 | 888 |
| sj_ifw | 0.0149 | 654 |
| sample_mean_lp | 0.0149 | 811 |
| lp_token | 0.0133 | 383 |
| lp_span | 0.0129 | 442 |
| model_size_log | 0.0000 | 0 |
| regime_enc | 0.0000 | 0 |

### Augment

| Feature | XGB Gain | LGB Splits |
|---------|----------|------------|
| vc | 0.4485 | 101 |
| agreement_count | 0.3409 | 180 |
| dataset_enc | 0.0715 | 76 |
| ac_ifw | 0.0567 | 424 |
| vc_ifw | 0.0123 | 232 |
| entity_type_enc | 0.0105 | 451 |
| entity_position | 0.0082 | 886 |
| entity_char_length | 0.0081 | 797 |
| entity_length | 0.0081 | 216 |
| sample_mean_lp | 0.0076 | 775 |
| sj_ifw | 0.0073 | 456 |
| sj | 0.0070 | 472 |
| lp_span | 0.0068 | 378 |
| lp_token | 0.0064 | 384 |
| model_size_log | 0.0000 | 0 |
| regime_enc | 0.0000 | 0 |

## IFW Feature Stability

| Feature | CoNLL | SciERC | FewNERD | Cross-Domain Std |
|---------|-------|--------|---------|------------------|
| agreement_count | 0.8570 | 0.5597 | 0.6881 | 0.1217 |
| vc | 0.8550 | 0.5518 | 0.6823 | 0.1242 |
| sj | 0.7360 | 0.4047 | 0.5089 | 0.1383 |
| ac_ifw | 0.7882 | 0.5217 | 0.6247 | 0.1097 |
| vc_ifw | 0.7863 | 0.5149 | 0.6196 | 0.1118 |
| sj_ifw | 0.1587 | 0.1937 | 0.3073 | 0.0634 |
| lp_token | 0.2757 | nan | 0.2484 | 0.0136 |
| lp_span | 0.3112 | nan | 0.3365 | 0.0127 |
| sample_mean_lp | 0.4670 | 0.2479 | 0.4216 | 0.0944 |

**Elapsed**: 48.7s

