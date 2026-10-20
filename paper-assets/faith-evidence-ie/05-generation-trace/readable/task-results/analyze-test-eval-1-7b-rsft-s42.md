# analyze test eval 1 7b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_1_7b_rsft_s42_20260521T173419_result.json`
- **Structured JSON:** [`2560d26f779f7a5e1e52.json`](../../sessions/25/2560d26f779f7a5e1e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "conclusion": "success",
  "metrics": {
    "ign_f1": 0.2933,
    "f1": 0.2933,
    "precision": 0.4625,
    "recall": 0.2148,
    "evi_f1_joint": 0.2320,
    "evi_f1_tp": 0.6196,
    "edcr": 0.8169,
    "truncated": "369/500",
    "format_ok": "500/500",
    "field_compliance": 0.202,
    "n_predictions": 26098,
    "n_docs": 500,
    "codalab_submission": true,
    "codalab_converted": 7793,
    "codalab_skipped_rel": 131,
    "codalab_skipped_entity": 750
  },
  "checkpoint_path": "/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42",
  "log_path": "~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s42.log",
  "notes": "1.7B RSFT test ign_f1=0.2933，显著低于 dev ign_f1=0.5119（dev→test 跌幅 42.7%）。也低于 14B test (0.3849) 和 LLaMA-8B test (0.3599)。注意 ign_f1=f1（test 无 train_annotated.json 做 ignore 过滤，符合预期）。369/500 截断率极高（73.8%），field_compliance 仅 20.2%（101/500 evidence 有效），recall 仅 0.2148，说明 1.7B 在 test 长文档上生成能力严重受限。CodaLab submission 已生成。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "conclusion": "success",
    "metrics": {
      "ign_f1": 0.2933,
      "f1": 0.2933,
      "precision": 0.4625,
      "recall": 0.2148,
      "evi_f1_joint": 0.232,
      "evi_f1_tp": 0.6196,
      "edcr": 0.8169,
      "truncated": "369/500",
      "format_ok": "500/500",
      "field_compliance": 0.202,
      "n_predictions": 26098,
      "n_docs": 500,
      "codalab_submission": true,
      "codalab_converted": 7793,
      "codalab_skipped_rel": 131,
      "codalab_skipped_entity": 750
    },
    "checkpoint_path": "/root/autodl-tmp/eval_results/test_eval_1_7b_rsft_s42",
    "log_path": "~/runs/faith-evidence-ie/test_eval_1_7b_rsft_s42.log",
    "notes": "1.7B RSFT test ign_f1=0.2933，显著低于 dev ign_f1=0.5119（dev→test 跌幅 42.7%）。也低于 14B test (0.3849) 和 LLaMA-8B test (0.3599)。注意 ign_f1=f1（test 无 train_annotated.json 做 ignore 过滤，符合预期）。369/500 截断率极高（73.8%），field_compliance 仅 20.2%（101/500 evidence 有效），recall 仅 0.2148，说明 1.7B 在 test 长文档上生成能力严重受限。CodaLab submission 已生成。"
  }
}
```

</details>

---
