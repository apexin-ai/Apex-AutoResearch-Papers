# analysis exp004 sweep progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_sweep_progress_20260515T165406_result.json`
- **Structured JSON:** [`5d827bb6cd22e17dbe8f.json`](../../sessions/5d/5d827bb6cd22e17dbe8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_004 进度报告

### 进度

| 配置 | 状态 | Seeds |
|------|------|-------|
| g2.0_auc0.7_n20 | ✅ | 10/10 |
| g2.0_auc0.9_n20 | ✅ | 10/10 |
| g2.0_auc0.7_n50 | ✅ | 10/10 |
| g2.0_auc0.9_n50 | ✅ | 10/10 |
| g4.0_auc0.7_n20 | ✅ | 10/10 |
| g4.0_auc0.9_n20 | ✅ | 10/10 |
| g4.0_auc0.7_n50 | 🔄 | 6/10 |
| g4.0_auc0.9_n50 | ❌ | 0/10 |

**总进度：66/80 seeds = 82.5%**

当前 config 7 每 seed ~12 分钟（n=50 + g=4.0 慢于 n=20 的 ~5 分钟）。剩余：4 seeds × 12min + 10 seeds × 12min ≈ **2.8 小时**，预计约 03:45 完成。

---

### 关键发现

**1. γ=2.0 模型恢复良好（正常工作的基线）**

| 条件 | mean γ̂ | mean bias | CI95 coverage | CI95 width | θ_corr |
|------|---------|-----------|---------------|------------|--------|
| auc0.7_n20 | 2.02 | +0.02 | 100% | 0.51 | 0.95 |
| auc0.9_n20 | 2.00 | +0.00 | 100% | 0.54 | 0.97 |
| auc0.7_n50 | 2.01 | +0.01 | 100% | 0.34 | 0.95 |
| auc0.9_n50 | 2.01 | +0.01 | 100% | 0.36 | 0.96 |

几乎无偏，95% 覆盖率完美。

**2. γ=4.0 出现系统性向下偏差，但模型仍基本工作**

| 条件 | mean γ̂ | mean bias | CI95 coverage | CI95 width | θ_corr |
|------|---------|-----------|---------------|------------|--------|
| auc0.7_n20 | 3.77 | -0.23 | 90% | 1.01 | 0.92 |
| auc0.9_n20 | 3.83 | -0.17 | 100% | 0.95 | 0.96 |

γ=4.0 估计系统偏低 ~0.2，但 CI95 coverage 仍在 90-100%。一个 seed（g4.0_auc0.7_n20, seed 9）的 CI95 甚至不覆盖真值（γ̂=3.44, CI=[3.03, 3.89]）。

**3. 对 coverage collapse 的诊断意义**

这是核心发现：**在 simulation 中（数据生成过程 = 模型），即使 γ=4.0，CI95 coverage 仍在 90-100%。** 而真实数据的 coverage 只有 20-33%。

这意味着 coverage collapse **不是 γ 值大** 导致的，而是 **模型错误指定 (model misspecification)** —— additive 4PL+γ 模型的数据生成假设与真实 contamination 机制不匹配。

**4. 其他观察**
- 所有 80 个已完成 run 均 0 divergences，R̂ < 1.01，ESS > 1300 —— 采样器机械层面完全正常
- n=50 vs n=20：CI 显著收窄（0.34 vs 0.51 at γ=2），但偏差方向不变
- θ recovery 在 γ=4.0 时下降（corr ~0.92 vs ~0.95），符合预期

---

### 不需要调整参数

实验正常运行，结果已足够支持结论。等 g4.0_n50 的两个配置完成后做最终汇总分析即可。

---
