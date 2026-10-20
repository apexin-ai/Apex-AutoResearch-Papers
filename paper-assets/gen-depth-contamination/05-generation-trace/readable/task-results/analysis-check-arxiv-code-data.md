# analysis check arxiv code data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check-arxiv-code-data_20260520T030754_result.json`
- **Structured JSON:** [`5dca541e856db5b78b21.json`](../../sessions/5d/5dca541e856db5b78b21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告如下：

---

## 1. arXiv depth chain 数据

**存在，数据充足。** 共有以下目录（均在 `/root/autodl-tmp/gen-depth-contamination/data/`）：

| 目录 | Scorer 模型 | 样本数 | Depth 层级 |
|------|------------|--------|-----------|
| `exp_024_arxiv` | Qwen-1.5B (原始) | 13,200 | depth 0-5 (6级) |
| `exp_025_pythia_arxiv` | Pythia-1.4B | 13,200 | depth 0-5 |
| `exp_arXiv_llama8b` | LLaMA-8B | 13,200 | depth 0-5 |
| `exp_arXiv_mistral7b` | Mistral-7B | 13,200 | depth 0-5 |
| `exp_arXiv_olmo` | OLMo | 13,200 | depth 0-5 |
| `exp_arXiv_qwen7b` | Qwen-7B | 13,200 | depth 0-5 |
| `exp_arXiv_llama8b_crossscorer` | LLaMA-8B (cross) | 13,200 | depth 0-5 |
| `exp_arXiv_mistral7b_crossscorer` | Mistral-7B (cross) | 13,200 | depth 0-5 |
| `exp_arXiv_qwen1b5_crossscorer` | Qwen-1.5B (cross) | 13,200 | depth 0-5 |
| `exp_arXiv_qwen7b_crossscorer` | Qwen-7B (cross) | 13,200 | depth 0-5 |

每个 depth 级别 2,200 样本（13,200 / 6 = 2,200）。OBD K*=3 的生成链，depth 0 为 seed。

## 2. Code depth chain 数据

**存在，数据充足。** 

| 目录 | Scorer 模型 | 样本数 | Depth 层级 |
|------|------------|--------|-----------|
| `exp_code_pythia1b4` | Pythia-1.4B | 33,000 | depth 0-5 |
| `exp_code_llama8b` | LLaMA-8B | 33,000 | depth 0-5 |
| `exp_code_mistral7b` | Mistral-7B | 33,000 | depth 0-5 |
| `exp_code_qwen1b5` | Qwen-1.5B | 33,000 | depth 0-5 |
| `exp_code_qwen7b` | Qwen-7B | 33,000 | depth 0-5 |
| `exp_code_qwen1b5_pythia_scorer` | Qwen-1.5B (Pythia cross) | 33,000 | depth 0-5 |
| `code_python_seed` | Seed 数据 | - | - |

每个 depth 级别 5,500 样本（33,000 / 6）。Code domain 样本量大于 arXiv（5,500 vs 2,200/depth）。

## 3. 数据格式

**三个 domain 完全一致**，均为：
- `depth_0.jsonl` ~ `depth_5.jsonl`（原始文本）
- `features.csv`（15 列统计特征：`doc_id, depth, surp_mean, surp_std, surp_skew, surp_kurt, surp_d1_mean, surp_d1_std, surp_d1_skew, surp_d2_mean, surp_d2_std, ttr, hapax_ratio, self_bleu, freq_kurtosis, freq_entropy, low_freq_ratio`）

Wiki/arXiv/Code 的 features.csv schema 完全相同，**可直接复用 DeBERTa 脚本**。

## 4. DeBERTa 脚本

现有 4 个脚本（`/root/autodl-tmp/gen-depth-contamination/scripts/`）：
- `run_deberta_upperbound.py` — upper bound 实验
- `run_deberta_cross_transfer.py` — cross-model transfer
- `run_deberta_c4_1b5.py` — C4 domain 专用
- `analyze_deberta_results.py` — 结果分析

## 5. 已有 DeBERTa 结果

- `exp_deberta_upperbound/` — **仅 wiki**（wiki_pythia, wiki_olmo, wiki_qwen7b, wiki_llama8b, wiki_mistral7b）
- `deberta_cross_transfer/` — **仅 wiki 跨模型**（wiki_X → wiki_Y，13 对）
- `exp_deberta_c4_1b5/` — C4 domain（qwen_rw, qwen_cont256）

**arXiv 和 Code 的 DeBERTa 实验尚未运行。** arXiv 已有的结果（exp_024_arxiv, exp_025_pythia_arxiv, exp_026_arxiv_filtering）是 feature-based 分类器结果（pairwise AUC/JSD/ordinal），不是 DeBERTa。Code 的结果目录也是 feature-based 的。

---
