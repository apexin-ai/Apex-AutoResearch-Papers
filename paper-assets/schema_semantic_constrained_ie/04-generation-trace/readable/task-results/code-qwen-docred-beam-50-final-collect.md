# code qwen docred beam 50 final collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_docred_beam_50_final_collect_20260517T044659_result.json`
- **Structured JSON:** [`241062ea9a6cbe76e48c.json`](../../sessions/24/241062ea9a6cbe76e48c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总如下：

## Qwen DocRED Beam Search 50 docs 结果

| 指标 | Beam (50 docs) | Baseline Greedy (full_s1, 998 docs) |
|------|----------------|--------------------------------------|
| 行数 | 50 | 998 |
| Parse failures | 3 (6%) | 11 |
| ET% (Entity Type violation) | 0.0% | — |
| RV% (Relation Vocab violation) | 0.0% | — |
| DR% (Domain/Range violation) | 0.0% | 0.0% |
| CF% (Cross-field violation) | 0.55% | 2.57% |
| E_F1 | 58.64 | 59.37 |
| R_F1 (all_set) | 9.37 | 8.23 |

**关键发现：**
- **R_F1 提升**：beam search 9.37 vs greedy 8.23（+1.14pp），在仅 50 docs 子集上已可见改善
- **CF violation 大幅降低**：0.55% vs 2.57%
- **ET/RV/DR 全为 0**：schema 约束完全满足
- **E_F1 基本持平**：58.64 vs 59.37（-0.73pp，样本量差异可解释）
- 3 个文档 parse failure（6%），日志显示其中一个（UNESCO Confucius Prize）耗时 129s 后 FAIL

Beam search 在约束遵守和关系 F1 上均优于 greedy baseline。

---
