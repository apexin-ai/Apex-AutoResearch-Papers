# ops exp026 deep check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_deep_check_20260515T105333_result.json`
- **Structured JSON:** [`72b44e30697f469cbf55.json`](../../sessions/72/72b44e30697f469cbf55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 Deep Check

### Process: ALIVE, uptime=15m33s, GPU mem=[41715/97887 MiB, 41709/97887 MiB] (43%/43%), GPU util=[50%, 100%]

### Progress: step 0/150, estimated hours remaining = N/A (no steps completed yet; val_before_train just finished, first training step starting)

### val_before_train (16 episodes): success=6.25%, action_is_valid=63.1%, action_is_effective=87.9%, pass@1=6.25%

### Truncation: 25 occurrences (all during val_before_train rollouts)

### Metrics (per completed step):
| Step | pg_loss | KL | entropy | grad_norm | train_success | action_is_valid |
|------|---------|-----|---------|-----------|---------------|-----------------|
| (none) | — | — | — | — | — | — |

No training steps completed yet — the log ends at "Training Progress: 0%|  0/150".

### Alerts: none
- traceback: 0
- NaN: 0
- "error" matches: 3 (all from config text, not actual errors)
- Benign warnings: gym deprecation, Ray docker CPU detection, `anchor_obs` non-numeric metric skips

### Step 0→1 transition: not yet reached
Val_before_train completed at 18:48. Training step 0 rollout is starting now.

### Key config confirmed:
- Model: `qwen3_exp021_ragen_sft_v4` (SFT v4 checkpoint)
- Mode: `step_independent`, history_length=5
- lr=1e-6 (constant), entropy_coeff=0.001, kl_loss_coef=0.01
- Val: 16 env_groups × 1 group_size = **16 episodes** (C003 compliant)
- Train: 4 env_groups × 16 group_size = 64 rollouts/step

### Recommendation: **continue** — clean startup, val baseline established (6.25% success is expected pre-training), no errors. Check again after ~30–40 min to see if step 0 completes and first training metrics appear.

---
