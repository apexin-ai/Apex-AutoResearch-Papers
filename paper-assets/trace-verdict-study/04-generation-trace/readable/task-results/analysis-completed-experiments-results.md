# analysis completed experiments results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_completed_experiments_results_20260518T154927_result.json`
- **Structured JSON:** [`0c4c6c86d698485af5e7.json`](../../sessions/0c/0c4c6c86d698485af5e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇总

| 实验 | Accuracy | 假设范围 | 结论 |
|---|---|---|---|
| **qwen15b_tail512_seed123** | **97.65%** [96.8-98.5] | 93-97% | **success** — seed robustness confirmed, seed123 甚至高于 seed42 (95.6%) 2pp |
| **codellama13b_tail384_seed42** | **82.7%** [80.7-84.7] | 85-95% | **negative** — label_only_loss 未能在 tail-384 提供显著优势 |

CodeLlama-13B tail-384 的 82.7% 与 DeepSeek (80.7%)、Qwen-7B (79.8%) 处于同一水平，fail_recall 仅 51.6%。384 tokens 的信号不足是 universal 的，label_only_loss 和更大模型容量都无法补偿。

---
