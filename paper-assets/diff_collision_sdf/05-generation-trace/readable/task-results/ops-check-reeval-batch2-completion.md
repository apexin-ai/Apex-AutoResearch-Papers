# ops check reeval batch2 completion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_reeval_batch2_completion_20260526T143815_result.json`
- **Structured JSON:** [`b449681f6f5af7753c85.json`](../../sessions/b4/b449681f6f5af7753c85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 已清除。

## Batch2 Reeval 汇总（rotation-fixed, eval_seed=7, 200 episodes/experiment）

所有 4 个 eval 全部完成，0 frozen EE，确认 rotation-fixed 版本。

### 总体指标

| Experiment | λ | seed | TSR (%) | CAR (%) | avg_max_ee_disp |
|---|---|---|---|---|---|
| reeval_sdf_s1_l005_30k | 0.005 | 1 | 50.5 | 54.0 | 0.3883 |
| reeval_sdf_s1_l01_30k | 0.01 | 1 | 55.5 | 57.5 | 0.3852 |
| reeval_sdf_s2_l005_30k | 0.005 | 2 | 56.0 | 52.5 | 0.3858 |
| reeval_sdf_s2_l01_30k | 0.01 | 2 | 53.5 | 54.5 | 0.3877 |

### Per-task 明细

| Task | s1_l005 TSR/CAR | s1_l01 TSR/CAR | s2_l005 TSR/CAR | s2_l01 TSR/CAR |
|---|---|---|---|---|
| T0 orange_juice | 28/64 | 22/60 | 34/46 | 24/64 |
| T1 chocolate_pudding | 72/70 | 80/76 | 82/74 | 72/68 |
| T2 milk | 30/68 | 54/72 | 38/72 | 48/72 |
| T3 bbq_sauce | 72/14 | 66/22 | 70/18 | 70/14 |

### 多种子汇总（含 s0 已有数据）

**λ=0.01 三种子：**
- s0: CAR=57.0%, TSR=52.5% (已有)
- s1: CAR=57.5%, TSR=55.5%
- s2: CAR=54.5%, TSR=53.5%
- **均值: TSR=53.8±1.5%, CAR=56.3±1.6%**

**λ=0.005 三种子：**
- s0: 已有 (reeval_sdf_s0_l005_30k)
- s1: TSR=50.5%, CAR=54.0%
- s2: TSR=56.0%, CAR=52.5%

### 关键观察

- **T3 bbq_sauce** CAR 在所有条件下都极低（14-22%），拖低整体 CAR — 碰撞严重
- **T1 chocolate_pudding** 表现最好，TSR 72-82%，CAR 68-76%
- **λ=0.01 vs λ=0.005** 差异不大，l01 略高 TSR，CAR 相近
- 所有实验 frozen_ee=0，rotation fix 有效

---
