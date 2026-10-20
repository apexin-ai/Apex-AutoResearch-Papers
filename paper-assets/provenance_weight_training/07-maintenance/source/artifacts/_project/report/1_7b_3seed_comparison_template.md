# 1.7B 3-Seed Comparison Template

> Status: 2-seed data filled, seed456 pending (adaptive RUNNING, uniform ANALYZING)
> Config: Qwen3-1.7B, ρ=0.4, τ=0.8, 200M tokens, from-scratch v5
> Generated: 2026-05-20

---

## 1. Main Results: PPL + Downstream

### 2-Seed Summary (filled)

| Metric | Uniform s42 | Uniform s123 | Uniform Mean±Std | Adaptive s42 | Adaptive s123 | Adaptive Mean±Std | Δ(A−U) Mean±Std |
|--------|-------------|-------------|------------------|-------------|-------------|-------------------|----------------|
| Holdout PPL | 13.280 | 13.265 | 13.272±0.011 | 13.270 | 13.250 | 13.260±0.014 | −0.012±0.003 |
| OWT PPL | 13.291 | 13.292 | 13.291±0.001 | 13.282 | 13.291 | 13.287±0.006 | −0.005±0.006 |
| Wiki PPL | 10.919 | 10.942 | 10.931±0.016 | 10.955 | 10.952 | 10.954±0.002 | **+0.023±0.018** |
| DS Mean | 0.6256 | 0.6256 | 0.6256±0.000 | 0.6251 | 0.6286 | 0.6269±0.002 | +0.001±0.002 |

### 3-Seed Table (seed456 TBD)

| Metric | Uniform s42 | Uniform s123 | Uniform s456 | U Mean±Std | Adaptive s42 | Adaptive s123 | Adaptive s456 | A Mean±Std | Δ(A−U) |
|--------|-------------|-------------|-------------|------------|-------------|-------------|--------------|------------|--------|
| Holdout PPL | 13.280 | 13.265 | **?** | ? | 13.270 | 13.250 | **?** | ? | ? |
| OWT PPL | 13.291 | 13.292 | **?** | ? | 13.282 | 13.291 | **?** | ? | ? |
| Wiki PPL | 10.919 | 10.942 | **?** | ? | 10.955 | 10.952 | **?** | ? | ? |
| DS Mean | 0.6256 | 0.6256 | **?** | ? | 0.6251 | 0.6286 | **?** | ? | ? |

---

## 2. Downstream Breakdown (per benchmark)

| Benchmark | U s42 | U s123 | U s456 | U Mean | A s42 | A s123 | A s456 | A Mean | Δ(A−U) |
|-----------|-------|--------|--------|--------|-------|--------|--------|--------|--------|
| ARC-Easy (norm) | 0.7235 | 0.7260 | ? | — | 0.7176 | 0.7138 | ? | — | — |
| ARC-Challenge (norm) | 0.4334 | 0.4317 | ? | — | 0.4403 | 0.4386 | ? | — | — |
| HellaSwag (norm) | 0.6107 | 0.6118 | ? | — | 0.6164 | 0.6147 | ? | — | — |
| PIQA (norm) | 0.7432 | 0.7454 | ? | — | 0.7443 | 0.7459 | ? | — | — |
| WinoGrande | 0.6172 | 0.6133 | ? | — | 0.6069 | 0.6298 | ? | — | — |

---

## 3. Key Comparison Dimensions

### 3a. Holdout Δ(adaptive−uniform)

| Seed | Adaptive | Uniform | Δ |
|------|----------|---------|---|
| 42 | 13.270 | 13.280 | −0.010 |
| 123 | 13.250 | 13.265 | −0.015 |
| 456 | ? | ? | ? |
| **Mean** | **13.260** | **13.272** | **−0.012** |

2-seed: 方向一致（两个 seed 均 adaptive < uniform），幅度 0.010–0.015。
3-seed 关注: seed456 是否维持 negative Δ？

### 3b. OOD Δ(adaptive−uniform)

| Seed | OWT Δ | Wiki Δ |
|------|-------|--------|
| 42 | −0.009 | **+0.036** |
| 123 | −0.001 | +0.010 |
| 456 | ? | ? |
| **Mean** | **−0.005** | **+0.023** |

### 3c. Downstream Δ(adaptive−uniform)

| Seed | DS Mean Δ |
|------|-----------|
| 42 | −0.0005 |
| 123 | +0.0030 |
| 456 | ? |
| **Mean** | **+0.0012** |

预期：保持 ≈0（0.6B 三 seed 结论：downstream 不受 weighting 影响）

---

## 4. Wiki OOD Seed-Level Variance — 重点关注

**问题**：Wiki PPL Δ(A−U) 在 seed42 为 +0.036 vs seed123 仅 +0.010，差异 3.6×。

