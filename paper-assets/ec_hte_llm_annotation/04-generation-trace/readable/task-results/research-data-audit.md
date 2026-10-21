# research data audit

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-audit_20260523T110848_result.json`
- **Structured JSON:** [`60552715d3598d878a95.json`](../../sessions/60/60552715d3598d878a95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/data_audit_report.md`。

**核心结果**:
- **Table 1**: 全部 33 个 cell 精确匹配 ✅
- **主文定量声明**: 52 个数字中 40 个精确匹配 (76.9%)

**需要关注的 3 个问题**:

1. 🔴 **AUC = 0.86** (出现 3 次: abstract, experiments, method) — 源数据 exp-005 显示 `subgroup_level_auc = 0.833`，不是 0.86。0.86 是 `subgroup_correlation`，疑似混淆了 correlation 和 AUC。建议修正为 0.83。

2. 🟡 **"AUC decreases from 0.86 to 0.82" (theory.tex Remark 1)** — 0.82 无法在任何 CSV 中找到来源。

3. 🟡 **"global correction degrades to 74–82%" (theory.tex, A5 violation)** — 数据显示 global coverage = 84.5%，与 74–82% 差距较大。可能来自旧版实验或不同参数化。

---
