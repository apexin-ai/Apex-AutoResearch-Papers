# verify wandb step metrics two runs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_wandb_step_metrics_two_runs_20260518T035600_result.json`
- **Structured JSON:** [`ae74b6aa1b6483b81dda.json`](../../sessions/ae/ae74b6aa1b6483b81dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data retrieved. The W&B metric is `train/frac_reward_zero_std`. Here are the complete results.

---

## Run tyv20u2k (grpo_standard_20_fair)

| Step | train/grad_norm | train/frac_reward_zero_std | train/reward | train/loss |
|------|----------------|---------------------------|-------------|------------|
| 10   | 6.6250         | 0.500                     | 0.05125     | 0.08650    |
| 20   | 2.9531         | 0.625                     | 0.05563     | 0.10029    |
| 30   | 2.1250         | 0.500                     | 0.06688     | 0.06140    |
| 40   | 0.7969         | 0.500                     | 0.08125     | 0.06564    |
| 50   | 1.8594         | 0.575                     | 0.01875     | 0.09103    |
| 60   | 2.1875         | 0.550                     | 0.04313     | 0.12414    |
| 70   | 2.2969         | 0.575                     | 0.04688     | 0.06855    |
| 80   | 1.6953         | 0.550                     | 0.04563     | 0.06845    |
| **90**   | **0.0173**     | 0.550                     | 0.03063     | 0.10009    |
| 100  | 2.4063         | 0.550                     | 0.05375     | 0.07660    |

**Paper claim: "grad_norm drops to 0.017"** → **VERIFIED**. grad_norm = 0.017334 at **step 90**. This is a single-step anomaly; it recovers to 2.41 at step 100.

---

## Run li451oi4 (grpo_cka_only_20)

| Step | train/frac_reward_zero_std | train/grad_norm | train/reward | train/loss |
|------|---------------------------|----------------|-------------|------------|
| 10   | 0.175                     | 1.8906         | 0.25313     | 0.03907    |
| 20   | 0.200                     | 1.2500         | 0.21813     | 0.15016    |
| 30   | 0.200                     | 1.1016         | 0.25000     | -0.02080   |
| 40   | 0.350                     | 0.9844         | 0.23438     | 0.01860    |
| 50   | 0.150                     | 1.9766         | 0.35438     | 0.14885    |
| 60   | 0.200                     | 3.7500         | 0.29938     | 0.14619    |
| **70**   | **0.125**                 | 1.1641         | 0.30750     | 0.11588    |
| 80   | 0.250                     | 2.6719         | 0.34188     | 0.13204    |
| 90   | 0.300                     | 1.2188         | 0.24188     | 0.10321    |
| 100  | 0.200                     | 1.4141         | 0.34438     | 0.22997    |

**Paper claim: "frac_zero_std 0.125 at step 70"** → **VERIFIED**. frac_reward_zero_std = 0.125 at **step 70** (exact match).

---

## Summary

| Claim | Source Run | Verified Value | Step | Status |
|-------|-----------|---------------|------|--------|
| grad_norm drops to 0.017 | tyv20u2k | 0.01733 | 90 | **VERIFIED** |
| frac_zero_std 0.125 at step 70 | li451oi4 | 0.12500 | 70 | **VERIFIED** |

Note: The W&B metric key is `train/frac_reward_zero_std` (not `frac_zero_std`). Both claims are confirmed directly from W&B step-level history data.

---
