# ops fix gradient analysis launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_gradient_analysis_launch_20260523T181026_result.json`
- **Structured JSON:** [`ab8c83d3d7be9be0f9be.json`](../../sessions/ab/ab8c83d3d7be9be0f9be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete gradient analysis comparison:

---

## 关键梯度数据对比表（4 Conditions × 201 batches）

### 1. Action Gradient Norm — DINOv2 (代表层)

| Layer | Vanilla | Full OCC | Random OCC | **Detach** | Detach/Van 比 |
|-------|---------|----------|------------|------------|--------------|
| dino_0 | 0.069 | 0.062 (0.90×) | 0.071 (1.03×) | **0.006** | **0.08×** |
| dino_7 | 0.157 | 0.145 (0.92×) | 0.167 (1.07×) | **0.002** | **0.01×** |
| dino_8 | 0.221 | 0.193 (0.87×) | 0.235 (1.06×) | **0.004** | **0.02×** |
| dino_14 | 0.207 | 0.190 (0.92×) | 0.235 (1.13×) | **0.004** | **0.02×** |
| dino_17 | 0.264 | 0.245 (0.93×) | 0.301 (1.14×) | **0.009** | **0.03×** |
| dino_22 | 0.352 | 0.318 (0.90×) | 0.386 (1.10×) | **0.031** | **0.09×** |

### 2. Action Gradient Norm — SigLIP (代表层)

| Layer | Vanilla | Full OCC | Random OCC | **Detach** | Detach/Van 比 |
|-------|---------|----------|------------|------------|--------------|
| siglip_0 | 0.097 | 0.109 (1.12×) | 0.098 (1.01×) | **0.005** | **0.06×** |
| siglip_8 | 0.087 | 0.099 (1.14×) | 0.087 (1.00×) | **0.003** | **0.04×** |
| siglip_16 | 0.067 | 0.073 (1.09×) | 0.065 (0.97×) | **0.004** | **0.06×** |
| siglip_25 | 0.108 | 0.105 (0.97×) | 0.118 (1.09×) | **0.014** | **0.13×** |

### 3. Gradient Interaction（仅 Full OCC 和 Random OCC 有 aux 梯度流）

| 指标 | Full OCC (DINOv2) | Full OCC (SigLIP late) | Random OCC (DINOv2) | Random OCC (SigLIP late) |
|------|-------------------|----------------------|---------------------|------------------------|
| Cosine Similarity | **≈ -0.01** | ≈ 0.002 | ≈ +0.006 | ≈ +0.018 |
| Conflict Rate | **≈ 50%** (随机) | ≈ 24% (轻微对齐) | ≈ 50% (随机) | ≈ 23% (轻微对齐) |
| Aux Grad Norm | 0.023–0.098 | 0.232 | 0.008–0.034 | 0.070 |

### 4. 核心结论

**Q: OCC 辅助头是通过梯度放大还是隐式正则化起作用？**

**A: 隐式正则化（gradient flow health），不是梯度放大。** 证据链：

1. **Full OCC ≈ Vanilla**：action grad norm 比值 0.87–1.14×，没有显著放大或压制。OCC 辅助头的存在没有改变 action 梯度的量级。

2. **Random OCC ≈ Vanilla**：即使辅助目标是随机噪声（无语义信息），action grad norm 仍然健康（1.00–1.14×）。说明辅助头的语义内容不重要，**重要的是梯度流本身**。

3. **Detach → 灾难性崩塌**：梯度范数骤降至 Vanilla 的 **1%–13%**（中间层最严重，低至 1%）。Detach 切断了辅助头对 encoder 的梯度流，encoder 失去了维持梯度传播的"供养"，action 梯度也跟着崩塌。

4. **Cosine ≈ 0，Conflict ≈ 50%**：action 与 aux 梯度方向近似正交/随机，排除了方向性引导（directional guidance）假说。

**机制解释**：辅助头训练过程中通过 encoder 反向传播的额外梯度信号，防止了 frozen backbone + LoRA 训练中的梯度消失/特征退化。这是一种 **gradient flow regularization** 效应 —— 辅助头的存在维持了 encoder 的梯度通道健康，而非直接"教"encoder 什么方向更好。Detach 条件断掉这条通道后，encoder 梯度立即崩塌到接近零，导致下游 action 性能骤降。

---
