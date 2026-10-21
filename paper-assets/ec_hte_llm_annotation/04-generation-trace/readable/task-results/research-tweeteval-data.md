# research tweeteval data

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tweeteval-data_20260520T214120_result.json`
- **Structured JSON:** [`3a19f6e313a933ca3c3a.json`](../../sessions/3a/3a19f6e313a933ca3c3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告已写入 `/home/ubuntu/ec_hte_llm_annotation/results/tweeteval_exploration.md`。

核心结论：

- **首选 sentiment**（N=45,615）：样本量远超需求，子群变量丰富（hashtag 23%、mention 33%、长度三分组均匀），3类标签结构清晰
- **次选 hate / offensive**（N=9K-12K）：样本量充足，涉及社会价值判断，LLM 可能产生有意义的 HTE
- **Stance 子任务不推荐**：所有 5 个 stance 子任务的 N < 1,000，子群划分后每 cell 不足 100 条，统计功效不足；且子群结构贫乏（hashtag 接近 100%，无 URL/emoji）

---
