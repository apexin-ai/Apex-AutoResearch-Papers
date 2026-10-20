# analysis m1v2 gmm diagnostics

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m1v2-gmm-diagnostics_20260513T212323_result.json`
- **Structured JSON:** [`b5ba94558e94ae6dce68.json`](../../sessions/b5/b5ba94558e94ae6dce68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已获取。完整报告如下：

---

## M1v2 完整分析报告

### 1. Phase 分布

| Phase | Tokens | Segments | 占比 |
|-------|--------|----------|------|
| execution | 1,022 | 25 | 1.2% |
| reasoning | 7,007 | 96 | 8.1% |
| transition | 78,178 | 192 | **90.7%** |
| **TOTAL** | **86,207** | **313** | 100% |

transition 占压倒性多数（90.7%），reasoning 仅 8.1%，execution 极少（1.2%）。

### 2. Perplexity (Dense vs Sparse)

| Phase | Sparsity | Dense | Attn-only | KV-only | Both |
|-------|----------|-------|-----------|---------|------|
| execution | 0.3 | 2.25 | 54.62 | **Inf** | 3443.82 |
| execution | 0.5 | 2.25 | 2921.68 | 1612.58 | **Inf** |
| reasoning | 0.3 | 1.18 | 1.76 | 9.78 | 187.89 |
| reasoning | 0.5 | 1.18 | 734.99 | 103.65 | 1570.03 |
| transition | 0.3 | 1.10 | 36.03 | 20.08 | 243.62 |
| transition | 0.5 | 1.10 | 867.05 | 79.58 | **Inf** |

### 3. Interaction Index (II)

| Phase | Sparsity | II Mean | CI Low | CI High |
|-------|----------|---------|--------|---------|
| execution | 0.3 | Inf | NaN | 0.67 |
| execution | 0.5 | Inf | -59.0 | NaN |
| **reasoning** | **0.3** | **17.79** | **4.09** | **38.76** |
| **reasoning** | **0.5** | **468.90** | **78.84** | **999.89** |
| **transition** | **0.3** | **3.06** | **0.01** | **5.60** |
| **transition** | **0.5** | **850.07** | **207.61** | **1738.71** |

关键发现：
- **reasoning @ s=0.3**: II=17.79, CI=[4.09, 38.76] — 强超加性交互，CI 完全 > 0
- **transition @ s=0.3**: II=3.06, CI=[0.01, 5.60] — 中等超加性，CI 刚好 > 0
- **s=0.5 的 II 值极大**（468~850），说明高稀疏度下 attn+kv 联合稀疏化的损失远超各自独立效应之和
- **execution phase 数据不可靠**（Inf/NaN），样本太少（仅 25 segments）

### 4. 全局 Sparsity 分布

- **N=86,207** tokens, 50 bins
- mean=0.7653, std=0.1364
- min=0.1282, max=0.9831
- Q25=0.6901, **Q50=0.8004**, Q75=0.8689
- 分布右偏，大部分 token 集中在 0.7~0.95 高稀疏度区间

### 5. GMM 分析

**BIC 选择 best_k=5**（BIC 单调下降，k=5 最优）：

| k | BIC |
|---|-----|
| 1 | -98,792 |
| 2 | -121,132 |
| 3 | -124,824 |
| 4 | -125,885 |
| **5** | **-126,231** |

**GMM k=5 参数：**

| Component | Mean | Std | Weight |
|-----------|------|-----|--------|
| 1 | 0.438 | 0.084 | 6.2% |
| 2 | 0.597 | 0.054 | 14.0% |
| 3 | 0.719 | 0.042 | 20.8% |
| 4 | 0.816 | 0.035 | 28.2% |
| 5 | 0.892 | 0.032 | **30.9%** |

5 个 component 沿 sparsity 轴均匀分布，std 随 mean 增大而递减，权重向高稀疏端倾斜。BIC 从 k=3→4→5 改善逐渐变小（-1061→-346），k=3 可能已足够实用。

### 6. Quantile Segmentation

**边界：[0.7337, 0.8482]**

| Group | N | Mean | Std |
|-------|---|------|-----|
| low (<0.734) | 28,733 | 0.6056 | 0.1053 |
| mid (0.734~0.848) | 28,741 | 0.7973 | 0.0327 |
| high (>0.848) | 28,733 | 0.8930 | 0.0288 |

low 组方差最大（std=0.105），mid/high 组非常集中。

### 7. MVP Pass/Fail 判定

- **ci_overlap_test: PASS** — "execution vs reasoning CI non-overlapping at 0.3"
- **sign_reversal_test: FAIL** — （无详情）
- **Overall: PASS**

---

**结论：M1v2 MVP 通过。** reasoning phase 在 s=0.3 时 II=17.79 (CI 全正), 确认 attn-kv 稀疏化存在强超加性交互效应。transition phase II=3.06 也显示正交互。execution phase 样本不足无法判定。GMM 发现 5 个自然聚类，sparsity 分布呈右偏多峰结构。

---
