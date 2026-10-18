# ops verify c4ext and cleanup 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_c4ext_and_cleanup_41074_20260520T011513_result.json`
- **Structured JSON:** [`d644443c69d1e5a30ddb.json`](../../sessions/d6/d644443c69d1e5a30ddb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 任务 1: PID 26118 验证结果

**身份确认：C4-ext (OpenVLA Smart Compress M=128)**

| 项目 | 值 |
|------|-----|
| 命令行 | `python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml` |
| GPU | GPU 0, 30108 MiB |
| 日志路径 | `/root/runs/importance_margin_vla_compress/train_openvla_sc_m128_seed42.log` |
| 训练范围 | VisionTokenCompressor only (403M / 7.9B = 5.08% trainable) |
| **当前 step** | **14150 / 100000 (14.15%)** |
| **当前 loss** | **~2.8–3.2 (稳定在 ~2.9)** |
| LR | 9.58e-05 (warmup 完成，cosine decay 中) |
| Grad norm | 0.8–1.1 (健康) |
| 速度 | 0.6 sps (~82s / 50 steps) |
| **预计剩余** | **~39.7 小时 → 约 5/22 凌晨完成** |

之前 Worker 看到 RoboFlamingo 输出是因为 tmux session 混淆——GPU 1 上确实在跑另一个 RoboFlamingo 训练 (`train_c5_roboflamingo_v2.log`)。`logs/` 目录下的 `train_openvla_vtc_m128_seed42.log` 是更早的一次中止尝试，实际输出写到了 `/root/runs/`。

---

## 任务 2: 磁盘分析

**总量 250GB, 已用 230GB, 剩余 21GB (92%)**

### 空间分布

| 路径 | 大小 | 说明 |
|------|------|------|
| `.hf_cache/datasets/parquet` | 66G | HF datasets 缓存 (LIBERO parquet) |
| `checkpoints/roboflamingo_libero_c5_v2/` | 51G | RoboFlamingo C5 v2 (best.pt 26G + checkpoint_ep1.pt 26G) |
| `importance.../checkpoints/openvla_sc_m128/` | 38G | **当前活跃训练** (checkpoint.pt 19G + checkpoint_step10000.pt 19G) |
| `.hf_cache/lerobot/hub` | 33G | LIBERO lerobot 格式缓存 |
| `openvla-libero-object/` | 15G | OpenVLA 预训练模型 |
| `importance.../checkpoints/openvla_sc_m128_lora/` | 8G | **已 killed** LoRA 实验 (step 1183 被 SIGTERM) |
| `libero_data/datasets/` | 7G | LIBERO 原始数据 |
| `models/OpenFlamingo-3B...` | 6.4G | OpenFlamingo 模型权重 |
| `.hf_cache/models--openflamingo...` | 4G | OpenFlamingo 的 HF 缓存副本 |
| `.hf_cache/datasets--yifengzhu-hf--LIBERO-datasets` | 2.2G | LIBERO 的另一份缓存 |
| `models/mpt-1b + clip` | 1.8G | RoboFlamingo 依赖模型 |

### 清理建议

| 优先级 | 路径 | 大小 | 可否安全删除 | 理由 |
|--------|------|------|-------------|------|
| **P0** | `checkpoints/openvla_sc_m128_lora/checkpoint_step1183.pt` | **8G** | **可删** | 已 killed 实验，SIGTERM 终止于 step 1183，无保留价值 |
| **P1** | `.hf_cache/models--openflamingo/...` | **4G** | **可删** | 与 `models/OpenFlamingo-3B...` 重复，RoboFlamingo 代码应直接引用后者 |
| **P2** | `.hf_cache/datasets--yifengzhu-hf--LIBERO-datasets` | **2.2G** | **可删** | 已有 lerobot 格式和 parquet 格式的 LIBERO，此份多余 |
| **P3** | `checkpoints/roboflamingo_libero_c5_buggy_20260519/` | **~4K** | **可删** | buggy 实验，仅 config.json，空间可忽略 |
| **P4** | `checkpoints/openvla_sc_m128/checkpoint_step10000.pt` | **19G** | **需确认** | 活跃训练的中间 checkpoint。checkpoint.pt 是最新(step 10000 save)，两份内容可能相同。删除后仅靠 checkpoint.pt 恢复，有一定风险 |
| **P5** | `checkpoints/roboflamingo_libero_c5_v2/checkpoint_ep1.pt` | **26G** | **需确认** | 如果 best.pt 已包含最优权重且 RoboFlamingo 训练结束，可删中间 checkpoint |
| ❌ | `.hf_cache/datasets/parquet` | 66G | **不能删** | 当前活跃训练的数据源 |
| ❌ | `.hf_cache/lerobot/hub` | 33G | **不能删** | lerobot 数据依赖 |
| ❌ | `openvla-libero-object` | 15G | **不能删** | C4-ext 训练的 base model |
| ❌ | `models/*` | 8.2G | **不能删** | RoboFlamingo 依赖 |

### 汇总

| 类别 | 可释放空间 |
|------|-----------|
| 安全删除 (P0-P3) | **~14.2G** |
| 需确认后删除 (P4-P5) | **~45G** |
| 不可删除 | ~122G |

安全删除 P0-P3 后可从 21G → ~35G free。如果确认 P4/P5 也可删，最多释放到 ~80G。

---
