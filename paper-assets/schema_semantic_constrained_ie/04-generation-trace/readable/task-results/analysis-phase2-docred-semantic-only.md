# analysis phase2 docred semantic only

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_docred_semantic_only_20260514T141517_result.json`
- **Structured JSON:** [`17a580041316e0122928.json`](../../sessions/17/17a580041316e0122928.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下。unconstrained 基准的验证也完全匹配（DR=18.46%, RV=29.66%, ET=8.18%），方法论一致。

## DocRED Semantic-Only 分析结果

### Violation Rates（对比 unconstrained baseline，同方法论）

| Metric | Unconstrained | Semantic_only | Delta | Relative |
|--------|-------------|--------------|-------|----------|
| DR% | 18.46% | **15.05%** | **-3.41pp** | ↓18.5% |
| RV% | 29.66% | 29.87% | +0.21pp | ~unchanged |
| ET% | 8.18% | **18.44%** | **+10.26pp** | ↑125% |
| CF% | 0.17% | 3.52% | +3.35pp | ↑ |

### F1 Metrics（all_set 方法，同方法论）

| Metric | Unconstrained | Semantic_only | Delta |
|--------|-------------|--------------|-------|
| E-F1 | 57.79% | 57.81% | +0.02pp |
| R-F1 | 7.71% | 7.70% | -0.01pp |

### 关键发现

**DR↓ 有效但幅度有限**：TypeConstraintProcessor 将 DR 从 18.46% 降至 15.05%（-3.41pp, ↓18.5%），确认 domain/range 约束生效。

**ET↑↑ 严重副作用**：ET 从 8.18% 暴涨至 18.44%（+10.26pp）。原因是 TypeConstraintProcessor 干扰了 relation 字段中 entity type 的 token 生成，产生大量畸形类型：
- `PERSON`(1081次，应为PER)
- ` TIME`/` LOC`/` MISC`/` PER`(带前导空格，共504次)
- `ORGB`/`OR`(截断，147次)

Entity 列表中的 ET 两组完全相同（499/~20k），所有退化都发生在 relation head/tail 类型字段。

**F1 无变化**：E-F1/R-F1 几乎不变。

### Registry JSON

```json
{
  "documents_checked": 987,
  "parse_failures": 11,
  "total_entities": 20185,
  "total_triples": 17571,
  "domain_range_violation_rate": 0.1505,
  "relation_vocabulary_violation_rate": 0.2987,
  "entity_type_violation_rate": 0.1844,
  "cross_field_consistency_violation_rate": 0.0352,
  "entity_f1": 57.81,
  "entity_precision": 57.27,
  "entity_recall": 58.37,
  "relation_f1": 7.7,
  "relation_precision": 6.54,
  "relation_recall": 9.37,
  "f1_method": "all_set",
  "duplicates_removed": 0,
  "total_lines_before_dedup": 998
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "documents_checked": 987,
    "parse_failures": 11,
    "total_entities": 20185,
    "total_triples": 17571,
    "domain_range_violation_rate": 0.1505,
    "relation_vocabulary_violation_rate": 0.2987,
    "entity_type_violation_rate": 0.1844,
    "cross_field_consistency_violation_rate": 0.0352,
    "entity_f1": 57.81,
    "entity_precision": 57.27,
    "entity_recall": 58.37,
    "relation_f1": 7.7,
    "relation_precision": 6.54,
    "relation_recall": 9.37,
    "f1_method": "all_set",
    "duplicates_removed": 0,
    "total_lines_before_dedup": 998
  }
}
```

</details>

---
