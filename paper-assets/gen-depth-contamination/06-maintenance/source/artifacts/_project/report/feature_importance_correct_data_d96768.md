# Feature Importance (Corrected Data Sources)

## Data Sources

| Model | Data Path | Rows | 1v2 Raw AUC |
|-------|-----------|------|-------------|
| OLMo-1B | `data/exp_olmo1b_c4_rerun/features.csv` | 30000 | 0.508 |
| Pythia-1.4B | `data_exp020_pythia_nuc09/features.csv` | 30000 | 0.678 |
| Qwen-1.5B (cont) | `data_exp022_cross_scorer/qwen_cont256__qwen_base/features.csv` | 30000 | 0.617 |

**Changes from old batch script:**
- OLMo: `olmo_c4_qwen_scorer` → `exp_olmo1b_c4_rerun` (self-scored rerun)
- Pythia: `pythia_c4_qwen_scorer` → `data_exp020_pythia_nuc09` (nucleus p=0.9 self-scored)
- Qwen-cont: same `qwen_cont256__qwen_base` (exp_017 features.csv not on disk)
- Qwen-base: dropped (only 3 models now)

**Note:** exp_017 (Qwen-cont self-scored) features.csv does not exist on disk (confirmed by `run_bootstrap_10k.py` note). Used `qwen_cont256__qwen_base` (raw AUC 0.617 ≈ target 0.611).

## Method

- Permutation importance via `sklearn.inspection.permutation_importance`
- LightGBM classifier, GroupKFold 5-fold, 10 repeats, seed=42
- θ=0.60, n_estimators=200, max_depth=6, lr=0.05
- 15D features: surp_{mean,std,skew,kurt}, surp_d1_{mean,std,skew}, surp_d2_{mean,std}, ttr, hapax_ratio, self_bleu, freq_{kurtosis,entropy}, low_freq_ratio

## Results: 1v2 Permutation Importance (ΔAUC)

| Feature | OLMo-1B | Pythia-1.4B | Qwen-1.5B (cont) |
|---------|---------|-------------|-------------------|
| **Surprisal σ** | -0.0004 (#11) | **+0.1018 (#1)** | **+0.0653 (#1)** |
| **Freq Entropy** | +0.0022 (#7) | **+0.0426 (#2)** | **+0.0369 (#2)** |
| Surprisal μ | +0.0004 (#9) | +0.0242 (#3) | +0.0357 (#3) |
| Hapax Ratio | +0.0037 (#4) | +0.0161 (#4) | +0.0267 (#4) |
| Surprisal Kurt | +0.0009 (#8) | +0.0012 (#11) | +0.0134 (#5) |
| TTR | -0.0017 (#15) | +0.0044 (#7) | +0.0081 (#6) |
| Δ¹ Surp μ | -0.0013 (#14) | +0.0035 (#8) | +0.0063 (#7) |
| Δ² Surp μ | -0.0010 (#12) | +0.0031 (#9) | +0.0053 (#8) |
| Surprisal Skew | +0.0024 (#6) | +0.0003 (#14) | +0.0042 (#9) |
| Δ¹ Surp σ | +0.0066 (#1) | +0.0098 (#5) | +0.0027 (#10) |
| Low-Freq Ratio | +0.0033 (#5) | +0.0063 (#6) | +0.0024 (#11) |
| Freq Kurt | -0.0000 (#10) | +0.0013 (#10) | +0.0010 (#12) |
| Self-BLEU | -0.0011 (#13) | +0.0011 (#12) | +0.0006 (#13) |
| Δ² Surp σ | +0.0046 (#3) | +0.0008 (#13) | -0.0006 (#14) |
| Δ¹ Surp Skew | +0.0048 (#2) | -0.0010 (#15) | -0.0013 (#15) |

## Results: 0v1 Permutation Importance (ΔAUC)

| Feature | OLMo-1B | Pythia-1.4B | Qwen-1.5B (cont) |
|---------|---------|-------------|-------------------|
| **Δ¹ Surp σ** | **+0.1595 (#1)** | **+0.2332 (#1)** | **+0.1618 (#1)** |
| Freq Entropy | +0.0037 (#7) | +0.0087 (#3) | +0.0294 (#2) |
| Surprisal Kurt | +0.0187 (#2) | +0.0021 (#5) | +0.0039 (#6) |
| Surprisal Skew | +0.0148 (#3) | +0.0017 (#6) | +0.0006 (#9) |
| Surprisal σ | +0.0029 (#9) | +0.0194 (#2) | +0.0171 (#3) |
| Self-BLEU | +0.0113 (#4) | +0.0007 (#9) | +0.0009 (#8) |
| Surprisal μ | +0.0067 (#5) | +0.0029 (#4) | +0.0066 (#4) |
| TTR | +0.0037 (#8) | +0.0013 (#7) | +0.0064 (#5) |

(0v1 truncated to top features; all models show raw AUC > 0.98, indicating strong 0v1 separability across all models)

## Key Findings

1. **OLMo K*=1 confirmed**: No feature contributes meaningfully on 1v2 (max ΔAUC = 0.007, all within noise). The classifier barely outperforms random (raw AUC = 0.508).

2. **Pythia/Qwen K*=2 key features**: Surprisal σ (#1) and Freq Entropy (#2) are the dominant features for both models on 1v2. Surprisal σ alone accounts for ΔAUC > 0.065 in both cases.

3. **Cross-model consistency**: The top-4 features for 1v2 are identical in Pythia and Qwen-cont: Surprisal σ → Freq Entropy → Surprisal μ → Hapax Ratio.

4. **0v1 universally strong**: All models show Δ¹ Surp σ as the dominant feature for 0v1 (ΔAUC > 0.16), confirming that the human-vs-generated boundary is always detectable.

5. **Derivative features shift roles**: Δ¹ Surp σ dominates 0v1 but drops in importance for 1v2 (especially for Qwen-cont where it falls to #10). The 1v2 boundary is characterized by base surprisal statistics rather than derivative features.

## Comparison with Previous (Incorrect) Analysis

Previous batch script used cross-scored data for OLMo and Pythia (`olmo_c4_qwen_scorer`, `pythia_c4_qwen_scorer`), which inflated the scorer-dependent signal. The corrected analysis uses self-scored data, giving lower 1v2 AUC but more representative feature importance rankings.

The core finding is preserved: Surprisal σ and Freq Entropy remain the top-2 features for K*≥2 models. OLMo remains at K*=1 with no significant 1v2 features.

## Artifacts

- Server JSON: `results/feature_importance_correct/{olmo,pythia,qwen_cont}/importance_results.json`
- Combined JSON: `results/feature_importance_correct/all_models_importance.json`
- Script: `scripts/feature_importance_correct.py`
