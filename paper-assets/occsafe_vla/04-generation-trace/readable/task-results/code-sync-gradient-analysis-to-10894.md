# code sync gradient analysis to 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync_gradient_analysis_to_10894_20260524T132631_result.json`
- **Structured JSON:** [`a4e9282498d03f103c37.json`](../../sessions/a4/a4e9282498d03f103c37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过：
- `LN OK: GroupNorm(1, 128, ...)`
- `BN OK: BatchNorm2d(128, ...)`

同步完成。occ_head.py 两边已一致，gradient_analysis.py 新增了 `--occ_norm` 参数（bn/ln）并传入 `BEVOccupancyHead` 构造。10894 训练完成后可直接跑 `--occ_norm ln` 的梯度分析。

---
