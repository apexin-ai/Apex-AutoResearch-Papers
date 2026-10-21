# analyze eval scalar object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-scalar-object-seed43_20260516T060326_result.json`
- **Structured JSON:** [`1c070203ff140c18b598.json`](../../sessions/1c/1c070203ff140c18b598.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success。

**结果汇总：scalar seed=43 = 10% SR**

| Task | SR |
|------|-----|
| bbq_sauce | 30% |
| chocolate_pudding | 30% |
| orange_juice | 30% |
| milk | 10% |
| 其余 6 tasks | 0% |

Seed=43 的 10% 与 seed=42 的 9% 基本一致，确认 scalar 是最差 CRM variant。Seed=43 object benchmark 对比表：

| Method | SR |
|--------|-----|
| argmin | 17% |
| obs_only 0.1 | 12% |
| perdof | 12% |
| **scalar** | **10%** |

---
