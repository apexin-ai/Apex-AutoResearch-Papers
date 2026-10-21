# Eval Completeness Audit — occsafe_vla

> 审计日期: 2026-05-24 | 总实验: 67 | 成功: 52 | 负向: 3 | 失败/killed: 4 | RUNNING: 8

## 审计标准

每个有 eval 的实验检查以下 4 项：
1. **50r** — eval_rollouts = 50（500 episodes / 10 tasks）
2. **Per-task** — T0-T9 的 TSR 和 CAR breakdown
3. **@50000** — checkpoint step 为 50000（非 47500）
4. **at_50000_50r 格式** — registry 中使用 `at_50000_50r` 嵌套格式（旧格式）或顶层等价（新格式）

---

## A. 完整（50r + per-task + @50000）— 24 个

| # | exp_id | 条件 | Seed | CAR | TSR | 数据来源 |
|---|--------|------|------|-----|-----|----------|
| 1 | mvp_vanilla_s0 | Vanilla | s0 | 0.788 | 0.900 | at_50000_50r |
| 2 | mvp_vanilla_s1 | Vanilla | s1 | 0.766 | 0.918 | at_50000_50r |
| 3 | mvp_vanilla_s2 | Vanilla | s2 | 0.786 | 0.904 | at_50000_50r |
| 4 | mvp_occ_s0 | Full OCC | s0 | 0.832 | 0.904 | at_50000_50r |
| 5 | occ_s1_fresh | Full OCC | s1 | 0.788 | 0.938 | at_50000_50r |
| 6 | mvp_occ_s2 | Full OCC | s2 | 0.770 | 0.840 | at_50000_50r |
| 7 | ablation_occ_detach_s0 | Detach | s0 | 0.746 | 0.914 | at_50000_50r |
| 8 | ablation_occ_detach_s1 | Detach | s1 | 0.744 | 0.898 | at_50000_50r |
| 9 | ablation_random_occ_s0 | Random OCC | s0 | 0.814 | 0.856 | at_50000_50r |
| 10 | ablation_random_occ_s1 | Random OCC | s1 | 0.798 | 0.902 | at_50000_50r |
| 11 | cutoff_s0_eval | cutoff_35k | s0 | 0.768 | 0.912 | 顶层 50r |
| 12 | cutoff_s1_eval | cutoff_35k | s1 | 0.798 | 0.918 | 顶层 50r |
| 13 | cutoff_s2_v2_eval | cutoff_35k | s2 | 0.770 | 0.970 | 顶层 50r (推断) |
| 14 | cutoff_15k_s0_eval | cutoff_15k | s0 | 0.804 | 0.912 | 顶层 50r |
| 15 | cutoff_25k_s0_eval | cutoff_25k | s0 | 0.688 | 0.844 | 顶层 50r |
| 16 | cutoff_25k_s1_eval | cutoff_25k | s1 | 0.760 | 0.930 | 顶层 50r |
| 17 | reverse_cutoff_s0_eval | reverse_cutoff | s0 | 0.700 | 0.788 | 顶层 50r |
| 18 | reverse_cutoff_s1_eval | reverse_cutoff | s1 | 0.736 | 0.890 | 顶层 50r |
| 19 | depth_s0_eval | Depth | s0 | 0.736 | 0.940 | 顶层 50r |
| 20 | depth_s1_eval | Depth | s1 | 0.818 | 0.906 | 顶层 50r |
| 21 | depth_s2 | Depth | s2 | 0.758 | 0.860 | 顶层 50r |
| 22 | depth_s3 | Depth | s3 | 0.806 | 0.848 | 顶层 50r |
| 23 | detach_ln_s1_eval | Detach+LN | s1 | 0.756 | 0.906 | 顶层 50r |
| 24 | detach_ln_s2_eval | Detach+LN | s2 | 0.748 | 0.884 | 顶层 50r |

## B. 50r eval 但缺少 per-task breakdown — 5 个

| # | exp_id | 条件 | Seed | CAR | TSR | 缺失项 |
|---|--------|------|------|-----|-----|--------|
| 1 | ablation_occ_detach_s2 | Detach | s2 | 0.748 | 0.624 | per_task；_eval 记录为空 |
| 2 | ablation_random_occ_s2 | Random OCC | s2 | 0.754 | 0.848 | per_task；_eval 记录为空 |
| 3 | cutoff_45k_s0_eval | cutoff_45k | s0 | 0.764 | 0.896 | per_task |
| 4 | detach_ln_s0_eval | Detach+LN | s0 | 0.792 | 0.914 | per_task |
| 5 | vanilla_retrain_s0_eval | Vanilla retrain | s0 | 0.768 | 0.882 | per_task |

