# Training Progress Report — 2026-05-20 10:20 UTC

## GPU Status
| GPU | Exp | PID | Uptime | Step | Loss | VRAM | Speed | ETA |
|-----|-----|-----|--------|------|------|------|-------|-----|
| cuda:0 | baseline_spatial_bowl_s0 | 100319 | 3h47m | 3719/30000 (12%) | 0.0194 | 37.4/97.9 GB | ~3.6s/it | ~26h |
| cuda:1 | baseline_spatial_bowl_s1 | 94453 | 3h59m | 3948/30000 (13%) | 0.0314 | 37.4/97.9 GB | ~3.5s/it | ~25h |
| cuda:2 | baseline_object_pudding_s0 | 95429 | 3h59m | 3980/30000 (13%) | 0.0197 | 37.4/97.9 GB | ~3.6s/it | ~26h |
| cuda:3 | a1_sdf_spatial_bowl_s0 | 123362 | 1h56m | 1962/30000 (7%) | 0.2624 | 13.4/97.9 GB | ~3.8s/it | ~30h |

GPU utilization: 100% / 75% / 100% / 100%

## A1 Phase 2 Status
- **Phase 2 triggered: No** (current step 1962 < 5000 threshold)
- VRAM: 13.4 GB — consistent with Phase 1 (~13.4GB expected)
- No "phase", "unfreeze", or "lora" transition logs found
- Expected Phase 2 trigger at step 5000, ETA ~3.2h from now

## Checkpoints
- **baseline_spatial_bowl_seed0**: 1 checkpoint (step 2000), saved 08:36
- **baseline_spatial_bowl_seed1**: 1 checkpoint (step 2000), saved 08:24
- **baseline_object_pudding_seed0**: 1 checkpoint (step 2000), saved 08:22
- **a1_sdf_spatial_bowl_seed0**: 5 checkpoints (steps 1, 2, 500, 1000, 1500), latest at 09:55

## Alerts
- **A1 loss significantly higher than baselines**: A1 loss ~0.26 vs baselines ~0.02. Expected — A1 is at step 1962 (early training, Phase 1 with frozen backbone), while baselines are at step ~3900. Object_pudding baseline had similar ~0.25 loss at step 1962.
- **Checkpoint path mismatch**: Registry records flat paths (e.g. `baseline_spatial_bowl_0/`) but actual structure is nested (`baseline_spatial_bowl/baseline_spatial_bowl_seed0/`).
