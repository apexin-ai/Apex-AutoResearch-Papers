# C3: Extreme BCS Batch Sample Size Investigation

## 1. Per-BCS-Level Batch Count

### Figure 1b / Table 2 Data Points

| Pool Size | Count | Low-BCS Acc | High-BCS Acc | Δ (pp) | **N per group** | Method | 95% CI |
|-----------|-------|-------------|--------------|--------|-----------------|--------|--------|
| 16-rel | 8 | 88.9% | 79.8% | 9.1 | **1** | Greedy single batch | --- |
| 40-rel (80-pool) | 8 | 83.3% | 50.0% | 33.3 | **1** | Greedy single batch | not reported |
| 80-rel | 8 | 82.3% | 51.0% | 31.2 | **1** | Greedy single batch | [17.7, 42.7] |
| 80-rel | 16 | 82.8% | 51.6% | 31.2 | **1** | Greedy single batch | [22.9, 39.6] |

**Confirmed N=1 per group for all Figure 1b data points.**

### Evidence trail

- **80-rel**: `eval_exp2.json` contains `count_8_low_bcs` (acc=0.8229, BCS=0.4715, n=96 instances) and `count_8_high_bcs` (acc=0.5104, BCS=0.9706, n=96 instances). Single greedy-constructed batches.
- **40-rel**: Worker analysis (`worker_analysis_exp_fewrel_40rel_r4`) confirms `count_8_low_bcs=0.833, count_8_high_bcs=0.500`, same greedy construction.
- **16-rel**: No CI reported ("---"), consistent with N=1. Values (0.889, 0.798) do not match integer fractions of 96 (80-rel instance count), suggesting different instance count (~496 = 8 types × 62 instances/type for 16-rel pool with 1000 samples).
- **Paper text** (results.tex line 52): Explicitly states "based on a single extreme batch per BCS level at 16-rel scale."

### CI Methodology (Critical Finding)

The 95% CIs ([17.7, 42.7] and [22.9, 39.6]) are **instance-level bootstrap CIs**, NOT batch-level replications.

Source: `bootstrap_ci.py` lines 249-291:
```python
low_arr = np.array([1] * c_low + [0] * (n_low - c_low))  # binary correct/incorrect
high_arr = np.array([1] * c_high + [0] * (n_high - c_high))
for i in range(n_boot):
    bl = low_arr[rng.randint(0, n_low, size=n_low)]  # resample instances
    bh = high_arr[rng.randint(0, n_high, size=n_high)]
    boot_deltas[i] = bl.mean() - bh.mean()
```

- count_8: resamples 96 instances (8 types × 12) per batch
- count_16: resamples 192 instances (16 types × 12) per batch
- Captures: test-instance sampling variance
- **Does NOT capture**: variance from batch composition (which types are selected)

## 2. Available Multi-Batch Evidence (Already in Paper)

The paper does NOT rely solely on N=1 comparisons. Existing multi-batch evidence:

| Evidence | N | Effect | Significance | Paper location |
|----------|---|--------|-------------|----------------|
| 100-batch regression (16-rel pool) | 100 | slope=-0.509, R²=0.218 | p=9.6e-7 | §4.3 "Practical magnitude" |
| 100-batch regression (80-pool-16sub) | 100 | slope=-0.401, R²=0.049 | p=0.027 | §4.3 "Practical magnitude" |
| Quartile comparison (16-rel) | 25 vs 25 | Δ=-5.3pp | CI: [-7.4, -3.2] | §4.3 |
| Quartile comparison (80-pool-16sub) | 25 vs 25 | Δ=-3.9pp | CI: [-8.2, 0.4] | §4.3 |
| 25v25 BCS-controlled (v2 prompt) | 25 vs 25 | Δ=-25.5pp, r=-0.919 | p<0.001 | §4.3 "Prompt sensitivity" |
| 5v5 BCS-controlled (fewrel_v2_bcs) | 5 vs 5 | Δ=7.92pp | CI: [-5.21, 21.46] (**n.s.**) | Not in main text |
| D035 extreme-5 (16-rel) | 5 vs 5 | Δ=11.65pp | CI: [5.2, 14.8] | Appendix |
| D035 extreme-5 (80-pool-16sub) | 5 vs 5 | Δ=9.79pp | CI: [1.5, 17.7] | Appendix |

### Key observation

The 5v5 BCS-controlled comparison (N=5 per group, same 80-rel pool) gives Δ=7.92pp with CI crossing zero — **not statistically significant**. This is because the 5 "low" and 5 "high" batches have overlapping BCS ranges (low: 0.47–0.67, high: 0.78–0.97), and high_3 is an outlier (acc=0.9271 despite BCS=0.82).

The 25v25 comparison IS significant (Δ=25.5pp) because it uses more carefully constructed batches with tighter BCS separation.

## 3. Severity Assessment

### Not as catastrophic as feared

