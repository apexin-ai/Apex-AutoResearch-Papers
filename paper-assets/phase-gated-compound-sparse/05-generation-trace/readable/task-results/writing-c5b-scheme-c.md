# writing c5b scheme c

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_c5b_scheme_c_20260514T145226_result.json`
- **Structured JSON:** [`00bbfc4e7a12251a30a8.json`](../../sessions/00/00bbfc4e7a12251a30a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已更新完成。修改点：

1. **§2.5 新增** — "Implementation Scheme: C (Director Decision 2026-05-14)"，明确 KV eviction phase-aware + head pruning uniform 的方案，含 rationale 和 interpretive value
2. **§3.2 Condition B** — 标题描述改为明确 KV eviction，allocation rule 标注为 KV eviction allocation rule，注明 head pruning 保持 uniform
3. **§3.3 Condition C** — 加注 "only KV eviction sparsity varies by phase; head pruning remains uniform"
4. **§7 Scenario C** — 用 Scheme C 视角重写 FAIL 解释：head pruning 固定损伤是 compound severity 主要来源
5. **§9 Handoff Checklist** — 新增 Scheme C 专项条目，compute-match 约束明确限定为 KV eviction budget

---
