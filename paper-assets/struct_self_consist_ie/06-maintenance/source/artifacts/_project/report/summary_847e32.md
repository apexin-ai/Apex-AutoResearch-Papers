# B2-v2: Multi-Domain Joint Training Entity Verifier

**Date**: 2026-05-20
**Total entities**: 86,246 across 9 configs (3 datasets x 3 seeds, all Qwen-7B FT)

## Setup

B2 original trained on CoNLL+SciERC (including 72B ZS/FS configs) and tested on FewNERD, achieving LGB AUC=0.8335. B2-v2 uses leave-one-dataset-out cross-validation with 9 Qwen-7B FT configs to evaluate cross-domain generalization symmetrically.

| Dataset | Configs | Instances | Entities | Pos Rate |
|---------|---------|-----------|----------|----------|
| CoNLL   | 3 seeds (N=16) | 8,268 | 27,965 | 58.8% |
| SciERC  | 3 seeds (N=16) | 1,587 | 9,572 | 44.1% |
| FewNERD | 3 seeds (N=8, cap=3000) | 9,000 | 48,709 | 49.9% |

## Leave-One-Dataset-Out Results

| Fold | Train | Test | LGB AUC | XGB AUC | LGB ECE | Greedy F1 | Best F1 | F1 Delta |
|------|-------|------|---------|---------|---------|-----------|---------|----------|
| 1 | SciERC+FewNERD | **CoNLL** | 0.9378 | 0.9391 | 0.0304 | 0.9121 | 0.9152 | +0.0031 |
| 2 | CoNLL+FewNERD | **SciERC** | 0.8006 | 0.7910 | 0.1274 | 0.6655 | 0.6709 | +0.0054 |
| 3 | CoNLL+SciERC | **FewNERD** | 0.8477 | 0.8603 | 0.1357 | 0.7937 | 0.7861 | **-0.0076** |
| 4 | ALL (5-fold CV) | random | 0.9313±0.0012 | 0.9325±0.0012 | 0.0072 | — | — | — |

## Comparison with B2 Original (Fold 3 = same train/test split direction)

| Metric | B2 Original | B2-v2 | Delta |
|--------|-------------|-------|-------|
| LGB AUC | 0.8335 | 0.8477 | **+0.0142** |
| XGB AUC | 0.8282 | 0.8603 | **+0.0321** |
| LGB ECE | — | 0.1357 | — |
| Greedy F1 | 0.7321 | 0.7937 | +0.0616 (different data) |

**Caveat**: B2 original included 72B ZS/FS configs (harder to classify); B2-v2 uses only 7B FT. The AUC improvement is partially confounded by more homogeneous training data. The greedy F1 difference (0.7321 vs 0.7937) reflects different FewNERD subsets and N values.

## Per-Config AUC (Fold 3, LGB)

| Config | AUC | Entities |
|--------|-----|----------|
| fewnerd_7b_s123 | 0.8415 | 15,936 |
| fewnerd_7b_s456 | 0.8503 | 16,360 |
| fewnerd_7b_s789 | 0.8510 | 16,413 |

## Feature Stability (Point-Biserial r with Correctness Label)

| Feature | CoNLL | SciERC | FewNERD | Cross-Domain Std | Interpretation |
|---------|-------|--------|---------|------------------|----------------|
| agreement_count | 0.857 | 0.560 | 0.688 | 0.122 | Most discriminative but unstable |
| vc | 0.855 | 0.552 | 0.682 | 0.124 | Same pattern as agreement |
| sj | 0.736 | 0.405 | 0.509 | 0.138 | Highest instability |
| sample_mean_lp | 0.467 | 0.248 | 0.422 | 0.094 | Moderate |
| lp_span | 0.311 | — | 0.337 | **0.013** | Very stable |
| lp_token | 0.276 | — | 0.248 | **0.014** | Very stable |
| entity_position | -0.011 | -0.030 | -0.005 | **0.011** | Stable but weak |
| entity_type_enc | 0.179 | -0.064 | 0.075 | 0.100 | Dataset-specific |
| entity_length | -0.012 | -0.087 | -0.175 | 0.067 | Direction consistent, magnitude varies |

## Feature Importance (XGB Gain, Fold 3)

| Feature | Gain | Note |
|---------|------|------|
| vc | 0.432 | Dominant |
| agreement_count | 0.367 | |
| **dataset_enc** | **0.094** | Model relies on dataset identity |
| entity_type_enc | 0.019 | |
| entity_length | 0.014 | |

## Key Findings

1. **Cross-domain gap persists but narrows**: Fold 3 AUC (0.848 LGB) > B2 original (0.834), but still far below IID upper bound (0.931). The gap is ~0.083 AUC points.

2. **AUC improvement does NOT translate to F1 improvement on FewNERD**: Despite +0.014 AUC, Fold 3 Path A F1 is -0.0076 below greedy. This is because:
   - High ECE (0.136) means predicted probabilities are miscalibrated cross-domain
   - The model overconfidently assigns high scores to CoNLL/SciERC-like patterns that don't hold on FewNERD

3. **SciERC is the hardest domain to generalize to**: Fold 2 AUC=0.80, ECE=0.13. However, Path A still gives +0.005 F1 delta, likely because SciERC's greedy baseline is weaker.

4. **Feature stability inversely correlates with discriminative power**: The most useful features (agreement_count, vc, sj with r=0.55-0.86) have the highest cross-domain std (0.12-0.14). The most stable features (lp_span, lp_token with std=0.01) are weakly discriminative (r=0.25-0.34).

5. **dataset_enc leakage**: In Fold 3, dataset_enc has 0.094 XGB gain — the model uses dataset identity as a feature, which is problematic for cross-domain generalization. A domain-invariant model should not rely on this.

## Implications for Paper

- Joint training with all 3 datasets does improve AUC on held-out domains, but the improvement is modest and does not solve the cross-domain calibration problem.
- For verifier-weighted construction to work cross-domain, the model needs either (a) domain-specific calibration, or (b) features that are both discriminative and stable — currently no single feature satisfies both.
- The lp_span/lp_token features are the best candidates for cross-domain transfer (stable + moderately discriminative), but they require token-level logprobs which not all configs have.
