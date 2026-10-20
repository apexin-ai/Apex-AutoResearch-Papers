# V5 Profiling Experiments Status Check
**Time**: 2026-05-14 10:31 UTC

## GPU Utilization
| GPU | Memory Used | Utilization |
|-----|------------|-------------|
| 0 | 33509 MiB | 76% |
| 1 | 33509 MiB | 78% |
| 2 | 26565 MiB | 99% |
| 3 | 26565 MiB | 99% |

## Experiment Status

| exp_id | GPU | PID | Status | Progress | Elapsed | ETA |
|--------|-----|-----|--------|----------|---------|-----|
| mvp_v5_fixed_s020_r2 | cuda:0 | 51024 | **ALIVE** | 29/50 | ~19 min | ~10:45 UTC |
| mvp_v5_fixed_s030_r2 | cuda:1 | 51161 | **ALIVE** | 29/50 | ~19 min | ~10:45 UTC |
| mvp_v5_random_s015 | cuda:2 | 51961 | **ALIVE** | 20/50 | ~12 min | ~10:49 UTC |
| mvp_v5_random_s025 | cuda:3 | 52103 | **ALIVE** | 20/50 | ~12 min | ~10:49 UTC |

## Notes
- All 4 experiments running normally, no anomalies
- Output directories are empty — results written on completion (after 50/50)
- Fixed (importance) experiments on GPU 0/1 use more VRAM (33.5 GB vs 26.6 GB) but lower GPU utilization (76-78% vs 99%)
- Warning observed: "Skipped 1 NaN attention layers: [27]" in importance-based experiments (same as prior runs, non-fatal)
- All experiments have tmux sessions for the fixed pair; random pair launched via submit_training_job wrapper
