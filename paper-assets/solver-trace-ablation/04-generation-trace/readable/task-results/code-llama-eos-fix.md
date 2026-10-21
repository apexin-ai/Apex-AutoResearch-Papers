# code llama eos fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-eos-fix_20260521T083101_result.json`
- **Structured JSON:** [`a2f2d54fe8c8efb0ea66.json`](../../sessions/a2/a2f2d54fe8c8efb0ea66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

**诊断报告**：TRL GRPOTrainer 在 `__init__` 中从 `tokenizer.eos_token_id`（单个值 128001）构建自己的 `self.generation_config`，并在 `model.generate()` 调用时使用它，完全忽略 `model.generation_config`。之前的 patch 修改了 `trainer.model.generation_config`（无效目标）。

**修复方案**：将 patch 目标从 `trainer.model.generation_config` 改为 `trainer.generation_config`，同时更新 `trainer.generation_kwargs["eos_token_id"]`（被 `unwrap_model_for_generation` 使用）。条件检测不变：仅当 tokenizer 包含 `<|eot_id|>` 且非 unk 时才 patch。

**Dry-run 结果（10 步）**：avg reward=0.14, parse_rate=1.0, clipped_ratio=0.25, loss 非零。对比修复前（reward=0, loss=0, clipped_ratio=1.0），完全恢复正常。

**训练提交**：PID 857887, tmux session `d165-llama-exec-s42`, 日志 `/tmp/d165_llama_exec_s42_r3.log`, 500 步 ~82 分钟预计完成。

---
