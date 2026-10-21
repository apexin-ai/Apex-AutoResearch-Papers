# ops verify llama rp11 final

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-llama-rp11-final_20260516T114502_result.json`
- **Structured JSON:** [`1ff47d9ed9a167648133.json`](../../sessions/1f/1ff47d9ed9a167648133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan-016-llama32-3b-rp11 完成，结论: success**

| 指标 | 值 |
|------|-----|
| 总条数 | 4416 (预期 4975) |
| 跳过 | 283 条 (empty output) |
| depth 0 | 995 (100%) |
| depth 1 | 975 (98.0%) |
| depth 2 | 912 (91.7%) |
| depth 3 | 822 (82.6%) |
| depth 4 | 712 (71.6%) |

rp=1.1 的 skip 率随 depth 递增明显——depth 越深空输出越多，总 skip 率 ~11.3%。这与 rp=1.1 抑制重复导致模型在深层续写时更容易生成空/截断输出一致。

Registry 已标记 DONE/success，cron 已删除。

---
