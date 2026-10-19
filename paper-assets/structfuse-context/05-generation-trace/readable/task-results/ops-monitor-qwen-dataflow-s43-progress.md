# ops monitor qwen dataflow s43 progress

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-qwen-dataflow-s43-progress_20260515T181558_result.json`
- **Structured JSON:** [`d411abd1ecdfcdea931e.json`](../../sessions/d4/d411abd1ecdfcdea931e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**dataflow_s43 状态报告：**

- **当前 step**: 550 / 2810 (epoch 1)
- **训练速度**: ~229 steps/h（与预期 228 一致）
- **唯一 eval 数据点**: eval@500 — val_loss=0.4617, R@1=0.5495, R@5=0.9728, R@10=1.0

**R@1 对比（@step 500）：**

| 策略 | R@1 @500 | Best R@1 |
|------|----------|----------|
| random_s43 | — | 0.5554 (step 1500) |
| embed_s43 | — | 0.5606 (step 1500) |
| **dataflow_s43** | **0.5495** | 进行中 |

dataflow_s43 @500 的 R@1=0.5495 略低于 random/embed 的最终 best，但这是第一个 eval 点，后续可能提升。

**ETA：**
- eval@1000: ~2h 后（约 step 1000 时触发）
- 训练完成（2810 steps）: ~9.9h 后

**无 early stopping 迹象** — 目前只有 1 个 eval 点，patience=2 尚不可能触发。

无新 eval 数据需要更新 registry，当前 metrics 与上次检查一致。

---
