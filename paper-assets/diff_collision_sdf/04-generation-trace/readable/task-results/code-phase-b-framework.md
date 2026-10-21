# code phase b framework

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase_b_framework_20260519T174225_result.json`
- **Structured JSON:** [`f322b6ad64e0e143b325.json`](../../sessions/f3/f322b6ad64e0e143b325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。文件结构：

```
artifacts/src/
├── __init__.py
├── sdf_decoder.py          — SDF MLP (395K params), L1 clamped loss + Eikonal
├── sdf_gradient_refiner.py — 梯度引导 action refinement (1.05M extra params)
├── sdf_data.py             — 多场景 SDF GT 加载 + importance sampling
└── train_colliforce.py     — 两阶段训练骨架 + ColliForceConfig dataclass
```

关键设计决策：
- **SDF decoder** 完全复用 KG-3 验证通过的架构（4层 MLP, hidden=256, Softplus(beta=5), skip at layer 2），增加了 cross-attention aggregation 选项
- **Gradient refiner** 的 `GradientCorrection` 用 zero-init linear projection，确保训练初期 refinement 接近恒等映射，不干扰 backbone 收敛
- **collision cost** 用 `Softplus(-SDF + margin)` 替代 `ReLU`，梯度更平滑
- **EEPositionExtractor** 从 action features 学习到 3D 坐标的映射（需要后续用 FK 数据 supervise）
- 所有 `TODO` 标注了具体需要对接 openpi 的位置

需要后续补齐的部分：openpi 模型加载、suffix_out hook、LoRA 注入、tyro CLI、wandb 集成。

---
