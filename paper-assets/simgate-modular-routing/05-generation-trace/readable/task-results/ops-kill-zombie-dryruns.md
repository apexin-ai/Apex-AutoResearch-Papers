# ops kill zombie dryruns

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-dryruns_20260514T144128_result.json`
- **Structured JSON:** [`ae8ec1a24e9fb1e03a91.json`](../../sessions/ae/ae8ec1a24e9fb1e03a91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**清理结果：**

- PID 281564、282738、285291 — 已成功 kill（返回码 0，进程不再存在）
- 但发现**另一组 counterfactual 进程仍在运行**：
  - `290557` — tmux session `alfworld_cf`
  - `290558` — bash wrapper
  - `290564` — `python src/alfworld_counterfactual.py --n_tasks 140 --gpu_id 1`（占 26% CPU，1.6GB 内存）
  - `290565` — tee 日志

这组是正式运行（非 dryrun），在 tmux session `alfworld_cf` 中。需要一并清理吗？

---
