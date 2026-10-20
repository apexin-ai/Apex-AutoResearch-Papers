# Eval Status Check — 2026-05-14/15

## Experiment 1: cls8b-s42-ckpt800-val8192-eval (westd)

| Field | Value |
|-------|-------|
| Status | **RUNNING** |
| Server | seetacloud-westd-4x5090 (root) |
| PID | 300321 (wrapper: 300315) |
| tmux | `cls8b-s42-ckpt800-val8192-eval` |
| Started | 2026-05-15 06:39:49 |
| Elapsed | ~15 min |
| Progress | **5110 / 9335 (54.7%)** |
| Running Acc | **84.6%** |
| Speed | ~1.5s / 10 samples |
| ETA | ~2026-05-15 07:06 (~11 min remaining) |
| GPU | cuda:0, 99% util, 19241/32607 MiB |
| Log | `/root/autodl-tmp/logs/cls8b-s42-ckpt800-val8192-eval.log` (buffered, use tmux capture) |

## Experiment 2: cls4b-v5-ckpt600-val5120-eval (home)

| Field | Value |
|-------|-------|
| Status | **RUNNING** |
| Server | home-1x5090 (sonny) |
| PID | 3179262 |
| tmux | `eval_8b_val5120_fix` (name is misleading, actually running 4B v5) |
| Started | 2026-05-14 15:24 |
| Elapsed | ~31 min |
| Progress | **4000 / 9335 (42.9%)** |
| Running Acc | **82.8%** |
| Speed | ~7.5s / batch of 16 (~0.47s/sample) |
| ETA | ~2026-05-14 16:37 (~42 min remaining) |
| GPU | cuda:0, 100% util, 31727/32607 MiB |
| Output dir | `results/repo_cls_v5_ckpt600_val5120/` (4000 lines in predictions.jsonl) |

## Experiment 3: cls4b-v5-val5120-sweep (home)

| Field | Value |
|-------|-------|
| Status | **WAITING** (for ckpt-600 eval to finish) |
| PID | 3180425 |
| Started | 2026-05-14 15:31:54 |
| Elapsed | ~22 min |
| Script | `run_v5_val5120_sweep.sh` |
| Remaining ckpts | 4000, 4200, 4400, 4600 |

The sweep script waits for PID of ckpt-600 eval to exit (polling every 30s), then runs ckpt-4000 → 4200 → 4400 → 4600 sequentially. Each checkpoint eval takes ~70 min on this GPU at batch_size=16. Full sweep ETA: ~5-6 hours from when ckpt-600 finishes.

## PIDs for cron registration

| Experiment | Server | PID |
|------------|--------|-----|
| cls8b-s42-ckpt800-val8192-eval | seetacloud-westd-4x5090 | 300321 |
| cls4b-v5-ckpt600-val5120-eval | home-1x5090 | 3179262 |
| cls4b-v5-val5120-sweep | home-1x5090 | 3180425 |
