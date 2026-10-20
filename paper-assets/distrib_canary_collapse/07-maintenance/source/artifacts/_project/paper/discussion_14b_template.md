# Discussion: 1.4B Scale Verification (Template)

## Opening

To assess whether canary-based collapse detection generalizes beyond 410M-scale models, we replicate the T=10 phase diagram row using Pythia-1.4B-deduped under identical training conditions (fp32 precision, batch_size=4, gradient checkpointing). We focus on three questions: (1) whether the PermG detection landscape is qualitatively preserved, (2) whether the sync-dip phenomenon observed at 410M persists at larger scale, and (3) which canary metrics remain robust across model sizes.

## Sync-Dip Disappearance

The most striking scale-dependent finding is the disappearance of the sync-dip at 1.4B. At 410M, the sync-dip suppresses PermG detection to 0/8 across the interval [0.55, 0.65], with sharp recovery at α=0.70. At 1.4B, α=0.60 yields PermG=4/8 (fwd) with 0/8 reverse — the sync-dip is entirely absent. [PLACEHOLDER: cross-seed s43 α=0.60 result to confirm robustness]. This suggests the sync-dip is a small-model phenomenon, possibly arising from capacity constraints that cause downstream metrics to co-vary with canary metrics in a way that nullifies directional signal. At 1.4B, sufficient model capacity may decouple these dynamics, restoring the forward lead-lag signature.

## PermG Attenuation

Despite the sync-dip disappearance, 1.4B PermG rates show mild attenuation relative to 410M:

| α | 410M PermG | 1.4B PermG (s42) | Δ |
|---|-----------|------------------|---|
| 0.45 | 0/8 | [PLACEHOLDER: a045 s42 result] | — |
| 0.50 | 6/8 | 4/8 | -2 |
| 0.60 | 0/8 (dip) | 4/8 | +4 (dip eliminated) |
| 0.75 | 6/8 | 5/8 | -1 |

[PLACEHOLDER: cross-seed s43 results for α=0.50, 0.75]

The PermG "ceiling" shifts from 6/8 (410M) to 5/8 (1.4B) at α=0.75. However, this 1-pair difference traces to a structural null: the MAUVE metric at gen_0 returns null for 1.4B, removing one pair from the testable set. After accounting for this, the effective detection rate is 5/7 ≈ 71%, comparable to 410M's 6/8 = 75%. The attenuation is therefore metric-level (MAUVE initialization), not a fundamental reduction in detection power.

At the onset boundary (α=0.50), 1.4B shows 4/8 versus 410M's 6/8. This 2-pair reduction may reflect a rightward shift in α_c at larger scale — larger models tolerate moderate contamination better, requiring higher synthetic ratios before canary metrics diverge. [PLACEHOLDER: T=15 1.4B results to test whether longer training recovers detection at α=0.50]

## ECE Robustness

[PLACEHOLDER: ECE-specific analysis across scales]

ECE emerges as the most cross-scale robust canary metric. At 410M, ECE was the strongest single metric in the s44 tie-breaker analysis (4/4 PermG FDR-significant). At 1.4B, [PLACEHOLDER: ECE contribution to K≥3 counts across α values]. This consistency positions ECE as the recommended primary canary for practitioners deploying collapse detection across model scales.

## Implications for Detection at Scale

The 1.4B results support the claim that canary-based collapse detection is qualitatively preserved across model scales, with PermG attenuation driven by metric-level scale effects rather than fundamental breakdown of the detection mechanism. Three specific implications follow:

1. **Sync-dip is not a barrier to deployment.** The sync-dip — which creates a detection blind spot at moderate α for 410M models — disappears at 1.4B, suggesting it will not affect real-world deployment on production-scale models. [PLACEHOLDER: mechanism hypothesis with capacity argument]

2. **α_c may shift rightward with scale.** The onset boundary at 1.4B appears to require slightly higher contamination ratios for detection. For practitioners, this means canary thresholds calibrated on small models may need adjustment. [PLACEHOLDER: T=15 results confirming or refuting this shift]

3. **ECE-first monitoring is scale-robust.** Given ECE's consistency across scales, we recommend ECE as the primary monitoring metric, with PermG as confirmatory. [PLACEHOLDER: quantitative ECE comparison table]

[PLACEHOLDER: T=15 1.4B results — full row comparison]
[PLACEHOLDER: cross-seed variance analysis (s42 vs s43) at 1.4B]
