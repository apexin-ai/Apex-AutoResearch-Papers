# ops pilot final results prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pilot-final-results-prep_20260513T114711_result.json`
- **Structured JSON:** [`f63a9d97286472bcad12.json`](../../sessions/f6/f63a9d97286472bcad12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已更新。变更摘要：

**pilot_results.json**:
- Qwen embedding_distance: status → `completed`，添加 `final_metrics.val_loss=0.5935`，移除 `current_step`
- StarCoder dataflow_aware: 添加 `best_metrics` (val_loss=0.5257, R@1=0.4756)，添加 `eval_history`，`best_step` 设为 500

**pilot_results_summary.md**:
- Qwen embedding 行: status → completed，notes 补充 final val_loss=0.5935
- StarCoder dataflow 行: 填入 eval@500 指标 (val_loss=0.5257, R@1=0.4756)
- Cross-model 对比表: 增加 Status 列，新增 StarCoder2 dataflow 行
- Observations: 新增 dataflow eval@500 低于 random baseline 的观察

---
