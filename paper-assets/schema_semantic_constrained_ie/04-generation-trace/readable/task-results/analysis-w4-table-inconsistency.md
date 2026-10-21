# analysis w4 table inconsistency

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w4_table_inconsistency_20260515T085646_result.json`
- **Structured JSON:** [`919f7c98448242d495f4.json`](../../sessions/91/919f7c98448242d495f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/rebuttal/w4_table_inconsistency_report.md`。

**核心结论**：
1. **Prompt 一致** — `run_extraction_docred.py:91` 是项目唯一的 prompt 构造函数，Phase 0/Phase 2 unconstrained 都调用 `schema_informed=False` 分支。
2. **当前 jsonl 唯一** — 只有一个 `docred_unconstrained.jsonl`（2026-05-14 21:09），所有 4 个 violation report 都基于它（相同 998 docs / 17497 triples / 20171 entities）。
3. **同一 jsonl 上 v1 vs v2**：DR=18.46% 和 RV=29.66% **完全相同**，只有 ET 不同（v1: 8.18%，v2: 2.48%）。
4. **Table 1 数字（18.7 / 28.9 / 7.5）在当前 outputs 找不到对应文件** — 来自更早一版被覆盖的 Phase 0 推理 + v1 checker。Table 3（18.46 / 29.66 / 2.48）来自当前 jsonl + v2 checker。

**推荐方案 B**：用 v2 数据替换 Table 1 DocRED 行（18.5 / 29.7 / 2.5 / 0.1），与 abstract/conclusion/Table 3 统一。Schema-informed 行建议用 v2 checker 对 `raw_outputs_docred_schema.jsonl` 重评一次。

报告含 9 处需修订位置清单 + 现成的 reviewer 答复。

---
