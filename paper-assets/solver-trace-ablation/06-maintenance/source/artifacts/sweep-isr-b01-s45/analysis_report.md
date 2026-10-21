# Analysis Report: sweep-isr-b01-s45

## Conclusion: FAILED

Training ran **100 steps instead of 500**. Results are not comparable with existing ISR β=0.1 experiments (plan002 series, all 500 steps).

## Root Cause

**Config merge bug in `train_grpo.py` (lines 395-401).**

The config merge logic only applies YAML values when the argparse value is `None`:
```python
if current is None or (isinstance(v, bool) and v and not current):
    setattr(args, k, v)
```

Since `--num_steps` has `default=100` (not None), the config file's `num_steps: 500` is silently ignored. The command did not pass `--num_steps` explicitly on the CLI.

**This bug also affects sweep-isr-b005-s42** (confirmed: also 100 reward_log entries).

## Training Statistics (100 steps)

| Metric | Value |
|--------|-------|
| Actual steps | 100 |
| Expected steps | 500 |
| Steps with prove_rate=0 | 60/100 (60%) |
| Steps with prove_rate>0 | 40/100 (40%) |
| Runtime | ~15 min (02:41–02:56 UTC) |
| Epoch | 0.4 |
| Final LR | 1e-08 |
| Checkpoint | checkpoint-100 |

### Non-zero step prove_rate distribution
- 0.125 (1/8): ~12 steps
- 0.25 (2/8): ~7 steps
- 0.375 (3/8): ~6 steps
- 0.5 (4/8): ~12 steps
- 0.875 (7/8): ~3 steps

### Notable training dynamics
- First non-zero reward at step 20 (prove_rate=0.5, isr=0.167)
- Peak step: 96 (prove_rate=0.875, isr=0.461)
- Final step 100: prove_rate=0, isr=0 (no convergence)
- LR schedule completed full cosine decay to 1e-08 in 100 steps (should span 500)

## Comparison with ISR β=0.1 baselines (500 steps)

Cannot compare — 100-step model is severely undertrained.

Existing 500-step data for reference:
| Seed | Source | PR | H7_rate | genuine_rate |
|------|--------|----|---------|-------------|
| s42 | plan002-b01-s42-1000 (500-step data N/A) | — | — | — |
| s43 | plan002-b01-s43-r2 | 0.61 | 1.00 | 0.00 |
| s44 | plan002-b01-s44 | 0.89 | 1.00 | 0.00 |

## Remediation

1. **Immediate fix**: Retrain with explicit `--num_steps 500` in the command
2. **Permanent fix**: Change argparse defaults for overridable params to `None`, or fix config merge to track which CLI args were explicitly set (using `parser.get_default()` comparison or a sentinel)
3. **Scope check**: All other sweep experiments launched with `--config` but without explicit `--num_steps` are affected

## Files
- Checkpoint: `/root/autodl-tmp/outputs/sweep_isr_b01_s45/`
- Reward log: `/root/autodl-tmp/outputs/sweep_isr_b01_s45/reward_log.jsonl`
- Trainer state: `/root/autodl-tmp/outputs/sweep_isr_b01_s45/checkpoint-100/trainer_state.json`
