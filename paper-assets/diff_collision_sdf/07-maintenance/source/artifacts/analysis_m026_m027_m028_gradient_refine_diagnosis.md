# M026-M028 Gradient Refinement 综合诊断 — 2026-05-22

## 诊断背景

Oracle M024fix 深度分析发现：85.6% episodes 冻结（fake safety），23/23 移动 episode 100% 碰撞。
启动 gradient 符号调查 + spatial 碰撞部位调查，发现 3 个新 bug + 1 个结构性限制。

## M026: SDF Decoder Clamp 零梯度导致输出失标

**代码位置**：`sdf_decoder.py:95-96`
```python
pred_c = sdf_pred.clamp(-0.05, 0.05)   # BUG: 饱和区梯度为零
gt_c = sdf_gt.clamp(-0.05, 0.05)
sdf_l1 = (pred_c - gt_c).abs().mean()
```

**机制**：decoder 预测 0.5（GT=0.03），clamp 后 pred_c=0.05，∂loss/∂pred = 0。
模型永远收不到"把输出压回 [-0.05, 0.05]"的梯度信号。

**影响**：decoder 输出漂移到 0.15-0.85 >> refine_margin(0.01) → refinement 永不触发。
这是所有 A3 eval 中 refined_count=0 的真正原因。

**修复方案**：
```python
# 方案 A: soft clamp
pred_scaled = 0.05 * torch.tanh(sdf_pred / 0.05)

# 方案 B: range penalty
range_penalty = F.relu(sdf_pred.abs() - 0.05).mean()
```

## M027: `sdf_gt` 死代码 — Oracle 实验标签无效

`--sdf_gt_path` 加载 GT 数据传入 `evaluate_task()`，但函数体内从未使用。
所有 "oracle" 实验实际使用 learned decoder，不是真正的 oracle。

**影响**：oracle_a3_force_refine 和 oracle_a3_m024fix 的 "oracle" 标签是假的。
需要实现真正的 oracle SDF（GT 点云 nearest-neighbor + 数值梯度）来验证方法上限。

## M028: 训练-Eval Refine 逻辑不匹配

| | 训练 (sdf_gradient_refiner.py) | Eval (eval_safelibero.py) |
|---|---|---|
| 梯度对象 | ∂SDF/∂suffix_out（特征空间）| ∂SDF/∂position（空间坐标）|
| 修改目标 | shift features → action_out_proj → 新 action | 直接 shift action[:3] |
| 作用空间 | 高维特征空间 | 3D 笛卡尔空间 |

训练教模型"当特征被 SDF 梯度调整后输出更安全的 action"。
Eval 做的是"在 action 空间沿 SDF 空间梯度修正"。
这两个操作数学上无关。

## Spatial Bowl 碰撞部位诊断

### 碰撞检测机制
```python
# eval_safelibero.py:426-435
displacement = np.sum(np.abs(current_pos - initial_pos))  # L1
if displacement > 0.001:  # 1mm threshold
    return True  # 任何 link 推动 obstacle 都算碰撞
```

### 关键证据
- 碰撞在 step 4-20 发生（EE 尚未到达目标）→ arm body 碰撞
- 6 个 obstacle 包围 workspace，moka_pot 碰撞体放大 1.6 倍
- Object suite CAR 80-96% vs Spatial CAR 0%（同 obstacle，不同 arm trajectory）

### 结论
EE-only SDF 在 spatial 场景天然无效。需要 whole-arm collision avoidance。

## 综合影响

A3 Runtime Refinement 遭遇四重失败：
1. M024: 坐标错误（已修复）
2. M026: decoder 失标（训练 bug，需重训）
3. M027: oracle 是假的（代码 bug，需实现真 oracle）
4. M028: train-eval 不匹配（设计问题，需对齐）

A1 路径不受影响：训练时 SDF signal 不依赖 runtime gradient。
