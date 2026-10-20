# ops check e2 lr decay

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_e2_lr_decay_20260518T134057_result.json`
- **Structured JSON:** [`ea8ae84796b2349f379d.json`](../../sessions/ea/ea8ae84796b2349f379d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
LR 状态: 无法判断（运行已崩溃）
当前 LR: 无数据
当前 step: 无训练步数据（W&B 内部 _step=563 但无 metrics 记录）
reward/mean 趋势: 无数据
运行状态: **failed**，仅运行 307 秒（~5 分钟）即崩溃
```

**关键发现**:

run `k5ex8kfs` (`grpo_standard_20_extended_300`) 状态为 **failed**，运行仅 307 秒后崩溃。learning_rate、reward/mean、loss 三个指标均无数据（未记录任何训练步），说明训练在开始实际 step 之前就失败了。

从 config 看：
- `lr_scheduler_type`: **linear**（不是 cosine）
- `learning_rate`: 1e-06
- `warmup_steps`: 0

**建议**: LR 衰减问题暂时无法评估，优先排查崩溃原因。需要检查服务器上的训练日志（`/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/` 或 stdout/stderr）确认失败原因。是否需要我去服务器查日志？

---
