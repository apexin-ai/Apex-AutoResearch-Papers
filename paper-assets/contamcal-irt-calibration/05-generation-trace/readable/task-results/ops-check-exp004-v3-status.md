# ops check exp004 v3 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp004-v3-status_20260515T001202_result.json`
- **Structured JSON:** [`81ec8926ef33d87c61f7.json`](../../sessions/81/81ec8926ef33d87c61f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认并更新 registry。

**exp-004 v3 (PID 599562) 状态：异常退出（磁盘配额超限）**

| 指标 | 值 |
|------|-----|
| 失败原因 | `Errno 122: Disk quota exceeded`（cmdstanpy MCMC 临时文件撑满 /tmp） |
| 崩溃位置 | 第 10/12 个 condition (`auc0.65_n50_prior1.0_binary`) |
| 结果文件 | 11/12 个 config 已保存，缺失 `auc0.65_n100_prior1.0_binary` |
| 成功 runs | **57/120**（47.5%） |
| 失败 runs | 50 runs 因磁盘满失败，13 runs 未执行 |

Registry 已更新为 `DONE/failed`，failure_reason 已记录。

---
