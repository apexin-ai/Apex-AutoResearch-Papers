# check plan 008 pruning sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan_008_pruning_sweep_20260516T150940_result.json`
- **Structured JSON:** [`89fb80aa596088e71970.json`](../../sessions/89/89fb80aa596088e71970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_008 **没有在运行**。两台服务器的状态：

**westd-27271:**
- 无相关进程，无 tmux session
- GPU 完全空闲（0 MiB / 97GB × 2，0% 利用率）
- `eval_pruning_sweep.py` 脚本存在，但默认输出文件 `eval_results/pruning_sweep.json` 不存在 — **脚本从未被执行过**
- 最近的活动是 `formal_bound_dryrun.json`（23:09）和 `plan_005_formal_bound.log`（22:32），属于 plan_005

**cqa1-33015:**
- 无 plan_008 相关文件或进程
- tmux 里跑的是 `libero_full_ft_baseline` 和 `libero_lora_baseline`，与 plan_008 无关

**结论：plan_008_pruning_sweep 状态标记为 RUNNING 但实际从未启动。** 脚本已就绪（`eval_pruning_sweep.py`），但没有被执行。需要手动启动，或将 registry 状态更新为 NOT_STARTED。

---
