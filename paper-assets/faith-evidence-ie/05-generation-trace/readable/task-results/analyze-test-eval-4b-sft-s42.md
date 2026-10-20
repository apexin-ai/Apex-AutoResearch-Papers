# analyze test eval 4b sft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_4b_sft_s42_20260521T224707_result.json`
- **Structured JSON:** [`92edf0950244cf547cf0.json`](../../sessions/92/92edf0950244cf547cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已无残留，无需删除。

---

**诊断结果：test_eval_4b_sft_s42 — 成功完成**

**日志末尾**：500/500 docs 推理完毕，耗时 4h10m（30.04 s/doc），无 error/OOM。

**Metrics**：

| 指标 | 值 |
|------|-----|
| F1 | 0.2232 |
| Ign-F1 | 0.2232 |
| Precision | 0.2871 |
| Recall | 0.1826 |
| Evi-F1 (DREEAM/joint) | 0.1640 |
| Evi-F1 (TP only) | 0.6121 |
| EDCR | 0.8652 |
| Predictions | 23,993 |
| Format OK | 497/500 |
| Truncated | 323/500 |
| CodaLab converted | 10,609 |

**注意**：Ign-F1 = F1 因为 test set 无 train_annotated.json 做去重（符合预期）。

**GPU 状态**：cuda:0 已释放（0 MiB），cuda:1/2/3 被其他任务占用。

**Registry**：已更新 metrics + conclusion=success + status=DONE。Cron 无活跃任务。

---
