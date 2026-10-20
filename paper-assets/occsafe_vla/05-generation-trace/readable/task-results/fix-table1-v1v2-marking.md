# fix table1 v1v2 marking

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table1-v1v2-marking_20260527T034920_result.json`
- **Structured JSON:** [`0f4d615ea60ce7947af5.json`](../../sessions/0f/0f4d615ea60ce7947af5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无报错，编译通过。4 项修改完成：

1. **Table 1 L26**: `Detach+LN` → `Detach+LN$^\star$`，ΔCAR `$+$2.0` → `---`
2. **Table 1 caption L16**: 加了 `unless marked $^\star$`
3. **L45**: `the LN cells have $n{=}1$ each` → `Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\star$)`
4. **L47**: 同上模式修改

---
