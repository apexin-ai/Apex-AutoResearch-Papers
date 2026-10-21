# data fewshot predictions collect

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fewshot_predictions_collect_20260521T181350_result.json`
- **Structured JSON:** [`265cad7532ec3a0e9628.json`](../../sessions/26/265cad7532ec3a0e9628.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。6 个 fewshot baseline prediction 文件已从 westd-11235 下载到本地 `artifacts/fewshot_predictions/`，并注册为 artifact `art_20260521_16ea99`（type=data, tags=[fewshot, predictions, plan_020]）。

文件清单：
| 文件 | 模型 | 条件 | Shots | Accuracy |
|---|---|---|---|---|
| fewshot_gpt4o_exception_only_0shot.json | GPT-4o | exception_only | 0 | 87.98% |
| fewshot_gpt4o_exception_only_3shot.json | GPT-4o | exception_only | 3 | 86.81% |
| fewshot_gpt4o_no_trace_0shot.json | GPT-4o | no_trace | 0 | 84.45% |
| fewshot_gpt41_exception_only_0shot.json | GPT-4.1 | exception_only | 0 | 82.18% |
| fewshot_gpt41_exception_only_3shot.json | GPT-4.1 | exception_only | 3 | 81.93% |
| fewshot_gpt41_no_trace_0shot.json | GPT-4.1 | no_trace | 0 | 77.31% |

每个文件含 1190 条 per-sample predictions。SFT baseline（Qwen-7B）exception_only 精度 99.83%，远超 few-shot 最佳的 87.98%。

---
