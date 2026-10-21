# Diagnostic: w2-qwen3-1.7b pilot experiments

**Date**: 2026-05-16 19:20 UTC+8

## Summary

Both experiments are **actively running**. The cron failure is a tracking-only issue (dot in exp_id violates tmux `[a-zA-Z0-9_-]+` naming). The training processes themselves are unaffected.

## GPU Status

| GPU | PID | Memory | Utilization | Experiment |
|-----|-----|--------|-------------|------------|
| cuda:0 | 806960 | 41026 MiB / 97887 MiB | 17% | w2-qwen3-1.7b-exec-pilot |
| cuda:1 | 807036 | 41026 MiB / 97887 MiB | 88% | w2-qwen3-1.7b-isr-pilot |

## Training Progress

### w2-qwen3-1.7b-exec-pilot (cuda:0)
- **Status**: Running
- **Step**: 76 / 500 (15%)
- **Elapsed**: ~11:34
- **Latest reward**: 0.25 (prove_rate=0.25, isr=0.125)
- **Log**: `/root/runs/solver-trace-ablation/w2-qwen3-1.7b-exec-pilot.log` (73 KB, last write 19:19)
- **Output**: `/root/autodl-tmp/outputs/w2_1.7b_exec_only_s42/` — checkpoint-50 saved, reward_log.jsonl active

### w2-qwen3-1.7b-isr-pilot (cuda:1)
- **Status**: Running
- **Step**: 75 / 500 (15%)
- **Elapsed**: ~11:29
- **Latest reward**: 0.508 (prove_rate=0.50, isr=0.083, beta_t=0.10)
- **Log**: `/root/runs/solver-trace-ablation/w2-qwen3-1.7b-isr-pilot.log` (75 KB, last write 19:19)
- **Output**: `/root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/` — checkpoint-50 saved, reward_log.jsonl active

## tmux

`tmux ls` blocked by ssh_read_only whitelist. However, both GPU processes and actively-growing logs confirm the training is running.

## Conclusion

No action needed. Both 1.7B pilot experiments are healthy and ~15% through 500 steps. ETA ~65 min remaining at current pace (~9s/step).
