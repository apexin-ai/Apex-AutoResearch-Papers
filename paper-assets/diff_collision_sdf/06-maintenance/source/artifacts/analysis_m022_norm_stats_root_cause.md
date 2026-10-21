# M022 Action Collapse Root Cause Analysis — A3 Eval v11

**Date**: 2026-05-22  
**Server**: westd-35807, conda env `libero`  
**Eval file**: `v11_eval_safelibero_object_all_levelII_best_a3_seed0.json`

## 症状回顾

A3 eval v11 在 safelibero_object (4 tasks × 50 episodes = 200 episodes) 上:
- **TSR = 0%**（全部 200 episodes 均未完成任务）
- **73% episodes（146/200）** obstacle max_displacement < 1e-4（机器人几乎不动）
- displacement 聚集在 4 个浮点噪声值：5.58e-10, 2.05e-09, 4.98e-09, 1.16e-06（MuJoCo solver 数值漂移）
- 25.5%（51/200）episodes 发生了碰撞（displacement > 0.001）

## 1. A3 vs Baseline norm_stats 对比

**结论：完全相同，norm_stats 不是根因。**

| 维度 | A3 | Baseline |
|------|-----|---------|
| state dims | 8 | 8 |
| action dims | 7 | 7 |
| actions mean | [0.0735, 0.1231, -0.0319, 0.0022, 0.0049, -0.0096, 0.0920] | 同左 |
| actions std | [0.2026, 0.4856, 0.4882, 0.0253, 0.0491, 0.0399, 0.9958] | 同左 |
| q01/q99 | null | null |

A3 checkpoint 的 `assets/safelibero_object/norm_stats.json` 与 baseline checkpoint 的 `norm_stats.json` 字节级一致。不存在 SDF 相关的额外维度或不同的统计量。A1 的 norm_stats 也完全相同。

## 2. norm_stats 加载/应用链路

**结论：链路正确，无加载错误。**

加载路径：
```
_load_policy_a3()
  → 扫描 A3 checkpoint/assets/ 目录
  → load_norm_stats(a3_assets_dir, "safelibero_object")
  → 传入 create_trained_policy(config, PI0_BASE_WEIGHTS, norm_stats=a3_norm_stats)
  → Policy.__init__ 构建 Normalize/Unnormalize transforms
```

Normalize/Unnormalize 实现（`openpi/transforms.py`）：
- Normalize: `(x - mean) / (std + 1e-6)`
- Unnormalize: `x * (std + 1e-6) + mean`，支持 pad_to_dim

由于 A3 和 baseline 使用相同的 norm_stats，归一化链路不可能产生差异。

## 3. Action Collapse 的根因分析

### 3.1 排除项

| 假设 | 状态 | 证据 |
|------|------|------|
| norm_stats 差异 | ❌ 排除 | A3/baseline/A1 完全相同 |
| LoRA 参数未加载 | ❌ 排除 | 504 params loaded，98.1% nonzero，magnitudes ~0.01-0.02 |
| 模型本身不能产生多样动作 | ❌ 排除 | 诊断脚本验证 base+LoRA 模型对随机输入产生 49/50 unique position diffs |
| SDF 精炼破坏了动作 | ❌ 排除 | **refine_count = 0/200，SDF 精炼从未触发** |

### 3.2 关键发现：SDF 精炼从未触发

```
refine_count: mean=0.0, max=0, zero=200/200
SDF min: mean=0.7932, min=0.4636, below_margin(0.01)=0/200
```

SDF decoder 对所有位置预测 SDF >> refine_margin (0.01)，精炼条件 `sdf_scalar < refine_margin` 永远不满足。这意味着 **v11 eval 中 A3 的推理路径与"不带精炼的纯 LoRA 模型"完全等价**。

### 3.3 真正的根因：A3 LoRA 训练导致的退化

A3 eval pipeline 的等效形式（因为精炼从不触发）：

```
actions = policy.infer(obs)  # pi0_base + A3_LoRA
# _refine_action_a3() 被调用但 sdf > margin，action 原样返回
```

