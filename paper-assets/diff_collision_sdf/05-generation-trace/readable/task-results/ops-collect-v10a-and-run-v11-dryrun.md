# ops collect v10a and run v11 dryrun

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_v10a_and_run_v11_dryrun_20260522T104606_result.json`
- **Structured JSON:** [`b590bcfd16c530ed4a80.json`](../../sessions/b5/b590bcfd16c530ed4a80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收齐。汇总如下：

---

## 1. A3 eval v10a 完整结果（50 episodes/task）

| Task | Task Name | TSR | CAR | Avg Displacement | Avg Smoothness |
|------|-----------|-----|-----|-----------------|----------------|
| 0 | orange_juice → basket | 0% | **90%** | **0.0009m** | 0.0045 |
| 1 | chocolate_pudding → basket | 0% | **88%** | 0.0108m | 0.0068 |
| 2 | milk → basket | 0% | 64% | 0.0168m | 0.0043 |
| 3 | bbq_sauce → basket | 0% | 76% | 0.0162m | 0.0041 |
| **Avg** | | **0%** | **79.5%** | | |

A3 eval log 还显示所有 episode 的 `refined=0`，说明 SDF gradient refinement 在 inference 时完全没触发（sdf_min 都在 0.6+ 范围，远高于 refine_margin）。

## 2. Baseline v10 结果对比

| Task | Baseline v10 CAR | A3 v10a CAR | Baseline v10 Disp | A3 v10a Disp |
|------|-----------------|-------------|-------------------|--------------|
| 0 | 74% | **90%** ↑ | 0.0478m | **0.0009m** ↓↓ |
| 1 | 86% | **88%** ↑ | 0.0184m | **0.0108m** ↓ |
| 2 | 66% | 64% ≈ | 0.0387m | **0.0168m** ↓ |
| 3 | **90%** | 76% ↓ | 0.0129m | 0.0162m ↑ |
| **Avg** | **79.0%** | **79.5%** | **0.0295m** | **0.0112m** |

A3 平均 displacement 降到 0.011m（vs baseline 0.030m），下降 62%。Task 0 尤其显著（0.048→0.001）。但 TSR 都是 0%。

## 3. Baseline v11 dry-run 结果（Task 0，3 episodes）

| Episode | Success | Collided | Steps | Max Displacement | Smoothness |
|---------|---------|----------|-------|-----------------|------------|
| 0 | False | **True** | 300 | 0.0120m | 0.0049 |
| 1 | False | False | 300 | 0.0000m | 0.0043 |
| 2 | False | False | 300 | 0.0000m | 0.0020 |
| **Avg** | 0% TSR | 66.7% CAR | | **0.0040m** | 0.0037 |

## 4. v10 vs v11 displacement 对比

Baseline v10 Task 0 avg displacement = **0.0478m**，v11 dry-run = **0.0040m**。

**这个结果与预期的 v11 > 0.1m 不符。** v11 dry-run displacement 反而比 v10 更低（0.004 vs 0.048）。仅 3 episodes 样本量太小不能下结论，但目前看不到 displacement 增大的趋势。

## 异常

- eval 脚本没有 `--replan_steps` 和 `--output_prefix` 参数（help 中不存在），dry-run 用的是默认参数
- A3 eval 的 refined=0（SDF refinement 从未触发），说明当前 refine_margin 阈值可能设太低

---
