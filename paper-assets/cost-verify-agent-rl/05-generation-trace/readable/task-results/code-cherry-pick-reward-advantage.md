# code cherry pick reward advantage

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cherry_pick_reward_advantage_20260515T083522_result.json`
- **Structured JSON:** [`8142e8701e30374361c1.json`](../../sessions/81/8142e8701e30374361c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's a summary of the changes:

### Modified files

**1. `ragen/env/alfworld/env.py`** (line 227)
- Added `anchor_obs: observation` to the `step()` info dict — raw observation text before formatting with admissible actions. Used for Phase 2 GiGPO anchor state grouping.

**2. `ragen/trainer/step_rewards.py`** (new, 109 lines)
- `assign_step_rewards()` — converts episode-level rewards to per-step rewards: -0.1 penalty for invalid actions, episode reward on terminal step
- `compute_step_discounted_returns()` — backward discounted returns within each episode (R_t = r_t + γR_{t+1})
- `compute_episode_returns()` — single return per episode (from step 0) for group normalization

**3. `ragen/trainer/core_algos.py`** (appended ~50 lines)
- `compute_grpo_step_advantage()` — GRPO group normalization for step-level samples. Groups by task uid, normalizes `(return - mean) / (std + ε)`, broadcasts to response tokens.

**4. `ragen/trainer/agent_trainer.py`** (3 changes)
- Added imports for new functions
- Added `context_window_mode` and `invalid_action_penalty_coef` parameters to `compute_advantage()`
- Added `step_independent` overlay: when mode is `step_independent` and estimator is GRPO, replaces the standard token-level advantage with step-level discounted returns + GRPO normalization
- Both `compute_advantage` call sites (lines ~838 and ~1414) now pass these parameters

**5. `tests/test_step_rewards.py`** (new, 9 tests)
- Covers: reward assignment (success/fail), discounted returns (single/multi episode), episode returns, GRPO advantage (all-same, varied, single rollout), end-to-end pipeline

### Integration contract with ctx_manager Worker
The step_independent branch expects these fields in `non_tensor_batch`:
- `episode_ids` — episode identifier per sample
- `is_action_valid` — 1.0/0.0 per sample
- `is_terminal` — 1.0 for last step of episode
- `reward` — episode-level reward per sample

---
