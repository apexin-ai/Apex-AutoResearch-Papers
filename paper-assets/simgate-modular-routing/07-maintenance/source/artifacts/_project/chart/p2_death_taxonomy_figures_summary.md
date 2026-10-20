# P2 Death Failure Taxonomy Figures

## 数据
- 133 episodes, 25 tasks (prescreening dataset)
- Internal (LLM): 74 deaths (55.6%), 59 non-death
- Deterministic: 15 deaths (11.3%), 118 non-death

## Figure 1: death_action_distribution.pdf
双面板：左 = 完整动作分布（connect 占 86.7%），右 = 放大非 connect 动作，`focus on` 在 death 中 5.5% vs non-death 1.8% (3x)

## Figure 2: death_action_timeline.pdf
6 个代表性 death episode 的逐步动作序列，标注 fatal `focus on` 步骤

## Figure 3: death_action_comparison.pdf
Internal vs Deterministic 策略的非 connect 动作分布对比

## 关键发现
1. ALL 74 death episodes 包含恰好 1 个 `focus on [X]` fatal action
2. 最常见 death target: `focus on workshop` (33/74 = 44.6%)
3. Death episodes 被 unproductive connect loops 主导 (86.7%)
4. Non-death episodes 显示更多样的 productive actions

## 文件位置
westd-18266:/root/autodl-tmp/simgate-modular-routing/artifacts/
