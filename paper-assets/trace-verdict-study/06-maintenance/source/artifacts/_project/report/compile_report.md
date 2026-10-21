# LaTeX Compile Report

**Date:** 2026-05-16
**Compiler:** pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025)
**Build:** pdflatex x3 + bibtex

## Result: SUCCESS

| Metric | Value |
|--------|-------|
| Pages | 14 (A4) |
| File size | 322 KB |
| Errors | 0 |
| Undefined references | 0 |
| Missing citations | 0 |
| LaTeX warnings | 0 |
| Overfull hbox | 3 (minor, all < 30pt) |
| Underfull hbox | 131 (normal for ACL format) |

## Fixes Applied

1. **fig4_trace_length.pdf** — Matplotlib 生成的 PDF 不符合 Adobe 规范，pdflatex 无法 include。用 Ghostscript 重新处理修复。
2. **experiments.tex** — Table 2 (component ablation) 添加 `\resizebox{\columnwidth}{!}{...}` 消除 62pt overfull。
3. **appendix.tex** — Table 7 (full Qwen results) 添加 `\resizebox` 消除 22pt overfull。
4. **appendix.tex** — Table 8 (full DeepSeek results) 添加 `\resizebox` 消除 90pt overfull。
5. **appendix.tex** — Table 3 (hyperparameters) 添加 `\resizebox`，合并 Hardware 行消除 18pt overfull。

## Remaining Overfull (acceptable)

- Abstract text: 29pt (long inline formula/numbers)
- Discussion paragraph: 13pt (text flow)
- Verbatim block: 13pt (code example, cannot wrap)

## File Inventory

All required files present:
- main.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex, appendix.tex
- references.bib, acl.sty, acl_natbib.bst
- Figures: fig1_trace_overview.pdf, fig2_calibration.pdf, fig3_cross_model_gap.pdf, fig4_trace_length.pdf
