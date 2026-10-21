# ops add 55k checkpoint monitor

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_add_55k_checkpoint_monitor_20260514T034533_result.json`
- **Structured JSON:** [`1d4765c38103947637bc.json`](../../sessions/1d/1d4765c38103947637bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新监控进程 PID=119586 已启动，首轮判定已完成。所有新增检查点数据已写入 checkpoint_results.jsonl。

## 汇总

### 新增判定结果

| 实验 | 检查点 | eval_return | 判定 | 备注 |
|------|--------|-------------|------|------|
| **008a** | 45K | 563.41 | **ON_TRACK** | 远超 006@45K(477) 和 001@45K(443) |
| **008a** | 55K | **487.92** | **HOLDING** | vs 006@55K=360.4，**未崩塌**，value_eval_ratio=0.3762 |
| 008c | 45K | 226.55 | BELOW | 低于阈值 400 |
| 008c | 55K | 241.87 | DECLINING | 低于 360 阈值 |

### 008a 关键结论

008a 的 eval_return 轨迹：35K(501) → 45K(563) → 55K(488)。从 45K 到 55K 有回落（-13%），但 **488 >> 360（006 崩塌值）**，确认 fixed dt=2 方案成功阻止了 006 的崩塌模式。评级 **B+**。

### 监控状态
- 旧进程 113940 已终止
- 新进程 119586 运行中，检查点增加到 35K/45K/55K/65K/105K
- 008d 尚在 32K，后续检查点将自动触发判定

---
