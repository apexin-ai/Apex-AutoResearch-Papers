# N2 RoBERTa Feature Overlap Analysis

## Probing R²
| Feature | RoBERTa R² | DeBERTa R² | RF Rank |
|---------|-----------|-----------|---------|
| bigram_entropy | 0.829 | 0.807 | 17 |
| rep_2gram | 0.819 | 0.815 | 14 |
| mean_surprisal | 0.818 | 0.814 | 11 |
| type_token_ratio | 0.811 | 0.853 | 18 |
| trigram_entropy | 0.789 | 0.783 | 9 |
| var_ppl | -4215.8 | -28.1 | 5 |
| mean_ppl | -9.50 | -4.18 | 7 |

## Cross-Architecture Consistency
| Metric | RoBERTa | DeBERTa |
|--------|---------|---------|
| Spearman ρ | -0.456 (p=0.050) | -0.484 (p=0.036) |
| Top-5 overlap | 0/10 | 0/10 |
| Top-10 Jaccard | 0.111 | 0.111 |

## Conclusion
Systematic representation bias confirmed across architectures. Transformers encode surface text features; RF relies on perplexity distribution statistics. The gap is structural, not model-specific.