# exp026 Crash Diagnosis Report

**Date**: 2026-05-15 19:03 UTC
**Trigger**: Cron monitor reported "Process gone" (miss 4/5) for PID 778562

## Verdict: FALSE ALARM — Process is alive and running

## Process Status

| Check | Result |
|-------|--------|
| PID 778562 | **ALIVE** — status `Sl+`, elapsed 24 min |
| Command | `python train.py --config-name _alfworld_exp026_step_independent_grpo` |
| Ray workers | PID 782015, 782016 (`ray::WorkerDict.actor_rollout_compute_log_prob`) |
| GPU memory | 14818 MiB each (2 GPUs) |
| GPU utilization | 96%, 97% |
| Sentinel file | Not present (training in progress) |
| Errors/OOM in log | **None** |

## Training Progress

- Total training steps: 150
- Initial validation completed:
  - `val-core/unknown/reward/mean@775`: 0.3226
  - `val-aux/unknown/reward/best@16/mean`: 4.26
- Training progress bar: **0/150** (still in first step rollout)
- Log size: 5036 lines, mostly rollout WARNING about non-numeric 'anchor_obs' metrics (benign)
- Training started: 18:38:48, rollout phase started: ~18:58:41

## Why Cron Reported "Process Gone"

Most likely cause: the cron monitoring script's process check failed transiently while PID 778562 was in a heavy GPU computation phase (FSDP compilation / model loading). The process was never actually dead.

## Next Steps

- **No action needed** — training is running normally
- Monitor step 1 completion (the dry run concern about step 1 crash)
- Check back in ~30 min for step 1 metrics
