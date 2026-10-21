## α_eff Variance Decomposition

### Summary

The correlation between per-batch α_eff and true clean fraction is r≈0.69 (R²≈0.47, simulation with 2000 batches at B=4). The 53% unexplained variance decomposes into two identifiable sources:

| Source | Contribution to gap | Fraction of unexplained | Evidence |
|--------|-------------------|------------------------|----------|
| Detector measurement noise | 0.372 | **70.2%** | R²(oracle)=1.0 vs R²(soft α_eff at b=0)=0.63 |
| Adaptive b-transformation | 0.158 | **29.8%** | R²(soft b=0)=0.63 vs R²(adaptive b*)=0.47 |
| **Total** | **0.529** | **100%** | |

### Methodology

Simulated 2000 random batches of size B=4 from the scored training data (N=371,499; 44.4% real, 55.6% synthetic). For each batch, computed:
- **True clean fraction** from ground-truth depth labels
- **Oracle α_eff** (b=0, perfect q-scores: q=0 for real, q=1 for synthetic) → R²=1.0 by construction
- **Soft α_eff** (b=0, actual q-scores) → R²=0.63
- **Binary fraction** (q<0.5 threshold) → R²=0.55
- **Adaptive α_eff** (b* from Algorithm 1 with τ=0.7) → R²=0.47

### Source 1: Detector Noise (70.2%)

The TF-IDF detector has overall binary accuracy of 85.8% at q=0.5 threshold:
- **False positive rate** (real→synthetic): 19.4% (31,994/164,889 real samples)
- **False negative rate** (synthetic→real): 10.1% (20,830/206,610 synthetic samples)
- 8.8% of samples fall in the boundary zone q∈[0.4,0.6], where accuracy drops to 55.0%
- 4.3% of samples in q∈[0.45,0.55] with accuracy at 52.5% (near random)

This is the dominant source: even the simplest α_eff formulation (b=0, just averaging 1−q_i) already has R²=0.63, losing 37% of variance purely from detector imprecision.

### Source 2: Adaptive b-Transformation (29.8%)

The adaptive algorithm solves for b* such that α_eff(b*)≥τ, which pushes α_eff toward the threshold τ=0.7 for most batches. This compresses the output range and reduces correlation with true composition:
- 93% of B=4 batches have b*>0 (active reweighting)
- Mean b*=0.90 (std=1.55)
- α_eff(adaptive) concentrates around 0.59 vs true fraction mean of 0.44

This is a deliberate design choice: the algorithm trades proxy fidelity for convergence guarantee (α_eff≥τ).

### Batch Size Effect

| Metric | B=4 (empirical) | B=16 (empirical) | Ratio |
|--------|-----------------|-------------------|-------|
| Var(α_eff) | 0.02901 | 0.00283 | **10.25×** |
| Std(α_eff) | 0.1703 | 0.0532 | 3.20× |
| Var(mean_q) | — | — | **4.04×** |
| Mean α_eff | 0.6093 | 0.6764 | — |
| Mean b* | (from sim) | (from sim) | — |

The raw q-score variance ratio (4.04×) matches the theoretical binomial prediction (B₁/B₂ = 16/4 = 4.0). But α_eff variance ratio is 10.25×, exceeding the binomial prediction because the adaptive b-transformation amplifies composition variance nonlinearly.

Simulation R² at B=16: R²(soft)=0.58, R²(adaptive)=0.44 — essentially unchanged from B=4. This confirms that **batch size affects variance, not correlation quality**. The R²≈0.49 is fundamentally limited by detector quality, not by small-batch noise.

### Theoretical Batch Sampling Noise

For ρ̂=0.556 (population synthetic fraction):

| B | Var(batch synth frac) | Std | P(all synthetic) | P(all real) |
|---|----------------------|-----|-------------------|-------------|
| 4 | 0.0617 | 0.248 | 9.57% | 3.88% |
| 8 | 0.0309 | 0.176 | 0.92% | 0.15% |
| 16 | 0.0154 | 0.124 | 0.008% | 0.0002% |
| 32 | 0.0077 | 0.088 | — | — |

With B=4, roughly 13.4% of batches are mono-composition (all-synthetic or all-real), creating extreme α_eff values. With B=16, this drops to <0.01%.

### Interpretation for Reviewers

The 51% unexplained variance does **not** indicate that α_eff fails as a convergence proxy. The decomposition shows:

1. **70% is inherent to any soft detector proxy** — it would exist for any method that uses q-scores instead of ground-truth labels. This is the cost of not having an oracle, shared by all detector-based data selection methods (including detect-and-remove).

2. **30% is the intended behavior of the adaptive algorithm** — b* is chosen to guarantee α_eff≥τ, not to maximize correlation with true fraction. This "saturation" is precisely what provides the convergence guarantee (Theorem 1).

3. **Batch size scaling is as expected** — mean_q variance follows binomial 1/B scaling (ratio=4.04 for B=4→16). The amplified α_eff ratio (10.25×) reflects the nonlinear b-transformation but does not indicate instability.

The relevant metric is not R²(α_eff, true_fraction) but whether α_eff-guided training achieves lower perplexity — which the main experiments confirm (Section 5).

### Raw Data

- Empirical step_metrics: 73,236 steps (B=4, 3 seeds), 18,809 steps (B=16, 3 seeds)
- Simulation: 2,000 batches per batch size, seed=42
- Full JSON: `/root/provenance_weight_training/alpha_eff_variance_decomposition.json`
