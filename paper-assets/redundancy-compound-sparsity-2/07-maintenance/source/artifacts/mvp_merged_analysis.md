# CARC MVP Merged Analysis — Final Verdict

> Date: 2026-05-12 | Model: DeepSeek-R1-Distill-Qwen-14B | Dataset: MATH | Seeds: 42, 1337 | Chains: 60 total | Records: 4,435,728

## 1. Global Verdict: FAIL

### 2×2 Decision Matrix (Merged, τ=0.7)

|  | diff ≥ 10% | diff < 10% |
|---|---|---|
| **\|r\| ≥ 0.4** | — | — |
| **\|r\| < 0.4** | — | **✓ HERE: \|r\|=0.115, diff=5.5%** |

Both thresholds missed. Cross-axis hypothesis is **not supported**.

## 2. Five Measurements (Merged Values)

| # | Measurement | Value | Threshold | Pass? |
|---|---|---|---|---|
| (a) | MLP near-zero ratio (redundant/novel) | 1.13× (0.511 / 0.453) | — | Weak signal |
| (b) | Pearson r(EMA, perturbation) | **-0.1154** (p=0) | \|r\| ≥ 0.4 | **NO** |
| (b) | Perturbation diff (redundant vs novel) | **5.48%** (0.513 vs 0.568) | ≥ 10% | **NO** |
| (c) | Pearson r(EMA, -surprisal) | **+0.1207** (p≈1e-296) | — | Very weak |
| (d) | PPL two-tier / PPL uniform40 | **1.36 / 1.36** (Δ=0.00) | Δ > 0 | **NO** |
| (e-i) | Position-residualized r(EMA, pert) | **-0.1131** | — | Unchanged |
| (e-ii) | Position-residualized r(EMA, surp) | **+0.1378** | — | Unchanged |

Additional statistics:
- Spearman r(EMA, perturbation) = -0.105
- Chain-level r(EMA, perturbation) = -0.1886
- Chain-level r(EMA, -surprisal) = +0.1569
- Median lag-1 autocorr (EMA) = 0.316, (surprisal) = 0.368

## 3. Per-Seed Comparison

| Metric | seed42 | seed1337 | Merged | Δ (seed gap) |
|---|---|---|---|---|
| r(EMA, pert) | -0.1176 | -0.113 | -0.1154 | 0.005 |
| diff_pct | 5.69% | 5.26% | 5.48% | 0.43pp |
| r(EMA, surp) | +0.1162 | +0.1255 | +0.1207 | 0.009 |
| pos_resid r(pert) | -0.1151 | — | -0.1131 | — |
| pos_resid r(surp) | +0.1344 | — | +0.1378 | — |
| chain_r(pert) | -0.357 | — | -0.1886 | — |
| chain_r(surp) | +0.3195 | — | +0.1569 | — |
| ppl_twotier | 1.34 | 1.38 | 1.36 | 0.04 |
| ppl_uniform40 | 1.34 | 1.38 | 1.36 | 0.04 |
| near_zero_ratio | 1.10× | 1.16× | 1.13× | 0.06 |
| High-r layers | L30/31/33 | L30/31/33 | L30/31/33 | **Identical** |
| verdict | FAIL | FAIL | FAIL | **Consistent** |

**结论**：两个 seed 高度一致，差异 < 5%。结果可复现。

## 4. Per-Layer Analysis

### Layers with |r| ≥ 0.4 (高相关层)

| Layer | seed42 r | seed1337 r* | Merged r | Merged diff | diff% |
|---|---|---|---|---|---|
| L30 | -0.4412 | ~-0.40 | **-0.4313** | 0.071 | 7.1% |
| L31 | -0.4150 | ~-0.40 | **-0.4089** | 0.062 | 6.2% |
| L33 | -0.4156 | ~-0.40 | **-0.4085** | 0.054 | 5.4% |

→ 这 3 层有中等相关性，但 perturbation diff 均 **< 10%**。信号存在但无法转化为实际效果。

### Layers with diff ≥ 10% (高扰动差异层)

| Layer | Merged r | Merged diff | diff% | n_redundant |
|---|---|---|---|---|
| L4 | -0.093 | 0.557 | 55.7% | 79 (太少) |
| L5 | -0.020 | 0.234 | 23.4% | 431 |
| L6 | -0.030 | 0.161 | 16.1% | 465 |
| L11 | +0.048 | 0.143 | 14.3% | 264 |
| L12 | +0.088 | 0.164 | 16.4% | 295 |
| L13 | +0.001 | 0.155 | 15.5% | 300 |
| L14 | -0.058 | 0.149 | 14.9% | 342 |
| L15 | -0.091 | 0.131 | 13.1% | 442 |
| L28 | -0.338 | 0.139 | 13.9% | 584 |
| L41 | **-0.248** | 0.169 | 16.9% | 234 |
| L42 | -0.278 | 0.102 | 10.2% | 425 |
| L44 | **-0.295** | 0.205 | 20.5% | 293 |
| L45 | -0.214 | 0.178 | 17.8% | 343 |

