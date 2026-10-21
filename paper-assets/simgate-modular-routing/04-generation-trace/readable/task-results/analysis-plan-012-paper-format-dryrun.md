# analysis plan 012 paper format dryrun

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-012-paper-format-dryrun_20260513T221342_result.json`
- **Structured JSON:** [`fbfaebf37fe2ac28ef0f.json`](../../sessions/fb/fbfaebf37fe2ac28ef0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总结果：

### 分析结果

**Aggregate (30 tasks, 249 episodes)**:
- Δ_full = +38.33, Δ_no_death = +0.48
- death_avoidance_fraction = 98.75%
- r = 0.986, p ≈ 0 (30 tasks)
- Label dist: det-preferred=102, no-preference=146, internal-preferred=1

**Outlier**: `measure-melting-point-unknown-substance` DAF=59.4%（任务说的 0.38 似乎是旧数据，prescreening 实际是 0.594）

**Genuine det tasks (DAF < 95%)**: 4 个（非 5 个）
- `measure-melting-point-unknown-substance`: 59.4%, Δ_nd=+16.5
- `find-living-thing`: 89.2%, Δ_nd=+4.5
- `find-plant`: 93.5%, Δ_nd=+4.0
- `find-non-living-thing`: -0.0%, Δ_nd=-6.8（det 实际更差）

### 产出文件 (`results/decomposition_dryrun/`)
| 文件 | 大小 | 说明 |
|------|------|------|
| `death_decomposition_report.json` | 29KB | 完整分析报告，含 per-task 和 aggregate |
| `paper_table1_data.json` | 11KB | 论文 Table 1 专用格式 |
| `fig1_death_scatter.pdf/png` | 25/150KB | Scatter: death_rate_diff vs Δ，回归线+r值，outlier 标注 |
| `fig2_label_distribution.pdf/png` | 16/202KB | Stacked bar: per-task label 分布 |
| `fig3_death_avoidance.pdf/png` | 18/212KB | Bar: per-task DAF，红色标注 <95% tasks |

### 论文适配性
- JSON 结构完整，per-task breakdown 包含所有 Table 1 需要的字段
- paper_table1_data.json 可直接用于生成 LaTeX 表格
- 3 张图均有 PDF（论文排版用）+ PNG（预览用）
- `plot_death_decomposition.py` 已就绪，plan-001b 完整数据到位后改 `--report` 路径即可重新生成

---
