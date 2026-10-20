# s42 1.4B 6-pair D102 Results

Date: 2026-05-24
Pipeline: batch_d102_6pair.py (5-method, 5000 perm, BH FDR, D111 direction filter peak_lag<0, C009)
Pairs: 6 (2 canaries × 3 distinct, mauve excluded per D210)

## Summary Table

| α | T | PermG fwd | PermG rev | Robust ≥3/5 | ent→d1 | ent→d2 | ent→d3 | ece→d1 | ece→d2 | ece→d3 |
|------|-----|-----------|-----------|-------------|--------|--------|--------|--------|--------|--------|
| 0.45 | 10 | 0/6 | 0/6 | 0/6 | 1(ty) | 1(diff) | 2(naive,ty) | 2(naive,ty) | 2(naive,diff) | 2(naive,ty) |
| 0.50 | 10 | 4/6 | 0/6 | 2/6 | 2(perm,ty) | 2(naive,ty) | 2(naive,ty) | 2(perm,ty) | 3(naive,perm,ty) | 3(naive,perm,ty) |
| 0.60 | 10 | 4/6 | 0/6 | 0/6 | 2(perm,ty) | 1(ty) | 2(naive,ty) | 1(perm) | 2(perm,ty) | 2(perm,ty) |
| 0.75 | 10 | 5/6 | 0/6 | 0/6 | 1(perm) | 1(perm) | 0 | 2(perm,ty) | 2(perm,ty) | 2(perm,ty) |
| 0.45 | 15 | 3/6 | 0/6 | 3/6 | 2(naive,ty) | 2(naive,ty) | 2(naive,ty) | 3(naive,perm,ty) | 3(naive,perm,ty) | 3(naive,perm,ty) |
| 0.50 | 15 | 3/6 | 0/6 | 1/6 | 2(naive,ty) | 2(naive,ty) | 2(naive,ty) | 1(perm) | 2(naive,perm) | 3(naive,perm,ty) |
| 0.60 | 15 | 6/6 | 0/6 | 4/6 | 3(naive,perm,ty) | 3(naive,perm,ty) | 3(naive,perm,ty) | 2(perm,ty) | 2(perm,ty) | 3(naive,perm,ty) |
| 0.75 | 15 | — | — | — | — | — | — | — | — | — |

## Notes
- **t15_a075_s42**: No 1.4B experiment data exists. Only 410M version (t15_a075_s42_fp32) found.
- All reverse PermG = 0/6 across all experiments (good: no reverse causality detected).
- T=15 generally shows improved detection vs T=10 at same α (e.g., α=0.45: 0/6→3/6 robust; α=0.60: 0/6→4/6 robust).
- α=0.75 T=10: PermG 5/6 but Robust 0/6 — PermG detects but other methods don't agree (xcorr/threshold fail due to rapid saturation).
- Diff_xcorr and threshold_onset rarely fire for s42 in this pipeline (these methods sensitive to orientation/series shape).

## Data Sources
- t10_a045, t10_a060, t10_a075, t15_a045, t15_a050, t15_a060: westd-17855
- t10_a050: westd-19828
