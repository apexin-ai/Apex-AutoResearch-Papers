## exp_032b_dual_critic_walker_s1 分析

### 训练概况
- 总步数: 224K env steps, 52599 update counts
- 训练时长: 6.42 hours
- 最终 eval return: **516.0** (@ 215K)
- Peak eval return: **551.8** (@ 205K)
- 最终 NVE (ve_ratio): **0.1** (@ 215K)
- Peak NVE: **1.4** (@ 85K)
- 训练正常完成 (EXIT_CODE=0)
- Checkpoint: logdir/exp_032b_dual_critic_walker_s1/latest.pt

### NVE 轨迹

| Step | NVE | Alert | 备注 |
|------|-----|-------|------|
| 15K  | 0.0 | 0 | 初始 |
| 25K  | 0.2 | 0 | |
| 35K  | 0.4 | 0 | |
| 45K  | 0.8 | **1** | 唯一一次 alert 触发 |
| 55K  | 0.7 | 0 | |
| 65K  | 0.7 | 0 | |
| 75K  | 0.7 | 0 | |
| 85K  | **1.4** | 0 | ← **Peak NVE** |
| 95K  | 0.7 | 0 | 开始下降 |
| 105K | 0.5 | 0 | |
| 115K | 0.9 | 0 | 小幅回升 |
| 125K | 0.3 | 0 | 快速下降 |
| 135K | 0.4 | 0 | |
| 145K | 0.3 | 0 | |
| 155K | 0.2 | 0 | |
| 165K | 0.2 | 0 | |
| 175K | 0.2 | 0 | |
| 185K | 0.1 | 0 | 稳定低位 |
| 195K | 0.1 | 0 | |
| 205K | 0.1 | 0 | |
| 215K | 0.1 | 0 | |

NVE 全程 < 1.5。Peak 1.4 在 85K 出现后迅速回落，125K 之后稳定在 0.1-0.4 区间。Dual-critic min(Q1,Q2) 有效抑制了 value overestimation。

### Eval Return 轨迹

| Step | Eval Return | vs Baseline (~900) |
|------|-------------|-------------------|
| 5K   | 31.0   | 3% |
| 15K  | 183.8  | 20% |
| 25K  | 121.8  | 14% |
| 35K  | 157.9  | 18% |
| 45K  | 105.9  | 12% |
| 55K  | 174.5  | 19% |
| 65K  | 209.7  | 23% |
| 75K  | 240.8  | 27% |
| 85K  | 108.9  | 12% |
| 95K  | 174.3  | 19% |
| 105K | 227.8  | **25%** (baseline @105K: ~900) |
| 115K | 111.4  | 12% |
| 125K | 321.5  | 36% |
| 135K | 224.1  | 25% |
| 145K | 312.3  | 35% |
| 155K | 360.8  | 40% |
| 165K | 342.3  | 38% |
| 175K | 406.3  | 45% |
| 185K | 433.8  | 48% |
| 195K | 543.5  | 60% |
| 205K | 551.8  | **61%** ← peak |
| 215K | 516.0  | 57% |

Eval return 持续上升但极其缓慢，在 224K 步时仅达到 baseline 的 ~57%。训练结束时仍有上升趋势但斜率放缓。

### 其他观察

- **Gate 完全坍塌**: gate_dt_2_frac = 1.0 全程不变，gate 未利用任何多速率能力（entropy=0.0）。Adaptive horizon 机制在此配置下无效。
- **Value1 ≈ Value2**: 两个 critic 输出几乎一致（差异 < 0.5），min(Q1,Q2) 并未产生显著的保守估计效应。
- **Actor loss ≈ 0**: 后期 actor_loss 接近 0，表明 actor 梯度信号极弱，学习停滞。

### Conclusion: **NEGATIVE**

理由: NVE 控制良好（peak 1.4 < 1.5，无 CIVO 爆发），但 eval return 仅达 baseline 的 57%（516 vs ~900），远未 match baseline。Dual-critic 成功抑制 value overestimation，但代价是策略学习严重受损——两个 critic 快速收敛到一致使 min 操作几乎无效，真正的问题可能是 gate 坍塌（dt=2 锁定）导致 horizon 受限。

### 与 s0 (exp_032) 对比

s0 仍在 RUNNING（bjb1-40020），暂无可比数据。待 s0 完成后补充对比分析。

### 对 Intervention Hierarchy 的含义

Dual-critic 作为 architecture-level CIVO intervention 的效力存疑：
1. NVE 抑制效果好，但可能过度保守
2. 性能代价过大（~43% drop），不满足"eval matches baseline"标准
3. Gate 坍塌是独立的 confound——需要排除 gate 问题后才能公平评估 dual-critic 的真实效果
