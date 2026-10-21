# eval lead2 ckpt20 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lead2_ckpt20_eval_20260517T123030_result.json`
- **Structured JSON:** [`99ca0011180ada5ddc06.json`](../../sessions/99/99ca0011180ada5ddc06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**Checkpoint 结构**：LoRA adapter（`adapter_model.safetensors` + `adapter_config.json`）

**adapter_config.json 关键内容**：
- `peft_type`: LORA
- `base_model_name_or_path`: `/root/autodl-tmp/merged_sft_rsft_ced_s43`
- `r`: 64, `lora_alpha`: 128, `lora_dropout`: 0.05
- `target_modules`: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- `task_type`: CAUSAL_LM

**额外处理**：
1. `merged_sft_rsft_ced_s43` 不存在，已重建（Qwen3-4B + SFT adapter merge + RSFT_CED_s43 adapter merge → 7.6GB）
2. `inference.py` 对 adapter 强制要求 `--sft_adapter` 的校验过于严格，已 patch：当 `--base_model` 非默认值时改为 warning

**提交状态**：
- PID: **446829**
- GPU: cuda:1
- tmux session: `lead2_ckpt20_eval`
- Log: `/root/autodl-tmp/logs/lead2_ckpt20_eval.log`
- Registry: RUNNING
- 985 docs / 247 batches，推理已开始

---
