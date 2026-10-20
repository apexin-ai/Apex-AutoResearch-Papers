# analysis push a v3 capability gap 8point

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_push-a-v3-capability-gap-8point_20260520T224050_result.json`
- **Structured JSON:** [`ef3718ed15f847423b0d.json`](../../sessions/ef/ef3718ed15f847423b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件在 `/root/symb_invariant_consensus/results/push_a_v3_capability_gap_8point/`：

### 主要结果（Director 版，LLaMA #5 用 w=3 gain=+4.17）

| 指标 | 值 |
|------|-----|
| Spearman ρ | 0.970 (p < 0.001) |
| Pearson r | 0.907 (p = 0.002) |
| Linear R² | 0.823, slope=0.143 [0.076, 0.209], RMSE=1.34 pp |
| Sigmoid R² | 0.875, RMSE=1.13 pp (L=15.0, k=0.059, x₀=7.4) |
| Isotonic R² | 0.983, RMSE=0.42 pp |
| Break-even (linear) | Δ* ≈ −43.4 pp |
| Significant points | 4/8 (p<0.05) |

### w=5 consistent 版（LLaMA #5 用 w=5 gain=+1.67）

| 指标 | 值 |
|------|-----|
| Spearman ρ | 0.898 (p = 0.002) |
| Pearson r | 0.885 (p = 0.004) |
| Linear R² | 0.784, slope=0.146 [0.069, 0.223] |
| Sigmoid R² | 0.895, RMSE=1.08 pp |
| Significant points | 3/8 (p<0.05) |

Director 版 Spearman 更强（0.970 vs 0.898），因为 LLaMA w=3 的 gain=+4.17 更符合单调递增趋势。

输出文件：`results.json`、`capability_gap_scatter_v3.pdf/png`、`latex_stats.txt`（含两版 LaTeX-ready 统计字符串）。

---
