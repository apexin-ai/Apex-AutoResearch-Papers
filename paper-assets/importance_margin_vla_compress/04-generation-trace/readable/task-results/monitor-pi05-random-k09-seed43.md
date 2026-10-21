# monitor pi05 random k09 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_pi05-random-k09-seed43_20260521T185940_result.json`
- **Structured JSON:** [`ac0c816ef8b1f6962777.json`](../../sessions/ac/ac0c816ef8b1f6962777.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**π0.5 random k=0.9 seed43 — 进度报告**

- **状态**: 运行中（PID 531274, 已运行 ~1h07m）
- **进度**: 270/500 episodes 完成（**54%**），正在执行 Task 5（20/50 eps）
- **每 task 平均耗时**: ~12 min
- **剩余**: T5 剩 30 eps + T6-T9 共 4 个 task ≈ **55 min**
- **预计完成时间**: ~03:55 服务器时间

**已完成 task 的 success rate**:

| Task | SR |
|------|----|
| T0 (alphabet soup) | 16% |
| T1 (cream cheese) | 16% |
| T2 (salad dressing) | 10% |
| T3 (bbq sauce) | 2% |
| T4 (ketchup) | 6% |
| T5 (tomato sauce) | 20% (进行中, 20 eps) |

当前累计 SR: 25/250 = **10.0%**（前 5 个 task）。数值偏低，random pruning 在 k=0.9 下表现显著差于 importance-based 方法。

---
