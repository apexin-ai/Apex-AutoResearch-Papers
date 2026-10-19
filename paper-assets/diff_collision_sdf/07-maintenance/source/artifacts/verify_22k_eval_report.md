# 22K Eval 验证报告

**日期**: 2026-05-27
**文件**: `/root/autodl-tmp/eval_results/eval_s0_l1_22k_seed7.json` (85,177 bytes)
**Checkpoint**: `a1_sdf_pi05_object_pudding_seed0_l1/22000`
**Seed**: 7 | **Safety Level**: II | **Episodes/task**: 50 | **Tasks**: 4

## 1. 数据验证结果

Reviewer 报告值全部匹配，eval 数据有效。

| 指标 | Reviewer 报告 | 实际值 | 验证 |
|------|--------------|--------|------|
| 总体 CAR | 60.5% | 60.5% | PASS |
| 总体 TSR | 45.5% | 45.5% | PASS |
| Frozen rate | 0% | 0% | PASS |
| 总 episodes | 200 | 200 | PASS |
| orange_juice CAR | 66% | 66% | PASS |
| chocolate_pudding CAR | 76% | 76% | PASS |
| bbq_sauce CAR | 32% | 32% | PASS |

## 2. Per-task 完整数据

| Task | CAR | TSR | avg_smoothness | avg_max_disp | avg_max_ee_disp |
|------|-----|-----|----------------|-------------|-----------------|
| orange_juice | 0.66 | 0.18 | 0.000782 | 0.0365 | 0.397 |
| chocolate_pudding | 0.76 | 0.74 | 0.000817 | 0.0484 | 0.417 |
| milk | 0.68 | 0.32 | 0.000635 | 0.0420 | 0.357 |
| bbq_sauce | 0.32 | 0.58 | 0.000637 | 0.0891 | 0.399 |
| **平均** | **0.605** | **0.455** | **0.000718** | **0.0540** | **0.393** |

所有 task 的 avg_max_ee_displacement > 0.3m，确认无 frozen episode。

## 3. s1 22K Checkpoint

**存在**。路径: `a1_sdf_pi05_object_pudding_seed1_l1/22000/`

- model.safetensors: 7.5GB
- 创建时间: 2026-05-27 07:30
- s1 最新 checkpoint: **24000**（已超过 22K）

## 4. GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 0 MiB / 97887 MiB | 0% | **空闲** |
| cuda:1 | 27045 MiB / 97887 MiB | 100% | 训练中 |
| cuda:2 | 27045 MiB / 97887 MiB | 100% | 训练中 |
| cuda:3 | 27037 MiB / 97887 MiB | 100% | 训练中 |

cuda:0 已释放，可用于后续 eval 任务。

## 5. s0 训练进度

- s0 最新 checkpoint: **24000**（保存于 2026-05-27 09:23）
- best_loss: 0.0121 @ step 24000
- 距离 30K 目标还差 ~6000 steps
- s0 和 s1 均在 cuda:1-3 上继续训练（3 GPU 各占 ~27GB）
