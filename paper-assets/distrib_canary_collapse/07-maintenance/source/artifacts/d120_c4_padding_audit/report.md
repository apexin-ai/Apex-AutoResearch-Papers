# D120 Recomputation: C4 s42 + Padding-410M Audit

**Date**: 2026-05-20
**Server**: westd-17855
**Script**: `run_5method_analysis_d102.py` (D105 true 3σ + D111 direction integrated)
**Parameters**: n_perm=5000, threshold=true_3sigma_d105, direction=peak_lag<0 (C009)

## Summary Table

| Experiment | α | Domain | PermG_fwd | PermG_rev | naive | diff | thresh_3σ | TY | K≥3 | K≥4 |
|---|---|---|---|---|---|---|---|---|---|---|
| c4_a025_s42_fp32 | 0.25 | C4 | 0/8 | 0/8 | 4/8 | 8/8 | 2/8 | N/A | 0/8 | 0/8 |
| c4_a050_s42_fp32 | 0.50 | C4 | 8/8 | **7/8** | 4/8 | 8/8 | 0/8 | N/A | 4/8 | 0/8 |
| c4_a075_s42_fp32 | 0.75 | C4 | 8/8 | 0/8 | 8/8 | 8/8 | 0/8 | N/A | 8/8 | 0/8 |
| padding_a100_s42_fp32 | 1.0 | Wiki(pad) | 6/8 | 0/8 | 6/8 | 6/8 | 0/8 | N/A | 6/8 | 0/8 |

## C4 Cross-Domain Dose-Response (D120)

C4 α dose-response under D120 true 3σ:
- **α=0.25**: PermG=0/8, K3=0/8. Below detection threshold. Consistent with wiki domain.
- **α=0.50**: PermG=8/8, K3=4/8. Transition zone. **Notable: PermG_rev=7/8 (bidirectional)**. This is unique to C4 cross-domain — wiki α=0.50 typically shows 0/8 reverse. Indicates stronger mutual feedback in cross-domain contamination.
- **α=0.75**: PermG=8/8, K3=8/8. Full detection. Strong unidirectional asymmetry (rev=0/8).

### Comparison with s43 (same script, prior D120 batch)

| α | s42 PermG | s43 PermG | s42 K≥3 | s43 K≥3 |
|---|---|---|---|---|
| 0.50 | 8/8 | 8/8 | 4/8 | 3/8 |
| 0.75 | 8/8 | 8/8 | 8/8 | 8/8 |

Cross-seed consistent for PermG. K≥3 minor variation at α=0.50 (4 vs 3) from naive_xcorr variability.

## Padding-410M Audit (Table 7)

### D120 Results
- **PermG_fwd**: 6/8 (FDR-corrected, per-direction)
- **PermG_rev**: 0/8 → strong directional asymmetry
- **K≥3**: 6/8
- **Failing pairs**: token_entropy→mauve (0/5), ece→mauve (0/5)
  - mauve NaiveR = -0.436 (weak, wrong sign), DiffR peak_lag=-4/-5 (too deep)

### Comparison with Wiki Baseline

| Metric | padding_a100_s42 | wiki_a100_s42 (registry) |
|---|---|---|
| K≥3 | 6/8 | 6/8 |
| PermG_fwd | 6/8 | 6/8 |
| Failing pairs | mauve | mauve (inferred) |

**Conclusion**: Padding side (D093 right→left fix) has **no detectable effect** on lead-lag signal. K3=6/8 matches wiki baseline exactly. The 2 failing pairs are both mauve, consistent across padding variants.

## TY Granger API Error

All 4 experiments hit `VARResults.test_causality() got an unexpected keyword argument 'signonly'` on westd-17855. This is a statsmodels version incompatibility specific to this server.

**Impact**: TY returns N/A → max consensus = 3/5 (naive+diff+perm) → K≥4 capped at 0/8 for all D120 runs on this server. Previous analyses on other servers had working TY (e.g., c4_a075_s43 TY=1/8).

