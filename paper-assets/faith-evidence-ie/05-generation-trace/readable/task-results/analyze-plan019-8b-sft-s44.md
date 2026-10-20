# analyze plan019 8b sft s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan019_8b_sft_s44_20260518T203015_result.json`
- **Structured JSON:** [`0d26caa5059047dbe974.json`](../../sessions/0d/0d26caa5059047dbe974.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
conclusion: success
train_loss: 0.5691
eval_loss: epoch1=0.6805 / epoch2=0.6861 / epoch3=0.7196
eval_mean_token_accuracy: epoch1=0.8399 / epoch2=0.8405 / epoch3=0.8379
training_runtime_s: 3823.9
epochs: 3
total_steps: 570
checkpoint_path: /root/autodl-tmp/sft_output_qwen3_8b_s44
trainable_params: 174,587,904 (2.09% of 8.37B)
checkpoints_saved: checkpoint-190, checkpoint-570, + final adapter

notes: 与 s42 对比:
  - train_loss: 0.5691 vs 0.5705 (略低，几乎一致)
  - eval_loss (epoch3): 0.7196 vs 0.7186 (几乎一致)
  - eval_mean_token_accuracy (epoch3): 0.8379 vs 0.8377 (几乎一致)
  - training_runtime: 3824s vs 3932s (快 ~108s)
  - 两个 seed 的指标高度一致，训练稳定可复现
  - eval_loss 从 epoch1→3 呈上升趋势 (0.6805→0.7196)，说明 epoch2 后开始轻微过拟合（与 s42 模式一致）
  - best eval_loss 在 epoch1 (0.6805)，但 token accuracy 在 epoch2 最高 (0.8405)
  - EXIT_CODE=0，final model + adapter 正常保存
```

---
