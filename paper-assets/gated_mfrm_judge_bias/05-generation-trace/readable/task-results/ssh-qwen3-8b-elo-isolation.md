# ssh qwen3 8b elo isolation

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen3-8b-elo-isolation_20260524T095450_result.json`
- **Structured JSON:** [`6bb59a5033c6ae898938.json`](../../sessions/6b/6bb59a5033c6ae898938.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verified. Also note `run_n17_downstream.py` uses `bdt.ARENA_ELO` (importing from `bootstrap_delta_tau`), so it automatically picks up the change.

## 产出

### 任务 1: ARENA_ELO 隔离

**修改的文件（从 ARENA_ELO 中移除 qwen3-8b）：**
| 文件 | ARENA_ELO 改动 | ESTIMATED_ELO 新增行 |
|------|--------------|-------------------|
| `exp003/analyze_003b.py` | 删除 `"qwen3-8b": 1105` → 7 entries | line 65 |
| `exp003/bootstrap_delta_tau.py` | 删除 `"qwen3-8b": 1170` → 17 entries | line 55 |
| `exp003/evaluation.py` | 删除 `"qwen3-8b": 1170` → 17 entries | line 46 |

`run_n17_downstream.py` 通过 `import bootstrap_delta_tau as bdt` 使用 `bdt.ARENA_ELO`，无需单独改。`bootstrap_delta_tau.py` 中原有的 `EXCLUDE_MODELS = ["qwen3-8b"]` 仍保留作为双重保险，但现在 qwen3-8b 已不在 ARENA_ELO 中，τ 计算不可能匹配到它。

### 任务 2: Judgment data N=17 unique target models

**19 个 unique target models：**

| # | Model |
|---|-------|
| 1 | claude-3-5-sonnet-20241022 |
| 2 | claude-3-haiku-20240307 |
| 3 | claude-3-opus-20240229 |
| 4 | gemma-2-27b-it |
| 5 | gemma-2-9b-it |
| 6 | gpt-3.5-turbo-0613 |
| 7 | gpt-4-0314 |
| 8 | gpt-4-0613 |
| 9 | gpt-4-turbo-2024-04-09 |
| 10 | gpt-4o-2024-05-13 |
| 11 | gpt-4o-mini-2024-07-18 |
| 12 | llama-3-70b-instruct |
| 13 | llama-3-8b-instruct |
| 14 | llama-3.1-70b-instruct |
| 15 | llama-3.3-70b-instruct |
| 16 | mistral-large-2407 |
| 17 | mixtral-8x22b-instruct-v0.1 |
| 18 | qwen2.5-72b-instruct |
| 19 | qwen3-8b |

注意：数据中有 19 个而非 17 个 unique target model（命名 N=17 可能指 ARENA_ELO 中有 Arena ranking 的 17 个，加上 qwen3-8b 和 gpt-3.5-turbo-0613 vs 0125 的版本差异）。另外 `gpt-3.5-turbo-0613`（数据中）vs `gpt-3.5-turbo-0125`（ARENA_ELO 中）和 `llama-3.3-70b-instruct`（数据中）vs `llama-3.3-70b`（ARENA_ELO 中）存在命名不匹配，需要 `ARENA_NAME_MAPPING` 覆盖。

---