The paper's evidence structure is layered:

1. **Primary quantitative evidence**: 100-batch BCS–accuracy regression (R²=0.218, p<0.001). This is robust, based on 100 independent random batches with continuous BCS variation.
2. **Confirming evidence**: Quartile comparisons (N=25 per group), within-pool slope consistency (permutation p=0.60), cross-model replication.
3. **Illustrative evidence**: Single extreme-batch comparison showing the maximum possible gap when BCS is pushed to its extremes.

The paper already acknowledges the single-batch nature (results.tex line 52). The primary claim is R²=0.218, not the 31.2pp extreme gap.

### Genuine concerns

1. **Figure 1b visual weight exceeds its statistical weight.** A bar chart with N=1 per bar communicates certainty that doesn't exist. Readers will interpret each bar as a mean with replication.
2. **CI misinterpretation risk.** The CIs reflect instance-level variance, not batch-level generalizability. A reader seeing "[17.7, 42.7]" would assume "any low-BCS batch vs any high-BCS batch yields 17–43pp gap." The 5v5 data shows this is NOT the case.
3. **40-rel and 80-rel share extreme batches.** The greedy high-BCS batch uses the same types (participant, participant of, part of, member of, follows, followed by, has part, instance of) across pool sizes. The "scaling" from 40-rel to 80-rel is partially an artifact of using the same extreme types.
4. **16-rel has no CI at all.** The "---" entry in the table suggests the authors recognized the N=1 limitation but didn't address it.

## 4. Improvement Recommendations

### A. If keeping Figure 1b as-is (minimal change)

1. Add a footnote: "Each bar represents a single greedy-constructed batch. CIs reflect test-instance bootstrap, not batch-level replication."
2. Add error bars from the D035 extreme-5 analysis or quartile comparison to show batch-level variance.

### B. Generating more extreme batches (if time permits)

**Feasibility**: For 80-rel pool, count_8 → C(80,8) ≈ 28 billion possible batches. Can sample many near-extreme batches:

```
Method: Fix BCS threshold, randomly sample type subsets meeting the threshold
- Low BCS: sample 10-20 batches with BCS < Q10 of random distribution
- High BCS: sample 10-20 batches with BCS > Q90 of random distribution
- Run evaluation on each → compute group-level CI
```

Estimated N achievable:
- Low extreme: ~10-20 batches (many dissimilar combinations exist)
- High extreme: ~5-10 batches (fewer maximally similar combinations)
- This would give adequate power for a two-sample t-test

### C. Reframing (recommended)

1. **Lead with the 100-batch regression** as primary evidence (already does this in §4.3 "Practical magnitude")
2. **Replace Figure 1b** with a BCS-accuracy scatter plot showing all 100 batches + regression line + CI band
3. **Demote extreme-batch comparison** to supplementary/appendix as an illustrative example
4. **Report the 25v25 comparison** (Δ=25.5pp, r=-0.919) as the primary "interventional" evidence

### D. For the 16-rel gap specifically

The 16-rel 100-batch bootstrap data exists on the server. Can compute:
- Extreme-5 mean comparison: Δ=11.65pp, CI=[5.2, 14.8] (already computed in D035)
- This is a legitimate N=5 comparison and should replace the N=1 value in the table

## 5. Impact on Paper Evidence Structure

### Current claim pathway
```
Pairwise SCS-confusion (r=0.11-0.13) → Batch-level BCS-accuracy (R²=0.22) → Extreme-batch gap (31.2pp)
```

### Validity of each link
- **Link 1** (pairwise): Robust, n=1953/11026 pairs, bootstrap CIs exclude zero. ✅
- **Link 2** (batch regression): Robust, n=100 batches, continuous predictor. ✅
- **Link 3** (extreme gap): N=1, instance-level CI only. ⚠️ Overstates certainty.

### Recommendation
The evidence structure is sound if Link 3 is reframed as illustrative. The R²=0.218 regression IS the main evidence. The extreme-batch comparison shows what happens at the BCS distribution tails, not the typical effect.

The typical effect is the IQR-based gap: **2.2pp** (CI: [0.4, 4.0]) — modest but real, and well-supported by 100 batches.

## 6. Statistical Power Analysis

### N=1 group comparison
- No meaningful between-batch effect size or power calculation is possible
- Instance-level bootstrap CI answers: "Is the accuracy difference significant for THESE two specific batches?" → Yes
- Cannot answer: "Would any low-BCS batch vs any high-BCS batch show a similar gap?" → Unknown

### Effect size from multi-batch data
- 5v5 comparison: Cohen's d = 0.52 (medium), but CI crosses zero
- 25v25 comparison: Cohen's d = 5.1 (very large), highly significant
- 100-batch regression: f² = 0.28 (large effect for regression)

### Power for detecting the regression effect
- With R²=0.218, n=100: power > 0.99 at α=0.05
- The regression evidence is fully powered. No concern here.
