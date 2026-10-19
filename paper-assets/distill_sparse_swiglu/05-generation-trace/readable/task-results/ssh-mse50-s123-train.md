# ssh mse50 s123 train

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mse50_s123_train_20260520T185500_result.json`
- **Structured JSON:** [`3c7cae4e5c3520686f4d.json`](../../sessions/3c/3c7cae4e5c3520686f4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动：

- **exp_id**: `mse50_s123`
- **server/GPU**: westd-34887 / cuda:0 (PID 235945, tmux session `mse50_s123`)
- **log**: `~/runs/distill_sparse_swiglu/mse50_s123.log`(已确认进入 "Loading model" 阶段)
- **Registry**: RUNNING, parent=`mse50_s42_eval_7task`, hypothesis 已填

关键修正（与 prompt 原命令偏离）：
- MSE 用独立脚本 `src/train_perlayer_mse.py`，不接受 `--loss_type`/`--dataset`/`--lambda_max`/`--gradient_checkpointing`/`--log_every`。命令已与 `mse50_s42_train`（registry 中）逐参数对齐，仅改 seed 42→123。
- checkpoint 文件名确认为 `predictor_mse.pt`（与 mse30_test 目录一致）。

---
