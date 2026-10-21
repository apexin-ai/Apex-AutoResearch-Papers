# analysis paper audit review

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_audit_review_20260518T215610_result.json`
- **Structured JSON:** [`dca4597ffc0b578e2034.json`](../../sessions/dc/dca4597ffc0b578e2034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。总结：

**核心发现：**
1. **无 delta > 1pp** — 24 条记录最大偏差 +0.85pp（4B SciERC），论文数字无需紧急修改
2. **无 needs_update 字段** — 所有条目 status=verified
3. **9/24 条目缺 degen_pct**，其中 3 个可从 recalc 补充（4B CoNLL=90.57%, SciERC seed123=17.2%, seed456=20.42%），4 个仍需补跑（rank=8, N=32, N=16 seed42, FewNERD N=8 seed42）
4. **退化率交叉验证通过** — 所有 15 个重叠条目 audit 与 recalc 精确匹配

**待办：** 4 个位置需补跑 `unified_metrics.compute_degeneracy()`（rank=8, N=32, N=16 seed42, FewNERD N=8 seed42）。Canonical 数值已录入 memory.md。

---
