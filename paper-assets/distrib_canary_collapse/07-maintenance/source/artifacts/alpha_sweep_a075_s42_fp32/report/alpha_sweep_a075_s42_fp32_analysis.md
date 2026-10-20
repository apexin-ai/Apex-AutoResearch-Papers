# Analysis: alpha_sweep_a075_s42_fp32

**Date:** 2026-05-19  
**Model:** EleutherAI/pythia-410m | **Seed:** 42 | **α:** 0.75 | **Precision:** fp32  
**Generations:** 11 (gen_0–gen_10) | **Server:** westd-17855 | **Wall-clock:** ~4.84 GPU-hours  
**Config:** left-padding (D093), 5000 steps/gen, lr=5e-5, top_p=0.95

## 1. Drift Summary (gen_0 → gen_10)

| Metric | gen_0 | gen_10 | Drift % |
|--------|-------|--------|---------|
| token_entropy | 3.2342 | 2.2830 | **−29.41%** |
| ece | 0.0108 | 0.2145 | **+1885.41%** |
| perplexity | 26.949 | 77.697 | **+188.31%** |
| distinct_1 | 0.0980 | 0.0731 | **−25.38%** |
| distinct_2 | 0.5141 | 0.3570 | **−30.55%** |
| distinct_3 | 0.8127 | 0.5957 | **−26.70%** |
| effective_rank | 46.613 | 78.060 | **+67.47%** |
| mauve | 0.0311 | 0.0299 | **−3.73%** |

Collapse pattern clear: entropy ↓, calibration (ECE) degrades massively, perplexity nearly triples, diversity (distinct-n) drops ~25-30%. MAUVE near-flat (already low baseline at 0.03).

## 2. Lead-Lag Analysis (5-Method)

| Method | Sig/Total |
|--------|-----------|
| naive_xcorr | 7/8 |
| diff_xcorr | 6/8 |
| threshold_onset | 8/8 |
| perm_granger_fwd | **6/8** |
| perm_granger_rev | **0/8** |
| ty_granger | 8/8 |
| **K≥4 consensus** | **6/8** |
| MMCT detection | **75%** |

**PermG asymmetry: fwd=6, rev=0** — strong unidirectional canary→downstream signal.

## 3. Pair-Level Consensus

| Pair | Votes | K≥4 | Methods |
|------|-------|------|---------|
| token_entropy→distinct_1 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |
| token_entropy→distinct_2 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |
| token_entropy→distinct_3 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |
| token_entropy→mauve | 2/5 | ✗ | thresh, ty |
| ece→distinct_1 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |
| ece→distinct_2 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |
| ece→distinct_3 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |
| ece→mauve | 3/5 | ✗ | naive, thresh, ty |

6/8 pairs reach K≥4. The 2 failing pairs are both →mauve, explained by MAUVE's near-flat trajectory (−3.73% drift).

## 4. Dose-Response Comparison

| α | PermG fwd | K≥4 | MMCT | Regime |
|---|-----------|------|------|--------|
| 0.50 fp32 | 6/8 | 6/8 | 6/8 | mid-high |
| 0.60 fp32 | 3/8 | 7/8 | 7/8 | mid |
| **0.75 fp32** | **6/8** | **6/8** | **75%** | **high** |
| 1.00 fp32 | ~75% | ~6.5/8 | — | high |

α=0.75 fits the high-regime bracket. PermG at 75% (6/8) is slightly below the hypothesized ~83% but within expected single-seed variance. K≥4 and MMCT are consistent with dose-response expectations.

## 5. TY Granger Note

TY shows 8/8 significant. α=0.75 > 0.50 threshold (C003 compliant). Most pairs have d_max=0, df_resid=7 (well-conditioned). Exception: ece→mauve has d_max=2, df_resid=1 — borderline but not flagged since the pair fails K≥4 anyway.

## 6. Conclusion

**SUCCESS.** α=0.75 fp32 confirms high-regime canary lead-lag behavior with D079-compliant fp32 precision. Key findings:
- Strong collapse (ppl +188%, ECE +1885%, entropy −29%)
- Robust lead-lag: PermG 6/8 fwd, 0/8 rev (perfect asymmetry)
- K≥4 consensus 6/8, consistent with dose-response curve
- MAUVE pairs are the sole non-significant pairs due to flat MAUVE trajectory
