# Paper Data Summary — diff_collision_sdf

> 生成时间: 2026-05-26
> 数据来源: registry (status=DONE, conclusion=success/negative 中已确认的指标)
> 标记说明: ✅ 已确认 | ⏳ 待收集 | 🔧 displacement-fixed eval

---

## Table 1: Pi0.5+A1 SDF 训练结果矩阵

所有实验 n_episodes=200。

### λ=0.005

| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
|------|------|------|---------|---------|-------------|------------|--------|--------|------|
| 0 | 30K | 30K | 5.5 | 50.0 | 0.0433¹ | — | — | eval_pi05_a1_30k_s0_l005 | ✅ 旧脚本,obstacle disp |
| 0 | 30K | 30K | 7.5 | 47.0 | 0.0485¹ | — | — | eval_pi05_a1_30k_s0_l005_r4 | ✅ retry,旧脚本 |
| 0 | best | — | — | — | — | — | — | — | ⏳ seed0 无 best/ ckpt (训练未保存) |
| 1 | 30K | 30K | 4.0 | 54.0 | 0.4955 | **0%** | **No** | eval_pi05_a1_30k_s1_l005_disp | ✅🔧 displacement-fixed |
| 1 | 30K | 30K | 5.5 | 52.5 | — | — | — | eval_pi05_a1_30k_s1_l005_v2 | ✅ 无 disp 数据 |
| 1 | 30K | 30K | 4.0 | 51.5 | — | — | — | eval_pi05_a1_30k_s1_l005_v3 | ✅ v4 rerun |
| 1 | best | 16K | 6.5 | 53.0 | 0.37~0.65² | **0%** | **No** | eval_pi05_a1_best_s1_l005_16k | ✅🔧 has ee_disp |
| 2 | 30K | 30K | 9.5 | 54.5 | — | — | — | eval_pi05_a1_30k_s2_l005_v2 | ✅ |
| 2 | 30K | 30K | 9.0 | 53.0 | — | — | — | eval_pi05_a1_30k_s2_l005_v3 | ✅ v4 rerun |
| 2 | best | 10K | 9.0 | 55.5 | 0.5046 | **0%** | **No** | eval_pi05_a1_best_s2_l005_10k | ✅🔧 displacement-fixed |

¹ obstacle displacement (旧脚本), 非 ee_displacement
² per-task ee_disp: task0=0.5179, task1=0.5146, task2=0.6475, task3=0.3707

### λ=0.01

| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
|------|------|------|---------|---------|-------------|------------|--------|--------|------|
| 0 | 30K | 30K | 5.5 | 53.0 | 0.0297¹ | — | — | eval_pi05_a1_30k_s0_l01 | ✅ 旧脚本,obstacle disp |
| 0 | 30K | 30K | 6.5 | 52.5 | 0.4725 | **0%** | **No** | eval_pi05_a1_30k_s0_l01_disp | ✅🔧 displacement-fixed |
| 0 | best | — | — | — | — | — | — | — | ⏳ seed0 无 best/ ckpt |
| 1 | 30K | 30K | 7.5 | 52.5 | — | — | — | eval_pi05_a1_30k_s1_l01_v2 | ✅ |
| 1 | best | — | — | — | — | — | — | — | ⏳ 待 eval |
| 2 | 30K | 30K | 7.5 | 53.0 | — | — | — | eval_pi05_a1_30k_s2_l01_v2 | ✅ v3 rerun |
| 2 | best | — | — | — | — | — | — | — | ⏳ 待 eval |

### 汇总统计 (displacement-fixed 数据)

| 配置 | avg_CAR | avg_TSR | avg_ee_disp | fake_safe% |
|------|---------|---------|-------------|------------|
| λ=0.005, best (seed1+seed2) | 54.25 | 7.75 | 0.500 | 0% |
| λ=0.005, 30K (seed1 disp) | 54.0 | 4.0 | 0.496 | 0% |
| λ=0.01, 30K (seed0 disp) | 52.5 | 6.5 | 0.473 | 0% |

---

## Claim 1 证据: A1 Baseline (Pi0 Full-FT) 的 Fake Safety

> 来源: eval_a1_lora_object_v11_rerun (800 episodes, DONE, conclusion=negative)

