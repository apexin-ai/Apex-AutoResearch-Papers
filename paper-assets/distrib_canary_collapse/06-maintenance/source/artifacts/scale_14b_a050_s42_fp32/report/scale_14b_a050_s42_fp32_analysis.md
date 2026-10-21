# 5-Method Lead-Lag Analysis: scale_14b_a050_s42_fp32

## Experiment Configuration
| Parameter | Value |
|-----------|-------|
| Model | EleutherAI/pythia-1.4b |
| Dataset | WikiText-103 (5000 samples) |
| Seed | 42 |
| Precision | fp32 |
| Alpha (synthetic ratio) | 0.50 |
| Generations | 10 (gen_0 = baseline, gen_1..10 = iterative) |
| Steps/gen | 5000 |
| Batch size | 4 |
| Learning rate | 5e-5 |
| top_p | 0.95 |
| PermG n_perm | 5000 |

## Per-Generation Metrics

| Gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | mauve | eff_rank |
|-----|--------------|------|------------|------------|------------|------------|-------|----------|
| 0 | 2.946 | 0.007 | 19.68 | 0.1003 | 0.5242 | 0.8218 | 0.0308 | 50.76 |
| 1 | 2.127 | 0.105 | 20.76 | 0.0982 | 0.5186 | 0.8151 | 0.0316 | 75.06 |
| 2 | 2.114 | 0.129 | 25.46 | 0.0842 | 0.4409 | 0.7279 | 0.0329 | 82.75 |
| 3 | 2.158 | 0.130 | 26.58 | 0.0779 | 0.3943 | 0.6615 | 0.0311 | 83.54 |
| 4 | 2.141 | 0.138 | 28.60 | 0.0742 | 0.3625 | 0.6017 | 0.0314 | 82.59 |
| 5 | 2.146 | 0.144 | 30.23 | 0.0722 | 0.3399 | 0.5556 | 0.0320 | 83.10 |
| 6 | 2.133 | 0.150 | 31.69 | 0.0713 | 0.3306 | 0.5379 | 0.0306 | 84.26 |
| 7 | 2.182 | 0.147 | 32.40 | 0.0706 | 0.3235 | 0.5238 | 0.0279 | 83.08 |
| 8 | 2.187 | 0.149 | 33.24 | 0.0701 | 0.3189 | 0.5150 | 0.0307 | 82.59 |
| 9 | 2.198 | 0.154 | 34.82 | 0.0698 | 0.3160 | 0.5083 | 0.0303 | 83.92 |
| 10 | 2.192 | 0.157 | 35.18 | 0.0696 | 0.3146 | 0.5054 | 0.0310 | 83.42 |

## Drift Statistics (gen_0 to gen_10)

| Metric | gen_0 | gen_10 | Delta | % Change |
|--------|-------|--------|-------|----------|
| token_entropy | 2.946 | 2.192 | -0.754 | -25.6% |
| ece | 0.007 | 0.157 | +0.150 | +2118% |
| perplexity | 19.68 | 35.18 | +15.49 | +78.7% |
| distinct_1 | 0.100 | 0.070 | -0.031 | -30.6% |
| distinct_2 | 0.524 | 0.315 | -0.210 | -40.0% |
| distinct_3 | 0.822 | 0.505 | -0.316 | -38.5% |
| mauve | 0.031 | 0.031 | +0.000 | +0.6% |
| eff_rank | 50.76 | 83.42 | +32.66 | +64.3% |

Key pattern: token_entropy drops sharply at gen_1 (2.946 to 2.127, -27.8%) then stabilizes. ECE and eff_rank also jump at gen_1. Perplexity increases gradually and steadily. Distinct_1/2/3 decrease monotonically. Mauve is flat (always near 0.031).

## 5-Method Lead-Lag Results

### Per-Pair Results

