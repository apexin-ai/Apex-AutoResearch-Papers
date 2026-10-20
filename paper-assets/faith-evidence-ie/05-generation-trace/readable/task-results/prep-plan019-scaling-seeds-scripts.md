# prep plan019 scaling seeds scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan019_scaling_seeds_scripts_20260518T171145_result.json`
- **Structured JSON:** [`3269fd5ea4476d50263d.json`](../../sessions/32/3269fd5ea4476d50263d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过语法检查。汇总如下：

## 创建的脚本（4个）

| 脚本 | 类型 | 模型 | Seed | 关键路径 |
|------|------|------|------|----------|
| `sft_8b_s44.sh` | SFT | Qwen3-8B | 44 | output: `sft_output_qwen3_8b_s44/` |
| `sft_llama_s44.sh` | SFT | LLaMA-3.1-8B | 44 | output: `sft_output_llama_3_1_8b_s44/` |
| `eval_8b_s44.sh` | RSFT Eval | Qwen3-8B | 42 | model: `rsft_output_qwen3_8b_k1_s44`, sft_adapter: `sft_output_qwen3_8b_bf16` |
| `eval_llama_s44.sh` | RSFT Eval | LLaMA-3.1-8B | 42 | model: `rsft_output_llama_3_1_8b_k1_s44`, sft_adapter: `sft_output_llama_3_1_8b` |

## 已存在的脚本（无需创建）

| 脚本 | 类型 | 状态 |
|------|------|------|
| `sft_1_7b_s43.sh` | SFT 1.7B s43 | 已有 |
| `train_8b_s44.sh` | RSFT 8B s44 | 已有 |
| `train_llama_s44.sh` | RSFT LLaMA s44 | 已有 |

## SFT 超参数（8B/LLaMA 一致，匹配 canonical）

lr=2e-4, epochs=3, batch=1, grad_accum=16, warmup=0.05, lora_rank=64, lora_alpha=128, lora_dropout=0.05, max_length=4096, bf16, no-quantize

## 验证通过

- 所有依赖路径（base model, sft adapter, rsft data）均已确认存在
- CUDA_VISIBLE_DEVICES 全部使用 `${GPU:-${CUDA_VISIBLE_DEVICES:-0}}` 新格式
- Eval 脚本使用 D076 协议（`--model_path=rsft_checkpoint --base_model=base --sft_adapter=adapter`）
- `bash -n` 语法检查 4/4 通过

---
