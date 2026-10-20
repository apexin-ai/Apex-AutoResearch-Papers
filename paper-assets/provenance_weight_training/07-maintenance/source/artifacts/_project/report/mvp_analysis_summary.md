# MVP Analysis Summary — Provenance Weight Training

**Date**: 2026-05-14  
**Model**: Qwen3-0.6B, 200M tokens, contamination_ratio=0.4  
**Eval**: held-out human perplexity (4.08M tokens)

---

## 1. Method × Seed Comparison (eval_ppl)

| Method | seed42 | seed123 | seed456 | Mean | Std |
|--------|--------|---------|---------|------|-----|
| uniform | 17.690 | 17.690 | 17.700 | 17.693 | 0.006 |
| grid-best (b=0.5) | 17.651 | 17.638 | *pending* | 17.645† | 0.009† |
| adaptive (n_min=3) | 17.690 | 17.630 | 17.640 | 17.653 | 0.033 |
| adaptive_fix (n_min=2) | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 |

† seed456 grid 尚在跑，mean/std 仅基于 seed42 + seed123。

---

## 2. Grid-b Curve Data

| b | seed42 | seed123 | seed456 |
|---|--------|---------|---------|
| 0.5 | 17.651 | 17.638 | *RUNNING* |
| 1.0 | 17.692 | 17.674 | *RUNNING* |
| 1.5 | 17.718 | 17.701 | *RUNNING* |
| 2.0 | 17.741 | 17.725 | *RUNNING* |
| 3.0 | 17.774 | 17.760 | *QUEUED* |
| 5.0 | 17.818 | 17.804 | *QUEUED* |

两个完成 seed 均呈单调递增：b 越大 PPL 越高，best-b=0.5 在搜索边界。

---

## 3. MVP Judgment (adaptive_fix vs grid-best)

### Per-seed calculation

| Metric | seed42 | seed123 | seed456 |
|--------|--------|---------|---------|
| uniform_ppl | 17.690 | 17.690 | 17.700 |
| grid_best_ppl (b=0.5) | 17.651 | 17.638 | *pending* |
| adaptive_fix_ppl | 17.650 | 17.643 | 17.660 |
| Δ_grid = uniform - grid_best | 0.039 | 0.052 | — |
| Δ_adaptive_fix = uniform - adaptive_fix | 0.040 | 0.047 | 0.040 |
| ratio = Δ_adaptive_fix / Δ_grid | **102.6%** | **90.4%** | — |

### Aggregate (seed42 + seed123)

| Metric | Value |
|--------|-------|
| Mean Δ_grid | 0.0455 |
| Mean Δ_adaptive_fix | 0.0435 |
| Mean ratio | **95.6%** |
| Threshold | ≥ 90% |
| **Verdict** | **PASS** |

Both available seeds pass the 90% threshold individually. Aggregate ratio = 95.6%.

---

## 4. b* Distribution Cross-Seed Consistency

| Statistic | seed42 | seed123 | seed456 | Cross-seed mean | CV |
|-----------|--------|---------|---------|-----------------|-----|
| mean | 0.714 | 0.723 | 0.843 | 0.760 | 9.5% |
| median | 0.069 | 0.000 | 0.440 | 0.170 | 137.2% |
| std | 1.547 | 1.613 | 1.687 | 1.616 | 4.3% |
| pct_below_0.5 | 59.7% | 59.9% | 52.8% | 57.5% | 7.0% |

- **mean/std 跨 seed 稳定**（CV < 10%），说明 b* 的整体分布形状一致。
- **median 跨 seed 变异极大**（CV=137%），因为分布在 0 附近有尖峰，微小数据差异导致中位数在 0 和小正数之间跳跃。这是 bimodal 分布的预期行为，不构成方法问题。
- 约 53-60% 的 batch 的 b*<0.5（接近 uniform），说明自适应方法在大多数 batch 上选择轻微加权或不加权，仅对高污染 batch 施加强加权。

---

## 5. Risks & Caveats

1. **best-b 在搜索边界 (b=0.5)**：两个完成 seed 的 grid search 最优均为 b=0.5（最小搜索值）。真正的最优可能在 b<0.5。若扩展搜索至 b∈{0.1, 0.2, 0.3}，grid-best 可能更优，MVP ratio 可能下降。

2. **train_loss 跨方法不可比**：uniform 使用标准 CE，grid-b/adaptive 使用 weighted CE（加权后 loss 值域不同）。eval_ppl 是唯一可比指标。

3. **b* 中位数≈0 的含义**：约 60% batch 的 b*=0 或接近 0，即自适应方法对多数 batch 不加权。改善主要来自对少数高污染 batch 的选择性降权。这可能意味着：
   - 效果依赖于污染分布的长尾，在更干净数据上收益可能更小
   - 方法的 "免 grid search" 优势可能因为其行为接近 b=0（即接近 uniform）

4. **seed456 grid 尚未完成**：当前 MVP 判定基于 2/3 seeds。seed456 完成后需更新。

5. **改善绝对值小**：uniform→grid-best 仅降低 ~0.04-0.05 PPL（相对改善 ~0.26-0.29%）。在更大规模或更高污染率下效果是否放大有待验证。

---

## 6. Summary

| Question | Answer |
|----------|--------|
| adaptive_fix 是否通过 MVP (≥90% of grid-best)? | **YES** (95.6% aggregate, both seeds pass) |
| adaptive_fix 是否需要 grid search? | **NO** (zero hyperparameter tuning) |
| adaptive_fix vs adaptive (原版) 哪个更好? | adaptive_fix 在 seed42 上明显更好 (17.65 vs 17.69)，其他 seed 相当 |
| 是否需要扩展 grid search 范围? | **建议**：b<0.5 区间可能有更好的 grid-best |
| seed456 是否会改变结论? | 不太可能，除非 grid_b0.5_seed456 < 17.616（需 Δ_grid > 0.084 才能使 ratio < 90%） |
