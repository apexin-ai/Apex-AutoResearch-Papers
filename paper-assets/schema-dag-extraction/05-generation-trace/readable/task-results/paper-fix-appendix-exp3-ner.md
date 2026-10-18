# paper fix appendix exp3 ner

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_appendix_exp3_ner_20260517T133636_result.json`
- **Structured JSON:** [`03079603e5c7eab38391.json`](../../sessions/03/03079603e5c7eab38391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications pass:

1. **旧值已清除** — `0.962`, `0.822`, `0.666` 均不存在
2. **无 em-dash** — 全文无 `—`
3. **NER 表格 6 行** — count 2/6/12/22/44/66 全部包含，数值正确
4. **Narrative 合规** — NER 部分无 "tightly track" / "near-identical"；"near-identical" 仅用于 FewRel RE slopes
5. **FewRel (Exp 1) 完整保留** — RE 表格数据和 slopes 未变
6. **结论段按 D055 结构**：FewRel = quantitative match, NER = directional consistency + U-shape replication, combined = architecture-independent in direction

---