**Mitigation**: K≥3 (the primary paper metric) is unaffected. K≥4 comparisons across servers require TY fix or exclusion from vote denominator.

## Changes from Pre-D120 Registry

| Exp | Field | Old | D120 | Reason |
|---|---|---|---|---|
| c4_a025 | threshold_onset | 8/8 | 2/8 | D105 true 3σ (std of full series) |
| c4_a025 | diff_xcorr | 0/8 | 8/8 | C009 sign fix (peak_lag>0 → peak_lag<0) |
| c4_a050 | PermG_rev | 0/8 | 7/8 | D120 integrated analysis detects bidirectional |
| c4_a050 | K3 | 6/8 | 4/8 | C009 fix adjusts naive direction counts |
| c4_a075 | naive_xcorr | 0/8 | 8/8 | C009 sign fix recovers naive |
| c4_a075 | diff_xcorr | 0/8 | 8/8 | C009 sign fix recovers diff |
| c4_a075 | K3 | 6/8 | 8/8 | C009 recovery of naive+diff |
| padding | K4 | 6/8 | 0/8 | TY broken on 17855 (was 4th method) |

## Per-Experiment Detail

### c4_a025_s42_fp32 (α=0.25)

Forward consensus per pair:
```
token_entropy<distinct_1  2/5  [naive, diff]
token_entropy<distinct_2  1/5  [diff]
token_entropy<distinct_3  2/5  [diff, threshold]
token_entropy<mauve       2/5  [naive, diff]
ece<distinct_1            2/5  [naive, diff]
ece<distinct_2            1/5  [diff]
ece<distinct_3            2/5  [diff, threshold]
ece<mauve                 2/5  [naive, diff]
```

diff_xcorr bidirectional (fwd=8/8, rev=8/8) — no directional selectivity, consistent with α below onset. PermG 0/8 correctly identifies no signal.

### c4_a050_s42_fp32 (α=0.50)

Forward consensus per pair:
```
token_entropy<distinct_1  3/5  [naive, diff, perm]
token_entropy<distinct_2  2/5  [diff, perm]
token_entropy<distinct_3  3/5  [naive, diff, perm]
token_entropy<mauve       3/5  [naive, diff, perm]
ece<distinct_1            3/5  [naive, diff, perm]
ece<distinct_2            2/5  [diff, perm]
ece<distinct_3            2/5  [diff, perm]
ece<mauve                 2/5  [diff, perm]
```

PermG bidirectional note: 8/8 forward + 7/8 reverse. The only non-significant reverse pair is mauve→token_entropy (PermFDR not sig). This bidirectionality may reflect C4's domain diversity creating stronger feedback loops at moderate α.

### c4_a075_s42_fp32 (α=0.75)

All 8 pairs: 3/5 [naive, diff, perm]. Perfect PermG asymmetry (8/8 fwd, 0/8 rev). PermG F-stats range 239-1390 (forward) vs 0.02-0.70 (reverse). Cleanest directional separation in the C4 sweep.

### padding_robustness_a100_s42_fp32 (α=1.0)

```
token_entropy<distinct_1  3/5  [naive, diff, perm]
token_entropy<distinct_2  3/5  [naive, diff, perm]
token_entropy<distinct_3  3/5  [naive, diff, perm]
token_entropy<mauve       0/5  [none]
ece<distinct_1            3/5  [naive, diff, perm]
ece<distinct_2            3/5  [naive, diff, perm]
ece<distinct_3            3/5  [naive, diff, perm]
ece<mauve                 0/5  [none]
```

Mauve failure: NaiveR=-0.436 (weak negative), DiffR at lag=-4/-5 (too deep to be meaningful), PermG F<1 (no Granger signal). Mauve is measuring text quality at a coarser level that doesn't track the generation-by-generation canary signal.
