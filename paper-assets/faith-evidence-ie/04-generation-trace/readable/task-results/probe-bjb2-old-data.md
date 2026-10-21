# probe bjb2 old data

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_bjb2-old-data_20260520T071025_result.json`
- **Structured JSON:** [`4d3157726cc245b05111.json`](../../sessions/4d/4d3157726cc245b05111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-12179 数据完整性报告

### 磁盘总览
- 总容量 250G，已用 208G (83%)，剩余 43G

---

### 1. 完整资产（有 safetensors，大小正常）

**Adapter 模型（16 个 SFT + 14 个 RSFT = 30 个）：**

| 目录 | 大小 | safetensors |
|------|------|-------------|
| `sft_output_llama_3_1_8b` (s42) | 4.5G | 641M ✓ |
| `sft_output_llama_3_1_8b_s43` | 4.5G | ✓ |
| `sft_output_llama_3_1_8b_s44` | 4.5G | ✓ |
| `sft_output_llama_3_1_8b_no_evidence` | 4.5G | ✓ |
| `sft_output_14b` | 7.3G | 491M ✓ |
| `sft_output` (4B s42) | 5.8G | 253M ✓ |
| `sft_output_seed43` | 2.1G | ✓ |
| `sft_output_seed44` | 2.1G | ✓ |
| `sft_output_qwen3_1_7b_bf16` | 1.9G | ✓ |
| `sft_output_qwen3_1_7b_bf16_seed43` | 1.9G | ✓ |
| `sft_output_qwen3_1_7b_bf16_seed44` | 1.9G | ✓ |
| `sft_output_qwen3_1_7b_no_evidence` | 1.9G | ✓ |
| `sft_output_qwen3_8b_bf16` | 4.6G | ✓ |
| `sft_output_qwen3_8b_s43` | 4.6G | ✓ |
| `sft_output_qwen3_8b_s44` | 4.6G | ✓ |
| `sft_output_qwen3_8b_no_evidence` | 4.6G | ✓ |
| `rsft_output_llama_3_1_8b_k1` (s42) | 4.5G | 641M ✓ |
| `rsft_output_llama_3_1_8b_k1_s43` | 4.5G | ✓ |
| `rsft_output_llama_3_1_8b_k1_s44` | 4.5G | ✓ |
| `rsft_output_qwen3_1_7b_k1` | 1.9G | ✓ |
| `rsft_output_qwen3_1_7b_k1_s43` | 1.9G | ✓ |
| `rsft_output_qwen3_1_7b_k1_s44` | 1.9G | ✓ |
| `rsft_output_qwen3_8b_k1` | 4.6G | ✓ |
| `rsft_output_qwen3_8b_k1_s43` | 4.6G | ✓ |
| `rsft_output_qwen3_8b_k1_s44` | 4.6G | ✓ |
| `rsft_output_4b_sft_s44` | 4.1G | ✓ |
| `rsft_output_4b_sft_s44_bf16` | 7.5G | ✓ |
| `rsft_output_ced_s43` | 8.0G | ✓ |
| `rsft_output_nli_large` | 8.0G | ✓ |
| `rsft_output_random_k1` | 3.5G | ✓ |

**基座模型（3 个，70G）：**
| 目录 | 大小 | 状态 |
|------|------|------|
| `models/meta-llama/Meta-Llama-3.1-8B` | 15G | 4 shards, 完整 ✓ |
| `models/Qwen3-4B` | 7.6G | 3 shards, 完整 ✓ |
| `models/Qwen/` | 47G | (含 Qwen3-8B / 14B 等) ✓ |

**数据集：**
| 资产 | 大小/行数 | 状态 |
|------|-----------|------|
| `data/` | 497M | ✓ |
| `rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl` | 2952 行 | ✓ |
| `rsft_filtered/rsft_train.jsonl` | 2718 行 | ✓ |
| `rsft_generations_14b/` | 133M | ✓ |
| `eval_results/` | 370M, ~130 个结果目录/文件 | ✓ |

---

### 2. 空目录（0 字节，已清空）

| 目录 | 说明 |
|------|------|
| `rsft_data/` | 0 |
| `rsft_score_input_s0/` | 0 |
| `rsft_score_input_s1/` | 0 |
| `rsft_score_input_s2/` | 0 |
| `rsft_score_input_s3/` | 0 |

这些是中间产物（scoring pipeline 的临时输入），已被清理，不影响最终数据。

---

### 3. 可迁移数据量估算

| 类别 | 大小 |
|------|------|
| Adapter 模型 (30个) | ~117G |
| 基座模型 (3个) | ~70G |
| 数据集 + scored/filtered | ~1.5G |
| eval_results | ~370M |
| 生成数据 (14b + 4b + llama) | ~750M |
| 其它 (baselines, GRPO, freige, misc) | ~18G |
| **合计** | **~208G** |

基座模型如果新服务器已有则不需迁移，实际需迁移约 **138G**（adapter + 数据 + eval）。

---
