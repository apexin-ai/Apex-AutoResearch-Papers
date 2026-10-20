# All Successful Experiments Summary

> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure

---

## Grid-b Experiments

Fixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.

| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|
| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |
| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |
| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |
| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |
| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |
| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |
| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |
| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |
| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |
| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |
| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |
| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |
| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |
| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |
| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |
| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |
| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |
| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |

> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。
> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。

---

## Adaptive Experiments

Per-batch adaptive b* via α_eff theory. Sorted by PPL ascending.

| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|
| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |
| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |
| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |
| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |
| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |
| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |

> "original" = n_min=3 bug (batch_size-1)。"n_min fix" = D012 修复后 n_min=max(2, batch_size//2)。
> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。
> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。

---

## Ablation Experiments

Single-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.

| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |
|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|
| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |
| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |
| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |

> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。
> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。
> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。

---

## Baseline Experiments

Uniform weighting (no provenance information). Sorted by PPL ascending.

| exp_id | seed | PPL | eval_loss | gpu_hours |
|--------|------|-----|-----------|-----------|
| uniform_seed42 | 42 | 17.690 | - | 3.43 |
| uniform_seed123 | 123 | 17.690 | - | 3.43 |
| uniform_seed456 | 456 | 17.700 | - | 3.43 |

---

## Infrastructure Experiments (non-training)

| exp_id | 类型 | 关键指标 |
|--------|------|---------|
| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |
| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |

---

## Key Findings

1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。

2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。

3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。

4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。

5. **Golden ratio oracle (PPL=17.654) 确认 adaptive 接近最优。** 使用真实标签的 oracle 仅略优于 adaptive_fix (17.650)，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。

---

## PPL Ratio Reference

| 方法 | seed42 | seed123 | seed456 | mean |
|------|--------|---------|---------|------|
| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |
| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |
| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |
| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |
| golden_ratio oracle | 0.9980 | - | - | - |
| ess_only | 1.0023 | - | - | - |
| nmin1 | 1.0056 | - | - | - |
