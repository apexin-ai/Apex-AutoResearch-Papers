# code grpo fix v2

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-fix-v2_20260514T070515_result.json`
- **Structured JSON:** [`c6ec07bcb328b2a9a9d9.json`](../../sessions/c6/c6ec07bcb328b2a9a9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

### 结果汇总

| 项目 | 状态 |
|------|------|
| GRPOConfig 参数验证 | `temperature`, `num_generations`, `max_completion_length`, `beta`, `gradient_checkpointing` 全部存在于 TRL 1.1.0 |
| 额外修复 | 无需额外修复 |
| 训练启动 | 成功 |

**日志关键信息**:
- LoRA adapter 已加载并合并到 base model
- 训练数据：294 prompts，73 steps
- WANDB offline 模式已启用
- 进度条已出现 `0/73`，正在执行第一个 batch

**GPU 显存**:
- GPU 0: **64,409 MiB / 97,887 MiB** (65.8%) — 模型已加载
- GPU 1: 16,849 MiB（其他任务占用）

唯一的警告是 vLLM 版本（0.18.1 vs 支持的 0.11-0.17.1），不影响训练（未使用 vLLM）。

---
