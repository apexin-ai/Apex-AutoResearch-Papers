# eval acts2 ckpt4500 result

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acts2-ckpt4500-result_20260522T182649_result.json`
- **Structured JSON:** [`d8c6a27c2a86a5e5f226.json`](../../sessions/d8/d8c6a27c2a86a5e5f226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ACT s2 ckpt-4500 Eval 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.2229** |
| ToF | 0.1271 |
| NoF | 0.9061 |
| n_valid / n_invalid | 181 / 181 |
| 耗时 | 1407s (~23min) |

### vs Vanilla (0.1335)

- **差值**: +0.0894 (+66.9%)
- **是否 > vanilla**: **YES**

ckpt-4500 的 SYCONScore 0.2229 大幅超过 vanilla baseline 0.1335。ToF 从 vanilla 水平略有下降（0.1271），但 NoF 很高（0.9061），说明模型在 invalid pressure 场景下几乎不被带偏，抗压能力很强。

---
