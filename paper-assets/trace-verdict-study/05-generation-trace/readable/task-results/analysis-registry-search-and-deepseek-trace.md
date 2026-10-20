# analysis registry search and deepseek trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_registry_search_and_deepseek_trace_20260518T235132_result.json`
- **Structured JSON:** [`eccfddfa6c2aa855523a.json`](../../sessions/ec/eccfddfa6c2aa855523a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部获取。汇总如下：

---

## ALL tail-512 / tail related experiments (Registry)

| exp_id | status | conclusion | accuracy |
|---|---|---|---|
| codellama13b_full_trace_tail1024_seed42 | DONE | failed | N/A |
| codellama13b_full_trace_tail1024_seed42_v2 | DONE | negative | 0.876 |
| codellama13b_full_trace_tail1024_seed42_v3 | DONE | success | N/A |
| codellama13b_full_trace_tail2048_seed42 | DONE | failed | N/A |
| codellama13b_full_trace_tail2048_seed42_v2 | DONE | negative | N/A |
| codellama13b_full_trace_tail2048_seed42_v3 | DONE | negative | N/A |
| codellama13b_full_trace_tail256_seed42 | DONE | success | 0.779 |
| codellama13b_full_trace_tail384_seed42 | DONE | negative | 0.8269 |
| codellama13b_full_trace_tail512_seed123 | DONE | success | 0.9824 |
| **codellama13b_full_trace_tail512_seed42** | **QUEUED** | — | N/A |
| codellama13b_full_trace_tail512_seed456 | ALLOCATED | — | N/A |
| deepseek_full_trace_tail1024_seed42 | DONE | success | 0.9647 |
| deepseek_full_trace_tail2048_seed42 | DONE | success | 0.9496 |
| deepseek_full_trace_tail256_seed42 | DONE | success | 0.7639 |
| deepseek_full_trace_tail384_seed42 | DONE | success | 0.807 |
| deepseek_full_trace_tail512_seed123 | DONE | failed | N/A |
| deepseek_full_trace_tail512_seed123_v2 | DONE | success | 0.9504 |
| **deepseek_full_trace_tail512_seed42** | **DONE** | **success** | **0.939** |
| deepseek_full_trace_tail512_seed456 | DONE | success | 0.9605 |
| full_trace_tail256_seed42 | DONE | negative | 0.789 |
| full_trace_tail_1024_seed42 | DONE | success | 0.9647 |
| full_trace_tail_256_seed42 | DONE | negative | 0.7748 |
| **full_trace_tail_512_seed42** | **DONE** | **success** | **0.936** |
| full_trace_tail_seed42 | DONE | success | 0.973 |
| qwen15b_full_trace_tail1024_seed42 | DONE | success | 0.966 |
| qwen15b_full_trace_tail2048_seed42 | DONE | success | 0.979 |
| qwen15b_full_trace_tail256_seed42 | DONE | negative | 0.726 |
| qwen15b_full_trace_tail384_seed42 | DONE | negative | 0.7361 |
| qwen15b_full_trace_tail512_seed123 | DONE | success | 0.9765 |
| qwen15b_full_trace_tail512_seed42 | DONE | success | 0.956 |
| qwen15b_full_trace_tail512_seed456 | DONE | success | 0.9672 |
| qwen7b_full_trace_tail384_seed42 | DONE | success | 0.798 |
| qwen7b_full_trace_tail512_seed123 | DONE | success | 0.9597 |
| qwen7b_full_trace_tail512_seed42 | PREPARING | — | N/A |
| qwen7b_full_trace_tail512_seed456 | DONE | success | 0.9765 |

---

## DEEPSEEK TAIL-512 SEED42 来源追查

从服务器 eval_results.json 确认的实际 accuracy 值：

| 实验 | accuracy | 文件路径 |
|---|---|---|
| deepseek_full_trace_tail512_seed42 | **93.95%** (0.9395) | `.../deepseek_full_trace_tail512_seed42/final/eval_results.json` |
| deepseek_full_trace_tail512_seed456 | 96.05% (0.9605) | `.../deepseek_full_trace_tail512_seed456/final/eval_results.json` |
| deepseek_full_trace_tail512_seed123_v2 | 95.04% (0.9504) | `.../deepseek_full_trace_tail512_seed123_v2/final/eval_results.json` |

**关键发现 — 93.61% 的真正来源：**

`grep -r "0.9361"` 命中了两个位置：
1. `deepseek_full_trace_tail1024_seed42` — 但这是 **fail_f1=0.9362**，不是 accuracy（accuracy=0.9647）
2. **`full_trace_tail_512_seed42`**（无模型前缀，Qwen-7B）— **accuracy = 0.9361**

**结论：93.61% 来自 `full_trace_tail_512_seed42`（Qwen-7B），不是 DeepSeek。** DeepSeek tail-512 seed42 的真实 accuracy 是 **93.95%**。

---
