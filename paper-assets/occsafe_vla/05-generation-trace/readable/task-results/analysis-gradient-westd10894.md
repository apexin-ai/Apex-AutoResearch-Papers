# analysis gradient westd10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_westd10894_20260523T034851_result.json`
- **Structured JSON:** [`4d10e8ac368f1f5da4f4.json`](../../sessions/4d/4d10e8ac368f1f5da4f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 梯度分析报告

### 1. 代码结构

| 组件 | 类名 | 位置 |
|------|------|------|
| 主模型 | `OpenVLAForActionPrediction` (wraps `PrismaticForConditionalGeneration`) | `prismatic/extern/hf/modeling_prismatic.py` |
| OCC Head | `BEVOccupancyHead` (in_dim=2176, out_res=64, ConvTranspose2d decoder) | `prismatic/models/occ_head.py` |
| Action Head | `L1RegressionActionHead` (MLP, input_dim=4096) | `prismatic/models/action_heads.py` |
| Vision Backbone | `PrismaticVisionBackbone` (fused, embed_dim=2176) | `prismatic/extern/hf/modeling_prismatic.py` |

**Encoder 层名列表：**
- DINOv2 ViT-L/14: `featurizer.stem`, `featurizer.blocks.{0-23}` (24 blocks, 1024-dim)
- SigLIP ViT-SO400M/14: `fused_featurizer.stem`, `fused_featurizer.blocks.{0-26}` (27 blocks, 1152-dim)
- 注：`blocks.23` (DINOv2) 和 `blocks.26` (SigLIP) 梯度恒为零，为 timm register-token 架构特性

---

### 2. Random OCC s2: Action vs OCC 梯度范数

avg_action_loss=0.236, avg_occ_loss=0.059

| 层 | Action Grad Norm | OCC Grad Norm | 比值 (action/occ) |
|----|-----------------|---------------|-------------------|
| featurizer.stem | 0.700 | 0.028 | 25.0x |
| featurizer.blocks.0 | 0.071 | 0.003 | 22.2x |
| featurizer.blocks.8 | 0.237 | 0.010 | 24.5x |
| featurizer.blocks.22 | 0.393 | 0.045 | 8.7x |
| fused_featurizer.stem | 0.137 | 0.006 | 22.8x |
| fused_featurizer.blocks.0 | 0.038 | 0.006 | 6.3x |
| fused_featurizer.blocks.25 | 0.121 | 0.026 | 4.7x |

Action 梯度在所有层都显著大于 OCC 梯度。DINOv2 侧差距更大（8-25x），SigLIP 侧较小（5-23x）。两个 backbone 的梯度范数都随深度递增。

---

### 3. Detach vs Random OCC: Action Gradient Norm 差异

| 层 | Random OCC (action) | Detach (action) | 放大倍数 |
|----|--------------------|-----------------|---------| 
| featurizer.stem | 0.700 | 0.011 | **62.2x** |
| featurizer.blocks.0 | 0.071 | 0.006 | **11.4x** |
| featurizer.blocks.8 | 0.237 | 0.004 | **64.9x** |
| featurizer.blocks.22 | 0.393 | 0.032 | **12.3x** |
| fused_featurizer.stem | 0.137 | 0.002 | **68.5x** |
| fused_featurizer.blocks.0 | 0.038 | 0.002 | **19.0x** |
| fused_featurizer.blocks.25 | 0.121 | 0.015 | **8.3x** |

**核心发现：OCC 梯度流将 action 梯度放大了 8-69 倍。** Detach 条件下 OCC 梯度全部为零（符合预期），但 action 梯度本身也显著更弱。同时 Detach 的 action_loss（0.434）远高于 Random OCC（0.236），说明没有 OCC 梯度流时 action 学习效果更差。

---

### 4. Cosine Similarity 分布（Random OCC s2）

| 指标 | DINOv2 范围 | SigLIP 范围 |
|------|------------|------------|
| Mean cosine sim | -0.006 ~ +0.027 | -0.006 ~ +0.005 |
| Std | 0.075 ~ 0.101 | 0.017 ~ 0.048 |
| Conflict rate | 42% ~ 47% | 47% ~ 57% |

Action 和 OCC 梯度方向**近乎正交**（cosine similarity ≈ 0），冲突率接近随机水平（50%）。这意味着 OCC 梯度流不是通过"对齐方向"帮助 action 学习，而是通过**丰富梯度景观**（增大梯度幅度、提供更多训练信号）间接增强了 vision backbone 的表征学习。

---

### 5. 生成文件

服务器 `westd-10894:/root/occsafe_vla/analysis/results/`：

| 文件 | 说明 |
|------|------|
| `random_occ_s2_gradient_stats.json` | Random OCC 逐层统计 |
| `random_occ_s2_gradient_raw.json` | Random OCC 逐 batch 原始数据 |
| `random_occ_s2_gradient_analysis.{pdf,png}` | Random OCC 4-panel 图 |
| `detach_s2_gradient_stats.json` | Detach 逐层统计 |
| `detach_s2_gradient_raw.json` | Detach 逐 batch 原始数据 |
| `detach_s2_gradient_analysis.{pdf,png}` | Detach 4-panel 图 |
| `gradient_comparison.{pdf,png}` | 两条件对比 4-panel 图 |

脚本：
- `/root/occsafe_vla/analysis/gradient_analysis.py` — 梯度分析主脚本
- `/root/occsafe_vla/analysis/compare_gradients.py` — 对比可视化脚本

已注册 artifact: `gradient_analysis_results` (art_20260523_70512d)

---
