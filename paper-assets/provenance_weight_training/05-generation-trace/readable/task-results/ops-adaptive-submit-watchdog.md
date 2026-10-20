# ops adaptive submit watchdog

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_adaptive-submit-watchdog_20260514T024549_result.json`
- **Structured JSON:** [`d7029370e273cba5dbb3.json`](../../sessions/d7/d7029370e273cba5dbb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1/2/3 全部 99% 利用率、46523 MiB 显存占用，adaptive 实验全部正常运行。

## 汇报

| uniform PID | 状态 | adaptive exp_id | adaptive PID | GPU | GPU 占用 |
|------------|------|-----------------|-------------|-----|---------|
| 47603 | 已结束（首次检查即 DEAD） | adaptive_seed42 | 58888 | cuda:1 | 99%, 46523 MiB |
| 47749 | 已结束（首次检查即 DEAD） | adaptive_seed123 | 58978 | cuda:2 | 99%, 46523 MiB |
| 47890 | 已结束（首次检查即 DEAD） | adaptive_seed456 | 59058 | cuda:3 | 99%, 46523 MiB |

- **uniform 完成时间**：3 个 uniform 进程在首次轮询时已全部结束
- **adaptive 提交时间**：立即提交，GPU 空闲间隔 < 1 分钟
- **日志路径**：`~/runs/provenance_weight_training/adaptive_seed{42,123,456}.log`

---
