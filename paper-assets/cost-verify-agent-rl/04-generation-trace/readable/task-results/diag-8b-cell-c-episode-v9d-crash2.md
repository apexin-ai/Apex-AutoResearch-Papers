# diag 8b cell c episode v9d crash2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_8b_cell_c_episode_v9d_crash2_20260520T051422_result.json`
- **Structured JSON:** [`7ad090c7af5bd1b0e8ad.json`](../../sessions/7a/7ad090c7af5bd1b0e8ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**崩溃原因**：SFT 基础模型 `/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231` 在磁盘清理中被删除。代码初始化时 `huggingface_hub` 将不存在的本地路径当作 repo ID 校验，抛出 `HFValidationError`。

**修复方案**：将 config 中 `model_path` 改为仍存在的 `/root/autodl-tmp/models/Qwen3-8B`（base model，架构相同），配合 `resume_mode: auto` 会自动从 step 5 checkpoint（92GB，完好）恢复权重继续训练。

报告已写入 `artifacts/8b_cell_c_episode_v9d/diag_v9d_crash2.md`。

---
