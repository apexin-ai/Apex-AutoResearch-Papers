# fix 34685 preventive cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_34685_preventive_cleanup_20260528T014617_result.json`
- **Structured JSON:** [`65da1480fc3c39040ee1.json`](../../sessions/65/65da1480fc3c39040ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 项目 | 值 |
|------|-----|
| **清理前** | 300G used / 51G free (86%) |
| **删除量** | ~135G (9 × 15G) |
| **清理后** | 166G used / **185G free (48%)** |

**剩余 checkpoint 目录：**
- `detach_ln_v2_s2/`
- `detach_ln_v2_s3/`
- `full_occ_ln_v2_s0c/`
- `full_occ_ln_v2_s3/`
- `vanilla_object_s0/`

目标 ≥100G free 已达成（185G available）。

---
