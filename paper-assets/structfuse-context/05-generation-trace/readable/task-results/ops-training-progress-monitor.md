# ops training progress monitor

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-monitor_20260513T103619_result.json`
- **Structured JSON:** [`ce6b19cd839d84b62e33.json`](../../sessions/ce/ce6b19cd839d84b62e33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

| 实验 | 当前阶段 | step | 最佳指标 | 状态 |
|------|----------|------|----------|------|
| **m2_embed_verify** | embedding_distance (2/3) | 1300/~1600 | val_loss=0.4603, R@1=**0.5557** (step 500) | eval@1000 未改善 (1/3)，接近尾声 |
| **plan_013_starcoder** | dataflow (3/3) | 500 | embedding best: val_loss=0.4816, R@1=0.5078 | eval@500 即将触发 |

关键观察：
- m2_embed_verify 的 embedding_distance 策略 best R@1=0.5557，优于 random 的 0.5122，支持 "结构化负例更优" 的假设
- starcoder 的 embedding 策略 best R@1=0.5078，低于 Qwen 的 0.5557，编码器差异明显
- 两个实验都还有 ~1-2 小时完成剩余策略

---
