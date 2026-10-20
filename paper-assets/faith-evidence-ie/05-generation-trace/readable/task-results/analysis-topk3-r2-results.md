# analysis topk3 r2 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_topk3_r2_results_20260515T132412_result.json`
- **Structured JSON:** [`4f8e89b722b00950ee71.json`](../../sessions/4f/4f8e89b722b00950ee71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**结果摘要：** `mvp2_rsft_ced_scoring_topk3_r2` 成功完成。

- **8037 samples** selected（top_k=1 的 2718 的 2.96 倍），覆盖 2691/2716 docs（99.1%）
- Selected 均值质量：CED=0.621（比 topk1 低 4.7pp）、F1=0.576、combined=0.679
- 核心 trade-off：数据量 3x vs 质量降 ~5pp CED
- 输出路径：`/root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl`

---
