# code verify condition truncation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_condition_truncation_20260518T145556_result.json`
- **Structured JSON:** [`7b0bb2f9b262c4f8b880.json`](../../sessions/7b/7b0bb2f9b262c4f8b880.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**`full_trace_tail` ≠ `full_trace_tail_512`**，截断逻辑不同：

| | `full_trace_tail` | `full_trace_tail_512` |
|---|---|---|
| **trace 截断上限** | 无固定上限 | **512 tokens** (`MAX_TRACE_TOKENS = 512`) |
| **截断策略** | 先算 `trace_budget = MAX_SEQ_LENGTH - overhead`，保留 trace 尾部 budget 个 token | 先将 trace 硬截到 512 token（取尾部），再检查整体是否超 2048，若超则进一步缩小 |
| **实际 trace 长度** | 取决于 code+test 的长度，budget 可能远大于 512（code/test 短时 trace 可用上千 token） | 最多 512 token，无论 code/test 多短 |

文件大小也印证了差异：`full_trace_tail_train.jsonl` = 28MB vs `full_trace_tail_512_train.jsonl` = 10.6MB（行数相同都是 4720），说明 `full_trace_tail` 平均保留的 trace 远多于 512 tokens。

---
