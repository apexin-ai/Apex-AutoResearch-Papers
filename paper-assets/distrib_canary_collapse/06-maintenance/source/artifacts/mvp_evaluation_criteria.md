# MVP Evaluation Criteria: Canary Lead-Lag Detection

> **Pre-registered evaluation protocol.** Defined before MVP results are available to prevent post-hoc threshold adjustment. Any deviation from this document must be logged with justification in `memory.md` before analysis proceeds.

**MVP setup:** Pythia-410m, WikiText-103, 100% synthetic full replacement, 10 generations (Gen 0–9), 3 seeds (42/43/44). Canary metrics: `token_entropy`, `self_bleu`, `ece`, `effective_rank`. Downstream metrics: `perplexity`, `distinct_1`, `distinct_2`, `distinct_3`, `mauve`.

**Core hypothesis:** At least one canary metric family consistently leads at least one downstream metric by ≥1 generation across all 3 repetitions.

---

## 1. Cross-Correlation Significance Threshold

### The small-sample problem

With N=10 time points per series and max_lag=5, the effective overlap at extreme lags is only 5 data points. Pearson correlation on 5 points has catastrophically low power — even r=0.9 is not significant at p<0.05 with n=5 (critical r ≈ 0.878 for one-tailed test at df=3). Standard asymptotic p-values are unreliable here.

### Recommended method: Permutation test

For each (canary, downstream, seed) triplet:

1. Compute the observed peak |r| at the peak lag from `cross_correlate()`.
2. Generate B=10,000 permutations of the downstream series (random shuffle, breaking temporal structure).
3. For each permutation, recompute cross-correlation across all lags and record the max |r| across all lags (this accounts for multiple-lag testing).
4. p-value = (number of permutation max |r| ≥ observed peak |r|) / B.

### Significance thresholds

| Criterion | Threshold | Rationale |
|-----------|-----------|-----------|
| Per-triplet significance | p < 0.10 (one-tailed) | Relaxed from 0.05 due to N=10; reduces false negatives at MVP stage |
| Effect size floor | \|peak r\| ≥ 0.60 | Correlation below 0.60 is unlikely practically meaningful even if "significant" at N=10 |
| Required for PASS | Both p < 0.10 AND \|r\| ≥ 0.60 must hold for the triplet to count as "significant" |

### Why not bootstrap CI?

Bootstrap CI for correlation requires exchangeable residuals, which temporal series violate. Block bootstrap with block length > 1 is infeasible at N=10. Permutation test is the correct nonparametric choice for testing "no temporal association" under the null.

### Implementation note

`analyze_mvp.py` currently selects peak lag by `max(abs(corrs))` without significance testing. The permutation test should be added as a post-processing step; the existing lag selection logic is retained.

---

## 2. "3/3 Reps Consistent" Judgment Rules

### Primary rule: Strict negative lag

A (canary, downstream) pair is **consistent** if and only if:

- All 3 seeds produce peak_lag < 0 (strictly negative), AND
- All 3 seeds pass the significance filter (§1: p < 0.10 and |r| ≥ 0.60).

This matches the existing `analyze_mvp.py` line 215: `all(l < 0 for l in all_lags)`.

### Lag dispersion tolerance

Peak lags need not be identical — only consistently negative. Examples:

| Seed lags | Consistent? | Reason |
|-----------|-------------|--------|
| -2, -1, -3 | ✅ Yes | All negative, spread is acceptable |
| -1, -1, -1 | ✅ Yes | Ideal case |
| -5, -1, -4 | ✅ Yes | Large spread but all negative; flag lag_std for discussion |
| -2, -1, 0 | ❌ No | Lag=0 is not negative; 0 means simultaneous, not leading |
| -2, +1, -1 | ❌ No | One seed shows canary lagging |

### Lag=0 is NOT a lead

Lag=0 indicates simultaneous movement, which does not support the "early warning" hypothesis. Lag=0 is treated as failure for the lead-lag criterion, even though it may indicate co-movement.

### Reporting

For each consistent pair, report: mean lag, lag std, min lag, max lag across seeds. If lag_std > 2.0, flag as "high dispersion — interpret with caution."

---

## 3. Non-Monotonic Indicator Handling (effective_rank)

