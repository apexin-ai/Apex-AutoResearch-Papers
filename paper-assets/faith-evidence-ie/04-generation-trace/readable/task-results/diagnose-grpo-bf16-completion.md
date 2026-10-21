# diagnose grpo bf16 completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_bf16_completion_20260518T192203_result.json`
- **Structured JSON:** [`55260232d60c916bb622.json`](../../sessions/55/55260232d60c916bb622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 诊断结果 ===
状态: 正常完成
完成 steps: 200/200
训练时长: 6h35m (23737s)
最终 checkpoint: /root/autodl-tmp/grpo_bf16_g4/checkpoint-200
cuda:2: 空闲 (0MiB)

=== Metrics (最终 step) ===
reward_mean: 1.7646
  - f1_reward:    1.2756
  - ced_reward:   0.2261
  - format_reward: 0.2629
train_loss: 0.0983
entropy: 0.1184
clipped_ratio: 0.10

=== Registry 操作 ===
conclusion: success ✓
metrics: 已写入 ✓
spec: checkpoint_path + log_path 已写入 ✓
cron: 已删除 ✓
```

注意：cuda:1 和 cuda:3 各有一个 python 进程占用 ~11.4GB，非本实验相关。

---
