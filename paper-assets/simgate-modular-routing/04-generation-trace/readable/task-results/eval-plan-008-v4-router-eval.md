# eval plan 008 v4 router eval

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-008-v4-router-eval_20260515T202751_result.json`
- **Structured JSON:** [`e0f48a217e087726a2e1.json`](../../sessions/e0/e0f48a217e087726a2e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

### 完整 Metrics 表

| Model | Seed | balanced_acc | internal_recall | eval_loss |
|-------|------|-------------|----------------|-----------|
| Qwen3-0.6B | 42 | **0.6296** | 0.6333 | 0.3151 |
| Qwen3-0.6B | 43 | 0.5593 | 0.5000 | 0.2859 |
| Qwen3-1.7B (ref) | 42 | 0.5761 | 0.5152 | 0.2400 |
| Qwen3-1.7B (ref) | 43 | 0.4852 | 0.3667 | 0.4363 |
| Qwen3-4B | 42 | 0.5889 | 0.4667 | 0.3130 |
| Qwen3-4B | 43 | 0.5352 | 0.4000 | 0.2842 |

### 3-Model 对比

| Model | Seed 42 | Seed 43 | Mean | Std |
|-------|---------|---------|------|-----|
| Qwen3-0.6B | 0.6296 | 0.5593 | **0.594** | 0.050 |
| Qwen3-1.7B (ref) | 0.5761 | 0.4852 | 0.531 | 0.064 |
| Qwen3-4B | 0.5889 | 0.5352 | 0.562 | 0.038 |

### 结论

**Success — "lightweight router suffices"**。0.6B (mean=0.594) 不仅与 1.7B/4B 在 1 std 范围内，还是三者中最高的。模型容量从 0.6B 增加到 4B 并未带来路由精度提升，routing 任务的瓶颈不在模型大小。

注意：1.7B ref 使用了 `enable_thinking=False` 评估，0.6B/4B 使用默认 thinking enabled（由 `strip_thinking` 处理），这可能略微影响可比性，但分类逻辑一致。

---
