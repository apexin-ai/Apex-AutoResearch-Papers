# eval repobench monitor

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_repobench_monitor_20260516T075543_result.json`
- **Structured JSON:** [`02345b19cbdac4470470.json`](../../sessions/02/02345b19cbdac4470470.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 7 个 `best_by_val_loss` 目录都存在，脚本不会跳过任何 checkpoint。

## 总结

| 项目 | 状态 |
|------|------|
| **执行模式** | 无自动编排——上个 Worker 只启动了 random_s42 单个进程 |
| **当前运行** | `repobench_random_s42`（PID 158952，GPU 1，15:53 启动，~30/500 batches in python_cff split） |
| **编排脚本** | 已创建并启动（PID 159855），等待 random_s42 完成后顺序运行剩余 6 个 |
| **已完成** | 0/7 |
| **运行中** | random_s42（预计还需 ~2.5 小时） |
| **排队中** | random_s43 → random_s44 → embed_dist_s43 → embed_dist_s44 → dataflow_s43 → dataflow_s44 |
| **GPU 约束** | GPU 1 已近满载（StarCoder 训练 54GB + evals），顺序执行是唯一可行方式 |
| **预计总完成时间** | 每个 checkpoint ~2.5-3 小时，7 个共 ~17-21 小时（约明天上午 8-12 点 CST） |

脚本逻辑：跳过已有输出文件的 checkpoint → 如果某个中途失败可以安全重跑。日志：`/root/autodl-tmp/structfuse/logs/repobench_eval_all.log`。

---
