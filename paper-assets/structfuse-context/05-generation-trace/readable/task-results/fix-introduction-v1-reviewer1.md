# fix introduction v1 reviewer1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_introduction-v1-reviewer1_20260515T085237_result.json`
- **Structured JSON:** [`7dacc6b274b33e9dac1e.json`](../../sessions/7d/7dacc6b274b33e9dac1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 项修正全部完成，验证通过：

| # | 修正 | 状态 |
|---|------|------|
| 1 | `jimenez2024swebench` bib entry | 已添加（ICLR 2024, 7 位作者） |
| 2 | BM25 策略删除 | four→three，contribution 列表已去除 BM25，P3 "BM25 similarity"→"lexical similarity" |
| 3 | 数字→placeholder | `+X.X pp across N random seeds (95% CI: [a, b])` + TODO 注释 |
| 4 | encoder claim | "on Qwen2.5-Coder-3B (with StarCoder2-3B validation in progress)" |
| 5 | Contribution 重排 | 1=systematic comparison, 2=CodeQL pipeline, 3=preliminary mechanistic analysis |
| 6 | zero cost 措辞 | P4→"negligible additional cost"，baseline→"requiring no gradient computation"，contributions→"without requiring gradient computation" |

注：P3 line 19 的 "zero additional inference cost" 保留未改——该处描述的是 training-time intervention 不增加推理开销，语义准确且与任务指定的 "zero additional computational cost" 不同。

---