**注意**: ablation_occ_detach_s2 的 TSR=0.624 异常低（s0/s1 的 TSR=0.914/0.898），需要核查。

## C. 分析类实验（无需 eval）— 5 个

| # | exp_id | 类型 |
|---|--------|------|
| 1 | cka_analysis | CKA 表征分析 |
| 2 | cka_detach_ln | CKA Detach+LN 分析 |
| 3 | cka_random_occ | CKA Random OCC 分析 |
| 4 | gradient_analysis | 梯度分析 |
| 5 | gradient_analysis_mixed_seed | 混合 seed 梯度分析 |

## D. 训练实验与 eval 对应关系

### D1. 训练实验有对应 eval — 15 个 ✓

| 训练 exp_id | eval exp_id | eval 状态 |
|-------------|-------------|-----------|
| cutoff_15k_s0 | cutoff_15k_s0_eval | ✓ 完整 |
| cutoff_25k_s0 | cutoff_25k_s0_eval | ✓ 完整 |
| cutoff_25k_s1 | cutoff_25k_s1_eval | ✓ 完整 |
| cutoff_45k_s0 | cutoff_45k_s0_eval | ⚠ 缺 per-task |
| cutoff_s0 | cutoff_s0_eval | ✓ 完整 |
| cutoff_s1 | cutoff_s1_eval | ✓ 完整 |
| cutoff_s2_v2 | cutoff_s2_v2_eval | ✓ 完整 |
| depth_s0 | depth_s0_eval | ✓ 完整 |
| depth_s1 | depth_s1_eval | ✓ 完整 |
| detach_ln_s0 | detach_ln_s0_eval | ⚠ 缺 per-task |
| detach_ln_s1 | detach_ln_s1_eval | ✓ 完整 |
| detach_ln_s2 | detach_ln_s2_eval | ✓ 完整 |
| reverse_cutoff_s0 | reverse_cutoff_s0_eval | ✓ 完整 |
| reverse_cutoff_s1 | reverse_cutoff_s1_eval | ✓ 完整 |
| vanilla_retrain_s0 | vanilla_retrain_s0_eval | ⚠ 缺 per-task |

### D2. 训练实验无 eval — 1 个 ✗

| 训练 exp_id | 条件 | 说明 |
|-------------|------|------|
| **full_occ_retrain_s0** | Full OCC retrain | 训练完成，未跑 eval |

### D3. 空 eval 记录 — 2 个

| eval exp_id | 对应训练 | 说明 |
|-------------|----------|------|
| ablation_occ_detach_s2_eval | ablation_occ_detach_s2 | 标记 success 但 metrics 为空 |
| ablation_random_occ_s2_eval | ablation_random_occ_s2 | 标记 success 但 metrics 为空 |

eval 数据记录在训练 exp 中（50r, @50000），但缺 per-task。这两个 _eval 实验的结果 JSON 可能在服务器上仍然存在。

## E. 只有 @47500 没有 @50000 eval — 0 个

所有旧 OCC 实验（mvp_occ_s0, mvp_occ_s2, occ_s1_fresh）均有 at_50000_50r 和 at_47500_50r 两个 checkpoint 的 eval。无实验仅有 47500 eval。

**注意**: mvp_occ_s0 和 mvp_occ_s2 的顶层 CAR/TSR 是 20r@47500 的旧数据，50r@50000 数据在 `at_50000_50r` 字段中。

## F. 只有 20r eval — 1 个

| exp_id | 条件 | 20r CAR | 说明 |
|--------|------|---------|------|
| mvp_occ_s1 | Full OCC | 0.685 | 已被 occ_s1_fresh (50r) 替代，不影响 |

---

## Dose-Response 条件 Eval 覆盖

### 核心条件（用于论文 Figure）

