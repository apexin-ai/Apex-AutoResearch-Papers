# ssh plan012 clip action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan012-clip-action-probe_20260516T014922_result.json`
- **Structured JSON:** [`1d9f3a90795a75fa977e.json`](../../sessions/1d/1d9f3a90795a75fa977e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Same-code apples-to-apples comparison (MLP 1024→256→7, same seed/split/epochs):**

| Feature | cls_token R² | patch_mean R² |
|---------|-------------|--------------|
| **CLIP ViT-L/14** | 0.8046 | 0.7814 |
| **DINOv2 ViT-L** | 0.8137 | 0.8093 |

**Bootstrap CIs (task-level, 10k resamples):**
- **cls_token**: CLIP - DINO = -0.009, 95% CI [-0.020, +0.002], p=0.10 → **not significant**
- **patch_mean**: CLIP - DINO = -0.028, 95% CI [-0.034, -0.022], p<0.001 → DINO slightly better

**关键发现：** 初始 CLIP R²=0.81 看起来远高于之前 DINO=0.71 的参考值，但这是因为原始 probe 使用了不同超参数（DINO 17 epochs 就早停 vs CLIP 训练到 100 epochs）。用同一套代码重跑后，CLIP ≈ DINO（cls_token p=0.10）。

**结论：** CLIP RSA=0.557 >> DINO RSA=0.388，但 CLIP R² ≈ DINO R²。VL pretraining 增加 geometric alignment（RSA 高）但不增加 predictive content（R² 持平）。支持 geometric-functional dissociation 假说。

**注意：** 原始 Projector ref R²=0.706 来自不同代码，不直接可比。如需严格三方对比，需要用同一套代码重跑 Projector probe。

Registry `plan_012_clip_vit_control` 已更新。

---
