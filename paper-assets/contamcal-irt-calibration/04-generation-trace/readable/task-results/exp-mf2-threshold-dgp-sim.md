# exp mf2 threshold dgp sim

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mf2-threshold-dgp-sim_20260518T051629_result.json`
- **Structured JSON:** [`a06baebb869744963068.json`](../../sessions/a0/a06baebb869744963068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260518_d6632e`).

## Summary

Threshold DGP simulation (MF2/D139) completed successfully: 40 seeds across 4 conditions, 27.9 min total, zero divergences.

**Surprising finding**: the linear 2PL+γ model **overestimates** γ under step-function DGP (ratio 1.09-1.33), rather than attenuating it as hypothesized. The worst case is threshold_0.5 with 33% overestimation. Meanwhile, PPP remains in the 0.50-0.56 range, meaning standard posterior predictive checks cannot detect this misspecification. CI95 coverage drops from nominal 95% to 90% under all threshold conditions.

The linear sanity check (ratio=0.87) shows mild attenuation, likely noise from J=16.

---
