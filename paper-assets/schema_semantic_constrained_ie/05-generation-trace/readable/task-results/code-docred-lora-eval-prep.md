# code docred lora eval prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred_lora_eval_prep_20260515T192805_result.json`
- **Structured JSON:** [`cca4d740289b4ecebb12.json`](../../sessions/cc/cca4d740289b4ecebb12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**训练状态**: 两个 DocRED LoRA 训练均在 step 382/573 (epoch 2/3)，还剩 ~191 steps。

**关键发现**:
- Checkpoint 路径与预期略有不同：Qwen 目录是 `qwen_lora_docred`（非 `qwen3_8b_lora_docred`）
- 训练脚本**自带 merge 步骤**，训练完成后会自动合并到 `/root/autodl-tmp/checkpoints/{qwen,llama}_lora_docred_merged/`
- **eval 脚本已存在**: `scripts/run_docred_lora_eval.sh`，包含 4 条 eval 命令（Qwen/Llama × unconstrained/constrained），路径已正确
- 磁盘 162GB 可用，足够两个 merged 模型 (~16GB each)

**输出**: `artifacts/docred_lora_eval_commands.md`，包含:
- 2 条备用手动 merge 命令（Qwen + Llama，仅在自动 merge 失败时用）
- 4 条 eval 命令（含 `run_docred_lora_eval.sh` 快捷方式）
- 建议执行顺序和 DocRED 特有注意事项（max_new_tokens=4096, 96 relation types）

---
