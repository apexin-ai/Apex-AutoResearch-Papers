# check bjb1 32546 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-32546-status_20260526T075129_result.json`
- **Structured JSON:** [`74f5a23aaba22fd470b2.json`](../../sessions/74/74f5a23aaba22fd470b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== π0.5 CRM K=2 Status (all RUNNING, no JSON yet) ===
[RUNNING] pi05-crm-k2-goal-s42-bjb1   (GPU 0, 26%): ~5/10 tasks  (put_the_bowl_on_top_of_the_cabinet 100%)
[RUNNING] pi05-crm-k2-goal-s43-bjb1   (GPU 1, 20%): ~5/10 tasks  (put_the_bowl_on_top_of_the_cabinet 95%)
[RUNNING] pi05-crm-k2-goal-s44-bjb1   (GPU 2, 57%): ~5/10 tasks  (put_the_bowl_on_top_of_the_cabinet 100%)
[RUNNING] pi05-crm-k2-object-s42-bjb1 (GPU 3, 26%): ~4-5/10 tasks (in pick_up_the_ketchup)
[RUNNING] pi05-crm-k2-object-s43-bjb1 (GPU 4, 24%): ~4-5/10 tasks (in pick_up_the_ketchup)
[RUNNING] pi05-crm-k2-object-s44-bjb1 (GPU 5, 59%): ~4-5/10 tasks (in pick_up_the_ketchup)

所有 6 个 tmux session 仍活跃；6 GPU 全部有 ~12 GB 显存占用。
预估剩余 ~50–60 分钟（目前进度过半）。

=== SmolVLA 历史 JSON (object benchmark, K=2 CRM obs-only norm=0.05) ===
eval_object_crm_obs_only_norm0.05_seed42.json: SR=77.0%
eval_object_crm_obs_only_norm0.05_seed43.json: SR=78.5%
eval_object_crm_obs_only_norm0.05_seed44.json: SR=74.0%
  → mean=76.5%

=== SmolVLA 历史 JSON (object adaptive conformal norm=0.2 tau=0.25) ===
eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json: SR=77.5%
eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json: SR=75.0%
  (seed42 缺失)

=== 额外发现: 已有 π0.5 CRM K=2 object 历史 JSON (与当前 re-run 同名 base) ===
eval_object_crm_obs_only_norm0.05_seed42_pi05_K2.json: SR=89.0%
eval_object_crm_obs_only_norm0.05_seed43_pi05_K2.json: SR=87.0%
eval_object_crm_obs_only_norm0.05_seed44_pi05_K2.json: SR=88.0%
  → mean=88.0%（当前 object 跑完后请核对是否一致或重复）
```

---
