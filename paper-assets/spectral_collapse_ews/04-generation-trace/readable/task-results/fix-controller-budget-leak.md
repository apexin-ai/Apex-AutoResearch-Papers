# fix controller budget leak

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_controller_budget_leak_20260516T092448_result.json`
- **Structured JSON:** [`1fe568d20e67a3879072.json`](../../sessions/1f/1fe568d20e67a3879072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。修复内容：

1. **`get_first_gen_ratio`** — 扣减 `B_rem` 并递增 `t`
2. **`upper_clip` 公式** — `(remaining_gens - 1)` → `remaining_gens`，为最后一代正确预留 `r_min`
3. **`remaining_gens <= 0` 分支** — 不再强制分配 `r_min`，改为 `max(0, min(r_max, B_rem))`

总预算 2.5 精确消耗完毕，每代至少分配 `r_min=0.20`。

---
