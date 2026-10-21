# analysis eval step100 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_step100_results_20260514T193713_result.json`
- **Structured JSON:** [`635a26acf24472952686.json`](../../sessions/63/635a26acf24472952686.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 评估结果：`mvp2_eval_ced_kl001_r4_step100` (checkpoint-100)

### 核心指标

```json
{
  "f1": 0.2167,
  "ign_f1": 0.2167,
  "precision": 0.2849,
  "recall": 0.1749,
  "evi_f1": 0.5746,
  "evi_precision": 0.5244,
  "evi_recall": 0.6353,
  "edcr": 0.8539,
  "tp": 2125,
  "pred_count": 7460,
  "gold_count": 12151,
  "n_predictions": 11067,
  "n_parseable": 985,
  "n_documents": 985,
  "n_truncated": 21,
  "n_format_ok": 985,
  "format_ok_rate": 1.0,
  "format_compliance_rate": 1.0,
  "field_compliance_rate": 0.9787,
  "evidence_format_rate": 0.9787,
  "n_distractor_citations": 18390,
  "n_total_citations": 21536,
  "inference_time_seconds": 5139.9
}
```

### 日志末尾 20 行

```
2026-05-15 03:35:07,333 INFO Inference done. 21/985 truncated, 0 errors.
2026-05-15 03:35:07,334 INFO Inference: 5139.9s (5.22 s/doc)
2026-05-15 03:35:07,892 INFO Loaded 37785 training triples for Ign-F1
2026-05-15 03:35:08,002 INFO Metrics → /root/autodl-tmp/eval_results/grpo_ced_kl001_step100/checkpoint-100/metrics.json
2026-05-15 03:35:08,133 INFO Predictions → /root/autodl-tmp/eval_results/grpo_ced_kl001_step100/checkpoint-100/predictions.json

==================================================
  F1:          0.2167
  Ign-F1:      0.2167
  Evi-F1:      0.5746
  EDCR:        0.8539
  Format OK:   985/985 (100.0%)
  Truncated:   21/985
  Predictions: 11067
==================================================

Summary saved to /root/autodl-tmp/eval_results/grpo_ced_kl001_step100/summary.json
  Total: 1, Evaluated: 1, Skipped: 0, Failed: 0
  Best by F1: checkpoint-100 (step 100)
    F1=0.2167  Ign-F1=0.2167  Evi-F1=0.5746  EDCR=0.8539
EXIT_CODE=0
```

### 要点

- **F1 = 0.2167**，precision 0.2849 vs recall 0.1749，recall 明显偏低（gold 12151，仅命中 2125）
- **Evi-F1 = 0.5746**，evidence 质量尚可（recall 0.6353 > precision 0.5244）
- **EDCR = 0.8539**，distractor citation 比例高（18390/21536 = 85.4%）
- **格式完美**：985/985 全部可解析，field compliance 97.87%
- 21/985 文档截断（2.1%），0 错误
- 推理耗时 5139.9s（~85.7 min），5.22 s/doc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "f1": 0.2167,
    "ign_f1": 0.2167,
    "precision": 0.2849,
    "recall": 0.1749,
    "evi_f1": 0.5746,
    "evi_precision": 0.5244,
    "evi_recall": 0.6353,
    "edcr": 0.8539,
    "tp": 2125,
    "pred_count": 7460,
    "gold_count": 12151,
    "n_predictions": 11067,
    "n_parseable": 985,
    "n_documents": 985,
    "n_truncated": 21,
    "n_format_ok": 985,
    "format_ok_rate": 1.0,
    "format_compliance_rate": 1.0,
    "field_compliance_rate": 0.9787,
    "evidence_format_rate": 0.9787,
    "n_distractor_citations": 18390,
    "n_total_citations": 21536,
    "inference_time_seconds": 5139.9
  }
}
```

</details>

---
