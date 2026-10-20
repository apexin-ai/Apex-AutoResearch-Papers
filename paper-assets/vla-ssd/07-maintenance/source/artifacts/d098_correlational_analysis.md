# D098: Correlational Analysis — R² Exit Collapse vs Published Success Rate

## 1. Data Sources

**R² Δ (trained)**: Peak R² − exit R² from SSD probing experiments on trained VLA models.

**Published success rates**:
- OpenVLA (finetuned): Table 5 in TraceVLA paper (Zheng et al., arXiv 2412.10345v2), reporting OpenVLA finetuned baseline on LIBERO
- TraceVLA (finetuned): Table 5 in TraceVLA paper (Zheng et al., arXiv 2412.10345v2)
- NORA (finetuned, no action chunking): Table 2 in NORA paper (Hung et al., arXiv 2504.19854v1)

## 2. Combined Data Table

| Arch | Suite | R² Δ (trained) | Published SR (%) | Source |
|------|-------|----------------|-------------------|--------|
| OpenVLA | Goal | 0.016 | 70.4 | TraceVLA Table 5 |
| OpenVLA | Object | 0.121 | 83.8 | TraceVLA Table 5 |
| OpenVLA | Long | 0.004 | 45.7 | TraceVLA Table 5 |
| TracVLA | Goal | 0.228 | 75.1 | TraceVLA Table 5 |
| TracVLA | Spatial | 0.138 | 84.6 | TraceVLA Table 5 |
| TracVLA | Object | 0.294 | 85.2 | TraceVLA Table 5 |
| TracVLA | Long | 0.198 | 54.1 | TraceVLA Table 5 |
| NORA | Goal | 0.691 | 77.0 | NORA Table 2 |
| NORA | Spatial | 0.302 | 85.6 | NORA Table 2 |

Excluded: OpenVLA-Spatial (no exit R² data available), NORA-Object/Long (no R² data).

## 3. Spearman Rank Correlation

| Metric | Value |
|--------|-------|
| n | 9 |
| Spearman ρ | **0.583** |
| p-value | **0.099** |
| Significant at α=0.05? | No |
| Pearson r (reference) | 0.362, p=0.339 |

**Result**: Positive but non-significant trend. The direction suggests models/suites with larger exit collapse tend to have higher success rates, but the evidence does not reach conventional significance.

## 4. Subgroup Analyses

### 4.1 Within-Architecture

| Arch | n | Spearman ρ | p |
|------|---|------------|---|
| OpenVLA | 3 | 1.000 | <0.001 |
| TracVLA | 4 | 0.400 | 0.600 |
| NORA | 2 | — | (too few) |

Within OpenVLA, R² Δ and SR are perfectly rank-correlated (Long < Goal < Object for both metrics). Within TracVLA, the relationship is weak — the Long suite breaks the monotonic pattern (highest R² Δ after Object, but lowest SR).

### 4.2 Within-Suite (Cross-Architecture)

| Suite | Architectures | R² Δ → SR | Pattern |
|-------|--------------|-----------|---------|
| Goal | OpenVLA(0.016,70.4) → TracVLA(0.228,75.1) → NORA(0.691,77.0) | ρ=1.0 (n=3) | Monotonic positive |
| Spatial | TracVLA(0.138,84.6) → NORA(0.302,85.6) | n=2 | Consistent direction |
| Object | OpenVLA(0.121,83.8) → TracVLA(0.294,85.2) | n=2 | Consistent direction |
| Long | OpenVLA(0.004,45.7) → TracVLA(0.198,54.1) | n=2 | Consistent direction |

All within-suite comparisons show the same direction: higher R² Δ ↔ higher SR. Goal suite (the only one with n=3) yields perfect rank correlation.

### 4.3 Sensitivity to NORA Variant

| NORA variant used | Spearman ρ | p |
|-------------------|------------|---|
| Base (no AC) | 0.583 | 0.099 |
| With Action Chunking | 0.583 | 0.099 |
| NORA-Long (AC) | 0.800 | 0.010 |

Using the NORA-Long variant (SR: Goal=89.4%, Spatial=92.2%) strengthens the correlation to significance, but this may reflect cherry-picking the strongest model variant.

## 5. Interpretation

### What the data suggests

The positive direction (ρ ≈ 0.58) is consistent across every within-suite comparison: architectures with larger R² exit collapse on a given suite also achieve higher task success rate. This pattern is suggestive of a functional connection — models that develop stronger mid-network spatial representations (producing a higher peak) and then compress them more aggressively at exit layers may be performing a more effective abstraction from perception to action.

### Why it does not reach significance

1. **Small n**: With only 9 data points (and 3 architectures), statistical power is limited.
2. **Architecture confound**: NORA has both the highest R² Δ and generally high SR, but this could be driven by model capacity (3B params, better backbone) rather than representational dynamics per se.
3. **Suite difficulty confound**: Long-horizon suites consistently have lower SR AND lower R² Δ (especially for OpenVLA), creating a spurious positive correlation driven by task difficulty rather than architecture.

### Conservative conclusion

The data show a **consistent positive trend** between exit collapse magnitude and task success, but the correlation is **not statistically significant** at conventional levels (ρ=0.58, p=0.10, n=9). The within-suite direction is uniformly positive, which is more informative than the overall correlation because it controls for suite difficulty. However, with only 2–3 architectures per suite, this remains suggestive rather than conclusive.

**This analysis neither confirms nor refutes a functional connection between exit collapse and task performance.** It provides directional evidence that could be strengthened with additional architectures or suites.

## 6. Caveats

- **Confounds**: Architecture differences (model size, backbone, training data) are not controlled. The correlation may partly reflect "better models have both more structured representations and higher SR."
- **NORA variant ambiguity**: We used base NORA (no AC) for primary analysis. The R² Δ measurements should be confirmed against the specific checkpoint analyzed.
- **Non-independence**: Multiple suites from the same architecture are not independent observations. The effective degrees of freedom are closer to 3 (architectures) than 9 (data points).
- **Published SR variability**: Different papers may use slightly different evaluation protocols (number of seeds, rollout count). OpenVLA numbers come from the TraceVLA paper's re-evaluation, not the original OpenVLA paper.
