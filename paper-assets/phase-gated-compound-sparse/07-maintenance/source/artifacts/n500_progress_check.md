# C2 n=500 Experiment Progress Check
**Timestamp:** 2026-05-15 11:00 UTC (19:00 server time)

## Experiment Matrix (2 models × 2 masking × 4 sparsity = 16 conditions)

| Condition | Status | Progress | Notes |
|-----------|--------|----------|-------|
| ds_imp_s015 | ✅ Done | 500/500 | results file complete |
| ds_rand_s015 | ✅ Done | 500/500 | results file complete |
| ds_imp_s020 | ✅ Done | 500/500 | results file complete |
| ds_rand_s020 | ✅ Done | 500/500 | results file complete |
| ds_imp_s025 | 🔄 Running | 461/500 | GPU 0, started 06:55 |
| ds_rand_s025 | ✅ Done | 500/500 | results file complete |
| ds_imp_s030 | ⏳ Pending | 0/500 | queued after ds_imp_s025 in run_c2_n500_gpu0.sh |
| ds_rand_s030 | 🔄 Running | 5/500 | GPU 1, started 10:54 |
| qw_imp_s015 | ✅ Done | 500/500 | results file complete |
| qw_rand_s015 | ✅ Done | 500/500 | results file complete |
| qw_imp_s020 | ✅ Done | 500/500 | results file complete |
| qw_rand_s020 | ✅ Done | 500/500 | results file complete |
| qw_imp_s025 | ✅ Done | 500/500 | results file complete |
| qw_rand_s025 | ✅ Done | 500/500 | results file complete |
| qw_imp_s030 | 🔄 Running | 152/500 | GPU 2, started 09:53 |
| qw_rand_s030 | 🔄 Running | 133/500 | GPU 3, started 10:01 |

**Summary: 11/16 done, 4/16 running, 1/16 pending**

## GPU Utilization

| GPU | Util% | VRAM Used/Total | Running |
|-----|-------|-----------------|---------|
| 0 | 77% | 33.4/97.9 GB | ds_imp_s025 (461/500) |
| 1 | 78% | 16.4/97.9 GB | ds_rand_s030 (5/500) |
| 2 | 99% | 27.8/97.9 GB | qw_imp_s030 (152/500) |
| 3 | 76% | 28.4/97.9 GB | qw_rand_s030 (133/500) |

All 4 GPUs active. tmux/screen sessions alive.

## ETA Estimates

| Condition | Remaining | Est. completion (server time) |
|-----------|-----------|-------------------------------|
| ds_imp_s025 | 39 problems | ~19:30 May 15 |
| ds_imp_s030 | 500 problems | ~23:30 May 15 (auto-queued after s025) |
| ds_rand_s030 | 495 problems | ~23:00-00:00 May 15-16 |
| qw_imp_s030 | 348 problems | ~21:00-22:00 May 15 |
| qw_rand_s030 | 367 problems | ~21:30-22:30 May 15 |

**Bottleneck:** ds_imp_s030 (GPU 0) — won't start until ds_imp_s025 finishes. All 16 conditions estimated complete by ~00:00 May 16 server time.

**NOT ALL_COMPLETE**
