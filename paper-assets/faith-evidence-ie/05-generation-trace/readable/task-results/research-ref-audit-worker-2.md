# research ref audit worker 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-2_20260526T103533_result.json`
- **Structured JSON:** [`9038984352d0cc15ebf8.json`](../../sessions/90/9038984352d0cc15ebf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/ref_audit_worker2.md`。

**结果**: 52 条引用, 14 条有问题, 17 条未被引用。

**P0 严重 (6条)**:
- `gulcehre2023rest` — 作者名错 (Dyer/Grangier → Doucet/de Freitas) + entry type 错
- `ma2023dreeam` — Venue 错 (Findings → EACL main)
- `wang2025relprior` — 标题严重偏差
- `rafailov2023direct` — 作者顺序错 (Ermon/Manning 互换)
- `xu2024lmrc` — 标题多余 "LMRC:" 前缀
- `wang2025rullm` — 标题多余 "Ru-LLM:" 前缀 + 可能多一位作者

**P1 中等 (2条)**: `li2026qurl` 和 `liu2026gdpo` venue 需从 arXiv 更新为已接收会议

**全部 7 条 2026 引用均确认真实存在**, 无虚构引用。

---
