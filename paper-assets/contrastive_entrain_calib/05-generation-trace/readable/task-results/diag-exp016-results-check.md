# diag exp016 results check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp016-results-check_20260519T045653_result.json`
- **Structured JSON:** [`6da5d0e6f4f5e9ba47d7.json`](../../sessions/6d/6da5d0e6f4f5e9ba47d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**exp-016 修复版仍在运行，预计约 12 分钟后完成。**

### 关键发现

| 项目 | 状态 |
|------|------|
| PID 85457 | 运行中 |
| 当前进度 | alpha=5.0, 240/362 samples |
| Hook 修复 | **已生效** |
| 结果文件 | **过期**（09:45 旧版产物，当前 run 10:07 启动） |

### Hook 触发统计（当前修复版）

| Alpha | Hooks fired |
|-------|-------------|
| 0.0 | 0 ✓ |
| 0.5 | 617,904 ✓ |
| 1.0 | 610,855 ✓ |
| 2.0 | 611,702 ✓ |
| 5.0 | 运行中 |

Hooks 确认生效。脚本在所有 alpha 完成后才写入 `results_summary.json`，所以当前文件是旧 run 的残留（所有 alpha 相同的那个 bug 版本）。

### 预计完成时间

alpha=5.0 以 ~2min/20samples 的速率推进，剩余 ~122 samples ≈ 12 分钟后完成写入新结果。

### 下一步

等 ~15 分钟后重新检查结果文件时间戳和内容，验证不同 alpha 是否产生不同的 NoF/WRR。

---
