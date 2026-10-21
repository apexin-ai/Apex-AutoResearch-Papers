# diagnose disk integrity check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_disk-integrity-check_20260520T063112_result.json`
- **Structured JSON:** [`6eea7a51c5d52f9ffc13.json`](../../sessions/6e/6eea7a51c5d52f9ffc13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告。

---

## 磁盘状态

```
总容量: 50G | 已用: 50G | 剩余: 971M (99%)
```

## 空间占用 Top 7

| 目录 | 大小 | 说明 |
|------|------|------|
| models/Qwen/ | 39G | Qwen3-1.7B/8B/14B，唯一幸存的基础模型 |
| grpo_bf16_g4/ | 3.5G | GRPO adapter，有 adapter_model.safetensors |
| baselines/dreeam/ | 3.0G | DREEAM baseline |
| .hf_cache/ | 2.4G | HF 缓存 |
| freige/ | 586M | 项目代码 |
| data/ | 497M | docred 数据集 |
| eval_results/ | 370M | 评测结果（部分完整） |

---

## 1. 确认完整的关键资产

| 目录 | 大小 | 状态 |
|------|------|------|
| models/Qwen/Qwen3-14B | 28G | **完整** |
| models/Qwen/Qwen3-8B | 7.5G | **完整** |
| models/Qwen/Qwen3-1.7B | 3.8G | **完整** |
| grpo_bf16_g4/ | 3.5G | **完整** (adapter_model.safetensors 504MB) |
| baselines/dreeam/ | 3.0G | **完整** |
| data/docred/ | 451M | **完整** (5 json 文件) |
| freige/ | 586M | **完整** (项目代码) |
| eval_results/d102_llama_k1_s42 | 6.4M | **完整** (metrics.json 可读) |
| eval_results/eval_llama_rsft_s42_no_evidence | 6.5M | **完整** (metrics.json 可读) |
| eval_results/ (大部分有数据的子目录) | ~370M | **完整** — 约 60+ 个含 metrics.json 的结果目录 |

---

## 2. 确认丢失/清空的目录（严重）

### LLaMA 基础模型 — **全部丢失**
| 目录 | 状态 |
|------|------|
| models/meta-llama/Meta-Llama-3.1-8B/ | **空目录，无文件** |
| models/Qwen3-4B/ | **空目录，无文件** |

### 全部 SFT adapters — **全部丢失** (17 个目录)
| 目录 | 状态 |
|------|------|
| sft_output_llama_3_1_8b/ | **空** — RSFT 的直接上游，最关键 |
| sft_output_llama_3_1_8b_no_evidence/ | **空** |
| sft_output_llama_3_1_8b_s43/ | **空** |
| sft_output_llama_3_1_8b_s44/ | **空** |
| sft_output_14b/ | **空** |
| sft_output_qwen3_1_7b_bf16/ (s42/s43/s44) | **全空** |
| sft_output_qwen3_8b_bf16/ (s42/s43/s44) | **全空** |
| sft_output_qwen3_*_no_evidence/ | **全空** |
| sft_no_evidence_output/ | **空** |
| sft_output/, sft_output_seed43, sft_output_seed44 | **全空** |

### 全部 RSFT adapters — **全部丢失** (13 个目录)
| 目录 | 状态 |
|------|------|
| rsft_output_llama_3_1_8b_k1/ | **0B** — checkpoint-1100/1107 目录在但内容清空 |
| rsft_output_llama_3_1_8b_k1_s43/ | **0B** — 同上 |
| rsft_output_llama_3_1_8b_k1_s44/ | **0B** — 同上 |
| rsft_output_qwen3_1_7b_k1/ (s42/s43/s44) | **全 0B** |
| rsft_output_qwen3_8b_k1/ (s42/s43/s44) | **全 0B** |
| rsft_output_random_k1/ | **0B** |
| rsft_output_nli_large/ | **0B** |
| rsft_output_ced_s43/ | **0B** |
| rsft_output_4b_sft_s44/ | **0B** |

### 全部 RSFT 中间数据 — **全部丢失**
| 目录 | 状态 |
|------|------|
| rsft_scored_llama_3_1_8b_k1/ | **空** |
| rsft_filtered/ | **空** (rsft_train.jsonl 不存在) |
| rsft_scored_* (11 个目录) | **全空** |
| rsft_filtered_* (4 个目录) | **全空** |
| rsft_data/ (4 shards) | **全空** |
| rsft_generations/ (4 shards) | **全空** |
| rsft_generations_14b/ | **空** |
| rsft_generations_4b_sft_s44/ | **空** |
| rsft_candidates_llama_3_1_8b/ | **空** |

### 空的 eval_results 子目录（~20 个）
bf16_g8_step30/50, dpo_ced_ckpt400, grpo_extract_r4_step10, grpo_flatnli_r3, plan_006_llama_rsft_seed43_eval, plan_006_qwen3_1_7b_rsft_eval, qwen3_1_7b_no_evidence_eval_v2, qwen3_8b_no_evidence_eval, redocred_rsft_eval/_r3, rsft_flat_nli_s44_reeval, rsft_s44_dev_with_preds, rsft_topk3/_fixed, sft, sft_4b_s43/s44_eval, sft_llama_s43/s44_eval

---

## 3. 可安全清理的目录

| 目录 | 说明 |
|------|------|
| 上述所有 0B 的空壳目录（~80+个） | 只剩目录结构，无任何文件，可全部删除回收 inode |
| .hf_cache/ (2.4G) | 可清理，重新下载即可 |
| .pytest_cache/ | 16K，无用 |
| rsft_probe_d034/ | 空 |
| scripts/ | 空 |
| mvp1_results/ | 空 |

---

## 4. 不确定，需进一步检查

| 目录 | 说明 |
|------|------|
| rsft_output_4b_sft_s44_bf16/ | du 显示 4K 但无文件（find 返回空），checkpoints 子目录在但可能空 |
| eval_outputs/ (54M) | 有 7 个子目录有内容，未逐一验证 json 完整性 |
| lead1_ced_filter_results/ (19M) | 未检查内容 |
| logs/ (1.4M) | 未检查 |

---

## 诊断结论

**AutoDL 重启后发生了大面积文件清空**。所有 safetensors/模型权重文件被删除，但目录结构和小文件（metrics.json、config）保留。这是典型的 AutoDL 磁盘满后自动清理或数据盘损坏的表现。

**影响范围**：
- **LLaMA 3.1-8B 基础模型** — 需重新下载 (~15GB)
- **Qwen3-4B 基础模型** — 需重新下载 (~8GB)
- **全部 30+ 个 SFT/RSFT adapter** — 需重新训练
- **全部 RSFT 中间数据（生成/打分/筛选）** — 需重新生成
- **eval_results 部分丢失** — 但主要结果（d102_*, plan_006_*, llama_rsft_*等）幸存

**幸存的关键资产**：Qwen3 全系列基础模型（39G）、grpo_bf16_g4 adapter（3.5G）、全部 docred 数据、大部分 eval metrics、项目代码。

**当前磁盘 99% 满**，主要被 Qwen3-14B (28G) 占据。重新训练前需先清理空目录和决定是否保留 Qwen3-14B。

---
