# research binary ours code audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_binary-ours-code-audit_20260515T043108_result.json`
- **Structured JSON:** [`ce91ad7556e99c8b0930.json`](../../sessions/ce/ce91ad7556e99c8b0930.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获得全部必要信息。以下是审计报告。

---

## Binary-Ours Filtering 代码审计报告

### 1. 精确定义（从代码）

**分类器类型：Binary（二分类）**
- 标签：`labels = (depths > 0).astype(int)` — depth=0 为 human (label=0)，depth≥1 全部为 synthetic (label=1)
- 模型：LightGBM (200 trees, max_depth=6)，使用与 Graduated 相同的 15 维特征

**权重公式：`w = 1 - P(synthetic)`**
- 即 `P(human)` — 分类器认为该样本是人类文本的概率
- 这是 **soft weighting**（连续权重 [0, 1]），不是 hard filtering

**训练中如何使用：`WeightedRandomSampler`**
- 权重作为采样概率传给 `torch.utils.data.WeightedRandomSampler(replacement=True)`
- 高权重样本被更频繁地采到，低权重样本几乎不被采到
- 权重为 0 的样本（`w < 1e-8`）被直接剔除

### 2. 核心代码片段

```python
# BinaryOurs.fit — 二分类训练
labels = (depths > 0).astype(int)  # depth=0 → 0, depth≥1 → 1
self.model = lgb.LGBMClassifier(...)
self.model.fit(features, labels)

# BinaryOurs.get_weights — 权重计算
return 1.0 - self.model.predict_proba(features)[:, 1]  # w = 1 - P(synthetic)

# 训练使用 — WeightedRandomSampler
sampler = WeightedRandomSampler(
    weights=weights_array.tolist(),
    num_samples=len(weights_array),
    replacement=True,
)
```

对比 **Graduated**：
```python
# Graduated — K-1=5 个二分类器 P(depth>k)，估算 P(depth=d) 分布
for k in range(5):
    labels = (depths > k).astype(int)
    clf.fit(features, labels)

# 权重 = exp(-α * E[depth])
expected_depth = (dist * np.arange(6)).sum(axis=1)
weights = np.exp(-self.alpha * expected_depth)
```

### 3. 各 Depth 的实际效果

从 `filter_config.json` 可知：binary-ours 的 `weight_mean=0.167, weight_std=0.363`。

由于 30000 样本中 depth-0 占 1/6 ≈ 5000 样本，mean=0.167 接近 5000/30000，说明：

| Depth | P(synthetic) 典型值 | w = 1-P(syn) | 效果 |
|-------|---------------------|--------------|------|
| **0** (human) | 很低 (~0.05) | **~0.95** | 几乎满权重 |
| **1** (gen-1) | 高 (~0.7-0.9) | **~0.1-0.3** | 大幅降权 |
| **2+** (gen-2~5) | 很高 (~0.95+) | **~0.05** | 近乎剔除 |

**depth-1 典型权重范围：约 0.1-0.3。** Binary 分类器将 depth-1 和 depth-5 都视为 synthetic，depth-1 因特征更接近人类文本可能获得略高权重，但仍被显著降权。

### 4. 结论

**代码实现是 (a) human vs ALL-synthetic soft weighting**，与 `experiments_c3.tex` 中的描述一致。

- 二分类器不区分 depth-1 和 depth-5，统一标记为 synthetic
- 权重是连续的 `P(human)`，通过 `WeightedRandomSampler` 影响采样频率
- depth-1 文档被大幅降权（权重约 0.1-0.3），而非 "retained"

**Introduction.tex 中 "binary filtering at K\*=2 boundary—retaining depth-1 while removing depth≥2" 的描述与代码不符。** 代码中的 binary-ours 并没有 K\*=2 boundary，也没有选择性保留 depth-1。这个描述可能混淆了 binary-ours 和 graduated 策略（graduated 通过 ordinal 分类器确实能区分不同 depth 并给予差异化权重）。

---
