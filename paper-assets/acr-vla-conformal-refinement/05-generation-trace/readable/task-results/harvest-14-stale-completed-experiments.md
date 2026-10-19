# harvest 14 stale completed experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_14-stale-completed-experiments_20260525T004657_result.json`
- **Structured JSON:** [`667b038c2e6df2294c93.json`](../../sessions/66/667b038c2e6df2294c93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 14 experiments successfully registered as DONE with conclusion=success.

| exp_id | server | suite | mode | seed | SR | registered |
|---|---|---|---|---|---|---|
| eval-supp-obj-vla-only-s42 | bjb1-32546 | object | vla_only | 42 | 79.0% | ✓ |
| eval-supp-obj-vla-only-s43 | bjb1-32546 | object | vla_only | 43 | 77.0% | ✓ |
| eval-supp-obj-vla-only-s44 | bjb1-32546 | object | vla_only | 44 | 77.5% | ✓ |
| eval-supp-goal-vla-only-s42-bjb1 | bjb1-32546 | goal | vla_only | 42 | 83.5% | ✓ |
| eval-supp-crm-norm005-goal-s48 | bjb2-28827 | goal | crm_obs_only | 48 | 80.0% | ✓ |
| eval-supp-crm-norm005-spatial-s49 | bjb2-28827 | spatial | crm_obs_only | 49 | 78.5% | ✓ |
| eval-supp-crm-norm005-spatial-s48 | bjb2-28827 | spatial | crm_obs_only | 48 | 78.0% | ✓ |
| crm-norm005-goal-s49 | bjb1-18228 | goal | crm_obs_only | 49 | 83.5% | ✓ |
| crm-norm005-object-s48 | bjb1-18228 | object | crm_obs_only | 48 | 73.5% | ✓ |
| eval-supp-goal-vla-only-s42 | cqa1-32758 | goal | vla_only | 42 | 82.0% | ✓ |
| eval-supp-goal-vla-only-s43 | cqa1-32758 | goal | vla_only | 43 | 83.5% | ✓ |
| eval-supp-goal-vla-only-s44 | cqa1-32758 | goal | vla_only | 44 | 85.0% | ✓ |
| eval-supp-goal-vla-only-s50 | cqa1-32758 | goal | vla_only | 50 | 80.0% | ✓ |
| eval-supp-spatial-vla-only-smolvla-s42 | cqa1-32758 | spatial | vla_only | 42 | 78.5% | ✓ |

State transitions per exp: PREPARING → QUEUED → RUNNING (with spec) → DONE (with hypothesis/metrics/checkpoint_path/log_path/conclusion=success). All 14 JSON files verified to exist with `overall_success_rate` matching the brief; metrics stored with `success_rate`, `successes`, `total=200`, `K`/`norm` for CRM ablations.

---
