# audit cqa1 gpu harvest deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_gpu_harvest_deploy_20260527T073348_result.json`
- **Structured JSON:** [`ed2fe04cc8c4c2d545f8.json`](../../sessions/ed/ed2fe04cc8c4c2d545f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete audit report.

---

## cqa1-33015 GPU Status (all 4 active)

| GPU | PID | VRAM | Experiment | Progress | ETA |
|-----|------|------|-----------|----------|-----|
| 0 | 896333 | 15.3 GB | eval_openvla_attn_k095_goal_seed42_v2 | T4/10, ep 20/50 | ~4-5h |
| 1 | 11249 | 15.3 GB | eval_openvla_random_k095_goal_seed42_v2 | T10/10, ep 20/50 | **~15 min** |
| 2 | 938642 | 10.0 GB | pi05_attn_k095_long (2nd run, redundant) | T8/10, ep 30/50 | ~45 min |
| 3 | 897100 | 15.3 GB | eval_openvla_attn_k05_goal_seed42_v3 | T7/10, ep 30/50 | ~2.5h |

## Harvested

**eval_pi05_attn_k095_long_seed42_strict** → DONE, **SR=77.0%** (strict confirmed: code uses `if done:` only, no reward check)

| Task | SR |
|------|----|
| T0 alphabet_soup+tomato | 88% |
| T1 cream_cheese+butter | 98% |
| T2 stove+moka_pot | 84% |
| T3 bowl_bottom_drawer | 98% |
| T4 white_mug+yellow_mug | 84% |
| T5 book_caddy | 96% |
| T6 mug_plate_pudding | 14% |
| T7 soup+cream_cheese | 80% |
| T8 two_moka_pots | 30% |
| T9 mug_microwave | 98% |

Note: strict SR=77.0% equals the original non-strict value. The code on cqa1 was already using `if done:` (no `reward > 0.5` anywhere in eval_pi05_pruning_libero.py).

## Failed experiments

- **eval_pi05_random_k07_long_seed42_strict**: OOM at 07:13 UTC — GPU 1 occupied by PID 11249 (OpenVLA random goal)
- **eval_pi05_random_k05_long_seed42_strict**: OOM at 07:13 UTC — GPU 0 occupied by PID 896333 (OpenVLA attn goal)
- **eval_pi05_baseline_goal_seed42_strict**: tmux pane empty, log stalled at T3/10 ep 20/50 — likely OOM'd sharing GPU 0

Neither k07/k05 strict runs are in the registry (never registered).

## Anomalies

- **eval_openvla_l2norm_k095_object_seed42**: Registry says RUNNING on cqa1 but **no process found**. Previous run succeeded with SR=70.6% (500 eps). Retry never materialized.
- **eval_pi05_random_k075_long_seed42_strict**: Registry says RUNNING but failure_reason=SIGTERM. Should be FAILED.
- **GPU 2 (PID 938642)**: Completed pi05 attn k=0.95 at 04:20 UTC, then tmux restarted a 2nd identical run (redundant since we already have SR=77.0%).

## Deployment plan

No GPUs free right now. Two options:

1. **Wait ~15 min**: GPU 1 frees when random goal finishes → deploy **eval_pi05_random_k07_long_seed42_strict** there. Then wait ~45 min for GPU 2 (redundant 2nd run finishes) → deploy **k05 strict**.

2. **Kill redundant GPU 2 run now**: We already have the pi05 attn k=0.95 strict result (77.0%). The 2nd run is wasted compute. Kill it → deploy k05 strict immediately, and k07 on GPU 1 in 15 min.

Both experiments (~3.5h each) finish well before the May 28 12:00 UTC deadline.

**Which option do you prefer?** Or should I wait for GPU 1 and deploy k07 first, then handle GPU 2 after?

---
