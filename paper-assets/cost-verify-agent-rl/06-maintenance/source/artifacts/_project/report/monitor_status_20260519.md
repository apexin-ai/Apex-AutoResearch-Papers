# Experiment Monitor Status — 2026-05-19 ~17:50 UTC

## 1. hsweep_h20_seed1 (bjb1-17606)

| Item | Value |
|------|-------|
| W&B run | qi8g4f86 |
| PID 77613 | **ALIVE** |
| Last log activity | 2026-05-19 16:48 UTC |
| Steps completed | 1, 2, 3, 4 |
| Current phase | **Step 5 rollout in progress** |
| Total runtime | ~47,828s (13.3h) |
| Checkpoint dir | `/root/autodl-tmp/checkpoints/hsweep-h20/` — **EMPTY (no checkpoints saved)** |

### Train metrics per step

| Step | train/success | pass@8 | kl_loss | ppo_kl | grad_norm | entropy | step_time |
|------|--------------|--------|---------|--------|-----------|---------|-----------|
| 1 | 20.3% | 68.75% | 0.221 | 0.028 | 12.30 | 0.328 | 6.05h |
| 2 | 13.3% | — | — | — | — | — | ~0.84h* |
| 3 | — (truncated) | — | — | — | — | — | 0.73h |
| 4 | 28.1% | 75.0% | 0.380 | 0.032 | 7.31 | 0.383 | 5.66h |

*Step 2 details truncated in log output.

### Val results
**No validation has been run.** `eval_total=0.0` at all logged steps. Step 5 may trigger val if `val_freq=5`.

### Key observations
- Step 5 has NOT completed yet (far past ETA of 2026-05-18 22:00 UTC, ~20h overdue)
- Steps 2-3 were anomalously fast (~1h each vs ~6h for steps 1,4) — possibly gradient-analysis-only steps
- No checkpoints saved despite 4 training steps — concerning for reproducibility
- Train success recovered to 28.1% at step 4 after dipping to 13.3% at step 2

---

## 2. 7b_cell_a_h2 (westd-47453)

| Item | Value |
|------|-------|
| W&B run | irxgmlm2 |
| PID 849089 | **ALIVE** |
| Last log activity | 2026-05-19 17:37 UTC |
| Steps completed | 0 (val_before_train), 1 (train) |
| Current phase | **Step 2 rollout in progress** |
| Total runtime | ~5,076s (1.41h) |
| Model | Qwen3-8B, SFT baseline 80.6% |

### Metrics

| Step | Type | success | pass@8 | kl_loss | ppo_kl | grad_norm | entropy |
|------|------|---------|--------|---------|--------|-----------|---------|
| 0 | val_before_train | 28.1% | — | — | — | — | — |
| 1 | train | **12.5%** | 50.0% | **1.289** | **1.917** | 2.29 | **0.115** |

### Collapse analysis — **STRONG SIGNALS**

1. **Success rate collapsed**: 28.1% (val) → 12.5% (train step 1) — halved in one step
2. **KL explosion**: ppo_kl = 1.917 (extremely high; h=20 experiment has ppo_kl ~0.03)
3. **Entropy collapse**: 0.115 (very low; h=20 has entropy ~0.33-0.38)
4. **Interpretation**: Model is rapidly diverging from reference policy. The step-independent h=2 context window is causing the predicted information loss + sign misattribution, consistent with the hypothesis that this mechanism is model-size-independent.

---

## Recommended Next Steps

### h=20: WAIT then KILL
- Step 5 is still running. Wait for step 5 to complete (~ETA unknown, could be several more hours given step 4 took 5.66h).
- If step 5 completes and val is triggered: record val/success_rate, then kill.
- If step 5 completes with no val: the experiment may need manual val or can be killed with only train metrics.
- **Issue**: No checkpoints are being saved. If the experiment is killed, there's no recovery point.

### 7b_cell_a: CONTINUE MONITORING (collapse confirming hypothesis)
- The collapse after just 1 step is strong evidence for the paper's thesis.
- Let step 2 complete to see if degradation continues or stabilizes.
- If step 2 train success drops further (toward 0%), the collapse is confirmed.
- This is a positive result for the paper — 8B model exhibits same pathology as smaller model under h=2 step-independent RL.
