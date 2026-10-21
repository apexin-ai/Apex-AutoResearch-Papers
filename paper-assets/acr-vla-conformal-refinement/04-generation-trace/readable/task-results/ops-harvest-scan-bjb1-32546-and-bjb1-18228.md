# ops harvest scan bjb1 32546 and bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-scan-bjb1-32546-and-bjb1-18228_20260518T185328_result.json`
- **Structured JSON:** [`09a1d20cfffef83e1b0a.json`](../../sessions/09/09a1d20cfffef83e1b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full report.

---

## bjb1-18228

### GPU Status
| GPU | Util | VRAM | Status |
|-----|------|------|--------|
| cuda:0 | 0% | 1 MiB / 24G | **IDLE** |
| cuda:1 | 99% | 9.5G / 24G | busy |
| cuda:2 | 99% | 12.8G / 24G | busy |
| cuda:3 | 22% | 2.9G / 24G | busy (perdof-default-seed43, mid-eval) |

### Still Running (6 tmux sessions)
| Session | GPU | Output file |
|---------|-----|-------------|
| eval-perdof-object-default-seed43 | cuda:3 | eval_object_perdof_default_seed43.json |
| eval-perdof-object-norm003-seed44 | cuda:2 | eval_object_perdof_norm003_seed44.json |
| eval-perdof-object-norm003-seed44-r2 | cuda:2 | (same output, conflict!) |
| eval-obs-only-object-norm003-seed43 | cuda:1 | eval_object_obs_only_norm003_seed43.json |
| eval-obs-only-object-norm003-seed46 | cuda:1 | eval_object_obs_only_norm003_seed46.json |
| eval-obs-only-object-norm005-seed46 | cuda:2 | eval_object_obs_only_norm005_seed46.json |

### Completed Experiments (22 JSON files, all potentially unharvested)
| exp_id | SR% | Date | JSON path |
|--------|-----|------|-----------|
| obs_only_norm02_seed48 | 18% | May 19 00:49 | eval_object_obs_only_norm02_seed48.json |
| obs_only_norm03_seed48 | 16% | May 18 21:10 | eval_object_obs_only_norm03_seed48.json |
| obs_only_norm01_seed48 | 18% | May 18 19:39 | eval_object_obs_only_norm01_seed48.json |
| perdof_norm02_seed45_r3 | 12% | May 18 18:14 | eval_object_perdof_norm02_seed45_r3.json |
| obs_only_norm02_k5_seed42 | 14% | May 18 09:34 | eval_object_obs_only_norm02_k5_seed42.json |
| k1_crm_multiscale_seed44 | 10% | May 18 04:38 | eval_k1_crm_multiscale_object_seed44_bjb1-18228.json |
| k1_crm_multiscale_seed43 | 9% | May 18 04:37 | eval_k1_crm_multiscale_object_seed43_bjb1-18228.json |
| openvla_vla_only_seed42 | 0% | May 18 01:38 | eval_openvla_object_vla_only_seed42.json |
| obs_only_norm01_seed45 | 14% | May 17 20:34 | eval_object_obs_only_norm01_seed45.json |
| perdof_norm01_seed44 | 8% | May 17 18:39 | eval_object_perdof_norm01_seed44.json |
| obs_only_norm02_seed46 | 15% | May 17 13:04 | eval_object_obs_only_norm02_seed46.json |
| perdof_norm03_seed44 | 4% | May 17 12:40 | eval_object_perdof_norm03_seed44.json |
| vla_only_seed46 | 13% | May 17 06:08 | eval_object_vla_only_seed46.json |
| perdof_seed44 | 8% | May 17 02:12 | eval_object_perdof_seed44.json |
| reconvla_seed44 | 13% | May 16 23:28 | eval_object_reconvla_seed44.json |
| obs_only_norm02_seed44 | 16% | May 16 22:38 | eval_object_obs_only_norm02_seed44.json |
| perdof_default_norm_r2 | 0% | May 16 16:57 | eval_object_perdof_default_norm_r2.json |
| perdof_seed43 | 12% | May 16 11:10 | eval_object_perdof_seed43.json |
| obs_only_seed43 | 12% | May 16 08:40 | eval_object_obs_only_seed43.json |
| reconvla_seed43 | 17% | May 16 08:34 | eval_object_reconvla_seed43.json |
| mag_obsonly_norm03 | 36% | May 16 01:20 | eval_mag_obsonly_norm03.json |
| reconvla_spatial_r2 | 10% | May 15 15:06 | eval_reconvla_spatial_r2.json |

### Anomalies
- **LOST RESULT: `vla_only_seed45_r2`** -- Log shows completed with 11% SR, but **JSON file is missing**. Log text says "Results saved to logs/eval_object_vla_only_seed45_r2.json" but file doesn't exist on disk.
- **`scalar-seed45-r2`: NOT FOUND** on this server. No scalar experiments exist here at all.
- **perdof-default-seed43**: Still running on cuda:3, currently at `pick_up_the_butter_and_place_it_in_the_basket` rollout 1/10.
- **cuda:0 is IDLE** (confirmed, 0% util, 1 MiB).
- **cuda:3 is NOT idle** -- Director report of "1 GPU idle 5min+" was about cuda:0 only.
- **Stale process**: PID 702897 (eval-k1-seed43, CUDA_VISIBLE_DEVICES=1) has no tmux session but process still exists. JSON already written. Zombie process wasting memory on cuda:1.

### Idle GPUs: **cuda:0**

---

## bjb1-32546

### GPU Status
| GPU | Util | VRAM | Status |
|-----|------|------|--------|
| cuda:0 | 99% | 9.9G / 24G | busy |
| cuda:1 | 98% | 9.0G / 24G | busy |
| cuda:2 | 99% | 9.0G / 24G | busy |
| cuda:3 | 99% | 9.9G / 24G | busy |
| cuda:4 | 98% | 8.5G / 24G | busy |
| cuda:5 | 98% | 9.9G / 24G | busy |

All 6 GPUs fully occupied.

### Still Running (13 tmux sessions)
| Session | GPU | Target output |
|---------|-----|---------------|
| eval-perdof-object-norm003-seed43 | cuda:2 | eval_object_perdof_norm003_seed43.json |
| eval-perdof-object-norm005-seed43 | cuda:1 | eval_object_perdof_norm005_seed43.json |
| eval-obs-only-object-norm003-seed44 | cuda:0 | eval_object_obs_only_norm003_seed44.json |
| eval-obs-only-object-norm003-seed45 | cuda:3 | eval_object_obs_only_norm003_seed45.json |
| eval_perdof_default_seed45 | cuda:4 | eval_object_perdof_default_seed45.json |
| eval-perdof-object-norm003-seed45 | cuda:5 | eval_object_perdof_norm003_seed45.json |
| eval-perdof-object-norm005-seed46 | cuda:0 | eval_object_perdof_norm005_seed46.json |
| eval-obs-only-object-default-seed47 | cuda:1 | eval_object_obs_only_default_seed47.json |
| eval-obs-only-object-norm03-seed46 | cuda:3 | eval_object_obs_only_norm03_seed46.json (**dup! JSON already exists from May 18 07:28, SR=17%**) |
| eval-perdof-object-norm03-seed46 | cuda:2 | eval_object_perdof_norm03_seed46.json |
| eval-obs-only-object-norm01-seed47 | cuda:5 | eval_object_obs_only_norm01_seed47.json |
| eval-scalar-object-seed46 | cuda:4 | eval_object_scalar_seed46.json |
| eval-dc-r2 | none | **IDLE shell, experiment finished long ago** |

### Completed Experiments (41 JSON files)
| exp_id | SR% | Date | JSON path |
|--------|-----|------|-----------|
| perdof_norm01_seed43 | 12% | May 18 22:32 | eval_object_perdof_norm01_seed43.json |
| obs_only_norm005_seed45 | 14% | May 18 22:11 | eval_object_obs_only_norm005_seed45.json |
| obs_only_norm01_seed46 | 18% | May 18 21:17 | eval_object_obs_only_norm01_seed46.json |
| obs_only_norm005_seed44 | 16% | May 18 21:03 | eval_object_obs_only_norm005_seed44.json |
| perdof_norm005_seed44 | 9% | May 18 20:32 | eval_object_perdof_norm005_seed44.json |
| perdof_norm02_seed43 | 9% | May 18 18:34 | eval_object_perdof_norm02_seed43_bjb1-32546.json |
| perdof_default_seed46 | 0% | May 18 09:25 | eval_object_perdof_default_seed46.json |
| obs_only_norm005_seed43_r2 | 14% | May 18 08:41 | eval_object_obs_only_norm005_seed43_r2.json |
| obs_only_default_seed46 | 15% | May 18 08:10 | eval_object_obs_only_default_seed46.json |
| obs_only_norm03_seed46 | 17% | May 18 07:28 | eval_object_obs_only_norm03_seed46.json |
| perdof_norm01_seed47_r2 | 14% | May 18 06:58 | eval_object_perdof_norm01_seed47_r2.json |
| perdof_norm01_seed46 | 10% | May 18 04:56 | eval_object_perdof_norm01_seed46.json |
| k1_crm_multiscale_seed43 | 9% | May 18 04:24 | eval_k1_crm_multiscale_object_seed43.json |
| k1_crm_multiscale_seed44 | 10% | May 18 04:20 | eval_k1_crm_multiscale_object_seed44.json |
| k1_crm_accg_seed44 | 7% | May 18 01:19 | eval_k1_crm_accg_object_seed44.json |
| k1_crm_accg_seed42 | 11% | May 18 01:17 | eval_k1_crm_accg_object_seed42.json |
| k1_crm_accg_seed43 | 12% | May 18 01:10 | eval_k1_crm_accg_object_seed43.json |
| perdof_norm03_seed45_r2 | 6% | May 17 18:53 | eval_object_perdof_norm03_seed45_r2.json |
| reconvla_seed47 | 10% | May 17 18:50 | eval_object_reconvla_seed47.json |
| obs_only_norm02_seed47 | 20% | May 17 18:46 | eval_object_obs_only_norm02_seed47.json |
| perdof_norm01_seed45 | 11% | May 17 17:23 | eval_object_perdof_norm01_seed45.json |
| reconvla_seed46 | 10% | May 17 16:41 | eval_object_reconvla_seed46.json |
| obs_only_norm02_seed45 | 16% | May 17 05:19 | eval_object_obs_only_norm02_seed45.json |
| scalar_seed44_r2 | 6% | May 17 05:09 | eval_object_scalar_seed44_r2.json |
| obs_only_default_seed44 | 16% | May 17 04:34 | eval_object_obs_only_default_seed44.json |
| obs_only_norm01_seed44 | 16% | May 17 03:41 | eval_object_obs_only_norm01_seed44.json |
| obs_only_norm03_seed44 | 18% | May 17 03:33 | eval_object_obs_only_norm03_seed44.json |
| vla_mean_seed44 | 10% | May 17 02:31 | eval_object_vla_mean_seed44.json |
| obs_only_norm02_seed43_r2 | 16% | May 16 15:19 | eval_object_obs_only_norm02_seed43_r2.json |
| obs_only_default_norm | 17% | May 16 14:39 | eval_object_obs_only_default_norm.json |
| perdof_norm02 | 11% | older | eval_object_perdof_norm02.json |
| scalar_seed43 | 10% | older | eval_object_scalar_seed43.json |
| obs_only_norm003 | 16% | older | eval_object_obs_only_norm003.json |
| vla_mean_seed43 | 15% | older | eval_object_vla_mean_seed43.json |
| vla_only_seed43 | 12% | older | eval_object_vla_only_seed43.json |
| obs_only_norm02 | 22% | older | eval_object_obs_only_norm02.json |
| vla_mean | 12% | older | eval_object_vla_mean.json |
| reconvla | 12% | older | eval_object_reconvla.json |
| obs_only | 19% | older | eval_object_obs_only.json |
| perdof | 11% | older | eval_object_perdof.json |
| vla_only | 12% | older | eval_object_vla_only.json |

### Anomalies
- **eval-dc-r2 tmux session**: Shell idle at prompt. Whatever it was running is long finished. Can be killed to free the tmux slot.
- **eval-acr-object-v4-obs-only**: Zombie tmux process (PID 13796) from May 15, already exited with code 0. Not in tmux ls but process lingers.
- **eval-obs-only-object-norm03-seed46**: Re-launched at 00:32 May 19 but JSON already exists from May 18 07:28 (SR=17%). This will overwrite the existing result. Likely a cron misjudgment.
- **scalar-seed45-r2**: NOT FOUND on this server either. Only scalar_seed43 and scalar_seed44_r2 exist. scalar_seed46 is currently running.

### Idle GPUs: **None** (all 6 at 98-99%)

---

## Summary of Key Issues

1. **LOST RESULT on bjb1-18228**: `vla_only_seed45_r2` completed (11% SR) but JSON is missing from disk.
2. **scalar-seed45-r2 does not exist** on either server. No such experiment was ever run.
3. **bjb1-18228 cuda:0 is idle** and available for new work.
4. **bjb1-32546 is fully saturated** (6/6 GPUs busy, 12 active evals + 1 idle tmux).
5. **Cron duplicate on bjb1-32546**: `obs_only_norm03_seed46` re-launched despite already having a result.
6. **63 total completed JSON files** across both servers (22 on 18228, 41 on 32546) -- verify against your harvest log to identify what's actually missing.

---
