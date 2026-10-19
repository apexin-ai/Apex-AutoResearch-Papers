# submit bce v3 critical retry

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_bce_v3_critical_retry_20260516T044236_result.json`
- **Structured JSON:** [`1a09e41ab76715bd2077.json`](../../sessions/1a/1a09e41ab76715bd2077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 最终报告

**实验 bce_isocompute_v3_s42 正在正常运行，无需任何干预。**

| 项目 | 值 |
|------|-----|
| 状态 | RUNNING |
| Python PID | 205598 |
| Wrapper PID | 205597 |
| GPU | cuda:1, 90938 MiB 已用 |
| 进度 | Step 200/2700 |
| 速度 | 1.05s/step |
| 日志 | `/root/distill_sparse_swiglu/logs/bce_isocompute_v3_s42.log` |
| 预计完成 | ~13:25 UTC (约 43 分钟后) |
| 训练指标 | loss=0.6538, bce=0.6519, sparsity=0.518 |

**根因：之前的 Worker 声称"进程死了"是因为检查了错误的日志路径 `/root/runs/distill_sparse_swiglu/`（不存在），实际日志在 `/root/distill_sparse_swiglu/logs/`。** 进程实际上通过 nohup 正确启动并一直在跑。

---
