# Paper v1/v2 Data Consistency Audit

**Date:** 2026-05-27  
**Auditor:** Claude  
**Scope:** All .tex files in `docs/paper/`  
**Truth source:** v2 verified data provided in task specification

---

## ❌ Issues Requiring Immediate Correction

### 1. Appendix statistical tests report v1 data without labeling — contradicts main text

**Location:** `appendix.tex:69`

> Detach OCC shows negligible difference from Vanilla ($d \approx -0.04$, $p = 0.91$)

**Problem:** These are v1 statistics. With v2 data (Detach OCC 0.767 vs Vanilla 0.745), Cohen's d ≈ +0.9 (large positive effect, not -0.04), and the main text reports p = 0.28 (abstract line 27, discussion.tex:6). The appendix section does not label these as v1, creating a direct numerical contradiction with the main text p-value.

**Fix options:**
- (a) Update to v2 statistics (d and p from v2 Detach OCC n=4 vs Vanilla n=3), or
- (b) Explicitly label as v1 data and note the main-text v2 p-value is 0.28

---

### 2. Detach+LN in Table 1 uses v1 data but table caption says "v2 code"

**Location:** `results.tex:16` (caption) vs `method.tex:49` (disclosure)

Table 1 caption states: *"Factorial conditions (above midrule) use v2 code."*  
Method section states: *"Detach+LN uses v1 ($n{=}3$)."*  

Detach+LN sits above the midrule (results.tex:26) with CAR = 0.765 ± 0.023, but this is v1 data. The v2 truth value is **0.802** (n=1). The table caption is factually incorrect for this row.

**Downstream consequences:**
- The ΔCAR of +2.0 for Detach+LN compares v1 data (0.765) against v2 Vanilla (0.745) — a cross-codebase comparison
- Random OCC (also v1, above midrule) correctly has ΔCAR omitted for this exact reason; Detach+LN should receive the same treatment or be flagged with `$^\star$`
- The -2.5pp LN factorial delta (results.tex:45,58; introduction.tex:10; conclusion.tex:4; fig caption results.tex:68) mixes v2 Full OCC+LN (0.740) with v1 Detach+LN (0.765). With all-v2 data the delta would be **-6.2pp** (0.740 vs 0.802), which would actually **reverse** the claim that "BN cell shows a larger deficit than LN"

**Fix options:**
- (a) Add `$^\star$` marker to Detach+LN row; omit its ΔCAR like Random OCC; update caption to note the exception
- (b) Replace with v2 value (0.802, n=1, mark with `$^\dagger$`); update all -2.5pp references to -6.2pp; revise the interaction narrative

---

### 3. "LN cells have n=1 each" contradicts Detach+LN n=3

**Location:** `results.tex:45` and `results.tex:47`

> "the LN cells have $n{=}1$ each"

But Detach+LN in Table 1 shows 3 seeds (v1 data), and method.tex:49 says "Detach+LN uses v1 ($n{=}3$)." If "n=1" refers to v2 seeds only, then the factorial table should use the v2 Detach+LN value (0.802), not the v1 value (0.765). The claim and the data are inconsistent with each other regardless of interpretation.

**Fix:** Align the n-count statement with the data actually used in the table. Either say "Detach+LN uses v1 (n=3)" or switch to v2 (n=1) and mark accordingly.

---

## ⚠️ Issues to Note (Non-blocking)

### 4. Per-task collision rates (43-93%) sourced from v1

**Location:** `introduction.tex:3`

> "On the three most constrained tasks, collision rates reach 43--93%."

This is from v1 per-task data (T6 CAR 0.57 → 43%, T5 CAR 0.07 → 93%) while the preceding sentence uses v2 overall CAR (74.5%). The discussion notes Vanilla shifts <1.5pp across codebases, so the per-task range is likely approximately valid, but strictly this mixes v1 task-level with v2 aggregate data.

### 5. Gradient amplitude analysis from v1 — properly labeled

**Location:** `appendix.tex:86,91`

Figure captions correctly note "v1 codebase checkpoint" and "v2 validation pending." The Detach gradient suppression (~4% of Vanilla norms) is correctly described as a v1 artifact (appendix.tex:121). No action needed.

### 6. Appendix line 69: "all gradient-flow conditions also show p > 0.35"

These p-values are likely from v1 data (same paragraph as the v1 d/p values). Should be verified against v2 data or labeled as v1.

---

## ✅ Verified Correct

