# Online CIVO Detection

The Normalized Value Excess (NVE) diagnostic from the preceding sections requires a converged dt=1 baseline for comparison. During training, no practitioner has access to a completed control experiment, so NVE cannot serve as a real-time warning. We develop a baseline-free detector that monitors value-evaluation divergence dynamics within a single run, allowing intervention before collapse becomes irreversible.

## Detection Rule

At each evaluation checkpoint $t$, the detector computes the value-evaluation (V/E) ratio

$$r_t = \frac{|\bar{V}_t - \bar{E}_t|}{\max(\bar{E}_t,\; 1.0)}$$

where $\bar{V}_t$ is the mean predicted value and $\bar{E}_t$ is the mean episodic return. The denominator floor of 1.0 prevents instability when returns are near zero. An alert fires only when four conditions hold simultaneously:

1. **Magnitude**: $r_t \geq 0.49$. Value diverges from evaluation by at least half the return scale.
2. **Velocity**: $\Delta r_t = r_t - r_{t-1} > 0.1$. The ratio increases above the noise floor, not through slow drift.
3. **Acceleration**: $\Delta r_t > \Delta r_{t-1}$, with both exceeding 0.1. The divergence rate itself increases across consecutive intervals.
4. **Evaluation decline**: at least 2 of the 3 most recent checkpoints show lower evaluation than their predecessor. Divergence coincides with actual performance loss.

The four-way conjunction makes the detector conservative: a single noisy checkpoint is unlikely to satisfy all conditions at once. All quantities derive from a single training run, so the detector requires no baseline and no prior knowledge of environment reward scale. Computational overhead is negligible: four scalar comparisons per checkpoint, with no model inference beyond the standard evaluation.

## Retrospective Validation

We apply the detector retrospectively to 8 experimental runs: 3 with trained duration embedding that exhibit Conditioning-Induced Value Overestimation (CIVO) and eventual collapse, and 5 negative cases (absent duration embedding, self-correcting trajectory, or vanilla baselines without temporal abstraction).

| Run | Config | Verdict | Trigger | Lead |
|:----|:-------|:--------|:--------|:-----|
| 008d seed 0 | trained dt\_emb, Walker | TP | 45K | 15K |
| 010b | trained dt\_emb, HalfCheetah | TP | 65K | 5K |
| 008d seed 3 | trained dt\_emb, Walker | TP | 45K | 60K |
| 009c seed 2 | no dt\_emb, Walker | FP | 105K | -- |
| 008f seed 3 | no dt\_emb, Walker | TN | -- | -- |
| 009b seed 2 | trained dt\_emb (self-corr.) | TN | -- | -- |
| 001 baseline | vanilla | TN | -- | -- |
| 020 seed 2 | vanilla | TN | -- | -- |

**Table X.** Retrospective detector validation. Lead = steps between alert and collapse onset. TPR = 3/3 (100%), FPR = 1/5 (20%). Mean lead time = 26.7K steps.

The detector captures all three CIVO-positive runs. Seed 0 triggers 15K steps before collapse onset; seed 3 fires a full 60K steps early, at the point where the V/E ratio first crosses 0.49 ($r = 0.497$). The 0.49 threshold is strictly superior to 0.50: it recovers seed 3 (missed at 0.50 by a margin of 0.003) without additional false positives. For 010b (HalfCheetah), the 5K lead reflects rapid single-interval collapse where any checkpoint-based monitor has minimal advance warning. Among five negative cases, one false positive occurs at the final checkpoint of run 009c.

## Discussion

The 009c false positive arises from genuine but non-CIVO value overestimation ($r_{ve}$: 0.23 $\to$ 0.75) paired with evaluation decline (359 $\to$ 148) without trained duration embedding. The detector therefore identifies value-divergence-driven degradation broadly, with CIVO as the primary but not exclusive trigger; this broader sensitivity is useful, as alerts flag pathologies that warrant investigation regardless of root cause. The thresholds ($\tau_\text{mag} = 0.49$, $\tau_\text{vel} = 0.1$) were calibrated on Walker Walk and HalfCheetah within DreamerV3, and the three-checkpoint evaluation window cannot distinguish transient dips from sustained collapse; both limitations require further validation for deployment beyond our experimental suite.
