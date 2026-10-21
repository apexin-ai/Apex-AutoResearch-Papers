# paper section3 method warnings fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section3_method_warnings_fix_20260514T055617_result.json`
- **Structured JSON:** [`a5e42f0342d1d39cd9c8.json`](../../sessions/a5/a5e42f0342d1d39cd9c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用工具列表中，跳过注册步骤。

验证结果：

1. **"invariant" 已清除** — 文件中不再出现该词（grep 零匹配）
2. **Head type masking 三路径已覆盖** — Match（registry 与 domain 一致 → 单一类型）、Conflict（registry 与 domain 冲突 → fallback 到 dom(r_j) 全集，优先 ontology）、Unknown（r_j 未知 → 仅 grammar 层）
3. **无 formalize/revisit taxonomy 的承诺** — 第 55 行的 forward reference 已删除；第 11 行改为 "Further discussion...appears in" 而非 "Formal analysis...deferred to"
4. **Fallback 定位为 engineering robustness** — "grammar-first fallback"，明确标注为 error recovery 而非 formal guarantee，附 SciERC/DocRED 触发率数据

---
