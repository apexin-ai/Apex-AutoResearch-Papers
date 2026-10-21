## H1+H2 FK 中介分析调查

### 论文原文 (experiments.tex:166)

> Length-controlled regression confirms 60% of the Flesch-Kincaid (FK) cross-axis effect is mediated by sentence length (Sobel z = 2.15, p = .031); under the assumed causal structure (Figure~\ref{fig:dag}), FK acts as a plausible mediator (S → FK → Y; \citealp{pearl2009causality}), yielding a direct-effect Style OR of 2.15 for GPT-4o (total OR = 2.70; Appendix~\ref{app:fk_length}).

### 涉及的两个分析

该句混合了两个独立分析的结果：

1. **OLS FK 中介分析** (`fk_length_control.py`) — X=style_axis, M=delta_sentlen, Y=delta_FK
   - 产出 Sobel z/p 和 "60% mediation"
2. **GEE FK 协变量分析** (`fk_gee_covariate.py`) — 在 judge 偏好 GEE 模型中加入 FK 作为协变量
   - 产出 Style OR（with/without FK control）

### 源文件内容

#### fk_length_control_results.json → mediation_passed_only

```json
{
  "a_X_to_M": 4.192,
  "b_M_to_Y_given_X": 0.387,
  "c_total_X_to_Y": 2.688,
  "c_prime_direct": 1.066,
  "indirect_ab": 1.622,
  "sobel_se": 0.451,
  "sobel_z": 3.595,
  "sobel_p": 0.000324,
  "proportion_mediated": 0.603
}
```

#### fk_gee_covariate.py → GPT-4o output (重跑确认)

```json
{
  "without_fk": {
    "n": 86,
    "style_or": 2.7002,
    "style_p": 0.001731
  },
  "with_fk": {
    "n": 86,
    "style_or": 2.1536,
    "style_p": 0.132118,
    "fk_or": 1.0524,
    "fk_p": 0.56235
  },
  "style_or_change_pct": -20.24
}
```

### 正确值确认

| 指标 | 论文值 | 正确值 | 来源 |
|------|--------|--------|------|
| Sobel z | 2.15 | **3.60** | fk_length_control_results.json → mediation_passed_only |
| Sobel p | .031 | **0.0003** | 同上 |
| Direct-effect Style OR | 2.15 | **2.15** ✓ | fk_gee_covariate.py → GPT-4o with_fk style_or=2.1536 |
| Total Style OR | 2.70 | **2.70** ✓ | fk_gee_covariate.py → GPT-4o without_fk style_or=2.7002 |

### 错误原因分析

**只有 Sobel z 和 p 是错误的。** OR 值正确。

错误机制：作者将 Style OR=2.15（FK-controlled direct effect）误写为 Sobel z=2.15，然后从错误的 z 值计算出 p：
- 2 × (1 - Φ(2.15)) = 2 × 0.0158 = **0.0316 ≈ .031** ← 论文中的 p 值

即 p=.031 不是独立来源，而是从错误的 z=2.15 推导出来的。

### 额外发现

FK-controlled Style OR=2.15 的 p 值为 **0.132**（非显著）。论文未报告此 p 值，但这意味着控制 FK 后 GPT-4o 的 style bias 不再显著，这实际上是一个更强的 mediation 证据（不仅 60% 被中介，且残余效应不显著）。

### 建议修复值

```
(Sobel z = 3.60, p < .001)
```

其余 OR 值（2.15, 2.70）正确无需修改。但建议补充 FK-controlled Style OR 的 p 值和显著性状态。

### gee_n355 中的 2.15 是巧合

`gee_n355_results.json` n=355 Qwen3-32B style_or=2.1502 也等于 2.15，但这是不同分析（n=355 scaled formality，Qwen3 judge）。论文中的 2.15 确实来自 fk_gee_covariate 的 GPT-4o direct effect，而非 Qwen3 n=355 值的误放。数值相同纯属巧合。
