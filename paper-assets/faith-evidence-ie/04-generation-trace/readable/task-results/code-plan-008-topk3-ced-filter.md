# code plan 008 topk3 ced filter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_008_topk3_ced_filter_20260515T135350_result.json`
- **Structured JSON:** [`c8601c8b2ae93f2cc17b.json`](../../sessions/c8/c8601c8b2ae93f2cc17b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| | 样本数 | ced_score mean | median | min | max |
|---|---|---|---|---|---|
| 过滤前 | 8037 | 0.6205 | 0.6354 | 0.0000 | 0.9970 |
| 过滤后 | **7942** | 0.6280 | 0.6387 | 0.0013 | 0.9970 |

- 去除 **95** 个 `ced_score=0` 样本（占 1.18%）
- 过滤脚本: `/root/autodl-tmp/scripts/filter_topk3_ced.py`
- 输出数据: `/root/autodl-tmp/rsft_filtered_topk3_ced_filtered/rsft_train.jsonl`（7942 samples）

注：数据中字段名是 `ced_score`（非 `ced_reward`），两个变体数据已就绪：
- topk3_all: `/root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl`（8037）
- topk3_ced_filtered: `/root/autodl-tmp/rsft_filtered_topk3_ced_filtered/rsft_train.jsonl`（7942）

---
