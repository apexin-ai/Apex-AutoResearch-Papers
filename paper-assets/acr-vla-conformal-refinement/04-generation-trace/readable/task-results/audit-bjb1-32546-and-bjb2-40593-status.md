# audit bjb1 32546 and bjb2 40593 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb1-32546-and-bjb2-40593-status_20260525T100109_result.json`
- **Structured JSON:** [`544378ca59ded872ca86.json`](../../sessions/54/544378ca59ded872ca86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb1-32546 (6× RTX 4090) ===
GPU Status: 全部 6 张 GPU 完全空闲（0 MiB used, 0% util）
Running experiments: 无 tmux session；进程仅 jupyter-lab + tensorboard
Found output files (target seeds only, all n_rollouts=20 除非标注):

Spatial s47/s48/s49 (D149):
  - eval_spatial_vla_only_seed47.json:                                          SR=0.300 ⚠️ n_rollouts=10 (非 20)
  - eval_spatial_vla_only_seed48.json:                                          SR=0.775
  - eval_spatial_vla_only_seed49.json:                                          SR=0.795
  - eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed47.json:        MISSING ⚠️
  - eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed48.json:        SR=0.805
  - eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed49.json:        SR=0.810

Goal s42/s43/s44 (D149):
  - eval_goal_vla_only_seed42.json:                                            SR=0.835
  - eval_goal_vla_only_seed43.json:                                            SR=0.825
  - eval_goal_vla_only_seed44.json:                                            SR=0.850
  - eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:              MISSING ⚠️
  - eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json:              SR=0.845
  - eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json:              SR=0.865

Object s42/s43/s44 (D149):
  - eval_object_vla_only_seed42.json:                                          SR=0.790
  - eval_object_vla_only_seed43.json:                                          SR=0.770
  - eval_object_vla_only_seed44.json:                                          SR=0.775
  - eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:            MISSING ⚠️
  - eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json:            SR=0.775
  - eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json:            SR=0.750

Long s42/s43/s44 (D149):
  - eval_long_vla_only_seed42.json:                                            SR=0.580
  - eval_long_vla_only_seed43.json:                                            SR=0.570
  - eval_long_vla_only_seed44.json:                                            SR=0.565
  - eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json:              MISSING ⚠️
  - eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json:              SR=0.580
  - eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json:              MISSING ⚠️

=== bjb2-40593 (1× RTX 4090D) ===
GPU Status: GPU0 5838 MiB / 24564 MiB, 18% util
Running experiments: 无 tmux；nohup 后台进程
  - PID 375035: python src/evaluate.py --mode crm_obs_only --K 10 --benchmark goal --seed 42 --n_rollouts 20
    输出目标: logs/eval_goal_crm_seed42.json（注意：crm_obs_only 而非 adaptive_conformal_crm）
    启动 17:29，已跑 2h28m，最新日志：open_the_middle_drawer 14/20=70%
  - PID 308490: http.server 19876（serving CRM checkpoint），PID 643113: http.server 18888

=== 关键缺口汇总（影响 Table 1 完整性）===
1. spatial adaptive seed47 — 缺
2. goal adaptive seed42 — 缺
3. object adaptive seed42 — 缺
4. long adaptive seed42 — 缺
5. long adaptive seed44 — 缺
6. spatial vla_only seed47 n_rollouts=10 ≠ 20，需补跑 n=20

bjb2 当前跑的是 `crm_obs_only` baseline (goal s42)，不是 `adaptive_conformal_crm`，不能填补 adaptive 缺口。
```

---
