Worker D: Value distribution vs returns analysis

008d (collapsed) vs 008a (healthy):
- Correlation: -0.20 vs 0.54 (KEY metric)
- V(s) mean: 162.30 vs 263.99
- G_t mean: 68.37 vs 156.24
- Bias mean: 93.93 vs 107.75
- Overest. rate: 92.7% vs 82.8%
- V/G ratio: 7.36 vs 5.18

Key insight: correlation (not bias magnitude) distinguishes CIVO pathology.
008d critic predictions are NEGATIVELY correlated with actual returns — delusional critic.

Charts: artifacts/value_vs_returns.pdf/.png (local)
Data: artifacts/value_vs_returns.json
Script: scripts/plot_value_vs_returns.py