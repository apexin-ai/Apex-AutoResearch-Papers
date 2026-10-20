# analysis gradient cka scripts v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_cka_scripts_v2_20260523T034132_result.json`
- **Structured JSON:** [`92dbf1af4343138b546f.json`](../../sessions/92/92dbf1af4343138b546f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. 代码结构理解

| 组件 | 类名/路径 |
|---|---|
| 模型 | `OpenVLAForActionPrediction` (Llama-2-7B + DINOv2-L + SigLIP-SO400M) |
| Vision Backbone | `PrismaticVisionBackbone`: DINOv2 24 blocks (1024d) + SigLIP 27 blocks (1152d) → 2176d concat features, 256 patches |
| OCC Head | `BEVOccupancyHead`: Linear(2176→256) → ConvT(32) → ConvT(64) → Conv1x1, 带 BatchNorm2d |
| Depth Head | `DepthHead`: 同结构 + ReLU 输出 |
| Action Head | `L1RegressionActionHead`: MLPResNet, input_dim=llm_dim(4096) |
| Loss | action: L1Loss; occ: FocalLoss; depth: SmoothL1Loss |
| Detach 机制 | `patch_features.detach()` 在传入 aux head 前切断梯度 |
| Checkpoint | merged model (safetensors) + 单独的 `action_head/occ_head/depth_head/proprio_projector` pt 文件 |

### 2. 脚本全部跑通

三个脚本 (`gradient_analysis.py`, `cka_analysis.py`, `cka_compare.py`) 均已在 westd-34685 上验证通过。
- 需要 `batch_size=2`（batch_size=4 会 OOM，7B 模型 forward+backward 占 ~60GB）
- `labels` 必须 `.to(device)` 才能与 CUDA tensor 配合
- 数据有 1 个 task 缺少 occ/depth 标签（`pick_up_the_black_bowl`），脚本正确跳过

### 3. Full OCC 梯度分析（cutoff_s0, 20 batches）

| 指标 | 观察 |
|---|---|
| **Action grad norm** | DINOv2 逐层递增（0.11→0.50），SigLIP 相对平稳（0.08-0.17） |
| **Aux (OCC) grad norm** | 比 action 小 ~20x（0.006→0.052），同样后层较大 |
| **Cosine similarity** | 全部接近 0（-0.013 ~ +0.018），两组梯度近似正交 |
| **Conflict rate** | DINOv2 全层 ~50%（随机）；**SigLIP 后层 (17→25) 从 46% 降至 19%**，表明 aux 梯度方向与 action 梯度同向 |

### 4. Depth 梯度分析对比

| 指标 | Full OCC vs Depth |
|---|---|
| **Aux grad norm** | Depth aux 梯度比 OCC 大 **10-20x**（DINOv2-22: OCC=0.052 vs Depth=1.046；SigLIP: OCC=0.01-0.03 vs Depth=0.3-0.6） |
| **Cosine similarity** | 两个条件都 ~0 |
| **Conflict rate 模式** | 两个条件完全一致：SigLIP 后层 conflict rate 都降到 ~19% |

关键发现：**Depth 信号比 OCC 强约一个数量级**，但两者在 SigLIP 后层的梯度方向对齐模式相同（conflict rate 同步下降到 ~19%），说明这是 encoder 结构特性而非 task-specific 的。

### 5. CKA 分析

Full OCC vs Depth 的 cross-condition Linear CKA (100 images, 12 probe layers):
- **均值对角 CKA = 0.108**，两个条件在 encoder 中产生了显著不同的表征
- SigLIP 中层 (siglip_10~21) CKA 最高 (~0.13-0.20)
- DINOv2 早期层 CKA 最低 (~0.05)

### 6. 注意事项

- **Checkpoint 路径**：任务中给的 `occ_s1_fresh` 路径不存在，实际使用了 `cutoff_s0`（有 occ_head）和 `depth_s0`（有 depth_head）
- **dino_23 / siglip_26 梯度全零**：正常，模型使用 `get_intermediate_layers(n={num_blocks-2})`，最后一个 block 无梯度流过
- **生产运行建议**：增加到 `num_batches=200`、`num_images=500` 以获得更稳定的统计量；可考虑加入 Vanilla 和 Detach OCC 条件

---
