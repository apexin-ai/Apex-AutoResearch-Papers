# fix eval mbpp grpo rasp 20 retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_mbpp_grpo_rasp_20_retry_20260519T183201_result.json`
- **Structured JSON:** [`0b882283c70d3ab0ea41.json`](../../sessions/0b/0b882283c70d3ab0ea41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

| 步骤 | 状态 |
|------|------|
| kill 残留 tmux session | done |
| 确认 session 清理 | `eval_mbpp_grpo_rasp_20` 不在旧列表中 |
| 重新提交 (tmux + CUDA_VISIBLE_DEVICES=1) | PID 127964, tmux session 存活 |
| 物理 GPU 确认 | Bus ID `5A:00.0` = 物理 GPU 1, 12488 MiB |
| 日志 | 模型加载完成，MBPP dataset 已加载 (374 tasks) |
| Registry | RUNNING, retry_count=2 |

注意：因为 `submit_training_job` 工具不可用，这次是通过 `ssh_execute` 手动提交的 tmux session，没有框架的退出码监控钩子。如果进程结束，需要手动检查结果并更新 registry。

---
