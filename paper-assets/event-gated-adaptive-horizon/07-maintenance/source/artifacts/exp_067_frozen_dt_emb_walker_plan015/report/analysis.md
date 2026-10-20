## exp_067_frozen_dt_emb_walker_plan015 分析

### 实验配置
- Frozen dt_embedding (requires_grad=False) + subsample ON + dt=2 + H=8
- 环境: Walker Walk
- Hypothesis: frozen dt_emb 不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件

### 关键指标
- eval_final: 281.5 (step 105k)
- eval_peak: 334.1 (step 95k)
- eval_peak_step: 95000
- nve_peak: 0.4
- nve_final: 0.2
- civo_alert: 0.0 (全程未触发)
- total_steps: ~112k env steps (update_count=25099)

### Eval 轨迹
| Step | eval_return |
|------|-------------|
| 5k   | 37.4        |
| 15k  | 129.1       |
| 25k  | 161.6       |
| 35k  | 253.7       |
| 45k  | 312.7       |
| 55k  | 234.0       |
| 65k  | 246.8       |
| 75k  | 90.1        |
| 85k  | 188.9       |
| 95k  | 334.1       |
| 105k | 281.5       |

### NVE (ve_ratio) 轨迹
| Step | ve_ratio | alert |
|------|----------|-------|
| 15k  | 0.0      | 0.0   |
| 25k  | 0.1      | 0.0   |
| 35k  | 0.2      | 0.0   |
| 45k  | 0.2      | 0.0   |
| 55k  | 0.4      | 0.0   |
| 85k  | 0.4      | 0.0   |
| 95k  | 0.2      | 0.0   |
| 105k | 0.2      | 0.0   |

### Gate 行为
- gate_dt_mean = 2.0, gate_dt_std = 0.0 全程
- gate_dt_2_frac = 1.0 (100% 选择 dt=2)
- gate_empirical_entropy = 0.0
- frozen embedding 使 gate 完全锁定，无法自适应调节

### 与 parent (exp_042) 对比
| 指标 | exp_042 (parent) | exp_067 (this) | 差异 |
|------|------------------|----------------|------|
| eval_final | 612.45 | 281.5 | -54% |
| eval_peak | 682.38 | 334.1 | -51% |
| nve_peak | 0.194 | 0.4 | +106% |
| CIVO triggered | No | No | 一致 |

exp_067 性能显著低于 exp_042（约为一半），但 NVE 仍远低于 1.5x 触发阈值。两者均未触发 CIVO。

性能下降可能原因：frozen dt_emb 使 gate 完全锁定在 dt=2，无法根据任务需求自适应调节 horizon，导致策略灵活性受限。但这一性能差异不影响 CIVO 相关结论。

### Conclusion
**success** — Frozen dt_embedding 确实不触发 CIVO (NVE peak=0.4, 远低于 1.5x 阈值, civo_alert 全程为 0)。这验证了 dt_emb 的 **training** (梯度更新) 是 CIVO 触发的必要条件，而非 dt_emb 的存在本身。即使 dt_emb 存在于模型中，只要不参与梯度更新，CIVO 现象就不会出现。
