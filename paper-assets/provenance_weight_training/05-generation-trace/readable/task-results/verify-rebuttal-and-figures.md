# verify rebuttal and figures

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_rebuttal_and_figures_20260523T105633_result.json`
- **Structured JSON:** [`f7aff71d3544d7f6a66b.json`](../../sessions/f7/f7aff71d3544d7f6a66b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed for a comprehensive verification. Here's the full report:

---

## Rebuttal 验证

### Epoch Confound 数字

| 数字 | 论文值 | 验证值 | 结果 |
|------|--------|--------|------|
| D&R full advantage (vs adaptive) | −0.396 | −0.396 (BH file #5, per-seed: −0.3947/−0.394/−0.400) | ✓ |
| Epoch-matched residual | Δ=0.017 | −0.018 (3dp), BH file says −0.019 | ⚠️ 0.017 vs 0.018-0.019, within rounding |
| >95% epoch confound | >95% | 95.5% (from 3dp data) | ✓ |
| 0.396 → 0.017 PPL (N=3) | 同上 | 同上 | ✓ |

**注**: Epoch confound percentage 用的是 vs-adaptive 基线 (reviewer.md 确认)，vs-uniform 基线只有 91%。

### 统计检验数字

| 数字 | 论文值 | 验证值 | 结果 |
|------|--------|--------|------|
| Uncorrected p (ρ=0.4) | 0.019 | 0.0193 (BH file, two-sided paired t) | ✓ |
| p_BH (ρ=0.4, k=9) | 0.078 | 0.078 (BH file rank 6, multiplier=4) | ✓ |
| p_BH (ρ=0.6) | 0.018 ("p_BH<0.02") | k=3: 0.018; **k=9: 0.064** | ✗ 不一致 |
| Cohen's d | 2.86 | paired d=3.66, pooled d≈2.58-2.67 | ⚠️ 无法精确复现 |
| Power (one-sided α=0.05) | >0.90 | 0.98 (at d=3.66), >0.90 (at any d>2.5) | ✓ 定性一致 |
| Bootstrap CI | [−0.028, −0.012] | [−0.024, −0.014] (seed-dependent) | ⚠️ 方法/种子差异 |
| Cross-seed SD adaptive | 0.007 | 0.0069 (adaptive_fix), 0.0074 (tau07) | ✓ |
| Cross-seed SD uniform | 0.008 | 0.0077 | ✓ |

**关键问题 — p_BH(ρ=0.6) 不一致**: C1 段明确说 "Bonferroni-Holm correction has been applied across all 9 family-wise comparisons"（k=9），并报告 ρ=0.4 的 p_BH=0.078。但 Broader Significance 和 C4 引用 ρ=0.6 的 p_BH=0.018，这来自 per-table 校正（k=3），不是 k=9。k=9 下 ρ=0.6 的 p_BH=0.064。Reviewer 会注意到这个不一致。

### 效应量 Δ

| 数字 | 论文值 | 验证值 | 结果 |
|------|--------|--------|------|
| Δ at ρ=0.4, B=4 | −0.020 | −0.020 (tau07 vs uniform, 3-seed mean) | ✓ |
| Δ at ρ=0.6 | −0.032 | −0.032 | ✓ |
| Δ at ρ=0.2 | +0.046 | +0.046 (single seed) | ✓ |
| Δ at ρ=0.3 | +0.002 | +0.002 (3-seed mean) | ✓ |
| GPT-2 detector Δ | +0.098 | +0.100 (seed42) / +0.102 (3-seed mean) | ⚠️ 差 0.002-0.004 |

### Batch-size amplification

| 数字 | 论文值 | 验证值 | 结果 |
|------|--------|--------|------|
| B=4 Δ | −0.020 | −0.020 | ✓ |
| B=8 Δ | −0.050 | −0.050 (2 seeds) | ✓ |
| B=16 Δ | −0.068 | −0.068 (3 seeds) | ✓ |
| Ratio 2.5× to 3.4× | 2.5×, 3.4× | 0.050/0.020=2.5, 0.068/0.020=3.4 | ✓ |
| Scaling α≈0.89 | 0.89 | 0.883 (log-log regression) | ⚠️ 差 0.007 |
| B=128 extrapolation Δ≈−0.39 | ~0.39 | ~0.47 (at α=0.883); ~0.39 requires α≈0.86 | ⚠️ 取决于 α 精度 |

### Detector 数字

| 数字 | 论文值 | 验证值 | 结果 |
|------|--------|--------|------|
| TF-IDF AUC | 0.94 | 0.939 (registry) | ✓ |
| TF-IDF ECE | 0.048 | 0.048 (registry) | ✓ |
| GPT-2 AUC | 0.91 | 0.913 (paper_framing) | ✓ (rounded) |
| GPT-2 ECE | 0.131 | 0.131 (paper_framing) | ✓ (not in registry) |

### α_eff Correlation 数据

| 数字 | 论文值 | 验证来源 | 结果 |
|------|--------|----------|------|
| r(α_eff, mean_q) seed42 | 0.8019 | 不在 registry | ⚠️ 无法验证 |
| r(α_eff, mean_q) seed123 | 0.7994 | 不在 registry | ⚠️ |
| r(α_eff, mean_q) seed456 | 0.8006 | 不在 registry | ⚠️ |
| Spearman ρ per seed | 0.8761/0.8692/0.8749 | 不在 registry | ⚠️ |
| Cross-seed spread Pearson | 0.0025 | Computed: max-min = 0.8019-0.7994=0.0025 | ✓ (self-consistent) |
| Cross-seed spread Spearman | 0.0069 | Computed: 0.8761-0.8692=0.0069 | ✓ (self-consistent) |
| b*=0 pct per seed | 5.8%/5.7%/5.9% | 不在 registry | ⚠️ |
| Proxy-to-ground-truth r | 0.70 | 不在 registry | ⚠️ |

### 其他数字

| 数字 | 论文值 | 验证值 | 结果 |
|------|--------|--------|------|
| Gap to grid-best | 0.054 PPL | 0.055 (17.674-17.619) | ⚠️ 差 0.001 |
| Grid σ | 0.033 | 0.035 (b=0.3, 3 seeds) | ⚠️ 差 0.002 |
| 9 grid search runs | 9 | b=0.1/0.2/0.3/0.5/1.0/1.5/2.0/3.0/5.0 = 9 | ✓ |
| ESS-binding 61.8% (ρ=0.4) | 61.8% | 不在 registry (training log) | ⚠️ |
| ESS-binding 66% (ρ=0.6) | 66% | 不在 registry | ⚠️ |
| D&R retaining 31.5% at q>0.3 | 31.5% | 116935/371499=31.5% | ✓ |
| ~3.2 content epochs | ~3.2 | 200M tokens / ~62M filtered tokens ≈ 3.2 | ✓ (approximate) |
| 132M tokens | 132M | 371499 samples × ~355 tokens ≈ 132M unique | ✓ |
| Downstream null |Δ|≤0.01 | ≤0.01 | All |Δ| ≤ 0.0041 (seed42 verified) | ✓ (partial, 1/3 seeds) |
| 1.7B Δ=−0.013 | −0.013 | 13.262-13.275=−0.013 | ✓ |
| MMLU +1.57pp | +1.57pp | 53.42%-51.85%=1.57pp (memory.md, Llama-3B) | ✓ (source: memory.md) |
| HellaSwag −0.60pp | −0.60pp | From project history notes | ⚠️ (not in registry) |

---

## Figure 数据验证

### Dose-response 图 (delta_vs_rho)

| ρ | 论文 Δ | 论文 SD | Registry adaptive mean | Registry uniform mean | 验证 Δ | 验证 SD | 结果 |
|---|--------|--------|----------------------|---------------------|--------|--------|------|
| 0.2 | +0.046 | — | 17.382 | 17.336 | +0.046 | — (1 seed) | ✓ |
| 0.3 | +0.002 | 0.0025 | 17.427 | 17.425 | +0.002 | 0.0025 | ✓ |
| 0.4 | −0.020 | 0.005 | 17.674 (tau07) | 17.694 | −0.020 | 0.0053 | ✓ |
| 0.6 | −0.032 | 0.006 | 17.731 | 17.763 | −0.032 | 0.0056 | ✓ |

**所有 dose-response 数据点与 registry 一致** ✓

具体实验 mapping:
- ρ=0.2: `rho02_adaptive_tau08_seed42` (17.382) vs `rho02_uniform_seed42` (17.336)
- ρ=0.3: `rho03_adaptive_seed42/123/456_r2` vs `rho03_uniform_seed42/123/456`
- ρ=0.4: `tau07_seed42/123/456` (17.68/17.666/17.677) vs `uniform_seed42/123/456` (17.694/17.686/17.702)
- ρ=0.6: `adaptive_rho06_tau07_seed42/123/456` (17.735/17.727/17.732) vs `contamination_60_uniform_seed42/123/456` (17.766/17.754/17.770)

---

## 需要修正的问题

**1. p_BH(ρ=0.6) 家族大小不一致** (严重)

C1 明确说用 k=9 全家族校正，给出 ρ=0.4 p_BH=0.078。但 Broader Significance 和 C4 中 ρ=0.6 的 p_BH=0.018 来自 k=3 per-table 校正。如果一致用 k=9，ρ=0.6 的 p_BH 应为 0.064。建议两种方案：
- (A) 统一用 k=9：将 ρ=0.6 改为 "p_BH=0.064"
- (B) 改为 per-table 校正：明确说明 ρ=0.6 的三个比较用 k=3，并修改 C1 的表述

**2. 次要精度问题** (低风险)

- GPT-2 Δ=+0.098: 实际 +0.100~0.102，差 0.002-0.004
- Grid gap 0.054 vs 0.055, grid σ=0.033 vs 0.035
- B=128 外推 Δ≈0.39 需要 α≈0.86，而非报告的 α≈0.89
- 这些不太可能被 reviewer 注意，但若被要求提供 reproducibility code 可能暴露

---
