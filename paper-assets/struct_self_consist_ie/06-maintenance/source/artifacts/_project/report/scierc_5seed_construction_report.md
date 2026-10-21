## SciERC 5-seed Entity Construction Analysis

**Method:** LP-weighted entity construction, θ = 2/N = 0.25 (N=8 samples)  
**Data:** `scierc_mf4v2_seed{42,123,456,2024,3141}`, 529 instances/seed (gold-filtered)  
**Baseline:** Greedy (T=0) predictions embedded in each samples.jsonl

### Per-seed results

| Seed | Greedy F1 | Construction F1 | Δ (pp) | Sign | p-value |
|------|-----------|-----------------|--------|------|---------|
| 42   | 65.02     | 64.44           | −0.58  | −    | 0.8242  |
| 123  | 64.71     | 65.67           | +0.96  | +    | 0.0853  |
| 456  | 64.56     | 66.47           | +1.91  | +    | 0.0031* |
| 2024 | 64.78     | 66.25           | +1.48  | +    | 0.0233* |
| 3141 | 64.27     | 66.05           | +1.78  | +    | 0.0075* |

\* p < 0.05, paired bootstrap (B=10,000)

### Aggregate

- **Mean Δ:** +1.11 pp
- **Std:** 0.91 pp
- **Min / Max:** −0.58 / +1.91 pp
- **Direction:** 4 positive / 1 negative
- **Stability:** MOSTLY POSITIVE (4/5)
- **Pooled bootstrap (5×529 = 2,645 instances):** Δ = +1.11pp, 95% CI [+0.48, +1.75], p = 0.0003 (significant)

### Interpretation

1. **与论文报告的 "+0.32pp n.s." 不一致。** 当前 5-seed 分析得到的 mean Δ = +1.11pp，且 pooled bootstrap 显著（p=0.0003）。差异可能来自：论文使用的是 `exp_001_seed42_v2` 单种子数据（对应 seed 42 的 −0.58pp），而当前使用的是 `scierc_mf4v2_seed*` 多种子数据。需要确认论文引用的是哪组实验。

2. **方向稳定性：4/5 正方向。** Seed 42 是唯一的负方向（−0.58pp），但不显著（p=0.82）。其余 4 个种子均为正方向，其中 3 个 individually significant。

3. **建议：**
   - 如果论文报告的 "+0.32pp n.s." 来自旧实验 `exp_001_seed42_v2`，应更新为 `scierc_mf4v2` 5-seed 结果：**+1.11pp (p=0.0003)**
   - 可以强化 claim："entity construction produces a consistent positive gain on SciERC (4/5 seeds positive, pooled Δ = +1.11pp, p < 0.001)"
   - 但应注明 seed 42 为负方向，以保证严谨性
   - 如果要保守报告，可写 "4 of 5 seeds show positive gains (mean +1.11pp), though not uniformly significant at the individual seed level"
