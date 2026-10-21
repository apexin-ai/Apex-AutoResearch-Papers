# Scale-Stratified IRT Results (2PL+γ, RRF Exposure)

## Configuration
- Model: 2pl_gamma
- Exposure: RRF signal-based (per-model, per-item)
- MCMC: 4 chains, 1000 warmup, 1000 samples, adapt_delta=0.95, seed=42
- D045: 0.5B excluded from MMLU/ARC

## Per-Scale Results

| Scale | Benchmark | N | γ_mean | 95% CI | Rhat | ESS | PPP | rawMAE | calMAE | ΔMAE |
|-------|-----------|---|--------|--------|------|-----|-----|--------|--------|------|
| 0.5B | gsm8k | 7 | 0.6117 | [-0.186, 1.390] | 1.006 | 1332 | 0.163 | 0.0147 | 0.0129 | 0.0018 |
| 1.5B | mmlu | 8 | -0.2986 | [-1.662, 1.035] | 1.009 | 1355 | 0.441 | 0.0078 | 0.0025 | 0.0054 |
| 1.5B | gsm8k | 6 | -0.3487 | [-1.240, 0.517] | 1.006 | 1467 | 0.704 | 0.0128 | 0.0086 | 0.0042 |
| 1.5B | arc_challenge | 6 | 1.1675 | [0.170, 2.205] | 1.006 | 1259 | 0.013 | 0.0074 | 0.0344 | -0.0270 |
| 3B | mmlu | 7 | 0.4512 | [-1.048, 1.918] | 1.007 | 1336 | 0.263 | 0.0065 | 0.0062 | 0.0003 |
| 3B | gsm8k | 7 | 0.4232 | [-0.417, 1.264] | 1.007 | 1447 | 0.245 | 0.1675 | 0.0125 | 0.1550 |
| 3B | arc_challenge | 7 | 0.7577 | [-0.841, 2.361] | 1.006 | 747 | 0.088 | 0.0060 | 0.0251 | -0.0191 |

## Pooled Reference (all scales combined)

| Benchmark | N | γ_mean | 95% CI | PPP | ΔMAE |
|-----------|---|--------|--------|-----|------|
| mmlu | 15 | 0.5172 | [-0.550, 1.597] | 0.234 | 0.0098 |
| gsm8k | 20 | 0.1721 | [-0.289, 0.637] | 0.343 | 0.1552 |
| arc_challenge | 13 | 0.4859 | [-0.255, 1.253] | 0.027 | 0.0183 |

## Key Findings

1. **γ NOT monotonically scale-dependent**: No clean increasing/decreasing trend across 0.5B → 1.5B → 3B.
   - GSM8K γ: 0.5B=0.61, 1.5B=-0.35, 3B=0.42 (non-monotonic)
   - ARC γ: 1.5B=1.17, 3B=0.76 (1.5B > 3B, opposite to expected)

2. **3B GSM8K dominates calibration**: ΔMAE=0.155 for 3B alone ≈ pooled ΔMAE=0.155. The massive calibration improvement in pooled GSM8K comes entirely from 3B models.

3. **Power limitation**: With N=6-8 per stratum, CIs span ~1.5 units on either side. Only 1.5B ARC achieves significance (γ CI excludes 0), but PPP=0.013 indicates poor model fit.

4. **1.5B anomalies**: Negative γ for MMLU/GSM8K is counter-intuitive. Likely noise from small N combined with limited dosage range having RRF exposure.

5. **Convergence excellent**: All fits converged (Rhat ≤ 1.009, min ESS ≥ 747, 0 divergences).

## Interpretation for Paper

The scale-stratified analysis reveals that the IRT contamination parameter γ does not exhibit a clean scale-dependency pattern. This is likely due to:
- Underpowered strata (N=6-8 vs N=23 pooled)
- The contamination effect being benchmark-specific rather than scale-specific
- 3B GSM8K's strong dose-response manifesting as calibration improvement (ΔMAE) rather than a larger γ estimate

**Recommendation**: Report pooled results as primary, with scale-stratified as supplementary showing that 3B drives the GSM8K calibration gains. Do not claim γ is scale-dependent — the evidence does not support this.

## Output Paths
- 0.5B: /root/autodl-tmp/exp006/scale_stratified_irt/scale_0.5B/
- 1.5B: /root/autodl-tmp/exp006/scale_stratified_irt/scale_1.5B/
- 3B: /root/autodl-tmp/exp006/scale_stratified_irt/scale_3B/
