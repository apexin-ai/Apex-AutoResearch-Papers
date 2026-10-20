## OLMo-1B C4 selfbleu ablation

Data: `data/exp_olmo1b_c4_rerun/features.csv` (30000 samples, depth 0-5, Qwen-1.5B scorer)
Method: GroupKFold(5) OOF LightGBM + doc-level bootstrap(10000), θ=0.60, seed=42

- Full 15D: 0v1 AUC=0.9860, 1v2 AUC=0.5074, 2v3 AUC=0.4972, 3v4 AUC=0.5020, 4v5 AUC=0.4943, K*=1
- No self_bleu 14D: 0v1 AUC=0.9831, 1v2 AUC=0.5047, 2v3 AUC=0.4959, 3v4 AUC=0.5054, 4v5 AUC=0.4892, K*=1
- ΔK* = 0
- Conclusion: removing self_bleu does not change K*

### Per-pair detail (with 95% bootstrap CI)

| Pair | AUC_15D | CI_15D | AUC_14D | CI_14D | Δ |
|------|---------|--------|---------|--------|---|
| 0v1 | 0.9860 | [0.9843, 0.9877] | 0.9831 | [0.9811, 0.9850] | -0.0030 |
| 1v2 | 0.5074 | [0.4961, 0.5186] | 0.5047 | [0.4932, 0.5162] | -0.0026 |
| 2v3 | 0.4972 | [0.4859, 0.5087] | 0.4959 | [0.4847, 0.5072] | -0.0013 |
| 3v4 | 0.5020 | [0.4908, 0.5132] | 0.5054 | [0.4941, 0.5168] | +0.0034 |
| 4v5 | 0.4943 | [0.4828, 0.5058] | 0.4892 | [0.4781, 0.5005] | -0.0051 |
