# ssh paper precheck audit

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_paper_precheck_audit_20260524T042721_result.json`
- **Structured JSON:** [`1eff54614ee63a97897d.json`](../../sessions/1e/1eff54614ee63a97897d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Let me compile the report.

---

## 预检报告

### 1. 编译状态：**通过**

PDF 成功生成（16 页，544KB）。无 fatal error，无 undefined reference，无 missing file。

**Overfull hbox（8 处）：**
| 严重程度 | 位置 | 溢出量 |
|---------|------|--------|
| 严重 | appendix L311-325 | 27.8pt |
| 中等 | appendix L366-376 | 14.2pt |
| 中等 | appendix L385-395 | 14.2pt |
| 轻微 | abstract L6-7 | 0.7pt |
| 轻微 | abstract L9 | 0.5pt |
| 中等 | abstract L46 | 9.1pt |
| 轻微 | method L62-72 | 1.7pt |
| 轻微 | appendix L250-260 | 2.2pt |

27.8pt 那处（appendix 表格）会明显超出页面边界，应该修。

**Underfull（14 处）：** 多数 badness < 3500，属正常范围。1 处 badness=10000（introduction L50-51），可能有段落过于稀疏。1 处 vbox badness=10000（分页问题）。

**页数：** 主文 1-8 页（intro→conclusion），Limitations 在第 8 页，References 第 9-10 页，Appendix 第 11-16 页。主文 **8 页，符合 EMNLP 限制**。

**Warning：** 仅 `'h' float specifier changed to 'ht'`（无害）和 hyperref token warning（无害）。

### 2. 占位符清单

| 文件 | 行号 | 内容 |
|------|------|------|
| experiments.tex | 7 | `XX{,}XXX observations; XX.X\% fill rate` — 观测数和填充率未填 |
| experiments.tex | 29-37 | Table 1 右两列（17 models）全部 `TBD`（共 16 个 TBD） |
| experiments.tex | 40 | caption 中 `(TBD)` |
| limitations.tex | 1 | `XX.X\% fill rate (XX{,}XXX of XX{,}XXX potential cells)` — 三处 XX 未填 |
| method.tex | 85 | `XX.X\% fill rate` |

**合计：5 处 XX 占位符 + 16 个 TBD（Table 1 的 17-model 结果）。**

### 3. 数字一致性

**一致的数字（跨文件无矛盾）：**
- τ = 0.857 (G-MFRM) / 0.786 (baseline) / 0.952 / 0.905 — abstract, intro, experiments, conclusion, appendix 全部一致
- Δτ CI = [-0.071, 0.071] — experiments, appendix 一致
- P(Δτ ≥ 0) = 0.927 — experiments 一致
- LOO ELPD = -55.7, |Δ/SE| = 5.9 — abstract, experiments 一致
- c_n 值：GPT-3.5-Turbo = 5.60, GPT-4-0613 = 4.20, GPT-4o = 0.88, GPT-4o-mini = 0.93 — experiments, appendix table 一致
- d_j 值：Claude Opus +0.60, GPT-5.5 +0.53, DeepSeek +0.31, LLaMA -0.42, Mistral -0.74 — experiments, appendix table 一致
- Synthetic N=8: θ-RMSE -50.3%, c_n-RMSE -60.5% — appendix 一致
- Synthetic N=20: θ-RMSE -45.2%, c_n-RMSE -54.5%, p = 1.81×10⁻⁴ — appendix 一致
- Error prop: +5.9% θ, +7.9% c_n at σ=0.2 — method, experiments 一致
- N ≈ 17 for 80% power — experiments, appendix, limitations 一致
- 176 items, 316 原始 items — experiments, appendix 一致

**未发现跨文件数字矛盾。**

### 4. Figure 审计

| 引用名 | tex 位置 | 文件存在 | 生成脚本 |
|--------|---------|---------|---------|
| fig1_framework | method.tex:8 | `fig1_framework.pdf` | `gen_fig1.py` |
| fig2_ovb_bias | background.tex:40 | `fig2_ovb_bias.pdf` | `gen_fig2.py` (+ `collect_fig2_local.py`) |
| fig3_error_propagation | appendix.tex:198 | `fig3_error_propagation.pdf` | `gen_fig3.py` |
| fig4_bias_vs_rho | appendix.tex:176 | `fig4_bias_vs_rho.pdf` | 未找到独立脚本 |
| fig5_cn_recovery | appendix.tex:187 | `fig5_cn_recovery.pdf` | 未找到独立脚本 |
| fig_ppc | appendix.tex:165 | `fig_ppc.pdf` | 未找到独立脚本 |

**所有 6 张引用图的 PDF 文件均存在。** 3 张有生成脚本，3 张（fig4, fig5, fig_ppc）无独立脚本（可能由 `generate_diagnostics.py` 在 exp008 中生成）。

figures 目录中还有未被论文引用的图：`forest_cn.pdf`, `forest_dj.pdf`, `trace_*.pdf`（5 张）, `ablation_boxplots.pdf`, `model_comparison.pdf`, `pareto_k_plot.pdf`, `theta_tau_boxplot.pdf`。

### 阻塞项总结

1. **必须修**：5 处 XX 占位符（observations 数、fill rate）— experiments.tex:7, limitations.tex:1, method.tex:85
2. **必须修**：Table 1 右两列 17-model 结果全部 TBD（16 个值）
3. **建议修**：appendix L311-325 overfull 27.8pt（表格超出边界）
4. **非阻塞**：abstract ~190 words，在 200 限制内

---
