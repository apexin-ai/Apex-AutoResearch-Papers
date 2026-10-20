# exp detect remove submit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_detect_remove_submit_20260516T012437_result.json`
- **Structured JSON:** [`d555561d1483e483b348.json`](../../sessions/d5/d555561d1483e483b348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已经在运行但有问题。情况汇总：

**当前状态：**
- PID 275277 已在 cuda:1 上运行，步数 43/6103 (1%)，约 3 分钟前启动
- 与 grid_b0_3_seed42 (PID 274309) 共享 cuda:1，速度 ~4.45s/it，预估 7.5h（正常应 ~3.5h）
- **W&B 未启用** — 启动命令中用了 `WANDB_MODE=disabled`，没有 `--use_wandb` 参数
- Registry 状态停留在 ALLOCATED

**脚本问题：**
- `run_detect_remove.sh` 中数据路径是 `data/scored_data_filtered_t05.jsonl`（注意 `t05` 不是 `q05`），但实际运行的进程用的是正确的 `scored_data_filtered_q05.jsonl`（说明是直接构造命令行提交的，没用脚本）
- 脚本用了 `--use_wandb --wandb_project provenance-weight-training`，但实际运行的命令没有这些参数

**建议：** 杀掉当前进程（才跑了 1%），用启用 W&B 的命令重新提交。需要确认你是否同意？

---
