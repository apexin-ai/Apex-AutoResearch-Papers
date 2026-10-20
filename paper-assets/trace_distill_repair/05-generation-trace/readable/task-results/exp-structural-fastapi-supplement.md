# exp structural fastapi supplement

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_structural_fastapi_supplement_20260514T204809_result.json`
- **Structured JSON:** [`b79e47e6ce65e87c9f91.json`](../../sessions/b7/b79e47e6ce65e87c9f91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

补跑完成，但两个实例各有 8/20 segments 因 API 返回 None 而 fallback 为 error。error 率 40% 偏高，可能是 API 对这些 segments（包含较大 token 的 exception_chain/call_subtree）返回空内容。

**结果汇总：**

| 实例 | Segments | Keep | Drop | Error |
|------|----------|------|------|-------|
| fastapi_1 | 20 | 1 | 11 | 8 |
| fastapi_2 | 20 | 1 | 11 | 8 |

**更新后全局统计：**
- Total instances: 38（原 36 + 2）
- Excluded: 仅剩 `fastapi_3`, `fastapi_5`
- Grand total: 491 segs, 25 keep (5.1%), 450 drop, 16 error

error segments 有 16 个（fastapi_1/2 各 8），这些都是 API 返回 None content 导致的 fallback。如果需要重跑 error segments 可以再处理，否则补跑任务已完成。

---
