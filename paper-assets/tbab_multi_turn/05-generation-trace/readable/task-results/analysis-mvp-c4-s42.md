# analysis mvp c4 s42

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_c4_s42_20260518T150021_result.json`
- **Structured JSON:** [`6526a4fc3bac5f21d47b.json`](../../sessions/65/6526a4fc3bac5f21d47b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results summary:

## mvp_c4_s42 训练结果

| Metric | C4 s42 (Full TBAB) | C1 s42 (Baseline) | C1 s137 (Baseline) |
|---|---|---|---|
| final_train_loss | **0.308** | 0.2437 | 0.2471 |
| avg_train_loss | **0.5461** | 0.4426 | 0.4423 |

**其他指标：**
- train_runtime: 6040s (~1h 40min), 471 steps, 3 epochs
- throughput: 1.242 samples/s, 0.078 steps/s
- trainable params: 83.9M (1.15%)
- bridge tokens: [32000, 32001, 32002, 32003]

**Checkpoint：** `/root/tbab_multi_turn/checkpoints/c4_full_tbab_seed42`

**对比分析：** C4 的 train loss 显著高于 C1（final +26%, avg +23%）。这符合预期：C4 使用 bridge tokens + position reset，任务复杂度更高，模型需要同时学习 bridge token 语义和适应 position reset 改变的注意力模式。train loss 的绝对值差异不能直接判断方法有效性，需要后续 eval 在 lost_in_conversation 等 benchmark 上比较。

---
