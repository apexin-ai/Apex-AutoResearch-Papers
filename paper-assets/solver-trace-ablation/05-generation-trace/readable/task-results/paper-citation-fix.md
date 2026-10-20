# paper citation fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation-fix_20260515T225012_result.json`
- **Structured JSON:** [`d9f9f50584e852177158.json`](../../sessions/d9/d9f9f50584e852177158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- `references.bib`: 添加了 `lundberg-shap`（Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions", NeurIPS 2017, arXiv:1705.07874）
- `method.tex` 第 26 行: `\citep{demillo1978, sundararajan-ig}` → `\citep{demillo1978, sundararajan-ig, lundberg-shap}`

原本已有 `sundararajan-ig`（Integrated Gradients）覆盖 feature attribution，现在加上 SHAP 使引用更完整。改动不影响页数。

---