### Core v2 numbers in main text

| Claim | Location | Value in Paper | Truth Source | Status |
|-------|----------|---------------|-------------|--------|
| Vanilla CAR | abstract:27, intro:3, results.tex:24 | 0.745 ± 0.024, n=3 | 0.745 ± 0.024, n=3 | ✅ |
| Full OCC BN CAR | abstract:27, results.tex:30 | 0.725 ± 0.064, n=3 | 0.725 ± 0.064, n=3 | ✅ |
| Detach OCC BN CAR | abstract:27, results.tex:25 | 0.767 ± 0.024, n=4 | 0.767 ± 0.024, n=4 | ✅ |
| Full OCC+LN CAR | results.tex:29 | 0.740, n=1 | 0.740, n=1 v2 | ✅ |
| BN Δ (Full-Detach) | abstract:27, results.tex:45 | -4.2pp | 0.725-0.767=-4.2pp | ✅ |
| Detach OCC vs Vanilla p-value | abstract:27, discussion.tex:6 | p=0.28 | Task spec confirms | ✅ |
| Full OCC BN σ >2.5× | abstract:27, results.tex:11 | 0.064 / 0.024 = 2.67× | Correct | ✅ |
| Full OCC BN seed range | results.tex:11 | [0.654, 0.776] → Δ=-9.1pp | 0.745-0.654=0.091 | ✅ |
| Hedges' g (BN row) | results.tex:45 | -0.781 | Calculated ≈ -0.79 | ✅ |
| Bootstrap CI crosses zero | results.tex:45 | [-0.108, 0.014] | Contains 0 | ✅ |
| TSR Vanilla | intro:3, results.tex:24 | 87.8% | Matches table | ✅ |
| Interaction magnitude | results.tex:60 | 1.7pp | (-1.5)-(+0.2)=-1.7 | ✅ |

### Claims correctly stated

| Claim | Location | Status |
|-------|----------|--------|
| No "gradient collapse" language | all files | ✅ No v1 gradient collapse claim found |
| No "CKA degradation" claim | all files | ✅ CKA ≥ 0.95 (representations intact) stated throughout |
| No "1-13%" gradient norm data | all files | ✅ v1 ~4% mentioned only as acknowledged artifact (appendix.tex:121) |
| Detach ≈ Vanilla (not "significantly better") | abstract, discussion | ✅ "statistically indistinguishable" with p=0.28 |
| "consistently" backed by multi-condition evidence | intro:16, conclusion:4 | ✅ Both BN and LN show same directional pattern |
| No unsupported "significantly" | results.tex:45 | ✅ "not individually significant at α=0.05" (honest) |
| Cosine ≈ 0 / orthogonality mechanism | abstract:28, results.tex:76-77 | ✅ Correct v2 mechanism |
| Spatial content irrelevance | abstract:28, results.tex:9 | ✅ Supported by Full OCC ≈ Random OCC ≈ Depth |
| v1→v2 behavioral shift documented | appendix.tex:114-125 | ✅ Transparent and informative |
| Binomial test (11/12 vs 12/12) | N/A | ✅ No binomial test appears in current paper — check item not applicable |

### Supplementary conditions (below midrule, v1 data)

All ΔCAR values computed against v1 Vanilla (0.780), internally consistent:
- Depth: 0.780-0.780 = 0.0 ✅
- Cutoff@15K: 0.782-0.780 = +0.2 ✅
- Cutoff@25K: 0.724-0.780 = -5.6 ✅
- Cutoff@35K: 0.779-0.780 = -0.1 ✅
- Cutoff@45K: 0.764-0.780 = -1.6 ✅
- Reverse Cutoff: 0.718-0.780 = -6.2 ✅

---

## Summary

| Category | Count | Details |
|----------|-------|---------|
| ❌ Needs fix | 3 | Appendix p-value/d v1 residual; Detach+LN v1/v2 table caption mismatch; n=1 vs n=3 contradiction |
| ⚠️ Note | 3 | Per-task intro mixing; gradient figures (labeled OK); appendix p>0.35 provenance |
| ✅ Correct | All core v2 numbers, all mechanism claims, all supplementary ΔCARs |

**Most critical issue:** The Detach+LN data discrepancy (#2-#3) affects the factorial interaction narrative. If the v2 value (0.802) were used, the LN delta would be -6.2pp (larger than BN's -4.2pp), reversing the "BN shows larger deficit" claim. This needs a deliberate decision before submission.
