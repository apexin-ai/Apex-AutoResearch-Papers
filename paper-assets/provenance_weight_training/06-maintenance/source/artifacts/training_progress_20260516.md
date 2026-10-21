# Training Progress Report — 2026-05-16

## Summary

| exp_id | GPU | PID | Step/Total | Progress | Loss | Speed | ETA (remaining) | Status |
|--------|-----|-----|-----------|----------|------|-------|-----------------|--------|
| contamination_60_seed42_r2 | cuda:0 | 257977 | 5537/6103 | 90.7% | 9.8212 | 2.21s/it | ~21 min | RUNNING |
| grid_b0_3_seed42 | cuda:1 | 274304 | 334/6103 | 5.5% | 9.11 | 4.51s/it | ~7h 13min | RUNNING |
| contamination_60_ess_only_seed42 | cuda:2 | 265012 | 3261/6103 | 53.4% | 9.77 | 2.12s/it | ~1h 40min | RUNNING |
| contamination_60_grid_b0_5_seed42 | cuda:3 | 255781 | 6103/6103 | 100% | 9.2612 | — | — | COMPLETED |

## GPU Utilization

| GPU | Model | Util% | VRAM | Temp |
|-----|-------|-------|------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 95% | 46.5/95.6 GB | 58°C |
| cuda:1 | RTX PRO 6000 Blackwell | 99% | 93.0/95.6 GB | 56°C |
| cuda:2 | RTX PRO 6000 Blackwell | 99% | 46.5/95.6 GB | 57°C |
| cuda:3 | RTX PRO 6000 Blackwell | 0% | 0/95.6 GB | 36°C |

## Details

### contamination_60_seed42_r2 (cuda:0)
- PID 257977, running 3h 34min
- Step 5537/6103, ~566 steps remaining
- Latest loss: 9.8212, lr: 5.04e-06
- ETA: ~21 minutes

### grid_b0_3_seed42 (cuda:1)
- PID 274304, running 15min
- Step 334/6103, ~5769 steps remaining
- Latest loss: 9.11, lr: 4.98e-05 (still in warmup/early cosine)
- Note: speed 4.51s/it is 2x slower than other experiments — high VRAM usage (93/95.6 GB) suggests larger batch or model config
- ETA: ~7h 13min

### contamination_60_ess_only_seed42 (cuda:2)
- PID 265012, running 1h 59min
- Step 3261/6103, ~2842 steps remaining
- Latest loss: 9.77, lr: 2.44e-05
- ETA: ~1h 40min

### contamination_60_grid_b0_5_seed42 (cuda:3)
- PID 255781: **NOT FOUND** — process exited
- Log shows: "Training complete. Model saved to output/models/contamination_60_grid_b0_5_seed42/final"
- Final train_loss: 9.2612, runtime: 3h 38min
- EXIT_CODE=129 (SIGHUP) — training completed but process received hangup signal after saving
- GPU 3 now idle (0% util, 0 MB VRAM)
