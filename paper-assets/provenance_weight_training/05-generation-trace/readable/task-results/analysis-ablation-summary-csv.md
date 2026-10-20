# analysis ablation summary csv

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ablation-summary-csv_20260516T175320_result.json`
- **Structured JSON:** [`5e40c5266c1121885913.json`](../../sessions/5e/5e40c5266c1121885913.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已生成并注册（`art_20260516_4c1ef8`）。

**汇总**：44 个实验，9 个类别：

| 类别 | 数量 | 说明 |
|---|---|---|
| grid-b_sweep | 15 | b=0.1–5.0, seeds 42/123/456 |
| tau_sweep | 3 | τ=0.5, 0.6, 0.7 |
| n_min_ablation | 2 | n_min=1, 4 |
| rho_cross_validation | 6 | ρ=0.6 各方法对比 |
| ess_only_baseline | 3 | seeds 42/123/456 |
| adaptive | 6 | 含 3 fix + 3 原始 |
| uniform | 3 | seeds 42/123/456 |
| detect_remove | 1 | seed 42 |
| other | 5 | baseline/datagen/detector/golden_ratio/p0 |

文件路径：`artifacts/ablation_summary.csv`

---
