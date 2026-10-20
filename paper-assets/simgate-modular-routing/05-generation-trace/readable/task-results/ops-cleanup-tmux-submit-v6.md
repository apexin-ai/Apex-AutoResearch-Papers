# ops cleanup tmux submit v6

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-tmux-submit-v6_20260514T070051_result.json`
- **Structured JSON:** [`ab993748944d01e68661.json`](../../sessions/ab/ab993748944d01e68661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **Stale tmux sessions** — 全部清理（v3/v4/v5/v6）
2. **僵尸进程** — PID 239593（OOM 后占用 29GB 显存）已 kill，GPU 释放
3. **v6 重新提交** — tmux session `plan-002-formal-v6` 启动，PID 240633，GPU 0 占用 29848 MiB，训练正在进行
4. **Registry 更新** — status=RUNNING，spec 含 command/pid/log_path/data_path/data_count/model_name/seed/server/gpu

注意：之前的 v6 OOM 是因为框架的 submit 和我的 tmux submit 同时抢 GPU 0 导致。当前只有一个训练实例在跑，应该正常。

---
