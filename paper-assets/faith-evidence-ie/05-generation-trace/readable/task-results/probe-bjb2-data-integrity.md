# probe bjb2 data integrity

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_bjb2-data-integrity_20260520T070810_result.json`
- **Structured JSON:** [`fbe5331d409e93e11074.json`](../../sessions/fb/fbe5331d409e93e11074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-12179 数据完整性报告

### 磁盘总览
- **总量**: 208G / 250G (83%)
- **剩余**: 43G

### Adapter 完整性 — 全部完好

所有 30 个 adapter 目录均含有效 `adapter_model.safetensors`（非 0B）：

| 目录 | 大小 | adapter | 状态 |
|------|------|---------|------|
| **SFT — LLaMA 3.1 8B** ||||
| sft_output_llama_3_1_8b/ | 4.5G | 641M | ✓ |
| sft_output_llama_3_1_8b_no_evidence/ | 4.5G | 641M | ✓ |
| sft_output_llama_3_1_8b_s43/ | 4.5G | 641M | ✓ |
| sft_output_llama_3_1_8b_s44/ | 4.5G | 641M | ✓ |
| **SFT — Qwen3 8B** ||||
| sft_output_qwen3_8b_bf16/ | 4.6G | 666M | ✓ |
| sft_output_qwen3_8b_no_evidence/ | 4.6G | 666M | ✓ |
| sft_output_qwen3_8b_s43/ | 4.6G | 666M | ✓ |
| sft_output_qwen3_8b_s44/ | 4.6G | 666M | ✓ |
| **SFT — Qwen3 1.7B** ||||
| sft_output_qwen3_1_7b_bf16/ | 1.9G | 266M | ✓ |
| sft_output_qwen3_1_7b_bf16_seed43/ | 1.9G | 266M | ✓ |
| sft_output_qwen3_1_7b_bf16_seed44/ | 1.9G | 266M | ✓ |
| sft_output_qwen3_1_7b_no_evidence/ | 1.9G | 266M | ✓ |
| **SFT — Qwen3 4B** ||||
| sft_output/ (s42) | 5.8G | 253M | ✓ |
| sft_output_seed43/ | 2.1G | 504M | ✓ |
| sft_output_seed44/ | 2.1G | 504M | ✓ |
| **SFT — 14B** ||||
| sft_output_14b/ | 7.3G | 491M | ✓ |
| **RSFT — LLaMA 3.1 8B** ||||
| rsft_output_llama_3_1_8b_k1/ | 4.5G | 641M | ✓ |
| rsft_output_llama_3_1_8b_k1_s43/ | 4.5G | 641M | ✓ |
| rsft_output_llama_3_1_8b_k1_s44/ | 4.5G | 641M | ✓ |
| **RSFT — Qwen3 8B** ||||
| rsft_output_qwen3_8b_k1/ | 4.6G | 666M | ✓ |
| rsft_output_qwen3_8b_k1_s43/ | 4.6G | 666M | ✓ |
| rsft_output_qwen3_8b_k1_s44/ | 4.6G | 666M | ✓ |
| **RSFT — Qwen3 1.7B** ||||
| rsft_output_qwen3_1_7b_k1/ | 1.9G | 266M | ✓ |
| rsft_output_qwen3_1_7b_k1_s43/ | 1.9G | 266M | ✓ |
| rsft_output_qwen3_1_7b_k1_s44/ | 1.9G | 266M | ✓ |
| **RSFT — 其他** ||||
| rsft_output_4b_sft_s44/ | 4.1G | 252M | ✓ |
| rsft_output_4b_sft_s44_bf16/ | 7.5G | symlink→ckpt-567 | ⚠️ |
| rsft_output_ced_s43/ | 8.0G | 504M | ✓ |
| rsft_output_nli_large/ | 8.0G | 504M | ✓ |
| rsft_output_random_k1/ | 3.5G | 504M | ✓ |

### 其他数据

| 类别 | 大小 |
|------|------|
| models/ (base 模型) | 70G |
| baselines/ | 3.0G |
| eval_results/ | 370M |
| freige/ (代码) | 586M |
| data/ | 497M |
| rsft_scored_*/ (8 dirs) | ~490M |
| rsft_filtered_*/ (5 dirs) | ~245M |
| rsft_generations_*/ (3 dirs) | ~748M |

### 总结

- **29/30 adapter 完好**，均含有效 safetensors 文件
- **1 个异常**: `rsft_output_4b_sft_s44_bf16/adapter_model.safetensors` 是 symlink 指向 `checkpoint-567/`，需确认该 checkpoint 目录是否存在且完整
- SFT+RSFT adapter 合计 ~130G，base models 70G，数据/中间文件 ~5G
- 数据盘完好可用，适合作为迁移源

---
