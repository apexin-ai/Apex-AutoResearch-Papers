# check docred grammar only completion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_docred_grammar_only_completion_20260514T073900_result.json`
- **Structured JSON:** [`a527c63a8c06e3a7af01.json`](../../sessions/a5/a527c63a8c06e3a7af01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **phase2_docred_grammar_only** 已完成，registry 已更新为 DONE，cron 已清除。

## 结果摘要

| 指标 | Baseline (unconstrained) | Grammar-only |
|------|-------------------------|-------------|
| ET violations | 7.5% | **0%** |
| RV violations | 28.9% | **0.03%** (5/17341) |
| D/R violations | — | 26.2% (4539/17341) |
| Parse failures | — | 13/998 |

**结论**：Grammar-only constrained decoding 在 DocRED 96 种 relation types 上成功消除了 ET violations（7.5%→0%）和 RV violations（28.9%→0.03%），与 SciERC 上的结果一致，验证了 grammar 层在复杂 schema 上的泛化性。

D/R violations 仍有 26.2%，符合预期——grammar 层只约束 JSON 结构和 enum 值域，不约束 domain/range 语义一致性，这正是 semantic 约束层要解决的问题。

---
