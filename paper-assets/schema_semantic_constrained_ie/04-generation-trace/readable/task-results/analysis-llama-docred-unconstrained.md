# analysis llama docred unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_docred_unconstrained_20260514T194008_result.json`
- **Structured JSON:** [`a5383fc047bd88455235.json`](../../sessions/a5/a5383fc047bd88455235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部指标已获得。汇总如下：

```json
{
  "experiment": "llama_docred_unconstrained",
  "model": "Llama-3.1-8B-Instruct",
  "dataset": "DocRED",
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)",
  "f1_method": "all_set",

  "documents_checked": 930,
  "parse_failures": 68,
  "total_entities": 16735,
  "total_triples": 16437,

  "entity_type_violation_rate": "0.22%",
  "relation_vocabulary_violation_rate": "16.03%",
  "domain_range_violation_rate": "26.15%",
  "cross_field_consistency_violation_rate": "0.12%",

  "entity_precision": "61.22%",
  "entity_recall": "51.02%",
  "entity_f1": "55.65%",

  "relation_precision": "5.22%",
  "relation_recall": "7.00%",
  "relation_f1": "5.98%",

  "unrecognized_relations_total": 2635,
  "top_unrecognized": ["located in (405)", "date of event (93)", "date of release (60)", "parent (53)", "release date (50)"],
  "invalid_entity_types": {"&lt;empty>": 24, "CONTINENT": 5, "SERIES": 4, "RIVER": 1, "ETHNIC_GROUP": 1, "EVENT": 1}
}
```

**与 Qwen3-8B DocRED unconstrained 对比：**

| 指标 | Qwen3-8B | Llama-3.1-8B | 差异 |
|------|----------|-------------|------|
| parse_failures | 12 | 68 | Llama 解析失败率高 5.7× |
| ET | 2.48% | 0.22% | Llama ET 更低 |
| RV | 29.7% | 16.03% | Llama RV 更低，关系词汇更规范 |
| DR | 18.5% | 26.15% | Llama DR 更高，domain-range 约束违反更严重 |
| CF | 0.10% | 0.12% | 持平 |
| E-F1 | 58.15% | 55.65% | Llama 略低 -2.5pp |
| R-F1 | 7.74% | 5.98% | Llama 更低 -1.76pp |
| entities | 20171 | 16735 | Llama 产出更少实体 |
| triples | 17497 | 16437 | Llama 产出更少三元组 |

**分析：** Llama-3.1-8B 在 DocRED unconstrained 上整体表现弱于 Qwen3-8B——R-F1 低 1.76pp，E-F1 低 2.5pp，且 parse failure 率高得多（68 vs 12）。不过 Llama 的 RV 违反率反而更低（16% vs 30%），说明它更倾向使用标准关系名称；但 DR 违反率更高（26% vs 18.5%），表明即使关系名正确，head/tail 类型约束匹配更差。这为 constrained decoding 提供了更大的潜在改进空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "llama_docred_unconstrained",
    "model": "Llama-3.1-8B-Instruct",
    "dataset": "DocRED",
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)",
    "f1_method": "all_set",
    "documents_checked": 930,
    "parse_failures": 68,
    "total_entities": 16735,
    "total_triples": 16437,
    "entity_type_violation_rate": "0.22%",
    "relation_vocabulary_violation_rate": "16.03%",
    "domain_range_violation_rate": "26.15%",
    "cross_field_consistency_violation_rate": "0.12%",
    "entity_precision": "61.22%",
    "entity_recall": "51.02%",
    "entity_f1": "55.65%",
    "relation_precision": "5.22%",
    "relation_recall": "7.00%",
    "relation_f1": "5.98%",
    "unrecognized_relations_total": 2635,
    "top_unrecognized": [
      "located in (405)",
      "date of event (93)",
      "date of release (60)",
      "parent (53)",
      "release date (50)"
    ],
    "invalid_entity_types": {
      "&lt;empty>": 24,
      "CONTINENT": 5,
      "SERIES": 4,
      "RIVER": 1,
      "ETHNIC_GROUP": 1,
      "EVENT": 1
    }
  }
}
```

</details>

---
