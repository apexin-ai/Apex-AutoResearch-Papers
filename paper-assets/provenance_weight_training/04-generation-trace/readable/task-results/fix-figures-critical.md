# fix figures critical

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_figures_critical_20260524T044405_result.json`
- **Structured JSON:** [`0720b38be631e93298c9.json`](../../sessions/07/0720b38be631e93298c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8 个文件全部生成（4 figure × pdf/png）。

---

## 修改汇总

### Fix 1: Fig 2 constraint_regime_decomposition — τ=0.8 → τ=0.7
| 字段 | ρ=0.4 旧值 (τ=0.8) | ρ=0.4 新值 (τ=0.7) | ρ=0.6 旧值 | ρ=0.6 新值 |
|------|-----|-----|-----|-----|
| α_eff binding | 38.2% | **50.9%** | 33.4% | **46.8%** |
| ESS binding | 59.8% | **43.3%** | 66.0% | **48.7%** |
| Clean | 2.0% | **5.8%** | 0.6% | **4.5%** |

数据来源：τ=0.7 3-seed (seed42/123/456) step_metrics.jsonl 实时提取

### Fix 2: Fig 4 dr_dual_curve — adaptive 参考线
- 旧值：**17.651**（实际是 grid b=0.5 seed42 的 PPL）
- 新值：**17.674**（τ=0.7 3-seed adaptive mean = (17.680+17.666+17.677)/3）

### Fix 3: Fig 3 τ=0.8 PPL — 保持 17.6527
- 脚本值 17.6527 来自 `adaptive_fix_seed42`（n_min=2 修正版）
- Registry 中 17.644 来自 `adaptive_seed42`（n_min=3 原始版，有 bug）
- tau sweep 其他数据点均使用相同实验体系，**17.6527 是一致且正确的值**，不修改

### 生成文件路径
```
/root/provenance_weight_training/output/figures/
├── constraint_regime_decomposition.pdf  (22KB)
├── constraint_regime_decomposition.png  (53KB)
├── dr_dual_curve.pdf                    (29KB)
├── dr_dual_curve.png                    (103KB)
├── grid_b_trend_clean.pdf               (21KB)
├── grid_b_trend_clean.png               (88KB)
├── tau_rho_rank_preservation.pdf         (27KB)
└── tau_rho_rank_preservation.png         (118KB)
```

### 验证清单
- [x] Fig 2 柱状图数据 ≈ 50.9/43.3/5.8（ρ=0.4）
- [x] Fig 4 adaptive 参考线 = 17.674
- [x] Fig 3 τ=0.8 数据点 = 17.6527（与 adaptive_fix 一致，保持不变）
- [x] 所有 figure 重新生成成功

---
