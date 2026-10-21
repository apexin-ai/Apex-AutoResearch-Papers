# eval grid b0 2 and submit b0 3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b0_2_and_submit_b0_3_20260517T124529_result.json`
- **Structured JSON:** [`bf4465d9d2a8454f8109.json`](../../sessions/bf/bf4465d9d2a8454f8109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成：

**Part 1 — grid_b0_2_seed42 Eval**
- **PPL = 17.643**（loss = 2.8704，4,077,068 tokens）
- 与 grid_b0_3_seed42（PPL=17.640）几乎相同，b=0.2 和 b=0.3 在该区间性能持平
- Registry 已更新：metrics / conclusion=success / status=DONE

**Part 2 — grid_b0_3_seed456 提交**
- 服务器：westd-41312，GPU：cuda:3
- PID：88491（tmux session: grid_b0_3_seed456）
- output_dir 已修正为相对路径 `output/models/grid_b0_3_seed456`（通过 symlink 写入 autodl-tmp）
- Registry 状态已更新为 RUNNING

---
