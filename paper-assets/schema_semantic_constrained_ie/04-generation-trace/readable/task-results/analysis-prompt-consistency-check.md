# analysis prompt consistency check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prompt_consistency_check_20260513T215555_result.json`
- **Structured JSON:** [`f81a9f18b213f355f53c.json`](../../sessions/f8/f81a9f18b213f355f53c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

### 发现

- **SciERC**: Phase 2 的 `SCIERC_SYSTEM` + `SCIERC_USER_TEMPLATE` 与 Phase 0 的 `MINIMAL_SYSTEM_PROMPT` + `USER_TEMPLATE` **完全一致**，无需修复。

- **DocRED**: 发现两处排序不一致（同一集合，不同顺序）：
  1. **Entity types**: Phase 0 用 `PER, ORG, LOC, TIME, NUM, MISC`，Phase 2 用字母序 `LOC, MISC, NUM, ORG, PER, TIME`
  2. **Relation types**: Phase 0 按名称字母序排列，Phase 2 按 P-code 插入序

### 修复

在 `run_constrained_extraction.py` 中：
1. 添加 `DOCRED_ENTITY_TYPES = ["PER", "ORG", "LOC", "TIME", "NUM", "MISC"]` 常量
2. `build_messages` DocRED 分支改用 `DOCRED_ENTITY_TYPES` + `sorted(relation_types)`
3. `build_s2_entity_messages` / `build_s2_relation_messages` DocRED 分支同步修复

修复后两个数据集的 prompt 均与 Phase 0 逐字一致。

---
