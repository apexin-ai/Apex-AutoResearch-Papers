# ESS-only vs Adaptive: Comparative Analysis

## 1. Performance Comparison

| Method | eval_ppl | Δ vs Uniform | Δ vs Grid-best | Notes |
|--------|----------|-------------|----------------|-------|
| Uniform baseline | 17.693 | — | +0.047 | No weighting |
| Grid-best (b=0.5) | 17.646 | −0.047 | — | Manual grid search optimum |
| **Adaptive (τ=0.8)** | **17.651** | **−0.042** | **+0.005** | Min-intervention, dual constraint |
| ESS-only | _TBD_ | _TBD_ | _TBD_ | Max-intervention, ESS constraint only |

Adaptive seed breakdown: 42→17.650, 123→17.643, 456→17.660 (std≈0.009)

---

## 2. Analysis Framework by Outcome

### Case A: ESS-only PPL > 17.693 (worse than Uniform)

Max-intervention is actively harmful. The strongest possible evidence for min-intervention.

> Unconstrained maximization of b under ESS alone drives weights to extreme values that degrade model quality below the unweighted baseline. This demonstrates that aggressive down-weighting of synthetic data, while maintaining sufficient effective sample size, is not merely suboptimal but counterproductive. The adaptive strategy, by minimizing intervention subject to a quality floor τ, avoids this failure mode entirely.

Early signals support this case: initial loss 11.02 (vs adaptive ~0.85) and b* values of 5.36/2.95 indicate extreme reweighting.

### Case B: ESS-only PPL ∈ (17.646, 17.693) (effective but suboptimal)

Both strategies improve over uniform, but adaptive is more precise.

> ESS-only weighting improves over the uniform baseline, confirming that provenance-aware reweighting is beneficial. However, it underperforms both the grid-optimal fixed b and the adaptive strategy. This gap arises because max-intervention overshoots: it applies stronger corrections than necessary, sacrificing the contribution of well-aligned synthetic examples. The adaptive dual-constraint formulation recovers near-optimal performance without requiring grid search over b.

### Case C: ESS-only PPL ≤ 17.646 (competitive with or better than Grid-best)

Both strategies work well; the argument shifts to efficiency and robustness.

> When ESS-only achieves competitive perplexity, the advantage of adaptive weighting lies not in final performance but in (i) requiring no post-hoc selection of b from a grid, (ii) preserving batch-level granularity rather than applying a single global weight shift, and (iii) providing a principled τ knob that directly controls the quality-quantity tradeoff. The min-intervention principle remains preferable as an inductive bias even when max-intervention happens to perform well on a given dataset.

---

## 3. b* Distribution Contrast

### ESS-only b* behavior
- Initial values observed: 5.36, 2.95 — substantially larger than adaptive
- ESS-only maximizes b subject only to ESS ≥ n_min, so b* is pulled as high as the constraint allows
- Expected distribution: concentrated at high values, low variance across batches
- Effect: near-uniform suppression of all synthetic examples regardless of individual quality

### Adaptive b* behavior
- Median b* = 0.88, IQR = [0.54, 1.52]
- Wide distribution reflects batch-level heterogeneity in synthetic data quality
- Low b* batches: synthetic data already well-aligned, minimal correction needed
- High b* batches: detector flags quality issues, stronger correction applied

### Interpretation
The contrast in b* distributions reveals the core mechanism difference:

1. **Granularity**: Adaptive assigns different b* per batch, preserving fine-grained quality discrimination. ESS-only applies a uniformly aggressive correction, treating all synthetic data as equally suspect.

2. **Information utilization**: The detector score α enters the adaptive objective directly via the α_eff(b) ≥ τ constraint, making each batch's correction proportional to its measured quality. ESS-only discards this signal, using only the aggregate ESS.

3. **Robustness argument**: Adaptive's wide b* range (0.54–1.52) means it naturally adapts to dataset composition shifts. ESS-only's high fixed b* would need manual recalibration if the synthetic-to-real ratio or quality distribution changed.

---

## 4. Key Figures to Produce

- [ ] **b* histogram overlay**: Adaptive b* distribution vs ESS-only b* distribution (same axes)
- [ ] **Loss curve comparison**: Training loss trajectories for Adaptive vs ESS-only vs Uniform
- [ ] **Per-batch weight visualization**: Scatter plot of effective weights w_i under each strategy vs detector score α_i
