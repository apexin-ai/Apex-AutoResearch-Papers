# Binomial Test & Advantage Magnitude Analysis

**Source**: hsweep_h2_seed2 (W&B: jhwyg4tc), Cell A (h=2, step-independent GRPO)

---

## Experiment B: Binomial Test on 52.07% Credit Agreement

### Data

| Parameter | Value |
|-----------|-------|
| n (total windows) | 3000 |
| k (correct-sign windows) | 1562 |
| p̂ (credit agreement rate) | 52.07% |
| Episodes | 128 (65 success, 63 failure) |
| Group size K | 8 |
| Groups | 16 |

### Test 1: H₀: P = 0.5 (random chance)

| Metric | Value |
|--------|-------|
| Exact binomial p-value (two-sided) | **0.0247** |
| Normal approx z-score | 2.264 |
| Significant at α = 0.05? | **YES** |
| Effect size (p̂ − 0.5) | +2.07 pp |

**Interpretation**: The 52.07% credit agreement is statistically distinguishable from 50% random chance (p = 0.025). However, the effect size is trivially small (+2.07 percentage points), meaning the advantage sign carries almost no practical information about episode outcome. The current paper text says "indistinguishable from 50% random chance" — this should be revised to "marginally above 50% (p = 0.025) but with negligible practical significance" or "near-random."

### Wilson 95% CI

| Metric | Value |
|--------|-------|
| Wilson 95% CI | **[0.503, 0.539]** |
| Contains P = 0.5? | **NO** (lower bound 0.503) |
| Contains P = 0.191? | **NO** |

### Test 2: H₀: P = 0.191 (binary reward theory, Proposition 2)

| Metric | Value |
|--------|-------|
| Expected k under H₀ | 573 |
| Observed k | 1562 |
| Normal approx z-score | **45.9** |
| p-value | **< 10⁻¹⁰⁰** (essentially zero) |

**Interpretation**: The empirical 52.07% is overwhelmingly different from the binary-reward theoretical prediction of 19.1% (z = 45.9). This confirms that the penalty reward (−0.1 per invalid action) substantially shifts the credit agreement rate, as discussed in the appendix. The gap is expected: the binary theory assumes r ∈ {0, r₊}, but the penalty creates within-group variance even among failed episodes, allowing some windows to receive positive advantages by being "less bad."

### Summary Table for Paper

```
Credit agreement rate: 52.07% (1562/3000 windows)
Wilson 95% CI:         [50.3%, 53.9%]

vs H₀ = 50.0% (random):  p = 0.025, z = 2.26
  → Statistically significant but trivially small effect (+2.07 pp)

vs H₀ = 19.1% (binary theory): p ≈ 0, z = 45.9
  → Overwhelmingly rejects binary theory; penalty reward explains the gap
```

### Recommended Paper Language

Current: "52.07% under step-independent training (h=2), **indistinguishable** from 50% random chance."

Suggested revision: "52.07% under step-independent training (h=2), 95% CI [50.3%, 53.9%], marginally above random chance (binomial test p = 0.025) but with negligible practical significance—the advantage sign carries at most 2 percentage points of information beyond coin-flip. This is consistent with the prediction of Proposition 2 under penalty reward (Appendix A.2) and far below the level required for convergent learning."

---

## Experiment C: Advantage Magnitude Distribution

### Data Available

From `advantage_analysis_summary.json` on bjb1-17606. Per-window advantages from 3000 windows, already GRPO-normalized (group mean subtracted, divided by group std).

### Mean Advantage by Episode Outcome

| Group | N windows | Mean Â | Std Â |
|-------|-----------|--------|-------|
| Successful episodes | 1608 | +0.000734 | 0.03670 |
| Failed episodes | 1392 | −0.005438 | 0.01818 |

### Magnitude Ratio

| Metric | Value |
|--------|-------|
| \|mean(Â_fail)\| / \|mean(Â_success)\| | **7.41** |
| Theoretical K−1 | **7** |
| Match? | Yes (within 6%) |

### Interpretation

The ratio |mean_fail| / |mean_success| = 7.41 is close to K−1 = 7, but this requires careful interpretation:

**What the paper claims (Eq. 6 context)**: "In a group with one success and K−1 failures, the successful rollout's normalized advantage scales as ~(K−1) times larger than each failed rollout's." This is the m=1 special case where |Â_success|/|Â_fail| = (K−1)/1 = 7.

**What the empirical 7.41 measures**: The ratio of *mean* advantages aggregated across ALL groups and ALL m values, weighted by number of windows. This is a different quantity than the per-group ratio.

**Per-group theoretical analysis** (at p_episode = 50.78%):

| m (successes) | P(m) | \|Â_s\|/\|Â_f\| = (K−m)/m |
|---------------|------|---------------------------|
| 1 | 0.028 | 7.000 |
| 2 | 0.103 | 3.000 |
| 3 | 0.212 | 1.667 |
| 4 | 0.273 | 1.000 |
| 5 | 0.226 | 0.600 |
| 6 | 0.116 | 0.333 |
| 7 | 0.034 | 0.143 |

Weighted average per-group |Â_s|/|Â_f| = **1.32** (not 7).

The empirical aggregate ratio of 7.41 arises from the aggregation across groups, not from the m=1 case dominating. The total negative advantage mass (1392 × 0.005438 = 7.57) is ~6.4× the total positive mass (1608 × 0.000734 = 1.18), reflecting asymmetry in how GRPO normalization distributes signal when window counts vary across episodes.

### Additional Statistics

| Metric | Value |
|--------|-------|
| P(Â > 0 \| success episode) | 37.06% |
| P(Â > 0 \| failure episode) | 30.60% |
| Point-biserial r (advantage vs outcome) | 0.068 |
| p-value of correlation | 1.94 × 10⁻⁴ |
| Distribution overlap | 87.85% |
| Avg windows/episode (success) | 24.7 |
| Avg windows/episode (fail) | 22.1 |

### Key Takeaway for Paper

The magnitude data supports the "comparable magnitude" claim in a weak sense: the distributions of advantages for successful and failed episodes overlap by 88%, and even within successful episodes, only 37% of advantages are positive. The mean advantages are extremely small relative to their standard deviations (success: mean/std = 0.02; fail: mean/std = 0.30), confirming that GRPO normalization effectively destroys the signal at the per-window level.

The K−1 = 7 ratio claim should be stated as applying to the m=1 case specifically, not as a general property. The aggregate |mean_fail|/|mean_success| = 7.41 happens to be numerically close to K−1 but arises from a different mechanism (cross-group aggregation with unequal window counts).

---

*Generated 2026-05-23. Data from hsweep_h2_seed2 training run on bjb1-17606.*
