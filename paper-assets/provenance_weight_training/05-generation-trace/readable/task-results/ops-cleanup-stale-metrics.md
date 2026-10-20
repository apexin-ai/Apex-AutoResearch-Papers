# ops cleanup stale metrics

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-stale-metrics_20260514T070536_result.json`
- **Structured JSON:** [`7b399c4ff02eb67c844c.json`](../../sessions/7b/7b399c4ff02eb67c844c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总：

| 实验 | 旧数据行数 (备份) | 清空后当前行数 | 备份文件 |
|------|-------------------|---------------|----------|
| grid_b0_5_seed123 | 1420 | 10 | `step_metrics.jsonl.bak_pre_restart` |
| grid_b1_0_seed123 | 1410 | 10 | `step_metrics.jsonl.bak_pre_restart` |
| grid_b1_5_seed123 | 1410 | 10 | `step_metrics.jsonl.bak_pre_restart` |

truncate 后文件已有 10 行新数据写入，说明训练进程 fd 未断，正在正常写入干净数据。

---
