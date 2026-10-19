# ops training eval checkpoint monitor

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-eval-checkpoint-monitor_20260515T184647_result.json`
- **Structured JSON:** [`06d263639d8c2918ac67.json`](../../sessions/06/06d263639d8c2918ac67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果

两个目标数据点 **均未出现**，训练仍在推进中：

### Qwen dataflow_s43
- **当前**: step ~680/2810 (epoch 1/2)
- **eval@500 已有** (回顾): val_loss=0.4617, **R@1=0.5495**, R@5=0.9728, R@10=1.0
- **eval@1000 ETA**: ~04:05 CST (约1.5h后)
- **诊断信号**: eval@500 R@1=0.5495 低于 random baseline (0.5554) 和 embed baseline (0.5606)，趋势待 eval@1000 确认

### StarCoder embed_s42
- **当前**: step ~300/4242 (epoch 1/3)
- **eval@500 ETA**: ~03:36 CST (约50min后)
- **对比基线**: random_s42 best R@1=0.4604

### 附带发现
StarCoder 链已完成 random_s43 和 random_s44：
- random_s43: best R@1=0.4912 (early stop @2500)
- random_s44: best R@1=0.4897 (early stop @1500)

---
