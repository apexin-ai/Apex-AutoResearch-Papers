## Part A: n_rollouts 审计

### 1. obs_only ε=0.2（K=10，6 seeds，论文主结果）— ✅ 全部一致

| seed | exp_id | server | JSON 文件 | n_rollouts | total | SR | 一致? |
|------|--------|--------|-----------|------------|-------|-----|-------|
| 42 | eval-acr-object-obs-only-norm02 | bjb1-32546 | eval_object_obs_only_norm02.json | 10 | 100 | 22% | ✅ |
| 43 | eval-obs-only-object-norm02-seed43-r2 | bjb1-32546 | eval_object_obs_only_norm02_seed43_r2.json | 10 | 100 | 16% | ✅ |
| 44 | eval-obs-only-object-norm02-seed44-r2 | bjb1-18228 | eval_object_obs_only_norm02_seed44.json | 10 | 100 | 16% | ✅ |
| 45 | eval-obs-only-object-norm02-seed45 | bjb1-32546 | eval_object_obs_only_norm02_seed45.json | 10 | 100 | 16% | ✅ |
| 46 | eval-obs-only-object-norm02-seed46 | bjb1-18228 | eval_object_obs_only_norm02_seed46.json | 10 | 100 | 15% | ✅ |
| 47 | eval-obs-only-object-norm02-seed47 | bjb1-32546 | eval_object_obs_only_norm02_seed47.json | 10 | 100 | 20% | ✅ |

**mean = 17.5%，全部 n_rollouts=10，无问题。**

### 2. Argmin Baseline（6 seeds）— ✅ 全部一致

| seed | exp_id | server | JSON 文件 | n_rollouts | total | SR | 一致? |
|------|--------|--------|-----------|------------|-------|-----|-------|
| 42 | eval-reconvla-object | bjb1-32546 | eval_object_reconvla.json | 10 | 100 | 12% | ✅ |
| 43 | eval-argmin-object-seed43 | bjb1-18228 | eval_object_reconvla_seed43.json | 10 | 100 | 17% | ✅ |
| 44 | eval-argmin-object-seed44-r2 | bjb1-18228 | eval_object_reconvla_seed44.json | 10 | 100 | 13% | ✅ |
| 45 | eval-argmin-object-seed45 | bjb2-28827 | eval_object_argmin_seed45.json | 10 | 100 | 12% | ✅ |
| 46 | eval-argmin-object-seed46 | bjb1-32546 | eval_object_reconvla_seed46.json | 10 | 100 | 10% | ✅ |
| 47 | eval-argmin-object-seed47 | bjb1-32546 | eval_object_reconvla_seed47.json | 10 | 100 | 10% | ✅ |

**mean = 12.33%，全部 n_rollouts=10，无问题。**

### 3. VLA-Only Baseline（5 seeds）— ❌ seed45 混用

| seed | exp_id | server | JSON 文件 | n_rollouts | total | SR | 一致? |
|------|--------|--------|-----------|------------|-------|-----|-------|
| 42 | eval-vla-only-object | bjb1-32546 | eval_object_vla_only.json | 10 | 100 | 12% | ✅ |
| 43 | eval-vla-only-object-seed43 | bjb1-32546 | eval_object_vla_only_seed43.json | 10 | 100 | 12% | ✅ |
| 44 | eval-vla-only-object-seed44-r2 | bjb2-40593 | eval_object_vla_only_seed44.json | 10 | 100 | 10% | ✅ |
| **45** | eval-vla-only-object-seed45 | bjb2-28827 | eval_object_vla_only_seed45.json | **20** | **200** | 9% | **❌** |
| 46 | eval-vla-only-object-seed46 | bjb1-18228 | eval_object_vla_only_seed46.json | 10 | 100 | 13% | ✅ |

**当前 mean = 11.2%。seed45 用了 n_rollouts=20，与其他 4 seeds 不一致。**

### 4. Scalar CRM（4 seeds）— ❌ seed45 混用

| seed | exp_id | server | JSON 文件 | n_rollouts | total | SR | 一致? |
|------|--------|--------|-----------|------------|-------|-----|-------|
| 42 | eval-acr-object-v4-scalar | bjb1-32546 | (文件已删除) | 未知(推测10) | — | 9% | ? |
| 43 | eval-scalar-object-seed43 | bjb1-32546 | eval_object_scalar_seed43.json | 10 | 100 | 10% | ✅ |
| 44 | eval-scalar-object-seed44-r2 | bjb1-32546 | eval_object_scalar_seed44_r2.json | 10 | 100 | 6% | ✅ |
| **45** | eval-scalar-object-seed45 | bjb2-28827 | eval_object_scalar_seed45.json | **20** | **200** | 9% | **❌** |

**当前 mean = 8.5%。seed45 用了 n_rollouts=20。seed42 原始 JSON 已删除，无法验证。**

### 5. Magnitude Curve obs_only — ❌ 两个 seed45 数据点混用

