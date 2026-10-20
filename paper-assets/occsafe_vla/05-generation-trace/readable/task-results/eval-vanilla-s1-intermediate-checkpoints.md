# eval vanilla s1 intermediate checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vanilla_s1_intermediate_checkpoints_20260520T232851_result.json`
- **Structured JSON:** [`f28d0d4f65c5d07622c2.json`](../../sessions/f2/f28d0d4f65c5d07622c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 eval 完成。汇总：

## Vanilla S1 Learning Curve (LIBERO Spatial, 20 rollouts × 10 tasks = 200 episodes)

| Step | TSR | CAR | Collisions/Total |
|------|-----|-----|-----------------|
| 35000 | 0.860 | 0.700 | 60/200 |
| 40000 | 0.910 | 0.725 | 55/200 |
| 45000 | 0.965 | 0.730 | 54/200 |
| 50000 | 0.935 | 0.765 | 47/200 |

趋势：
- **TSR**: 35K→45K 单调上升（0.86→0.965），50K 略回落至 0.935
- **CAR**: 整体单调上升（0.700→0.765），碰撞从 60 降到 47
- 45K 是 TSR 峰值，50K 是 CAR 峰值

所有结果 JSON 保存在服务器 `/root/occsafe_vla/eval_results/` 下。

---