| | Wiki PPL | Adaptive | Uniform | Δ(A−U) |
|---|---------|----------|---------|--------|
| seed42 | | 10.955 | 10.919 | +0.036 |
| seed123 | | 10.952 | 10.942 | +0.010 |
| 2-seed mean | | 10.954 | 10.931 | +0.023 |
| 2-seed std(Δ) | | — | — | ±0.018 |

**分析**：
- Adaptive Wiki PPL 跨 seed 极稳定（10.955 vs 10.952, std=0.002）
- Uniform Wiki PPL 跨 seed 波动更大（10.919 vs 10.942, std=0.016）
- Δ 的 variance 主要来自 **uniform 侧**，不是 adaptive 侧
- seed42 的 uniform Wiki 偏低（10.919）是 Δ 偏大的原因

**seed456 将决定**：
1. Wiki Δ 的 3-seed 均值和方差 → 判断 +0.036 是否为 outlier
2. 若 seed456 Wiki Δ ≈ +0.010，则 3-seed mean Δ ≈ +0.019 (较温和)
3. 若 seed456 Wiki Δ ≈ +0.036，则 3-seed mean Δ ≈ +0.027 (需在论文 acknowledge)

**论文影响**：
- 若 3-seed Wiki Δ > +0.02 → 必须在 Results/Discussion 提及 "adaptive 的 holdout 优势不迁移至 Wiki OOD"
- 与 0.6B distribution matching finding 一致：adaptive 优势限于 in-dist

---

## 5. 与 0.6B 三 Seed 数据的 Scaling 对比

| Scale | Holdout Δ | OWT Δ | Wiki Δ | DS Δ | Data source |
|-------|-----------|-------|--------|------|-------------|
| **0.6B ρ=0.4 τ=0.8** | −0.043±0.007 | ~−0.05 | ~−0.05 | ≈0 | 3-seed ✅ |
| **0.6B ρ=0.6 τ=0.7** | −0.032±0.006 | ~−0.02 | ~−0.03 | ≈0 | 3-seed ✅ |
| **1.7B ρ=0.4 τ=0.8** | −0.012±0.003 | −0.005±0.006 | +0.023±0.018 | ≈0 | 2-seed, s456 TBD |

**观察**：
- Holdout Δ 从 0.6B→1.7B 缩小约 70%（−0.043 → −0.012）
- OOD: 0.6B 下 adaptive OOD 也优于 uniform；1.7B 下 Wiki 反转为 positive（uniform 更好）
- DS: 两个 scale 均 ≈0

---

## 6. 论文 Claim 对照：3-seed 数据影响评估

| Paper Claim | 2-seed 状态 | seed456 影响 | 风险等级 |
|-------------|------------|-------------|---------|
| **"method scales without degradation"** | ✅ holdout Δ=−0.012 (方向正确) | 若 s456 holdout Δ 仍 negative → claim 成立; 若 positive → 需修改措辞 | 低 |
| **"benefit diminishes at larger scale"** | ✅ 0.6B Δ=−0.043 → 1.7B Δ=−0.012 | 不太敏感，趋势已清晰 | 极低 |
| **禁止 claim "advantage persists at larger scale"** | ✅ 正确不 claim | 3-seed 统计可能让 Δ 不显著 → 更加确认不应 claim | N/A |
| **Wiki OOD 不利信号** | ⚠️ +0.036 (s42) vs +0.010 (s123) | 3-seed mean 和 p-value 将定论 | **中** |
| **Downstream neutral** | ✅ DS Δ ≈ 0 | 预期维持 | 极低 |
| **"no harm at scale" framing** | ✅ 但 Wiki Δ>0 是 nuance | 若 3-seed Wiki Δ 显著 positive → 需加 qualifier | **中** |

---

## 7. 填表指南（seed456 eval 完成后）

1. 从 eval 结果提取: `eval_ppl_holdout`, `eval_ppl_openwebtext`, `eval_ppl_wikipedia`, 5 个 downstream metrics
2. 填入 Section 1–3 的 "?" 列
3. 重算 3-seed mean/std 和 paired t-test (holdout, OWT, Wiki)
4. 更新 Section 4 Wiki variance 分析
5. 更新 Section 5 scaling 表
6. 根据 Section 6 风险评估更新 paper_framing.md 的 1.7B 叙事

**统计检验**（3-seed paired t-test 模板）：
```python
from scipy import stats
# paired t-test: adaptive vs uniform, 3 seeds
adaptive = [13.270, 13.250, ?]  # holdout PPL
uniform  = [13.280, 13.265, ?]
t, p = stats.ttest_rel(adaptive, uniform)
# p < 0.05 → statistically significant
```
