# infra plan003 humaid recount

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-humaid-recount_20260520T231106_result.json`
- **Structured JSON:** [`043419b3305078fc2c87.json`](../../sessions/04/043419b3305078fc2c87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9 个文件统计结果：

| File | Total | pred_valid | gold_valid | errors | 402_errors | Status |
|---|---|---|---|---|---|---|
| deepseek_few-shot-3.jsonl | 1500 | 1345 | 1500 | 155 | 0 | WARN |
| deepseek_few-shot-5.jsonl | 1500 | 1237 | 1500 | 263 | 0 | WARN |
| deepseek_zero-shot.jsonl | 1500 | 1500 | 1500 | 0 | 0 | OK |
| llama4_few-shot-3.jsonl | 1500 | 1498 | 1500 | 2 | 0 | OK |
| llama4_few-shot-5.jsonl | 1500 | 1471 | 1500 | 29 | 0 | WARN |
| llama4_zero-shot.jsonl | 1500 | 1500 | 1500 | 0 | 0 | OK |
| qwen3_few-shot-3.jsonl | 1500 | 1423 | 1500 | 77 | 77 | WARN |
| **qwen3_few-shot-5.jsonl** | **1500** | **0** | **1500** | **1500** | **1500** | **FAIL** |
| qwen3_zero-shot.jsonl | 1500 | 1500 | 1500 | 0 | 0 | OK |

要点：
- 全部 9 个文件各 1500 行，gold_label 全部有效
- 3 个文件完全无错（deepseek_zero-shot, llama4_zero-shot, qwen3_zero-shot）
- **qwen3_few-shot-5 全军覆没**：1500 条全是 402 错误，pred_valid = 0
- deepseek 的 few-shot 错误不是 402，是其他类型（可能解析/格式错误）
- llama4_few-shot-5 有 29 条错误，llama4_few-shot-3 仅 2 条

---
