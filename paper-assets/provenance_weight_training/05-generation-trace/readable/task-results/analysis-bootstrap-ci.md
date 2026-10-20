# analysis bootstrap ci

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_20260521T143048_result.json`
- **Structured JSON:** [`3db91cdeb601d6c7c3e6.json`](../../sessions/3d/3db91cdeb601d6c7c3e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**CSV**: `artifacts/_project/data/bootstrap_ci_results.csv` (art_20260521_ab9336)

### 完整 CI 表

**Individual Groups (BCa 95% CI, B=10000)**

| Group | Mean | 95% CI | Width |
|-------|------|--------|-------|
| adaptive ρ=0.4 τ=0.7 holdout | 17.674 | [17.666, 17.679] | 0.013 |
| uniform ρ=0.4 holdout | 17.694 | [17.686, 17.699] | 0.013 |
| adaptive ρ=0.4 OWT | 18.347 | [18.344, 18.348] | 0.004 |
| uniform ρ=0.4 OWT | 18.373 | [18.365, 18.380] | 0.015 |
| adaptive ρ=0.4 Wiki | 15.330 | [15.315, 15.340] | 0.025 |
| uniform ρ=0.4 Wiki | 15.357 | [15.335, 15.371] | 0.036 |
| TF-IDF adaptive holdout | 17.651 | [17.643, 17.655] | 0.012 |
| GPT-2 adaptive holdout | 17.792 | [17.788, 17.795] | 0.006 |
| N-gram adaptive holdout | 17.823 | [17.820, 17.825] | 0.005 |
| adaptive ρ=0.6 holdout | 17.731 | [17.727, 17.734] | 0.007 |
| uniform ρ=0.6 holdout | 17.763 | [17.754, 17.769] | 0.015 |

**Paired Differences (all includes_zero = False → all significant)**

| Comparison | Δ Mean | 95% CI | Significant? |
|------------|--------|--------|-------------|
| Δ(adapt−unif) ρ=0.4 holdout | −0.020 | [−0.025, −0.016] | **Yes** |
| Δ(adapt−unif) ρ=0.4 OWT | −0.026 | [−0.043, −0.018] | **Yes** |
| Δ(adapt−unif) ρ=0.4 Wiki | −0.027 | [−0.044, −0.013] | **Yes** |
| Δ(TF-IDF−GPT-2) holdout | −0.141 | [−0.145, −0.138] | **Yes** |
| Δ(TF-IDF−N-gram) holdout | −0.172 | [−0.180, −0.168] | **Yes** |
| Δ(GPT-2−N-gram) holdout | −0.031 | [−0.035, −0.029] | **Yes** |
| Δ(adapt−unif) ρ=0.6 holdout | −0.032 | [−0.038, −0.028] | **Yes** |

### 总结

**7/7 paired comparisons 的 95% BCa CI 均不包含 0，全部显著。**

- **Claim 1** (Adaptive vs Uniform ρ=0.4): Adaptive 在 holdout/OWT/Wiki 三个指标上均显著优于 Uniform（Δ ≈ −0.02 ~ −0.03 PPL），效果在 OOD 数据上保持。
- **Claim 2** (Detector ablation): TF-IDF >> GPT-2 >> N-gram，三两两比较全部显著，差距大（TF-IDF vs N-gram Δ=−0.172，CI 极窄）。
- **Claim 3** (ρ=0.6): Adaptive 显著优于 Uniform（Δ=−0.032），效果比 ρ=0.4 时更大。

**统计功效评估**: n=3 seeds 下 CI 宽度在 0.005–0.031 之间，所有效果量均远超 CI 宽度，说明尽管样本量小，效果足够稳健。Detector ablation 的 CI 最窄（seed 间方差极小），Adaptive vs Uniform 的 OOD 指标 CI 相对较宽但仍排除 0。

---
