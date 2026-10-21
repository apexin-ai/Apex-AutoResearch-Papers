# Sim Rollout 0% Success Rate — Diagnosis Report

## Summary

Rollout failure has **two independent causes**:

1. **[ROOT CAUSE] LoRA fine-tuning caused flow matching mode collapse** — the model's ODE inference converges to a fixed-point action regardless of visual input. Training action_loss (0.0187) is misleadingly low because `forward()` conditions on GT actions; `sample_actions()` starting from noise collapses.

2. **[BUG] Environment truncates at 300 steps but training episodes are 400 steps** — `gym.spec('gym_aloha/AlohaInsertion-v0').max_episode_steps = 300`, making completion impossible even for a perfect policy.

## Evidence

### Mode Collapse (Issue 1)

| Model variant | Action chunk std | Image sensitivity (Δ real vs random) |
|---|---|---|
| Pretrained (no LoRA) | **0.104** | **0.149** |
| LoRA fine-tuned (baseline ckpt) | 0.006 | 0.024 |

ODE convergence test (LoRA model, same observation):
- 10 steps: std=0.030, partially converged
- 50 steps: std=0.005, fully collapsed to fixed point
- 100 steps: std=0.006, same fixed point

The velocity field learned by LoRA has a stable attractor at ~[0, -0.08, 0.43, 0, ...] that ALL noise initializations converge to. The model effectively ignores the image.

### Truncation (Issue 2)

- Dataset episode length: 400 frames (frame_index max=399)
- Env max_episode_steps: 300 (from gym spec)
- eval_sim.py `--max_steps=400` was ineffective because gym's TimeLimit wrapper overrides

**Fixed**: `gym.make(..., max_episode_steps=args.max_steps)` now passed explicitly.

## Root Cause Analysis

During flow matching training:
- `forward()` receives GT actions → creates x_t = t*action + (1-t)*noise → predicts velocity
- The model sees the TARGET mixed with noise and learns to denoise locally
- Loss is low because each prediction is close to GT at that specific (x_t, t)

During inference:
- `sample_actions()` starts from pure noise (t=1) → iterates ODE
- The velocity field must form a GLOBALLY consistent flow from noise → actions
- LoRA with alpha/rank=2.0 disrupted the pretrained model's global flow structure
- Result: all trajectories converge to a single mode (dataset-average-like action)

## Recommended Fixes

### Quick fix (enables eval with partial model capability):
```python
# In eval_sim.py: reduce num_steps to prevent full collapse
# With 10 steps the model retains some diversity from noise
# Could also try num_steps=5 for even less convergence
```

### Proper fix (requires retraining):
1. **Reduce LoRA scaling**: alpha=32 (ratio 1.0 instead of 2.0)
2. **Add generation-aware training**: periodically run sample_actions during training and backprop through the full ODE (or use DDPM-style training with varying noise levels)
3. **Use fewer training steps**: the model may have overfit the velocity field to local structure without maintaining global flow
4. **Curriculum**: start with small num_steps and increase during training

### Alternative evaluation approach:
Use `policy.select_action()` with action queue (n_action_steps < chunk_size, e.g., 5) — shorter action execution + more frequent re-planning may partially compensate for collapsed chunks.

## What was NOT the cause:
- ✅ Image format correct (same [0,1] float, CHW, same resolution → resized internally)
- ✅ State format correct (14-dim, no normalization needed)
- ✅ Action space matches (14-dim, [-1,1] env bounds)
- ✅ Checkpoint loads correctly (0 missing, 0 unexpected keys)
- ✅ LoRA weights ARE being applied (output differs from pretrained)
- ✅ No try/except swallowing errors
- ✅ Wall clock timing is consistent with actual model inference
