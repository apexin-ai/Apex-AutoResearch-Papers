# code ambiguity injection pipeline

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ambiguity_injection_pipeline_20260520T073711_result.json`
- **Structured JSON:** [`e37aac6c50f8c72bbeff.json`](../../sessions/e3/e37aac6c50f8c72bbeff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部完成并注册：

| 文件 | 说明 |
|------|------|
| `clause_templates.json` | 90 matched pairs (30 scopal + 30 lexical + 30 incompleteness)，零售 46 条 / 航空 44 条 |
| `injection_pipeline.py` | 主流水线，支持模板直出和 LLM 精炼两种模式 |
| `validate_clauses.py` | 验证脚本，检查 schema、数量、D004 最小增量等 |

验证结果：0 errors，33 D004 ratio warnings（均为 incompleteness 类型的预期特征——不完整条款本身就短，补全后 word ratio 偏高，但内容均只添加了解决当前缺失点的最小信息）。

LLM 精炼模式用法：`python injection_pipeline.py --output clauses.json --refine --api-key sk-... --provider anthropic`（或 `--provider openai --model gpt-5.4`）。

---
