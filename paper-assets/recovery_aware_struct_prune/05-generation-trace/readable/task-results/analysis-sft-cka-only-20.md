# analysis sft cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_cka_only_20_20260517T142633_result.json`
- **Structured JSON:** [`78601770f61990b15671.json`](../../sessions/78/78601770f61990b15671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "success": true,
  "metrics": {
    "train_loss_initial": 1.958,
    "train_loss_final": 0.6165,
    "train_loss_average": 0.7486,
    "token_accuracy_final": 0.8362,
    "greedy_accuracy_100": null,
    "greedy_correct": null,
    "greedy_total": null,
    "eos_rate_greedy": null,
    "greedy_avg_len": null,
    "greedy_min_len": null,
    "greedy_max_len": null,
    "total_steps": 1870,
    "train_time_min": 33.4,
    "wandb_run_id": null,
    "checkpoint_saved": true,
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/"
  },
  "analysis": "训练正常完成但未运行 greedy/sampling evaluation。初始 loss 1.958 高于 RASP (1.86) 和 Standard (1.70)，说明 CKA-only 剪枝对模型的初始损伤最大。最终 loss 0.62 略优于两个基线 (0.64)，token accuracy 0.836 与基线相当。需要补跑 greedy evaluation 才能对比准确率。"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "success": true,
    "metrics": {
      "train_loss_initial": 1.958,
      "train_loss_final": 0.6165,
      "train_loss_average": 0.7486,
      "token_accuracy_final": 0.8362,
      "greedy_accuracy_100": null,
      "greedy_correct": null,
      "greedy_total": null,
      "eos_rate_greedy": null,
      "greedy_avg_len": null,
      "greedy_min_len": null,
      "greedy_max_len": null,
      "total_steps": 1870,
      "train_time_min": 33.4,
      "wandb_run_id": null,
      "checkpoint_saved": true,
      "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/"
    },
    "analysis": "训练正常完成但未运行 greedy/sampling evaluation。初始 loss 1.958 高于 RASP (1.86) 和 Standard (1.70)，说明 CKA-only 剪枝对模型的初始损伤最大。最终 loss 0.62 略优于两个基线 (0.64)，token accuracy 0.836 与基线相当。需要补跑 greedy evaluation 才能对比准确率。"
  }
}
```

</details>

---
