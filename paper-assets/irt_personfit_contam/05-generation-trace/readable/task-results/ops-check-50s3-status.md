# ops check 50s3 status

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-50s3-status_20260522T191641_result.json`
- **Structured JSON:** [`5294842bff77c4a58a35.json`](../../sessions/52/5294842bff77c4a58a35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**已完成的 s3 结果：**
| 条件 | 文件 | 关键指标 |
|------|------|----------|
| contam_15_s3 | ✅ `contam_15_s3_results.json` (02:49) | acc=73.5%, seen=82.0%, unseen=72.0%, lz*=5.44 |
| contam_25_s3 | ✅ `contam_25_s3_results.json` (00:28) | 已存在 |

**缺失：**
- `contam_50_s3_results.json` — 不存在（老路径和新路径都没有）

**当前训练：**
- `contam_50_s3` 正在跑，PID 56978，GPU 占用 27.6GB
- 进度：**1158/2256 steps (51%)**，epoch ~1.0 刚完成，已跑约 23 分钟
- 预计剩余 ~20 分钟完成训练，之后还需跑 eval

---
