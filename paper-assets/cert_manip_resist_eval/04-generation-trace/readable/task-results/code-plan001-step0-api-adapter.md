# code plan001 step0 api adapter

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-step0-api-adapter_20260522T071153_result.json`
- **Structured JSON:** [`7781b8477a18b986cf5a.json`](../../sessions/77/7781b8477a18b986cf5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

**9/9 API 模型全部验证通过。**

### 产出文件
1. **`/root/cert_manip_resist_eval/src/api_judge_service.py`** — 完整的 API adapter
2. **`/root/cert_manip_resist_eval/artifacts/results/api_adapter_validation.json`** — 验证结果

### 实现要点
- 复用 `judge_service.py` 的 prompt templates 和 `_parse_judge_output`
- Rate limiting（5 RPS）+ retry（3 次 exponential backoff）
- `batch_score` 使用 `ThreadPoolExecutor(max_workers=5)` 并发
- 记录每个请求的 latency / input_tokens / output_tokens

### 修复的兼容性问题
- **gpt-5.5**: 不支持 `temperature=0`，通过 `_NO_TEMP_ZERO` 集合跳过该参数
- **gemini-2.5-pro**: 输出极长（~1020 tokens），JSON 被截断。添加 `_parse_judge_output_robust` 用正则提取截断 JSON 中的 winner/score_a/score_b 字段

### 验证结果摘要

| Model | Latency | Tokens (in+out) | Winner |
|-------|---------|-----------------|--------|
| claude-opus-4 | 14.5s | 290+134 | A |
| gpt-5.5 | 5.1s | 262+195 | A |
| gemini-2.5-pro | 11.6s | 263+1020 (repaired) | A |
| gpt-4.1 | 3.2s | 263+101 | A |
| claude-sonnet-4 | 4.3s | 290+106 | A |
| gpt-4o | 2.6s | 263+78 | A |
| gemini-2.5-flash | 3.6s | 263+88 | tie |
| gpt-4o-mini | 2.9s | 263+60 | B |
| claude-3-haiku | 2.4s | 290+109 | A |

### 成本估算
- 37,800 calls × avg 272 input + 210 output tokens ≈ **$126**（粗算，gemini-2.5-pro 的长输出拉高了平均值；排除它后实际约 $50-70）

---
