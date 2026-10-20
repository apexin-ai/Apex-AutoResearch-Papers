MMCT v3 Results — westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/

Files: mmct_results.json (838KB), null_distribution.json, mmct_report.md, fpr_fnr_comparison.md, mmct_table7.md

Bug Fix: bidirectional reverse p-value now uses correct reverse null distribution.
New: weighted_global_forward/bidirectional modes (pooled FPR across all pairs).

α=0.75 Detection Rate (6 modes):
| Mode | Detection |
|------|-----------|
| weighted_pair_forward | 21/24 = 87.5% |
| weighted_pair_bidirectional | 15/24 = 62.5% |
| uniform_forward | 8/24 = 33.3% |
| uniform_bidirectional | 8/24 = 33.3% |
| weighted_global_forward | 3/24 = 12.5% |
| weighted_global_bidirectional | 2/24 = 8.3% |

All modes: FPR = 0/24 at α=0.00.

Table 7 (α=1.0, weighted_pair_forward):
Baseline 5/8, GPT-2m 7/8, OPT 5/8, 1.4B-s42 4/8, 1.4B-s43 4/8, C4-s42 5/8, C4-s43 4/8

Global weighting too conservative — per-pair weighting recommended as primary.