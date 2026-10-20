# ops fix grpo unpruned pid conflict

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-grpo-unpruned-pid-conflict_20260516T021740_result.json`
- **Structured JSON:** [`1e553f01cf42e03b44b9.json`](../../sessions/1e/1e553f01cf42e03b44b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

wandb summary 还没写入（训练刚 resume 不久）。从日志看进度已到 step 25/100 并在保存 checkpoint-25。

## 汇报

| 项目 | 状态 |
|------|------|
| **PID 75381（原进程）** | 已死，无需处理 |
| **PID 77647/77652（fix Worker 启动）** | 存活，是**唯一**的 grpo_unpruned_v2 训练进程 |
| **PID 冲突** | **不存在**——75381 已自然退出，77647 是其替代进程，从 checkpoint-20 resume |
| **GPU 占用** | cuda:1 → PID 77652 占 91016 MiB；cuda:0 → PID 74134（eval_gsm8k.py）占 17654 MiB |
| **当前 step** | 25/100，正在写 checkpoint-25 |
| **Checkpoints** | checkpoint-20, checkpoint-25 已存在 |
| **磁盘** | /root/autodl-tmp 250G 用 173G，剩余 78G（70%），充足 |
| **wandb** | run ID `hwucjf2n`，summary 尚未生成（刚启动 3 分钟） |

**结论：无需 kill 任何进程。** 77647 就是当前正确运行的训练任务，不是重复进程。

---
