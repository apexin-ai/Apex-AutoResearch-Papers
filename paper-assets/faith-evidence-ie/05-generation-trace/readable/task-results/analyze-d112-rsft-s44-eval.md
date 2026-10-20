# analyze d112 rsft s44 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d112_rsft_s44_eval_20260519T111108_result.json`
- **Structured JSON:** [`fa7fbf99f5dbcd3936d8.json`](../../sessions/fa/fa7fbf99f5dbcd3936d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是完整分析：

## D112 RSFT from SFT s44 Eval Results

```json
{
  "experiment_id": "d112_rsft_s44_eval",
  "model": "Qwen3-4B",
  "metrics": {
    "ign_f1": 0.2181,
    "ign_precision": 0.3523,
    "ign_recall": 0.1579,
    "f1": 0.2410,
    "precision": 0.3948,
    "recall": 0.1735,
    "evi_precision": 0.8204,
    "evi_recall": 0.7173,
    "evi_f1": 0.7654,
    "edcr": 0.7762,
    "evi_joint_precision": 0.3028,
    "evi_joint_recall": 0.1266,
    "evi_f1_joint": 0.1785,
    "format_compliance_rate": 0.8589,
    "field_compliance_rate": 0.1310,
    "n_truncated": 839,
    "n_total_documents": 985,
    "inference_time_seconds": 12108.3
  },
  "config": {
    "model_path": "/root/autodl-tmp/rsft_output_4b_sft_s44",
    "base_model": "/root/autodl-tmp/models/Qwen3-4B",
    "sft_adapter": "/root/autodl-tmp/sft_output_seed44",
    "max_new_tokens": 1024,
    "batch_size": 4,
    "split": "dev",
    "no_evidence": false
  },
  "checkpoint_path": "/root/autodl-tmp/rsft_output_4b_sft_s44",
  "log_path": "/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/metrics.json",
  "data_source": "metrics.json from server rtx5090-4x"
}
```

## Conclusion: **INVALID — 结果不可用**

**核心问题：极端截断导致指标无意义。**

| 模型 | n_truncated | truncation_rate | field_compliance | ign_f1 |
|---|---|---|---|---|
| SFT s44 baseline | 249/985 | 25.3% | 74.6% | 0.4734 |
| Canonical RSFT (from s42 SFT) | 214/985 | 21.7% | 77.6% | 0.4423 |
| **D112 RSFT (from s44 SFT)** | **839/985** | **85.2%** | **13.1%** | **0.2181** |

839/985 文档被截断（85.2%），field_compliance 仅 13.1%（同配置下其他模型 ~75-80%）。ign_f1=0.2181 纯粹是截断造成的 recall 崩塌（0.1579），不反映模型真实能力。

**ign_f1=0.2181 不能与任何 baseline 比较。conclusion = INVALID。**

RSFT 在 s44 SFT base 上训练后，模型输出变得异常冗长，max_new_tokens=1024 严重不足。需要用更大的 max_new_tokens（如 1536 或 2048）重新评估，或调查模型为何在 RSFT 后变得如此冗长。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment_id": "d112_rsft_s44_eval",
    "model": "Qwen3-4B",
    "metrics": {
      "ign_f1": 0.2181,
      "ign_precision": 0.3523,
      "ign_recall": 0.1579,
      "f1": 0.241,
      "precision": 0.3948,
      "recall": 0.1735,
      "evi_precision": 0.8204,
      "evi_recall": 0.7173,
      "evi_f1": 0.7654,
      "edcr": 0.7762,
      "evi_joint_precision": 0.3028,
      "evi_joint_recall": 0.1266,
      "evi_f1_joint": 0.1785,
      "format_compliance_rate": 0.8589,
      "field_compliance_rate": 0.131,
      "n_truncated": 839,
      "n_total_documents": 985,
      "inference_time_seconds": 12108.3
    },
    "config": {
      "model_path": "/root/autodl-tmp/rsft_output_4b_sft_s44",
      "base_model": "/root/autodl-tmp/models/Qwen3-4B",
      "sft_adapter": "/root/autodl-tmp/sft_output_seed44",
      "max_new_tokens": 1024,
      "batch_size": 4,
      "split": "dev",
      "no_evidence": false
    },
    "checkpoint_path": "/root/autodl-tmp/rsft_output_4b_sft_s44",
    "log_path": "/root/autodl-tmp/eval_results/d112_rsft_from_sft_s44/metrics.json",
    "data_source": "metrics.json from server rtx5090-4x"
  }
}
```

</details>

---
