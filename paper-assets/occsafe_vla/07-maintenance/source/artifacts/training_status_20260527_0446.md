# Training Status Report — 2026-05-27 04:46 UTC

**Deadline: 2026-05-28 12:00 UTC (31.2h from now)**

## Experiment Progress

| # | Server | GPU | exp_id | Cell | Step | Progress | Speed | ETA (UTC) | occ_loss | action_loss |
|---|--------|-----|--------|------|------|----------|-------|-----------|----------|-------------|
| 1 | 10894 | 0 | full_occ_ln_v2_s1c_r2 | C2 s43 | ~14868 | 29.7% | 1.08 it/s | May 27 ~14:00 | 0.0295 | 0.1172 |
| 2 | 10894 | 1 | full_occ_ln_v2_s2_r2 | C2 s44 | ~14856 | 29.7% | 1.08 it/s | May 27 ~14:00 | 0.0065 | 0.1240 |
| 3 | 10894 | 2 | detach_ln_v2_s0c_r2 | C4 s42 | ~14845 | 29.7% | 1.09 it/s | May 27 ~13:50 | 0.0109 | 0.1221 |
| 4 | 10894 | 3 | full_occ_ln_v2_s0d | C2 s42 | ~12272 | 24.5% | 1.08 it/s | May 27 ~16:30 | 0.0112 | 0.1504 |
| 5 | 34685 | 0 | detach_ln_v2_s1_35 | C4 s43 | ~19184 | 38.4% | 1.09 it/s | May 27 ~12:40 | 0.0108 | 0.0913 |
| 6 | 34685 | 1 | detach_ln_s4 | C4 s46 | ~19205 | 38.4% | 1.09 it/s | May 27 ~12:40 | 0.0109 | 0.1289 |
| 7 | 34685 | 2 | ablation_occ_detach_s4 | C3 s46 | ~16400 | 32.8% | 1.08 it/s | May 27 ~13:30 | 0.0082 | 0.1348 |
| 8 | 34685 | 3 | mvp_occ_s4 | C1 s46 | ~16356 | 32.7% | 1.08 it/s | May 27 ~13:30 | 0.0106 | 0.1152 |

*Loss values from latest [AUX] log entry (logged every 100 steps)*

## Process Status

All 8 processes **alive** and actively training.

| Server | PID | Elapsed | Status |
|--------|-----|---------|--------|
| 10894 | 481426 | 04:05:43 | Running |
| 10894 | 481643 | 04:05:39 | Running |
| 10894 | 481988 | 04:05:36 | Running |
| 10894 | 490803 | 03:25:43 | Running |
| 34685 | 681124 | 05:08:26 | Running |
| 34685 | 677568 | 05:09:35 | Running |
| 34685 | 735898 | 04:25:00 | Running |
| 34685 | 736253 | 04:24:52 | Running |

## GPU Utilization

**westd-10894:**
| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 99% | 62203 MiB | 97887 MiB |
| 1 | 99% | 62203 MiB | 97887 MiB |
| 2 | 84% | 62209 MiB | 97887 MiB |
| 3 | 99% | 62203 MiB | 97887 MiB |

**westd-34685:**
| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 99% | 62203 MiB | 97887 MiB |
| 1 | 99% | 62203 MiB | 97887 MiB |
| 2 | 95% | 62203 MiB | 97887 MiB |
| 3 | 99% | 63037 MiB | 97887 MiB |

## Disk Space

| Server | Total | Used | Avail | Use% |
|--------|-------|------|-------|------|
| westd-10894 | 250G | 213G | 38G | 86% |
| westd-34685 | 350G | 259G | 92G | 74% |

## Summary

- **All 8 experiments running normally**, no anomalies detected
- **Loss curves healthy**: action_loss converged to 0.09-0.15 range, occ_loss at 0.007-0.030
- **Slowest experiment**: full_occ_ln_v2_s0d (started ~40min later), ETA ~16:30 UTC May 27
- **All experiments will complete by May 27 ~17:00 UTC**, well within the May 28 12:00 UTC deadline (~19h margin)
- **GPU utilization**: all GPUs at 84-99%, operating normally
- **Disk**: 10894 at 86% (38G free) — sufficient for remaining checkpoints; 34685 at 74% (92G free)
