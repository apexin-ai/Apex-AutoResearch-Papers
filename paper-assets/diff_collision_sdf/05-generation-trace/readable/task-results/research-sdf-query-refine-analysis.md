# research sdf query refine analysis

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sdf_query_refine_analysis_20260521T234052_result.json`
- **Structured JSON:** [`6e85348244c409ccb52f.json`](../../sessions/6e/6e85348244c409ccb52f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码已获取，以下是分析结论。

---

## 分析结果

### 1. 训练时 SDF query 位置

**SDFGradientRefiner** (`sdf_gradient_refiner.py:89-90`):
```python
ee_pred = ee_extractor(pooled)        # [B, 3] — 预测当前 EE 位置
sdf_at_ee = sdf_decoder(pooled, ee_pred.unsqueeze(1))  # 在当前 EE 处查 SDF
```

`ee_extractor` 的训练目标是 `observation.state[:, :3]`（`train_a3_hook.py:320-321`）：
```python
ee_gt = observation.state[:, :3].float()   # = robot0_eef_pos，当前 EE
ee_pred = self.ee_extractor(pooled)
ee_loss = F.mse_loss(ee_pred, ee_gt)
```

**训练时 SDF query 位置 = 预测的当前 EE 位置（目标是 robot0_eef_pos）。**

用途：判断当前状态是否需要 refinement（`sdf_at_ee < margin`）。如果需要，通过 `∂SDF/∂suffix_features` 在特征空间做梯度上升，shift features → 重新计算 action → 得到 collision-safe target。

### 2. Eval 时 SDF query 位置

**_refine_action_a3** (`eval_safelibero.py:313-317`):
```python
current_ee = obs.get("robot0_eef_pos", np.zeros(3))  # 当前 EE（未使用）
next_ee = action[:3]  # 目标位置
query = torch.tensor(next_ee, ...).requires_grad_(True)
sdf_val, sdf_grad = sdf_decoder(feat, query, return_gradients=True)
```

**Eval 时 SDF query 位置 = action[:3]（预测的目标位置）。**

用途：查目标位置的 SDF，如果 < margin，沿 `∂SDF/∂position`（空间梯度）直接 shift action[:3]。

### 3. 两者差异

| 维度 | 训练 | Eval |
|------|------|------|
| Query 位置 | 预测的**当前** EE | 预测的**目标** EE (action[:3]) |
| 梯度对象 | ∂SDF/∂features（特征空间） | ∂SDF/∂position（空间坐标） |
| 修改方式 | shift features → recompute action | 直接 shift action[:3] |

**两者不一致，但这是设计使然，不是 bug。** 原因：

- **训练**做的是特征空间 refinement：通过 SDF 梯度修改特征，让 model 学会直接输出 collision-safe 的 action。查当前 EE 是为了判断"当前状态是否处于碰撞风险区"。
- **Eval**做的是动作空间 refinement：直接调整输出 action 的目标位置。查目标位置更合理——要避免的是**移动到**碰撞区，不是判断当前是否在碰撞区。

SDF decoder 能泛化到 action[:3] 作为 query，因为它在训练时用的是工作空间中随机采样的 query points（`train_a3_hook.py:325`），不仅仅是 EE 位置。

### 4. 潜在问题与建议

**当前实现是合理的，不需要修复。** 但有一个微妙的 train-eval mismatch 值得注意：

训练时 refinement 的触发条件是"**当前** EE 处 SDF < margin"——如果 arm 当前远离碰撞区但正在向碰撞区移动，训练时不会触发 refinement，但 eval 时（查目标位置）会触发。这意味着 eval 的 refinement 覆盖了一些训练时没有被 refinement 覆盖的 case，但这实际上是一件好事——eval 时的空间 refinement 是额外的安全网。

**如果想让 train-eval 更一致**，可以考虑训练时也在目标位置（action[:3] 对应的 GT action position）查 SDF 来触发 refinement，但这会改变训练逻辑，需要实验验证。当前方案已经在工作，不建议贸然修改。

---
