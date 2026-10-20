# code prep eval scripts phase2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_eval_scripts_phase2_20260519T123920_result.json`
- **Structured JSON:** [`46acdd281d2477c36093.json`](../../sessions/46/46acdd281d2477c36093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均已创建，语法检查通过。

### 产出汇报

**脚本 1**: `/root/autodl-tmp/freige/scripts/seed_expansion/eval_8b_sft_s43.sh`
- Base model: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- SFT adapter: `/root/autodl-tmp/sft_output_qwen3_8b_bf16_seed43` — **尚不存在**，脚本含 adapter_config.json 检查逻辑，训练未完成会报错退出
- D076 协议: `--model_path` = base model, `--sft_adapter` = adapter

**脚本 2**: `/root/autodl-tmp/freige/scripts/d112/eval_d112_rsft_bf16.sh`
- Base model: `/root/autodl-tmp/models/Qwen3-4B`
- SFT adapter (第一层): `/root/autodl-tmp/sft_output_seed44` — **已存在** (确认为 4B LoRA, base=Qwen3-4B)
- RSFT adapter (第二层): `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16` — 有 checkpoint-150~350，但根目录无 adapter_config.json（**训练未完成**），脚本含检查逻辑
- RSFT eval 模式: `--model_path` = RSFT adapter (auto-detect), `--base_model` = Qwen3-4B, `--sft_adapter` = SFT s44

**注意事项**:
1. 两个训练均未完成，提交 eval 前需确认 adapter_config.json 存在
2. 4B base model 路径是 `/root/autodl-tmp/models/Qwen3-4B`（无 `Qwen/` 前缀），与 8B 路径格式不同
3. 提交时需 `GPU=X bash script.sh` 或 `CUDA_VISIBLE_DEVICES=X` 指定空闲 GPU（C001/C002 约束）

---
