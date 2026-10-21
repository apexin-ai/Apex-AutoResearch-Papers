# analyze exp 003 eval s2 ckpt7500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp-003-eval-s2-ckpt7500_20260522T172657_result.json`
- **Structured JSON:** [`86ceccf22074a6978348.json`](../../sessions/86/86ceccf22074a6978348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

**exp-003-eval-s2-ckpt7500 结果汇总：**

| 指标 | 值 |
|------|-----|
| SYCONScore | 0.1241 |
| ToF | 0.0663 |
| NoF | 0.9724 |
| n_valid / n_total | 181 / 362 |
| vs vanilla | -0.0094 (-7.0%) |

SYCONScore 0.1241 < vanilla 0.1335，与 seed 1 ckpt-7500 (0.1046) 同为 negative，但 seed 2 表现略好。R3-only 两个 seed 在 ckpt-7500 均未超过 baseline。

---
