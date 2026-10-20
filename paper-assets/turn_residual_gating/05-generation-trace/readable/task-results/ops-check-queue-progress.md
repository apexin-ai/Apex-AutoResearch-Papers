# ops check queue progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_queue_progress_20260523T000638_result.json`
- **Structured JSON:** [`397be8232094c893f66e.json`](../../sessions/39/397be8232094c893f66e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Queue Runner 状态

**当前位置：[2/8] AR N=50 existing s42 checkpoints — 子任务 [3/4] LO (LoRA-only)**

| 子任务 | 状态 | 完成时间 |
|--------|------|----------|
| [1/4] TG s42 | 完成 | 07:24 |
| [2/4] UG s42 | 完成 | 07:58 |
| [3/4] LO s42 | **进行中** — 模型已加载完毕，正在生成 | — |
| [4/4] ? | 待执行 | — |

结果文件 `lo_s42_ar_n50.json` 已存在（08:06 更新），说明 LO 生成可能接近完成或已完成，日志尾部还没刷新到最终结果。

**GPU：** 43% 利用率，22.3 GB / 97.9 GB 显存（有活跃任务）

**tmux：** ssh_read_only 不允许执行 tmux ls，但 GPU 有负载，runner 在跑。

**整体进度：** 8 个 queue item 中完成了 1 个，第 2 个正在执行中（4 个子任务已完成 2-3 个）。

---
