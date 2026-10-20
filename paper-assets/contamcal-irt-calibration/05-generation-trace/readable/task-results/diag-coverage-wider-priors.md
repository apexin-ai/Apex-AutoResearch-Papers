# diag coverage wider priors

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_coverage-wider-priors_20260514T231108_result.json`
- **Structured JSON:** [`9152bd97de176d8b3e16.json`](../../sessions/91/9152bd97de176d8b3e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full deliverable.

---

## 线 2：Coverage 诊断 + Wider Priors Ablation

### 1. 当前 Stan 模型先验定义

**Original (`contam_irt_4pl_simple.stan`)**:
```stan
theta ~ normal(0, 1);
a ~ lognormal(0, 0.5);
b ~ normal(0, 1);
c ~ beta(5, 20);    // guessing ≈ 0.2
d ~ beta(20, 5);    // upper asymptote ≈ 0.8
gamma ~ normal(0, 1);
```

**Wider (`contam_irt_4pl_simple_wider.stan`)**:
```stan
theta ~ normal(0, 3);
a ~ lognormal(0, 1);
b ~ normal(0, 3);
c ~ beta(2, 8);
d ~ beta(8, 2);
gamma ~ normal(0, 5);
```

### 2. Wider Prior Ablation 结果

| Model | Original cal_score [95% CI] | Wider cal_score [95% CI] | GT | Orig | Wider |
|-------|---------------------------|--------------------------|------|------|-------|
| M0 (0.5B d000) | 0.479 [0.455, 0.504] | 0.467 [0.445, 0.487] | 0.469 | ✓ | ✓ |
| M1 (0.5B d005) | 0.393 [0.366, 0.421] | 0.355 [0.338, 0.372] | 0.469 | ✗ | ✗ |
| M2 (0.5B d025) | 0.437 [0.390, 0.484] | 0.352 [0.332, 0.371] | 0.469 | ✓ | ✗ |
| M3 (0.5B d100) | 0.539 [0.424, 0.637] | 0.316 [0.281, 0.350] | 0.469 | ✓ | ✗ |
| M4 (1.5B d000) | 0.738 [0.720, 0.755] | 0.714 [0.700, 0.727] | 0.772 | ✗ | ✗ |
| M5 (1.5B d005) | 0.744 [0.726, 0.760] | 0.713 [0.699, 0.727] | 0.772 | ✗ | ✗ |
| M6 (1.5B d025) | 0.761 [0.742, 0.776] | 0.712 [0.696, 0.727] | 0.772 | ✓ | ✗ |
| M7 (1.5B d100) | 0.790 [0.769, 0.802] | 0.711 [0.687, 0.732] | 0.772 | ✓ | ✗ |

| 指标 | Original | Wider | 变化 |
|------|----------|-------|------|
| **Coverage_95** | **0.625** | **0.125** | **−0.500** |
| Coverage_80 | 0.250 | 0.125 | −0.125 |
| Coverage_50 | 0.000 | 0.125 | +0.125 |
| Avg CI width | 0.068 | 0.039 | −0.029 |
| γ mean | −2.347 | +0.368 | — |
| γ 95% CI | [−3.46, −1.19] | [−1.92, +2.81] | 宽度 2.27→4.73 |
| R̂ max | 1.010 | 1.010 | same |
| ESS min | 817 | 378 | −439 |
| Divergences | 0 | 0 | same |

**关键观察**: 放宽先验后 coverage 从 62.5% 恶化到 12.5%。CI 宽度反而更窄（0.039 vs 0.068）。γ 估计从 −2.35 变到 +0.37——完全不同的后验模式。对 1.5B 模型（M4-M7），wider 模型的 calibrated scores 几乎相同（0.710-0.714），失去了区分不同 exposure 水平的能力。

### 3. EXP-004 N_models vs Coverage 关系

From exp-004 simulation sweep (true γ=0.5, 48/120 runs):

| N_models | AUC=0.55 Coverage_95 | AUC=0.80 Coverage_95 | CI Width (0.55) | CI Width (0.80) |
|----------|---------------------|---------------------|-----------------|-----------------|
| 20 | **80%** (8/10) | **90%** (9/10) | 0.133 | 0.258 |
| 50 | **90%** (9/10) | **100%** (10/10) | 0.087 | 0.163 |
| 100 | **100%** (7/7) | **100%** (1/1†) | 0.064 | 0.116† |

N=8 不在 sweep 范围内（最小 N=20），但外推趋势清晰：N 越小，coverage 越差。exp-004 在 N=20 时 coverage 已降到 80-90%，N=8 预期会更差。

### 4. 结论：Coverage 崩塌的根因与修复

**根因：N=8 下 calibrated score 的系统性偏差，不是先验问题。**

三层机制叠加：

1. **参数不可辨识（主因）**：N=8 模型 + 4PL 有 ~4700 个参数。虽然 MCMC 诊断正常（无 divergence，R̂ < 1.01），但 γ 和 θ 之间存在强相关。放宽先验后 γ 从 −2.35 跳到 +0.37，证明 γ 在 N=8 下高度不稳定。

2. **CLT 压缩 CI 宽度**：calibrated score = 1172 个 item 的后验均值，CLT 使 CI 宽度 ~σ/√1172 ≈ 0.03-0.07。这比 calibrated score 的实际偏差（0.03-0.15）窄得多，导致 GT 落在 CI 外。

3. **先验无法弥补**：1172 个 item 的似然主导了后验。放宽先验只是让模型找到另一个（更差的）模式，CI 宽度甚至更窄。

**修复方案（按优先级）**：

| 方案 | 预期效果 | 依据 |
|------|---------|------|
| **增加 N_models ≥ 20** | Coverage 80-90% | exp-004: N=20 coverage=80-90% |
| **增加 N_models ≥ 50** | Coverage 90-100% | exp-004: N=50 coverage=90-100% |
| 降低模型复杂度（2PL） | 减少参数、提高可辨识性 | 4PL 在 N=8 下过参数化 |
| 放宽先验 | **无效甚至有害** | 本实验证明：coverage 从 62.5%→12.5% |

**实操建议**：当前 ARC v2 数据只有 0.5B×4 + 1.5B×4 = 8 个模型。加入 seed=123 数据可到 ~12-16 个模型，但仍不够。要达到论文可报告的 coverage（≥90%），至少需要 N≥50 个模型，或者换用参数更少的 2PL 模型。

---
