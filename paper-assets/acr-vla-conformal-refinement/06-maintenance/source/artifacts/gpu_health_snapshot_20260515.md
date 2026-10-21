# GPU Health Snapshot — 2026-05-15 session restart

## Per-Server Status

### bjb2-40593 (1 GPU, RTX 4090 24GB)
| GPU | PID | Mem Used/Total | Util | Experiment |
|-----|-----|---------------|------|------------|
| cuda:0 | 227434 | 2499/24564 MiB | 12% | crm_obs_only spatial norm=0.03 (eval-mag-obsonly-norm003-b2) |

Completed: eval-reconvla-object (exit 0)

### bjb1-18228 (4 GPUs, RTX 4090 24GB each)
| GPU | PID | Mem Used/Total | Util | Experiment |
|-----|-----|---------------|------|------------|
| cuda:0 | 390936 | 5664/24564 MiB | 20% | crm_perdof object default_norm (eval-acr-object-v4-default-r2) |
| cuda:1 | 365930 | 3804/24564 MiB | 20% | crm_perdof object seed43 norm=0.1 (eval-perdof-object-seed43) |
| cuda:2 | 356495 | 3342/24564 MiB | 23% | crm_obs_only object seed43 norm=0.1 (eval-obs-only-object-seed43) |
| cuda:3 | 356701 | 3306/24564 MiB | 21% | reconvla object seed43 (eval-argmin-object-seed43) |

Completed: eval-argmin-only-spatial-r2 (exit 0). Note: eval-mag-obsonly-norm03-b2 was killed (exit 143).

### bjb1-32546 (6 GPUs, RTX 4090 24GB each)
| GPU | PID | Mem Used/Total | Util | Experiment |
|-----|-----|---------------|------|------------|
| cuda:0 | 121334 | 4737/24564 MiB | 23% | crm_obs_only object norm=0.03 (eval-mag-obsonly-norm003-object) |
| cuda:1 | 111718 | 4700/24564 MiB | 22% | vla_only mean object seed43 (eval-vla-mean-object-seed43) |
| cuda:2 | 114673 | 4736/24564 MiB | 22% | crm_scalar object seed43 norm=0.1 (eval-scalar-object-seed43) |
| cuda:3 | 148797 | 5665/24564 MiB | 24% | crm_obs_only object seed43 norm=0.2 (eval-obs-only-object-norm02-seed43-r2) |
| cuda:4 | 134103 | 5201/24564 MiB | 23% | crm_obs_only object default_norm (eval-acr-object-obs-only-default) |
| cuda:5 | 127741 | 5201/24564 MiB | 23% | (active, experiment TBD) |

Completed: eval-acr-object-v4-obs-only (10/10, exit 0), eval-vla-only-object-seed43 (10/10, done), eval-acr-object-v4-scalar (exit 0), eval-acr-object-obs-only-norm02 (exit 0), eval-mag-perdof-norm0p3-object (exit 0)

### bjb2-28827 (6 GPUs, RTX 4090 24GB each)
| GPU | PID | Mem Used/Total | Util | Experiment |
|-----|-----|---------------|------|------------|
| cuda:0 | 105947 | 5200/24564 MiB | 18% | crm_perdof object norm=0.03 (eval-mag-perdof-norm003-object) |
| cuda:1 | 109655 | 5200/24564 MiB | 19% | crm_perdof object norm=0.05 (eval-object-perdof-norm005) |
| cuda:2 | 140759 | 5664/24564 MiB | 19% | crm_perdof object norm=0.3 (eval-object-perdof-norm03-r3) |
| cuda:3 | 141024 | 5664/24564 MiB | 18% | crm_obs_only object norm=0.2 (eval-object-obs-only-norm02-v2) |
| cuda:4 | 101616 | 5200/24564 MiB | 18% | crm_obs_only object norm=0.05 (eval-object-obs-only-norm005) |
| cuda:5 | 103034 | 5200/24564 MiB | 18% | crm_obs_only object norm=0.3 (eval-object-obs-only-norm03) |

Completed: eval-mag-perdof-norm003 (spatial, 10/10, exit 0), eval-mag-perdof-norm02-seed43-object-r2 (exit file exists), many others.

## Experiment Progress

| exp_id | server:gpu | tasks_done/10 | status |
|--------|-----------|--------------|--------|
| eval-mag-obsonly-norm003-b2 | bjb2-40593:0 | 7/10 | running — on task 8 |
| eval-acr-object-v4-default-r2 | bjb1-18228:0 | 0/10 | running — just started (task 1 in progress) |
| eval-perdof-object-seed43 | bjb1-18228:1 | 4/10 | running — on task 5 |
| eval-obs-only-object-seed43 | bjb1-18228:2 | 5/10 | running — on task 6 |
| eval-argmin-object-seed43 | bjb1-18228:3 | 5/10 | running — on task 6 |
| eval-mag-obsonly-norm003-object | bjb1-32546:0 | 2/10 | running — on task 3 |
| eval-vla-mean-object-seed43 | bjb1-32546:1 | 2/10 | running — on task 3 |
| eval-scalar-object-seed43 | bjb1-32546:2 | 2/10 | running — on task 3 |
| eval-obs-only-object-norm02-seed43-r2 | bjb1-32546:3 | 0/10 | running — just started |
| eval-acr-object-obs-only-default | bjb1-32546:4 | 1/10 | running — on task 2 |
| eval-mag-perdof-norm003-object | bjb2-28827:0 | 1/10 | running — on task 2 |
| eval-object-perdof-norm005 | bjb2-28827:1 | 1/10 | running — on task 2 |
| eval-object-perdof-norm03-r3 | bjb2-28827:2 | 0/10 | running — just started |
| eval-object-obs-only-norm02-v2 | bjb2-28827:3 | 0/10 | running — just started |
| eval-object-obs-only-norm005 | bjb2-28827:4 | 1/10 | running — on task 2 |
| eval-object-obs-only-norm03 | bjb2-28827:5 | 1/10 | running — on task 2 |

### Recently Completed
| exp_id | server | tasks | exit |
|--------|--------|-------|------|
| eval-reconvla-object | bjb2-40593 | done | 0 |
| eval-argmin-only-spatial-r2 | bjb1-18228 | done | 0 |
| eval-acr-object-v4-obs-only | bjb1-32546 | 10/10 | 0 |
| eval-vla-only-object-seed43 | bjb1-32546 | 10/10 | 0 |
| eval-mag-perdof-norm003 (spatial) | bjb2-28827 | 10/10 | 0 |

## Conflicts / Alerts

- **bjb2-28827:cuda:2 — NO CONFLICT.** PID 138858 (eval-mag-perdof-norm02-seed43-object-r2) is dead (exit file exists). Only PID 140759 (eval-object-perdof-norm03-r3) occupies cuda:2 now, using 5645 MiB.
- **bjb1-18228: eval-mag-obsonly-norm03-b2 was killed** (EXIT_CODE=143, signal TERM). This is a past event, no current issue.
- **All 17 GPUs healthy** — every GPU has exactly one active experiment, no OOM, utilization 12-24%.
