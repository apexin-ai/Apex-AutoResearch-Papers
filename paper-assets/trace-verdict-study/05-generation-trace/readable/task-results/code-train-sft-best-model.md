# code train sft best model

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train_sft_best_model_20260515T132351_result.json`
- **Structured JSON:** [`3538524022c118751281.json`](../../sessions/35/3538524022c118751281.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码已经包含所有要求的参数，无需修改：

- `load_best_model_at_end=True` — 第 120 行
- `metric_for_best_model="eval_loss"` — 第 121 行
- `greater_is_better=False` — 第 122 行
- `eval_strategy="epoch"` — 第 115 行
- `save_strategy="epoch"` — 第 116 行
- `save_total_limit=3` — 第 119 行

训练结束后 `trainer.save_model(final_dir)` 会保存 best model（因为 `load_best_model_at_end=True` 使 Trainer 在训练结束时自动加载最佳 checkpoint），所以 evaluate.py 从 `{output_dir}/final` 加载时拿到的就是 best checkpoint。

---
