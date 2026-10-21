# ssh list target models

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_list-target-models_20260524T095258_result.json`
- **Structured JSON:** [`9c8157952e067351fc3a.json`](../../sessions/9c/9c8157952e067351fc3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，以下是完整结果。

---

## 1. Judgment Data 中的 Target Models（model_a）— 18 个

| # | model_a (judgment data) |
|---|------------------------|
| 1 | claude-3-5-sonnet-20241022 |
| 2 | claude-3-haiku-20240307 |
| 3 | claude-3-opus-20240229 |
| 4 | gemma-2-27b-it |
| 5 | gemma-2-9b-it |
| 6 | gpt-3.5-turbo-0613 |
| 7 | gpt-4-0613 |
| 8 | gpt-4-turbo-2024-04-09 |
| 9 | gpt-4o-2024-05-13 |
| 10 | gpt-4o-mini-2024-07-18 |
| 11 | llama-3-70b-instruct |
| 12 | llama-3-8b-instruct |
| 13 | llama-3.1-70b-instruct |
| 14 | llama-3.3-70b-instruct |
| 15 | mistral-large-2407 |
| 16 | mixtral-8x22b-instruct-v0.1 |
| 17 | qwen2.5-72b-instruct |
| 18 | qwen3-8b |

Baseline (`model_b`): **gpt-4-0314**（固定，仅此一个）

> 实际数据有 18 个 model_a，不是 17。可能 gpt-4-0613 作为 Arena Hard 的 reference answer generator 不算 "target"，或 qwen3-8b 是后加的。

---

## 2. ARENA_ELO 条目 — 18 个

| # | ARENA_ELO key | ELO |
|---|--------------|-----|
| 1 | gpt-4o | 1300 |
| 2 | claude-3-5-sonnet-20241022 | 1298 |
| 3 | gpt-4o-mini | 1286 |
| 4 | llama-3.3-70b | 1275 |
| 5 | gpt-4-turbo-2024-04-09 | 1272 |
| 6 | qwen2.5-72b | 1269 |
| 7 | claude-3-opus-20240229 | 1262 |
| 8 | llama-3.1-70b-instruct | 1261 |
| 9 | gemma-2-27b-it | 1231 |
| 10 | llama-3-70b-instruct | 1221 |
| 11 | gemma-2-9b | 1207 |
| 12 | gpt-4-0314 | 1206 |
| 13 | claude-3-haiku-20240307 | 1195 |
| 14 | gpt-4-0613 | 1186 |
| 15 | qwen3-8b | 1170 |
| 16 | llama-3-8b-instruct | 1166 |
| 17 | mixtral-8x22b-instruct-v0.1 | 1162 |
| 18 | gpt-3.5-turbo-0125 | 1125 |

---

## 3. Name Mapping 表

`ARENA_NAME_MAPPING` 已定义在 `exp003/evaluation.py:44`。

| Judgment Data Name | ARENA_ELO Key | 状态 |
|---|---|---|
| claude-3-5-sonnet-20241022 | claude-3-5-sonnet-20241022 | 直接匹配 |
| claude-3-haiku-20240307 | claude-3-haiku-20240307 | 直接匹配 |
| claude-3-opus-20240229 | claude-3-opus-20240229 | 直接匹配 |
| gemma-2-27b-it | gemma-2-27b-it | 直接匹配 |
| gemma-2-9b-it | gemma-2-9b | 需要 mapping（已有） |
| gpt-3.5-turbo-0613 | gpt-3.5-turbo-0125 | **版本不一致！** data 是 0613，ELO 是 0125。无 mapping 条目 |
| gpt-4-0613 | gpt-4-0613 | 直接匹配 |
| gpt-4-turbo-2024-04-09 | gpt-4-turbo-2024-04-09 | 直接匹配（mapping 有但值同键） |
| gpt-4o-2024-05-13 | gpt-4o | 需要 mapping（已有） |
| gpt-4o-mini-2024-07-18 | gpt-4o-mini | 需要 mapping（已有） |
| llama-3-70b-instruct | llama-3-70b-instruct | 直接匹配 |
| llama-3-8b-instruct | llama-3-8b-instruct | 直接匹配 |
| llama-3.1-70b-instruct | llama-3.1-70b-instruct | 直接匹配 |
| llama-3.3-70b-instruct | llama-3.3-70b | **需要 mapping，但 ARENA_NAME_MAPPING 中无此条目** |
| mistral-large-2407 | — | **ARENA_ELO 中无此模型，无法匹配** |
| mixtral-8x22b-instruct-v0.1 | mixtral-8x22b-instruct-v0.1 | 直接匹配 |
| qwen2.5-72b-instruct | qwen2.5-72b | **需要 mapping，但 ARENA_NAME_MAPPING 中无此条目** |
| qwen3-8b | qwen3-8b | 直接匹配 |

### 问题汇总

`ARENA_NAME_MAPPING` 缺失 3 个条目：

1. **`gpt-3.5-turbo-0613` → `gpt-3.5-turbo-0125`** — 版本号不同，需要确认是否合理映射
2. **`llama-3.3-70b-instruct` → `llama-3.3-70b`** — 缺 mapping
3. **`qwen2.5-72b-instruct` → `qwen2.5-72b`** — 缺 mapping
4. **`mistral-large-2407`** — ARENA_ELO 完全没有此模型，无法匹配

---
