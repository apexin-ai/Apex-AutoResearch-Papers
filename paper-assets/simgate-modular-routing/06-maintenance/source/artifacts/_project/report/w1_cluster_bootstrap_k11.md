## W1 Cluster Bootstrap 修正结果 (K=11)

数据源：baseline_245eps/episode_details.jsonl
Tasks: 11, Episodes: 245

### Wild Cluster Bootstrap (Webb 2023)
- p-value: < 0.001
- CI: [0.73, 1.00]
- 结论: 显著

### Exact Permutation Test
- p-value: 0.002
- 4/2048 permutations more extreme
- 结论: 显著

### Cluster-Robust T-Test
- t-statistic: 10.0
- df: 10
- p-value: 0.000002
- 结论: 显著

### Cohen's d
- d: 3.02
- 解读: 极大效应量 (>0.8 = large)

### Per-Cluster DAF
- 10/11 tasks: DAF = 1.0
- find-non-living-thing: DAF = 0.0 (唯一例外)

### 总结
四种方法一致显著。K=11 结果比 K=7 更强（更多 clusters 增加统计功效）。论文中 K=7 需修正为 K=11。