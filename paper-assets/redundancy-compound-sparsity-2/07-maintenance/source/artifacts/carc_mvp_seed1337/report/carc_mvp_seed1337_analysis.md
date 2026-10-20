# CARC MVP seed1337 实验分析

## 实验配置

| 参数 | 值 |
|------|-----|
| Model | DeepSeek-R1-Distill-Qwen-14B |
| Dataset | MATH (precalculus + mixed) |
| Samples | 30 chains |
| Seed | 1337 |
| max_new_tokens | 2048 |
| tau (redundancy threshold) | 0.7 |
| Layers evaluated | 48 (per-head, 8 KV heads) |
| Sparsity levels | 40% (uniform), 55% (two-tier) |

## 全局关键指标

| 指标 | 值 | 阈值 | 通过? |
|------|-----|------|-------|
| **Pearson r(EMA, perturbation)** | -0.1130 | \|r\| ≥ 0.4 | **NO** |
| **Perturbation diff (redundant vs novel @55%)** | 5.26% | ≥ 10% | **NO** |
| Spearman r(EMA, perturbation) | -0.1008 | — | — |
| Pearson r(EMA, -surprisal) | +0.1255 | — | — |
| Position-residualized r(EMA, perturbation) | -0.1110 | — | — |
| Position-residualized r(EMA, -surprisal) | +0.1413 | — | — |
| Chain-level r(EMA, perturbation) | +0.0162 | — | — |
| Chain-level r(EMA, -surprisal) | +0.0535 | — | — |
| PPL two-tier (55%/40%) | 1.38 | — | — |
| PPL uniform 40% | 1.38 | — | — |
| Delta PPL | -0.00 | — | — |
| Mean perturbation redundant @55% | 0.5143 | — | — |
| Mean perturbation novel @55% | 0.5669 | — | — |
| Redundant near-zero frac | 0.5234 | — | — |
| Novel near-zero frac | 0.4522 | — | — |
| Near-zero ratio (redundant/novel) | 1.16x | — | — |
| Median lag-1 autocorr (EMA) | 0.3394 | — | — |
| Median lag-1 autocorr (surprisal) | 0.3899 | — | — |
| n_redundant / n_novel | 17,852 / 2,085,844 | — | — |

## 2×2 MVP 判定矩阵

|  | perturbation diff ≥ 10% | perturbation diff < 10% |
|--|--|--|
| **\|r\| ≥ 0.4** | PASS | DISCORDANT-B |
| **\|r\| < 0.4** | DISCORDANT-A | **→ FAIL ←** |

### **判定结果：FAIL**
- |r| = 0.113 < 0.4 ✗
- diff = 5.26% < 10% ✗

## Per-Layer 分析

### 全部 48 层指标

