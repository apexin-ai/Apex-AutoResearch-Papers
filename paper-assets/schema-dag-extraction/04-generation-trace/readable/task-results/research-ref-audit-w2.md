# research ref audit w2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-w2_20260526T101511_result.json`
- **Structured JSON:** [`fe357e04c8bb5014ab52.json`](../../sessions/fe/fe357e04c8bb5014ab52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。63 条 bib entry 全部用 WebSearch 逐条验证。

**结果**：60 条正确，1 条错误，2 条疑似问题，4 条未引用。

需修复项：
1. **`sclar-sensitivity-2024`** — 标题有多余逗号："Design, or:" → "Design or:"
2. **`baan-2023-ecological`** — key 前缀 "baan" 不对应任何作者（实际第一作者 Orlikowski），建议改 key
3. **4 条 entry 未被任何 tex 引用**：`cohen-1988-statistical`、`muller2019when`、`peterson2019human`、`sclar-sensitivity-2024`，建议清理

报告已写入 `artifacts/_project/report/ref_audit_worker2.md`。

---
