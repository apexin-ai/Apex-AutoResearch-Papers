# analyze d158 14b rsft s44 dev no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d158_14b_rsft_s44_dev_no_evi_20260525T155058_result.json`
- **Structured JSON:** [`c85c49cef51784a42bc3.json`](../../sessions/c8/c85c49cef51784a42bc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功完成（EXIT_CODE=0），无 W&B run，无异常。完整指标：

```json
{
  "run_id": "d158_14b_rsft_s44_dev_no_evi",
  "status": "completed",
  "no_evidence": true,

  "f1": 0.5890,
  "ign_f1": 0.5752,
  "precision": 0.5560,
  "recall": 0.6261,
  "ign_precision": 0.5331,
  "ign_recall": 0.6246,

  "evi_f1": 0.0,
  "evi_f1_joint": 0.0,
  "edcr": 0.0,

  "tp": 7608,
  "pred_count": 13683,
  "gold_count": 12151,

  "n_documents": 985,
  "n_predictions": 19915,
  "n_truncated": 87,
  "n_format_ok": 984,
  "format_ok_rate": 0.9990,
  "n_parseable": 984,
  "format_compliance_rate": 0.9990,
  "field_compliance_rate": 0.0,
  "evidence_format_rate": 0.0,

  "inference_time_seconds": 17675.2,
  "inference_speed": "17.94 s/doc",

  "config": {
    "model_path": "/root/autodl-tmp/rsft_output_14b_s44",
    "base_model": "Qwen3-14B",
    "sft_adapter": "/root/autodl-tmp/sft_output_14b_s44",
    "split": "dev",
    "seed": 44,
    "no_evidence": true,
    "max_new_tokens": 2048,
    "batch_size": 1
  }
}
```

关键对比：配对的 with-evidence eval (d158_14b_rsft_s44_eval) ign_f1=0.5655，**no-evidence 版本 ign_f1=0.5752，高出 +0.97pp**。evidence 相关指标均为 0，符合 no-evidence eval 预期。field_compliance_rate=0.0 也正常——no-evidence 输出不含 evidence 字段所以 field_complete 为 0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "run_id": "d158_14b_rsft_s44_dev_no_evi",
    "status": "completed",
    "no_evidence": true,
    "f1": 0.589,
    "ign_f1": 0.5752,
    "precision": 0.556,
    "recall": 0.6261,
    "ign_precision": 0.5331,
    "ign_recall": 0.6246,
    "evi_f1": 0.0,
    "evi_f1_joint": 0.0,
    "edcr": 0.0,
    "tp": 7608,
    "pred_count": 13683,
    "gold_count": 12151,
    "n_documents": 985,
    "n_predictions": 19915,
    "n_truncated": 87,
    "n_format_ok": 984,
    "format_ok_rate": 0.999,
    "n_parseable": 984,
    "format_compliance_rate": 0.999,
    "field_compliance_rate": 0.0,
    "evidence_format_rate": 0.0,
    "inference_time_seconds": 17675.2,
    "inference_speed": "17.94 s/doc",
    "config": {
      "model_path": "/root/autodl-tmp/rsft_output_14b_s44",
      "base_model": "Qwen3-14B",
      "sft_adapter": "/root/autodl-tmp/sft_output_14b_s44",
      "split": "dev",
      "seed": 44,
      "no_evidence": true,
      "max_new_tokens": 2048,
      "batch_size": 1
    }
  }
}
```

</details>

---