| 指标 | 值 | 备注 |
|------|----|------|
| n_episodes | 800 | ✅ |
| avg_TSR | 0% | ✅ |
| avg_CAR | 91.5% | ✅ |
| fake_safe_rate | **99.6%** (729/732 safe eps, disp<0.1mm) | ✅ |
| real_safe_count | 3 | ✅ |
| collision_episodes | 68 | ✅ |
| collision_disp_mean_mm | 45.92 | ✅ |

Per-task fake safe breakdown:
| Task | fake_safe | 比例 |
|------|-----------|------|
| orange_juice | 192/192 | 100% |
| chocolate_pudding | 162/164 | 98.8% |
| milk | 194/194 | 100% |
| bbq_sauce | 181/182 | 99.5% |

**注意**: displacement 指 obstacle displacement（物体位移），非 ee_displacement。safe_disp_mean 极低(0.0003~0.008mm)证明机器人近乎完全冻结。

### Baseline (Full-FT, 无 SDF) 对比

来源: eval_baseline_v11_object (200 eps, DONE, conclusion=negative)

| 指标 | 值 |
|------|----|
| TSR | 0.5% |
| CAR | 83% |
| displacement_avg | 0.0271m |
| fake_safe_rate | 99.4% (165/166) |

**结论**: A1 (SDF aux + LoRA) CAR 91.5% 看似高于 baseline 83%，但 99.6% 为 fake safety（机器人冻结）。

---

## Claim 2 证据: Pi0.5 LoRA Baseline (无 SDF Loss)

### Object task

来源: eval_lora_baseline_object_v11 (200 eps, DONE, conclusion=negative)

| 指标 | 值 | exp_id |
|------|----|--------|
| TSR | 0% | eval_lora_baseline_object_v11 | ✅ |
| CAR | 82% | eval_lora_baseline_object_v11 | ✅ |
| displacement_avg | 0.01m | eval_lora_baseline_object_v11 | ✅ |
| task2_disp | 0.00001m (frozen) | eval_lora_baseline_object_v11 | ✅ |

### Spatial task

来源: eval_lora_baseline_spatial_v11 (200 eps, DONE, conclusion=negative)

| 指标 | 值 | exp_id |
|------|----|--------|
| TSR | 0% | eval_lora_baseline_spatial_v11 | ✅ |
| CAR | 0% | eval_lora_baseline_spatial_v11 | ✅ |
| displacement_avg | 0.23m | eval_lora_baseline_spatial_v11 | ✅ |

### Pi0.5 原始 baseline (3-seed)

| Seed | TSR | CAR | disp | exp_id |
|------|-----|-----|------|--------|
| 0 | 73% | 28% | — | eval_pi05_safelibero_object_v11 | ✅ (conclusion=negative) |
| 1 | 76% | 25% | 0.153 | eval_pi05_safelibero_object_v11_s1 | ✅ |
| 2 | 75% | 27.5% | 0.132 | eval_pi05_safelibero_object_v11_s2 | ✅ |
| **avg** | **74.7±1.5%** | **26.8±1.6%** | — | 3-seed aggregate | ✅ |

⏳ **待收集**: Pi0.5 + LoRA (无 SDF) 的 displacement-fixed eval（确认 fake safety 比例）

---

## Claim 3 证据: Oracle Variants

所有 oracle 实验均 conclusion=negative，证明 gradient-based runtime refinement 方向失败。

| 变体 | CAR | fake_safe% | avg_refined/ep | exp_id | 备注 |
|------|-----|------------|----------------|--------|------|
| A3 force refine | 81.2% | ~85.6%¹ | 300 | oracle_a3_force_refine_object_v11 | ✅ M027: 实际用 learned decoder 非 GT |
| A3 M024 fix | 85.6% | 85.6% | 300 | oracle_a3_m024fix_object_v11 | ✅ 23/23 moving eps = 100% collision |
| True GT adaptive α | 75.0% | **98.3%** | 14.2 | oracle_true_gt_adaptive_alpha_v11 | ✅ GT SDF 比 baseline 更差 |
| True GT fixed α=0.005 | 73.1% | **98.3%** | 14.8 | oracle_true_gt_fixed_alpha_v11 | ✅ α 大小无关紧要 |
| GT feature-space | 76.9% | **96.7%** | 241.7 | oracle_true_gt_feature_v11 | ✅ feature-space 也不行 |
| Baseline (无 refinement) | 83% | 99.4% | 0 | eval_baseline_v11_object | ✅ 对照组 |

