# analysis holm bonferroni

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_holm_bonferroni_20260525T214141_result.json`
- **Structured JSON:** [`2a60797f62a78341f953.json`](../../sessions/2a/2a60797f62a78341f953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are clean. Here's the summary:

---

**假设检验族定义：**
- **AR GAR 族**（每个 β level 独立）：4 个 Wilcoxon tests per β → 已有的 Bonferroni 改为 Holm-Bonferroni 表述
- **Instruction Retention 族**（m=2）：McNemar test + Pearson correlation

**Holm-Bonferroni 校正（IR 族，m=2）：**

| 排序 | 检验 | 原始 p | 调整阈值 α/(m−i+1) | 结论 |
|------|------|--------|-------------------|------|
| 1 | Pearson GAR-compliance | 0.007 | 0.05/2 = 0.025 | **显著** (0.007 < 0.025) |
| 2 | McNemar β=0 vs β=3 | 0.077 | 0.05/1 = 0.05 | **不显著** (0.077 > 0.05) |

校正后所有结论不变——McNemar 本来就不显著，Pearson 在更严格阈值下仍然显著。

**修改位置（均在 `appendix.tex`）：**
1. **Line 74** — IR 节 Correlation analysis 段：添加 Holm-Bonferroni 校正说明
2. **Line 143** — Statistical Test Details 节 Multiple comparisons 段：Bonferroni → Holm-Bonferroni，补充 IR 族校正
3. **Line 745** — Extended Statistical Analysis 节 Instruction retention 段：添加校正细节
4. **Line 747** — Extended Statistical Analysis 节 Multiple comparisons 段：补充 IR 族校正

---