A3 LoRA 的训练过程（`train_a3_hook.py`）：
1. **Phase 1 (step 0-5000)**：LoRA 冻结，只训练 SDF decoder + EE extractor
2. **Phase 2 (step 5000+)**：解冻 LoRA，总 loss = action_loss + λ_sdf × sdf_loss + λ_ee × ee_loss + λ_refine × refine_loss

**refine_loss 的机制**：`SdfGradRefineHooks.on_loss_computed()` 中：
- 捕获 suffix_out features
- 用 SDF decoder 预测 EE 位置的 SDF
- 计算 ∂SDF/∂suffix_out
- 沿梯度方向 shift suffix_out → 得到 v_t_refined
- refine_loss = MSE(v_t, v_t_refined.detach())

这训练模型"直接输出已经安全的动作"。**但如果训练中的 SDF decoder 在尚未充分学习时给出噪声梯度信号，或者对所有任务相关轨迹都预测低 SDF（高危），refine loss 会将 LoRA 拉向一个保守的退化不动点——模型学会"不动就是最安全的"。**

### 3.4 证据链

```
pi0_base（通用预训练，不含 LIBERO 任务知识）
    + A3 LoRA（在 refine loss 下训练，可能学到保守策略）
    → 对真实 observation 输出近零动作
    → 机器人不动 → obstacle displacement ≈ 0（浮点噪声）
    → TSR = 0%（任务完全失败）
```

对比 baseline：
```
pi0_base + baseline LoRA（标准 action loss fine-tune，无 SDF 干扰）
    → 正常动作输出
    → 有一定 TSR
```

### 3.5 4 个离散 displacement 值的解释

4 个值（5.58e-10, 2.05e-09, 4.98e-09, 1.16e-06）是不同 obstacle body 在 MuJoCo solver 中的数值漂移。不同障碍物的质量、摩擦系数、solver 迭代顺序导致微小差异。这些不是"4 种 action 模式"，而是"完全不动"时不同物体的 sim noise signature。

## 4. 附带发现：`_refine_action_a3()` 坐标 bug

`eval_safelibero.py` 第 ~320 行：
```python
next_ee = action[:3]  # openpi AbsoluteActions: action is absolute target position
```

**action 是 delta action**（`extra_delta_transform=False`，LIBERO 数据本身就是 delta 格式），不是绝对坐标。正确写法应该是：
```python
next_ee = current_ee + action[:3]  # delta → absolute
```

当前这个 bug 是 **latent** 的（因为精炼从不触发），但一旦修复精炼触发条件，这个 bug 会导致：
- SDF 查询位置错误（查询 delta 值附近而非实际 EE 目标位置）
- 梯度方向错误 → 精炼把动作推向错误方向

## 5. 修复建议

### 优先级 P0：验证 LoRA 退化假设

```bash
# 用 A3 checkpoint 但关闭精炼，确认问题在 LoRA 本身
python scripts/eval_safelibero.py \
    --model_type a3 --no_refine \
    --checkpoint <A3_ckpt> \
    --config_name pi0_libero_low_mem_finetune \
    --suite safelibero_object --task_id 0 --n_episodes 10
```

如果 `--no_refine` 仍然 TSR=0%，则确认是 LoRA 退化（而非 eval pipeline bug）。

### 优先级 P1：修复坐标 bug

```python
# _refine_action_a3() 中修改
current_ee = obs.get("robot0_eef_pos", np.zeros(3))
next_ee = current_ee + action[:3]  # delta → absolute
```

### 优先级 P2：重训 A3

训练策略调整：
1. **降低 λ_refine** 或使用 curriculum schedule（前期低后期高），防止 refine loss 在 SDF decoder 未收敛时干扰 LoRA
2. **验证 SDF decoder 训练时的校准**：检查训练日志中 sdf_loss 曲线，确认 decoder 在 Phase 2 开始时已收敛
3. **增加 action_loss 权重**：确保 task completion 信号不被 safety objectives 淹没
4. **考虑用 baseline fine-tuned 权重作为 A3 base**：而非 pi0_base，这样 LoRA 只需学习 safety delta，不需要同时学习 task knowledge

### 优先级 P3：增加诊断工具

- 在 eval 中记录每步 action 的 L2 norm，直接检测 action collapse
- 记录 EE trajectory 的 total displacement，区分"不动"和"原地打转"
- 对比 A3 `--no_refine` vs baseline 的 action distribution
