# D035: Seed43 Fisher Test — Kill Criterion 触发后的战略决策

**日期**: 2026-05-16
**触发**: obs_only vs argmin pooled Δ = +1.0pp, Fisher p = 0.89, kill criterion (|Δ| < 3pp) 触发

## 核心数据

| | seed42 | seed43 | pooled |
|---|--------|--------|--------|
| obs_only ε=0.1 | 19/100 | 12/100 | 31/200 = 15.5% |
| argmin | 12/100 | 17/100 | 29/200 = 14.5% |
| Δ | +7pp | -5pp | +1.0pp |
| Fisher p | 0.089 | — | 0.889 |

## 决策: 不立即杀项目，等 ε=0.2 seed43 + reframe

### 理由

1. **ε=0.2 seed43 仍在跑**（bjb1-32546:cuda:3, 1/10 tasks done）。seed42 ε=0.2 = 22% (+10pp over argmin)，效应更大。如果 ε=0.2 seed43 复现出 ≥5pp 优势，这个配置可以作为主打。等这个数据出来再做最终判断。

2. **Magnitude sweep 稳定性是真实发现**：obs_only 在 ε∈[0.03,0.30] 全程 35-44%（spatial），perdof 偏离 0.1 退化到 26-31%。这说明 obs features 提供的是鲁棒性，不是单点提升。

3. **Reframe 路径存在**：从 "obs_only significantly improves over argmin" 转为 "learned observation-conditioned corrections provide stable improvements across hyperparameter regimes, while conformal-feature corrections are brittle"。这是一个 analysis/understanding 贡献，CoRL 接受度尚可。

### 立即行动（MCP 重连后执行）

1. **等 ε=0.2 seed43 完成**（ETA ~8-12h based on 1/10 done），跑 Fisher test
2. **修复 Agent 脚本 per-task 数据错误**（artifacts/analysis/seed43_fisher_analysis.py L35-46）
3. **如果 ε=0.2 pooled Δ ≥ 5pp 且 p < 0.10**：
   - Pivot 主打配置到 ε=0.2
   - 更新 Table 1 和 Section 4.1
   - 加 seed44 for ε=0.2 巩固（如时间允许）
4. **如果 ε=0.2 也不显著**：
   - Reframe 论文为 analysis paper
   - 核心贡献：sample-then-correct 框架 + magnitude stability analysis + honest negative on conformal features
   - 降级 claim：报 effect size + CI，不 claim 统计显著
   - 强化 magnitude sweep figure (fig3) 作为主要 evidence
5. **通知用户**：报告 kill criterion 触发 + 两条路径 + 推荐等 ε=0.2 数据

### 不做的事

- 不加 seed44/45 for ε=0.1（power 分析显示即使 400 trials 也只有 70% power，浪费 GPU）
- 不降级投稿目标（CoRL 接受 analysis/negative result paper，不 fallback）
- 不在 ε=0.2 数据出来前仓促 reframe
