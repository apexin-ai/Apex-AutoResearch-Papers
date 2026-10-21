# audit cqa1 refresh 20260522T2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_refresh_20260522T2_20260522T204555_result.json`
- **Structured JSON:** [`a964b4028b1fa8442c90.json`](../../sessions/a9/a964b4028b1fa8442c90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full audit report for **cqa1-33015**:

---

## GPU 状态表

| GPU | VRAM Used | Util | 实验 | 状态 |
|-----|-----------|------|------|------|
| 0 | 15437/24564 MiB | 75% | OpenVLA baseline spatial (k=1.0 chain) | **⚠️ 0% SR on 8/10 tasks — 废跑** |
| 1 | loading... | - | **新部署**: SmolVLA chain (baseline→l2norm k0.9→random k0.9) × Spatial + Goal | 刚启动 |
| 2 | 10140/24564 MiB | 27% | pi0.5 Random k=0.3 Goal | Task 5/10, 累计 47.7%, ~1.5h remaining |
| 3 | loading... | - | pi0.5 L2norm k=0.9 Long → k=0.85 chain | 刚加载模型 |

## 收割结果

| 实验 | Suite | SR | 备注 |
|------|-------|-----|------|
| pi05 baseline seed42 | Long | **91.6%** | |
| pi05 baseline seed43 | Long | 90.4% | |
| pi05 baseline seed43 | Goal | 96.4% | |
| pi05 L2norm k=0.95 seed42 | Long | **86.8%** | -4.8pp vs baseline |
| pi05 L2norm k=0.95 seed42 | Goal | **89.4%** | ← registry 已更新 DONE |
| pi05 Random k=0.7 seed42 | Goal | 80.6% | |
| pi05 Random k=0.5 seed42 | Goal | 74.4% | |

## ⚠️ 严重问题：OpenVLA baseline spatial = 0%

OpenVLA baseline (`/root/autodl-tmp/openvla-libero-spatial`) 在 Spatial 全部 8 个已完成 task 上 **0/400 = 0.0%**。这个模型是 spatial-finetuned 的，却完全无法执行 spatial 任务。后续链（k=0.95, k=0.9, k=0.7）也不可能有结果。

**建议：kill 掉 GPU 0 的 OpenVLA chain**，腾出 GPU 0 部署其他实验（如 SmolVLA Long suite chain）。等你确认。

## 新部署

**GPU 1** — SmolVLA 6 实验 chain:
1. baseline Spatial → 2. L2norm k=0.9 Spatial → 3. Random k=0.9 Spatial
4. baseline Goal → 5. L2norm k=0.9 Goal → 6. Random k=0.9 Goal

## Registry 说明

用户提到的 `eval_smolvla_official_l2norm_k090_object_seed42` 和 `eval_smart_compress_m32_official` 在 registry 中不存在（可能从未注册或已被清理）。对应 JSON 结果文件存在于服务器上。

---
