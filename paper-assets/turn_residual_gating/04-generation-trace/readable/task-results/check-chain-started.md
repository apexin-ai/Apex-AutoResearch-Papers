# check chain started

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_chain_started_20260523T113816_result.json`
- **Structured JSON:** [`445e1c508421084a1f74.json`](../../sessions/44/445e1c508421084a1f74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：**

- **PID 84793**：仍在运行 `d048_ss_s123`（`train_phase2_v8b.py`），当前 Epoch 1 Step 2700 / 总 3000 步，约 90% 完成。GPU 占用 47GB/98GB，82% 利用率。
- **等待脚本 PID 93020**：已超时退出。日志 `/tmp/wait_and_launch.log` 显示 19:29 超时（10 分钟内 PID 84793 未退出），**链未启动**。
- **gpu_chain_next.sh**：未运行，`/tmp/gpu_chain.log` 不存在。
- **现有队列**：`d048_auto_transition.sh`（PID 56573）和 `d048_remaining_queue.sh`（PID 65789）仍在运行，可能已包含后续任务的自动调度。

训练还剩约 300 步，预计 20-30 分钟内完成。需要我重新设置等待脚本来等 84793 退出后启动 `gpu_chain_next.sh`，还是现有的 queue runner 已经覆盖了后续任务？

---
