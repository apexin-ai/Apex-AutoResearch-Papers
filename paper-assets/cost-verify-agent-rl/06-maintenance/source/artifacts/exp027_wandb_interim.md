# exp027 W&B Interim Check — 2026-05-15 ~17:45 UTC

## Run Info
- **Run ID**: y7jiibqk
- **Run Name**: exp027-alfworld-stable-grpo
- **State**: running
- **Runtime**: 10752s (~3h)
- **W&B Step**: 1 (step 0 = val_before_train completed; step 1 training in progress or just completed gradient update)
- **Entity/Project**: xiaoyucorynne- / cost-verify-agent-rl

## Available Metrics (Summary Only, No History)

| Metric | Value | Assessment |
|--------|-------|------------|
| actor/grad_norm | 19.44 | NORMAL (threshold: < 0.1 bad, > 50 bad) |
| actor/entropy | 0.275 | Single point, no trend — cannot assess collapse |
| actor/kl_loss | 0.0576 | First step value; needs monitoring |
| actor/kl_coef | 0.005 | Matches config |

## Missing Metrics (Not Yet Logged)
- train/success, val/success — no success data yet
- train/reward_mean, train/reward_std — no reward data
- actor/loss, critic/loss — no loss data
- rollout/success, rollout/reward_mean — no rollout data
- All history arrays are empty (0 data points)

## Analysis

### Why so little data?
- Started ~14:33 UTC, runtime ~3h = consistent with step 0 (val_before_train, 16 env_groups) + step 1 rollout/training
- verl logs per-step metrics only after a full step completes (rollout -> advantages -> PPO update -> log)
- Step 1 appears to be finishing its PPO update (actor/grad_norm and actor/kl_loss exist from the gradient step) but full step-level metrics (success, reward) haven't been aggregated yet
- This is normal behavior, NOT a sign of failure

### Early Warning Checks (per D037)
- **Consecutive 2-step success=0**: Cannot assess — no success data yet
- **KL spike > 0.01**: actor/kl_loss = 0.0576 (low_var_kl type). Only 1 data point at step 1, cannot determine spike. Needs monitoring at step 2+
- **Entropy monotonic decline 3 steps**: Cannot assess — only 1 data point (0.275)
- **Grad norm**: 19.44 is healthy — no gradient vanishing or explosion

### Preliminary Health
- grad_norm = 19.44: Well within normal range
- entropy = 0.275: Baseline established, need 3+ steps for trend
- kl_loss = 0.0576: Not alarming for step 1. Effective KL penalty contribution = 0.005 * 0.0576 = 0.000288
- No red flags

## Verdict
**Status: TOO EARLY TO JUDGE.** Only step 1 gradient metrics available; step-level success/reward not logged yet. All available indicators (grad_norm, entropy, kl_loss) are within healthy ranges. Next meaningful check: after step 2-3 complete (~2-3h from now, ~19:30-20:30 UTC).

## Config Highlights (Confirmed from W&B)
- GRPO with kl_loss (low_var_kl, coef=0.005)
- entropy_coeff: 0.01
- lr: 5e-7, constant schedule
- train_batch: 128 prompts, 8 env_groups x 16 group_size
- val: 16 env_groups x 1 group_size (meets C003 >= 16 episodes)
- step_independent mode, history_length=5
- val_before_train: true, test_freq: 5, save_freq: 5
- CUDA: 0,1 (matches C001)
