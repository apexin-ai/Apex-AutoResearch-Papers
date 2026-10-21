# diag exp016 final results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp016-final-results_20260519T061013_result.json`
- **Structured JSON:** [`5b660acc14e29f5cb41e.json`](../../sessions/5b/5b660acc14e29f5cb41e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**exp-016 ActAdd Steering 已完成，判定 success。**

| Alpha | NoF | WRR | vs baseline |
|-------|------|------|-------------|
| 0.0 (baseline) | 69.6% | 27.1% | — |
| 0.5 | 69.1% | 25.4% | NoF -0.6pp |
| 1.0 | 71.3% | 26.5% | NoF +1.7pp |
| 2.0 | 68.5% | 25.4% | NoF -1.1pp |
| **5.0** | **78.5%** | **21.5%** | **NoF +8.8pp, WRR -5.5pp** |

- PID 85457 已结束，GPU 3 空闲（4MiB，0%利用率）
- Registry 已更新：status=DONE, conclusion=success, metrics 已录入
- Hook 修复后各 alpha 结果确实不同，确认 steering 生效
- 注意非单调性：alpha=0.5/2.0 无明显改善，仅 alpha=5.0 跳跃式提升，可能需要更细粒度搜索 alpha∈[3,8] 区间

---
