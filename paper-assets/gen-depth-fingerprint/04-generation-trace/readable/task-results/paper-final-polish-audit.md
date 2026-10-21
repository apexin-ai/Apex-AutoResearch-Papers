# paper final polish audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-polish-audit_20260522T184620_result.json`
- **Structured JSON:** [`6d2f4a40e69fd0f08604.json`](../../sessions/6d/6d2f4a40e69fd0f08604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 审查报告

### 1. 编译验证 — **PASS** (修复后)

| 项目 | 结果 |
|------|------|
| Errors | **0** |
| Undefined references | **0** (初次编译有 2 个 undefined citations `xu_spectrum_detection`/`welleck_unlikelihood`，原因是 `.bib` 未同步；已修复) |
| pdfTeX dest warnings | **0** (初次编译的 `subsection.2.4` warning 在重编后消失) |
| natbib warnings | **0** |
| 主文页数 | Conclusion 在 p.8，Limitations/Ethics 也在 p.8，References 从 p.9 开始 → **≤8 页合规** |
| 总页数 | 36 页 |

**需关注**：`results.tex` L127–141 的 baselines 表有 **Overfull hbox (7.6pt)**，该表未用 `\resizebox` 包裹（对比 L39 的 LOGO 表用了 `\resizebox`）。

### 2. 全文一致性扫描

**a) Abstract 数字一致性 — PASS**

| Abstract 数值 | 正文来源 | 一致 |
|---|---|---|
| F1=0.694 | results.tex L53 Table 平均 Bin F1 | ✓ |
| 0.762 | results.tex L16 "3-class LOGO F1=0.762" | ✓ |
| 0.905 | results.tex L25 "3-class F1=0.905" | ✓ |
| d=0.76–1.17 | results.tex L91 | ✓ |
| d<0.10 | results.tex L80 | ✓ |
| d=0.55 | results.tex L80, L94 | ✓ |

**b) "base-model" vs "base model" — PASS**
用法统一且正确：复合形容词用连字符 `base-model` (如 "base-model generators")，名词用空格 `base models` (如 "applicability to base models")。

**c) Appendix 交叉引用 — PASS (有 minor)**
- 所有 `\ref{app:...}` 均有对应 `\label{app:...}`，**0 个悬空引用**
- 4 个 label 已定义但未被引用：`app:convergence`、`app:ddr-causality`、`app:ddr-supplement`、`app:holdout-split` — 这些附录节存在但没有任何地方用 `\ref` 指向它们（`app:holdout-split` 内部用的是 `tab:holdout-split`）。不影响编译，但 reviewer 可能会注意到未引用的附录节。

### 3. R48-W8 新增句检查 — **PASS**

`results.tex` L145：
> *"Concurrent iterative-generation studies use different chain operators (back-translation, rephrasing) and target different phenomena (factuality, convergence dynamics), precluding direct inclusion as depth classification baselines (Appendix~\ref{app:iterative-comparison})."*

- 编译正常，无 undefined citation ✓
- 引用格式正确（`\ref{app:iterative-comparison}` 有对应 label）✓
- 句子语法通顺 ✓

### 4. 遗留标记扫描 — **PASS**

`artifacts/_project/paper/*.tex` 和 `docs/paper/*.tex` 中均无 TODO/FIXME/XXX/HACK 标记。

---

### 建议修复（2 项）

1. **baselines 表 overfull hbox** — `results.tex` L127 的 `\begin{tabular}` 可改为 `\resizebox{\columnwidth}{!}{...}` 包裹，与 L39 的 LOGO 表保持一致
2. **4 个未引用附录 label** — 建议在正文或其他附录中添加对 `app:convergence`、`app:ddr-causality`、`app:ddr-supplement` 的引用，或去掉这些 label（`app:holdout-split` 作为 subsection label 在 `appendix_ddr_validation.tex` 内部被 `tab:holdout-split` 间接定位，可保留）

---
