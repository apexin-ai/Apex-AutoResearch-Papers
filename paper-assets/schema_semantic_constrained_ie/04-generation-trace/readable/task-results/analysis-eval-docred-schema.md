# analysis eval docred schema

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_docred_schema_20260514T014843_result.json`
- **Structured JSON:** [`2199a5f957603f2dd467.json`](../../sessions/21/2199a5f957603f2dd467.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## DocRED Schema-Informed Prompt 实验结果

| 指标 | Schema | Minimal Baseline | Delta |
|------|--------|-----------------|-------|
| **Entity Type Violation** | **0.61%** | 7.5% | **-6.89%** |
| **Relation Vocab Violation** | **18.4%** | 28.9% | **-10.5%** |
| **Domain/Range Violation** | **12.8%** | 18.7% | **-5.9%** |
| Cross-field Consistency | 0.15% | — | — |
| JSON Parse Rate | 94.5% | — | — |
| Total Entities | 19,524 | — | — |
| Total Triples | 16,782 | 16,540 | +242 |
| Docs Checked | 943/998 | — | 55 parse failures |

**三个核心违规维度全部显著下降**，schema-informed prompt 在 96 relation types 的大约束空间下依然有效。DR violation 从 18.7%→12.8%（go/no-go metric），ET 改善最大（降幅 92%）。

仍在运行的实验：`phase2_scierc_full_s2.jsonl` 410/551（GPU 0 占用 16.5GB）。

---