| Layer | Pearson r | Perturbation Diff | n_redundant | Per-layer 判定 |
|-------|-----------|-------------------|-------------|---------------|
| 0 | +0.3319 | -0.1463 (负向) | 267 | DISCORDANT |
| 1 | -0.0564 | +0.0029 (0.3%) | 277 | FAIL |
| 2 | -0.0032 | -0.0505 (负向) | 202 | FAIL |
| 3 | -0.2272 | +0.1566 (15.7%) | 47 | DISCORDANT-A |
| 4 | -0.0870 | +0.7719 (77.2%) | 30 | DISCORDANT-A* |
| 5 | -0.0221 | +0.1389 (13.9%) | 273 | DISCORDANT-A |
| 6 | -0.0408 | +0.0549 (5.5%) | 348 | FAIL |
| 7 | +0.0162 | +0.0634 (6.3%) | 360 | FAIL |
| 8 | -0.1147 | +0.0269 (2.7%) | 397 | FAIL |
| 9 | -0.0316 | +0.0310 (3.1%) | 219 | FAIL |
| 10 | +0.1279 | +0.0238 (2.4%) | — | FAIL |
| 11 | +0.0435 | +0.0788 (7.9%) | — | FAIL |
| 12 | +0.1182 | +0.0288 (2.9%) | — | FAIL |
| 13 | +0.0105 | +0.1080 (10.8%) | — | DISCORDANT-A |
| 14 | -0.0518 | +0.1580 (15.8%) | — | DISCORDANT-A |
| 15 | -0.0808 | +0.1229 (12.3%) | — | DISCORDANT-A |
| 16 | -0.1239 | +0.0715 (7.2%) | — | FAIL |
| 17 | -0.1273 | +0.1206 (12.1%) | — | DISCORDANT-A |
| 18 | -0.0880 | +0.0537 (5.4%) | — | FAIL |
| 19 | -0.0792 | +0.0685 (6.9%) | — | FAIL |
| 20 | -0.1766 | +0.0775 (7.8%) | — | FAIL |
| 21 | -0.1735 | +0.1559 (15.6%) | — | DISCORDANT-A |
| 22 | -0.1208 | +0.1086 (10.9%) | — | DISCORDANT-A |
| 23 | -0.0866 | +0.1550 (15.5%) | — | DISCORDANT-A |
| 24 | -0.1988 | +0.0278 (2.8%) | — | FAIL |
| 25 | -0.1974 | +0.1007 (10.1%) | — | DISCORDANT-A |
| 26 | -0.2860 | +0.0831 (8.3%) | — | FAIL |
| 27 | -0.2906 | +0.0367 (3.7%) | — | FAIL |
| 28 | -0.3230 | +0.1322 (13.2%) | — | DISCORDANT-A |
| 29 | -0.3326 | +0.0950 (9.5%) | — | FAIL |
| 30 | **-0.4202** | +0.0674 (6.7%) | — | **DISCORDANT-B** |
| 31 | **-0.4020** | +0.0586 (5.9%) | — | **DISCORDANT-B** |
| 32 | -0.2387 | +0.0457 (4.6%) | — | FAIL |
| 33 | **-0.4005** | +0.0555 (5.6%) | — | **DISCORDANT-B** |
| 34 | -0.3131 | +0.0254 (2.5%) | 432 | FAIL |
| 35 | -0.3358 | +0.0154 (1.5%) | 541 | FAIL |
| 36 | -0.3245 | +0.0786 (7.9%) | 152 | FAIL |
| 37 | -0.2343 | +0.0486 (4.9%) | 224 | FAIL |
| 38 | -0.2899 | +0.0301 (3.0%) | 467 | FAIL |
| 39 | -0.3705 | +0.0492 (4.9%) | 507 | FAIL |
| 40 | -0.2535 | +0.0978 (9.8%) | 208 | FAIL |
| 41 | -0.2510 | +0.1744 (17.4%) | 118 | DISCORDANT-A |
| 42 | -0.2798 | +0.1175 (11.8%) | 197 | DISCORDANT-A |
| 43 | -0.3194 | +0.1101 (11.0%) | 193 | DISCORDANT-A |
| 44 | -0.3089 | +0.2115 (21.1%) | 143 | DISCORDANT-A |
| 45 | -0.2144 | +0.1754 (17.5%) | 179 | DISCORDANT-A |
| 46 | -0.2965 | +0.0452 (4.5%) | 369 | FAIL |
| 47 | +0.0701 | +0.0072 (0.7%) | 77 | FAIL |

*L4: 77% diff 但 n_redundant=30，样本量过小不可靠

### Per-Layer 关键发现

1. **没有任何单层同时满足两个条件**（|r|≥0.4 且 diff≥10%）
2. **空间解耦**：相关性和扰动差异在层间呈反向分布
   - 高相关层 (L30-33, |r|~0.40): diff 仅 2.5%-6.7%
   - 高扰动差异层 (L41-45, diff 11%-21%): |r| 仅 0.21-0.32
3. **相关方向一致**：深层（L26+）r 值一致为负，表明 EMA score 越高（越 redundant），perturbation 越小——方向符合假设
4. **浅层异常**：L0 的 r=+0.33 为正，且 diff 为负向（redundant 的扰动反而更大）

## 对比分析

- **seed42 结果**：不存在（/root/carc/results_seed42.json 未找到）
- **W&B run ID**：日志中未发现 wandb 相关记录

## 原始日志关键段落

```
==============================================================
CARC MVP Results -- 5 Measurements
==============================================================

(a) MLP Activation Magnitudes (near-zero fraction)
    Redundant near-zero: 0.5234
    Novel near-zero:     0.4522
    Ratio (redundant/novel): 1.16x

(b) Perturbation@55% (redundant vs novel)
    Pearson  r(EMA, perturbation) = -0.1130  (p=0.00e+00)
    Spearman r(EMA, perturbation) = -0.1008  (p=0.00e+00)
    Mean perturbation: redundant@55% = 0.514267
                       novel@55%     = 0.566895
    Perturbation diff = 0.0526 (5.3%)
    Tokens: 17852 redundant, 2085844 novel  (tau=0.7)

(c) EMA <-> Surprisal Correlation
    Pearson r(EMA, -surprisal) = +0.1255  (p=3.10e-153)

(d) Perplexity: Two-tier vs Uniform
    PPL two-tier (55%/40%): 1.38
    PPL uniform 40%:        1.38
    Delta PPL: -0.00 (two-tier better)

(e) Position-residualized Correlations
    Partial r(EMA, perturbation | pos) = -0.1110
    Partial r(EMA, -surprisal | pos)   = +0.1413

==============================================================
Verdict: FAIL
  |r| >= 0.4 ? NO (0.1130)
  diff >= 10%? NO (5.3%)
==============================================================
```

## 总结

CARC MVP seed1337 **FAIL**。EMA centroid 作为统一冗余信号的假设未获验证：
- 全局相关性过弱（|r|=0.11，远低于 0.4 阈值）
- 扰动差异不足（5.3%，低于 10% 阈值）
- 即使 per-layer 分析，也没有任何层同时满足两个条件
- 两个信号在层间空间解耦是核心失败原因
