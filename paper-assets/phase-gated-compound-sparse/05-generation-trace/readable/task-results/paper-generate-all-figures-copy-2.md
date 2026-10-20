# paper generate all figures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_generate_all_figures_20260514T094637_result.json`
- **Structured JSON:** [`1e21c856541fbc344600.json`](../../sessions/1e/1e21c856541fbc344600.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 PDF 全部生成完毕，存放在 `/root/autodl-tmp/pacs/paper_figures/`：

| 文件 | 大小 | 内容 |
|------|------|------|
| `fig1_dose_response.pdf` | 20 KB | 6-point dose-response (G vs s)，importance 实线 + random 虚线，log scale，带 95% CI |
| `fig3_crossover.pdf` | 19 KB | s=0.25 grouped bar chart，importance vs random × 3 phases，标注 crossover |
| `fig4_bootstrap.pdf` | 18 KB | Forest plot，4 个 sparsity level 的 median diff + 95% CI + p-value + Cohen's d |
| `fig5_crossmodel.pdf` | 21 KB | DeepSeek vs Qwen 双模型 Δ 对比，Spearman ρ=1.0 标注 |

**数据验证**（数据文件 vs 任务描述）：
- Fig 1 importance G: 69.2, 103.1, 222.4, 274.2 — 匹配 ✓ （额外含 s=0.10 G=5.6, s=0.35 G=273.6）
- Fig 1 random G: 1.1, 0.9, 1.7, 1.6 — 匹配 ✓
- Fig 3 crossover 数值完全匹配 ✓
- Fig 4 使用 rebootstrap B=10000 数据，median_diff: 0.32, 1.15, 3.97, 9.94（与任务描述的 0.37, 0.97, 3.34, 9.85 有差异，**以 rebootstrap_b10000_results.json 为准**——该文件是更高精度的重新 bootstrap 结果）
- Fig 5 DeepSeek Δ: 0.39, 1.48, 7.16, 14.59；Qwen Δ: 0.04, 0.23, 1.27, 2.94 — 匹配 ✓

---
