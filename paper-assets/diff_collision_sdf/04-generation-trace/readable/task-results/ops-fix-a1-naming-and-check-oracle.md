# ops fix a1 naming and check oracle

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_a1_naming_and_check_oracle_20260522T155908_result.json`
- **Structured JSON:** [`53bfd75c6cf9ddf982fa.json`](../../sessions/53/53bfd75c6cf9ddf982fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## Part 1: 文件覆盖修复

**确认覆盖**：`eval_safelibero_object_all_levelII_best_lora_baseline_seed0.json` 的 checkpoint 指向 `a1_sdf_object_pudding`（A1），时间戳 23:50。LoRA baseline 原始写入在 23:04 被覆盖。

**已完成**：
- A1 结果备份为 `a1_lora_v11_eval_safelibero_object_all_levelII_best_seed0.json`
- LoRA baseline 从 log 重建为 `lora_baseline_v11_eval_safelibero_object_all_levelII_best_seed0.json`，包含 task-level 汇总：

| Task | TSR | CAR | Disp |
|------|-----|-----|------|
| orange_juice | 0% | 96% | 0.0072m |
| chocolate_pudding | 0% | 46% | 0.0257m |
| milk | 0% | 98% | 0.0000m |
| bbq_sauce | 0% | 88% | 0.0070m |
| **Overall** | **0%** | **82%** | — |

**注意**：per-episode 数据无法从 log 恢复（log 只有每 10 episode 进度和 task 汇总）。如需完整 per-episode 数据，需重跑 LoRA baseline object eval。

**Spatial LoRA baseline 未被覆盖**：checkpoint 正确指向 `baseline_spatial_bowl/baseline_lora_spatial_bowl_seed0/best`。

---

## Part 2: Oracle A3 Force Refine 进度

**正在运行**，cuda:2，task 1/4（chocolate pudding），episode 20/40 刚完成。

Task 0 结果：TSR=0%, CAR=95%, disp=0.0005m

按 ~2.2 min/10ep 估算，剩余 ~40 min（task 1 剩 20ep + task 2,3 各 40ep）。

---

## Part 3: a1_lora_spatial 训练

**即将完成**：step 29960/30000，loss ~0.02，ETA ~3 min。tmux session 名为 `a1_lora_spa`。最新 checkpoint 在 step 28000，`best` 也已存在。

---
