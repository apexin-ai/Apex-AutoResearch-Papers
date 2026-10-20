# ssh prep seed123 launch configs

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-seed123-launch-configs_20260513T014331_result.json`
- **Structured JSON:** [`81756eb75bd810ac3bad.json`](../../sessions/81/81756eb75bd810ac3bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置已保存到 `artifacts/seed123_launch_configs.md` 和 `memory.md`。

汇总：

**CLS seed123（home-1x5090）** — 仅改 3 项：`--seed 123`、`--output_dir checkpoints_repo_cls_seed123/`、`--run_name repo-cls-qwen3-4b-lora-home-seed123`。环境用 `/home/sonny/miniconda3` conda base。日志写 `/tmp/repo-level-cls-seed123_stdout.log`。

**CWM seed123（seetacloud-westd-4x5090）** — 仅改 3 项：`--seed 123`、`--output_dir checkpoints_repo_cwm_seed123/`、`--run_name repo-cwm-qwen3-4b-lora-seed123`。去掉 `--resume_from_checkpoint`（全新训练）。环境用 `/root/miniconda3` conda base，`CUDA_VISIBLE_DEVICES=2`。日志写 `/root/autodl-tmp/cwm_seed123_train.log`。

补充发现：CLS v4 的日志在 05-12 18:45 停止写入，进程 exit code 143——可能已结束或被 kill。CWM v10 当前在 seetacloud 正常训练中（从 checkpoint-200 resume，当前 checkpoints 到 600）。

---
