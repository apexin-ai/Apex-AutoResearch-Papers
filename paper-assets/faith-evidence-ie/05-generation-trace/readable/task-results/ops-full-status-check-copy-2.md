# ops full status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_20260516T101244_result.json`
- **Structured JSON:** [`12034bf5307cf268e958.json`](../../sessions/12/12034bf5307cf268e958.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。

```
GPU 状态:
  cuda:0  28.9/32.6 GB (95%)  — plan_006_qwen3_8b_no_evidence_sft (训练)
  cuda:1  11.1/32.6 GB (57%)  — plan_002_test_eval_s44_r2 (推理)
  cuda:2   5.5/32.6 GB (44%)  — plan_006_qwen3_1_7b_no_evidence_eval (推理)
  cuda:3  18.5/32.6 GB (64%)  — plan_006_qwen3_8b_sft_eval (推理)

仍在运行:
  - plan_006_qwen3_8b_no_evidence_sft: 403/570 steps (71%), ~16min 剩余
  - plan_006_qwen3_1_7b_no_evidence_eval: 117/247 batches (47%), ~54min 剩余
  - plan_006_qwen3_8b_sft_eval: 145/247 batches (59%), ~56min 剩余
  - plan_002_test_eval_s44_r2: 123/250 batches (49%), ~110min 剩余

已完成实验 (ANALYZING → DONE, registry 已更新):
  - reeval_ced_s42:      Ign-F1=0.4423, Rel-F1=0.4517, Evi-F1=0.8175
  - reeval_ced_s44:      Ign-F1=0.4511, Rel-F1=0.4621, Evi-F1=0.8050
  - reeval_flat_nli_s42: Ign-F1=0.4448, Rel-F1=0.4535, Evi-F1=0.8039

空闲 GPU: 无（4 张全部占用）
```

---
