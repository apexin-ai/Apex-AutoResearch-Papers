# research citation audit A

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-audit-A_20260529T063723_result.json`
- **Structured JSON:** [`4ceba701ad6a718b8195.json`](../../sessions/4c/4ceba701ad6a718b8195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成，结果写入 `artifacts/citation_audit_worker_A.md`。

**14/18 正确，4 条需要修复：**

| # | Key | 问题 |
|---|-----|------|
| 2 | `lian2026bayesianvla` | 标题过时 ("BayesianVLA" → "LangForce")；venue 需更新为 ICML 2026 |
| 5 | `zhang2026instruction` | 标题两处错误："Anchor" → "Anchors"，"Mechanistic" → "Causal" |
| 9 | `zheng2024tracevla` | 年份 2024 → 2025；venue 需更新为 ICLR 2025 |
| 13 | `brohan2023_rt2` | venue 需从 arXiv 更新为 CoRL 2023 (PMLR vol 229) |

---
