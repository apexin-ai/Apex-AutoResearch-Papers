# ops check eval c1s42 and c1s137

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-c1s42-and-c1s137_20260518T131610_result.json`
- **Structured JSON:** [`ff7d0473bfaa308ab0b2.json`](../../sessions/ff/ff7d0473bfaa308ab0b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. C1_s42 eval — 仍在运行

- PID 25961 存活，已运行 2h21m
- 进度：**82/91**（接近完成）
- 目前只有增量 `results_lora_only.jsonl`，summary 尚未生成
- 从日志看正确率偏低（可见范围内 68-82 只有 #71 CORRECT）

### 2. C1_s137 训练 — 已完成

| 项目 | 值 |
|---|---|
| Checkpoint | `/root/tbab_multi_turn/checkpoints/c1_lora_only_seed137` |
| 最终 step loss | 0.2471 |
| 平均 train_loss | 0.4423 |
| Epoch | 3.0 |
| 训练时长 | 8549s (~2h23m) |
| EXIT_CODE | 0 |

C1_s42 eval 剩 9 个 task，预计几分钟内完成。需要我稍后再查最终指标吗？

---
