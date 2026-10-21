# code grid b runner submit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grid-b-runner-submit_20260513T234921_result.json`
- **Structured JSON:** [`810d72076f7752a9aecc.json`](../../sessions/81/810d72076f7752a9aecc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

- **脚本创建** ✓ — `/root/provenance_weight_training/run_grid_b_seed42.sh`，6 个 b 值（0.5, 1.0, 1.5, 2.0, 3.0, 5.0）串行运行
- **submit_training_job** ✓ — PID `50134`，tmux session `grid_b_seed42_batch`，日志 `~/runs/provenance_weight_training/grid_b_seed42_batch.log`
- **GPU 0** — 当前 0% utilization / 0 MiB（模型正在加载中，日志显示已开始 b=0.5 的训练，`torch_dtype` 警告可忽略）
- GPU 1-3 被其他任务占用（94-99%），不受影响

预计 6 个 b 值总计约 10 小时完成。

---