| ε | seed | server | JSON 文件 | n_rollouts | SR | 一致? |
|---|------|--------|-----------|------------|-----|-------|
| 0.03 | 42 | bjb1-32546 | eval_object_obs_only_norm003.json | 10 | 16% | ✅ |
| 0.05 | 42 | bjb2-28827 | eval_object_obs_only_norm005.json | 10 | 13% | ✅ |
| 0.05 | 43 | bjb1-32546 | eval_object_obs_only_norm005_seed43_r2.json | 10 | 14% | ✅ |
| 0.1 | 42 | bjb1-32546 | eval_object_obs_only.json | 10 | 19% | ✅ |
| 0.1 | 43 | bjb1-18228 | eval_object_obs_only_seed43.json | 10 | 12% | ✅ |
| 0.1 | 44 | bjb1-32546 | eval_object_obs_only_norm01_seed44.json | 10 | 16% | ✅ |
| **0.1** | **45** | bjb1-18228 | eval_object_obs_only_norm01_seed45.json | **20** | 14% | **❌** |
| 0.2 | 42-47 | — | (见上表) | 10 | — | ✅ |
| 0.3 | 42 | bjb2-28827 | eval_object_obs_only_norm03.json | 10 | 19% | ✅ |
| 0.3 | 44 | bjb1-32546 | eval_object_obs_only_norm03_seed44.json | 10 | 18% | ✅ |
| 0.3 | 45 | bjb2-28827 | eval_object_obs_only_norm03_seed45_r2.json | 10 | 14% | ✅ |
| 0.3 | 46 | bjb1-32546 | eval_object_obs_only_norm03_seed46.json | 10 | 17% | ✅ |
| default | 44 | bjb1-32546 | eval_object_obs_only_default_seed44.json | 10 | 16% | ✅ |
| **default** | **45** | bjb2-28827 | eval_object_obs_only_default_seed45.json | **20** | 12% | **❌** |
| default | 46 | bjb1-32546 | eval_object_obs_only_default_seed46.json | 10 | 15% | ✅ |

### 6. Magnitude Curve perdof — ❌ ε=0.2 seed45 原始数据混用

| ε | seed | server | JSON 文件 | n_rollouts | SR | 一致? |
|---|------|--------|-----------|------------|-----|-------|
| 0.03 | 42 | bjb2-28827 | eval_object_perdof_norm003.json | 10 | 14% | ✅ |
| 0.05 | 42 | bjb2-28827 | eval_object_perdof_norm005.json | 10 | 14% | ✅ |
| 0.1 | 42 | bjb1-32546 | eval_object_perdof.json | 10 | 11% | ✅ |
| 0.1 | 43 | bjb1-18228 | eval_object_perdof_seed43.json | 10 | 12% | ✅ |
| 0.1 | 44 | bjb1-18228 | eval_object_perdof_norm01_seed44.json | 10 | 8% | ✅ |
| 0.1 | 45 | bjb1-32546 | eval_object_perdof_norm01_seed45.json | 10 | 11% | ✅ |
| 0.1 | 46 | bjb1-32546 | eval_object_perdof_norm01_seed46.json | 10 | 10% | ✅ |
| 0.1 | 47 | bjb1-32546 | eval_object_perdof_norm01_seed47_r2.json | 10 | 14% | ✅ |
| 0.2 | 42 | bjb1-32546 | eval_object_perdof_norm02.json | 10 | 11% | ✅ |
| 0.2 | 43 | bjb2-28827 | eval_object_perdof_norm02_seed43_r3.json | 10 | 9% | ✅ |
| 0.2 | 44 | bjb2-28827 | eval_object_perdof_norm02_seed44.json | 10 | 10% | ✅ |
| **0.2** | **45** | bjb2-28827 | eval_object_perdof_norm02_seed45.json | **20** | 9% | **❌** |
| 0.2 | 46 | bjb2-28827 | eval_object_perdof_norm02_seed46.json | 10 | 9% | ✅ |
| 0.2 | 47 | bjb2-28827 | eval_object_perdof_norm02_seed47.json | 10 | 11% | ✅ |
| 0.3 | 42 | bjb2-28827 | eval_object_perdof_norm03_r3.json | 10 | 4% | ✅ |
| 0.3 | 44 | bjb1-18228 | eval_object_perdof_norm03_seed44.json | 10 | 4% | ✅ |
| 0.3 | 45 | bjb1-32546 | eval_object_perdof_norm03_seed45_r2.json | 10 | 6% | ✅ |
| default | 42 | bjb1-18228 | eval_object_perdof_default_norm_r2.json | 10 | 0% | ✅ |
| default | 46 | bjb1-32546 | eval_object_perdof_default_seed46.json | 10 | 0% | ✅ |

### n_rollouts=20 的完整列表

| JSON 文件 | server | 数据组 | seed | SR | 在核心数据中? |
|-----------|--------|--------|------|----|---------------|
| eval_object_obs_only_default_seed45.json | bjb2-28827 | obs_only uncapped | 45 | 12% | magnitude curve |
| eval_object_obs_only_norm01_seed45.json | bjb1-18228 | obs_only ε=0.1 | 45 | 14% | magnitude curve |
| eval_object_perdof_norm02_seed45.json | bjb2-28827 | perdof ε=0.2 | 45 | 9% | magnitude curve (已有 r3 替换) |
| eval_object_vla_only_seed45.json | bjb2-28827 | VLA-only baseline | 45 | 9% | **论文 Table** |
| eval_object_scalar_seed45.json | bjb2-28827 | scalar CRM | 45 | 9% | **论文 Table** |

