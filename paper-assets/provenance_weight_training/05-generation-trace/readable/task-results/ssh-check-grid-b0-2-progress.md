# ssh check grid b0 2 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_grid_b0_2_progress_20260517T073458_result.json`
- **Structured JSON:** [`0ab9f5a4618d70c5e295.json`](../../sessions/0a/0ab9f5a4618d70c5e295.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**1. grid_b0_2_seed42 进度**
- 当前 step: **3713 / 6103** (61%)
- ETA: **~1h24m** (1:23:42 remaining, ~2.10s/it)
- 运行正常，epoch 0.16，GPU 3

**2. grid_b0_3_seed456.sh 存在于 westd-41312？**
- **YES** — `/root/provenance_weight_training/scripts/run_grid_b0_3_seed456.sh` 存在

**3. 硬编码 GPU 问题**
- 脚本内**没有**硬编码 `CUDA_VISIBLE_DEVICES`，可以由外部注入（如 tmux 启动时指定）。无需修改。

注意：脚本缺少 `--eval_data_path` 和 `--eval_steps` 参数（grid_b0_2 有这两个参数）。如果需要训练中评估，启动前需补上。

---
