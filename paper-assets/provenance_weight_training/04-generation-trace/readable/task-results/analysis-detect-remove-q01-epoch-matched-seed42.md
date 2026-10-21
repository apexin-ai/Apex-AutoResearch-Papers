# analysis detect remove q01 epoch matched seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_q01_epoch_matched_seed42_20260519T002540_result.json`
- **Structured JSON:** [`1df8ffb9db9cd203b5fb.json`](../../sessions/1d/1df8ffb9db9cd203b5fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```
eval_loss_holdout: N/A (未执行 eval)
eval_ppl_holdout: N/A
eval_loss: N/A
eval_perplexity: N/A
train_loss: 11.8483
checkpoint_path: /root/autodl-tmp/output/models/detect_remove_q01_epoch_matched_seed42/final
log_path: ~/runs/provenance_weight_training/detect_remove_q01_epoch_matched_seed42.log
training_completed: yes
total_steps: 919 (max_steps=919, epoch=0.26)
```

**关键发现：该实验没有运行任何 evaluation。** trainer_state.json 中 `best_metric: null`，log_history 里只有 weighting metrics，没有任何 `eval_*` 条目。`eval_steps=500` 已设置但 `should_evaluate=false`，说明训练脚本没有传入 eval dataset。

另外注意：`train_loss=11.8483` 异常偏高（Qwen3-0.6B 正常 loss 应在 2-3 左右）。这个值可能是 HuggingFace Trainer 对所有 step loss 的累积平均（包含初始高 loss steps），而从 step_metrics 看单步 loss 在 2-3 范围内是正常的。

---
