# ops bjb1 c prime resume maxturn50

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_c_prime_resume_maxturn50_20260522T013653_result.json`
- **Structured JSON:** [`2ad2046036aa28c7a3c6.json`](../../sessions/2a/2ad2046036aa28c7a3c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Resume from `global_step_5` confirmed. Both ranks loaded model + optimizer + rng + lr_scheduler from the checkpoint.

## Report

| Item | Value |
|------|-------|
| **PID** | 367061 |
| **tmux session** | `exp029_c_prime_resume_mt50` |
| **GPU** | cuda:0,1 @ ~8.9GB each |
| **W&B run ID** | `k9od7ujw` |
| **W&B URL** | https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/k9od7ujw |
| **max_turn** | 50 (confirmed in loaded config) |
| **Resume** | Loaded model/optimizer/rng/lr_scheduler from `global_step_5` on both ranks |
| **Config** | `_alfworld_c_prime_resume_mt50.yaml` |
| **Steps** | Will run steps 6-7 (total_training_steps=7, save_freq=5 → saves at step 7 as final) |

---
