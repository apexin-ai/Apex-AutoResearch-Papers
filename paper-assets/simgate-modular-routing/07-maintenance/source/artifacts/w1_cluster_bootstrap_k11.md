## W1 Cluster Bootstrap 修正结果 (K=11)

数据源：baseline_245eps/episode_details.jsonl
Tasks: 11, Episodes: 245
Point estimate DAF: 0.9041

### Wild Cluster Bootstrap (Webb 2023)
- t-statistic: 10.0000
- p-value: 0.0000 (Webb 6-point weights, B=10000)
- 95% CI: [0.7301, 1.0000]
- Boot mean: 0.9099 (std: 0.0828)
- 结论: DAF 在 cluster resampling 下高度显著，CI 下界远高于 0.5

### Exact Permutation Test
- Observed mean DAF: 0.9091
- p-value: 0.0020 (4/2048 exhaustive sign-flip permutations)
- 结论: 在最保守的非参数检验下仍显著 (p < 0.01)

### Cluster-Robust T-Test
- t-statistic: 10.0000
- p-value: 0.000002
- df: 10
- 95% CI: [0.7065, 1.1116]
- 结论: 以 task type 为分析单元的 t 检验极显著

### Cohen's d
- d: 3.0151 (large)
- 95% CI: [1.4331, 4.5971]
- 解读: 效应量极大 (>0.8 = large)，DAF 信号远超随机波动
- Per-cluster DAFs: 10/11 tasks DAF=1.0, 1 task (find-non-living-thing) DAF=0.0

### 总结
四种方法一致显著：
- Wild cluster bootstrap: p < 0.001
- Exact permutation: p = 0.002
- Cluster-robust t-test: p = 0.000002
- Cohen's d = 3.02 (极大效应量)

DAF 在 cluster-level 分析下稳健成立。10/11 task types 的 DAF=1.0（全部 deterministic 优势来自 death avoidance），唯一例外是 find-non-living-thing (DAF=0.0)。即使考虑 task-type 内相关性（非独立 episodes），结论不变。
