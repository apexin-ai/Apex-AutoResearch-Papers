# analysis phase2 docred unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_docred_unconstrained_20260514T131355_result.json`
- **Structured JSON:** [`80df6b8d2cff0a193879.json`](../../sessions/80/80df6b8d2cff0a193879.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DocRED Phase 2 Unconstrained Baseline — 完整结果

### 数据完整性
- JSONL: **998 行**, 0 重复（无需去重）
- 日志: 998/998 processed, success=986, fail=12
- Parse rate: **98.8%**

### Violation Rates

| 指标 | Phase 2 Unconstrained | Phase 0 Unconstrained | Phase 2 grammar_only | Phase 2 full_s1 |
|------|----------------------|----------------------|---------------------|----------------|
| **DR%** | **18.46%** | 18.7% | 26.17% | 10.19% |
| **RV%** | **29.66%** | 28.9% | 0.03% | 0.03% |
| **ET%** | **8.18%** | 7.5% | 0% | 0% |
| **CF%** | **0.10%** | — | — | — |

### F1 Metrics

| 指标 | Phase 2 Unconstrained | Phase 2 full_s1 |
|------|----------------------|----------------|
| **Entity F1** | **57.79%** (P=57.26, R=58.32) | — |
| **Relation F1** | **7.69%** (P=6.54, R=9.34) | 8.17% |

### 统计量
- Total entities: 20,171 | Total triples: 17,497
- 30.4% 预测 relation 使用了 ontology 外的名称（与 RV=29.66% 一致）
- Fuzzy relation matches: 129

### 对比分析
Violation rates 非常接近 Phase 0（DR 18.46% vs 18.7%, RV 29.66% vs 28.9%, ET 8.18% vs 7.5%），确认 Phase 2 unconstrained baseline 复现了无约束条件下的 violation profile。消融表的 baseline 有效——constrained 方法（grammar_only/full_s1）显著降低了 RV 和 ET violation，full_s1 进一步将 DR 从 18.46% 降至 10.19%。

---