### Problem

`effective_rank` may exhibit non-monotonic behavior: initial increase (model explores broader representation space early in fine-tuning) followed by decrease (collapse narrows representations). This complicates correlation-based analysis which assumes a consistent directional trend.

### Adopted method: Gen 4–9 linear regression slope

**Rationale:** Generations 0–3 capture the transient fine-tuning adjustment. Generations 4–9 (6 points) capture the steady-state collapse trajectory, which is the regime where early warning matters.

**Procedure:**

1. Fit OLS: `effective_rank ~ β₀ + β₁ · generation` on Gen 4–9 for each seed.
2. If β₁ < 0 in all 3 seeds → collapse direction is "decreasing" → use the standard sign flip in `normalize_for_correlation()`.
3. If β₁ > 0 in all 3 seeds → effective_rank is increasing through Gen 9 → collapse has not manifested in this metric → exclude `effective_rank` from lead-lag analysis and note it in results.
4. If β₁ signs are mixed across seeds → report `effective_rank` as **inconclusive** for this MVP; do not count it toward PASS or FAIL.

### Why not Spearman over the full series?

Spearman rank correlation over 10 points conflates the transient and steady-state regimes. A metric that rises for 3 generations then falls for 7 would show weak Spearman correlation, masking a real late-phase collapse signal.

### Why not "final trend only"?

"Final trend" (e.g., Gen 8→9 direction) is a single difference — too noisy to be reliable. Six points (Gen 4–9) provide a minimal but defensible regression.

### Application to other metrics

If any other canary metric exhibits non-monotonicity (visible in `metric_trends.png`), apply the same Gen 4–9 slope procedure before cross-correlation analysis. Document which metrics required this treatment.

---

## 4. MAUVE Baseline Interpretation

### Known issue

Validation run produced Gen 0 MAUVE = 0.034. Healthy models typically produce MAUVE > 0.8 on standard benchmarks.

### Probable causes (ordered by likelihood)

1. **max_length=256 truncation**: MAUVE computes distributional divergence over full text. 256-token truncation creates artifactual distributional mismatch between generated (which may naturally terminate earlier) and real text (truncated mid-sentence). This is the most likely cause.
2. **Pythia-410m base quality**: A 410M-parameter model without instruction tuning produces lower-quality unconditional generations, especially on WikiText-103's encyclopedic domain.
3. **Prompt/generation mismatch**: If generation uses different prompting strategy than the reference distribution, MAUVE captures this systematic offset rather than collapse-related degradation.

### Floor effect decision rule

**Definition:** MAUVE exhibits a floor effect if:

- Gen 0 MAUVE < 0.10 (already near minimum), AND
- The coefficient of variation across generations CV = std/mean < 0.50 (insufficient relative variation to detect trends).

If BOTH conditions hold across all 3 seeds:

1. **Demote MAUVE** from primary downstream metric to supplementary.
2. **Primary downstream metrics** become: `perplexity`, `distinct_1`, `distinct_2`, `distinct_3`.
3. MAUVE cross-correlation results are still computed and reported but do not count toward PASS/FAIL determination.
4. Log this demotion decision in `analysis_summary.json` with field `"mauve_demoted": true, "mauve_demoted_reason": "floor_effect"`.

### If MAUVE is NOT demoted

If Gen 0 MAUVE ≥ 0.10 or CV ≥ 0.50, retain MAUVE as a primary downstream metric — there is sufficient dynamic range to detect trends.

---

## 5. Graded Verdict System

Each (canary_family, downstream_metric) pair is evaluated independently. The overall verdict aggregates across all pairs.

### Per-pair criteria

| Pair verdict | Conditions |
|-------------|------------|
| **SIGNIFICANT LEAD** | 3/3 seeds: peak_lag < 0, p < 0.10, \|r\| ≥ 0.60 |
| **WEAK LEAD** | 3/3 seeds: peak_lag < 0, but ≥1 seed fails significance (p ≥ 0.10 or \|r\| < 0.60) |
| **NO LEAD** | Any seed has peak_lag ≥ 0 |

### Overall MVP verdict

