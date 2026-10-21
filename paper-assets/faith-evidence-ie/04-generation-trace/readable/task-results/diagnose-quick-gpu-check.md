# diagnose quick gpu check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_quick-gpu-check_20260521T004032_result.json`
- **Structured JSON:** [`e9c0162fe3440fea27ba.json`](../../sessions/e9/e9c0162fe3440fea27ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**命令 1 — 状态检查：**

```
=== PS ===
   PID STAT     ELAPSED COMMAND
 53413 Rl      03:49:09 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval --batch_size 1 --max_new_tokens 1024 --no-quantize --seed 42
 58417 Ss+     02:11:17 bash -c ... eval_llama_sft_s43_no_evidence_2048_r2 ...

=== GPU ===
0, 32503 MiB, 84 %
1, 18879 MiB, 91 %
2, 0 MiB, 0 %
3, 0 MiB, 0 %

=== 14B RSFT EVAL OUTPUTS ===
total 0 (空目录，仅 . 和 ..)

=== 14B RSFT NO-EVI OUTPUTS ===
(不存在)

=== LLAMA WITH-EVI 2048 ===
metrics.json (1572 bytes, May 21 08:16)
predictions.json (8373522 bytes, May 21 08:16)

=== S43 R2 LOG ===
timeout: failed to run command 'python': No such file or directory
(后跟大量 null bytes)
... 进度条最后: Inference: 54% | 134/247 [2:10:59<1:51:53, 59.42s/it]

=== TMUX SESSIONS ===
eval_llama_sft_s43_no_evidence_2048_r2: 1 windows (created Thu May 21 06:29:46 2026)
```

**命令 2 — 指标：**

```
=== plan017_14b_rsft_eval ===
NO_METRICS

=== plan017_14b_rsft_no_evidence_eval ===
NO_METRICS

=== eval_llama_sft_s42_with_evidence_2048 ===
{
  "precision": 0.5591,
  "recall": 0.5955,
  "f1": 0.5767,
  "ign_precision": 0.5373,
  "ign_recall": 0.5955,
  "ign_f1": 0.5649,
  "tp": 7236,
  "pred_count": 12942,
  "gold_count": 12151,
  "evi_precision": 0.7788,
  "evi_recall": 0.8288,
  "evi_f1": 0.8030,
  "n_evaluated": 19508,
  "edcr": 0.6428,
  "n_distractor_citations": 23472,
  "n_total_citations": 36513,
  "evi_joint_precision": 0.4042,
  "evi_joint_recall": 0.5102,
  "evi_f1_joint": 0.4510,
  "evi_tp": 9827,
  "evi_pred_total": 24313,
  "evi_gold_total": 19261,
  "format_compliance_rate": 0.9909,
  "field_compliance_rate": 0.8467,
  "evidence_format_rate": 0.8467,
  "n_total": 985,
  "n_parseable": 976,
  "n_field_complete": 834,
  "n_evidence_valid": 834,
  "n_documents": 985,
  "n_predictions": 20302,
  "n_truncated": 147,
  "n_format_ok": 976,
  "format_ok_rate": 0.9909,
  "inference_time_seconds": 10491.7,
  "config": {
    "model_path": "/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
    "base_model": "/root/autodl-tmp/models/Qwen3-4B",
    "sft_adapter": "/root/autodl-tmp/sft_output_llama_3_1_8b",
    "data_path": "/root/autodl-tmp/data/docred",
    "output_dir": "/root/autodl-tmp/eval_results/eval_llama_sft_s42_with_evidence_2048",
    "batch_size": 1,
    "max_new_tokens": 2048,
    "split": "dev",
    "seed": 42,
    "no_evidence": false,
    "quantize": false
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "precision": 0.5591,
    "recall": 0.5955,
    "f1": 0.5767,
    "ign_precision": 0.5373,
    "ign_recall": 0.5955,
    "ign_f1": 0.5649,
    "tp": 7236,
    "pred_count": 12942,
    "gold_count": 12151,
    "evi_precision": 0.7788,
    "evi_recall": 0.8288,
    "evi_f1": 0.803,
    "n_evaluated": 19508,
    "edcr": 0.6428,
    "n_distractor_citations": 23472,
    "n_total_citations": 36513,
    "evi_joint_precision": 0.4042,
    "evi_joint_recall": 0.5102,
    "evi_f1_joint": 0.451,
    "evi_tp": 9827,
    "evi_pred_total": 24313,
    "evi_gold_total": 19261,
    "format_compliance_rate": 0.9909,
    "field_compliance_rate": 0.8467,
    "evidence_format_rate": 0.8467,
    "n_total": 985,
    "n_parseable": 976,
    "n_field_complete": 834,
    "n_evidence_valid": 834,
    "n_documents": 985,
    "n_predictions": 20302,
    "n_truncated": 147,
    "n_format_ok": 976,
    "format_ok_rate": 0.9909,
    "inference_time_seconds": 10491.7,
    "config": {
      "model_path": "/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
      "base_model": "/root/autodl-tmp/models/Qwen3-4B",
      "sft_adapter": "/root/autodl-tmp/sft_output_llama_3_1_8b",
      "data_path": "/root/autodl-tmp/data/docred",
      "output_dir": "/root/autodl-tmp/eval_results/eval_llama_sft_s42_with_evidence_2048",
      "batch_size": 1,
      "max_new_tokens": 2048,
      "split": "dev",
      "seed": 42,
      "no_evidence": false,
      "quantize": false
    }
  }
}
```

</details>

---
