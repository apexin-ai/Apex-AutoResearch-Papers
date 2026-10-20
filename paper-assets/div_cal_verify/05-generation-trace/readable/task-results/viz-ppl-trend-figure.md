# viz ppl trend figure

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_ppl_trend_figure_20260513T203201_result.json`
- **Structured JSON:** [`3b6bf72c8f6ecd888a63.json`](../../sessions/3b/3b6bf72c8f6ecd888a63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 数据完整性报告

| 方法 | seed=42 | seed=123 | seed=456 | 完整度 |
|------|---------|----------|----------|--------|
| **Uncurated** | ✓ gen0-7 | ✓ gen0-7 | ✓ gen0-7 (从日志补全) | 3/3 |
| **External Only** | ✓ gen0-7 | ✓ gen0-7 | 运行中 | 2/3 |
| **RGDS** | ✓ gen0-7 | ✓ gen0-7 | 未启动 | 2/3 |
| **Random 50%** | ✓ gen0-7 | ✓ gen0-7 (从日志补全) | ✓ gen0-7 (从日志补全) | 3/3 |

**从日志提取的缺失数据：**
- `uncurated seed=456`: [36.64, **45.03, 52.06, 52.55, 51.55, 49.40, 45.74**, 44.69]
- `random_50 seed=123`: [36.46, 43.44, **49.59, 50.31, 47.64, 46.96, 41.05**, 41.75]
- `random_50 seed=456`: [36.91, 43.89, **46.22, 48.08, 45.26, 44.79, 45.63**, 44.60]

### 产出文件

| 文件 | 位置 |
|------|------|
| Figure 1 PDF | `westd-11235:/root/div_cal_verify/figures/fig1_ppl_trends.pdf` (19K) |
| Figure 1 PNG | `westd-11235:/root/div_cal_verify/figures/fig1_ppl_trends.png` (299K) |
| Table 1 CSV | `artifacts/tables/table1_gen7_summary.csv` |
| Table 1 LaTeX | `artifacts/tables/table1_gen7_summary_latex.tex` |

图表特征：RGDS 红线在 gen5+ 急剧上升至 ~78 PPL（model collapse），Random 50% 绿线全程最低收敛至 ~43 PPL，Uncurated 灰线居中 ~47 PPL，External 蓝线与 Uncurated 接近 ~48 PPL。n≥3 的用 std shading，n=2 的用 min-max range shading。

---
