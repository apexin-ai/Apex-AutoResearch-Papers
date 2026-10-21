# ops exp014 fixed rerun

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp014_fixed_rerun_20260521T000513_result.json`
- **Structured JSON:** [`d505d7476e629df08ff9.json`](../../sessions/d5/d505d7476e629df08ff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-014 全部完成。以下是完整结果汇总：

---

## exp-014 完整输出

### 1. Direction-Asymmetry Analysis (formality)

Consistent pairs: 55

| Direction | n | formal wins | win rate | 95% CI (Wilson) | Sign test p | Sig |
|-----------|---|-------------|----------|-----------------|-------------|-----|
| formal→casual | 33 | 26/33 | 78.8% | [0.6225, 0.8932] | 0.001319 | **YES** |
| casual→formal | 22 | 12/22 | 54.5% | [0.3466, 0.7308] | 0.831812 | NO |

- `formal→casual`: formality effect 与 original preference **同向混淆**
- `casual→formal`: **cleanly isolates formality effect** — formal 仅赢 54.5%，不显著

### 2. Pair-Level Bootstrap Logistic Regression

196 observations (2 trials × 98 pairs), bootstrap unit = pair

| Effect | Coef | SE | OR | OR 95% CI | z | p | Sig |
|--------|------|----|----|-----------|---|---|-----|
| **formal_effect** | 0.7928 | 0.3161 | **2.2095** | [1.2280, 4.3053] | 2.508 | **0.0121** | **YES** |
| original_effect | 0.5958 | 0.3220 | 1.8145 | [0.9757, 3.3693] | 1.850 | 0.0643 | NO |

Intercept (position A bias): -0.5851

### 3. GEE Decomposition (Exchangeable Correlation)

| Effect | Coef | SE | OR | OR 95% CI | p | Sig |
|--------|------|----|----|-----------|---|-----|
| **formal_effect** | 0.7931 | 0.3074 | **2.2103** | [1.2100, 4.0377] | **0.0099** | **YES** |
| original_effect | 0.5973 | 0.3074 | 1.8172 | [0.9948, 3.3194] | 0.0520 | NO |

### 4. Method Comparison

| Effect | Method | OR | OR 95% CI | p |
|--------|--------|----|-----------|---|
| formal_effect | Pair-bootstrap | 2.2095 | [1.228, 4.305] | 0.0121 |
| formal_effect | GEE | 2.2103 | [1.210, 4.038] | 0.0099 |
| original_effect | Pair-bootstrap | 1.8145 | [0.976, 3.369] | 0.0643 |
| original_effect | GEE | 1.8172 | [0.995, 3.319] | 0.0520 |

### 5. 关键对比与解读

**Formality effect 在 pair-clustered 后仍然显著：**
- Pair-bootstrap: p=0.012, GEE: p=0.010
- OR ≈ 2.21，judges 偏好 formal 版本的概率是 casual 的 2.2 倍
- 两种方法高度一致，结论稳健

**Original effect 在 pair-clustered 后降为 marginally significant：**
- Pair-bootstrap: p=0.064, GEE: p=0.052
- OR CI 下界分别为 0.976 和 0.995，刚好跨过 1.0
- 这意味着原始 observation-level bootstrap 可能高估了 original effect 的显著性（因为忽略了 pair 内依赖）

**核心发现：** 修正 independence violation 后，formality bias 仍然是 robust effect (p<0.05)，但 original preference 效应变为 borderline (p≈0.05-0.06)。这强化了论文的核心 claim——formality 是独立于 original preference 的显著偏差因素。

### 6. 其他已有输出

**exp-011 NLI sensitivity** (`exp011_nli_sensitivity.csv`): NLI threshold 从 0.7 到 0.95，pairwise win rate 稳定在 72-74%，p 值均 <0.003。说明 formality effect 对 NLI 过滤阈值不敏感。

**exp-012 CSV 尚未生成**（目录中无 exp-012 文件）。

---
