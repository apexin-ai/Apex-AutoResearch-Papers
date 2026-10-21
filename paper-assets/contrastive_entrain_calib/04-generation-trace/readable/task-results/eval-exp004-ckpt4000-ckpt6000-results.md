# eval exp004 ckpt4000 ckpt6000 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-ckpt4000-ckpt6000-results_20260520T144219_result.json`
- **Structured JSON:** [`9809cc686e67307be6c7.json`](../../sessions/98/9809cc686e67307be6c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均正常完成（EXIT_CODE=0）。结果如下：

## exp004_ckpt4000
- ToF: 0.1215
- NoF: 0.8950
- SYCONScore: 0.2140
- n_valid: 181
- n_invalid: 181
- n_total: 362
- vs_vanilla: SYCONScore 0.2140 vs 0.1335 = **+60.3%**

## exp004_ckpt6000
- ToF: 0.1547
- NoF: 0.8508
- SYCONScore: 0.2618
- n_valid: 181
- n_invalid: 181
- n_total: 362
- vs_vanilla: SYCONScore 0.2618 vs 0.1335 = **+96.0%**

完整轨迹（按 training steps 排序）：

| Checkpoint | ToF | NoF | SYCONScore | vs Vanilla |
|---|---|---|---|---|
| vanilla | — | — | 0.1335 | baseline |
| ckpt-500 | 0.0939 | 0.8895 | 0.1699 | +27.3% |
| ckpt-2000 | 0.1492 | 0.8785 | 0.2550 | +91.0% |
| **ckpt-4000** | **0.1215** | **0.8950** | **0.2140** | **+60.3%** |
| **ckpt-6000** | **0.1547** | **0.8508** | **0.2618** | **+96.0%** |
| ckpt-8000 | 0.1823 | 0.8674 | 0.3013 | +125.7% |

注意 ckpt-4000 的 SYCONScore (0.2140) 低于 ckpt-2000 (0.2550)，轨迹在 step 2000→4000 出现回落，之后 6000→8000 恢复上升。这个非单调性值得在论文中讨论——可能反映训练中期的 loss landscape 波动。

---
