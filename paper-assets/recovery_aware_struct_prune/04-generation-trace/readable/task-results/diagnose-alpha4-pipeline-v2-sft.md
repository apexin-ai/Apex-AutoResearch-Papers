# diagnose alpha4 pipeline v2 sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha4_pipeline_v2_sft_20260521T180459_result.json`
- **Structured JSON:** [`103a55716164d1c47c7b.json`](../../sessions/10/103a55716164d1c47c7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已启动，模型加载中。

---

**诊断结果**：pipeline_alpha4_0_v2 的 SFT 步骤因 TRL API 不兼容而失败——脚本传了 `max_seq_length` 给 `SFTConfig`，但当前 TRL 版本的参数名是 `max_length`。Pruning 步骤本身成功完成（19.09% sparsity，模型 12GB 完整）。

**修复**：`train_sft_warmup.py` 第 94 行 `max_seq_length` → `max_length`。

**SFT 提交结果**：
- exp_id: `sft_alpha4_20_manual`
- PID: `399511`
- server: `westd-29022`, GPU: `cuda:2`
- command: `python src/train_sft_warmup.py --model_path .../pruned_alpha4_20 --output_dir .../sft_alpha4_20 --num_epochs 2 --lr 2e-5`
- log: `~/runs/recovery_aware_struct_prune/sft_alpha4_20_manual.log`

---
