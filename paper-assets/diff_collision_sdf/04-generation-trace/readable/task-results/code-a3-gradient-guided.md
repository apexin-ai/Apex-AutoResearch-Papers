# code a3 gradient guided

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_a3_gradient_guided_20260519T224253_result.json`
- **Structured JSON:** [`6df543b1a169084f8c9c.json`](../../sessions/6d/6df543b1a169084f8c9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass: imports, class structure, TrainHooks interface, and end-to-end gradient flow (CPU smoke test).

## 产出报告

### 文件
| 文件 | 路径 |
|------|------|
| Gradient Refiner 模块 | `/root/colliforce-vla/colliforce/sdf_gradient_refiner.py` |
| A3 训练脚本 | `/root/colliforce-vla/scripts/train_a3_hook.py` |

### 架构设计

**SDFGradientRefiner** (无参数，纯计算模块)：
1. 从 suffix_out 均值池化 → EE 位置预测 → SDF 值
2. SDF < margin 的样本触发梯度修正
3. 计算 ∂SDF/∂suffix_out → 沿梯度方向偏移 suffix features (远离碰撞)
4. 原始 v_t 和修正后的 v_t_refined 通过 action_out_proj 计算
5. refine_loss = MSE(v_t, v_t_refined.detach()) — 训练模型直接输出安全动作

**Loss 构成 (Phase 2)**：
```
total = action_loss + 0.1 × sdf_loss + 0.01 × ee_loss + 0.1 × refine_loss
```

### 与 A1 的差异

| 维度 | A1 | A3 |
|------|----|----|
| SDF 角色 | 辅助任务，提升特征质量 | 梯度直接修正 action 预测 |
| 额外组件 | 无 | SDFGradientRefiner |
| Phase 2 Loss | action + sdf + ee | action + sdf + ee + **refine** |
| 新增参数 | 0 | 0 (refiner 无参数) |
| 新增超参 | 0 | alpha, margin, lambda_refine, grad_clip |

### 预期显存增量 (相对 A1)

- **Phase 1**: 零增量（refiner 不激活）
- **Phase 2**: ~200-500MB 额外
  - 每步额外前向：1次 SDF decoder (EE query) + 1次 action_out_proj (suffix_refined)
  - autograd.grad 用 `create_graph=False` → 不构建二阶计算图
  - 额外激活：suffix_refined [B, 50, 1024]、v_t [B, 50, 32]、v_t_refined [B, 50, 32]
  - 仅 near-collision 样本触发（非全 batch），实际开销视 refine_ratio 而定

### 使用方式
```bash
# Dry run (不占 GPU)
CUDA_VISIBLE_DEVICES=3 python scripts/train_a3_hook.py --scene spatial_bowl --dry_run

# 正式训练
CUDA_VISIBLE_DEVICES=3 python scripts/train_a3_hook.py --scene spatial_bowl --seed 0 \
    --refine_alpha 0.1 --refine_margin 0.01 --lambda_refine 0.1
```

---
