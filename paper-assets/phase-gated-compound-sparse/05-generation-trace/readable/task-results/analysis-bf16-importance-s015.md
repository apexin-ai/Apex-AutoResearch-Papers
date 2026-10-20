# analysis bf16 importance s015

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_importance_s015_20260514T062110_result.json`
- **Structured JSON:** [`e1f750244c8f47296c05.json`](../../sessions/e1/e1f750244c8f47296c05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## bf16_importance_s015 结果摘要

**数据质量：NaN=0，50 problems 全部完成，bf16 成功消除了 fp16 的数值问题。**

### Aggregate II (s=0.15)

| Phase | Mean | Median | 95% CI | Winsorized Mean |
|-------|------|--------|--------|-----------------|
| high_sparsity | **-0.1502** | 0.0058 | [-0.2946, -0.0554] | -0.0624 |
| mid_sparsity | **+0.4473** | 0.0807 | [+0.2680, +0.6687] | +0.3248 |
| low_sparsity | **+2.4058** | 0.3983 | [+1.4788, +3.6676] | +1.2789 |

- Gradient low/mid = **5.38×**
- Gradient low/|high| = **16.02×**
- Verdict: **PASS**（CI 不重叠 + 符号反转确认）

### Per-problem ii_low（供 permutation test）

| Problem | ii_low | Problem | ii_low |
|---------|--------|---------|--------|
| algebra/2470 | 0.1758 | prealgebra/192 | 0.2908 |
| intermediate_algebra/134 | 0.5178 | algebra/841 | 0.4504 |
| algebra/478 | -0.5199 | algebra/988 | -0.1209 |
| prealgebra/307 | -0.1514 | algebra/1004 | 0.7311 |
| counting_and_probability/761 | 1.7339 | prealgebra/1747 | -0.1034 |
| prealgebra/65 | 0.4150 | algebra/346 | 0.0179 |
| prealgebra/1840 | 0.0197 | geometry/248 | -0.0438 |
| precalculus/285 | 0.3268 | algebra/2593 | -0.4191 |
| algebra/2157 | -0.2967 | intermediate_algebra/1572 | 0.0668 |
| algebra/2743 | 0.3018 | geometry/846 | 0.5713 |
| number_theory/847 | 0.1361 | intermediate_algebra/199 | -0.0094 |
| prealgebra/631 | -0.0926 | intermediate_algebra/1014 | 0.3073 |
| prealgebra/1730 | 0.7028 | prealgebra/1995 | 0.9259 |
| prealgebra/1807 | 0.1211 | prealgebra/1742 | -0.8730 |
| algebra/1547 | 0.2006 | geometry/65 | 0.0126 |
| precalculus/1199 | 0.5725 | precalculus/659 | 0.4750 |
| prealgebra/1572 | 0.3045 | prealgebra/1973 | 0.3237 |
| number_theory/1287 | **4.1348** | prealgebra/1356 | 0.7377 |
| prealgebra/2057 | 1.1902 | geometry/465 | 0.3471 |
| algebra/972 | 1.3564 | intermediate_algebra/345 | **9.1029** |
| algebra/2277 | 0.5405 | intermediate_algebra/582 | 0.3488 |
| number_theory/427 | 0.3876 | number_theory/820 | 0.0057 |
| precalculus/768 | **7.7514** | prealgebra/1558 | 0.2029 |
| precalculus/323 | 0.5623 | counting_and_probability/159 | 1.4357 |
| algebra/853 | 0.8134 | algebra/892 | 0.2867 |

### 关键观察

1. **bf16 彻底消除了 NaN**——ii_low 50/50 valid，ii_high 49/50（1 个 None 是 0-segment 结构性缺失，非数值问题）
2. **ii_low 均值 2.41 远超 1.0**，确认 importance masking 在低稀疏度下的 compound interaction 显著放大
3. 高值尾部由 3 个 problem 驱动（ii_low > 4）：intermediate_algebra/345 (9.10)、precalculus/768 (7.75)、number_theory/1287 (4.13)
4. **符号反转**：high phase II<0 而 low/mid phase II>0，说明稀疏度方向性一致

---
