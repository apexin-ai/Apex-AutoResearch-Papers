# code plan012 qwen06b seed2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan012-qwen06b-seed2_20260515T234601_result.json`
- **Structured JSON:** [`e6dafdebc9cf27f5ae85.json`](../../sessions/e6/e6dafdebc9cf27f5ae85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

- **PID**: 257903，cuda:2
- **数据**: 18423 样本（4 generators），5-fold stratified CV
- **LoRA**: r=32, alpha=64, trainable 4.59M params (0.76%)
- **速度**: ~4.4 it/s，5529 steps/fold × 3 epochs × 5 folds
- **预估时间**: 每 fold ~21 min × 5 = ~105 min 总计

配置对比 cuda:0 变体：

| | cuda:0 (v1) | cuda:2 (v2) |
|---|---|---|
| seed | 42 | 123 |
| LoRA r | 16 | 32 |
| LoRA alpha | 32 | 64 |
| alpha/r | 2 | 2 |

实验已注册为 `plan-012-qwen06b-v2`，状态 RUNNING。日志在 `/tmp/plan012_qwen06b_v2.log`。

---
