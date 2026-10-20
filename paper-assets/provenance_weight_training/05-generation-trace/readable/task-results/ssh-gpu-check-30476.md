# ssh gpu check 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_check_30476_20260517T202233_result.json`
- **Structured JSON:** [`55c377b20a3569964875.json`](../../sessions/55/55c377b20a3569964875.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 — westd-30476 (2026-05-18 04:22 UTC)

所有 4 张 GPU **全部满载运行中**，无空闲。

---

### cuda:0 — grid_b0_1_seed42 (PID 34716)
| 项目 | 值 |
|------|------|
| 状态 | **运行中** |
| 进度 | 82% (6975/8477) |
| 速度 | ~3.22 it/s |
| ETA | **~8 分钟** |
| VRAM | 74980 MiB / 97887 MiB |
| Checkpoints | checkpoint-500, checkpoint-1000 |
| Output | `/root/autodl-tmp/output/models/grid_b0_1_seed42/` |
| Log | `/root/runs/provenance_weight_training/grid_b0_1_seed42.log` |

> 注意：config 打印 max_steps=6103 但实际训练 8477 步（可能基于实际 token 长度重算）。尚未完成。

---

### cuda:1 — grid_b0_3_seed123_r2 (PID 42432)
| 项目 | 值 |
|------|------|
| 状态 | **运行中** |
| 进度 | 17% (1014/6103) |
| 速度 | ~2.17 s/it（eval 后恢复中） |
| ETA | **~3h** |
| VRAM | 74980 MiB / 97887 MiB |
| Checkpoints | checkpoint-500, checkpoint-1000 |
| Output | `/root/autodl-tmp/output/models/grid_b0_3_seed123/` |
| Log | `/root/runs/provenance_weight_training/grid_b0_3_seed123_r2.log` |

> 刚在 step 1000 完成 eval（eval_loss=3.096）。b=0.3, tau_batch=0.8 确认正常。

---

### cuda:2 — rho02_adaptive_tau08_seed42 (PID 41387)
| 项目 | 值 |
|------|------|
| 状态 | **运行中** |
| 进度 | 53% (3215/6103) |
| 速度 | ~2.43 s/it |
| ETA | **~2h** |
| VRAM | 46496 MiB / 97887 MiB |
| Checkpoints | checkpoint-2000, checkpoint-2500, checkpoint-3000 |
| Output | `/root/autodl-tmp/output/models/rho02_adaptive_tau08_seed42/` |
| Log | `/root/runs/provenance_weight_training/rho02_adaptive_tau08_seed42.log` |

> D068 验证实验。adaptive b 值范围 0~6+，tau_batch=0.8 稳定，ESS~2-4（n_min=2 对应 batch_size=4）。

---

### cuda:3 — batchsize16_nmin8_r2 (PID 48891)
| 项目 | 值 |
|------|------|
| 状态 | **运行中** |
| 进度 | 20% (1216/6103) |
| 速度 | ~2.47 s/it |
| ETA | **~3.3h** |
| VRAM | 71164 MiB / 97887 MiB |
| Checkpoints | checkpoint-500, checkpoint-1000 |
| Output | `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2/` |
| Log | `/root/runs/provenance_weight_training/batchsize16_nmin8_r2.log` |

> **配置确认正确**: `per_device_train_batch_size=16`, `gradient_accumulation_steps=1`（隐含），`n_min=8`, `weighting_method=adaptive`, `tau=0.8`。b 值非零且动态变化（0.6~1.8），ESS~8-11 符合 n_min=8 预期。

---

### 总结

| GPU | 实验 | 进度 | 预计完成时间 (UTC) |
|-----|------|------|------|
| 0 | grid_b0_1_seed42 | 82% | ~04:30 |
| 1 | grid_b0_3_seed123_r2 | 17% | ~07:20 |
| 2 | rho02_adaptive_tau08_seed42 | 53% | ~06:20 |
| 3 | batchsize16_nmin8_r2 | 20% | ~07:50 |

cuda:0 即将最先完成（~8分钟内）。所有实验运行正常，无异常。

---
