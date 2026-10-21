# analysis 8b s44 eval logs

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b_s44_eval_logs_20260523T075718_result.json`
- **Structured JSON:** [`5fb90a1d11a384468c75.json`](../../sessions/5f/5fb90a1d11a384468c75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部成功完成（EXIT_CODE=0），PID 220069 已终止。汇总如下：

## 1. test_eval_8b_rsft_s44_no_evi (8B RSFT k1 s44, no-evidence)

```json
{
  "f1": 0.3264, "precision": 0.5006, "recall": 0.2422,
  "ign_f1": 0.3264, "ign_precision": 0.5006, "ign_recall": 0.2422,
  "evi_f1": 0.1511, "evi_f1_joint": 0.0627, "edcr": 0.7907,
  "n_documents": 500, "n_truncated": 39, "format_ok_rate": 0.992,
  "field_compliance_rate": 0.116, "evidence_format_rate": 0.112,
  "n_predictions": 18279, "tp": 4202, "pred_count": 8394, "gold_count": 17350
}
```

## 2. test_eval_8b_rsft_s44_with_evi (8B RSFT k1 s44, with-evidence)

```json
{
  "f1": 0.3329, "precision": 0.5133, "recall": 0.2463,
  "ign_f1": 0.3329, "ign_precision": 0.5133, "ign_recall": 0.2463,
  "evi_f1": 0.5897, "evi_f1_joint": 0.2458, "edcr": 0.8090,
  "n_documents": 500, "n_truncated": 29, "format_ok_rate": 0.996,
  "field_compliance_rate": 0.994, "evidence_format_rate": 0.964,
  "n_predictions": 15128, "tp": 4273, "pred_count": 8325, "gold_count": 17350
}
```

## 3. test_eval_8b_rsft_s43_no_evi (8B RSFT k1 s43, no-evidence)

```json
{
  "f1": 0.3224, "precision": 0.5017, "recall": 0.2375,
  "ign_f1": 0.3224, "ign_precision": 0.5017, "ign_recall": 0.2375,
  "evi_f1": 0.2301, "evi_f1_joint": 0.0938, "edcr": 0.7218,
  "n_documents": 500, "n_truncated": 43, "format_ok_rate": 0.998,
  "field_compliance_rate": 0.146, "evidence_format_rate": 0.146,
  "n_predictions": 18972, "tp": 4120, "pred_count": 8212, "gold_count": 17350
}
```

## 对比要点

| Metric | s43 no-evi | s44 no-evi | s44 with-evi |
|--------|-----------|-----------|-------------|
| **F1 / Ign-F1** | 0.3224 | **0.3264** | **0.3329** |
| Precision | 0.5017 | 0.5006 | **0.5133** |
| Recall | 0.2375 | 0.2422 | **0.2463** |
| **Evi-F1(TP)** | 0.2301 | 0.1511 | **0.5897** |
| **Evi-F1 Joint** | 0.0938 | 0.0627 | **0.2458** |
| **EDCR** | 0.7218 | 0.7907 | **0.8090** |
| Format OK | 99.8% | 99.2% | 99.6% |
| Evidence Format | 14.6% | 11.2% | **96.4%** |

s44 with-evidence 在所有指标上优于 no-evidence 变体：RE F1 高 0.65pp，evidence 指标大幅领先（Evi-F1 0.59 vs 0.15）。注意所有实验 Ign-F1 = F1（因缺少 train_annotated.json）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "f1": 0.3224,
    "precision": 0.5017,
    "recall": 0.2375,
    "ign_f1": 0.3224,
    "ign_precision": 0.5017,
    "ign_recall": 0.2375,
    "evi_f1": 0.2301,
    "evi_f1_joint": 0.0938,
    "edcr": 0.7218,
    "n_documents": 500,
    "n_truncated": 43,
    "format_ok_rate": 0.998,
    "field_compliance_rate": 0.146,
    "evidence_format_rate": 0.146,
    "n_predictions": 18972,
    "tp": 4120,
    "pred_count": 8212,
    "gold_count": 17350
  }
}
```

</details>

---
