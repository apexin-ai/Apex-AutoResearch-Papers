# check v2 training resume verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v2-training-resume-verify_20260514T173608_result.json`
- **Structured JSON:** [`9b16f8c200c58bbd52d7.json`](../../sessions/9b/9b16f8c200c58bbd52d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### CWM 8B v2 (cuda:2) — **已崩溃**
- **错误**: `FileNotFoundError: '/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/trainer_state.json'`
- **原因**: `--resume_from_checkpoint` 指向了 output_dir 顶层目录，而非具体的 checkpoint 子目录。`trainer_state.json` 在 `checkpoint-1600/` 里。
- **修复**: 改为 `--resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-1600`

### CLS 8B s123 v2 (cuda:3) — **即将崩溃**
- 当前还在数据处理阶段（train truncation 刚完成），尚未到 `trainer.train()` 调用
- 同样的问题：`--resume_from_checkpoint` 指向顶层目录，`trainer_state.json` 在 `checkpoint-3000/` 里
- **预计**会在模型加载完毕、调用 `trainer.train()` 时报同样的 `FileNotFoundError`
- **修复**: 改为 `--resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000`

### CWM eval (cuda:0/1) — 正常运行
- **eval_cwm_seed123**: 9320/9784 (95.3%), running_acc=59.0%
- **eval_cwm_v12**: 9440/9784 (96.5%), running_acc=57.9%
- 两个 eval 预计很快完成

### 需要操作
两个 v2 训练都需要用正确的 checkpoint 路径重新提交。要我现在 kill CLS 进程并用正确路径重新启动两个训练吗？

---
