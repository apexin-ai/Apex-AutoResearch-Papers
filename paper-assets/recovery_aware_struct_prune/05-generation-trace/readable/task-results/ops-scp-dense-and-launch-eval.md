# ops scp dense and launch eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp_dense_and_launch_eval_20260518T220721_result.json`
- **Structured JSON:** [`2f4df4f9e7113a314fc3.json`](../../sessions/2f/2f4df4f9e7113a314fc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **模型大小**: 15GB（westb-23072 和 westd-29022 一致）
- **传输**: 模型已存在于 westd-29022（之前有断链符号链接，已修复为实体目录）
- **Eval 状态**: 已在 westd-29022 GPU 0 上启动，tmux session `eval_math500_dense_2048`
  - GPU 0 占用 17585MiB，模型加载完成，正在加载 MATH 数据集
  - GPU 1 被其他任务占用（97% util）
- **Registry**: `eval_math500_dense_2048` → RUNNING
- **日志**: `/tmp/eval_math500_dense_2048.log`
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_2048.json`

---
