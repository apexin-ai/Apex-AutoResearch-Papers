# code d049 cf majority voting

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d049_cf_majority_voting_20260518T101948_result.json`
- **Structured JSON:** [`6af3e8721b8af379063a.json`](../../sessions/6a/6af3e8721b8af379063a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署并验证。Dry-run 结果：

- **246 文档**，修正前 698 个 CF 违规，修正后 596 个，修正率 14.6%
- 127 次修正，675 次被 AC 约束阻止
- 主要修正 pattern: `PER→FAC` (20), `PER→GPE` (14), `ORG→GPE` (10)
- AC-blocked 大量存在是合理的：多数 CF 违规本就是因为 Place 等角色的 AC 约束强制改了 entity_type（如人名在 Place 角色下被强制标为 LOC/FAC），majority voting 无法反向修正这些而不违反 AC

脚本位于 `/root/schema_semantic_constrained_ie/cf_majority_voting.py`。

---
