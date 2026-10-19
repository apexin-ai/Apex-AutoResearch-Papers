# research data availability

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-availability_20260518T044851_result.json`
- **Structured JSON:** [`dfd9ffbd28cca4954e8e.json`](../../sessions/df/dfd9ffbd28cca4954e8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/data_availability_report.md`。

核心发现：

- **TurnWiseData**：截至今日未公开发布，无法使用。论文未提供任何下载链接，HuggingFace 上也搜不到。
- **Microsoft/lost_in_conversation**：公开可用（HuggingFace + GitHub），600 条 sharded instructions，6 个任务，每条 2-8 shards/turns，有完整评估框架。
- **MVP 推荐**：lost_in_conversation 是唯一可用选项。主要局限是轮数上限仅 8 轮（低于期望的 20+），且是信息分片而非自然对话。建议 MVP 先用 code + math 任务子集验证核心假设，筛选 shard >= 5 的样本。

---
