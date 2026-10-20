# paper writing assembly

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_assembly_20260515T044904_result.json`
- **Structured JSON:** [`5ae696587c23b9c37796.json`](../../sessions/5a/5ae696587c23b9c37796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**main.tex** — `artifacts/_project/paper/main.tex`
- ACL 2023 模板，`\usepackage[review]{acl}` 匿名审稿模式
- `\input` 整合 introduction / related_work / method / results 四个已完成章节
- Discussion / Limitations / Conclusion / Ethics 以注释占位待另一 Worker 完成后启用
- Abstract 基于论文核心 claims 撰写
- `\graphicspath{{../chart/}}` 指向图表目录
- `\appendix` 含 Length Confound Analysis 占位（results.tex 引用了 `\ref{app:length}`）

**Tables** — results.tex 中 4 张表均已完整定义，数据与实验结果一致：
- Table 1 (tab:logo-results): 6 generator LOGO F1
- Table 2 (tab:ablation): Feature ablation
- Table 3 (tab:downstream): Downstream perplexity
- Table 4 (tab:baselines): Baseline comparison with CIs

**Bib 修复** — `strong_model_collapse` year 从 2024 改为 2025（ICLR 2025）

**Placeholder citations 修复** — method.tex 中 6 处 `\cite{placeholder}` 替换为正确引用键（pythia, olmo, qwen3, xgboost, fast_detectgpt, binoculars, ld_score）

**build.sh** — `artifacts/_project/paper/build.sh`，自动拷贝 bib 文件 + pdflatex×3 + bibtex 编译流程。编译前需将 `acl.sty` 和 `acl_natbib.bst` 放入 paper 目录。

---
