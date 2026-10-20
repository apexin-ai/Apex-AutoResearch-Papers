# analysis format metrics unified

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_format_metrics_unified_20260517T102712_result.json`
- **Structured JSON:** [`93a3b1c7252f09d6c567.json`](../../sessions/93/93a3b1c7252f09d6c567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Metric | C1 Δ (Gen0→2) | C5 Δ (Gen0→2) |
|--------|---------------|---------------|
| per_response_ttr | **-0.0129** | -0.0223 |
| trigram_repetition_rate | **+0.0159** | +0.0213 |
| opening_entropy | **-0.0051** | -0.0126 |
| near_duplicate_start_rate | +0.0085 | **+0.0045** |
| opening_unique_ratio | -0.0045 | **-0.0040** |

两个条件都出现 format diversity 退化。C5 (random) 在 TTR、trigram repetition、opening entropy 三个 metric 上退化幅度更大（分别高 74%、34%、147%），说明 ArmoRM curation 有适度的 format diversity 保持效果。唯一例外是 `near_duplicate_start_rate`，C1 增长略多，可能因为 ArmoRM 偏好特定开头模式。

---
