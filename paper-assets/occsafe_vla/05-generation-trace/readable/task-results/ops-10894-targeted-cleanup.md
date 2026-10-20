# ops 10894 targeted cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894_targeted_cleanup_20260524T175402_result.json`
- **Structured JSON:** [`70f65e3298cc39929731.json`](../../sessions/70/70f65e3298cc39929731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部删除完成。

**结果：**
| 目录 | 状态 |
|------|------|
| detach_ln_s0 (15G) | ✓ 已删除 |
| detach_ln_s1 (15G) | ✓ 已删除 |
| detach_ln_s2 (15G) | ✓ 已删除 |
| ablation_random_occ_s2 (15G) | ✓ 已删除 |
| cutoff_s2_v2 (15G) | ✓ 已删除 |

**磁盘状态：** 250G 总量，已用 102G，可用 **149G** (41%)。

回收了约 74G 空间，不需要第二批清理。full_occ_ln_s0 在 step 40000 保存 checkpoint 有充足空间。

---
