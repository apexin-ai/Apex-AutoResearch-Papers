## Cross-Judge-Group Type Ranking Correlation

### 6 types (all)
GPT-5.4-judged rates: [56.00, 28.00, 37.33, 39.33, 35.67, 32.00] (Incompleteness, Auth. Scope, Cond. Prec., Lexical, Scopal, Coreferential)
GPT-4.1-judged rates: [50.00, 62.00, 36.00, 48.00, 45.00, 31.00]
Spearman ρ = 0.09, p = 0.87

### 5 types (excluding auth scope)
GPT-5.4-judged rates: [56.00, 37.33, 39.33, 35.67, 32.00] (Incompleteness, Cond. Prec., Lexical, Scopal, Coreferential)
GPT-4.1-judged rates: [50.00, 36.00, 48.00, 45.00, 31.00]
Spearman ρ = 0.90, p = 0.037

### Interpretation
Excluding authorization scope (the type with lowest inter-judge agreement, κ=0.385) dramatically improves cross-judge-group correlation from ρ=0.09 (p=0.87) to ρ=0.90 (p=0.037). The remaining 5 types show strong, statistically significant rank agreement across judge groups. This confirms that the near-zero full correlation is driven almost entirely by authorization scope, whose ambiguous judgments diverge most across judges, rather than reflecting a systematic judge-group bias.
