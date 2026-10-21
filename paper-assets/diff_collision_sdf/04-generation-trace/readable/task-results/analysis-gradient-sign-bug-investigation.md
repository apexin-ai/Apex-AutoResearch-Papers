# analysis gradient sign bug investigation

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_sign_bug_investigation_20260522T192002_result.json`
- **Structured JSON:** [`d13825f08bc5627458dc.json`](../../sessions/d1/d13825f08bc5627458dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在全部代码和实验结果已读完。下面是完整诊断。

---

## 诊断结果

### 1. Refine 公式的完整数学

**Eval** (`eval_safelibero.py:292-337`):
```
next_ee = current_ee + action[:3]          # delta→absolute
sdf_val, ∇SDF = sdf_decoder(feat, next_ee) # 空间梯度 ∂SDF/∂position
grad_dir = ∇SDF / ||∇SDF||
action_refined[:3] = action[:3] + alpha * grad_dir   # alpha=0.1
```

**Training** (`sdf_gradient_refiner.py`):
```
grad_suffix = ∂SDF/∂suffix_out              # 特征空间梯度
suffix_refined = suffix_out + alpha * grad_suffix
v_t_refined = action_out_proj(suffix_refined)
refine_loss = MSE(v_t, v_t_refined.detach())
```

### 2. 符号判断：**代码符号正确，没有 +/- 反向 bug**

两处都用 `+ alpha * gradient`（梯度上升），SDF 增大方向 = 远离障碍物。数学上无误。

### 3. SDF 约定：标准约定

`sdf_pipeline.py:97`: `sdf_stack.append(-raw)` — pysdf 返回正=内部，取反后 **SDF > 0 = 安全，SDF < 0 = 碰撞**。GT 数据 clip 到 [-0.05, 0.05]。`verify_collision_sign` 和 `verify_gradients`（90%+ accuracy）均验证通过。

### 4. 真正的 bug：不是符号错误，而是 SDF decoder 输出严重失标

**从 eval 日志看到的现象**：
- `eval_a3_object_m024fix_v11.log`: 每个 episode `refined=0` — **refinement 从未激活**
- 所有 episode 的 `sdf_min` 在 0.15-0.85 范围，远高于 `refine_margin=0.01`
- SDF decoder 认为 EE 始终远离障碍物，从不触发 refine

**根因** — `compute_sdf_loss` (`sdf_decoder.py:95-96`):
```python
pred_c = sdf_pred.clamp(-0.05, 0.05)   # ← 关键！
gt_c = sdf_gt.clamp(-0.05, 0.05)
sdf_l1 = (pred_c - gt_c).abs().mean()
```

`torch.clamp` 在饱和区梯度为零。如果 decoder 预测 0.5（GT=0.03），clamp 后 pred_c=0.05，loss=0.02，但 **∂loss/∂pred = 0**（clamp 饱和区无梯度）。模型永远收不到"把输出压回 0.05 以内"的梯度信号，预测值可以无约束地漂移到 0.3-0.9。

eval 时 `sdf_scalar < 0.01` 永远为 False → refine 永远不执行 → A3 等价于 baseline。

### 5. 训练 vs Eval refine 逻辑不匹配

| | 训练 | Eval |
|---|---|---|
| 梯度对象 | ∂SDF/∂suffix_out (特征空间) | ∂SDF/∂position (空间坐标) |
| 修改目标 | shift features → 模型输出新 action | 直接 shift action[:3] |
| 验证 | 有 refine_loss 反馈 | 纯启发式，无验证 |

训练教模型"当特征被 SDF 梯度调整后输出更安全的 action"，但 eval 做的完全是另一件事——在 action 空间做空间梯度修正。这两个操作数学上无关。

### 6. `sdf_gt` 是死代码

`--sdf_gt_path` 加载 GT 数据传入 `evaluate_task()`，但函数体内从未使用。所谓"oracle SDF"实验实际仍使用的是 learned decoder，不是真正的 oracle。

---

## 修复建议（按优先级）

**P0: 修复 SDF loss 的 clamp 问题** — `sdf_decoder.py:95`

```python
# 方案 A：用 soft clamp (如 tanh scaling)，保留梯度
pred_scaled = 0.05 * torch.tanh(sdf_pred / 0.05)
gt_c = sdf_gt.clamp(-0.05, 0.05)
sdf_l1 = (pred_scaled - gt_c).abs().mean()

# 方案 B（更简单）：加 range penalty
range_penalty = F.relu(sdf_pred.abs() - 0.05).mean()
losses["sdf_total"] = sdf_l1 + 0.5 * range_penalty
```

**P1: 实现真正的 oracle SDF refine** — 用 GT 点云做 nearest-neighbor 查询 + 数值梯度，验证空间梯度 refine 在理想 SDF 下是否有效。

**P2: 对齐 eval refine 和训练 refine** — eval 也在特征空间做 refine（∂SDF/∂suffix_out → shift suffix → action_out_proj 重投射），而非直接修改 action 坐标。这样 eval 的 refine 操作与训练时学到的 refine_loss 一致。

---
