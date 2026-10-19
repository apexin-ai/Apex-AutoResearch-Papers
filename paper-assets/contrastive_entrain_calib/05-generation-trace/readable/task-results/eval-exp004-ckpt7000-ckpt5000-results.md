# eval exp004 ckpt7000 ckpt5000 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-ckpt7000-ckpt5000-results_20260520T150853_result.json`
- **Structured JSON:** [`70719261f90deec17ca4.json`](../../sessions/70/70719261f90deec17ca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是完整的 ACT baseline (exp-004) SYCONScore 训练轨迹（D027 unified eval）：

| Checkpoint | ToF | NoF | SYCONScore | vs Vanilla |
|---|---|---|---|---|
| Vanilla | - | - | **0.1335** | baseline |
| ckpt-500 | 0.0939 | 0.8895 | 0.1699 | +27.3% |
| ckpt-1000 | 0.1160 | 0.8729 | 0.2048 | +53.4% |
| ckpt-2000 | 0.1492 | 0.8785 | 0.2550 | +91.0% |
| **ckpt-5000** | **0.1547** | **0.8785** | **0.2631** | **+97.1%** |
| ckpt-4000 | 0.1215 | 0.8950 | 0.2140 | +60.3% |
| ckpt-6000 | 0.1547 | 0.8508 | 0.2618 | +96.1% |
| **ckpt-7000** | **0.1713** | **0.8619** | **0.2858** | **+114.1%** |
| ckpt-8000 | 0.1823 | 0.8674 | 0.3013 | +125.7% |

轨迹分析：
- ckpt-5000 (SYCONScore=0.2631) 和 ckpt-7000 (0.2858) 填补了 ckpt-4000→6000 和 ckpt-6000→8000 之间的空隙
- ckpt-4000 是一个明显的 dip（0.214），ckpt-5000 恢复到 0.2631，说明 4000 步附近的下降是暂时的
- 整体趋势：SYCONScore 随训练步数单调递增（除 ckpt-4000 外），ToF 稳步上升，NoF 略有下降但保持在 0.85+ 水平

---
