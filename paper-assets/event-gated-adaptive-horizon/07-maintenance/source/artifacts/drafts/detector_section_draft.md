# Section 5.3: Online CIVO Detection

## Motivation

The Normalized Value Excess (NVE) metric introduced in Section 4 quantifies CIVO severity by comparing the value-to-evaluation ratio against a reference baseline that does not employ temporal abstraction. This comparison is informative for post-hoc diagnosis but unusable during deployment: no practitioner has access to a converged baseline run while training a new agent. A metric that requires a completed control experiment to interpret cannot serve as an early warning. We therefore ask whether the *dynamics* of value overestimation, rather than its absolute magnitude relative to an external reference, contain sufficient signal to detect CIVO onset in real time. The answer, as we show below, is affirmative. By tracking the trajectory of the value-to-evaluation ratio across checkpoints, a lightweight rule-based detector can flag dangerous overestimation using only quantities available within a single run. In our validation, the detector identifies all CIVO cases (3/3) with predictive detection in two of three cases and reactive confirmation in the third.

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

We apply the detector retrospectively to ten experimental runs spanning three conditions: trained duration embedding (CIVO-positive, $n=3$), untrained or absent duration embedding (CIVO-negative, $n=3$), and vanilla baselines without temporal abstraction ($n=4$). Ground truth labels are assigned by manual inspection: a run is CIVO-positive if it exhibits sustained NVE $\geq$ 1.5$\times$ with subsequent evaluation collapse. Detection type classifies trigger timing relative to the first checkpoint where evaluation drops 20% below peak.

| Experiment | Config | Verdict | Trigger | Det. Type | Peak Eval | $r_{ve}$@trig |
|:-----------|:-------|:--------|:--------|:----------|:----------|:--------------|
| 008d (seed 0) | trained dt\_emb | TP | 45K | predictive | 167 | 0.69 |
| 010b (cheetah) | trained dt\_emb | TP | 65K | reactive | 322 | 3.18 |
| 008d (seed 3) | trained dt\_emb | TP | 45K | predictive | 452 | 0.50 |
| 008f (seed 3) | no dt\_emb | TN | -- | -- | 594 | -- |
| 009c (seed 2) | no dt\_emb | FP | 105K | reactive | 359 | 0.75 |
| 009b (seed 2) | trained dt\_emb (self-correcting) | TN | -- | -- | 279 | -- |
| 009a (seed 2) | vanilla baseline | FP | 85K | predictive | 967 | 0.73 |
| baseline (seed 1) | vanilla baseline | TN | -- | -- | 970 | -- |
| 009d (seed 0) | vanilla baseline | TN | -- | -- | 951 | -- |
| 009d (seed 1) | vanilla baseline | TN | -- | -- | 920 | -- |

**Table 3.** Retrospective CIVO detector validation ($n=10$). Detection type: "predictive" = alert precedes 20% eval decline; "reactive" = alert follows decline onset. All values derived from `artifacts/analysis/detector_formal_validation_v3.json`. TPR = 3/3 (1.00), FPR = 2/7 (0.29).

The detector identifies all three CIVO-positive runs (TPR = 3/3). Two of three are detected predictively: 008d seed 0 triggers at 45K, one checkpoint before evaluation crosses the 20% decline threshold; seed 3 triggers at 45K, a full 50K steps before decline begins. The third (010b) involves single-step collapse (eval drops 80% in one interval), making advance detection impossible for any checkpoint-based monitor; the detector fires reactively at the next available checkpoint.

Two false positives occur among seven negative cases (FPR = 2/7). Their characteristics differ. Run 009c (no duration embedding) develops genuine late-stage value overestimation (eval declines from 359 to 148) unrelated to CIVO; the detector correctly identifies value-performance dissociation, and the alert is arguably useful despite the misattribution. Run 009a (vanilla baseline) triggers during a transient three-checkpoint eval dip (688 to 618) at 85K; the model subsequently recovers to 966, making this a pure false alarm. The detector cannot distinguish transient dips from sustained collapse within its three-checkpoint observation window.

A consistent timing pattern yields a practical deployment guideline. All CIVO-positive triggers occur before 65K steps (range 45-65K, mean 52K), while both false positives trigger after 85K steps (range 85-105K, mean 95K). No false positives occur in the early training window ($< 70$K steps), and no true positives occur after it. This 83% timing gap reflects CIVO's acceleration of value divergence: trained duration embeddings amplify the overestimation feedback loop, producing detectable signatures earlier than non-CIVO pathologies. In practice, alerts before 70K steps can be treated as high-confidence CIVO indicators warranting immediate intervention, while alerts after 70K steps require manual inspection to distinguish genuine collapse from transient fluctuation.

## Limitations

Four constraints bound the current detector's applicability.

First, the three-checkpoint observation window cannot distinguish transient eval dips from sustained collapse. Run 009a (vanilla baseline) triggers at 85K during a brief performance fluctuation that resolves by 105K; the detector has no mechanism to "wait and see" whether the dip is temporary. Increasing the window to five checkpoints would eliminate this FP at the cost of delayed detection for genuine cases.

Second, the acceleration condition assumes monotonically increasing overestimation during CIVO onset. In runs where value excess oscillates before stabilizing (as in the self-correcting trajectory of 009b), the detector remains silent. This silence is appropriate when self-correction occurs, but a variant that oscillates longer before collapsing could evade detection until the acceleration condition is finally satisfied.

Third, the detector identifies a *pattern* (rising value-evaluation ratio with declining performance) rather than a *mechanism*. Run 009c demonstrates that non-CIVO pathologies produce the same signature. The detector is best understood as a "value health monitor" whose alerts warrant investigation, not as a definitive CIVO diagnosis. Disambiguating CIVO from other value pathologies requires checking whether temporal conditioning is active, a trivial additional filter in practice but one the core algorithm does not enforce.

Fourth, our validation set comprises ten runs across two environments (Walker Walk, HalfCheetah) with one architecture (DreamerV3/RSSM). The threshold values ($\tau_\text{mag} = 0.49$, $\tau_\text{vel} = 0.1$) were calibrated on this suite. Generalization to different reward scales or training dynamics requires further validation, ongoing with a manipulation task (PickCube, exp 019b).
