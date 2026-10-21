# paper figure fig edcr relations

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_edcr_relations_20260517T183627_result.json`
- **Structured JSON:** [`9b3314a336707e67d89f.json`](../../sessions/9b/9b3314a336707e67d89f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**产出**：`artifacts/fig_edcr_relations.pdf`（已注册 `art_20260517_bc35fb`）

**数据概览**：
- 93 个 relation types（比预期的 76 个多，来自 RSFT-CED s44 dev predictions）
- EDCR >= 0.70 的有 **45 个** relation（严重 decoupling，红色区域）
- EDCR < 0.30 的有 **13 个** relation（健康，绿色区域）
- 7 个 relation EDCR = 1.0（全为 distractor citations，tp=0）：capital of, chairperson, end time, instance of, original language of work, parent organization, work location
- 底部 EDCR = 0.0 的 relation（如 influenced by, location of formation 等）同样 tp=0，说明模型完全未预测这些 relation

---
