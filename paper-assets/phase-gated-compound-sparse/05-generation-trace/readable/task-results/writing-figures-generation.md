# writing figures generation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_figures_generation_20260514T090540_result.json`
- **Structured JSON:** [`ef6a8619a7146fa9caea.json`](../../sessions/ef/ef6a8619a7146fa9caea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部生成完毕，文件均非空。产出汇总：

| 图表 | 文件 | 大小 | 描述 |
|------|------|------|------|
| Figure 1 | `fig1_dose_response.pdf/png` | 23KB/154KB | Dose-Response 曲线，4 条线（2 模型 × 2 masking），symlog Y 轴，bootstrap 95% CI error bars |
| Figure 2 | `fig2_cohens_d.pdf/png` | 21KB/104KB | Cohen's d 趋势图，DS 0.44→0.80, QW 0.28→1.02，shaded CI，small/medium/large 阈值线 |
| Figure 3 | `fig3_crossover.pdf/png` | 22KB/79KB | s=0.25 时 importance vs random 的 phase-wise median II 柱状图，双模型并排 |
| Figure 4 | `fig4_per_problem_dist.pdf/png` | 65KB/228KB | 8 panel violin + scatter plot，2×4 (model × sparsity)，展示 per-problem ΔII 分布 |

**路径**: `/root/autodl-tmp/pacs/figures/`
**脚本**: `/root/autodl-tmp/pacs/analysis/generate_paper_figures.py`

注意事项：
- Figure 1 用了 symlog scale（linthresh=0.5）处理 importance vs random 的量级差异
- per-problem 数据中有少量 None 值（~1-4 per experiment）被过滤
- Figure 1 的 per-problem median diffs（如 DS importance s015=0.35）与 summary table 的 median_diff（0.39）略有差异——前者是 `median(ii_low - ii_high)`，后者是 `median(ii_low) - median(ii_high)`，两种定义都合理，当前脚本用的是前者（paired difference 的 median，统计上更严谨）

---
