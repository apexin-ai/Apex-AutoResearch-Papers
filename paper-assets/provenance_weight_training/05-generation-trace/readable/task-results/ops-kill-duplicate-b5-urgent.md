# ops kill duplicate b5 urgent

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_duplicate_b5_urgent_20260514T113535_result.json`
- **Structured JSON:** [`f9e5d7917126a9326858.json`](../../sessions/f9/f9e5d7917126a9326858.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**1. PID 92798** — 已成功 kill。

**2. PID 94717** — 正常运行中。
- RSS: 3.6GB，运行时间 13 分 21 秒
- GPU 显存: 46514 MiB（kill 掉重复进程后显存已恢复正常，OOM 风险解除）

**3. checkpoint 目录** — 无损坏迹象。
- `checkpoint-500/` 完整，`model.safetensors` 大小 1.19GB（合理）
- 所有文件在 19:31-19:32 期间统一写入，无冲突痕迹
- `step_metrics.jsonl` 持续更新中（19:36 最后写入）

**4. PID 92798 来源** — tmux session `grid_b5_0_seed123`。
- 该 session 于 19:22:46 创建，正是注册的那个 session（PID 94712→94716→94717 进程链）
- PID 92798 不属于这个 tmux session 的进程链，是一个被额外手动/重复启动的进程。tmux session 中只有一个 `grid_b5_0_seed123`，说明 92798 是在 tmux 之外启动的。

---
