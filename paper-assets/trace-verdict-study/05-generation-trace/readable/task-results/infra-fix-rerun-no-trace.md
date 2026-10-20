# infra fix rerun no trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-rerun-no-trace_20260514T185832_result.json`
- **Structured JSON:** [`d7a67195dd88c80cad11.json`](../../sessions/d7/d7a67195dd88c80cad11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### no_trace — 已完成，无需重跑

`no_trace_seed42_v3` 于 2026-05-15 02:22 成功完成（`EXIT_CODE=0`），21 分 8 秒跑完 444 steps / 3 epochs。

- `train_loss: 0.180`，`eval_loss: 0.645`，`eval_mean_token_accuracy: 0.890`
- Checkpoint 完整保存在 `/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/`（adapter_model.safetensors + tokenizer 全齐）
- 当前 `train_sft.py` 中无 `max_seq_length`，已用 `max_length=2048`，bug 在 v3 之前已修复

### full_trace 和 vota 当前进度

| 条件 | GPU | 进度 | 已跑 | 预计剩余 |
|------|-----|------|------|---------|
| full_trace | GPU 0 | 192/444 (43%) | ~58 min | ~72 min |
| vota | GPU 1 | 70/444 (16%) | ~19 min | ~104 min |

两个训练都在正常推进，vota 的 step 速度 ~16.7s/it 在 epoch 1 阶段，full_trace 类似。

---
