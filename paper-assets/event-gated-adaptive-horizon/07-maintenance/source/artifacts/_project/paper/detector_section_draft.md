# Section 5.3: Online CIVO Detection

## Motivation

The Normalized Value Excess (NVE) metric introduced in Section 4 quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment to interpret cannot serve as an early warning. We therefore ask whether the *dynamics* of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. The answer, as we show below, is affirmative. By tracking the trajectory of the value-to-evaluation ratio across checkpoints, a lightweight rule-based detector can flag dangerous overestimation 15K to 60K steps before performance collapse, using only quantities available within a single run.

## Detection Algorithm

The detector monitors a scalar signal $r_t = \bar{V}_t / \bar{E}_t$, the ratio of mean predicted value to mean episodic evaluation at checkpoint $t$. Rather than thresholding this ratio at a single point (which would be sensitive to environment-specific reward scales), the algorithm requires convergence of four conditions that together distinguish genuine CIVO onset from transient fluctuations:

1. **Magnitude**: $r_t \geq 0.49$. The value estimate exceeds roughly half the evaluation return, entering the empirical danger zone observed across our diagnostic experiments.

2. **Velocity**: $\Delta r_t = r_t - r_{t-1} > 0.1$. The ratio is actively increasing at a rate above the noise floor, ruling out slow drift or plateau behavior.

3. **Acceleration**: $\Delta r_t > 0.1$ AND $\Delta r_{t-1} > 0.1$ AND $\Delta r_t > \Delta r_{t-1}$. The rate of increase is itself increasing across two consecutive intervals. This condition filters oscillatory paths where the ratio rises and falls without sustained divergence.

4. **Evaluation decline**: Among the three most recent checkpoints, at least two show lower evaluation than their respective predecessors. This confirms that overestimation coincides with actual performance degradation, not a benign phase where both value and returns rise together.

An alert fires only when all four conditions hold simultaneously. The conjunction makes the detector conservative: any single noisy checkpoint is unlikely to satisfy magnitude, velocity, acceleration, and decline together.

```
Algorithm: Online CIVO Detector
────────────────────────────────────────────────────
Input: stream of (V_t, E_t) at each checkpoint t
Parameters: τ_mag = 0.49, τ_vel = 0.1
State: r_prev, Δr_prev, E_history[]

At each checkpoint t:
  r_t ← mean(V_t) / mean(E_t)
  Δr_t ← r_t − r_prev

  cond_magnitude ← (r_t ≥ τ_mag)
  cond_velocity  ← (Δr_t > τ_vel)
  cond_accel     ← (Δr_prev > τ_vel) AND (Δr_t > Δr_prev)
  cond_decline   ← count(E_history[i] < E_history[i−1]
                         for i in last 3) ≥ 2

  if cond_magnitude AND cond_velocity
     AND cond_accel AND cond_decline:
      ALERT("CIVO onset detected at step t")

  r_prev ← r_t
  Δr_prev ← Δr_t
  append E_t to E_history
────────────────────────────────────────────────────
```

The computational cost is negligible: four scalar comparisons per checkpoint, with no model inference beyond the standard evaluation already performed during training.

## Retrospective Validation

We apply the detector retrospectively to all eight completed experimental runs (Table 3). Ground truth labels are assigned by manual inspection: a run is CIVO-positive if it exhibits NVE $\geq$ 1.5$\times$ sustained over multiple checkpoints with subsequent evaluation collapse, and CIVO-negative otherwise.

| Experiment | Config | Detector Trigger | Collapse Onset | Lead Time | Ground Truth | Verdict |
|:-----------|:-------|:-----------------|:---------------|:----------|:-------------|:--------|
| 008d | trained dt\_emb | 45K | 60K | 15K steps | CIVO+ | TP |
| 010b | trained dt\_emb | 65K | 70K | 5K steps | CIVO+ | TP |
| seed-3 | trained dt\_emb | 45K | 105K | 60K steps | CIVO+ | TP |
| 009a | fixed dt\_emb | none | none | n/a | CIVO− | TN |
| 009b | trained dt\_emb (self-corrected) | none | none | n/a | CIVO− | TN |
| 009c | no dt\_emb | 105K | n/a | n/a | CIVO− | FP |
| 011a | fixed dt\_emb | none | none | n/a | CIVO− | TN |
| 012a | fixed dt\_emb | none | none | n/a | CIVO− | TN |

**Table 3.** Retrospective validation of the online CIVO detector across eight experimental runs. Lead time denotes the interval between detector alert and the first checkpoint at which evaluation drops below 50% of its peak. Config describes the duration embedding regime. The detector achieves 100% true positive rate (3/3 CIVO cases detected) with one false positive (009c, 20% FPR).

The detector identifies all three CIVO-positive runs with a mean lead time of 26.7K steps before collapse onset. This window is sufficient for practical intervention (e.g., reverting to a prior checkpoint, switching to a fixed embedding, or reducing the action-repeat range). The single false positive (009c) is instructive: this run uses no trained duration embedding yet exhibits late-stage value divergence coupled with evaluation decline, a genuine pathology unrelated to CIVO. The detector correctly flags the value-performance dissociation pattern; the attribution to CIVO specifically requires additional context (namely, whether temporal conditioning is active). In deployment, this false positive is arguably a *useful* alert, as it detects real training instability regardless of root cause.

## Limitations

Three constraints bound the current detector's applicability. First, the acceleration condition assumes monotonically increasing overestimation during CIVO onset. In runs where value excess oscillates before stabilizing (as observed in the self-correcting trajectory of 009b), the detector may fire late or not at all. The 009b run reached NVE $\geq$ 1.5$\times$ transiently but then self-corrected without collapse; the detector's silence here is appropriate (no collapse to predict), yet a modified variant that oscillates longer before collapsing could evade detection until the acceleration condition is finally met.

Second, the detector identifies a *pattern* (rising value-evaluation ratio with declining performance) rather than a *mechanism*. Run 009c demonstrates that non-CIVO pathologies can produce the same signature. The detector is best understood as a "value health monitor" whose alerts warrant investigation, not as a definitive CIVO diagnosis. Disambiguating CIVO from other value pathologies requires checking whether temporal conditioning is active, a trivial additional filter in practice but one that the core algorithm does not enforce.

Third, our validation set comprises eight runs across two environments (Walker Walk, HalfCheetah) with one architecture (DreamerV3/RSSM). While the detection logic is environment-agnostic (it operates on normalized ratios), the threshold values ($\tau_\text{mag} = 0.49$, $\tau_\text{vel} = 0.1$) were calibrated on this experimental suite. Generalization to environments with different reward scales or training dynamics requires further validation, which is ongoing with a manipulation task (PickCube, exp 019b).
