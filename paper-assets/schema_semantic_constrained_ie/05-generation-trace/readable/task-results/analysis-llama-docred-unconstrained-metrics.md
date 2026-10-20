# analysis llama docred unconstrained metrics

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_docred_unconstrained_metrics_20260516T002114_result.json`
- **Structured JSON:** [`3c3e2935e2a97594f646.json`](../../sessions/3c/3c3e2935e2a97594f646.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。计算结果：

```
ET_pct: 0.00
RV_pct: 0.15
DR_pct: 0.49
E_F1: 83.93
E_P: 84.93
E_R: 82.96
R_F1: 43.72
R_P: 38.59
R_R: 50.41
parse_fail_rate: 2.30
total_samples: 998
total_entities_pred: 19106
total_relations_pred: 16171
```

与 registry 原值基本一致，唯一修正：DR_pct 从 0.5 → 0.49（80/16171 = 0.4947%），补充了 `total_entities_pred` 和 `total_relations_pred`。

---
