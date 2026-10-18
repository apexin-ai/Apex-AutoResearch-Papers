# code api test and scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_api_test_and_scoring_20260521T050355_result.json`
- **Structured JSON:** [`db7c4d270a466e14c121.json`](../../sessions/db/db7c4d270a466e14c121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## API 测试结果

| Model | Status |
|-------|--------|
| GPT-4o | **200 OK** ✓ |
| Claude | 不可用（代理仅支持 OpenAI 模型） |
| Gemini | 不可用（同上） |

## Scoring 产出（全部完成）

### GPT-4o Verbosity Pairwise（100 条）
- `data/pairwise_results_gpt4o_verbosity.jsonl` ✓
- **Consistency**: 73.7%（73/99）
- **Verbose win rate**: 86.3%（63/73），**p < 0.000001**
- CI [76.6%, 92.4%]
- 双向分析：verbose→concise 80.8%（p=0.002），concise→verbose 89.4%（p<0.000001）
- NLI≥0.90 子集：86.7%（p<0.000001）

### GPT-4o Register Pairwise（100 条）
- `data/pairwise_results_gpt4o_register.jsonl` ✓
- **Consistency**: 49.5%（49/99）— 很低
- **Academic win rate**: 63.3%（31/49），**p = 0.085**（不显著）
- CI [49.3%, 75.3%]
- 方向分析：academic→conversational 78.3%（p=0.011），conversational→academic 50.0%（p=1.0）— 典型 originality bias
- NLI≥0.90：64.4%（p=0.072）

### GPT-4o Likert Scoring（各 100 条）
- `data/scored_gpt4o_verbosity.jsonl` ✓（100 条）
- `data/scored_gpt4o_register.jsonl` ✓（100 条）

**注**：脚本中移除了 `extra_body={"chat_template_kwargs": {"enable_thinking": False}}`，该参数仅适用于 Qwen3 本地 vLLM，OpenAI API 不支持。

---
