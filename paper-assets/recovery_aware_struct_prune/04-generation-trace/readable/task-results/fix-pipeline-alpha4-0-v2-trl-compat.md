# fix pipeline alpha4 0 v2 trl compat

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pipeline_alpha4_0_v2_trl_compat_20260521T183149_result.json`
- **Structured JSON:** [`f9ad3616b9f7bd8667b5.json`](../../sessions/f9/f9ad3616b9f7bd8667b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证全部通过。

## 修复报告

### TRL 版本
**TRL 1.4.0**（transformers 5.x 系列配套）

### 修复状态
`train_sft_warmup.py` 的修复**已经到位**。文件在报错后已被修改：
- **原代码（报错时）**：`max_seq_length=args.max_seq_length`（line 88 的 SFTConfig 调用）
- **当前代码（已修复）**：`max_length=args.max_seq_length`（line 94）

TRL 1.4.0 的 `SFTConfig` 将旧版 `max_seq_length` 参数重命名为 `max_length`。kwarg 名已正确更新，验证通过。

`sft_recovery.py` 同样已修复（line 114: `max_length=args.max_seq_length`）。

### GRPO 兼容性
`train_grpo_v5.py` 的 `GRPOConfig` 所有参数（`max_completion_length`, `temperature`, `repetition_penalty`, `num_generations`, `beta`, `loss_type` 等）与 TRL 1.4.0 **完全兼容**，无需修改。

### 次要问题（不阻塞运行）
1. **`logging_dir` 已废弃** — transformers v5.2 将移除此参数，建议改用 `TENSORBOARD_LOGGING_DIR` 环境变量。当前仅产生 warning，不影响运行。
2. **`torch_dtype` 已废弃** — `model_utils.py` 中的 `torch_dtype` 参数已改名为 `dtype`（日志中有 warning），不影响运行。

### Pipeline 脚本
`scripts/run_alpha4_pipeline.sh` 无需调整，所有 CLI 参数传递正确。Pipeline 可直接重新提交。

---
