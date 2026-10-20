# Hopper Contingency 调研报告

## 1. 环境可用性

**可用：YES**

- **正确 task string**: `dmc_hopper_hop`（DMC Hopper 只有 `stand` 和 `hop` 两个 task，无 `walk`）
- **Action dim**: 4（torso + thigh + leg + foot）
- **Obs dim**: position(6) + velocity(7) + touch(2) = 15 维 proprio
- **Config**: `--configs defaults dmc_proprio` 完全支持，之前已多次成功运行
- **EGL**: 不需要。`dmc_proprio` 模式用 MLP encoder，不渲染图像（GLFW warning 可忽略）

## 2. 历史实验 Kill 原因汇总

### exp_104 ~ exp_108（5 个）
- **原因**: 设计问题。早期批次创建后 ~8 分钟即被 abort，无 command/metrics 记录。被 `exp_hopper_*` 长名系列替代。

### exp_hopper_trained_s1
- **原因**: 设计问题。s0 已完成且结论明确（severe_learning_delay → 非 CIVO），s1 复制无额外价值，被 kill 以释放 GPU。

### exp_hopper_frozen_s1
- **原因**: 设计问题。运行 2.4 分钟后 kill。frozen_s0 + ext 已显示 persistent_phantom_value，s1 不再需要。

**结论：所有 kill 均为资源/设计决策，无技术障碍。代码完全可用。**

## 3. 已有实验结果速览

| 实验 | 条件 | eval_return | NVE pattern |
|------|------|-------------|-------------|
| exp_hopper_baseline | dt=1, no gate | **96.43** | 稳定 (ve_final=0.559) |
| exp_hopper_trained_s0 | gate+dt=2, trained dt_emb | 3.26 → 81.58 (ext) | severe_learning_delay → recovered |
| exp_hopper_frozen_s0 | gate+dt=2, frozen dt_emb | 0 → 0.56 (ext) | persistent_phantom_value, 未恢复 |
| exp_hopper_no_dt_emb_s0 | gate+dt=2, no dt_emb | 10.76 (11.2%) | gate 本身导致 delay |

### 关键发现
- Hopper baseline **NVE 稳定** (ve_ratio_final=0.559, peak 3.48 transient)，适合做 clean baseline
- 但 gate 机制在 Hopper 上引发 **severe learning delay**，而非 Walker/Cheetah 的标准 CIVO
- trained vs frozen 差异：trained 最终恢复 (81.58)，frozen 始终无法恢复 (0.56)——模式与 Walker/Cheetah 不同

## 4. 推荐实验命令

### Baseline (dt=1, no gate)
```bash
python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_hopper_hop \
  --logdir logdir/exp_hopper_baseline_s0 \
  --steps 105000 --seed 0 \
  --compile False --device cuda:0
```

### 训练时长预估
- 105K steps ≈ **2.9 小时**（单 GPU，参考 exp_hopper_baseline: 12318s）
- 150K steps ≈ **4.6 小时**（参考 ext 实验: +6000s for 45K extra steps）

## 5. 风险与注意事项

1. **Hopper 不展示标准 CIVO**：gate 机制本身在 Hopper 上导致 severe learning delay，与 Walker/Cheetah 的 CIVO onset 机制不同。如果目标是 "CIVO isolation baseline"，Hopper baseline 的 NVE 确实干净 (< 1.5×)，但 gate 实验的 failure mode 是 learning delay 而非 value overestimation。
2. **已有 baseline 数据**：`exp_hopper_baseline` 已完成且数据齐全 (eval_return=96.43)，如无需额外 seed 可直接复用。
3. **logdir 已存在**：服务器上有 `exp_hopper_baseline`, `exp_hopper_trained_s0`, `exp_hopper_frozen_s0` 等 logdir，新实验需用不同名避免覆盖。
4. **DMC Hopper 无 "walk" task**：只有 `stand` 和 `hop`，任务书中的 "Hopper Walk" 应更正为 **Hopper Hop**。
