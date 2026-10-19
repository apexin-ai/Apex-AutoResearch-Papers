# audit trigger rate extraction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_trigger-rate-extraction_20260526T083137_result.json`
- **Structured JSON:** [`987ee9b55759dd424a5c.json`](../../sessions/98/987ee9b55759dd424a5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12/12 全部找到。汇总：

```
=== TRIGGER RATE EXTRACTION (SmolVLA Adaptive, K=2, τ=0.25, norm=0.2) ===

Spatial: s42=19.65%, s43=19.45%, s44=19.98% → mean=19.69%
Goal:    s42= 8.78%, s43= 8.80%, s44= 6.77% → mean= 8.12%
Object:  s42= 3.55%, s43= 3.67%, s44= 3.64% → mean= 3.62%
Long:    s42= 3.87%, s43= 4.50%, s44= 4.90% → mean= 4.43%

数据来源:
  Spatial s42: bjb1-32546 eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json  (0.19649737)
  Spatial s43: bjb1-32546 eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json  (0.19447001)
  Spatial s44: bjb1-32546 eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json  (0.19977407)
  Goal    s42: bjb1-32546 eval_goal_adaptive_conformal_crm_K2_norm0.2_tau0.25_seed42.json  (0.08780898)
  Goal    s43: bjb1-32546 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json     (0.08803509)
  Goal    s44: bjb1-32546 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json     (0.06765068)
  Object  s42: bjb2-28827 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json   (0.03547850)
  Object  s43: bjb1-32546 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json   (0.03665214)
  Object  s44: bjb1-32546 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json   (0.03639900)
  Long    s42: bjb2-28827 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json     (0.03869130)
  Long    s43: bjb1-32546 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json     (0.04502165)
  Long    s44: cqa1-32758 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json     (0.04904963)
```

---
