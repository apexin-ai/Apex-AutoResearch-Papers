# analyze d158 14b rsft s44 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d158_14b_rsft_s44_eval_20260525T150520_result.json`
- **Structured JSON:** [`95f729109982816d52f3.json`](../../sessions/95/95f729109982816d52f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No W&B run ID in the log. Results:

```json
{
  "ign_f1": 0.5655,
  "f1": 0.5794,
  "precision": 0.5496,
  "recall": 0.6125,
  "ign_precision": 0.5259,
  "ign_recall": 0.6116,
  "evi_f1_tp": 0.8355,
  "evi_f1_joint": 0.4718,
  "edcr": 0.5955,
  "format_ok_rate": 1.0,
  "n_truncated": 95,
  "n_documents": 985,
  "n_predictions": 18151,
  "inference_time_seconds": 21564.6,
  "wandb_run_id": null,
  "checkpoint_path": "/root/autodl-tmp/rsft_output_14b_s44",
  "log_path": "~/runs/faith-evidence-ie/d158_14b_rsft_s44_eval.log"
}
```

**3-seed summary (14B RSFT k=1, dev, with-evidence):**

| seed | ign_f1 |
|------|--------|
| s42 | 0.5886 |
| s43 | 0.5815 |
| s44 | 0.5655 |
| **mean±std** | **0.5785 ± 0.0095** |

s44 比前两个 seed 低约 1.3-2.3 points，拉低了均值。无错误，format 100%，运行正常（~6h 推理）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "ign_f1": 0.5655,
    "f1": 0.5794,
    "precision": 0.5496,
    "recall": 0.6125,
    "ign_precision": 0.5259,
    "ign_recall": 0.6116,
    "evi_f1_tp": 0.8355,
    "evi_f1_joint": 0.4718,
    "edcr": 0.5955,
    "format_ok_rate": 1.0,
    "n_truncated": 95,
    "n_documents": 985,
    "n_predictions": 18151,
    "inference_time_seconds": 21564.6,
    "wandb_run_id": null,
    "checkpoint_path": "/root/autodl-tmp/rsft_output_14b_s44",
    "log_path": "~/runs/faith-evidence-ie/d158_14b_rsft_s44_eval.log"
  }
}
```

</details>

---
