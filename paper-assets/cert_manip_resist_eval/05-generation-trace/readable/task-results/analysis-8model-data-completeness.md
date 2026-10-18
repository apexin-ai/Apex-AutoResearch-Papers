# analysis 8model data completeness

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8model-data-completeness_20260522T124705_result.json`
- **Structured JSON:** [`e7dc2a395d270c423a1d.json`](../../sessions/e7/e7dc2a395d270c423a1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data exploration complete. Here's the full report.

---

## Individual Scoring 数据完整性报告

### 关键发现：本地模型不匹配

现有数据中的 6 个本地模型是 **大模型集**，与目标 8 模型中的 6 个小模型不一致：

| 现有本地模型 | 目标本地模型 | 匹配？ |
|---|---|---|
| qwen2.5-72b | Qwen2.5-7B | ✗ |
| llama3.1-70b | Llama-3.1-8B | ✗ (不同规模) |
| mistral-large | Mistral-7B-v0.3 | ✗ |
| qwen2.5-32b | Qwen2.5-3B | ✗ |
| qwen2.5-14b | Llama-3.2-3B | ✗ |
| **llama3.1-8b** | Mistral-Nemo-12B | ✗ |

`llama3.1-8b` 在现有数据中有完整 14/14 条件（在 checkpoint 文件里），与目标列表中的 Llama-3.1-8B 匹配。其余 5 个目标本地模型 **无任何 scoring 数据**。

### 逐模型完整性

| 模型 | 有数据条件数 | 缺失条件 |
|---|---|---|
| **Qwen2.5-7B** | 0/14 | 全部缺失 |
| **Llama-3.1-8B** | 14/14 ✅ | 无（在 `_step2v3_checkpoint.json` / `_taxonomy_checkpoint.json`） |
| **Mistral-7B-v0.3** | 0/14 | 全部缺失 |
| **Qwen2.5-3B** | 0/14 | 全部缺失 |
| **Llama-3.2-3B** | 0/14 | 全部缺失 |
| **Mistral-Nemo-12B** | 0/14 | 全部缺失 |
| **claude-3-haiku** | 14/14 ✅ | 无（14 个独立 JSON 文件，各 300 samples） |
| **gpt-4o** | 9/14 ⚠️ | 缺 5 个：arc_challenge × {sycophancy, score_manipulation, verbosity_bias, position_bias, authority_bias} |

### 数据位置

- **本地模型**: 嵌套在 checkpoint 文件中
  - `_step2v3_checkpoint.json` (5.2MB) — clean + prompt_injection/sycophancy/score_manipulation
  - `_taxonomy_checkpoint.json` (5.8MB) — clean + verbosity_bias/position_bias/authority_bias
- **API 模型**: `artifacts/results/plan001/individual_scores/` 下独立文件
  - 命名格式: `{model}__{dataset}__{condition}.json`

### 数据格式兼容性

| 字段 | 本地模型 (checkpoint) | API 模型 (individual files) |
|---|---|---|
| winner | ✓ | ✓ |
| score_a / score_b | ✓ | ✓ |
| reasoning | ✓ | ✓ |
| judge_id | ✓ | ✓ |
| _parse_method | ✗ | ✓ |
| latency_ms | ✗ | ✓ |
| input/output_tokens | ✗ | ✓ |
| **结构** | 嵌套: `{clean_scores: {dataset: {model: [...]}}}` | 扁平: `{condition, scores: [...], accuracy, n_samples}` |

核心评分字段（winner, score_a, score_b, reasoning, judge_id）**兼容**，API 数据多了延迟/token 统计字段，结构不同但可转换。

### 结论

- **完整数据模型**: 仅 2 个 — `Llama-3.1-8B` + `claude-3-haiku`
- **部分数据模型**: 1 个 — `gpt-4o` (9/14，缺 arc_challenge 的 5 个攻击条件)
- **无数据模型**: 5 个 — Qwen2.5-7B, Mistral-7B-v0.3, Qwen2.5-3B, Llama-3.2-3B, Mistral-Nemo-12B
- 需要运行 **5×14 + 5 = 75 个条件** 的 scoring 才能补齐全部 8 模型数据

---
