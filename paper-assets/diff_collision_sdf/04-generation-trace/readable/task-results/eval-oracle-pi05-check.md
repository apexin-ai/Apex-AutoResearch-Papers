# eval oracle pi05 check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_oracle-pi05-check_20260529T012305_result.json`
- **Structured JSON:** [`c2346778643b0e31d558.json`](../../sessions/c2/c2346778643b0e31d558.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Eval 仍在运行，目前进度：**

- 总计 4 个 task（task 0-3），已完成 2 个，正在跑 Task 2
- 每个 task 40 episodes，每 task 约 8-10 分钟，预计再需 ~20 分钟完成

**已完成结果：**

| Task | 名称 | TSR | CAR |
|------|------|-----|-----|
| 0 | pick up orange juice → basket | 25.0% (10/40) | 50.0% (20/40) |
| 1 | pick up chocolate pudding → basket | 90.0% (36/40) | 75.0% (30/40) |
| 2 | pick up milk → basket | 进行中 | 进行中 |
| 3 | (待运行) | - | - |

**初步观察：**
- Task 1 的 CAR 75.0% 显著高于 LoRA baseline 的 57.0%（整体），oracle refinement 在该 task 上效果明显
- Task 0 的 CAR 50.0% 较低，但 TSR 也只有 25%，说明这个 task 本身较难
- 所有 episode 的 `collided=False`，oracle SDF refinement 在避碰上表现良好

等 eval 全部完成后再做最终对比和 registry 更新。需要我稍后再查吗？

---
