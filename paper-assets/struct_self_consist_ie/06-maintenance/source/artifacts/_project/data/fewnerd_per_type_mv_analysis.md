## Per-Type MV Analysis Data — FewNERD

### 数据来源
- 数据集: FewNERD (8 coarse entity types)
- 分析范围: seed=42, 123, 456 (3-seed average)
- 分析对象: finetuned 3-epoch (fewnerd_mf4v2) + finetuned 3-epoch (exp_021)
- N=8 samples, entity-level majority vote (span-based strict match)
- 服务器输出: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_per_type_mv_analysis.json`

---

### 1. Finetuned 3-epoch (fewnerd_mf4v2), θ=0.25 (2/N), 3-seed avg

| Entity Type | n_inst | greedy_f1 | MV F1 | MV Δ (pp) |
|-------------|--------|-----------|-------|-----------|
| other | 3433 | 0.6385 | 0.6920 | +5.36±2.50 |
| product | 2276 | 0.6591 | 0.6782 | +1.90±2.27 |
| person | 8016 | 0.8219 | 0.8252 | +0.33±0.69 |
| organization | 6647 | 0.7209 | 0.7234 | +0.26±0.77 |
| event | 1306 | 0.6538 | 0.6559 | +0.20±0.59 |
| location | 8023 | 0.7927 | 0.7878 | -0.48±0.47 |
| art | 1277 | 0.7557 | 0.7430 | -1.27±0.79 |
| building | 1587 | 0.7012 | 0.6792 | -2.20±2.03 |

Correlation (3-seed avg): Pearson r=-0.52 (p=0.19), Spearman ρ=-0.36 (p=0.39) — NOT significant.

---

### 2. Finetuned model (exp_021, 3-epoch), θ=0.25, seed=42

| Entity Type | n_inst | greedy_f1 | MV F1 | MV Δ (pp) |
|-------------|--------|-----------|-------|-----------|
| other | 3433 | 0.6374 | 0.6825 | +4.51 |
| product | 2276 | 0.6564 | 0.6695 | +1.31 |
| person | 8016 | 0.8220 | 0.8252 | +0.31 |
| organization | 6647 | 0.7203 | 0.7186 | -0.18 |
| event | 1306 | 0.6551 | 0.6505 | -0.46 |
| location | 8023 | 0.7926 | 0.7872 | -0.54 |
| art | 1277 | 0.7557 | 0.7426 | -1.31 |
| building | 1587 | 0.7024 | 0.6858 | -1.66 |

Correlation: Pearson r=-0.48 (p=0.23), Spearman ρ=-0.36 (p=0.39)

---

### 3. Strict MV (θ=0.5) — where strong correlation emerges

#### exp_021 (finetuned 3-epoch), θ=0.5, seed=42

| Entity Type | n_inst | greedy_f1 | MV F1 | MV Δ (pp) |
|-------------|--------|-----------|-------|-----------|
| person | 8016 | 0.8220 | 0.8153 | -0.67 |
| art | 1277 | 0.7557 | 0.7405 | -1.51 |
| location | 8023 | 0.7926 | 0.7774 | -1.52 |
| organization | 6647 | 0.7203 | 0.6939 | -2.65 |
| other | 3433 | 0.6374 | 0.6072 | -3.02 |
| event | 1306 | 0.6551 | 0.6234 | -3.17 |
| product | 2276 | 0.6564 | 0.6226 | -3.38 |
| building | 1587 | 0.7024 | 0.6634 | -3.90 |

**Pearson r=0.8665 (p=0.005), Spearman ρ=0.7381 (p=0.037)**

#### fewnerd_mf4v2 (finetuned 3-epoch), θ=0.5, seed=42

| Entity Type | n_inst | greedy_f1 | MV F1 | MV Δ (pp) |
|-------------|--------|-----------|-------|-----------|
| location | 8023 | 0.7928 | 0.7621 | -3.07 |
| person | 8016 | 0.8216 | 0.7873 | -3.43 |
| art | 1277 | 0.7559 | 0.7207 | -3.53 |
| event | 1306 | 0.6542 | 0.6048 | -4.93 |
| organization | 6647 | 0.7202 | 0.6668 | -5.34 |
| product | 2276 | 0.6576 | 0.5904 | -6.72 |
| building | 1587 | 0.7023 | 0.6213 | -8.09 |
| other | 3433 | 0.6377 | 0.5360 | -10.17 |

**Pearson r=0.7746 (p=0.024), Spearman ρ=0.8095 (p=0.015)**

---

### Correlation Summary (greedy_f1 vs MV_delta)

| Dataset | θ | Pearson r | p-value | Spearman ρ | p-value |
|---------|------|-----------|---------|------------|---------|
| exp_021 | 0.25 | -0.48 | 0.228 | -0.36 | 0.385 |
| exp_021 | 0.375 | -0.11 | 0.797 | +0.02 | 0.955 |
| **exp_021** | **0.5** | **+0.87** | **0.005** | **+0.74** | **0.037** |
| mf4v2 (3-seed) | 0.25 | -0.52 | 0.190 | -0.36 | 0.385 |
| mf4v2 | 0.375 | +0.55 | 0.154 | +0.48 | 0.233 |
| **mf4v2** | **0.5** | **+0.77** | **0.024** | **+0.81** | **0.015** |

---

### Interpretation

1. **θ=0.5 (strict MV) shows strong positive correlation**: types with higher greedy_f1 suffer less MV degradation. Easy types (person, location) have more sample agreement → strict MV preserves most entities. Hard types (other, building) have diverse outputs → strict MV drops too many entities → large F1 loss.

2. **θ=0.25 (liberal MV) reverses the sign**: with a low threshold, hard types with rich diversity actually benefit from MV (aggregating diverse correct entities), while easy types see little change. The correlation flips to negative but is not significant.

3. **Previously reported "Corr ≈ +0.90 (p=0.002)"** most likely corresponds to exp_021 θ=0.5 (Pearson r=0.87, p=0.005). The slight discrepancy may come from a different random seed or filtering criterion.

4. **Practical implication**: Construction threshold θ critically determines whether MV helps or hurts per entity type. The optimal θ=0.25 (2/N) used in our paper avoids the strong type-dependent bias of θ=0.5.

---

### Raw Data Files
- Server JSON: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_per_type_mv_analysis.json` (θ=0.25, 3-seed, finetuned)
- Analysis scripts: `code/analyze_per_type_mv_fewnerd.py`, `code/analyze_per_type_mv_v2.py`
