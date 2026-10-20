# analysis compile results table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile-results-table_20260516T050941_result.json`
- **Structured JSON:** [`6dea1be9a318ff99f487.json`](../../sessions/6d/6dea1be9a318ff99f487.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 CSV 已生成并注册。汇总：

**`results_table_main.csv`** — 主结果 (ρ=0.4, 3 seeds)

| Method | seed42 | seed123 | seed456 | Mean | Δ |
|---|---|---|---|---|---|
| uniform | 17.694 | 17.686 | 17.702 | 17.694 | — |
| grid-best | 17.640 | 17.638 | 17.650 | 17.643 | -0.051 |
| adaptive | 17.653 | 17.643 | 17.657 | 17.651 | -0.043 |
| ESS-only | 17.730 | 17.720 | 17.719 | 17.723 | +0.029 |
| golden_ratio | 17.654 | — | — | — | — |

**`results_table_contamination.csv`** — ρ=0.6 对比 (seed42)

| Method | ρ=0.4 | ρ=0.6 | Degradation |
|---|---|---|---|
| uniform | 17.694 | 17.766 | +0.072 |
| grid b=0.5 | 17.651 | 17.704 | +0.053 |
| adaptive | 17.653 | 17.740 | +0.087 |
| ESS-only | 17.730 | 17.770 | +0.040 |

**`results_table_ablation.csv`** — τ sweep (0.5→0.95) + n_min sensitivity (1→4)

**`results_table_grid_b_curve.csv`** — b-PPL curve (b=0.3→5.0, 3 seeds), b=0.1 标注 TBD

注意事项：
- seed456 b≥2.0 数据异常（train_loss 偏低），已在注释中标注
- detect-and-remove 无 PPL 结果（只有分类器训练）
- golden_ratio 只有 seed42

---
