# ssh check 29046 progress and prescp

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-29046-progress-and-prescp_20260522T100001_result.json`
- **Structured JSON:** [`5fed1ab47cd449a9f403.json`](../../sessions/5f/5fed1ab47cd449a9f403.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SCP 完成，验证通过。汇总：

---

### exp-003-s2 (R3-only seed2)
- **当前 step**: 7231 / 8000 (90.4%)
- **速度**: ~25.6 s/step
- **剩余**: 769 steps × 25.6s = ~5h 28m
- **ETA**: 2026-05-22 ~23:30 (服务器时间)

### exp-004-s2 (ACT baseline seed2)
- **当前 step**: 2230 / 8000 (27.9%)
- **速度**: ~8.9 s/step (log 每 10 steps 一条，间隔 ~89s)
- **剩余**: 5770 steps × 8.9s = ~14h 16m
- **ETA**: 2026-05-23 ~08:15 (服务器时间)
- **Checkpoint save 间隔**: 500 steps ✓ (现有 500/1000/1500/2000)

### SCP 结果

| Checkpoint | 状态 |
|---|---|
| exp-004-s2 ckpt-2000 | **新传输** → 28034 ✓ |
| exp-003-s2 ckpt-7500 | 未生成 (当前 7231) |

28034 现有 exp004_s2: 500, 1000, 1500, **2000**。exp003_s2: 500–7000 不变。

---
