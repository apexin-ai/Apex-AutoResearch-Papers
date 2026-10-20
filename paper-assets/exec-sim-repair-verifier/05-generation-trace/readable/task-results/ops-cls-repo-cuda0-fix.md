# ops cls repo cuda0 fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cls-repo-cuda0-fix_20260516T184047_result.json`
- **Structured JSON:** [`5a06e737870d34f60d93.json`](../../sessions/5a/5a06e737870d34f60d93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动。

## 汇报

| 项目 | 状态 |
|------|------|
| **训练启动** | 成功 |
| **GPU 0** | 89% 利用率, 19427 MiB 显存 |
| **PID** | 548885 |
| **tmux session** | `cls-repo-v4` |
| **模型** | deepseek-coder-6.7b-instruct (6.76B params, LoRA 16.7M trainable, 0.25%) |
| **总步数** | 6633 steps (3 epochs) |
| **日志** | `~/runs/exec-sim-repair-verifier/deepseek-cls-repo-v4.log` |

**train_unified.py 支持的关键参数：**
- `--model_name_or_path`, `--data_dir`, `--task {cls,cwm}`, `--output_dir`
- `--train_file`, `--val_file` (覆盖默认文件名)
- `--epochs`, `--seed`, `--batch_size`, `--grad_accumulation`, `--lr`, `--warmup_ratio`
- `--max_seq_length`, `--max_steps`
- `--lora_rank`, `--lora_alpha`, `--lora_dropout`
- `--wandb_project`, `--run_name`, `--no_wandb`
- `--resume_from_checkpoint` (支持，可以用)

另外清理了旧的 v3 残留进程（之前占 GPU 0 但未释放）。

---
