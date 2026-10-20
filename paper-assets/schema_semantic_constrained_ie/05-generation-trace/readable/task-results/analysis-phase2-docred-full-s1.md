# analysis phase2 docred full s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_docred_full_s1_20260514T083040_result.json`
- **Structured JSON:** [`3202dc6d1e5b8e3323ae.json`](../../sessions/32/3202dc6d1e5b8e3323ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## phase2_docred_full_s1 结果

### 基本统计
| 指标 | 值 |
|------|-----|
| Documents | 988 checked / 11 parse failures |
| Entities | 20,218 |
| Triples | 17,372 |

### 违规率

| 指标 | full_s1 | unconstrained | schema_informed | grammar_only |
|------|---------|---------------|-----------------|--------------|
| **ET** | **0%** | 7.5% | 0.61% | 0% |
| **RV** | **0.03%** | 28.9% | 18.4% | 0.03% |
| **DR** | **10.19%** | 18.7% | 12.8% | 26.17% |
| **CF** | 2.57% | — | — | — |

### F1 指标
- Entity F1: P=0.645 R=0.662 **F1=0.653** (typed: 0.590)
- Relation F1: P=0.070 R=0.099 **F1=0.082**

### 判断
**Conclusion: success**（DR 5-15% 区间）。DR 从 unconstrained 18.7% 降到 10.19%（-8.5pp, -45.5% relative），但远未达到 SciERC full_s1 的 0.93%。

### 残留 DR 违规集中在
- P190 sister city (58%), P582 end time (43.5%), P205 basin country (37%), P576 dissolved (36.3%), P276 location (28.4%) — 这些关系的 domain/range 约束较宽泛，模型生成的 entity type 组合容易越界。

### 关键发现
Grammar 层完美消除了 ET (0%) 和 RV (0.03%)，但 semantic 层在 DocRED 96 关系上的 DR 约束效果弱于 SciERC (7 关系)。安全回退机制（allowed_types 与 grammar-valid tokens 无交集时跳过 semantic masking）可能是 DR 残留的重要原因。

---
