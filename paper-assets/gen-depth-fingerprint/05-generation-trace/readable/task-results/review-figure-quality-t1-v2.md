# review figure quality t1 v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_figure-quality-t1-v2_20260519T232837_result.json`
- **Structured JSON:** [`3221f8ad24306ed0f12a.json`](../../sessions/32/3221f8ad24306ed0f12a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Figure 质量检查报告

### 主要 Figure

#### fig1_differential_response.pdf (40KB)
- 字号：OK — 数值标注、坐标轴、分区标签均清晰
- 颜色对比度：OK — 绿/紫/橙三色区分明确，白色背景下对比度足够
- Legend：OK — 右侧分区标签（Drifting/Intermediate/Near-stationary）排布清晰
- H_min† 脚注标记已体现

#### fig2_framework.pdf (58KB)
- 字号：OK — 三面板 (a)(b)(c) 标签、模块文字均可读
- 颜色：OK — 蓝/橙/绿/紫色块编码清晰，信息密度高
- 布局：OK — 三列布局紧凑合理

#### fig3_baseline_comparison.pdf (22KB) / fig3_baseline_comparison.png (75KB)
- 格式：**PNG 副本可清理**（论文引用的是 PDF 版本）
- Annotation：OK — 数值标注、cost 灰色注释可读
- "ours" 行高亮明确（蓝色背景 + 大圆点）

#### fig1_combined.pdf (51KB)
- **⚠ Orphan** — 合并了 fig1 + fig2 的旧版本，论文未引用

### Appendix Figures

| 文件 | 大小 | 检查结果 |
|------|------|----------|
| fig_appendix_confusion.pdf | 29KB | OK — 双面板混淆矩阵，颜色对比度好，数值清晰 |
| fig_appendix_cross_temp.pdf | 29KB | OK — 柱状图+热力图两面板，配色区分清楚 |
| fig_appendix_ddr_trends.pdf | 34KB | **⚠ 问题见下** |
| fig_appendix_per_gen.pdf | 26KB | OK — 双面板，柱状图排序合理，热力图颜色梯度清楚 |
| fig_appendix_violin.pdf | 82KB | OK — 7 个 violin plot，深度颜色编码明确，ρ 标注清晰 |
| fig_appendix_umap.pdf | 2.1MB | **过大需人工检查** |
| fig_convergence_dynamics.pdf | 25KB | OK — 双面板 Cohen's d 趋势图，置信带清晰，(a)(b) 分离合理 |
| fig_ddr_holdout_split.pdf | 29KB | OK — Split A/B 散点图，filled/hollow 标记区分清楚 |
| fig_ddr_scatter.pdf | 34KB | OK — DDR 散点图，阈值虚线 + 菱形特殊标记清晰 |
| fig_transfer_heatmap.pdf | 53KB | **⚠ 问题见下** |

#### fig_appendix_ddr_trends.pdf 问题
1. **Entropy Min 分类标签不一致** — 该图标题标注为 `[INTERMEDIATE]`，但 fig1 和 DDR scatter 中将其归为 **Near-stationary**（带 †），appendix_convergence.tex caption 也写 "Near-stationary features (entropy max, tail decay, entropy min)"。需统一标签。
2. 3×3 网格布局中 7 个子图导致右下两格为空，轻微不平衡（minor）

#### fig_transfer_heatmap.pdf 问题
- **底部文字重叠** — x 轴标签 "Test generator" 与底部统计注释 "Mean cross-gen F1 = 0.810 [95% CI: 0.796, 0.822]" 位置冲突，两者在视觉上相互干扰

### Caption-引用一致性

| Label | 定义位置 | 问题 |
|-------|---------|------|
| `fig:baseline-ci` | main.tex:130 | **从未被 `\ref{fig:baseline-ci}` 引用** — 主论文 Figure 3 在正文中无交叉引用 |
| `fig:convergence-dynamics` | appendix_convergence.tex:5 | **从未被 `\ref` 引用** — appendix 独立 section，影响较小 |

其余 11 个 figure label 均被正文 `\ref` 正确引用。

### Orphan Figures（未被任何 .tex 引用的文件）

**可清理的旧版/重复文件：**
- `fig1_combined.pdf` / `fig1_combined.png` — 旧版合并图，已被 fig1 + fig2 分离替代
- `fig_convergence_dynamics_38638f.pdf` — hash 后缀旧版
- `fig_ddr_holdout_split_c6f4f0.pdf` — hash 后缀旧版

**PNG 副本（论文均引用 PDF）：**
- `fig1_differential_response.png`、`fig2_framework.png`、`fig3_baseline_comparison.png`
- `fig_convergence_dynamics.png`、`fig_ddr_holdout_split.png`、`fig_ddr_scatter.png`、`fig_transfer_heatmap.png`

**脚本/辅助文件（非图片，不影响论文）：**
- 6 个 `.py` 绘图脚本 + 1 个 `_caption.tex` + 1 个 `_pdf_images/` 目录

### 总结：需修复项

1. **fig_appendix_ddr_trends.pdf** — Entropy Min 标签从 `[INTERMEDIATE]` 改为 `[NEAR-STATIONARY]`（与 fig1/DDR scatter/convergence caption 一致）
2. **fig_transfer_heatmap.pdf** — 修复底部 x-axis label 与统计注释的文字重叠
3. **main.tex / results.tex** — 添加对 `fig:baseline-ci` 的 `\ref` 引用（如 "Figure~\ref{fig:baseline-ci}"）
4. 可选：清理 orphan 文件和 PNG 副本以保持 chart 目录整洁

---
