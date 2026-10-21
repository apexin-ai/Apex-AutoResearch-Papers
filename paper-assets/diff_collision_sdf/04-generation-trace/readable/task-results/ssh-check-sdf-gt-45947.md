# ssh check sdf gt 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_sdf_gt_45947_20260521T071910_result.json`
- **Structured JSON:** [`16cb0cafeb149a7fc153.json`](../../sessions/16/16cb0cafeb149a7fc153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. sdf_gt 文件

westd-45947 上存在的 sdf_gt 文件：

| 文件 | 路径 | 大小 |
|------|------|------|
| sdf_gt_object_chocolate.npz | `/root/colliforce-vla/data/` | 114 KB |
| sdf_gt_spatial_bowl.npz | `/root/colliforce-vla/data/` | 114 KB |
| sdf_gt_spatial_bowl.npz.bak | `/root/colliforce-vla/data/` | (备份) |

**sdf_gt_object_pudding.npz 不存在**——westd-45947 上也没有。

### 2. A3 Checkpoint

| 实验 | 路径 | 已保存 step | 大小 | best_loss |
|------|------|------------|------|-----------|
| spatial_bowl | `/root/autodl-tmp/checkpoints/a3_grad_refine_spatial_bowl/a3_grad_refine_spatial_bowl_seed0/` | 16000, 18000, **20000** (best) | 29G | 0.02306 @ step 20000 |
| object_pudding | `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/` | 18000, 20000 (best), **22000** | 29G | 0.02044 @ step 20000 |

### 3. 服务器间连通性

westd-45947 上 **没有 ~/.ssh/config**，无法直接 SSH 到 westd-35807。文件传输需通过本地中转或其他方式。

### 4. 磁盘空间

`/root/autodl-tmp`: 250G 总量，71G 已用，**180G 可用 (29%)**

### 5. A3 训练进度

| 实验 | 当前 step | 进度 | 最新 loss | 速度 |
|------|----------|------|----------|------|
| spatial_bowl | **20980**/30000 | 70% | ~0.027 | ~4.0 s/it |
| object_pudding | **23117**/30000 | 77% | ~0.022 | ~4.0 s/it |

两个训练都在正常运行，预计剩余约 10h (spatial_bowl) 和 7.7h (object_pudding)。

---
