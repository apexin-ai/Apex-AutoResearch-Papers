# check cls 8b s123 v2 exit status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cls-8b-s123-v2-exit-status_20260514T173747_result.json`
- **Structured JSON:** [`f38bda895a730fbde5f5.json`](../../sessions/f3/f38bda895a730fbde5f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

- **退出原因**: 崩溃 — `FileNotFoundError`，`--resume_from_checkpoint` 传了父目录 `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` 而非具体 checkpoint 子目录，Trainer 在父目录找不到 `trainer_state.json`
- **Exit code**: 1，时间 2026-05-15 01:40:25 UTC
- **最终训练 step**: 未进入训练（v1 最后 checkpoint 仍为 checkpoint-3000）
- **最新 checkpoint**: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000`
- **GPU cuda:3**: 已释放（0 MiB）

**修复方法**: 重新提交时改为 `--resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000`

---
