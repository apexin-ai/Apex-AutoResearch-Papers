# Contamination Rate Sweep: Literature Alignment Analysis

## 1. Dose-Response Pattern

Our finding that binary filtering advantage increases monotonically with contamination rate (HellaSwag: +0.57pp@10% → +1.18pp@50%) aligns with the broader literature:

- **Du et al. (2025)** show models tolerate ≤20% synthetic data but degrade rapidly beyond 30%, with degradation accelerating at higher proportions. Our sweep confirms this accelerating-harm pattern: the *marginal benefit* of filtering grows as contamination increases, consistent with superlinear degradation.
- **Dohmatob et al. (ICLR 2025, "Strong Model Collapse")** prove even a small constant fraction of synthetic data is asymptotically detrimental. Our results add empirical granularity: the damage is not just present but dose-dependent in downstream task terms.
- **Bakshi & Chakraborty (2026)** formalize how mixture weights control long-term performance under iterative contamination. Their framework predicts that maintaining non-trivial real-data weight avoids collapse, which maps to our binary filter preserving the real-data fraction at each contamination level.

**Verdict: Consistent.** No prior work reports the exact sweep we ran (systematic contamination rate × filtering strategy matrix), but the monotonic dose-response pattern is predicted by theory.

## 2. Binary vs Graduated/Weighted Filtering

Our most surprising result is that graduated filtering ≈ no_filter across all contamination rates. The literature is mixed:

- **Drayson et al. (EMNLP 2025)** use SIR (soft importance resampling) based on binary detection scores. Their weighting is continuous, but the underlying signal is binary (human vs machine). They never test ordinal/graduated depth signals, so no direct comparison exists.
- **Kuo et al. (ICLR 2025, "Not All LLM-Generated Data Are Equal")** find weighted-loss outperforms binary decisions for text classification with synthetic data. However, their setting differs fundamentally: they weight by quality within a single generation, not by generational depth across recursive generations.
- **He et al. (2025, "Golden Ratio Weighting")** derive theoretically optimal real-data weights that prevent collapse. Their weighting is on the real/synthetic axis, not depth-graduated. The golden ratio result applies to the mixing proportion, not to within-synthetic stratification.
- **Nait Saada et al. (2025, "The Data-Quality Illusion")** show that aggressive classifier-based filtering can hurt, suggesting filtering captures classifier artifacts rather than genuine quality. This partially explains why our graduated weighting (which assigns intermediate weights to depth-1 vs depth-2+ data) fails: if depth-1 and depth-2+ are already near-indistinguishable in feature space (our K*=2 finding), graduated weights based on noisy depth estimates add no signal.

**Verdict: Novel finding.** No paper has compared binary vs depth-graduated filtering for contamination. The failure of graduated filtering is best explained by our own K*=2 result: once depth≥1 features converge, graduated weighting on depths >1 is weighting on noise.

## 3. 100% Binary Filtering Limitation

At 100% contamination, binary filtering removes all data (trivially unusable). Literature context:

- **Amin et al. (NeurIPS 2025)** show even minimal curation (β>0 correct fraction) suffices for convergence, implying you need *some* data to train on. The 100% removal edge case is the degenerate β=0 scenario.
- **Kazdan et al. (ICML 2025)** show the accumulate regime avoids collapse because real data fraction never hits zero. Our 100% contamination scenario is the extreme replace regime where no real data exists.
- No paper explicitly discusses the "filter everything" failure mode, but it follows trivially from any filtering framework.

**Verdict: Expected limitation, not novel.** Worth noting in the paper as a practical boundary condition but not a contribution.

## 4. Key Gaps We Fill

| Gap | Our Contribution |
|-----|-----------------|
| No systematic contamination-rate × filtering-strategy sweep | First empirical matrix (5 rates × 3 strategies) |
| No comparison of binary vs depth-graduated filtering | Show graduated ≈ no_filter, explained by K*=2 |
| Dose-response mostly theoretical (Gaussian/linear) | Empirical dose-response on LLM downstream tasks (HellaSwag, ARC-C) |
| Weighting literature assumes meaningful quality gradation | Our K*=2 shows the gradation signal vanishes past depth 1 |

## 5. Papers to Add to Literature Map

- **Du et al. (2025)** "Characterizing Model Behavior Under Synthetic Data Training" — dose-response curves across scales and mixing ratios
- **He et al. (2025)** "Golden Ratio Weighting Prevents Model Collapse" — theoretical optimal weighting scheme
- **Bakshi & Chakraborty (2026)** "From Collapse to Improvement" — statistical framework for iterative contaminated training
- **Nait Saada et al. (2025)** "The Data-Quality Illusion" — challenges classifier-based quality filtering
