# ssh p0 step1 rerun exp002 9models

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_step1_rerun_exp002_9models_20260522T123351_result.json`
- **Structured JSON:** [`5ae8693b02f8787320d5.json`](../../sessions/5a/5ae8693b02f8787320d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果对比：

| 指标 | 旧版 (2 target models) | 新版 (8 target models) |
|---|---|---|
| **Judgments** | — | 12,122 (from 10 files) |
| **Judges** | 10 | 9 |
| **Items** | 493 | 317 |
| **Target models** | 2 (gpt-3.5-turbo-0125, gpt-4-0613) | 8 (gemma-2-9b, gpt-3.5-turbo-0125, gpt-4-0613, gpt-4o, gpt-4o-mini, llama-3.3-70b, qwen2.5-72b, qwen3-8b) |
| **e_i mean** | 0.236 | 0.212 |
| **e_i median** | 0.126 | 0.125 |
| **e_i std** | 0.247 | 0.236 |
| **e_i max** | 1.0 | 1.0 |
| **High exposure (e_i=1.0)** | 9 items | 2 items |
| **Source coverage** | 2 sources/item | 2 sources/item (A+C, no Source B) |

注意两点：

1. **Items 从 493 降到 317** — 新的 judgment 数据覆盖的 item 集合比旧版小。可能旧版用了 `--arena-hard-dir` 补充数据，或者新 judges 只覆盖了部分 items。需确认这是否符合预期。

2. **8 个 target models 而非 9 个** — exp001/results 有 9 个 judge 子目录（对应 9 个 judge model），但 target models 是 judgment 数据中的 `model_a` 字段去重后的结果。reference model (gpt-4-0314) 被排除，剩 8 个 target models。这说明 judge 目录名 ≠ target model，9 个 judge 用来评判 8 个 target model 的表现。

旧结果已备份到 `results_2model_backup/`。

---
