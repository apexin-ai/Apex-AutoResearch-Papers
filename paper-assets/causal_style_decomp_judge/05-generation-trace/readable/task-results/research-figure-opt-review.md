# research figure opt review

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_figure_opt_review_20260524T085559_result.json`
- **Structured JSON:** [`cdbe40f70c1f65eb08eb.json`](../../sessions/cd/cdbe40f70c1f65eb08eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`d=1.120` 只在 appendix 表格中，不在任何图表生成脚本中。heatmap 显示的是 BT win probabilities，不是 Cohen's d。

现在已有完整信息，给出审查结论。

---

## FigureOpt 审查结论

### 逐图对比

| 图名 | 决策 | 原因 |
|------|------|------|
| **pipeline_diagram** (Fig 1) | **保留优化版** | 优化版有彩色编号圆圈、清晰的间距和流程箭头。备份版文字严重重叠（"n=100 pairs" 与 "Counterfactual" 挤在一起），可读性差。尺寸从 649×151 缩至 427×97 更适合 `\columnwidth`。 |
| **forest_plot** (Fig 3) | **保留优化版** | 两版数据完全一致。优化版更紧凑（516×325 vs 758×328），使用小号填充/空心菱形标记，图例更简洁（"Sig. (p < .05)" / "Not sig."）。质量相当，紧凑版更适合双栏论文。 |
| **power_curve** (Fig 4) | **保留优化版** | 两版几乎一致：同样的 4 条曲线、同样的 n 标注、同样的 "typical n" 蓝色阴影区。数据未变（d=0.073）。尺寸微调（483×281 vs 497×314）无影响。 |
| **gee_decomposition** (Fig 5) | **保留优化版** | 优化版新增显著性标记（\*\*\*, \*\*, n.s.）在每根柱子上方，新增 "OR = 1" 参考线标签。这些都是对科学图表的实质改进。文件增大 38%（19.8→27.4KB）在合理范围。 |
| **cross_benchmark_heatmap** (Fig 6) | **保留优化版** | 两版在数据和视觉上几乎完全一致。尺寸微调（319×125 vs 309×115）。无退化。 |

### Post-check 3 Critical + 2 Warning 分析

**这些问题全部与图表优化无关**，是论文 LaTeX 的预存问题：

| 级别 | 内容 | 位置 | 处理 |
|------|------|------|------|
| **Critical** | `\ref{sec:amplification}` 无匹配 `\label` | main.tex:47 | 需在正文或 appendix 中添加 `\label{sec:amplification}` |
| **Critical** | `\ref{app:rewriter_indep}` 无匹配 `\label` | main.tex:48 | 需在 appendix 中添加 `\label{app:rewriter_indep}` |
| **Critical** | `\ref{sec:nli_validation}` 无匹配 `\label` | main.tex:53 | 需在对应章节添加 `\label{sec:nli_validation}` |
| **Warning** | `\label{sec:limitations}` 从未被引用 | cross-file | 可忽略或删除多余 label |
| **Warning** | 缺少 'Ethics Statement' 章节 | cross-file | EMNLP 2026 不强制要求 Ethics Statement 在 PDF 中（在 ARR checklist 填写），但建议加一小段 |

### 关于 d=1.120→0.211 的影响

`d=1.120` 仅出现在 `sections/appendix.tex:706`（Table T1），**不影响任何图表**。heatmap 展示的是 BT win probabilities（如 .630, .760），不是 Cohen's d。图表无需重新生成。

### 总结

5 张图全部**保留优化版**，无需恢复备份。3 critical + 2 warning 都是 LaTeX 引用/标签问题，非 FigureOpt 引起，需在论文 tex 文件中单独修复。

---
