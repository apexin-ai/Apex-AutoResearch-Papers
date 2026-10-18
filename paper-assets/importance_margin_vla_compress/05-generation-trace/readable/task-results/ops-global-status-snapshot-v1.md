# ops global status snapshot v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_global_status_snapshot_v1_20260522T091720_result.json`
- **Structured JSON:** [`0fb27efb6a545290edae.json`](../../sessions/0f/0fb27efb6a545290edae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929

| GPU | 实验 | 状态 | SR/进度 |
|-----|------|------|---------|
| 0 | l2norm_k0.50_spatial_seed43 | 运行中 | T7 done 82%, cumul 59.0% (400/500) |
| 1 | random_k0.30_spatial_seed43 | 运行中 | T7 ep30/50, cumul ~46% (350/500) |
| 2 | l2norm_k0.30_spatial_seed43 | 运行中 | T7 done 84%, cumul 52.5% (400/500) |
| 3 | random_k0.30_object_seed43_v4 | 运行中 | T3 ep40/50, cumul ~36% (150/500) |

已完成（本机 eval_results）: l2norm_k0.85_obj=98.4%, l2norm_k0.70_obj=57.2%, random_k0.30_obj=32.2%, random_k0.50_spa=72.8%, random_k0.85_spa=57.6%, random_k0.93_obj=30.0%

## westd-27271

| GPU | 实验 | 状态 | SR/进度 |
|-----|------|------|---------|
| 0 | — | 空闲 | — |
| 1 | — | 空闲 | — |

已完成: l2norm_k0.95_obj=98.4%, l2norm_k0.85_spa=88.0%, l2norm_k0.70_spa=68.4%, random_k0.95_spa=76.8%, random_k0.70_spa=73.8%

## westd-41074

| GPU | 实验 | 状态 | SR/进度 |
|-----|------|------|---------|
| 0 | random_k0.85_object_seed43 | 运行中 | T6 ep10, cumul 3.7% (300/500) ⚠️ |
| 1 | — | 空闲 | l2norm_k0.925_obj 已完成 98.4% |
| 2 | train_m96 | 训练中 | 94650/100000 (94.7%) |
| 3 | train_m64 | 训练中 | 49900/100000 (49.9%) |

已完成: l2norm_k0.925_obj=98.4%, l2norm_k0.925_spa=97.0%, l2norm_k0.30_obj=55.4%, l2norm_k0.50_obj=33.6%, l2norm_k0.70_obj=56.4%, random_k0.50_obj=68.4%, random_k0.70_obj=73.8%, random_k0.85_obj=3.8%⚠️, random_k0.90_obj=9.6%⚠️, random_k0.95_obj=72.8%

## cqa1-33015

可达，4×4090 (24GB)

| GPU | 实验 | 状态 | SR/进度 |
|-----|------|------|---------|
| 0 | l2norm_k0.95_object_seed43 | 运行中 | T2 done 96%, cumul 97.3% (重复⚠️) |
| 1 | l2norm_k0.90_object_seed43 | 运行中 | T2 done 98%, cumul 99.3%, T3开始 |
| 2 | l2norm_k0.925_spatial_seed43 | 运行中 | T3 ep40/50, cumul ~98%+ (重复⚠️) |
| 3 | random_k0.50_spatial_seed43 | 运行中 | T2 ep40/50, cumul ~86% (重复⚠️) |

注意：cqa1 的 GPU0/2/3 是已完成实验的重复跑。仅 GPU1 l2norm_k0.90_object 是新实验。

## 汇总

**Spatial seed43: 7/14 完成，3 运行中，4 缺失**

| | k=0.30 | k=0.50 | k=0.70 | k=0.85 | k=0.90 | k=0.925 | k=0.95 |
|---|---|---|---|---|---|---|---|
| l2norm | ⏳T7 52.5% | ⏳T7 59.0% | ✅68.4% | ✅88.0% | ❌ | ✅97.0% | ❌ |
| random | ⏳T7 ~46% | ✅72.8% | ✅73.8% | ✅57.6% | ❌ | ❌ | ✅76.8% |

缺失 4 个: l2norm_k0.90, l2norm_k0.95, random_k0.90, random_k0.925

**Object seed43: 12/14 完成，2 运行中**

| | k=0.30 | k=0.50 | k=0.70 | k=0.85 | k=0.90 | k=0.925 | k=0.95 |
|---|---|---|---|---|---|---|---|
| l2norm | ✅55.4% | ✅33.6% | ✅57.2% | ✅98.4% | ⏳cqa1 T3 | ✅98.4% | ✅98.4% |
| random | ✅32.2% (v4重跑中) | ✅68.4% | ✅73.8% | ⏳T6 3.7%⚠️ | ✅9.6%⚠️ | ✅30.0% | ✅72.8% |

⚠️ random_k0.85 (3.8%) / random_k0.90 (9.6%) / random_k0.925 (30.0%) object 结果异常低（对比 random_k0.70=73.8%, k0.95=72.8%），可能有 bug。

**训练进度**: m96 94.7% (ETA ~10hr), m64 49.9% (ETA ~23hr)

**空闲 GPU**: westd-27271 ×2, westd-41074 GPU1 — 共 3 GPU 可部署缺失的 spatial 实验。

---
