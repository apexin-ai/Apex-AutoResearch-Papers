# Narrative B Abstract Draft (CoRL 2026)

## Abstract (v1)

Vision-Language-Action (VLA) models for robotic manipulation suffer from compounding errors during closed-loop execution, yet improving their inference-time performance without retraining remains largely unexplored. Prior work on sample selection (choosing among multiple action candidates) offers modest gains but hits a ceiling when the candidate pool lacks high-quality samples. Correction conditioning, where a lightweight module adjusts selected actions before execution, represents an untapped axis for improvement, but the choice of conditioning features and the magnitude of corrections have not been systematically studied.

We propose a sample-then-correct pipeline that first selects promising action candidates via conformal prediction scores, then applies bounded additive corrections conditioned on auxiliary features. Through controlled experiments on the LIBERO manipulation benchmark, we conduct a systematic comparison of correction conditioning strategies and uncover a critical mechanism: observation-derived features yield corrections that remain robust across a wide range of magnitudes (mean success rate approximately 17% across seeds and norms vs. 10-12% VLA-only baseline), while per-degree-of-freedom conformal features cause progressive collapse as correction magnitude increases (from 14% to 0%). This divergence reveals that magnitude sensitivity, not feature informativeness alone, determines whether inference-time correction helps or harms a frozen VLA policy. Our findings establish that observation features provide safe correction signals, while conformal nonconformity scores require strict magnitude constraints to avoid catastrophic degradation.

---

**Word count:** ~210

## Self-check
- [x] Problem stated (VLA closed-loop robustness, inference-time without retraining)
- [x] Importance (selection ceiling, correction unexplored)
- [x] Proposal (sample-then-correct + systematic conditioning comparison)
- [x] Results (obs_only robust, perdof collapses, magnitude is key)
- [x] No em-dash
- [x] No -ing phrase endings
- [x] Abbreviations defined (VLA)
- [x] ≤3 key numbers (13-22%, 10-12%, 14%→0%)
- [x] Differentiation from A2C2 (systematic conditioning comparison) and ReconVLA (correction, not just UQ) implicit
- [x] Narrative B framing: mechanism insight is the core, SR improvement is evidence
