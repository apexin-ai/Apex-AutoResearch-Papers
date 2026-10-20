# analyze reeval rsft topk3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_reeval_rsft_topk3_20260516T001310_result.json`
- **Structured JSON:** [`41a71992640ded24b462.json`](../../sessions/41/41a71992640ded24b462.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。结论：**negative** — RSFT top_k=3 的 rel_f1=0.4454 虽超过 SFT baseline (+0.04)，但低于 CED RSFT top_k=1 (~0.46)，说明增大 top_k 引入了更多噪声样本，反而损害关系抽取性能。top_k=1 的 CED 过滤策略更优。

---
