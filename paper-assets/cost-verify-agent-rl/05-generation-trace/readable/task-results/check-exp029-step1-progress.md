# check exp029 step1 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_step1_progress_20260516T154415_result.json`
- **Structured JSON:** [`aacb49ee8b69b177cb95.json`](../../sessions/aa/aacb49ee8b69b177cb95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029 状态：已崩溃

**进程**: PID 872859 已死，GPU 0/1 均 0 MiB / 0% 利用率。

**崩溃点**: Step 0 训练完成后，wandb 日志写入时崩溃。

**错误**: `FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpzicbifxf'`
- 调用链: `wandb_run.log()` → `_log_table_artifact()` → `artifact.new_file()` → `tempfile.mkdtemp()` → `os.mkdir()` 失败
- `/tmp/` 当前只有 `ray/` 和 `tmux-0/`，wandb 的临时目录被清理或创建竞争失败

**已完成的 val_before_train metrics (step 0, 32 episodes)**:

| Metric | Value |
|--------|-------|
| success | **0.125** (12.5%) |
| pass@1 | 0.125 |
| action_is_valid | 0.783 |
| action_is_effective | 1.0 |
| num_actions | 44.59 |
| response_length | 7088.03 |
| reward/mean@32 | 1.25 |
| non-zero/success | 1.0 |

**未产出任何训练 metrics** — PPO forward pass 开始了（`compute_policy_loss` 被调用），但 step 0 的 metrics 在 wandb log 时崩溃，没有记录到 entropy/kl_loss/grad_norm/pg_loss。

**根因**: wandb 在 `/tmp` 下创建 artifact 临时文件时失败。可能是容器 `/tmp` 清理策略或 tmpfs 空间问题。修复方案：重启前设置 `TMPDIR=/root/autodl-tmp/tmp` 或 `WANDB_DIR=/root/autodl-tmp/wandb` 绕过。

---
