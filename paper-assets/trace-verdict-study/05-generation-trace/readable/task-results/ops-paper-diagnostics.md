# ops paper diagnostics

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_paper-diagnostics_20260523T075118_result.json`
- **Structured JSON:** [`63ac1c2a7005309b409f.json`](../../sessions/63/63ac1c2a7005309b409f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是诊断报告。

---

## 论文 LaTeX 完整性诊断报告

### 1. Appendix 引用完整性

**main.log:** 无 "undefined reference" 或 "multiply defined label" 警告。编译干净。

**Ref ↔ Label 对照:** 主文引用的所有 Appendix section/table/figure label 均在 appendix.tex 中有定义，无 dead reference。覆盖了 `sec:training_dynamics`, `sec:dedup_stats`, `sec:full_results`, `sec:per_class`, `sec:tokenizer_analysis`, `sec:irreducible`, `sec:exc_subcomponent`, `sec:regex_baselines`, `sec:zeroshot_cross_model`, `sec:trace_length_full`, `sec:exception_type`, `sec:error_overlap`, `sec:debugbench_full`, `sec:vota_algorithm`, `sec:vota_examples`, `sec:training_details`, `sec:calibration_analysis` 等全部标签。

**结论：无问题。**

---

### 2. Per-seed Breakdown 表格验证

**WARNING — `full_trace` 标准差不一致（1.11 vs 1.08）**

同一条件（Qwen-7B full_trace, 3-seed）的 std 在论文中出现两个不同值：

| 位置 | 值 |
|------|-----|
| `experiments.tex:30` (Table cross_model) | 81.44±**1.11** |
| `experiments.tex:90` (Table ablation) | 81.44±**1.08** |
| `experiments.tex:169` (footnote, 引用 Table cross_model) | 81.44%±**1.08** |
| `experiments.tex:170` (footnote) | 81.44%±**1.08** |
| `appendix.tex:221` (per-seed 表: 81.76/80.20/82.35) | 81.44±**1.08** |

用 per-seed 原始数据 {81.76, 80.20, 82.35} 计算样本标准差：**std = 1.11**。所以 `experiments.tex:30` 的 1.11 是正确的，其余 4 处的 1.08 **是错的**。

**INFO — 论文使用旧版 per-seed 数据**

论文全文使用旧版 3-seed 数据（81.76 / 80.20 / 82.35, mean=81.44）。新版 v5 数据（81.76 / 79.58 / 80.50, mean=80.61±1.09）未出现在任何 .tex 文件中。如果 v5 是最终实验结果，则需要全面更新。

---

### 3. Figure 文件检查

**graphicspath** 设为 `../../figures/paper/`（即 `/root/trace-verdict-study/figures/paper/`），**不是** `docs/paper/figures/`。

**引用 vs 文件对照：**

| \includegraphics 引用 | 文件存在? |
|------------------------|:---------:|
| `fig1_trace_overview` | ✓ |
| `fig2_calibration` | ✓ |
| `fig3_cross_model_gap` | ✓ |
| `budget_curve` | ✓ |
| `error_overlap` | ✓ |
| `training_dynamics` | ✓ |

**无 missing figure。**

**INFO — Orphan figures（graphicspath 中存在但未被引用）：**
- `fig4_trace_length.pdf/png`
- `fig_trace_length_ablation.pdf/png`

**INFO — `docs/paper/figures/` 目录未被 LaTeX 使用**（graphicspath 指向别处），内含过时文件：`error_containment.*`, `calibration_reliability.*`, `attention_pilot/*`。不影响编译，但可考虑清理。

---

### 4. 参考文献格式

**统计：** 47 条 bib 条目，402 行。无重复 key。

**WARNING — 2 条 bib 条目未被任何 .tex 文件引用：**
- `kamei2013large` — *A Large-Scale Empirical Study of Just-in-Time Quality Assurance*
- `liu2023codeexecution` — *Code Execution with Pre-trained Language Models*

**Missing in bib:** 无。所有 `\cite`/`\citep`/`\citet` 引用的 key 均在 `references.bib` 中有定义。

**重复标题：** 未检测到。

---

### 问题汇总

| # | 严重度 | 问题 |
|---|--------|------|
| 1 | **WARNING** | `full_trace` std 在 5 处出现，4 处写 1.08（错），1 处写 1.11（对） |
| 2 | **WARNING** | 2 条未引用的 bib 条目（`kamei2013large`, `liu2023codeexecution`） |
| 3 | **INFO** | 论文使用旧版 per-seed 数据，需确认是否应更新为 v5 |
| 4 | **INFO** | graphicspath 中有 2 个 orphan figure 文件 |
| 5 | **INFO** | `docs/paper/figures/` 目录非 LaTeX 使用目录，含过时文件 |

---
