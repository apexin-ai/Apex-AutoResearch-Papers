# ops audit westd38929 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd38929_v3_20260522T074057_result.json`
- **Structured JSON:** [`37893c7396a4f5dec31d.json`](../../sessions/37/37893c7396a4f5dec31d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 Python 进程均存活（PID 709233, 709369, 709608, 709985），正在加载模型权重，尚未到 GPU 阶段。这是正常行为——π0.5 模型大约需要 2-3 分钟加载到 GPU。

---

## 审计结果

| GPU | PID | 进程状态 | 显存 | 实验 | 行动 |
|-----|-----|---------|------|------|------|
| 0 | 603687→无 | 已完成 | 0 MiB | eval_pi05_random_k05_spatial_seed43 | 收割 → 重部署 |
| 1 | 486899→无 | 已完成 | 0 MiB | eval_pi05_random_k085_spatial_seed43 | 收割 → 重部署 |
| 2 | 562146→无 | 已完成 | 0 MiB | eval_pi05_l2norm_k085_object_seed43 | 收割 → 重部署 |
| 3 | 311261→无 | 已完成 | 0 MiB | eval_openvla_l2norm_k05_object_seed42_v5 | 收割 → 重部署 |

**空闲 GPU**: 0, 1, 2, 3（全部）

## 收割 metrics

| 实验 | Overall SR | Per-task SR |
|------|-----------|-------------|
| pi05_random_k0.50_spatial_seed43 | **72.8%** | 96, 72, 84, 48, 46, 48, 88, 80, 78, 88 |
| pi05_random_k0.85_spatial_seed43 | **57.6%** | 82, 62, 90, 8, 48, 38, 38, 74, 92, 44 |
| pi05_l2norm_k0.85_object_seed43 | **98.4%** | 100, 100, 100, 98, 100, 96, 98, 92, 100, 100 |
| openvla_l2norm_k0.50_object_seed42 | **39.2%** | 56, 14, 38, 32, 70, 32, 12, 50, 44, 44 |

## 新部署

| 实验 | GPU | PID | 二次确认 |
|------|-----|-----|---------|
| eval_pi05_l2norm_k05_spatial_seed43 | 0 | 709233 | ✓ 进程存活，模型加载中 |
| eval_pi05_random_k03_spatial_seed43 | 1 | 709369 | ✓ 进程存活，模型加载中 |
| eval_pi05_l2norm_k03_spatial_seed43 | 2 | 709608 | ✓ 进程存活，模型加载中 |
| eval_pi05_random_k0925_spatial_seed43 | 3 | 709985 | ✓ 进程存活，模型加载中 |

---