#### 1. token_entropy -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=-0.933, lag=5 | 0.0066 | - | lag>0 (reverse) | No |
| Diff XCorr | r=-0.943, lag=5 | 0.0163 | 0.0186 | lag>0 (reverse) | No |
| Threshold 3sigma | onset: c=1, d=10, lead=9 | - | - | forward | Yes |
| PermG fwd | F=27.01 | 0.0554 | 0.1477 | - | No |
| PermG rev | F=2.46 | 0.1804 | 0.5714 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 2. token_entropy -> distinct_1
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=-0.957, lag=5 | 0.0027 | - | lag>0 (reverse) | No |
| Diff XCorr | r=-0.955, lag=5 | 0.0112 | 0.0150 | lag>0 (reverse) | No |
| Threshold 3sigma | onset: c=1, d=None | - | - | no d_onset | No |
| PermG fwd | F=424.85 | 0.0784 | 0.1568 | - | No |
| PermG rev | F=0.84 | 0.4285 | 0.5714 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 3. distinct_1 -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=0.974, lag=5 | 0.0010 | - | lag>0 (reverse) | No |
| Diff XCorr | r=0.880, lag=0 | 0.0008 | 0.0061 | lag=0 (contemp.) | No |
| Threshold 3sigma | onset: c=None, d=10 | - | - | no c_onset | No |
| PermG fwd | F=1.08 | 0.2543 | 0.3391 | - | No |
| PermG rev | F=0.36 | 0.3987 | 0.5714 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 4. ece -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=0.975, lag=2 | 0.000008 | - | lag>0 (reverse) | No |
| Diff XCorr | r=0.881, lag=-1 | 0.0017 | 0.0045 | lag<0 (forward) | Yes |
| Threshold 3sigma | onset: c=3, d=10, lead=7 | - | - | forward | Yes |
| PermG fwd | F=28.62 | 0.0376 | 0.1504 | - | No |
| PermG rev | F=3.34 | 0.1318 | 0.5714 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 5. distinct_2 -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=0.976, lag=-2 | 0.000007 | - | lag<0 (forward) | Yes |
| Diff XCorr | r=0.841, lag=0 | 0.0023 | 0.0061 | lag=0 (contemp.) | No |
| Threshold 3sigma | onset: c=None, d=10 | - | - | no c_onset | No |
| PermG fwd | F=0.15 | 0.6635 | 0.7583 | - | No |
| PermG rev | F=0.00 | 0.9890 | 0.9890 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 6. distinct_3 -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=0.986, lag=-2 | 0.000001 | - | lag<0 (forward) | Yes |
| Diff XCorr | r=0.758, lag=0 | 0.0110 | 0.0150 | lag=0 (contemp.) | No |
| Threshold 3sigma | onset: c=None, d=10 | - | - | no c_onset | No |
| PermG fwd | F=0.02 | 0.9190 | 0.9190 | - | No |
| PermG rev | F=0.01 | 0.8894 | 0.9890 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 7. mauve -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=0.596, lag=1 | 0.0691 | - | lag>0 (reverse) | No |
| Diff XCorr | r=-0.844, lag=-4 | 0.0347 | 0.0397 | lag<0 (forward) | Yes |
| Threshold 3sigma | onset: c=None, d=10 | - | - | no c_onset | No |
| PermG fwd | F=0.90 | 0.3893 | 0.4462 | - | No |
| PermG rev | F=1.40 | 0.2713 | 0.5714 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

#### 8. effective_rank -> perplexity
| Method | Statistic | p-value | p_FDR | Direction | Significant (for K) |
|--------|-----------|---------|-------|-----------|-------------------|
| Naive XCorr | r=-0.806, lag=-4 | 0.0285 | - | lag<0 (forward) | Yes |
| Diff XCorr | r=-0.842, lag=-1 | 0.0044 | 0.0070 | lag<0 (forward) | Yes |
| Threshold 3sigma | onset: c=None, d=10 | - | - | no c_onset | No |
| PermG fwd | F=22.41 | 0.0518 | 0.1477 | - | No |
| PermG rev | F=1.25 | 0.3521 | 0.5714 | - | No |
| TY Granger | - | - | - | insufficient obs | No |

### Summary

