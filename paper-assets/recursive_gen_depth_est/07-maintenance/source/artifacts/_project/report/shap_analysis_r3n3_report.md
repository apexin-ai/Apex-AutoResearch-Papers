## SHAP TreeExplainer 9-Cell Analysis (R3-N3)

### Three-Way Concordance (SHAP vs Gini vs Permutation)
- Kendall's W: mean=0.8955, range=[0.8503, 0.9314]
- Spearman ρ(SHAP, Gini): mean=0.9312
- Spearman ρ(SHAP, Perm): mean=0.8392

### Cross-Cell SHAP Consistency
- Mean ρ=0.8047, range=[0.6263, 0.9439]

### Top-2 Feature Stability (SHAP)
- p90_ppl in top-2: 9/9 (100%)
- var_surprisal in top-2: 8/9 (89%)

### Aggregated SHAP Ranking
1. p90_ppl (0.0894)
2. var_surprisal (0.0803)
3. p75_ppl (0.0426)
4. mean_surprisal (0.0287)
5. mean_ppl (0.0262)

### Category Contribution
- PPL/surprisal features: 88.8%
- Lexical diversity features: 11.2%

### Output Files (results/shap_analysis/)
- concordance_summary.json
- three_way_comparison.json
- beeswarm_{pythia,gpt2xl,olmo}_nucleus095.png
- cross_cell_shap_consistency.png
- shap_importance*.json, shap_summary.txt, bar plots, heatmap
