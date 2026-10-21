# code fix gradient analysis ln support

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_gradient_analysis_ln_support_20260524T125811_result.json`
- **Structured JSON:** [`0fb5674c8528cf3a6788.json`](../../sessions/0f/0fb5674c8528cf3a6788.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过：

- `norm_type='ln'` → `GroupNorm(1, 128, eps=1e-05, affine=True)`
- `norm_type='bn'` → `BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)`

修改完成。两处改动：

1. **occ_head.py** — `BEVOccupancyHead.__init__` 新增 `norm_type="bn"` 参数，`"ln"` 时用 `GroupNorm(1, C)` 替代 `BatchNorm2d`
2. **gradient_analysis.py** — 新增 `--occ_norm` 参数（`bn`/`ln`），传入 `BEVOccupancyHead` 构造

使用时加 `--occ_norm ln` 即可加载 Detach_LN_s0 的 checkpoint。

---
