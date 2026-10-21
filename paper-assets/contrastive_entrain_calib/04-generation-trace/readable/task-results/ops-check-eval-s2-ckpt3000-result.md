# ops check eval s2 ckpt3000 result

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-s2-ckpt3000-result_20260525T154817_result.json`
- **Structured JSON:** [`566ffd99ec999e143078.json`](../../sessions/56/566ffd99ec999e143078.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**exp-003-s2-eval-ckpt3000 结果**

| 指标 | 值 |
|------|-----|
| ToF | 0.0387 |
| NoF | 0.9503 |
| SYCONScore | **0.0743** |
| n_total | 362 |
| elapsed | 4346s |

**跨 seed/step 对比：**
- seed 1 ckpt-3000: SYCONScore = 0.095
- seed 2 ckpt-2500: SYCONScore = 0.1241
- seed 2 ckpt-3000: SYCONScore = **0.0743** ← 明显下降

Seed 2 在 step 3000 出现性能退化（相比自身 ckpt-2500 下降 40%，也低于 seed 1 同步数）。

**状态更新：**
- Registry: DONE/success，metrics 已写入
- Cron: 已删除
- cuda:0: 已释放（0 MiB），可启动 exp-act-256

---
