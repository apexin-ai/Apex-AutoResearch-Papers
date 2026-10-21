# analysis m024 training code impact

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m024_training_code_impact_20260522T160514_result.json`
- **Structured JSON:** [`8a5ac870486d0c8d0c3d.json`](../../sessions/8a/8a5ac870486d0c8d0c3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。以下是详细报告。

---

## M024 坐标 Bug 影响范围报告

### 结论：训练代码 **没有** delta→absolute bug。Bug 仅存在于 eval 代码。

---

### 1. 训练代码 SDF 查询坐标的完整计算路径

`train_a3_hook.py` 的 `on_loss_computed()` (line 298) 中有三条 SDF 相关路径：

**路径 A — SDF 辅助 Loss（与 A1 相同）**：
```
SDF GT npz (固定的 workspace 坐标点)
  → sample_sdf_batch() 采样 query_pts [B, N, 3]
  → sdf_decoder(pooled, query_pts)
  → compute_sdf_loss(pred, gt)
```
查询点来自预计算的 GT 文件（`sdf_gt_spatial_bowl.npz`），是静态的 workspace 绝对坐标。**不涉及 action，无 bug。**

**路径 B — EE Loss**：
```
observation.state[:, :3]  ← 数据集中的 ground truth EE position
  → ee_gt (绝对坐标)
  → MSE(ee_extractor(pooled), ee_gt)
```
`state[:, :3]` 确认是 `eef_pos`（3D 世界坐标）。数据生成代码 `generate_training_data.py:226`：
```python
state = np.concatenate([eef_pos, eef_axisangle, gripper], axis=-1)  # 8-dim
```
所以 `state[:, :3]` = 绝对 EE 位置。**无 bug。**

**路径 C — 梯度精炼（Phase 2，A3 特有）**：
```
suffix_out → mean_pool → pooled [B, 1024]
  → ee_extractor(pooled) → ee_pred [B, 3]  (学习预测的绝对 EE 位置)
  → sdf_decoder(pooled, ee_pred.unsqueeze(1)) → sdf_at_ee [B]
  → 若 sdf < margin → 梯度上升 shift suffix → refine_loss
```
`SDFGradientRefiner.forward()` (sdf_gradient_refiner.py:86-90) 用 `ee_extractor` 预测 EE 位置，**不使用 action[:3]**。ee_extractor 的 GT 是绝对坐标，所以输出也是绝对坐标。**无 delta-as-absolute bug。**

---

### 2. 与 Eval 代码的对比

| | 训练代码 | Eval 代码 (bug) |
|---|---|---|
| SDF 查询坐标来源 | `ee_extractor(pooled)` — 预测的**当前** EE 绝对位置 | `action[:3]` — delta 位移，错误当作绝对坐标 |
| 坐标空间 | workspace 绝对坐标 ✓ | delta 空间（值域约 ±0.01），当作绝对坐标（值域约 0.1-0.8）✗ |
| 查询语义 | "机械臂现在是否在碰撞区" | 本意 "action 执行后是否会碰撞"，实际查询的位置完全错误 |

---

### 3. SDF Decoder 的 Input 语义

`sdf_decoder.py` 的 docstring (line 7-8)：
```
query_points: [B, N, 3] — 3D query positions in workspace coords
```
SDF GT 由 `sdf_pipeline.py` 生成，使用 MuJoCo 世界坐标（`world_verts = (geom_rot @ vertices.T).T + geom_pos`）。EE 位置同样是 MuJoCo 世界坐标。**两者在同一坐标空间。**

---

### 4. 影响评估

**A3 训练的 gradient signal 是正确的。** 具体来说：
- SDF 辅助 Loss → GT 点，正确 ✓
- EE Loss → GT 绝对位置，正确 ✓
- 梯度精炼 → ee_extractor 预测绝对位置，正确 ✓
- 已训练的模型权重**不受此 bug 影响**

Bug 仅影响 eval 推理时的 action refinement：`_refine_action_a3()` 把 delta action（量级 ~0.01）当作绝对坐标（正常量级 ~0.1-0.8）传给 SDF decoder，导致查询位置完全落在工作空间之外，SDF 预测值无意义。

---

### 5. 附带发现：训练 vs Eval 语义不对称

修复 eval bug 后仍存在一个设计层面的不对称：

- **训练**: 检查 SDF at **当前** EE（"机械臂现在安全吗？"）
- **Eval**: 检查 SDF at **下一步** EE（"action 执行后安全吗？"）

这意味着：
- 当前安全但 action 指向碰撞区 → 训练不触发精炼，eval 应该触发
- 当前在碰撞区但 action 指向安全区 → 训练触发精炼，eval 不应该触发

这不是 bug（训练用当前 EE 是合理的，因为要让特征编码碰撞感知），但可能影响 train-eval consistency。评估时如果想对齐训练逻辑，refinement 应该也用 `ee_extractor(suffix_features)` 预测当前 EE 位置来查 SDF，而不是用 action 推算下一步位置。

---

### 修复建议

**Eval 代码修复** (`eval_safelibero.py:317`)：
```python
# 修复方案 A: 与训练一致，用 ee_extractor 预测当前 EE
ee_pred = ee_extractor(feat)
query = ee_pred.unsqueeze(1)  # [1, 1, 3]

# 修复方案 B: 用正确的下一步绝对坐标
next_ee = current_ee + action[:3]  # delta → absolute
query = torch.tensor(next_ee, ...).reshape(1, 1, 3)
```

推荐方案 A，与训练语义一致。方案 B 语义更直观但与训练不对称。

---
