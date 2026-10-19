# ops starcoder pool50 eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_starcoder_pool50_eval_20260516T032527_result.json`
- **Structured JSON:** [`cd4c97b25c9375df2b88.json`](../../sessions/cd/cd4c97b25c9375df2b88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## StarCoder Pool=50 Eval

- **PID**: 138972
- **Checkpoints to eval**: 8 (auto-discovered `best_by_recall_at_1` + `best_by_val_loss` for 4 runs)
  - embedding_distance_s42, random_s42, random_s43, random_s44 (each × 2 selection criteria)
- **VRAM after start**: 68.5/97.9 GB (cuda:1, +15GB for eval, 29GB headroom for训练)
- **Val data**: `full_m2_starcoder_data/val_random_s42.jsonl` (2980 queries)
- **预估完成时间**: ~1.5-2h（8 checkpoints × ~12min each, 94 batches × ~4s/batch × 2 passes）
- **日志**: `/tmp/pool50_eval_starcoder.log`

注意：`--batch-mode` 发现了 8 个 checkpoint（含 `best_by_val_loss`），比预期的 4 个多。数据路径已修正为 StarCoder 专用 val 数据（非 Qwen 的 `full_m2_training_data`）。

---
