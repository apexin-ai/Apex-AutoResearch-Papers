# exp-022 Cross-Scorer 统计设计检查 (2026-05-16)

## 结论
Dream 审稿意见正确——16 个 K* 做 ANOVA 无法工作 (residual df=0)。但 pipeline 已产出 per-fold AUC (25 obs/cell, 总 N=400)，足以支撑多因素统计分析。

## 数据粒度 (per cell)
| 粒度 | 数量 |
|------|------|
| per-doc 特征 | 30000 (5000 docs × 6 depths) |
| per-fold AUC | 25 (5 pairs × 5 folds) |
| K* | 1 |

## ANOVA df 分析
| DV | Total df | Residual df | 可行？ |
|----|----------|-------------|--------|
| K* (1/cell) | 15 | 0 | ❌ |
| Fold AUC (25/cell) | 399 | ~356 | ✅ |

## 推荐分析方案
1. **主分析**: 3-way ANOVA, DV=fold AUC, factors=Generator(4)×Scorer(4)×DepthPair(5), fold as random effect
2. **K* 替代**: per-fold K* (logistic interpolation) → 80 obs → 2-way ANOVA (df_res=48)
3. **可视化**: 4×4 K* heatmap + bootstrap CI
