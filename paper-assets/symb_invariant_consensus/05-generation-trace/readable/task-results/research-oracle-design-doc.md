# research oracle design doc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_oracle-design-doc_20260517T163042_result.json`
- **Structured JSON:** [`7ddd9dfc9abc3b6128ac.json`](../../sessions/7d/7ddd9dfc9abc3b6128ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/oracle_experiment_design.md`。

核心结论：推荐方案 (a) Per-trace FOL Verification + MAX-SAT Aggregation。它是唯一能在控制提取质量的同时保留 SICA 聚合机制的设计，直接回答"完美提取下 MAX-SAT 是否优于投票"这一核心问题。方案 (b) 绕过了聚合、方案 (c) 测的是过滤而非聚合，均不适合。

---
