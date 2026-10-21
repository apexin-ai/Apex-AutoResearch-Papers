# diagnose exp b1 scd fewnerd curriculum q

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612_result.json`
- **Structured JSON:** [`733c6910238e81b715e6.json`](../../sessions/73/733c6910238e81b715e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results obtained. Now let me also check the log for the final output confirmation.

```json
{
  "checkpoint_verified": true,
  "checkpoint_details": {
    "path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-fallback-lora/",
    "base_model": "qwen3-8b-fewnerd-exp021-merged",
    "peft_type": "LORA",
    "lora_rank": 32,
    "lora_alpha": 64,
    "train_loss": 0.023,
    "eval_loss": 0.033,
    "epochs": 2,
    "adapter_size_mb": 349
  },
  "other_scd_experiments_status": {
    "exp_b1_scd_fewnerd_standard": "COMPLETED (train_loss=0.023, eval_loss=0.0329)",
    "exp_b1_scd_threshold_ablation": "RUNNING (~92% at last check, GPU 3)"
  },
  "eval_results": {
    "pre_scd_greedy_f1": 0.7482,
    "post_scd_greedy_f1": 0.7866,
    "delta_pp": 3.84,
    "n_instances": 37648,
    "post_scd_greedy_precision": 0.7663,
    "post_scd_greedy_recall": 0.8080,
    "post_scd_instance_avg_f1": 0.7809,
    "total_tp": 78252,
    "total_fp": 23869,
    "total_fn": 18590
  },
  "available_gpus": ["cuda:1", "cuda:2"]
}
```

**SCD distillation 效果显著**：FewNERD greedy F1 从 0.7482 提升到 **0.7866**，绝对提升 **+3.84pp**。这个涨幅与 CoNLL 上观察到的趋势一致（CoNLL: 0.9078→0.9184, +1.06pp），且 FewNERD 涨幅更大，说明 SCD 在更复杂的 8 类实体任务上收益更高。

Post-SCD greedy F1 (0.7866) 已超越 pre-SCD consensus_theta2n (0.7637)，意味着蒸馏后的单次 greedy 推理已经优于蒸馏前 8 次采样 + theta2n 构建的结果，验证了 SCD 的核心 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "checkpoint_verified": true,
    "checkpoint_details": {
      "path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-fallback-lora/",
      "base_model": "qwen3-8b-fewnerd-exp021-merged",
      "peft_type": "LORA",
      "lora_rank": 32,
      "lora_alpha": 64,
      "train_loss": 0.023,
      "eval_loss": 0.033,
      "epochs": 2,
      "adapter_size_mb": 349
    },
    "other_scd_experiments_status": {
      "exp_b1_scd_fewnerd_standard": "COMPLETED (train_loss=0.023, eval_loss=0.0329)",
      "exp_b1_scd_threshold_ablation": "RUNNING (~92% at last check, GPU 3)"
    },
    "eval_results": {
      "pre_scd_greedy_f1": 0.7482,
      "post_scd_greedy_f1": 0.7866,
      "delta_pp": 3.84,
      "n_instances": 37648,
      "post_scd_greedy_precision": 0.7663,
      "post_scd_greedy_recall": 0.808,
      "post_scd_instance_avg_f1": 0.7809,
      "total_tp": 78252,
      "total_fp": 23869,
      "total_fn": 18590
    },
    "available_gpus": [
      "cuda:1",
      "cuda:2"
    ]
  }
}
```

</details>

---
