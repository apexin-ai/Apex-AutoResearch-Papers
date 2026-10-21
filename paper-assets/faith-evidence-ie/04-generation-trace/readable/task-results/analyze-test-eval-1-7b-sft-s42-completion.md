# analyze test eval 1 7b sft s42 completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_1_7b_sft_s42_completion_20260522T023133_result.json`
- **Structured JSON:** [`1e1641b109b77afd6429.json`](../../sessions/1e/1e1641b109b77afd6429.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 不存在（可能已在之前的 session 中删除或未在本 session 创建）。

## 结果汇报

**test_eval_1_7b_sft_s42** — Qwen3-1.7B SFT s42, Re-DocRED test set

| 指标 | 值 |
|------|------|
| **Ign-F1** | **0.2579** |
| F1 | 0.2579 |
| Precision | 0.3977 |
| Recall | 0.1908 |
| Evi-F1 (DREEAM/joint) | 0.1975 |
| Evi-F1 (TP) | 0.5918 |
| EDCR | 0.8504 |
| Predictions | 26,863 |
| TP / Pred / Gold | 3,310 / 8,323 / 17,350 |

**格式合规**: 500/500 (100%), field_compliance 100%, evidence_format 98%

**Truncation**: 409/500 (81.8%) — 高截断率，1.7B 模型输出能力有限

**CodaLab submission**: 已生成，8,020 converted, 40 skipped (rel), 1,093 skipped (entity)

**对比 dev**: dev 3-seed mean ign_f1 = 0.4464, test ign_f1 = 0.2579, 差距约 **18.9pp**。这在预期范围内（~20pp），但注意 ign_f1 == f1（因为 test set 没有 train_annotated.json 做 ignore 过滤，这是正常的——CodaLab 提交后会得到官方 ign_f1）。

---
