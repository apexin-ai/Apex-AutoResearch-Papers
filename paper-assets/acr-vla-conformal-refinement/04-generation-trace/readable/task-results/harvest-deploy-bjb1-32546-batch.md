# harvest deploy bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest-deploy_bjb1-32546-batch_20260520T130502_result.json`
- **Structured JSON:** [`254aa41d515a9d20cbb6.json`](../../sessions/25/254aa41d515a9d20cbb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部提交成功。

---

## 收割结果

| 实验 | success_rate | 结论 |
|------|-------------|------|
| **eval-obs-only-goal-norm02-seed52** | **68%** | CRM obs_only Goal OOD, 最高 turn_on_stove/bowl_on_plate=100%, 最低 bowl_in_drawer=30% |
| **eval-argmin-object-seed49** | **16%** | Argmin baseline Object, bbq_sauce=40% 最高, 3 tasks=0% |
| **eval-argmin-object-seed48** | **15%** | Argmin baseline Object, chocolate_pudding=40% 最高, 3 tasks=0% |

## 新部署实验

| exp_id | GPU | PID | 说明 |
|--------|-----|-----|------|
| **eval-obs-only-object-norm02-seed50** | cuda:0 | 423273 | CRM obs_only Object ε=0.2 seed50 |
| **eval-argmin-object-seed50** | cuda:3 | 423608 | Argmin reconvla Object seed50 (替代已完成的 seed48) |
| **eval-vla-only-object-seed48-r2** | cuda:4 | 423884 | VLA-only Object seed48 重跑 (原 sr=0.1 有进程死亡) |
| **eval-obs-only-goal-norm02-seed53** | cuda:5 | 424172 | CRM obs_only Goal seed53 补种子 |

---
