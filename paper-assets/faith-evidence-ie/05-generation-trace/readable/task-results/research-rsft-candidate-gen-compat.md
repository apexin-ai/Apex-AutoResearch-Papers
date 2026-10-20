# research rsft candidate gen compat

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rsft_candidate_gen_compat_20260516T124116_result.json`
- **Structured JSON:** [`d700cbff7b64705e1f76.json`](../../sessions/d7/d700cbff7b64705e1f76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇报如下：

---

## rsft_generate.py 兼容性验证结果

### CLI 参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--base_model` | `/root/autodl-tmp/models/Qwen3-4B` | base model 路径 |
| `--sft_adapter` | `/root/autodl-tmp/sft_output` | SFT adapter 路径 |
| `--data_path` | None | DocRED 数据目录 |
| `--split` | `train` | 数据集 split |
| `--output_dir` | `/root/autodl-tmp/rsft_generations` | 输出目录 |
| `--num_generations` | 8 | N=8 candidates |
| `--temperature` | 0.7 | |
| `--top_p` | 0.95 | |
| `--batch_size` | 1 | |
| `--max_new_tokens` | 1024 | |
| `--seed` | 42 | |
| `--quantize` | store_true | 4bit QLoRA 量化 |
| `--start_idx` / `--end_idx` | 0 / -1 | 数据范围 |
| `--shard_id` / `--num_shards` | 0 / 1 | 多卡分片 |
| `--repetition_penalty` | 1.0 | |

### _apply_chat_template 兼容性：✅ 已就绪

- L43-47: `_apply_chat_template()` 已实现，正确处理 `enable_thinking` 参数兼容
- L39: 已导入 `LLAMA3_CHAT_TEMPLATE`
- L69-70: tokenizer 无 chat_template 时 fallback 到 `LLAMA3_CHAT_TEMPLATE`（LLaMA 兼容）

### Adapter 目录存在性：✅ 全部存在

**With-evidence:**
- `sft_output/` — Qwen3-4B ✅
- `sft_output_qwen3_1_7b_bf16/` — Qwen3-1.7B ✅
- `sft_output_qwen3_8b_bf16/` — Qwen3-8B ✅
- `sft_output_llama_3_1_8b/` — LLaMA-3.1-8B ✅

**No-evidence:**
- `sft_no_evidence_output/` — Qwen3-4B ✅
- `sft_output_qwen3_1_7b_no_evidence/` — Qwen3-1.7B ✅
- `sft_output_qwen3_8b_no_evidence/` — Qwen3-8B ✅
- `sft_output_llama_3_1_8b_no_evidence/` — LLaMA-3.1-8B ✅

**Base models:**
- `/root/autodl-tmp/models/Qwen3-4B` ✅
- `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` ✅
- `/root/autodl-tmp/models/Qwen/Qwen3-8B` ✅
- `/root/autodl-tmp/models/Meta-Llama-3.1-8B` ✅

### 需要额外适配的问题

1. **❌ 缺少 `--no_evidence` 参数** — 脚本只有硬编码的 with-evidence `SYSTEM_PROMPT`，没有 `NO_EVIDENCE_SYSTEM_PROMPT` 切换逻辑。如果要为 no-evidence adapter 生成 RSFT candidates，必须添加此支持（参照 C005 约束）。

2. **⚠️ `device_map="auto"`（L73）** — 按 C002/C003 约束，运行时必须设 `CUDA_VISIBLE_DEVICES=X` 限制到单卡，否则模型会跨 GPU 分布。

3. **base_model 路径不同** — 1.7B/8B 路径是 `/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,8B}`，LLaMA 是 `/root/autodl-tmp/models/Meta-Llama-3.1-8B`，均需通过 `--base_model` 显式指定（默认值只适用于 4B）。

---
