# Experiment Progress Snapshot

**Timestamp:** 2026-05-18 22:17 UTC

## westd-41312 (4 GPUs, all 97-100% utilization)

| Server | GPU | Experiment | Step/Total | Progress% | ETA (UTC) |
|--------|-----|-----------|------------|-----------|-----------|
| westd-41312 | cuda:0 | gpt2_adaptive_seed42 | 4393/6103 | 72% | ~23:24 |
| westd-41312 | cuda:1 | gpt2_uniform_seed42 | 4858/6103 | 80% | ~23:00 |
| westd-41312 | cuda:2 | adaptive_1_7b_seed123 | 2803/6103 | 46% | ~01:00 (May 19) |
| westd-41312 | cuda:3 | detect_remove_q08_seed42 | 4085/6103 | 67% | ~23:27 |

- GPU VRAM: cuda:0,1,3 = 45643/97887 MiB; cuda:2 = 61693/97887 MiB (1.7B model)
- Speed: 0.6B models ~2.08-2.32 s/it; 1.7B model ~2.94 s/it

## westd-30476 (3 GPUs active, cuda:2 idle)

| Server | GPU | Experiment | Step/Total | Progress% | ETA (UTC) |
|--------|-----|-----------|------------|-----------|-----------|
| westd-30476 | cuda:0 | detect_remove_q03_seed123 | 355/6103 | 6% | ~01:38 (May 19) |
| westd-30476 | cuda:1 | detect_remove_q03_seed456 | 354/6103 | 6% | ~01:38 (May 19) |
| westd-30476 | cuda:3 | detect_remove_q02_seed42 | 4233/6103 | 69% | ~23:22 |

- GPU VRAM: cuda:0,1,3 = 41757/97887 MiB; cuda:2 = 0 MiB (idle)
- Speed: all ~2.10 s/it

## Notes

- adaptive_1_7b_seed123 shows 6103 total steps in progress bar (not 3125 as expected for 1.7B). Verify config if this is intentional.
- westd-30476 cuda:2 is idle and available for additional experiments.
- detect_remove_q03_seed123 and q03_seed456 just started (~12 min elapsed), will run ~3.5 more hours.
