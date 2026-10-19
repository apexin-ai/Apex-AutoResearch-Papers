# ops training progress check 0516b

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check-0516b_20260515T180456_result.json`
- **Structured JSON:** [`f3dc39336270a4c1085f.json`](../../sessions/f3/f3dc39336270a4c1085f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## Qwen dataflow_s43 (cuda:0)
- **PID 337267 (chain) / 18427 (training)**: 均存活
- **进度**: step 500+/2810 (epoch 1/2), ~228 steps/h
- **eval@500**: val_loss=0.4617, R@1=**0.5495**, R@5=0.9728, R@10=1.0
- **early stopping**: 尚未触发（仅 1 次 eval）
- **ETA 本轮**: ~May 16 12:00 CST（如不 early stop）
- **剩余**: dataflow_s44 + bm25_s42 → 全部完成 ~May 17 14:00-18:00

## StarCoder embedding_distance_s42 (cuda:1)
- **PID 38016**: 存活，运行 50min
- **进度**: step 150/4242 (epoch 1/3, 3 epochs 不 early stop), ~220 steps/h
- **无 eval**: 首次 eval 在 step 500（~1.5h 后）
- **ETA 本轮**: ~May 16 20:30 CST
- **剩余 5 轮**: 全部完成 ~May 19-20

## Watchers
- PID 966920 (Qwen s42 watcher): 存活 1d 2h 31m
- PID 20226 (StarCoder BM25 watcher): 存活 2h 6m

⚠️ **重复风险仍在**: StarCoder 主链包含 embed_s42 + dataflow_s42，watcher 20226 也有这两个 run，需确认 supplement 已裁剪为仅 BM25。

---
