# Provenance Audit Report (D105)

**Date**: 2026-05-16  
**Auditor**: Worker (automated)  
**Scope**: 3 reported numerical discrepancies between paper and registry

---

## Summary

| ID | Claim | Current Paper Value | Registry Truth | Status |
|----|-------|-------------------|----------------|--------|
| c032 | LP cond RE ρ = 0.002 | **0.011** | 0.0112 | CORRECT (already fixed or misreported) |
| c023 | Q1-Q4 SJ ρ = 0.110→0.473 | **0.110→0.473** | 0.447→0.540 | **DISCREPANCY CONFIRMED** |
| c021 | WNUT SJ ρ = 0.062 | **0.089** | 0.089 | CORRECT (fixed in docs/ version) |

---

## Detailed Findings

### c032: LP Conditional RE ρ (72x差异)

**Reported**: Paper writes 0.002, registry truth is 0.0112  
**Actual finding**: Paper currently writes **0.011**, NOT 0.002

- `docs/paper/sections/experiments.tex:50` — "LP $^\dagger$RE collapses to $\rho{=}0.011$"
- `docs/paper/sections/appendix.tex:137` — figure caption: "LP RE collapses to near-zero ($\rho{=}0.011$)"

**Registry verification** (`exp_012_rerun_1024/report.json`):
```
re_logprob_baseline.conditional.rho = 0.01119 (n=238)
```

**Verdict**: Paper's 0.011 is a correct 3-decimal rounding of 0.01119. No error.

**Wrong-source confirmation**: exp_015 (max_tokens=512) gives cond rho=0.1457 (n=296) — different filtering threshold produces inflated n and different rho, but this value is NOT in the paper.

**Note on "0.002"**: This value was NOT found anywhere in the paper (current or old versions) as LP cond RE ρ. The task description may contain a misattribution. The only 0.002 values in experiments.tex are confidence intervals (±0.002) and unrelated deltas.

---

### c023: Q1-Q4 Stratification SJ ρ — CONFIRMED DISCREPANCY

**Location**: `docs/paper/sections/appendix.tex:150`

**Paper text**:
```latex
For RE, SJ $\rho$ increases monotonically with sentence length 
(Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$)
```

**Registry truth** (`exp009_stratification_results.json`, scierc_re, by_sent_len):
```
Q1 (lowest): n=143, sj_rho=0.4472
Q2:          n=151, sj_rho=0.3191
Q3:          n=119, sj_rho=0.4975
Q4 (highest):n=138, sj_rho=0.5401
```

**Discrepancy analysis**:
- Paper Q1=0.110 vs truth Q1=0.447 (4x difference)
- Paper Q4=0.473 vs truth Q4=0.540 (14% off)
- Paper claims "monotonically increasing" — truth is NON-monotonic (Q2 dips to 0.319)
- Paper's Fisher z-test p=0.004 may be valid for the wrong values, not the truth

**Possible confusion sources**:
1. **exp_009_v2** (re_seed42, tertile bins): T1=-0.046, T2=0.138, T3=0.267 — T2≈0.138 is close to 0.110 but not exact
2. **by_greedy_f1 dimension** (RE): values are -0.043, -0.003, 0.006, 0.210 — no match
3. **Different pipeline version**: The values 0.110 and 0.473 may originate from an intermediate analysis with different bin boundaries or conditional filtering not present in the final data

**Root cause hypothesis**: Values likely came from a preliminary analysis run (possibly with quartile boundaries computed on a subset, or from a different stratification variable) and were never reconciled with the final exp009 data.

**Correct text should read**: "For RE, SJ ρ ranges from 0.319 (Q2) to 0.540 (Q4) across sentence-length quartiles (Q1: 0.447); the pattern is non-monotonic."

---

### c021: WNUT SJ ρ

**Reported**: Paper writes 0.062, registry truth is 0.089  
**Actual finding**: Paper **already fixed** to 0.089 in current compilation version.

**Current paper** (`docs/paper/sections/appendix.tex:222`, Table tab:wnut):
```latex
SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
```

**Registry verification** (`exp003_wnut17_eval/report.json`):
```
correlation_softjaccard_vs_f1_full.rho = 0.08883 (n=689)
correlation_softjaccard_vs_f1_conditional.rho = 0.2884 (n=334)
```

**Old version** (`artifacts/_project/paper/experiments.tex:181`):
```latex
SJ achieves $\rho{=}0.062$ ($p{=}0.106$, not statistically significant)
```

**Verdict**: Already corrected. The old 0.062 (artifacts/ version) was likely from an earlier pilot run (exp003_wnut17_pilot?) or from full-set n=1287 without gold-empty filtering.

---

## TACRED Process Check

```
ps aux | grep tacred → No matches
```

No TACRED-related processes running on autodl-5090. The `exp_tacred_re_benchmark` in registry has status=PREPARING, conclusion=killed.

---

## Action Items

| Priority | Item | Action Required |
|----------|------|----------------|
| HIGH | c023 (appendix.tex:150) | Fix Q1-Q4 values to match registry truth. Remove "monotonically increasing" claim. Consider whether to report quartiles (non-monotonic) or focus on Q1 vs Q4 comparison only. |
| NONE | c032 | No action needed — paper is correct (0.011 ≈ 0.0112). |
| NONE | c021 | No action needed — already fixed in docs/ compilation version. |
| LOW | Constraint C001 reminder | Confirm artifacts/_project/paper/ files are NOT used in compilation. They contain stale values (0.062 for WNUT). |

---

## Data Provenance Chain

```
exp_012_rerun_1024 (max_tokens=1024, n_cond=238) → LP RE cond ρ=0.0112 → paper: 0.011 ✓
exp009_stratification_results.json (by_sent_len, scierc_re) → Q1=0.447, Q4=0.540 → paper: 0.110, 0.473 ✗
exp003_wnut17_eval (n=689, gold-filtered) → SJ ρ=0.089 → paper: 0.089 ✓
```
