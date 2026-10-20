# exp-003 Config 1-3 Deep Analysis

## Config 1 (Greedy) vs Config 2 (Nuc09) Pairwise AUC

| Depth-Pair | Greedy | Nuc09 | Δ |
|:---:|:---:|:---:|:---:|
| 0v1 | 0.9797 | **0.9946** | +0.0149 |
| 1v2 | **0.6893** | 0.6866 | −0.0027 |
| 2v3 | 0.5613 | **0.5917** | +0.0304 |
| 3v4 | 0.5404 | **0.5466** | +0.0062 |
| 4v5 | **0.5139** | 0.5068 | −0.0071 |

## Feature Ranking Spearman ρ (single-feature AUC, 1v2)

| 对比 | ρ | p-value |
|:---|:---:|:---:|
| Greedy vs Nuc09 | 0.600 | 0.018 |
| Greedy vs T07 | 0.914 | 2e-6 |
| Nuc09 vs T07 | 0.782 | 0.00057 |

## Top-3 Features (1v2)

| Config | #1 | #2 | #3 |
|:---|:---|:---|:---|
| Greedy | self_bleu (0.5961) | hapax_ratio (0.5752) | ttr (0.5462) |
| Nuc09 | hapax_ratio (0.6561) | ttr (0.6043) | surp_skew (0.5997) |
| T07 | hapax_ratio (0.6365) | ttr (0.5867) | low_freq_ratio (0.5805) |

## Cross-Experiment 1v2 AUC Ranking (all 7 configs)

| Rank | Config | 1v2 AUC |
|:---:|:---|:---:|
| 1 | MVP-Qwen-Rewrite | 0.6957 |
| 2 | Config1-Greedy | 0.6893 |
| 3 | Config3-T07 | 0.6887 |
| 4 | Config2-Nuc09 | 0.6866 |
| 5 | Exp001-Pythia-Cont | 0.6539 |
| 6 | Exp002-OLMo-Cont | 0.6146 |
| 7 | Exp017-Qwen-Cont | 0.6114 |

**D016 Universality (θ=0.60): CONFIRMED — all 7 configs > 0.60**

## θ-Sensitivity Table

| Config | θ=0.55 | θ=0.60 | θ=0.65 | θ=0.70 |
|:---|:---:|:---:|:---:|:---:|
| Greedy | K*=3 | K*=2 | K*=2 | K*=1 |
| Nuc09 | K*=3 | K*=2 | K*=2 | K*=1 |
| T07 | K*=3 | K*=2 | K*=2 | K*=1 |
