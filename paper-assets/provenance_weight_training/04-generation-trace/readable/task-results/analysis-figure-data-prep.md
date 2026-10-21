# analysis figure data prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_figure-data-prep_20260516T051202_result.json`
- **Structured JSON:** [`a7a82c385d5e877a71df.json`](../../sessions/a7/a7a82c385d5e877a71df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 CSV 数据文件全部生成并注册完成：

| 文件 | 行数 | 说明 |
|------|------|------|
| `fig_tau_sweep.csv` | 7行 | τ=0.5~0.95 + uniform参考线，含 b* 统计量 |
| `fig_b_landscape.csv` | 20行 | 3 seed 的 grid-b PPL + adaptive 标注点，seed456 已截断至 b≤1.5 |
| `fig_nmin_ablation.csv` | 5行 | n_min=1~4 + uniform参考线 |
| `fig_contamination_comparison.csv` | 4行 | ρ=0.4 vs ρ=0.6 四种方法对比 |
| `fig_method_comparison.csv` | 5行 | 跨 seed 方法对比，含 mean/std |

所有 PPL 值均从 registry 实际 metrics 提取，未使用 fallback。待补充：b=0.1 seed42 完成后需更新 `fig_b_landscape.csv`。

---
