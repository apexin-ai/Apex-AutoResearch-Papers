# analysis progress scan all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_progress-scan-all_20260515T101810_result.json`
- **Structured JSON:** [`cfd3ddf0fe164f449039.json`](../../sessions/cf/cfd3ddf0fe164f449039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full report:

```
== bjb1-32546 Object Eval Progress ==
(all on LIBERO object benchmark, 10 tasks × 10 rollouts each)

eval-reconvla-object (reconvla, no CRM):
  5/10 tasks done, working on T5
  T0=0% T1=0% T2=10% T3=30% T4=0%
  Avg so far: 8% (4/50)

eval-acr-object-v4-perdof (crm_perdof, norm=0.1):
  5/10 tasks done, T5 at rollout 5/10
  T0=0% T1=0% T2=20% T3=30% T4=0%
  Avg so far: 10% (5/50)

eval-acr-object-v4-obs-only (crm_obs_only, norm=0.1):
  5/10 tasks done, T5 at rollout 5/10
  T0=0% T1=10% T2=20% T3=40% T4=10%
  Avg so far: 16% (8/50)  ← best among object evals

eval-acr-object-v4-scalar (crm_scalar, norm=0.1):
  5/10 tasks done, working on T5
  T0=0% T1=0% T2=10% T3=10% T4=0%
  Avg so far: 4% (2/50)  ← worst

eval-acr-object-obs-only-norm02 (crm_obs_only, norm=0.2):
  3/10 tasks done, T3 at rollout 5/10
  T0=0% T1=0% T2=30%
  Avg so far: 10% (3/30)

eval-vla-mean-object (vla_only, mean baseline):
  5/10 tasks done, working on T5
  T0=0% T1=0% T2=10% T3=30% T4=10%
  Avg so far: 10% (5/50)

  EXTRA: eval-acr-object-v4-default (acr_vla, perdof ckpt, no norm cap):
  3/10 tasks done, T3 at rollout 5/10
  T0=0% T1=0% T2=0%
  Avg so far: 0% (0/30)  ← no norm cap → hurting badly

== bjb2-28827 Magnitude Sweep Progress ==
(all on LIBERO spatial benchmark, 10 tasks × 10 rollouts)

eval-mag-perdof-norm003 (acr_vla, norm=0.03):
  5/10 tasks done, T5 at rollout 5/10
  T0=60% T1=100% T2=0% T3=30% T4=10%
  Avg so far: 40% (20/50)

eval-mag-perdof-norm005 (acr_vla, norm=0.05):
  5/10 tasks done, starting T5
  T0=50% T1=100% T2=0% T3=30% T4=0%
  Avg so far: 36% (18/50)

eval-mag-perdof-norm02 (acr_vla, norm=0.2):
  5/10 tasks done, T5 at rollout 5/10
  T0=60% T1=90% T2=0% T3=20% T4=0%
  Avg so far: 34% (17/50)

eval-mag-perdof-norm03 (acr_vla, norm=0.3):
  5/10 tasks done, starting T5
  T0=70% T1=50% T2=10% T3=10% T4=0%
  Avg so far: 28% (14/50)

eval-mag-obsonly-norm005 (crm_obs_only, norm=0.05):
  5/10 tasks done, T5 at rollout 5/10
  T0=80% T1=90% T2=0% T3=40% T4=10%
  Avg so far: 44% (22/50)

eval-mag-obsonly-norm02 (crm_obs_only, norm=0.2):
  5/10 tasks done, T5 at rollout 5/10
  T0=90% T1=100% T2=0% T3=30% T4=10%
  Avg so far: 46% (23/50)  ← best among all mag sweep

== bjb2-40593 ==
eval-mag-obsonly-norm003-b2 (crm_obs_only, norm=0.03, spatial):
  3/10 tasks done, starting T3
  T0=90% T1=100% T2=0%
  Avg so far: 63% (19/30)  ← high but only 3 tasks

== GPU Utilization Summary ==
bjb1-32546: 6 GPUs active, 3.3-4.3 GB VRAM, 21-24% util (all running)
bjb2-28827: 6 GPUs active, 3.6 GB VRAM each, 18-19% util (all running)
bjb2-40593: 1 GPU active, 4.6 GB VRAM, 13% util

== Key Observations ==

1. ALL experiments are ~50% done (5/10 tasks) except 3 that are at 3/10
2. Object benchmark results are universally poor (4-16% avg) — obs_only@0.1 
   leads at 16% but still low
3. Spatial mag sweep shows obs_only consistently beats perdof:
   - obs_only norm=0.02: 46% | obs_only norm=0.05: 44% | obs_only norm=0.03 (b2): 63%*
   - perdof norm=0.03: 40% | perdof norm=0.05: 36% | perdof norm=0.2: 34% | perdof norm=0.3: 28%
4. T2 (table_center) is 0% across ALL spatial experiments — likely an impossible task
5. Norm=0.3 for perdof degraded T1 from 100%→50%, suggesting over-correction
6. No experiments near completion yet — earliest finishes likely in ~4-5 hours
```

---
