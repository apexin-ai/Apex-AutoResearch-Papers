# ops starcoder pool50 eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_starcoder_pool50_eval_20260516T050926_result.json`
- **Structured JSON:** [`c71964e3236e2a146f59.json`](../../sessions/c7/c71964e3236e2a146f59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

batch-mode 发现了 8 个 checkpoints（4 个 best_by_recall_at_1 + 4 个 best_by_val_loss），正在 encoding 第一个 checkpoint（embedding_distance_s42/best_by_recall_at_1）的 queries，进度 95%。

## StarCoder Pool=50 Eval
- **PID**: 142966
- **Checkpoints**: 8 个（4x best_by_recall_at_1 + 4x best_by_val_loss）
  - embedding_distance_s42, random_s42, random_s43, random_s44（各 2 个 best checkpoint）
- **Base model**: `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`（从 training_config.json 自动读取）
- **GPU**: cuda:1 via CUDA_VISIBLE_DEVICES=1
- **VRAM after launch**: 86.6/97.9 GB（GPU 1），50.8/97.9 GB（GPU 0）
- **Status**: running（正在 encode 第 1 个 checkpoint 的 queries）
- **Log**: `/tmp/pool50_eval_starcoder.log`
- **Output**: `/root/autodl-tmp/structfuse/results/pool50_eval_starcoder_all.json`

---
