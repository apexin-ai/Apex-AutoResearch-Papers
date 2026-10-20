# diagnose adaptive fix failure

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_adaptive_fix_failure_20260514T173932_result.json`
- **Structured JSON:** [`1d84eacaf6e95a25a96d.json`](../../sessions/1d/1d84eacaf6e95a25a96d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

三组实验崩溃原因完全相同。三个日志文件头部均显示：

```
pretrain_weighted.py: error: unrecognized arguments: --overwrite_output_dir
EXIT_CODE=2
```

`pretrain_weighted.py` 使用自定义 argparse，**不支持 `--overwrite_output_dir` 参数**。该参数是 HuggingFace `TrainingArguments` 的内置参数，但这个脚本没有使用 `HfArgumentParser` / `TrainingArguments`，而是手动定义了参数列表。

脚本支持的完整参数列表（从 usage 输出）：
`--data_path`, `--output_dir`, `--model_name`, `--weighting_method`, `--grid_b_value`, `--contamination_ratio`, `--num_train_tokens`, `--max_steps`, `--num_train_epochs`, `--batch_size`, `--gradient_accumulation_steps`, `--learning_rate`, `--max_length`, `--tau`, `--n_min`, `--use_wandb`, `--wandb_project`, `--wandb_run_name`, `--seed`, `--eval_data_path`, `--eval_steps`, `--save_steps`, `--logging_steps`, `--warmup_ratio`, `--weight_decay`, `--save_total_limit`, `--save_only_model`, `--resume_from_checkpoint`, `--bf16`, `--no_bf16`

### 修复方案

**只需调命令参数，不需要改代码。** 从启动命令中删除 `--overwrite_output_dir` 即可。

如果确实需要覆盖已有输出目录的行为，有两个选择：
1. 启动前手动删除已有的 output_dir
2. 在 `pretrain_weighted.py` 的 argparse 中添加 `--overwrite_output_dir` 参数并在训练逻辑中实现对应功能

### 补充说明

seed123 和 seed456 的日志文件中，错误信息后面跟着大量 null bytes 和旧训练进度数据——这是之前运行遗留的内容（日志文件未被清空，而是被 truncate 后部分覆写）。尾部看到的训练进度（27%/24%）是**旧数据**，不是本次运行的输出。

---
