MMCT v1 results summary. Full data on westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/

Files:
- mmct_results.json (332KB) — full results
- null_distribution.json — null distribution + per-method FPR profiles
- mmct_report.md — per-condition tables
- fpr_fnr_comparison.md — 4-way tradeoff comparison

Key Results:
| Mode | FPR (α=0.00) | Det. α=0.25 | Det. α=0.50 | Det. α=0.75 |
|------|-------------|-------------|-------------|-------------|
| uniform_forward | 0.000 | 0.000 | 0.000 | 0.333 |
| uniform_bidirectional | 0.000 | 0.000 | 0.000 | 0.333 |
| weighted_forward | 0.000 | 0.438 | 0.542 | 0.875 |
| weighted_bidirectional | 0.000 | 0.125 | 0.167 | 0.375 |

Note: α=1.0 data not found in results/alpha_sweep/ — needs follow-up with correct paths.