¹ oracle_a3_force_refine 未直接报告 fake_safe%，从 displacement 数据推断

**关键结论**: 即使使用 ground-truth SDF，gradient-based action refinement 也无法产生真正的避障行为（96-98% fake safety）。Feature-space 不优于 action-space。这验证了 A1 (training-time integration) 路线的必要性。

---

## Over-Avoidance 发现 (30K vs Best Checkpoint)

> 核心问题: 30K checkpoint 的 CAR 升高是因为 over-avoidance（真正避障但过度保守）还是 frozen（假安全）？

### Displacement-fixed 对比

| 配置 | Step | CAR | TSR | avg_ee_disp | fake_safe% | exp_id |
|------|------|-----|-----|-------------|------------|--------|
| seed1, λ=0.005 | **30K** | 54.0 | 4.0 | 0.4955 | 0% | eval_pi05_a1_30k_s1_l005_disp | ✅🔧 |
| seed1, λ=0.005 | **16K best** | 53.0 | 6.5 | 0.37~0.65 | 0% | eval_pi05_a1_best_s1_l005_16k | ✅🔧 |
| seed0, λ=0.01 | **30K** | 52.5 | 6.5 | 0.4725 | 0% | eval_pi05_a1_30k_s0_l01_disp | ✅🔧 |
| seed2, λ=0.005 | **10K best** | 55.5 | 9.0 | 0.5046 | 0% | eval_pi05_a1_best_s2_l005_10k | ✅🔧 |

### Per-task displacement (30K seed1 λ=0.005)

| Task | ee_disp | safe_ee_disp | CAR |
|------|---------|--------------|-----|
| orange_juice (task0) | 0.5062 | 0.4247 | 54% |
| chocolate_pudding (task1) | 0.4991 | 0.5006 | 58% |
| milk (task2) | 0.6088 | 0.6213 | 92% |
| bbq_sauce (task3) | 0.3680 | 0.3628 | 12% |

### Per-task displacement (30K seed0 λ=0.01)

| Task | ee_disp | safe_ee_disp | CAR |
|------|---------|--------------|-----|
| orange_juice (task0) | 0.4781 | 0.4627 | 76% |
| chocolate_pudding (task1) | 0.5387 | 0.4446 | 32% |
| milk (task2) | 0.5169 | 0.5273 | 84% |
| bbq_sauce (task3) | 0.3561 | 0.3764 | 18% |

**结论**: 30K 和 best checkpoint 的 ee_displacement 量级相近（0.47-0.50m），均远高于 frozen 阈值（0.1mm）。fake_safe% 全部为 0。30K 的 CAR 升高不是因为 frozen/action collapse，而是 over-avoidance（真正在避障，但更保守导致 TSR 下降）。

---

## 训练配置参考 (DONE+success)

| exp_id | 配置 | best_loss | best_step |
|--------|------|-----------|-----------|
| train_pi05_a1_obj_s0_l005 | seed0, λ=0.005 | 0.00786 | 26K (无 best/ ckpt) |
| train_pi05_a1_obj_s0_l01 | seed0, λ=0.01 | 0.00801 | — (无 best/ ckpt) |
| train_pi05_a1_obj_s1_l005 | seed1, λ=0.005 | 0.01143 | 16K |
| train_pi05_a1_obj_s1_l01 | seed1, λ=0.01 | 0.01168 | 16K |
| train_pi05_a1_obj_s2_l005 | seed2, λ=0.005 | 0.00874 | 10K |
| train_pi05_a1_obj_s2_l01 | seed2, λ=0.01 | 0.00911 | 10K |

---

## 数据完整性统计

- **已确认数据点**: 42 个（含所有 Table 1 已完成 eval、Claim 1-3 证据、Oracle 5 个变体、Over-avoidance 4 组对比）
- **待收集占位符**: 5 个
  1. seed0 best checkpoint eval (λ=0.005) — 训练未保存 best/ ckpt
  2. seed0 best checkpoint eval (λ=0.01) — 训练未保存 best/ ckpt
  3. seed1 best checkpoint eval (λ=0.01) — 待执行
  4. seed2 best checkpoint eval (λ=0.01) — 待执行
  5. Pi0.5 + LoRA (无 SDF) displacement-fixed eval — 待执行
- **Displacement-fixed eval 已完成**: 4 个（seed1_l005_30K, seed0_l01_30K, seed1_l005_16K_best, seed2_l005_10K_best）
