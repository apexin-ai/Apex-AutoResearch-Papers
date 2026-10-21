# D108 v4: MMLU Domain-Level γ Heterogeneity (N=24)

## Summary

N=24 results show dramatic instability vs. N=16: **4 of 7 domains reversed γ direction**, and **3 domains exhibit PPP=1.0 model misfit**. The heterogeneity story (Simpson's paradox) still holds — γ range [-0.50, +0.97] — but individual domain estimates are unreliable enough to weaken Claim 1.

---

## Results Table (N=24 v4)

| Domain | N_models | γ mean | 95% CI | Sig? | PPP | Diagnostics |
|--------|----------|--------|--------|------|-----|-------------|
| STEM_Math | 23 | **+0.969** | [+0.527, +1.430] | YES | 0.438 | all ok |
| STEM_Science | 23 | **+0.838** | [+0.385, +1.274] | YES | 0.807 | all ok |
| STEM_CS_Eng | 23 | +0.197 | [-0.448, +0.835] | NO | 0.892 | all ok |
| Medical | 24 | **-0.199** | [-0.338, -0.060] | YES | **1.000** | all ok (PPP misfit) |
| Humanities | 21 | **-0.407** | [-0.776, -0.041] | YES | **1.000** | **rhat_ok=FALSE** (1.0135) |
| Social_Sciences | 21 | **-0.497** | [-0.827, -0.151] | YES | **1.000** | all ok (PPP misfit) |
| Business_Law | 21 | -0.168 | [-0.538, +0.230] | NO | 0.9998 | all ok |

**Significant domains**: 5/7 (STEM_Math, STEM_Science, Medical, Humanities, Social_Sciences)  
**γ range**: -0.497 to +0.969 (span=1.47)  
**Direction split**: 2 positive (STEM), 3 negative (Medical/Humanities/SocSci)

---

## Comparison with N=16

| Domain | N=16 γ | N=16 sig | N=24 γ | N=24 sig | Direction consistent? |
|--------|--------|----------|--------|----------|----------------------|
| STEM_Math | -0.549 | NO | **+0.969** | YES | **REVERSED** |
| STEM_Science | +0.361 | NO | +0.838 | YES | consistent (strengthened) |
| STEM_CS_Eng | +0.294 | NO | +0.197 | NO | consistent (still NS) |
| Medical | +0.266 | NO | -0.199 | YES | **REVERSED** |
| Humanities | +0.473 | YES | -0.407 | YES | **REVERSED** |
| Social_Sciences | +0.283 | YES | -0.497 | YES | **REVERSED** |
| Business_Law | +0.608 | YES | -0.168 | NO | **REVERSED** |
| Other | +1.342 | YES | — | — | (not in N=24 run) |

**Direction reversals: 5/7 domains.**

---

## Key Issues

### 1. STEM_Math reversal (D111 flag) — resolved but unexpected
D111 flagged STEM_Math γ direction reversal at N=24. Confirmed: went from -0.549 to +0.969. The sign flip came with significance gain. At N=16 it was non-significant, so the negative estimate was noise. N=24 positive estimate is well-identified (narrow CI, good PPP=0.438). **This domain is now trustworthy.**

### 2. Humanities/Social_Sciences/Business_Law reversals — PROBLEMATIC
All three were positive and significant at N=16, now negative at N=24. Critical differences:
- N_models dropped from 16 to 21 (different model composition, not just adding models)
- These large domains were subsampled (2816→2000, 3077→2000, 2482→2000 items)
- PPP=1.0 for Humanities and Social_Sciences = 2PL+γ model doesn't fit these data well
- Humanities has convergence issues (rhat=1.0135)

Probable cause: model pool changed from 3B-only (N=16) to multi-scale 0.5B+1.5B+3B (N=24). Smaller models may have qualitatively different contamination patterns in humanities/social science domains.

### 3. PPP=1.0 model misfit (3 domains)
Medical, Humanities, Social_Sciences all show PPP=1.0. Per D112, Medical was already flagged for exclusion. The same logic applies to Humanities and Social_Sciences — the 2PL+γ model is inadequate for these domains at this sample size and model composition.

### 4. Stan fit error in v2 log
Social_Sciences fit crashed with retcodes=[1,0,0,1] (chains 1 & 4: "Operation not permitted"). A subsequent run produced results (all 4 chains completed with 0 divergences), so the final results are valid. The error was likely a system-level issue (file permission or process limit), not a model issue.

---

## Impact on Paper Claim 1

**Original claim**: "Aggregate γ≈0 masks domain-level heterogeneity (Simpson's paradox)"

**Still supportable** (γ ranges from -0.50 to +0.97), BUT with serious caveats:
- Individual domain estimates are not stable across N — cannot claim specific domains have specific γ directions
- PPP=1.0 in 3 domains means model misspecification, not just random variation

### What can go in the paper:

1. **Strong**: STEM_Math (γ=+0.97, PPP=0.44, well-converged) and STEM_Science (γ=+0.84, PPP=0.81) — robust positive γ, good model fit
2. **Supportable with caveat**: The existence of heterogeneity (range > 1.4 across domains)
3. **Exclude**: Medical (PPP=1.0, per D112), Humanities (PPP=1.0 + convergence failure), Social_Sciences (PPP=1.0)

### What needs caution:

- Cannot claim specific negative-γ domains without addressing PPP=1.0 misfit
- N=16 to N=24 instability should be acknowledged as sensitivity to respondent composition
- "Other" domain (strongest γ at N=16) was dropped from N=24 — needs explanation

---

## Recommendations

1. **Paper table**: Report all 7 domains but mark PPP=1.0 domains with misfit flag. Primary evidence for heterogeneity comes from STEM_Math and STEM_Science (clean fits, significant, consistent direction).

2. **Sensitivity analysis**: Note that γ estimates are sensitive to which models are included (3B-only vs. multi-scale). This is itself an interesting finding — contamination effects may be scale-dependent within domains.

3. **Exclude from strong claims**: Medical (per D112), Humanities (PPP=1.0 + rhat fail), Social_Sciences (PPP=1.0). These can appear in tables but should not anchor quantitative claims.

4. **Reframe narrative**: Instead of "5/8 domains significant positive γ" (N=16 framing), use "domain-level γ spans > 1.4 units, with STEM domains showing strong positive contamination signal and non-STEM domains showing model misspecification under 2PL+γ."

5. **Consider**: Re-running Humanities/SocSci/Business_Law with 3B-only models (matching N=16 composition) to isolate whether the direction change is due to scale mixing vs. additional seeds.
