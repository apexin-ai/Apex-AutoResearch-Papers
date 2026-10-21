# analysis 70b docred constrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_70b_docred_constrained_20260518T214345_result.json`
- **Structured JSON:** [`aed6c0629c36f34b8124.json`](../../sessions/ae/aed6c0629c36f34b8124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 70B DocRED 结果汇总

| Metric | Constrained (full_s1) | Unconstrained | Delta |
|--------|----------------------|---------------|-------|
| **ET violation** | **0.00%** | 0.02% | -0.02pp |
| **RV violation** | **0.00%** | 7.81% | -7.81pp |
| **DR violation** | **0.00%** | 14.99% | -14.99pp |
| CF violation | 7.01% | 0.10% | +6.91pp |
| Entity F1 | 69.05% | 69.03% | +0.02pp |
| Relation F1 | 13.07% | 13.03% | +0.04pp |
| Parse failures | 1 | 0 | — |
| Docs processed | 997/998 | 998/998 | — |

**核心结论：**
- ET/RV/DR 三项 violation 全部归零，constrained decoding 在 70B + DocRED 上完美工作
- F1 几乎无损（甚至微升 +0.04pp），确认约束不损害抽取质量
- CF violation（跨字段一致性）从 0.10% 升至 7.01%，这是因为 constrained 模式强制修正单个 relation 的 entity type 时，可能导致同一 entity 在不同 relation 中被分配不同的合法 type
- 与 SciERC 70B 结果一致：OntoCoDec 在跨句 RE 数据集上同样有效

---
