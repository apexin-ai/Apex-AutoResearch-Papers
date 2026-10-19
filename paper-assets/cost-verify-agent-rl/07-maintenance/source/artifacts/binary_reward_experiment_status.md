# Binary Reward Credit Agreement Experiment Status

**Date**: 2026-05-23
**Server**: bjb1-17606, PID 14928
**Config**: `_alfworld_binary_credit_agreement.yaml`
**W&B Run**: `binary-credit-agreement` (ID: `5rqm7ofr`)

## Training Status

- **Progress**: 33% (1/3 iterations complete, ~59 min/iter)
- **Elapsed**: ~1h40m
- **Estimated completion**: ~2h more (total ~3h40m)
- **Status**: RUNNING

## Configuration

| Parameter | Value |
|-----------|-------|
| Model | qwen3_exp021_ragen_sft_v4 |
| Cell | A (h=2, step_independent GRPO) |
| Reward | Pure binary (penalty_coef=0.0, format_penalty=0) |
| gamma | 0.95 |
| K (group_size) | 8 |
| env_groups | 16 |
| total_training_steps | 3 |
| GPU | cuda:0 only |
| kl_loss_coef | 0.01 |
| entropy_coeff | 0.001 |
| lr | 1e-6 |

## Advantage Data Collection

- **File**: `/root/autodl-tmp/binary_credit_adv_log.jsonl`
- **Total records**: 400 (200 per iteration, capped at 200/batch)
- **Env var**: `LOG_PER_SAMPLE_ADV=1`, `ADV_LOG_PATH=/root/autodl-tmp/binary_credit_adv_log.jsonl`
- **Source code**: `ragen/trainer/agent_trainer.py:352-382`

### Data Schema

```json
{
  "episode_id": int,
  "window_position": int,
  "step_return": float,    // gamma-discounted return for this window
  "advantage": float,      // GRPO-normalized advantage
  "uid": str,              // group/prompt identifier
  "window_action_valid": float,
  "window_action_valid_ratio": float
}
```

## Iteration 1 Results (200 records, 49 episodes)

### Per-Group (uid) Breakdown

| uid | Episodes | Windows | Success Windows | Fail Windows | Zero-Adv |
|-----|----------|---------|-----------------|--------------|----------|
| 0   | 8        | 14      | 0               | 14           | 14       |
| 1   | 8        | 26      | 2               | 24           | 0        |
| 2   | 8        | 18      | 7               | 11           | 0        |
| 3   | 8        | 61      | 16              | 45           | 0        |
| 4   | 8        | 52      | 13              | 39           | 0        |
| 7   | 8        | —       | 0               | —            | all      |
| 8   | 7        | 8       | 0               | 8            | 8        |
| 9   | 8        | 13      | 0               | 13           | 13       |

- **6/10 groups** had zero successes → all advantages = 0 (no gradient signal)
- **4/10 groups** had mixed outcomes → non-zero advantages
- Groups with all-fail episodes produce zero variance → zero advantages → zero gradient

### Credit Agreement Analysis

**Naive sign agreement**: 157/157 = **100.0%** (excluding zero-advantage records)

This is **trivially 100%** because:

1. `compute_grpo_outcome_advantage` (core_algos.py:26) computes `scores = token_level_rewards.sum(dim=-1)` per window
2. With gamma=0.95, successful-episode windows have `step_return > 0` (gamma-discounted), failed-episode windows have `step_return = 0`
3. GRPO normalizes by group mean/std → positive step_return → above-mean → positive advantage
4. So `sign(advantage) == sign(step_return > 0)` by construction

### Why This Doesn't Match Proposition 2's 19.1% Prediction

Proposition 2 assumes **episode-level uniform advantage**: all windows in a successful episode get the same positive advantage regardless of their actual contribution. Under that assumption, with p=12.5% success rate and K=8, the predicted correct-sign rate is 19.1%.

**The implementation differs**: gamma-discounting (γ=0.95) creates **window-level variation** in step_returns, which flows into per-window advantages. Example from episode 34:

| Window | step_return | advantage | Interpretation |
|--------|-------------|-----------|----------------|
| pos=0  | 8.145       | +0.0886   | Before success |
| pos=1  | 8.574       | +0.1396   | Before success |
| pos=4  | 10.000      | +0.1371   | Success step   |
| pos=5  | 0.000       | -0.0166   | After success  |
| pos=8  | 0.000       | -0.0183   | After success  |

Windows before/at task completion get positive advantage; windows after get negative. This is implicit step-level credit assignment through gamma-discounting, NOT the uniform episode-level advantage that Proposition 2 models.

### Action Validity vs. Advantage (within successful episodes)

| Category | Count |
|----------|-------|
| Valid action + positive advantage | 31 |
| Valid action + negative advantage | 7 |
| Invalid action + positive advantage | 7 (wrong credit) |
| Invalid action + negative advantage | 0 |

7 invalid-action windows received positive advantage in successful episodes — these are cases where the gamma-discounted return is positive despite the specific action being invalid. This represents a real credit misattribution at the action-validity level.

## Iteration 2 Results (200 records, 56 episodes)

**All 56 episodes failed.** All 200 advantages = 0. No gradient signal in this batch.

This suggests the model's success rate dropped in iteration 2, possibly due to:
- Different prompt distribution
- Random variance at low success rate (~12.5%)
- Policy shift from iteration 1 training

## Implications for Proposition 2

1. **The current experiment does NOT test Proposition 2 as stated.** Proposition 2's 19.1% prediction assumes γ=1 (uniform step_return across windows). With γ=0.95, the step_returns already provide implicit credit assignment, making naive sign agreement trivially 100%.

2. **To properly test Proposition 2**, either:
   - Set γ=1.0 so all windows in a successful episode get identical step_return
   - Or redefine credit agreement at a finer granularity (e.g., action validity as ground truth)

3. **Practical concern**: 6/10 groups produced zero advantages (all-fail groups). With p≈12.5%, this is expected: P(all 8 fail) = 0.875^8 ≈ 34.4%. Combined with the fact that all-fail groups contribute zero gradient, effective training signal comes from minority of batches.

4. **Iteration 2's total failure** (0/56 episodes succeeded) confirms the high variance problem at low success rates.

## Files on Server

| File | Location |
|------|----------|
| Training log | `/root/autodl-tmp/binary_credit_training.log` |
| Advantage data | `/root/autodl-tmp/binary_credit_adv_log.jsonl` |
| Config | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_binary_credit_agreement.yaml` |
| Checkpoint dir | `/root/autodl-tmp/checkpoints/binary-credit-agreement/` |
| W&B local dir | `/root/autodl-tmp/wandb_tmp/wandb/run-20260523_174317-5rqm7ofr` |

## Next Steps

- [ ] Wait for training to complete (iteration 3, ~1h remaining)
- [ ] Collect final advantage data (should have 600 total records)
- [ ] Consider re-running with γ=1.0 for proper Proposition 2 comparison
- [ ] Analyze action-validity-based credit agreement more carefully as alternative metric
