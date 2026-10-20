# bugfix ty granger 14b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_ty_granger_14b_20260520T165937_result.json`
- **Structured JSON:** [`ea00b4ff5b08d70cce70.json`](../../sessions/ea/ea00b4ff5b08d70cce70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 8 对 TY Granger 现在都有正常的 chi2/p_value 值，无 error。

---

## 诊断报告

### 错误根因

`analyze_scale_14b_a050.py` 的 `ty_granger()` 函数手动构造 Wald 检验时，**参数协方差矩阵维度错误**：

```python
# BUG: 用原始 endog (T,2) 计算 Gram 矩阵 → kron((2,2),(2,2)) = (4,4)
cov_params = np.kron(np.linalg.inv(fitted.model.endog.T @ fitted.model.endog / n_used), sigma) / n_used
```

但约束矩阵 `C` 需要匹配 VAR 参数个数 = `2 * p_total + 1`（含截距）。对于 scale_14b：
- T=11, d_max=2（ADF 需二阶差分才平稳）, k=1, p_total=3
- `C` shape = `(1, 7)`, `cov_params` shape = `(4, 4)`
- `C @ cov_params` → **(1,7) @ (4,4) → matmul 维度不匹配**

应使用 VAR 的设计矩阵（含截距+滞后项）而非原始 endog 来构造协方差。

### 修复

将手写 Wald test 替换为 statsmodels 内置 `fitted.test_causality(causing=1, caused=0, kind='wald')`，内部正确使用完整的参数协方差矩阵。

### 重跑结果

| Pair | chi2 | p_value | significant |
|------|------|---------|-------------|
| token_entropy→perplexity | 2.06 | 0.560 | No |
| token_entropy→distinct_1 | 16.14 | 0.001 | **Yes** |
| distinct_1→perplexity | 0.43 | 0.933 | No |
| ece→perplexity | 3.64 | 0.303 | No |
| distinct_2→perplexity | 0.94 | 0.816 | No |
| distinct_3→perplexity | 0.35 | 0.950 | No |
| mauve→perplexity | 96.29 | 0.000 | **Yes** |
| effective_rank→perplexity | 3.93 | 0.269 | No |

TY Granger 从 0/8 变为 **2/8**（token_entropy→distinct_1, mauve→perplexity）。

### 注意

d_max=2 对所有 pair 成立，p_total=3，nobs 仅 8。T=11 下 TY 统计功效很低。mauve→perplexity 的 chi2=96.29 可能是过拟合 artifact（8 obs, 3 lag parameters），需谨慎解读。Summary 从 `K>=3: 0/8` 维持不变。

---
