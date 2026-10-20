# ops check progress final batch

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-progress-final-batch_20260527T162952_result.json`
- **Structured JSON:** [`a42d32577f5cc1b12b10.json`](../../sessions/a4/a42d32577f5cc1b12b10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均在运行，预计 25-40 分钟内完成。

**核心结论：**

| | Walker 008f s0 | Cheetah 008a s0 |
|---|---|---|
| 当前 step | 80K / 105K | 88K / 105K |
| Peak eval | 233.8 @ 45K | **483.0 @ 85K ↑** |
| vs baseline | 25.5% of 916 ❌ | **108.8% of 444 ✓** |
| vs 同配置 s1 | 远低于 503 | 远超 281 (+72%) |
| Gate | 锁死 dt=2 | 锁死 dt=2 |

**严重问题：两个实验 gate 全程锁死 dt=2，empirical entropy=0。自适应 horizon 机制完全未工作，实验本质上是固定 dt=2 的 baseline。**

Cheetah s0 虽然 eval 数字好看（超 baseline），但这是在 gate 失效条件下取得的，不能归因于自适应机制。Walker s0 表现平庸，45K 后性能退化明显。

报告已保存至 `art_20260527_987f09`。

---
