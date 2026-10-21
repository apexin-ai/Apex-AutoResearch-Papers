# analysis plan 016 llama sft eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_016_llama_sft_eval_20260516T141254_result.json`
- **Structured JSON:** [`1d8797888c1a2fbabf49.json`](../../sessions/1d/1d8797888c1a2fbabf49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "experiment": "plan_016_llama_3_1_8b_sft_eval",
  "model": "Meta-Llama-3.1-8B + SFT adapter",
  "mode": "with-evidence",
  "split": "dev",

  "core_metrics": {
    "f1": 0.5514,
    "ign_f1": 0.5384,
    "evi_f1": 0.8151,
    "evi_f1_joint": 0.4317,
    "edcr": 0.6280
  },

  "precision_recall": {
    "precision": 0.5464,
    "recall": 0.5565,
    "ign_precision": 0.5239,
    "ign_recall": 0.5537,
    "evi_precision": 0.7799,
    "evi_recall": 0.8537
  },

  "format_quality": {
    "format_compliance_rate": 0.9949,
    "field_compliance_rate": 0.7980,
    "evidence_format_rate": 0.7980,
    "n_parseable": 980,
    "n_field_complete": 786,
    "n_format_ok": 980
  },

  "volume": {
    "n_documents": 985,
    "n_total": 985,
    "n_predictions": 15325,
    "n_truncated": 197,
    "truncation_rate": "20.0%"
  },

  "performance": {
    "inference_time_seconds": 7331.3,
    "seconds_per_doc": 7.44,
    "batch_size": 4,
    "max_new_tokens": 1024
  },

  "comparison_vs_no_evidence": {
    "no_evidence_ign_f1": 0.5452,
    "with_evidence_ign_f1": 0.5384,
    "no_evidence_rel_f1": 0.5624,
    "with_evidence_rel_f1": 0.5514,
    "evidence_tax_ign_f1": 0.0068,
    "evidence_tax_rel_f1": 0.0110
  },

  "config": {
    "model_path": "/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
    "sft_adapter": "/root/autodl-tmp/sft_output_llama_3_1_8b",
    "no_evidence": false,
    "quantize": false,
    "seed": 42
  }
}
```

**关键发现：**

- **Evidence tax 很小**：rel_f1 仅下降 1.1%（0.5624→0.5514），ign_f1 下降 0.68%（0.5452→0.5384）。模型在输出 evidence 的同时几乎没有牺牲关系抽取性能。
- **Evidence 质量高**：evi_f1=0.8151，证据召回 85.4%。
- **截断问题显著**：197/985 (20%) 被截断，field_compliance 仅 79.8%（受截断影响，很多样本 evidence 字段不完整）。提高 max_new_tokens 可能进一步改善 evi_f1 和 field_compliance。
- **EDCR=0.628**：约 63% 的 citation 是 distractor，说明模型还在引用大量无关证据句。
- **无 W&B run ID**（日志中未出现）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "plan_016_llama_3_1_8b_sft_eval",
    "model": "Meta-Llama-3.1-8B + SFT adapter",
    "mode": "with-evidence",
    "split": "dev",
    "core_metrics": {
      "f1": 0.5514,
      "ign_f1": 0.5384,
      "evi_f1": 0.8151,
      "evi_f1_joint": 0.4317,
      "edcr": 0.628
    },
    "precision_recall": {
      "precision": 0.5464,
      "recall": 0.5565,
      "ign_precision": 0.5239,
      "ign_recall": 0.5537,
      "evi_precision": 0.7799,
      "evi_recall": 0.8537
    },
    "format_quality": {
      "format_compliance_rate": 0.9949,
      "field_compliance_rate": 0.798,
      "evidence_format_rate": 0.798,
      "n_parseable": 980,
      "n_field_complete": 786,
      "n_format_ok": 980
    },
    "volume": {
      "n_documents": 985,
      "n_total": 985,
      "n_predictions": 15325,
      "n_truncated": 197,
      "truncation_rate": "20.0%"
    },
    "performance": {
      "inference_time_seconds": 7331.3,
      "seconds_per_doc": 7.44,
      "batch_size": 4,
      "max_new_tokens": 1024
    },
    "comparison_vs_no_evidence": {
      "no_evidence_ign_f1": 0.5452,
      "with_evidence_ign_f1": 0.5384,
      "no_evidence_rel_f1": 0.5624,
      "with_evidence_rel_f1": 0.5514,
      "evidence_tax_ign_f1": 0.0068,
      "evidence_tax_rel_f1": 0.011
    },
    "config": {
      "model_path": "/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
      "sft_adapter": "/root/autodl-tmp/sft_output_llama_3_1_8b",
      "no_evidence": false,
      "quantize": false,
      "seed": 42
    }
  }
}
```

</details>

---