| 条件 | Seeds | 50r@50K | Per-task | 完整度 | 缺失 |
|------|-------|---------|----------|--------|------|
| **Full OCC** | s0,s1,s2 | ✓✓✓ | ✓✓✓ | **100%** | — |
| **Detach** | s0,s1,s2 | ✓✓✓ | ✓✓✗ | **67%** | s2 per-task |
| **Vanilla** | s0,s1,s2 | ✓✓✓ | ✓✓✓ | **100%** | — |
| **Random OCC** | s0,s1,s2 | ✓✓✓ | ✓✓✗ | **67%** | s2 per-task |
| **Detach+LN** | s0,s1,s2 | ✓✓✓ | ✗✓✓ | **67%** | s0 per-task |
| **Depth** | s0,s1,s2,s3 | ✓✓✓✓ | ✓✓✓✓ | **100%** | — |

### Dose-Response 曲线条件

| 条件 | Seeds | 50r@50K | Per-task | 完整度 | 缺失 |
|------|-------|---------|----------|--------|------|
| **cutoff_15k** | s0 | ✓ | ✓ | **100%** | — |
| **cutoff_25k** | s0,s1 | ✓✓ | ✓✓ | **100%** | — |
| **cutoff_35k** | s0,s1,s2 | ✓✓✓ | ✓✓✓ | **100%** | — |
| **cutoff_45k** | s0 | ✓ | ✗ | **0%** | per-task |
| **reverse_cutoff** | s0,s1 | ✓✓ | ✓✓ | **100%** | — |

### 补充条件

| 条件 | Seeds | 50r@50K | Per-task | 完整度 | 缺失 |
|------|-------|---------|----------|--------|------|
| **Vanilla retrain** | s0 | ✓ | ✗ | **0%** | per-task |
| **Full OCC retrain** | s0 | ✗ | ✗ | **0%** | 未跑 eval |

---

## Negative 实验 Eval 完整性

| exp_id | 50r@50K | Per-task | at_50000_50r | 说明 |
|--------|---------|----------|-------------|------|
| mvp_occ_s0 | ✓ | ✓ | ✓ | 完整 |
| mvp_occ_s1 | ✗ (20r) | ✓ (20r) | ✗ | 已被 occ_s1_fresh 替代 |
| mvp_occ_s2 | ✓ | ✓ | ✓ | 完整 |

---

## 行动项

### P0 — 阻塞论文图表

| # | exp_id | 需要补什么 | 说明 | 工作量 |
|---|--------|-----------|------|--------|
| — | 无 | — | 所有 dose-response 核心数据点（CAR/TSR）已有 50r@50000 eval | — |

### P1 — 补 per-task 到 registry（可能不需要重跑 eval）

eval 结果 JSON 文件可能在服务器上仍然存在，per-task 数据只是没有录入 registry。**优先尝试从服务器上的 JSON 文件提取 per-task，而非重跑 eval。**

| # | exp_id | 需要补什么 | 可能的 JSON 路径 | 优先级 |
|---|--------|-----------|----------------|--------|
| 1 | ablation_occ_detach_s2 | per-task breakdown | 服务器 result JSON | P1 |
| 2 | ablation_random_occ_s2 | per-task breakdown | 服务器 result JSON | P1 |
| 3 | cutoff_45k_s0_eval | per-task breakdown | 服务器 result JSON | P1 |
| 4 | detach_ln_s0_eval | per-task breakdown | 服务器 result JSON | P1 |
| 5 | vanilla_retrain_s0_eval | per-task breakdown | 服务器 result JSON | P1 |

### P2 — 需要跑 eval

| # | exp_id | 需要补什么 | 优先级 |
|---|--------|-----------|--------|
| 1 | full_occ_retrain_s0 | 完整 50r eval | P2（仅梯度分析参考需要） |

### P3 — 数据异常需核查

| # | exp_id | 异常 | 说明 |
|---|--------|------|------|
| 1 | ablation_occ_detach_s2 | TSR=0.624 | 远低于 s0 (0.914) 和 s1 (0.898)，可能 eval 异常或数据录入错误 |

---

## 统计摘要

- **完整 eval (50r+per-task+@50000)**: 24/32 有 eval 的实验 (75%)
- **50r@50000 但缺 per-task**: 5/32 (16%)
- **无 eval（训练实验有对应 _eval）**: 15 个（全部已有）
- **无 eval（训练实验无 _eval）**: 1 个 (full_occ_retrain_s0)
- **分析类（不需要 eval）**: 5 个
- **Dose-response 核心 CAR/TSR 覆盖率**: 100%（所有条件均有 50r@50000）
- **Dose-response per-task 覆盖率**: ~85%（5 个缺 per-task，均可能从服务器 JSON 补录）
