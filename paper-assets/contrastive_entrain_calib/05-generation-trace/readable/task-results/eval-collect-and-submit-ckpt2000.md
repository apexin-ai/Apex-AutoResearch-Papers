# eval collect and submit ckpt2000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-and-submit-ckpt2000_20260522T094333_result.json`
- **Structured JSON:** [`41684a528a8e475fdad3.json`](../../sessions/41/41684a528a8e475fdad3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### Part 1: Eval 结果收集

| Experiment | SYCONScore | ToF | NoF | Conclusion |
|---|---|---|---|---|
| **ACT s2 ckpt-1500** (`exp-004-s2-eval-ckpt1500`) | **0.2137** | 0.1215 | 0.884 | success |
| **R3-only s2 ckpt-7000** (`exp-003-eval-s2-ckpt7000`) | **0.0945** | 0.0497 | 0.9503 | negative |

ACT s2 轨迹更新：500=0.223 → 1000=0.256 → **1500=0.214**（下降，与 seed 1 的 1500=0.170 类似出现 dip）。

R3-only s2 ckpt-7000=0.0945，低于 vanilla baseline (0.1335)，与 seed 1 ckpt-7000=0.105 一致——R3-only 持续 negative。

### Part 2: ACT s2 ckpt-2000 eval

已提交到 GPU 0（PID 992567），registry `exp-004-s2-eval-ckpt2000` 状态 RUNNING。预计 ~1 小时完成。

---
