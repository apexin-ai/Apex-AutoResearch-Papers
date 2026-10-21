# verify deepseek predictions

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_deepseek_predictions_20260516T011401_result.json`
- **Structured JSON:** [`8aa3ea92f599fd60c34b.json`](../../sessions/8a/8aa3ea92f599fd60c34b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个注册全部成功。汇总结果：

---

## 一致性验证结果

| 实验 | predictions n | pred_acc | eval_acc | 状态 |
|------|-------------|----------|----------|------|
| deepseek_exception_only/checkpoint-148 | 1190 | 0.9983 | 0.9983 | **MATCH** |
| deepseek_exception_only_seed123/checkpoint-148 | 1190 | 0.9143 | 0.9143 | **MATCH** |
| deepseek_exception_only_seed456/checkpoint-148 | 1190 | 0.9933 | 0.9933 | **MATCH** |
| deepseek_no_trace/final | 1190 | 0.7336 | 0.7336 | **MATCH** |
| deepseek_vota/final | 1190 | 0.8445 | 0.1597 | **MISMATCH** |
| deepseek_full_trace/checkpoint-148 | 1190 | 0.2353 | 0.2849 | **MISMATCH** |
| deepseek_full_trace/final | 1190 | 0.1059 | 0.2849 | **MISMATCH** |

## 已注册到 registry

- `deepseek_no_trace_seed42` → `.../deepseek_no_trace/final/predictions.jsonl`
- `deepseek_exception_only_seed42` → `.../deepseek_exception_only/checkpoint-148/predictions.jsonl`
- `deepseek_exception_only_seed123` → `.../deepseek_exception_only_seed123/checkpoint-148/predictions.jsonl`
- `deepseek_exception_only_seed456` → `.../deepseek_exception_only_seed456/checkpoint-148/predictions.jsonl`

## 未注册（MISMATCH）

- **deepseek_vota_seed42**: predictions 算出 84.45%，eval_results 记录 15.97%。predictions.jsonl 与 eval_results.json 可能来自不同 eval run。
- **deepseek_full_trace_seed42**: checkpoint-148 和 final 的 predictions 均与 eval_results 不一致。

## deepseek_full_trace_seed42_v3 缺失确认

**CONFIRMED MISSING** — v3 目录有 checkpoint-148/296/444/final 和 eval_results.json，但整个目录树中无任何 predictions.jsonl 文件。需要重新运行 eval 生成 predictions。

---
