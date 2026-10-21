# Paper Number Consistency Audit

**Date**: 2026-05-14
**Scope**: All quantitative claims in abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex
**Sources**: plan-012-full (registry), bootstrap_95ci.json, plan-003-baseline-245eps, plan-004-ablation-b, plan-004-v5, math-pilot-50.json, step-tie-rate analysis

---

## 1. Death Avoidance Core Data

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Δ_full | +29.60 | 29.6 | plan-012-full metrics.delta_full | **[PASS]** |
| Δ_nd | +2.84 | 2.84 | plan-012-full metrics.delta_nd | **[PASS]** |
| DAF | 90.41% | 0.9041 → 90.41% | plan-012-full metrics.death_avoidance_fraction | **[PASS]** |
| DAF formula check | 1 − 2.84/29.60 | = 0.90405 → 90.41% | arithmetic | **[PASS]** |
| r | 0.9698 | 0.9698 | plan-012-full metrics.pearson_r | **[PASS]** |
| p | 8.12×10⁻⁷ | 8.12e-07 | plan-012-full metrics.pearson_p | **[PASS]** |
| Task types | 11 | 11 | plan-012-full metrics.tasks | **[PASS]** |
| Episodes | 245 | 245 | plan-012-full metrics.episodes | **[PASS]** |
| Death rate internal | 42.9% | 0.429 → 42.9% | plan-012-full metrics.death_rate_int | **[PASS]** |
| Death rate deterministic | 16.3% | 0.163 → 16.3% | plan-012-full metrics.death_rate_det | **[PASS]** |
| Death rate ratio "2.6×" | 42.9/16.3 = 2.63 | matches | arithmetic | **[PASS]** |
| det-preferred | 86 | 86 | plan-012-full metrics.label_dist | **[PASS]** |
| internal-preferred | 9 | 9 | plan-012-full metrics.label_dist | **[PASS]** |
| no-preference | 150 | 150 | plan-012-full metrics.label_dist | **[PASS]** |
| Label total | 86+9+150=245 | 245 | arithmetic | **[PASS]** |
| Abstract "r = 0.97" | 0.97 | 0.9698 rounds to 0.97 | rounding | **[PASS]** |
| Abstract "approximately 90%" | ~90% | 90.41% ≈ 90% | rounding | **[PASS]** |
| Introduction "Δ_nd = +2.84 is 9.6% of Δ_full" | 9.6% | 2.84/29.60 = 9.59% ≈ 9.6% | arithmetic | **[PASS]** |
| Episodes "20–40 per type" | 20–40 | range: 20 (most tasks) to 40 (find-non-living-thing) | per-task data | **[PASS]** |

---

## 2. Table 1 (Baseline Comparison)

### Scores (vs bootstrap_95ci.json, n=245)

| Strategy | Paper Score | Source Score | Verdict |
|----------|------------|-------------|---------|
| Always-Internal | −39.07 | −39.07 | **[PASS]** |
| Always-Det | −9.47 | −9.47 | **[PASS]** |
| Oracle | −6.58 | −6.58 | **[PASS]** |
| Random | −22.38 | −22.38 | **[PASS]** |
| Trained Router | −10.70 | −10.70 | **[PASS]** |

### 95% Bootstrap CIs (vs bootstrap_95ci.json)

| Strategy | Paper CI | Source CI | Verdict |
|----------|---------|----------|---------|
| Always-Internal | [−46.40, −32.27] | [−46.40, −32.27] | **[PASS]** |
| Always-Det | [−14.71, −4.29] | [−14.71, −4.29] | **[PASS]** |
| Random | [−28.67, −15.75] | [−28.67, −15.75] | **[PASS]** |
| Oracle | [−11.54, −1.70] | [−11.54, −1.70] | **[PASS]** |
| Trained Router | [−16.33, −5.27] | [−16.33, −5.27] | **[PASS]** |

### Death Rates (vs plan-003-baseline-245eps + plan-012-full + plan-003-e2e-ablation-b-correct)

