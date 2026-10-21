# eval collect s2 ckpt2500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-s2-ckpt2500_20260521T104658_result.json`
- **Structured JSON:** [`f7c2cfe21e22a717faa5.json`](../../sessions/f7/f7c2cfe21e22a717faa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。Cron 列表为空（本 session 无 cron），无需删除。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| ToF | 0.0552 |
| NoF | 0.9724 |
| **SYCONScore** | **0.1046** |
| n_total | 362 |

**Seed 2 trajectory 对比：**
- ckpt-2000: SYCONScore = 0.0846
- **ckpt-2500: SYCONScore = 0.1046** ← 新
- ckpt-3000: SYCONScore = 0.0945

Seed 2 ckpt-2500 (0.1046) 高于两端 (0.0846, 0.0945)，呈非单调趋势。与 seed 1 一致——R3-only 训练 trajectory 均远低于 vanilla baseline (0.134)。

---