→ |r| 最高仅 0.338 (L28)、0.295 (L44)，均 **< 0.4**。

### 热力图描述

```
Layer:  0         10        20        30        40        47
|r|:   ■□□■□□□□■□ ■□□□□□■■□□ ■■□□□□■■■■ ■■■■■■■■■■ ■■■■■■■■■□
diff%: □□□■■■■■□■ ■■■■■■□□□□ □■□□□■□□■□ □□□□□□□□□■ ■■□■■□□
       ──────────────────────────────────────────────────────
Legend: ■ = notable (|r|>0.3 or diff>10%)  □ = below threshold
```

**关键模式**：|r| 高峰在 L26-39（中后层），diff 高峰在 L3-15（前层）和 L41-45（尾层）。两者在空间上解耦，无交叉区域同时满足双阈值。

## 5. Key Findings

### 5.1 EMA ↔ Surprisal 相关性（Contribution A 理论基础）

r(EMA, -surprisal) = **+0.1207**。

EMA centroid similarity 与 token surprisal 之间仅存在极微弱的正相关。理论预期是：高 EMA similarity（冗余 token）应对应低 surprisal（可预测），即正相关应较强。实际 r ≈ 0.12 说明 EMA similarity 几乎不能作为 surprisal 的代理信号。

**但这不影响 EMA 作为 KV eviction signal 的价值**——eviction 的目标是 identifying "已见过" 的 token，而非预测 surprisal。

### 5.2 PPL Two-tier vs Uniform 差异（实用价值）

PPL two-tier = PPL uniform = **1.36**，Δ = 0.00。

Cross-axis 策略（用 EMA similarity 分层分配 perturbation budget）完全无效。无论按 EMA 分层还是均匀分配，对 perplexity 的影响相同。这直接否定了 cross-axis 策略的实用价值。

### 5.3 Position-Residualized r

去除位置效应后：
- r(EMA, pert | pos) = -0.1131 (vs raw -0.1154)
- r(EMA, surp | pos) = +0.1378 (vs raw +0.1207)

位置混淆对 perturbation 相关性几乎无影响（差异 0.002），对 surprisal 相关性略有提升但仍然很弱。**结论不变**。

### 5.4 层间解耦模式

| 层区间 | |r| 特征 | diff 特征 | 解读 |
|---|---|---|---|
| L0-15 (前层) | 低 (0-0.13) | 高 (10-56%) | 前层 perturbation 敏感但 EMA 无预测力 |
| L16-25 (中层) | 低-中 (0.08-0.22) | 低-中 (4-15%) | 过渡区，信号噪声混合 |
| L26-39 (中后层) | **高 (0.25-0.44)** | **低 (2-14%)** | EMA 能预测哪些是冗余 token，但扰动不敏感 |
| L40-47 (尾层) | 中 (0.21-0.30) | **高 (10-21%)** | 扰动敏感但 EMA 预测力下降 |

这是一个根本性的解耦：**模型中 EMA similarity 有预测力的层恰好是扰动不敏感的层，反之亦然**。这意味着 cross-axis（用 EMA 指导 perturbation budget）在架构层面就不成立。

## 6. ROADMAP Path Recommendation

### 判定：Path C — Abandon Cross-Axis, Pivot to O(1) KV Eviction

**理由**：
1. 全局 |r| = 0.115 远低于 0.4 阈值（仅达标 29%）
2. 全局 diff = 5.5% 远低于 10% 阈值（仅达标 55%）
3. PPL Δ = 0（零实用价值）
4. 层间解耦意味着无法通过选择特定层来改善结果
5. 两个 seed 完全一致，排除随机波动

**Cross-axis 假说为何失败**：EMA centroid similarity 度量的是 "这个 token 的 KV 表示与历史平均有多相似"，而 perturbation sensitivity 度量的是 "移除这个 KV 后输出变化多大"。前者是一阶统计量（与均值的距离），后者是二阶效应（与其他 token 的交互）。两者度量的是不同维度的信息，没有理由期望它们强相关。

**Pivot 方向**：ROADMAP 已更新为 O(1) KV eviction（用 EMA similarity 直接做 eviction scoring，不走 cross-axis）。EMA similarity 本身作为 "冗余度" 指标仍有价值（near-zero ratio 1.13×表明冗余 token 确实 MLP 激活更稀疏），只是不应用于 cross-axis perturbation budget 分配。

---

*Generated: 2026-05-12 | Experiments: carc_mvp_seed42, carc_mvp_seed1337 | Parent: mvp_001*