| Strategy | Paper Death% | Source | Verdict |
|----------|-------------|--------|---------|
| Always-Internal | 42.9% | plan-012-full death_rate_int=0.429; plan-003-baseline-245eps: 42.9% | **[PASS]** |
| Always-Det | 16.3% | plan-012-full death_rate_det=0.163; plan-003-baseline-245eps: 16.3% | **[PASS]** |
| Oracle | 14.3% | plan-003-baseline-245eps: 14.3%; plan-013: 35 both-died episodes → 35/245=14.29% | **[PASS]** |
| Random | 27.8% | plan-003-baseline-245eps: 27.8% | **[PASS]** |
| Trained Router | 17.6% | plan-003-e2e-ablation-b-correct death_rate=0.1755 → 17.55% ≈ 17.6% | **[PASS]** |

### Δ_full consistency with Table 1

| Check | Value | Verdict |
|-------|-------|---------|
| det − int = −9.47 − (−39.07) = 29.60 = Δ_full | 29.60 | **[PASS]** |
| "router 1.23 points below always-det" = −10.70 − (−9.47) | −1.23 | **[PASS]** |

---

## 3. Tie Rate

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Step-level tie rate | 97.4% | 97.39% (5935/6094 steps, 245 eps, 11 tasks) | plan-012-step-tie-rate | **[PASS]** |
| "corrected from 98.2%" | 98.2% → 97.4% | 97.39% confirmed; 98.2% was MVP-era value on different methodology | step-tie-rate analysis notes | **[PASS]** |

---

## 4. Router Training

### GA=8 (plan-004-ablation-b, seed 42)

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Generation accuracy | 65.4% | 0.6536 → 65.36% ≈ 65.4% | plan-004-ablation-b metrics.generation_level.accuracy | **[PASS]** |
| Internal recall | 51.5% | 0.5152 → 51.52% ≈ 51.5% | plan-004-ablation-b metrics.generation_level.internal_recall | **[PASS]** |

### GA=1 (plan-004-v5, seed 42)

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Logit accuracy | 74.5% | 0.7451 → 74.51% ≈ 74.5% | plan-004-v5 metrics.logit_level.accuracy | **[PASS]** |
| Balanced accuracy | 79% | 0.7905 → 79.05% ≈ 79% | plan-004-v5 metrics.logit_level.balanced_accuracy | **[PASS]** |
| Generation accuracy | 53.3% | 0.5333 → 53.33% ≈ 53.3% | plan-004-v5 metrics.generation_eval.accuracy | **[PASS]** |
| Internal recall | 26.7% | 0.2667 → 26.67% ≈ 26.7% | plan-004-v5 metrics.generation_eval.internal_recall | **[PASS]** |
| Logit–generation gap | 21.2 pp | 74.51% − 53.33% = 21.18% ≈ 21.2% | arithmetic | **[PASS]** |

### 4-Seed Results (GA=8, seeds 42/123/456/789)

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Balanced acc mean | 58.1% | (59.27+57.36+57.48+58.31)/4 = 58.105% | 4-seed registry entries | **[PASS]** |
| Balanced acc ± | ±0.8% | sample σ = 0.884%, pop σ = 0.766% | arithmetic | **[NOTE]** ±0.8 is between pop (0.77) and sample (0.88) stds; closest natural rounding would be ±0.9 (sample) or ±0.8 (population). Acceptable. |
| Internal recall range | 51.5%–81.8% | 51.52%–81.82% | seeds 42, 789 | **[PASS]** |
| "8 points above chance" | 58.1% − 50% = 8.1 pp | arithmetic | **[PASS]** |

### End-to-End Router Eval

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Sim invocation ratio | 97.0% | 0.9703 → 97.03% | plan-003-e2e-ablation-b-correct metrics.sim_ratio | **[PASS]** |

---

