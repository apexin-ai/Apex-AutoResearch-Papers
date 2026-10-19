# paper check citation audit status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_check-citation-audit-status_20260515T202514_result.json`
- **Structured JSON:** [`224b7825f86b7c185527.json`](../../sessions/22/224b7825f86b7c185527.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/citation_audit_report.md`。

**结论：审计未通过，2 个 blocking 问题：**

1. **chen2026reconvla 跨章节不一致** — `sections/introduction.tex` 已按 D034 修正为"UQ 框架"定位，但 `related_work.tex`（仍说"action selection"）和 `method.tex`（仍说"conformal selection frontend of ReconVLA"）未同步更新。三个章节对 ReconVLA 的描述互相矛盾。

2. **braun2025cgs / CGS 命名归因** — 论文说"Braun et al. develop Conformalized Gaussian Scoring (CGS)"，但 braun2025cgs 原文标题是"Multivariate Standardized Residuals for Conformal Prediction"。"CGS"可能是本文自创术语，不应归因给 braun2025cgs。需核实原文是否使用该术语。

其余 29 个 \cite{} 键全部在 bib 中存在，22 个方法归因基于论文标题验证通过。bib 中有 14 个未引用条目，提交前建议清理。

---
