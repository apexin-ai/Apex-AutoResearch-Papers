# 实验状态检查 — exp_037 & exp_038

**检查时间**: 2026-05-21

---

## exp_037_wide_critic_cheetah

| 项目 | 值 |
|------|-----|
| 服务器 | bjb1-45299 |
| PID | 14487 |
| 状态 | **ALIVE** |
| 运行时长 | 3h55m |
| 当前 step | **156000 / 210000** (74.3%) |
| FPS | 10.8 |

### 关键指标

| Step | eval_return | train_return (avg) | civo/ve_ratio | value_mean |
|------|-------------|-------------------|---------------|------------|
| 125000 | 286.8 | ~93 | 0.1 | 20.2 |
| 135000 | 238.9 | ~98 | 0.1 | 19.0 |
| 145000 | 186.5 | ~108 | 0.1 | 18.3 |
| 155000 | 182.4 | ~129 | 0.1 | 17.7 |

- gate_dt: 固定 2（gate_dt_2_frac=1.0）
- eval_return 下降趋势（286.8→182.4），但 train_return 在上升（93→129），存在 train-eval gap
- actor_loss ≈ 0, actor_grad_norm ≈ 0~0.1

---

## exp_038_dual_critic_walker_s2

| 项目 | 值 |
|------|-----|
| 服务器 | bjb1-40020 |
| PID | 175633 |
| 状态 | **ALIVE** |
| 运行时长 | 3h55m |
| 当前 step | **112000 / 210000** (53.3%) |
| FPS | 7.6 |

### 关键指标

| Step | eval_return | train_return (avg) | civo/ve_ratio | value_mean |
|------|-------------|-------------------|---------------|------------|
| 85000 | 344.7 | ~329 | 0.4 | 142.0 |
| 95000 | 311.8 | ~315 | 0.4 | 116.0 |
| 105000 | 283.1 | ~300 | 0.3 | 91.9 |

- gate_dt: 固定 2（gate_dt_2_frac=1.0）
- dual critic 正常工作：value1_mean ≈ value2_mean（差异 <0.3）
- eval_return 下降趋势（344.7→283.1），train_return 同步下降
- value_mean 持续走低（142→92），value function 在收缩

---

## 备注

- 两个实验 gate 均锁定 dt=2（gate_fixed_dt=2），未触发自适应
- exp_037 的 eval 下降但 train 上升，可能过拟合或 eval 噪声
- exp_038 的 train 和 eval 同时下降，且 value 持续收缩，需关注后续走势
