# review bm25 mining code

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_bm25-mining-code_20260515T020409_result.json`
- **Structured JSON:** [`bb229288304806362124.json`](../../sessions/bb/bb229288304806362124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Review 报告已写入 `artifacts/paper_drafts/bm25_code_review.md`。

核心结论：**BM25 Phase 2 训练可以安全进行。**

关键审查结果：
- **正确性全部通过**: positive/query 排除、pool_size=50、num_negatives=7、BM25Okapi 标准参数 (k1=1.5, b=0.75)，均与其他策略一致
- **数据一致性完全匹配**: 3 seeds record counts 与 random 策略完全相同 (11308/11236/11264)，val 直接复制
- **3 个低风险 warning**: repo 目录缺失时静默 fallback、小 repo padding 用字母序、BM25 query 用原始文件内容——均不影响实验有效性
- **Overlap 分析合理**: BM25 vs random 15.5%, vs embedding 30.6%, vs dataflow 25.5%，说明 BM25 确实提供了差异化的 negative mining

---