**模式：所有 n_rollouts=20 的实验都是 seed45，集中在 bjb2-28827 服务器上的早期批次。后续在其他服务器重跑的实验（如 r2/r3）已修正为 n_rollouts=10。**

### 结论

1. **论文主结果（obs_only ε=0.2，6 seeds）：✅ 无混用**，全部 n_rollouts=10
2. **Argmin baseline（6 seeds）：✅ 无混用**，全部 n_rollouts=10
3. **VLA-only baseline：❌ seed45 混用了 n_rollouts=20**（其余 4 seeds 都是 10）
4. **Scalar CRM：❌ seed45 混用了 n_rollouts=20**（seed42 文件已删，seed43/44 是 10）
5. **Magnitude curve obs_only：❌ ε=0.1 seed45 和 default seed45 用了 n_rollouts=20**
6. **Magnitude curve perdof：❌ ε=0.2 seed45 原始数据用了 n_rollouts=20**（但已有 r3 替换，n_rollouts=10，SR=12%）

**需要行动：**
- VLA-only seed45 需要用 n_rollouts=10 重跑
- Scalar seed45 需要用 n_rollouts=10 重跑
- obs_only ε=0.1 seed45 需要用 n_rollouts=10 重跑（目前 eval-obs-only-object-norm01-seed48 RUNNING，但 seed45 的 redo 未启动）
- obs_only default seed45 需要用 n_rollouts=10 重跑
- perdof ε=0.2 seed45：已有 r3 (n_rollouts=10, SR=12%)，可直接替换

---

## Part B: perdof ε=0.2 核实

### 完整 seed 列表

| seed | 原始文件 | 原始 SR | 原始 n_rollouts | r3 文件 | r3 SR | r3 n_rollouts | 建议使用 |
|------|----------|---------|-----------------|---------|-------|---------------|----------|
| 42 | bjb1-32546: eval_object_perdof_norm02.json | 11% | 10 | — | — | — | 11%（原始）|
| 43 | bjb2-28827: eval_object_perdof_norm02_seed43_r3.json | 9% | 10 | (本身是 r3) | — | — | 9%（r3）|
| 44 | bjb2-28827: eval_object_perdof_norm02_seed44.json | 10% | 10 | — | — | — | 10%（原始）|
| 45 | bjb2-28827: eval_object_perdof_norm02_seed45.json | 9% | **20** | bjb1-18228: eval_object_perdof_norm02_seed45_r3.json | 12% | 10 | **12%（r3）** |
| 46 | bjb2-28827: eval_object_perdof_norm02_seed46.json | 9% | 10 | — | — | — | 9%（原始）|
| 47 | bjb2-28827: eval_object_perdof_norm02_seed47.json | 11% | 10 | — | — | — | 11%（原始）|

### Reviewer #37 的 [14, 9, 10, 12, 9, 11] 分析

Reviewer 给出的值：[14, 9, 10, 12, 9, 11]，mean ≈ 10.83%

逐项对比：

| 位置 | Reviewer 值 | 实际 perdof ε=0.2 | 匹配? | 分析 |
|------|------------|-------------------|-------|------|
| seed42 | 14% | 11% | **❌** | **14% 是 perdof ε=0.03 seed42 的值**，不是 ε=0.2 |
| seed43 | 9% | 9% | ✅ | |
| seed44 | 10% | 10% | ✅ | |
| seed45 | 12% | 原始 9% / r3 12% | ✅(r3) | Reviewer 用的是 r3 替换值 |
| seed46 | 9% | 9% | ✅ | |
| seed47 | 11% | 11% | ✅ | |

**结论：Reviewer #37 的 14% 是错误的，混淆了 perdof ε=0.03 seed42 (SR=14%) 和 perdof ε=0.2 seed42 (SR=11%)。**
其余 5 个值正确，且 Reviewer 已正确采用了 seed45 的 r3 替换值（12%）。

### 建议 mean

**使用 r3 替换 seed45（必须替换，因为原始数据 n_rollouts=20 不一致）：**

| seed | SR | n_rollouts |
|------|----|------------|
| 42 | 11% | 10 ✅ |
| 43 | 9% | 10 ✅ |
| 44 | 10% | 10 ✅ |
| 45 | **12%**（r3 替换） | 10 ✅ |
| 46 | 9% | 10 ✅ |
| 47 | 11% | 10 ✅ |

**n=6, mean = (11+9+10+12+9+11)/6 = 62/6 = 10.33%**

对比：
- 当前论文值（含 n_rollouts=20 的原始 seed45=9%）: mean = 9.83%
- 修正后（r3 seed45=12%）: **mean = 10.33%**
- Reviewer #37 的值（含错误 14%）: mean = 10.83%

如果 seed48（当前 RUNNING, exp_id=eval-perdof-object-norm02-seed48）完成后加入：
- n=7, mean 待定