| Verdict | Required evidence |
|---------|-------------------|
| **STRONG PASS** | ≥2 canary families each have ≥1 SIGNIFICANT LEAD pair against non-demoted downstream metrics |
| **PASS** | ≥1 canary family has ≥1 SIGNIFICANT LEAD pair against a non-demoted downstream metric |
| **CONDITIONAL PASS** | No SIGNIFICANT LEAD pairs exist, but ≥1 canary family has ≥1 WEAK LEAD pair in all 3 seeds. Proceed to Phase 2 with this canary family prioritized but with explicit acknowledgment that MVP evidence is suggestive, not conclusive |
| **FAIL** | No canary family achieves even WEAK LEAD consistency across 3 seeds |

### The 2/3 problem

If 2/3 seeds show a lead but 1/3 does not: this is **NO LEAD** for that pair (not CONDITIONAL PASS). The hypothesis requires consistency across seeds to rule out stochastic artifacts. A 2/3 result may be noted in discussion but does not contribute to the verdict.

**Exception:** If the dissenting seed shows peak_lag = 0 (simultaneous, not reverse), and the other 2 seeds show peak_lag ≤ -2 with p < 0.05, record this as a "near miss" in the report. It does not change the verdict but informs Phase 2 design (e.g., whether more seeds are needed).

### Handling `effective_rank` non-monotonicity

If `effective_rank` is marked **inconclusive** per §3, its pairs are excluded from the verdict entirely (neither helping nor hurting). The verdict is computed over the remaining 3 canary families only. If `effective_rank` is the *only* canary with leads and it is inconclusive, the overall verdict is FAIL (we cannot claim a lead based on an inconclusive metric).

---

## 6. Decision Summary Table

| # | Check | Rule | If TRUE | If FALSE |
|---|-------|------|---------|----------|
| 1 | MAUVE Gen 0 < 0.10 AND CV < 0.50 across all seeds? | §4 floor effect test | Demote MAUVE to supplementary | Retain MAUVE as primary downstream |
| 2 | `effective_rank` Gen 4–9 slope sign consistent across seeds? | §3 slope test | Include in analysis (flip sign if β₁ < 0) | Mark inconclusive, exclude from verdict |
| 3 | For each (canary, downstream) pair: all 3 seeds peak_lag < 0? | §2 strict negative | Pair is a lead candidate | Pair is NO LEAD |
| 4 | For lead candidates: all 3 seeds p < 0.10 AND \|r\| ≥ 0.60? | §1 significance | SIGNIFICANT LEAD | WEAK LEAD |
| 5 | ≥1 canary family has ≥1 SIGNIFICANT LEAD pair? | §5 PASS threshold | **PASS** (or STRONG PASS if ≥2 families) | Go to check 6 |
| 6 | ≥1 canary family has ≥1 WEAK LEAD pair (3/3 consistent)? | §5 CONDITIONAL threshold | **CONDITIONAL PASS** — proceed with caveats | **FAIL** |

### Post-verdict actions

| Verdict | Next step |
|---------|-----------|
| STRONG PASS | Proceed to Phase 2 (synthetic ratio gradient). Prioritize the leading canary families. |
| PASS | Proceed to Phase 2. Expand to more seeds (5 instead of 3) to strengthen evidence. |
| CONDITIONAL PASS | Proceed to Phase 2 with modifications: increase to 20 generations (more statistical power) and 5 seeds. Re-evaluate with the same criteria at Phase 2 completion. |
| FAIL | Revisit canary metric definitions or pivot research direction. Analyze whether collapse itself occurred (check perplexity trajectory); if no collapse happened in 10 generations, the null result is expected and the experiment should be extended. |

---

## Appendix: Implementation Checklist for `analyze_mvp.py`

The current `analyze_mvp.py` implements checks 2–3 and part of check 5 (binary PASS/FAIL). The following additions are needed before final analysis:

- [ ] Add permutation test (§1) to `estimate_lead_time()` or as a wrapper function
- [ ] Add per-seed significance filtering before aggregation
- [ ] Add MAUVE floor effect detection (§4) before cross-correlation
- [ ] Add `effective_rank` monotonicity check (§3) via Gen 4–9 OLS
- [ ] Extend `analysis_summary.json` with graded verdict (§5) and all intermediate decisions
- [ ] Report lag dispersion statistics (mean, std, min, max) per consistent pair
