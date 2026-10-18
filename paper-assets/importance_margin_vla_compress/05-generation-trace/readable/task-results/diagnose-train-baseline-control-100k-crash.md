# diagnose train baseline control 100k crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_baseline_control_100k_crash_20260518T122844_result.json`
- **Structured JSON:** [`72a921f90d59e38d42f7.json`](../../sessions/72/72a921f90d59e38d42f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**崩溃原因：`wandb.init()` 失败，服务器上没有 W&B API key。** 模型/checkpoint/数据都加载成功了，但 line 473 的 `wandb.init()` 因为缺少认证直接抛异常退出。

根因：cqa1-33015 上没有 `~/.netrc`、没有 `~/.config/wandb/`、没有 `WANDB_API_KEY` 环境变量。训练命令也没传这个变量。

**修复：** 在训练命令里加 `export WANDB_API_KEY=&lt;key>` 或 `export WANDB_MODE=offline`。另外建议加 `CUDA_VISIBLE_DEVICES=0`，因为 GPU 1 当前被 eval job 占用。

报告已保存到 `artifacts/worker_output_baseline_control_crash.md`。

---
