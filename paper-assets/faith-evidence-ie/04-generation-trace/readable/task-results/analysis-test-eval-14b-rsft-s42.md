# analysis test eval 14b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_14b_rsft_s42_20260521T152925_result.json`
- **Structured JSON:** [`dbd33da52514bc64215f.json`](../../sessions/db/dbd33da52514bc64215f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中没有 precision/recall 分项，没有 W&B URL。

```
=== METRICS ===
ign_f1: 0.3849
f1: 0.3849
evi_f1: 0.2688
evi_f1_tp: 0.6025
edcr: 0.7865
truncation_rate: 13.40% (67/500)
=== END METRICS ===

=== NOTES ===
1. WARNING: train_annotated.json not found, Ign-F1 = F1 — test set 没有 train_annotated.json，无法计算 ignore 版本的 F1（排除训练集中出现的关系），所以 Ign-F1 直接等于 F1。这是 test set 评估的正常行为，最终以 CodaLab 提交结果为准。
2. Test F1=0.3849 相比 dev ign_f1=0.5896 有显著下降（-0.2047），可能原因：(a) test set 分布与 dev 差异大；(b) 本地 F1 计算与 CodaLab 官方评估可能不同——需提交 codalab_submission.json 到 CodaLab 获取官方分数。
3. CodaLab 文件已生成：11235 条转换成功，225 条因关系类型跳过，349 条因实体跳过。
4. Format OK: 499/500（1 篇文档格式解析失败）。
5. 无 W&B URL。
6. 推理耗时 5h18m，平均 38.17s/doc。
=== END NOTES ===
```

---
