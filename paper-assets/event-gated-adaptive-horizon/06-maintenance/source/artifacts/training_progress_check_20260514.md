# Training Progress Check — 2026-05-14

## 1. exp_008e_v3_walker_s1 (cuda:1, PID 898127) — Crown Jewel C6 Seed 1

| 指标 | 值 |
|------|-----|
| 状态 | ALIVE (elapsed: 8m40s) |
| 当前 step | 5,000 / 105,000 (4.8%) |
| eval_return @5K | 31.0 |
| value_mean @5K | 0.00175 |
| v/e ratio @5K | ~0.0 (value function 未收敛，太早无意义) |
| gate_dt_mean | 1.0 (fixed dt=1，符合预期) |
| fps | 尚未报告 (初始 prefill 阶段) |

### Normalized v/e 分析
太早，无法计算。需要至少到 25K 步才有参考意义。baseline @5K 无参考值，首个 baseline v/e 参考在 25K (0.087)。

### Delusional Critic 检查
数据不足，无法判断。value_mean = 0.002 vs target_mean = 0.183，value 远低于 target，目前正常。

### 预计完成时间
假设 fps 约 6-7（与 009a 类似，考虑 gate 开销），剩余 100K 步。预计 **~4-5 小时后完成**（约 2026-05-14 18:00-19:00 UTC）。

---

## 2. exp_009a_baseline_walker_s2 (cuda:0, PID 142508)

| 指标 | 值 |
|------|-----|
| 状态 | ALIVE (elapsed: 9h25m) |
| 当前 step | ~240,000 / 500,000 (48%) |
| 最新 eval_return @235K | 914.78 |
| value_mean @235K | 663.0 |
| v/e ratio @235K | 0.725 |
| fps | 7.67 |

### eval_return 轨迹

| Step | eval_return |
|------|-------------|
| 25K  | 325.3 |
| 45K  | 498.0 |
| 65K  | 688.9 |
| 85K  | 618.7 (回落) |
| 105K | 836.5 |
| 125K | 865.5 |
| 145K | 869.2 |
| 165K | 864.0 |
| 185K | 907.3 |
| 205K | 887.0 |
| **215K** | **956.0 (峰值)** |
| 225K | 892.1 |
| 235K | 914.8 |

### 与 exp_001 baseline 对比
- exp_001 最终 eval ~950
- 009a_s2 在 215K 已达 956.0（超过 exp_001 最终值）
- 当前 235K 处于 914.8，正常波动范围
- 训练健康，性能符合预期

### value_mean 分析
- v/e = 663.0 / 914.78 = 0.725
- value 低于 eval_return 约 27%，合理（DreamerV3 value 通常低于 actual return）
- 无 value overestimation 迹象

### 预计完成时间
剩余 260K 步 @ 7.67 fps = ~33,900 秒 = **~9.4 小时**，预计 **~2026-05-14 23:30 UTC**。

---

## 异常信号汇总

| 实验 | 状态 | 说明 |
|------|------|------|
| 008e_v3_s1 | 待观察 | 刚启动不到 10 分钟，需等待至少到 25K 步再检查 |
| 009a_baseline_s2 | 正常 | eval_return 健康增长，value 无过估，fps 稳定 |

## 建议下次检查时间
- **008e_v3_s1**: ~1 小时后（应到 ~25-30K 步，可计算首个有意义的 normalized v/e）
- **009a_baseline_s2**: ~3 小时后（应到 ~320K 步）
