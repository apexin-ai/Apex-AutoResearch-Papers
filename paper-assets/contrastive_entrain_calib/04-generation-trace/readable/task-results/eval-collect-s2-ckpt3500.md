# eval collect s2 ckpt3500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-s2-ckpt3500_20260521T111430_result.json`
- **Structured JSON:** [`b12ec4a6ed20c9d278b7.json`](../../sessions/b1/b12ec4a6ed20c9d278b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**exp-003-eval-s2-ckpt3500 结果：**

| 指标 | 值 |
|------|-----|
| ToF | 0.0387 |
| NoF | 0.9724 |
| SYCONScore | **0.0744** |

Seed 2 完整趋势：ckpt-2000=0.085 → ckpt-2500=0.105 → ckpt-3000=0.095 → **ckpt-3500=0.074**。SYCONScore 持续下降，ckpt-2500 仍是 seed 2 的峰值。与 vanilla baseline (0.134) 差距进一步拉大。

---
