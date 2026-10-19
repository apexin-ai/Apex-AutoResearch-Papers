# Contribution List (Narrative B)

## Contributions

1. **A sample-then-correct pipeline for inference-time VLA improvement.** We introduce a two-stage framework that combines conformal prediction-based candidate selection with bounded additive corrections, enabling post-hoc performance gains on frozen VLA policies without retraining or architectural modification. *(Section 3: Method; Table 1: pooled results across seeds)*

2. **Mechanism insight: observation features provide robust correction signals while per-DOF conformal features collapse under magnitude scaling.** Through systematic comparison of conditioning strategies, we demonstrate that observation-derived corrections maintain stable performance across magnitudes (13-22% success rate for norm 0.03-1.42), whereas per-degree-of-freedom nonconformity scores exhibit monotonic degradation (14% to 0%) beyond a narrow safe region. This establishes magnitude sensitivity as the critical factor determining correction viability. *(Section 4.2: Magnitude Curve Analysis; Figure 2: magnitude-performance curves; Table 2: cross-magnitude comparison)*

3. **Magnitude sensitivity as a previously unidentified failure mode for learned corrections.** We show that the same correction architecture succeeds or fails depending solely on the conditioning feature's interaction with correction norm, revealing that bounded magnitude control is necessary for safe inference-time intervention on VLA policies. *(Section 4.3: Uncapped comparison; obs_only 17% vs perdof 0% at default norm)*

4. **Honest negative result: per-DOF conformal features do not generalize as correction signals.** Despite their theoretical appeal as calibrated uncertainty estimates per action dimension, conformal nonconformity scores fail to provide useful directional guidance for corrections when magnitude is not tightly constrained. This negative finding informs future work on conformal prediction applications in robot learning. *(Section 4.4: Discussion; Spatial benchmark shows no method separates from baseline at 34-35%)*
