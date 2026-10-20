# ops add 008e to monitor

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_add_008e_to_monitor_20260514T041129_result.json`
- **Structured JSON:** [`dc3f904a49fb577d63f4.json`](../../sessions/dc/dc3f904a49fb577d63f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Monitor 已成功启动（PID 123053）：

- **跟踪实验**: 008a, 008d, 008e（已移除 008c）
- **检查点**: 35K/45K/55K/65K/105K
- **已判定**: 008a 的 35K-65K、008c 的 35K-65K、008d 的 35K 已有历史结果
- **008e 额外监控**: 每个检查点会计算 `value_mean/eval_return` 比率，>40% 输出 WARN，>50% 输出 ALERT

---
