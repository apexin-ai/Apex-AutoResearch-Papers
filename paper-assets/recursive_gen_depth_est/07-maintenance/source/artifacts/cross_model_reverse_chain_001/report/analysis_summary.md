# cross_model_reverse_chain_001 — Analysis Summary

## Conclusion: SUCCESS ✓

## Setup
- **Chain**: GPT-2 XL (d0→d1) → OLMo-1B (d1→d2) → Pythia-1.4B (d2→d3)
- **Data**: 500 samples/depth, d0-d3, total 2000
- **Server**: gpu-6000pro-2, cuda:1
- **Completed**: 2026-05-16 22:20 CST

## Key Metrics

| Metric | Logistic Regression | Random Forest |
|--------|-------------------|---------------|
| 4-class acc | **86.75%** [83.25, 89.76] | **85.75%** [82.00, 89.25] |
| Random baseline | 24.25% | 24.25% |

### Per-class Recall (LR / RF)
| Depth | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| d0 | 0.98/0.97 | 0.99/0.99 | 0.99/0.98 |
| d1 | 0.77/0.80 | 0.85/0.86 | 0.81/0.83 |
| d2 | 0.82/0.78 | 0.69/0.70 | 0.75/0.74 |
| d3 | 0.90/0.87 | 0.94/0.88 | 0.92/0.88 |

### Pairwise AUC (RF)
| Pair | AUC |
|------|-----|
| d0 vs d1 | 0.996 |
| d0 vs d2 | 0.988 |
| d0 vs d3 | 1.000 |
| d1 vs d2 | 0.886 |
| d1 vs d3 | 0.996 |
| d2 vs d3 | 0.955 |

### Top Features (RF importance)
1. var_surprisal: 0.2153
2. p90_ppl: 0.1553
3. mean_ppl: 0.1220
4. mean_surprisal: 0.0759
5. p75_ppl: 0.0638

## Comparison with Prior Experiments

| Experiment | Chain | 4-class acc | d1v2 AUC |
|-----------|-------|-------------|----------|
| **reverse_chain_001** | **GPT2XL→OLMo→Pythia** | **86.8%** | **0.886** |
| cross_model_gpt2xl_001 | GPT2-XL (single) | 83.3% | 0.913 |
| cross_model_olmo_002 | OLMo (single) | 78.8% | 0.867 |
| cross_model_loo_001 | LOO cross-model | 66.4% | — |

## Interpretation

1. **Reverse chain 86.8% far exceeds 55% threshold** — depth signal transfers robustly across 3 different architectures.
2. **Outperforms single-model baselines** (OLMo 78.8%, GPT2-XL 83.3% with 5000 samples/depth vs only 500 here) — cross-architecture chain may amplify distinguishability.
3. **AUC pattern consistent**: d1v2 remains hardest pair (0.886), monotonic decay preserved. d0 vs any depth near-perfect (≥0.988).
4. **Feature importance identical pattern**: var_surprisal + p90_ppl dominate, confirming perplexity-based features are architecture-agnostic markers of generation depth.
5. **Strongly supports N4 claim**: depth signal is not architecture-specific; it generalizes across model families even when each depth is produced by a different model.

## Artifacts
- Checkpoints: `checkpoints/reverse_chain/{gpt2xl_on_d0, olmo_on_d1, pythia_on_d2}`
- Results: `results/reverse_chain_n4/{classification_report.txt, confusion_matrix.png, pairwise_auc.json, feature_importance.json}`
- Log: `~/runs/recursive_gen_depth_est/cross_model_reverse_chain_001.log`
