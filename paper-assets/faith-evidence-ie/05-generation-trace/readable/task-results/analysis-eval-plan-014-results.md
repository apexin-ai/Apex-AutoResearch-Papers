# analysis eval plan 014 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_plan_014_results_20260515T183729_result.json`
- **Structured JSON:** [`f7897983555e85fde95f.json`](../../sessions/f7/f7897983555e85fde95f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。完整对比：

| 指标 | SFT baseline (with evidence) | SFT no-evidence | 差异 |
|------|-----|------|------|
| **rel_f1** | 0.4057 | **0.4893** | **+0.0836 (+20.6%)** |
| rel_precision | — | 0.4884 | — |
| rel_recall | — | 0.4902 | — |
| evi_f1 | 0.7979 | 0.0000 | (设计如此) |
| format_ok_rate | — | 99.2% | — |
| n_truncated | — | 298/985 | — |
| inference_time | — | 4103.8s | — |

**结论：evidence 生成显著拖累了关系抽取性能。** 去掉 evidence 后 rel_f1 从 0.4057 跃升到 0.4893，提升 20.6%。这说明在当前 SFT 框架下，让模型同时学习关系抽取和证据生成两个任务存在明显的 multi-task interference——生成证据句子消耗了模型容量，反而损害了核心的关系抽取能力。

---
