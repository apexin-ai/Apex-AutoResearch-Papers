# ssh data download arena mt

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_data_download_arena_mt_20260521T234538_result.json`
- **Structured JSON:** [`2ca638aa80cbad2d9e57.json`](../../sessions/2c/2ca638aa80cbad2d9e57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据下载和整理完成。汇总如下：

```
=== Arena-Hard (v0.1) ===
Prompts: 500 条
  格式: {uid, category, cluster, prompt}
  转换后: prompts.jsonl — {id, prompt, cluster}
Models with responses: [gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613]
  转换后: responses/{model}.jsonl — {id, response}
Model judgments: gpt-4-1106-preview 评判 gpt-3.5-turbo-0125 和 gpt-4-0613
License: Apache 2.0
Data size: 21MB

=== MT-Bench ===
Questions: 80 条 (8 categories: coding, extraction, humanities, math, reasoning, roleplay, stem, writing)
  格式: {question_id, category, turns: [str, str]} (multi-turn, 2 turns)
Reference answers: 30 条 (gpt-4, 仅覆盖需要参考答案的 categories)
  格式: {question_id, answer_id, model_id, choices: [{index, turns: [str, str]}], tstamp}
Judge prompts: judge_prompts.jsonl (FastChat 原始 judge prompt 模板)
Models with answers: 无公开 model answer（FastChat repo 不提供，需自行生成）
Data size: 112KB
```

**数据路径:**
- `/root/gated_mfrm_judge_bias/data/arena_hard/` — prompts.jsonl, responses/, model_answer/, model_judgment/
- `/root/gated_mfrm_judge_bias/data/mt_bench/` — question.jsonl, reference_answer/, judge_prompts.jsonl

---
