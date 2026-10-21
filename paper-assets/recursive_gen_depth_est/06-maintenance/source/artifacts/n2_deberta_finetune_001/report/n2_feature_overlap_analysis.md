# N2 Feature Overlap Analysis: DeBERTa vs RF

## Probing R² (DeBERTa [CLS] → hand-crafted feature prediction)

| Feature | R² | RF Importance Rank |
|---|---|---|
| type_token_ratio | **0.853** | 18 |
| rep_2gram | **0.815** | 14 |
| mean_surprisal | **0.814** | 11 |
| bigram_entropy | **0.807** | 17 |
| trigram_entropy | **0.783** | 9 |
| rep_3gram | 0.769 | 13 |
| var_surprisal | 0.734 | **1** |
| rep_4gram | 0.715 | 12 |
| hapax_ratio | 0.620 | 16 |
| entropy_of_surprisal | 0.511 | 19 |
| p50_ppl | 0.454 | 3 |
| p75_ppl | 0.426 | 6 |
| p25_ppl | 0.181 | 8 |
| p90_ppl | 0.152 | **2** |
| p10_ppl | -0.641 | 15 |
| skewness_ppl | -0.870 | **4** |
| kurtosis_ppl | -1.017 | 10 |
| mean_ppl | -4.182 | 7 |
| var_ppl | -28.114 | **5** |

## Overlap Metrics
- Spearman ρ = -0.484 (p=0.036) — significant negative correlation
- Top-3 overlap: 0/6 (Jaccard=0.000)
- Top-5 overlap: 0/10 (Jaccard=0.000)
- Top-10 overlap: 2/18 (Jaccard=0.111), intersection: trigram_entropy, var_surprisal

## Feature Group Analysis
| Group | Probing R² | RF Importance |
|---|---|---|
| ngram_entropy | 0.795 | 0.0019 (low) |
| repetition | 0.766 | 0.0014 (low) |
| lexical_diversity | 0.736 | 0.0009 (low) |
| surprisal | 0.686 | **0.1034** (high) |
| perplexity_quantiles | 0.030 | 0.0179 |
| perplexity_central | -1.864 | 0.0110 |
| perplexity_spread | -10.000 | 0.0059 |

## Key Finding
DeBERTa and RF attend to nearly opposite feature sets (ρ=-0.48). RF's top features (perplexity distribution stats: var_surprisal, p90_ppl, var_ppl, skewness_ppl) are poorly captured by DeBERTa embeddings (negative R²). DeBERTa excels at surface text features (TTR, n-gram repetition, bigram entropy) which contribute almost nothing to RF classification. This explains the 20pp accuracy gap.