# analysis 70b docred unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_70b_docred_unconstrained_20260518T214043_result.json`
- **Structured JSON:** [`f712e08ddc2240d67dba.json`](../../sessions/f7/f712e08ddc2240d67dba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总结果：

## 70B DocRED Unconstrained 结果

**完成状态**: 998/998 docs, 0 parse failures (100% success)

**Violation Rates**:
| Type | Rate |
|---|---|
| ET | 0.02% |
| RV | 7.8% |
| DR | 15.0% |
| CF | 0.07% |

**F1 Metrics**:
- Entity F1: **69.03%** (P=75.03%, R=63.92%)
- Relation F1: **13.03%** (P=12.43%, R=13.69%) — method_all_set

**vs 70B SciERC Unconstrained**:
- Entity F1 大幅提升 (69.03% vs 35.17%)，因为 DocRED 实体类型粗粒度 (6 types)
- Relation F1 略高 (13.03% vs 11.22%)
- RV violation 高很多 (7.8% vs 0.6%)，DocRED 用 Wikidata PIDs 做 relation identifier，unconstrained 模型更容易生成 OOV relation
- DR violation 翻倍多 (15.0% vs 6.5%)，ontology 更复杂，constrained decoding 的潜在收益空间更大

结果已写入 `artifacts/70b_docred_unconstrained_analysis.md`。

---
