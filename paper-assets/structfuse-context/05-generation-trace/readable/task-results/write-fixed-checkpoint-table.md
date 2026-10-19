# write fixed checkpoint table

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_fixed-checkpoint-table_20260515T061857_result.json`
- **Structured JSON:** [`c1e78f94e9076f729e9e.json`](../../sessions/c1/c1e78f94e9076f729e9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`art_20260515_b69433` 已注册。

表格内容：
- **s43**: @500 和 @1000 两行有完整 embedding vs random 对比（Δ=+0.89pp, +1.05pp），@1500 embedding 待补
- **s42**: 3 个 step 的 random 数据已填，embedding 列标 `---`（尚未开始）
- **s44**: 未纳入表格主体（registry 无 per-step 明细），在 table note 中说明 best R@1=0.6009
- Table note 明确标注数据缺失原因和预计补全时间

需要 `\usepackage{multirow}` 和 `\usepackage{booktabs}`。

---
