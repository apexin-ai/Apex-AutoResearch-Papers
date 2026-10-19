# deploy bjb2 28827 goal k2 paired s45s46s47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-goal-k2-paired-s45s46s47_20260525T060126_result.json`
- **Structured JSON:** [`9c24d61da9617f14b0f1.json`](../../sessions/9c/9c24d61da9617f14b0f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 paired Goal K=2 experiments deployed on bjb2-28827.

| GPU | exp_id | mode | seed | PID |
|-----|--------|------|------|-----|
| 0 | eval-k2-goal-adapt-s45-paired | adaptive_conformal_crm | 45 | 639192 |
| 1 | eval-k2-goal-vla-only-s45-paired | vla_only | 45 | 639189 |
| 2 | eval-k2-goal-adapt-s46-paired | adaptive_conformal_crm | 46 | 639190 |
| 3 | eval-k2-goal-vla-only-s46-paired | vla_only | 46 | 639199 |
| 4 | eval-k2-goal-adapt-s47-paired | adaptive_conformal_crm | 47 | 639193 |
| 5 | eval-k2-goal-vla-only-s47-paired | vla_only | 47 | 639194 |

- CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`
- GPUs occupied: all 6 × ~5.5GB, utilization 15–22% (rollouts active); GPU 4 momentarily at 0% (between rollouts, memory held)
- Logs: `/root/acr-vla-conformal-refinement/logs/eval_goal_{adaptive_k2_tau025,vla_only}_seed{45,46,47}_paired.{log,json}`
- Sentinels with `EXIT=...` will write to `/tmp/goal_k2_launch/&lt;exp_id>.sentinel` on completion
- Registry: all 6 in RUNNING with full spec + hypothesis

Note: scheduled wakeup at 06:08 already fired and was answered; no further wakeups outstanding.

---
