# research find 4b rsft s42 checkpoint

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_find_4b_rsft_s42_checkpoint_20260519T125818_result.json`
- **Structured JSON:** [`0d39a84461f284c9a449.json`](../../sessions/0d/0d39a84461f284c9a449.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从 `rsft_output_random_k1` 的 training_args.bin 中解析出 **seed=42**（`K*` = ASCII 42）。这就是 canonical 4B RSFT s42。

## 结果

### 所有 RSFT 目录及 base model

| 目录 | Base Model | 备注 |
|------|-----------|------|
| `rsft_output_random_k1` | Qwen3-4B | **seed=42, canonical** |
| `rsft_output_ced_s43` | Qwen3-4B | seed=43, CED method |
| `rsft_output_4b_sft_s44` | Qwen3-4B | D112 QLoRA (排除) |
| `rsft_output_4b_sft_s44_bf16` | Qwen3-4B | D112 bf16 (排除) |
| `rsft_output_qwen3_1_7b_k1[_s43/_s44]` | Qwen3-1.7B | 3个目录 |
| `rsft_output_qwen3_8b_k1[_s43/_s44]` | Qwen3-8B | 3个目录 |
| `rsft_output_llama_3_1_8b_k1[_s43]` | Llama-3.1-8B | 2个目录 |

### Canonical 4B RSFT s42

- **路径**: `/root/autodl-tmp/rsft_output_random_k1`
- **base_model**: `/root/autodl-tmp/models/Qwen3-4B`
- **seed**: 42
- **LoRA**: r=64, alpha=128, dropout=0.05
- **文件列表**:
  ```
  adapter_config.json
  adapter_model.safetensors
  added_tokens.json
  chat_template.jinja
  checkpoint-1000/
  checkpoint-1020/
  merges.txt
  special_tokens_map.json
  tokenizer.json
  tokenizer_config.json
  training_args.bin
  vocab.json
  README.md
  ```
- adapter 完整（adapter_config.json + adapter_model.safetensors 均存在）

---
