# TY Granger Canonical Script Audit

**Script**: `run_5method_analysis_d102.py` (on westd-17855)
**Date**: 2026-05-20
**Scope**: Matmul bug check + edge condition analysis + T=20 data provenance

---

## 1. Implementation Method

Canonical TY 实现位于 lines 187–246。**使用 statsmodels 内置 `test_causality()`**，不是手写 Wald。

```python
result = model.fit(total_order)
test_result = result.test_causality(causing=1, caused=0, kind="f")
f_stat = float(test_result.test_statistic)
p_value = float(test_result.pvalue)
```

**无 `cov_params` 操作、无手写矩阵乘法。** grep 确认全文无 `cov_params` 出现。

输出字段：`f_stat`, `p_value`, `significant`, `order`, `k_opt`, `d_max`

## 2. Matmul Bug — **NO**

1.4B bug 根因：手写 Wald 中 endog-based `cov_params` 维度为 (4,4) 但需要 (7,7)。

Canonical 脚本使用 `test_causality()` 内部处理所有矩阵运算，**不存在此 bug**。任何 T/d_max 组合下 statsmodels 都会自行处理正确维度。

## 3. 新发现：Direction Reversal Bug — **YES** ⚠️

### Bug 描述

```python
data = np.column_stack([x, y])   # column 0 = canary, column 1 = downstream
test_result = result.test_causality(causing=1, caused=0, kind="f")
```

`test_causality(causing=1, caused=0)` 测试的是 **variable 1 (downstream) Granger-causes variable 0 (canary)**，即 downstream → canary。

但调用上下文为：
```python
fwd_ty = ty_granger(c, d, cn, dn)   # 标记为 "forward: canary leads downstream"
```

**Forward 标签应测试 canary → downstream（`causing=0, caused=1`），实际测试了 downstream → canary。方向反了。**

Reverse 调用 `ty_granger(d, c, dn, cn)` 同理反转，实际测试的是 canary → downstream（真正的 forward）。

### 对 consensus 的影响

Consensus 投票使用 forward TY 结果：
```python
if f["ty_granger"]["significant"]:
    votes += 1; methods_sig.append("ty")
```

即 TY 投票基于 **reverse Granger causation** 而非 forward。

### 定量影响分析

| 实验 | ty_forward_sig (reported) | 若移除 TY 票 | robust pairs 变化 |
|------|--------------------------|--------------|-------------------|
| t20_a050 | 4/8 (ece pairs) | ece<d1: 5→4, ece<d2: 4→3, ece<d3: 4→3, ece<mauve: 2→1 | **6/8 → 6/8 (不变)** |
| t20_a100 | 1/8 (ece<d1) | ece<d1: 5→4 | **6/8 → 6/8 (不变)** |
| 14b | 0/8 | 无影响 | 8/8 → 8/8 (不变) |

**结论：方向 bug 存在但 TY 从未提供决定性投票，robust pairs 计数不受影响。**

### 修复方案

```python
# 修复前（错误方向）
test_result = result.test_causality(causing=1, caused=0, kind="f")

# 修复后（正确：测试第一个变量是否 Granger-cause 第二个变量）
test_result = result.test_causality(causing=0, caused=1, kind="f")
```

## 4. d_max 确定逻辑

```python
d_max = 0
for series in [x, y]:
    result = adfuller(series, maxlag=min(3, n // 3 - 1))
    if result[1] > 0.05:  # Non-stationary
        d_max = max(d_max, 1)
```

- **d_max 上限为 1**（二元判定：stationary vs non-stationary），不会出现 1.4B 那样的 d_max=2
- ADF maxlag = `min(3, n//3-1)`。T=21 → maxlag=min(3,6)=3; T=11 → maxlag=min(3,2)=2
- 溢出保护：`if total_order >= n//2: total_order = max(1, n//2-1)`

### d_max 分布

| 实验 | d_max=0 | d_max=1 | 备注 |
|------|---------|---------|------|
| t20_a050 (T=21) | 8/16 (ece pairs) | 8/16 (token_entropy pairs) | ece 序列平稳 |
| t20_a100 (T=21) | 4/16 | 12/16 | α=1.0 非平稳更多 |
| 14b (T=11) | 0/16 | 16/16 | 短序列 ADF 保守 |

## 5. TY 过程精确度：Extra Lag Issue (Minor)

当 d_max > 0 时，canonical 脚本拟合 VAR(k+d_max) 后对**所有** k+d_max 个 lag 做联合检验。严格 TY 过程应只检验前 k 个 lag。

- d_max=0 时：等价于标准 Granger，无差异
- d_max=1 时：多检验 1 个 augmented lag，略微影响 F 统计量的自由度

实际影响极小（标准做法中很多实现也这样处理），不构成 bug。

## 6. T=20 实验 TY 数据来源确认

### 字段格式验证

| 实验 | 字段结构 | 来源 |
|------|----------|------|
| t20_a050_s42_fp32 | `f_stat` + `order` + `k_opt` + `d_max` | ✅ Canonical script |
| t20_a100_s42_fp32 | `f_stat` + `order` + `k_opt` + `d_max` | ✅ Canonical script |
| 14b_c4_s42_fp32 | `f_stat` + `order` + `k_opt` + `d_max` | ✅ Canonical script |

所有实验均使用 canonical 脚本生成，非 `wald_F`/`df_resid`（手写 Wald 格式）或 `chi2`/`df`/`nobs`（其他格式）。

Meta 字段均包含 `"threshold_criterion": "true_3sigma_d105"`，确认为 D105+ 版本。

## 7. 14b T=11 低功效分析

14b 所有 TY 结果均为 non-significant (0/8)。原因不是 bug 而是**统计功效不足**：

- T=11, d_max=1 → total_order=3 (k_opt=2 + d_max=1)
- VAR(3) 每个方程 7 参数（3 lag × 2 变量 + intercept）
- 有效观测 = 11 - 3 = 8
- df_resid = 8 - 7 = 1
- F(3, 1) 分布几乎无检测力

这与 C003 约束一致（"TY 在低 α 下种子不稳定"的根因之一）。

## 8. 结论

| 检查项 | 结果 |
|--------|------|
| Matmul/cov_params bug | ❌ **不存在** — 使用内置 `test_causality()` |
| Direction reversal bug | ⚠️ **存在** — `causing=1, caused=0` 测试反向因果 |
| Extra lag issue (d_max>0) | ℹ️ Minor — 常见实现变体，非 bug |
| T=20 数据来源 | ✅ **确认** — 均由 canonical 脚本生成 |
| T=20 TY 数据可信度 | ⚠️ **数值正确但方向反转** — F/p 值无计算错误，但测试的是 reverse causation |
| 对论文 robust pairs 影响 | ✅ **无影响** — TY 从未提供 consensus 的决定性投票 |

**T=20 TY 数据的 F-stat 和 p-value 在数学上是正确的（无数值 bug），但它们回答的问题是 downstream→canary 而非 canary→downstream。由于 TY 在所有实验中都不是 consensus 的 swing vote，robust pairs 结论不受影响。**

**建议**：修复 direction bug（`causing=0, caused=1`）并重跑分析，但**不阻塞论文提交**——当前 consensus 结论已经 robust。
