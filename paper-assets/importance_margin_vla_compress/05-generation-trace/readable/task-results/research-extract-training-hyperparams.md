# research extract training hyperparams

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_extract_training_hyperparams_20260519T022017_result.json`
- **Structured JSON:** [`7d32f00349a2227e326e.json`](../../sessions/7d/7d32f00349a2227e326e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## Smart Compress 训练超参数 (M=32, seed42)

> 来源：`configs/smart_compress.yaml` (base config, seed=42) + `train_smart_compress.py` 中的代码。seed42 的训练 log 不在此服务器上，wall clock 数据取自 seed43 (同配置)。

### Optimizer
| 参数 | 值 | 来源 |
|---|---|---|
| optimizer | AdamW | script (`torch.optim.AdamW`) |
| learning_rate | 1.0e-4 | config |
| weight_decay | 1.0e-10 | config |
| betas | (0.9, 0.95) | config |
| gradient_clipping (max_grad_norm) | 10.0 | config |

### Schedule
| 参数 | 值 | 来源 |
|---|---|---|
| total_steps | 100,000 | config |
| warmup_steps | 1,000 | config |
| warmup_type | LinearLR (start_factor=0.01) | script |
| lr_scheduler | CosineAnnealingLR | script |
| eta_min (min lr) | 2.5e-6 | config (`decay_lr`) |
| scheduler_composition | SequentialLR [LinearLR → CosineAnnealingLR] | script |

### Batch
| 参数 | 值 | 来源 |
|---|---|---|
| batch_size_per_gpu | 4 | config |
| gradient_accumulation_steps | 1 | script (无 accumulation 逻辑) |
| num_gpus | 1 | log (单卡 cuda:0) |
| effective_batch_size | **4** | 4 × 1 × 1 |

### Precision
| 参数 | 值 | 来源 |
|---|---|---|
| mixed_precision | **None (fp32)** | script (无 autocast/GradScaler/amp) |

### Compressor Architecture
| 参数 | 值 | 来源 |
|---|---|---|
| num_queries (M) | 32 | config |
| num_heads | 12 | config |
| num_layers | 2 | config |
| dropout | 0.1 | config |

### Model
| 参数 | 值 | 来源 |
|---|---|---|
| pretrained | smolvla_base | config |
| total_params | 472,226,016 | log |
| trainable_params | 122,060,832 (25.85%) | log |
| compressor_params | 22,179,840 | log |
| expert+projection_params | 99,880,992 | log |

### Hardware & Timing
| 参数 | 值 | 来源 |
|---|---|---|
| GPU | NVIDIA GeForce RTX 4090 D | nvidia-smi |
| num_gpus | 1 | log |
| wall_clock_time | ~6h 43m | log (seed43: 00:21→07:04) |
| steps_per_second | ~4.1-4.2 | log |
| time_per_step | ~0.24s | log |

### Other
| 参数 | 值 | 来源 |
|---|---|---|
| seed | 42 | config |
| num_workers | 4 | config |
| eval_every | 5,000 steps | config |
| save_every | 1,000 steps | config |
| log_every | 50 steps | config |
| eval_batch_size | 1 | config |

### 注意
- `smart_compress_m32_official.yaml` 用了 `smolvla_libero` 作为 pretrained (而非 `smolvla_base`)，同为 seed=42。如果论文中的 M=32 seed42 结果来自 official 配置，pretrained 基座应标注为 `smolvla_libero`。
- seed42 的训练 log 不在此服务器 `/root/runs/` 下，可能在其他服务器或 wandb 中。

---
