# check baseline plus libero10 results

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_baseline-plus-libero10-results_20260516T103137_result.json`
- **Structured JSON:** [`a7828a9111c46feef3ea.json`](../../sessions/a7/a7828a9111c46feef3ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**进程状态**：PID 675231 已结束，eval 正常完成（eval_info.json 于 May 16 17:22 写入，10 tasks × 50 episodes 全部完成）。

### libero_10 per-task SR

| Task | SR |
|------|-----|
| 0 | 42.0% (21/50) |
| 1 | 70.0% (35/50) |
| 2 | 86.0% (43/50) |
| 3 | 88.0% (44/50) |
| 4 | 62.0% (31/50) |
| 5 | 90.0% (45/50) |
| 6 | 62.0% (31/50) |
| 7 | 54.0% (27/50) |
| 8 | 42.0% (21/50) |
| 9 | 76.0% (38/50) |
| **Avg** | **67.2%** (336/500) |

### baseline_plus 4-suite 汇总

| Suite | Avg SR |
|-------|--------|
| libero_spatial | 81.6% |
| libero_object | 88.8% |
| libero_goal | 87.8% |
| libero_10 | **67.2%** |
| **Overall** | **81.4%** |

libero_10 是最难的 suite，67.2% 明显低于其他三个（81-89%），但这在预期范围内——libero_10 任务复杂度更高。Task 0 和 Task 8 最弱（42%），Task 5 最强（90%）。

---
