# code fix violation checkers

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_violation_checkers_20260513T180257_result.json`
- **Structured JSON:** [`90e870975e0e98ba693b.json`](../../sessions/90/90e870975e0e98ba693b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果清楚地证实了 Reviewer 指出的问题。

## 修改结果总结

### 核心修复
两个 checker 的 violations 从 3 类拆分为 4 类独立计数，`relation_vocabulary_violations` 不再混入 `domain_range_violations`。

### DocRED 对比（37 docs, 610 triples）

| 指标 | 旧版（混合） | 新版（拆分） |
|---|---|---|
| violated_triples (旧指标) | 20/30 = **66.7%** | N/A |
| relation_vocabulary_violations | 不区分 | **193/610 = 31.6%** |
| domain_range_violations | 20 (含 vocab) | **88/610 = 14.4%** |
| **go_nogo_metric** | 0.6667 (高估) | **0.1443** |

旧版把 193 个 vocab violations 都算进了 domain_range，导致违规率被严重高估。新版的 go_nogo_metric 仅基于 domain_range_violation_rate (14.4%)，排除了 grammar-constrained decoding 能解决的 vocab violations。

### SciERC (3 samples, 5 triples)
- Relation vocab violations: 0/5 (0.0%)
- Domain/range violations: 1/5 (20.0%)
- Fuzzy matches: 0

### 新增功能
1. **4 类 violation 独立计数**：entity_type / relation_vocabulary / domain_range / cross_field_consistency
2. **Fuzzy matching**：token overlap >80% 和 Levenshtein ≤2，DocRED 匹配了 8 个原本会算 vocab violation 的 triples
3. **go_nogo_metric**：per-triple domain_range_violation_rate，明确排除 vocab violations

### 产出文件
- `violation_checker.py` (345 行)
- `violation_checker_docred.py` (354 行)
- `outputs/violation_report_fixed.json`
- `outputs/violation_report_docred_fixed.json`

---
