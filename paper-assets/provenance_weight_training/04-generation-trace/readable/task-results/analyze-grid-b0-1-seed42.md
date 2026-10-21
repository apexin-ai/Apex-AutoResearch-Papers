# analyze grid b0 1 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grid_b0_1_seed42_20260516T084409_result.json`
- **Structured JSON:** [`1ac689236ffba768fca0.json`](../../sessions/1a/1ac689236ffba768fca0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成，但**尚未运行 holdout 评估**。汇总已有信息：

```
eval_loss_holdout: 未评估（需运行 posthoc eval）
PPL: 未评估
train_loss_final: 8.417 (Trainer 聚合值 = 4 batch items × ~2.1 per-token weighted loss)
total_steps: 6103
wandb_run_id: none
checkpoint_path: /root/provenance_weight_training/output/models/grid_b0_1_seed42/final
  (中间 checkpoints: checkpoint-5500, checkpoint-6000, checkpoint-6103)
结论: 待定——需要对 final checkpoint 运行 posthoc eval
```

`posthoc_eval_seed42.json` 只覆盖了 b≥0.5 的实验（grid_b0_5 到 grid_b5_0），grid_b0_1 和 grid_b0_3 不在其中。

需要运行类似以下的 posthoc eval 来获取 PPL：
```bash
python eval_holdout.py --checkpoint output/models/grid_b0_1_seed42/final --data data/human/eval_holdout.jsonl --max_docs 5000
```

是否需要我现在触发 eval？

---
