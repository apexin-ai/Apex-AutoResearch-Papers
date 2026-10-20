# Unified Temporal Label Model Comparison

## Summary

Six label aggregation strategies evaluated on 54,809 windows (3 LFs). Cross-evaluation against MV labels on conf≥2 test set (gold proxy).

## Main Table

| Model | Self-F1 | MV-Agr | Conf≥2 F1 | MV-All F1 | Notes |
|---|---|---|---|---|---|
| **MV** | 0.8468 | 1.000 | **0.8946** | 0.8468 | Baseline |
| **TWV (σ=2)** | 0.8107 | 0.8849 | **0.9003** | 0.8211 | Best TLM on conf≥2 (+0.6pp vs MV) |
| **HMM** | 0.9657 | 0.6852 | 0.7502 | 0.6564 | Stagnation over-prediction |
| **Lag-HMM** | 0.7882 | 0.8204 | 0.8936 | 0.7496 | Conf-anchored, ≈MV on conf≥2 |
| **FlyingSquid** | 0.8186 | 0.8204 | 0.7816 | 0.7343 | Systematic stagnation bias |
| **Snorkel** | 0.9068 | 0.4226 | 0.2582 | 0.3768 | Catastrophic failure |

## Key Findings

1. **TWV (σ=2) is the best TLM**: +0.6pp over MV baseline on conf≥2, with 88.5% MV agreement.
2. **FlyingSquid degrades from MV**: All 9,841 disagreements flip progress→stagnation (100% directional). Conf≥2 F1 drops from 0.8946 (MV) to 0.7816 (−11.3pp).
3. **Snorkel is catastrophic**: Only 42.3% MV agreement, conf≥2 F1=0.2582. Unusable with only 3 LFs in our binary setup.
4. **HMM has high self-F1 but poor cross-eval**: 96.6% self-F1 but only 75.0% conf≥2 F1 — it learns its own biased labels.
5. **Lag-HMM recovers via conf-anchoring**: Perfect agreement on conf≥2/3 (by design), conf≥2 F1=0.8936.

## Confidence-Level Agreement

| Model | Conf=1 | Conf=2 | Conf=3 |
|---|---|---|---|
| TWV | 0.859 | 0.949 | 0.999 |
| HMM | 0.629 | 0.821 | 0.968 |
| Lag-HMM | 0.750 | 1.000 | 1.000 |
| FlyingSquid | 0.790 | 0.893 | 1.000 |
| Snorkel | 0.449 | 0.319 | 1.000 |

## Conclusion for Paper

FlyingSquid and Snorkel are negative baselines that strengthen the TWV result. Neither generative label model improves over naive MV, and both degrade significantly on the conf≥2 cross-eval metric. This supports the paper's claim that temporal smoothing (TWV) is the appropriate aggregation strategy for sequential LF votes, not i.i.d. generative models that ignore trajectory structure.
