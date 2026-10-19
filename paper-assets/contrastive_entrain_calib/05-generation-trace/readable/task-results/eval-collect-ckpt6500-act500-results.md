# eval collect ckpt6500 act500 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-ckpt6500-act500-results_20260522T070247_result.json`
- **Structured JSON:** [`451fd413120f6928a3be.json`](../../sessions/45/451fd413120f6928a3be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

### Results

| Experiment | SYCONScore | ToF | NoF | vs Vanilla (0.1335) |
|---|---|---|---|---|
| **exp003-s2-ckpt6500** (R3-only seed2) | **0.1046** | 0.0552 | 0.9779 | -21.7% |
| **exp004-s2-ckpt500** (ACT seed2) | **0.2232** | 0.1271 | 0.9171 | +67.2% |

对比 seed 1：
- R3-only seed1 ckpt-6500 = 0.153 → seed2 ckpt-6500 = 0.1046，**seed 2 未复现 spike，反而低于 vanilla**。Conclusion: negative。
- ACT seed1 ckpt-500 = 0.170 → seed2 ckpt-500 = **0.2232**，seed 2 大幅超过 seed 1（+31%）。ACT 跨 seed 稳定且 seed 2 更强。Conclusion: success。

### GPU 状态
4 卡全空闲（每卡 2 MiB，0% utilization）。Eval 已全部完成。

---
