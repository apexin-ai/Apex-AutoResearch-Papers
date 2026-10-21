# DeepSeek TRAJ v2 Eval Results

## s42 (seed=42) — DONE

| Metric | Value |
|--------|-------|
| Test Accuracy | **83.24%** |
| Best Eval Loss | 0.0796 (step 504) |
| Train Loss | 0.0857 |
| Majority Baseline | 53.59% |
| Accuracy vs Baseline | +29.65pp |
| Per-test Consistency | 79.84% |

### Per-class Metrics

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| unresolved | 79.6% | 92.4% | 85.5% | 553 |
| resolved | 89.2% | 72.7% | 80.1% | 479 |

### Confusion Matrix

|  | Pred unresolved | Pred resolved |
|--|-----------------|---------------|
| **Actual unresolved** | 511 (TN) | 42 (FP) |
| **Actual resolved** | 131 (FN) | 348 (TP) |

- Checkpoint: `/root/autodl-tmp/checkpoints_deepseek_traj_v2/best/`
- Log: `/tmp/deepseek_traj_v2.log`
- Eval log: `/tmp/eval_deepseek_traj_v2.log`
- Results JSON: `/home/sonny/exec-sim-repair-verifier/eval_traj_v2_s42_results.json`

## s123 (seed=123) — RUNNING

- PID 513115, training in progress
- Progress: step 635/756 (~84%), epoch ~2.5/3
- Speed: ~3.85 s/step
- Best eval_loss so far: 0.0770 (step 504, epoch 2) — **better than s42's 0.0796**
- ETA: ~8 min remaining from last check (2026-05-16 ~14:21 UTC)
- Checkpoint dir: `/root/autodl-tmp/checkpoints_deepseek_traj_v2_s123/`
- Log: `/tmp/deepseek_traj_v2_s123.log`

**Action needed**: Once s123 training completes, run eval on cuda:3.

## Comparison with CLS Baselines

| Method | Model | Seed | Test Accuracy |
|--------|-------|------|---------------|
| CLS (func) | DeepSeek-Coder-6.7B | 42 | **86.85%** |
| CWM (func) | DeepSeek-Coder-6.7B | 42 | **86.83%** |
| TRAJ v2 (func) | DeepSeek-Coder-6.7B | 42 | **83.24%** |

TRAJ v2 is 3.6pp below CLS and CWM at the function level. This aligns with the hypothesis that trajectory-level classification is harder — the model must reason about execution traces rather than static code diffs. The gap supports the "task reformulation matters" narrative: CLS is a more efficient framing for function-level verification.

Note: s123's lower eval_loss (0.077 vs 0.080) suggests it may close the gap slightly.