| Method | Significant pairs (fwd, direction-filtered) |
|--------|---------------------------------------------|
| PermG (FDR) | 0/8 |
| TY Granger | 0/8 (all insufficient obs) |
| Diff XCorr (FDR + lag<0) | 3/8 (ece->ppl, mauve->ppl, eff_rank->ppl) |
| Naive XCorr (lag<0) | 3/8 (distinct_2->ppl, distinct_3->ppl, eff_rank->ppl) |
| Threshold Onset 3sigma | 2/8 (token_entropy->ppl, ece->ppl) |

| PermG reverse (false positive control) | 0/8 (as expected) |

**Consensus K-votes:**

| Pair | K | Methods |
|------|---|---------|
| token_entropy -> perplexity | 1/5 | thresh3s |
| token_entropy -> distinct_1 | 0/5 | - |
| distinct_1 -> perplexity | 0/5 | - |
| ece -> perplexity | 2/5 | diff, thresh3s |
| distinct_2 -> perplexity | 1/5 | naive |
| distinct_3 -> perplexity | 1/5 | naive |
| mauve -> perplexity | 1/5 | diff |
| effective_rank -> perplexity | 2/5 | naive, diff |

**K>=3: 0/8, K>=4: 0/8**

### Cross-Scale Comparison

| Metric | 410M alpha=0.50 (ref) | 1.4B alpha=0.50 s42 (this) | 1.4B alpha=1.0 s42 | 1.4B alpha=1.0 s43 | 1.4B C4 alpha=1.0 s42 |
|--------|----------------------|---------------------------|--------------------|--------------------|----------------------|
| PermG fwd | 6/8 | **0/8** | 2/8 | 6/8 | 8/8 |
| TY Granger | 4/8 | 0/8 | - | - | - |
| K>=3 | - | **0/8** | 3/8 | 3/8 | 8/8 |
| K>=4 | 6/8 | **0/8** | - | - | - |

### Notes

1. **TY Granger failure**: All 8 pairs returned insufficient observations. T=11 with d_max augmentation leaves too few degrees of freedom for the VAR model.

2. **XCorr lag anomaly**: Several pairs (token_entropy->ppl, token_entropy->d1, d1->ppl) show peak xcorr at lag=+5 (maximum positive lag), indicating downstream metrics nominally "lead" the canary. This is an artifact of the sharp gen_0->gen_1 transition in token_entropy (-27.8%) followed by stabilization, while perplexity/distinct_1 drift gradually. The correlation is real but the lag structure reflects smoothness differences, not true temporal causation.

3. **PermG borderline signals**: ece->ppl raw p=0.0376 (significant before FDR), token_entropy->ppl p=0.0554, eff_rank->ppl p=0.0518. These borderline signals suggest very weak lead-lag that does not survive multiple testing correction.

4. **Threshold onset pattern**: Only token_entropy (onset=gen_1) and ece (onset=gen_3) breach 3-sigma threshold. Most other canary metrics (distinct_1/2/3, mauve, eff_rank) never cross 3-sigma, though they show sustained monotonic drift. Perplexity onset = gen_10 (last generation).

## Conclusion

**NEGATIVE.** Pythia-1.4B at alpha=0.50 does NOT show statistically detectable lead-lag causation from canary metrics to perplexity.

- PermG_fwd = 0/8 (FDR-corrected), with no pair reaching K>=3 consensus
- The 410M model at the same alpha=0.50 shows PermG=6/8 and K>=4=6/8
- This demonstrates that **the onset detection boundary shifts upward with model scale**: larger models require stronger contamination (higher alpha) before the lead-lag signal becomes detectable
- Even at alpha=1.0 on WikiText, 1.4B results are inconsistent across seeds (PermG 2/8 vs 6/8), whereas 1.4B on C4 at alpha=1.0 gives PermG=8/8

The model collapse itself is unambiguous (perplexity +79%, distinct_1 -31%), but the causal lead-lag structure from canary to downstream metrics is too weak to detect at this contamination level for 1.4B-scale models.