# ops close early signal s1 eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_close_early_signal_s1_eval_20260527T003442_result.json`
- **Structured JSON:** [`f206340aeb28c6ab8806.json`](../../sessions/f2/f206340aeb28c6ab8806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE，无活跃 cron 需要清除。

```
eval_early_signal_s1_l1_20k 结果:
- 状态: success
- CAR: 56%, TSR: 51%
- frozen_ee: 0%
- 硬约束: TSR≥35% ✅, frozen=0% ✅
- A/B/C 信号: B (56% ≤ 57%)
- Per-task:
  - orange_juice: CAR=62%, TSR=20%
  - task1:        CAR=76%, TSR=82%
  - milk:         CAR=66%, TSR=42%
  - bbq_sauce:    CAR=20%, TSR=60%
- 2-seed 20K mean CAR: (55 + 56) / 2 = 55.5% → 场景 B 确认
```

两个 seed 在 20K 都落入 null distribution 内（mean=54.5%, σ=2.15%），2-seed mean 55.5% 距 null mean 仅 +0.47σ，A1 SDF λ=0.1 在 20K 无显著信号，场景 B 成立。

---
