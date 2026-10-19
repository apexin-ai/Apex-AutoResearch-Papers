# check exp029 correct log

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_correct_log_20260516T190514_result.json`
- **Structured JSON:** [`fc40ef60e0a2b9d4eeec.json`](../../sessions/fc/fc40ef60e0a2b9d4eeec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the complete step 1 metrics in the wandb output.log.

## Exp029 Step 1 Metrics

### Train Rollout
| Metric | Value |
|--------|-------|
| **train/AlfworldSG/success** | **17.97%** |
| **train/AlfworldSG/pass@8** | **56.25%** |
| train/AlfworldSG/action_is_valid | 0.6824 |
| train/AlfworldSG/action_is_effective | 0.9947 |
| train/AlfworldSG/num_actions | 42.03 |
| train/AlfworldSG/manager_invalid_action | 0.0054 |
| **train/response_length** | **7112.43** |
| train/batch_size | 128 |

### Actor/PPO
| Metric | Value |
|--------|-------|
| **actor/entropy** | **0.02775** |
| **actor/kl_loss** | **9.15e-4** |
| **actor/pg_loss** | **-4.59e-5** |
| **actor/grad_norm** | **1.267** |
| actor/pg_clipfrac | 7.80e-4 |
| actor/ppo_kl | -2.03e-5 |
| actor/entropy_loss | 0.05552 |
| actor/kl_coef | 0.01 |

### Critic/Score
| Metric | Value |
|--------|-------|
| critic/score/mean | 1.797 |
| critic/advantages/mean | -0.238 |
| response_length/mean | 12689.19 |
| response_length/max | 16381.0 |

### Initial Validation (Step 0, baseline)
| Metric | Value |
|--------|-------|
| val-env/AlfworldSG/success | 12.5% |
| val-env/AlfworldSG/pass@1 | 12.5% |
| val-env/AlfworldSG/action_is_valid | 0.783 |

### Status
- **Progress**: 1/100 steps, 30m10s/step, ETA ~49h48m
- **Step 2**: PPO update in progress (compute_policy_loss running on both GPUs)
- **GPU**: 0: 55788 MiB, 1: 56640 MiB (0% util — between compute phases)
- **W&B**: run `6d4oml60` — `exp029-alfworld-episode-level`

Training is healthy. Train success 17.97% vs baseline val 12.5% — slight improvement. pass@8 at 56.25% shows good diversity. grad_norm 1.267 and kl_loss 9.15e-4 are both in normal range with lr=1e-6.

---
