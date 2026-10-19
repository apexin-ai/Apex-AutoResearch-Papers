# diagnose eval a3 v11 object

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_a3_v11_object_20260522T141131_result.json`
- **Structured JSON:** [`2c50912195d4b4267575.json`](../../sessions/2c/2c50912195d4b4267575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Cron 误报确认，eval 已正常完成。** 但结果很差：

| 指标 | 值 |
|------|-----|
| **Avg TSR** | **0.0%** (200 episodes 全部失败) |
| **Avg CAR** | **74.5%** (task 1 仅 48%) |

两个严重问题：

1. **机械臂卡住不动** — 大量 episode 的 max_displacement 在 1e-6 ~ 1e-10 量级，说明模型输出的 action 几乎没有让臂移动
2. **SDF refinement 从未触发** — 所有 200 episodes 的 refine_count = 0，A3 的 gradient refinement 模块在推理时完全没有生效（SDF min 值始终远高于 refine_margin=0.01）

报告已写入 `artifacts/diagnose_eval_a3_v11_object.md`，结果 JSON 在 `/root/autodl-tmp/eval_results/v11_eval_safelibero_object_all_levelII_best_a3_seed0.json`。

---
