# exp_fewnerd_mf4_s123_v2 实验结果分析

## 实验信息
- 数据集: FewNERD / NER
- 实例数: 37,648
- Samples/instance: 8
- Temperature: 1.0
- 模型: qwen3-8b-fewnerd-exp021-merged
- Seed: 123
- 状态: **正常完成** (EXIT_CODE=0)

## seed=123 关键指标

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.7883 |
| oracle_f1 | 0.8892 |
| oracle_headroom_pp | 10.09 |
| fleiss_kappa_mean | 0.3503 |
| soft_jaccard_mean | 0.6701 |
| rho_sj_full | +0.3083 (p=0.0) |
| rho_sj_cond | +0.2005 (p=3.15e-258) |
| rho_fleiss_full | +0.1593 (p=5.34e-184) |
| rho_fleiss_cond | +0.0059 (p=0.316, n.s.) |
| logprob_auroc_full | 0.6069 |
| logprob_auroc_cond | 0.5909 |
| sample_f1_mean | 0.6374 |
| sample_f1_std | 0.3815 |
| sample_f1_pct_zero | 20.4% |
| structural_beats_surface | YES (delta=+0.1490) |
| verdict | MARGINAL |

### MV/LP Selection Metrics
未计算（pipeline 未包含），与 s42/s456 一致。无 mv_strict_f1、lp_best_f1、degeneracy_rate。

## 3-Seed 汇总 (s42 / s456 / s123)

### 核心指标 mean ± std

| 指标 | s42 | s456 | s123 | mean | std |
|------|-----|------|------|------|-----|
| greedy_f1 | 0.7885 | 0.7883 | 0.7883 | 0.7884 | 0.0001 |
| oracle_f1 | 0.8787 | 0.8810 | 0.8892 | 0.8830 | 0.0055 |
| oracle_headroom (pp) | 9.02 | 9.27 | 10.09 | 9.46 | 0.56 |
| fleiss_kappa | 0.3537 | 0.3555 | 0.3503 | 0.3532 | 0.0026 |
| soft_jaccard | 0.6751 | 0.6845 | 0.6701 | 0.6766 | 0.0073 |
| sample_f1_pct_zero (%) | 23.0 | 19.4 | 20.4 | 20.9 | 1.9 |

### 观察

1. **greedy_f1 极其稳定**：3-seed std=0.0001，几乎无波动（0.7883–0.7885）
2. **oracle_f1 有一定变异**：std=0.0055，s123 的 oracle 比 s42 高约 1pp，说明采样多样性在不同 seed 下有差异
3. **oracle_headroom 均值 9.46pp**：确认 greedy 与 oracle 之间存在显著提升空间
4. **fleiss_kappa 稳定偏低**（~0.35）：采样间一致性中等偏低，符合 "fair agreement" 水平
5. **soft_jaccard 稳定**（~0.68）：结构性一致性指标在合理范围
6. **structural_beats_surface 三个 seed 均为 YES**：结构性指标始终优于表面指标
7. **sample_f1_pct_zero 均值 20.9%**：约 1/5 的样本生成完全错误，有优化空间
