# analyze plan019 1 7b rsft s44 r2 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan019_1_7b_rsft_s44_r2_eval_20260519T111056_result.json`
- **Structured JSON:** [`c3372547261e654e65cd.json`](../../sessions/c3/c3372547261e654e65cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```json
{
  "eval_name": "plan019_1_7b_rsft_s44_r2_eval",
  "conclusion": "success",
  "data_source": "/root/autodl-tmp/eval_results/rsft_1_7b_s44_r2_eval/metrics.json",
  "checkpoint_path": "/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44",
  "log_path": "/root/autodl-tmp/eval_results/rsft_1_7b_s44_r2_eval/predictions.json",

  "ign_f1": 0.5125,
  "ign_precision": 0.5173,
  "ign_recall": 0.5078,
  "f1": 0.5294,
  "precision": 0.5434,
  "recall": 0.5162,
  "evi_precision": 0.8150,
  "evi_recall": 0.8387,
  "evi_f1": 0.8267,
  "edcr": 0.6181,
  "evi_joint_precision": 0.4284,
  "evi_joint_recall": 0.4294,
  "evi_f1_joint": 0.4289,
  "format_compliance_rate": 0.9990,
  "field_compliance_rate": 0.7543,
  "n_truncated": 240,
  "inference_time_seconds": 8615.6
}
```

**与基准对比：**

| 指标 | s42 RSFT | s43 RSFT | **s44 RSFT** |
|------|----------|----------|-------------|
| ign_f1 | 0.5122 | 0.5109 | **0.5125** |
| ign_precision | — | 0.5186 | 0.5173 |
| ign_recall | — | 0.5035 | 0.5078 |
| f1 | — | 0.5271 | 0.5294 |
| evi_f1 | — | 0.8278 | 0.8267 |
| edcr | — | 0.6245 | 0.6181 |

**Conclusion: success.** ign_f1=0.5125，与 s42 (0.5122) 和 s43 (0.5109) 高度一致，三个 seed 的 RSFT 表现稳定在 0.51 附近。各项子指标也基本对齐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_name": "plan019_1_7b_rsft_s44_r2_eval",
    "conclusion": "success",
    "data_source": "/root/autodl-tmp/eval_results/rsft_1_7b_s44_r2_eval/metrics.json",
    "checkpoint_path": "/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44",
    "log_path": "/root/autodl-tmp/eval_results/rsft_1_7b_s44_r2_eval/predictions.json",
    "ign_f1": 0.5125,
    "ign_precision": 0.5173,
    "ign_recall": 0.5078,
    "f1": 0.5294,
    "precision": 0.5434,
    "recall": 0.5162,
    "evi_precision": 0.815,
    "evi_recall": 0.8387,
    "evi_f1": 0.8267,
    "edcr": 0.6181,
    "evi_joint_precision": 0.4284,
    "evi_joint_recall": 0.4294,
    "evi_f1_joint": 0.4289,
    "format_compliance_rate": 0.999,
    "field_compliance_rate": 0.7543,
    "n_truncated": 240,
    "inference_time_seconds": 8615.6
  }
}
```

</details>

---
