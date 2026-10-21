# ops status westd41074 v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_westd41074_v5_20260522T080945_result.json`
- **Structured JSON:** [`d03ce1ac396952352ec4.json`](../../sessions/d0/d03ce1ac396952352ec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41074 GPU 状态快照

### nvidia-smi processes
```
PID=304126, GPU-b12dc93c, 10529 MiB
PID=304198, GPU-b927bd9e, 10541 MiB
PID=68539,  GPU-754fc39d, 28546 MiB
PID=59671,  GPU-5de49e5a, 27526 MiB
```

### GPU memory
```
GPU 0: 10548/97887 MiB, util 43%
GPU 1: 10560/97887 MiB, util 38%
GPU 2: 28555/97887 MiB, util  0%
GPU 3: 27535/97887 MiB, util  0%
```

### PID check
| PID | Elapsed | Command |
|-----|---------|---------|
| 59671 | 23:13:35 | `train_openvla_smart_compress.py --config openvla_smart_compress_m64.yaml --wandb-run openvla_sc_m64_seed42_v6` |
| 68539 | 2d 04:49:35 | `train_openvla_smart_compress.py --config openvla_smart_compress_m96.yaml` |
| 304126 | 00:22:56 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_object --seed 43 --gpu 0` |
| 304198 | 00:22:54 | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.925 --suite libero_object --seed 43 --gpu 0` |

### tmux sessions
(blocked by read-only whitelist)

### recent logs (top 5)
| Log | Last output |
|-----|-------------|
| `eval_pi05_random_k05_spatial_seed43` | T2 ep=50: 84% → Total: 126/150=**84.0%** (21.7min) |
| `eval_pi05_l2norm_k05_spatial_seed43` | T2 ep=30: 25/30=83% (in progress) |
| `eval_pi05_random_k095_object_seed43` | EXIT_CODE=129 (killed) |
| `eval_pi05_l2norm_k0925_spatial_seed43` | EXIT_CODE=0 (completed) |
| `eval_pi05_l2norm_k0925_spatial_seed42` | EXIT_CODE=0 (completed) |

---

## westd-38929 GPU 状态快照

### nvidia-smi processes
```
PID=708992, GPU-b42ecc48, 10510 MiB
PID=709233, GPU-2b25bd52, 10456 MiB
PID=709369, GPU-d885bcad, 10456 MiB
PID=766525, GPU-acf987b3, 10535 MiB
```

### GPU memory
```
GPU 0: 10528/97887 MiB, util  2%
GPU 1: 10474/97887 MiB, util 28%
GPU 2: 10474/97887 MiB, util 30%
GPU 3: 10062/97887 MiB, util  0%
```

### PID check
| PID | Elapsed | Command |
|-----|---------|---------|
| 708992 | 00:47:33 | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.5 --suite libero_spatial --seed 43 --gpu 0` |
| 709233 | 00:47:22 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.3 --suite libero_spatial --seed 43 --gpu 0` |
| 709369 | 00:47:18 | `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.3 --suite libero_spatial --seed 43 --gpu 0` |
| 766525 | 00:19:16 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_object --seed 43 --gpu 0` |

### recent logs (top 5)
| Log | Last output |
|-----|-------------|
| `eval_pi05_l2norm_k05_spatial_seed43` | T3: 16% → Total: 133/200=**66.5%**, T4 ep=10: 40% (in progress) |
| `eval_pi05_random_k03_spatial_seed43` | T3 ep=50: 10% → Total: 112/200=**56.0%** (44.4min, in progress) |
| `eval_pi05_l2norm_k03_spatial_seed43` | T3 ep=50: 20% → Total: 113/200=**56.5%** (43.5min, in progress) |
| `eval_pi05_random_k0925_spatial_seed43` | T2 ep=20: 85% (in progress) |
| `eval_pi05_random_k05_spatial_seed43` | EXIT_CODE=0 (completed) |

---
