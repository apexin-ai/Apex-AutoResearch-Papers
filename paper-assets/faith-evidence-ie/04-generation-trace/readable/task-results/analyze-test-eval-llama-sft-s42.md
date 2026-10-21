# analyze test eval llama sft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_llama_sft_s42_20260521T231044_result.json`
- **Structured JSON:** [`c108801cbe4c19aad294.json`](../../sessions/c1/c108801cbe4c19aad294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃 cron，无需删除（可能在上一个 session 中已清除或未在本 session 创建）。

---

## 诊断结果：test_eval_llama_sft_s42 — 成功

**判断依据**：推理 500/500 完成，predictions.json + codalab_submission.json + test_summary.json 均已生成，日志无错误。

### 完整 Metrics

| 指标 | 值 |
|------|-----|
| **Ign-F1** | **0.3420** |
| F1 | 0.3420 |
| Precision | 0.4698 |
| Recall | 0.2689 |
| Evi-F1(DREEAM/joint) | 0.2409 |
| Evi-F1(TP) | 0.5819 |
| EDCR | 0.8403 |
| Format OK | 490/500 |
| Truncated | 327/500 |
| Predictions | 23,821 |
| CodaLab converted | 9,502 |

**注**：Ign-F1 = F1 因 test set 无 train_annotated.json 去重。

### GPU 状态

| GPU | 显存占用 |
|-----|---------|
| 0 | 6,071 MiB |
| 1 | 32,503 MiB |
| **2** | **0 MiB** |
| **3** | **0 MiB** ✓ |

cuda:3 已释放。

### Registry

已更新为 `DONE / success`，metrics 已写入。

---