## 5. Cross-Environment (MATH Pilot)

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| Problems | 50 | 50 | math-pilot-50.json n_problems | **[PASS]** |
| Level | 4–5 | Level 4-5 | experiment design | **[PASS]** |
| Internal accuracy | 80% | 40/50 = 80% | math-pilot-50.json internal_accuracy | **[PASS]** |
| Code interpreter accuracy | 72% | 36/50 = 72% | math-pilot-50.json codeinterp_accuracy | **[PASS]** |
| No-preference rate | 88% | 44/50 = 88% | math-pilot-50.json labels_filtered.nopref=44 | **[PASS]** |
| det-preferred | 1 | 1 | math-pilot-50.json labels_filtered.det=1 | **[PASS]** |
| internal-preferred | 5 | 5 | math-pilot-50.json labels_filtered.int=5 | **[PASS]** |
| no-preference | 44 | 44 | math-pilot-50.json labels_filtered.nopref=44 | **[PASS]** |

---

## 6. find-non-living-thing Exception

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| n | 40 | 40 | plan-012 per-task decomposition | **[PASS]** |
| Deaths | zero | dr_int=0.00, dr_det=0.00 | plan-012 per-task decomposition | **[PASS]** |
| Δ_full | +9.58 | +9.58 | plan-012 per-task decomposition | **[PASS]** |

---

## 7. Oracle Degeneracy

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| "96.3% decisions match always-det" | 96.3% | (86 det + 150 no-pref) / 245 = 236/245 = 96.33% ≈ 96.3% | episode-level from label distribution | **[PASS]** |

Note: plan-003-baseline-245eps reports oracle sim_ratio=96.2% (step-level). Paper uses 96.3% (episode-level). Both are valid; paper is internally consistent using episode-level interpretation.

---

## 8. Additional Claims

| Claim | Paper Value | Source Value | Source | Verdict |
|-------|-------------|-------------|--------|---------|
| "ScienceWorld spans 30 task types" | 30 | ScienceWorld has 30 task types | ScienceWorld documentation | **[PASS]** |
| "Episodes capped at 30 steps" | 30 | Consistent across all experiment configs | experiment scripts | **[PASS]** |
| "$-100$ death penalty" | −100 | ScienceWorld standard | ScienceWorld environment | **[PASS]** |
| "~90% is death avoidance" (related_work.tex) | ~90% | 90.41% | plan-012-full | **[PASS]** |
| "Keyword match rate 85.8%" (experiments.tex) | 85.8% | 85.8% | plan-011-rule-based v1 | **[PASS]** |

---

## Summary

| Category | Total Checks | PASS | FAIL | NOTE |
|----------|-------------|------|------|------|
| Death Avoidance Core | 18 | 18 | 0 | 0 |
| Table 1 Scores | 5 | 5 | 0 | 0 |
| Table 1 CIs | 5 | 5 | 0 | 0 |
| Table 1 Death Rates | 5 | 5 | 0 | 0 |
| Table 1 Derived | 2 | 2 | 0 | 0 |
| Tie Rate | 2 | 2 | 0 | 0 |
| Router (GA=8) | 2 | 2 | 0 | 0 |
| Router (GA=1) | 5 | 5 | 0 | 0 |
| Router (4-seed) | 4 | 3 | 0 | 1 |
| Router (e2e) | 1 | 1 | 0 | 0 |
| MATH Pilot | 8 | 8 | 0 | 0 |
| find-non-living-thing | 3 | 3 | 0 | 0 |
| Oracle Degeneracy | 1 | 1 | 0 | 0 |
| Other | 5 | 5 | 0 | 0 |
| **TOTAL** | **66** | **65** | **0** | **1** |

### Result: **0 FAIL, 1 NOTE**

The single NOTE: 4-seed balanced accuracy reported as 58.1±0.8% — the ±0.8 is slightly imprecise (sample std is 0.884, population std is 0.766). Neither rounds naturally to 0.8. This is a minor presentation issue, not an error.

### Notation Inconsistency (non-numeric)
- Δ_nd (abstract, conclusion) vs Δ_no_death (introduction, experiments, method) — same quantity, inconsistent subscript notation across sections. Recommend unifying.
