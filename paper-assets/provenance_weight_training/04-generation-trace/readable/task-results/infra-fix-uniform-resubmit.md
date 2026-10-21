# infra fix uniform resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-uniform-resubmit_20260513T232214_result.json`
- **Structured JSON:** [`380b0a0763ee838287a7.json`](../../sessions/38/380b0a0763ee838287a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 tmux session 存在，GPU 1 已在训练（93% utilization, 44GB），GPU 2-3 正在加载模型。

### 汇报

| 实验 | GPU | PID | tmux session | 状态 |
|------|-----|-----|-------------|------|
| uniform_seed42 | cuda:1 | 47603 | uniform_seed42 | 成功，已在训练 |
| uniform_seed123 | cuda:2 | 47749 | uniform_seed123 | 成功，模型加载中 |
| uniform_seed456 | cuda:3 | 47890 | uniform_seed456 | 成功，模型加载中 |

所有修改已完成：
- 旧 tmux sessions 和残留进程已 kill
- `pretrain_weighted.py` 已添加 `--save_total_limit` 和 `--save_only_model` CLI 参数，TrainingArguments 已对接
- 旧数据文件已删除
- 3 个任务均通过 `submit_training_job` 正确提交（有 cron 监控），从 checkpoint-500 恢复，`save_total_limit=2`，`save_only_model` 启用

---
