# code horseshoe murphy topel prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_horseshoe_murphy_topel_prep_20260522T065735_result.json`
- **Structured JSON:** [`b50d29d6fe505fffdcec.json`](../../sessions/b5/b50d29d6fe505fffdcec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 产出

| 文件 | 语法 | Smoke Test |
|------|------|-----------|
| `lib/priors.py` | OK | PASSED — 零信号 c_n ≈ 0.05, 非零信号 0.48/0.98 |
| `lib/murphy_topel.py` | OK | N/A (需 Stage 1/3 log-lik 函数) |
| `lib/rope_test.py` | OK | PASSED — 小效应 p_rope=0.998 → equivalent, 大效应 p_rope=0.000 → not_equivalent |
| `lib/README.md` | — | — |

### Horseshoe Shrinkage 结果
```
c_n posterior mean: [0.0552, 0.4815, 0.0559, 0.9813, 0.0519]
观测值(真值):       [0.0,    0.5,    0.0,    1.0,    0.0   ]
```
Horseshoe 正确地将零信号压缩至 ~0.05，同时保留非零信号的估计精度。相比 HalfNormal 的均匀 shrinkage，这正是我们要的自适应效果。

### Murphy-Topel 额外依赖
不需要。`jax.jacfwd` / `jax.jacrev` 是 JAX 内置的自动微分，环境中已有 JAX。

### 与 `models_v3.py` 集成建议

`_gmfrm_model_v3` 中需改 3 行（第 36-38 行）：

```python
# 删除:
sigma_c = numpyro.sample("sigma_c", dist.HalfNormal(1.0))
c_raw = numpyro.sample("c_raw", dist.HalfNormal(1.0).expand([N]))
c = numpyro.deterministic("c", c_raw * sigma_c)

# 替换为:
from lib.priors import horseshoe_prior_cn  # (放文件顶部)
c = horseshoe_prior_cn(N)
```

Murphy-Topel 需在 `fit_joint_gmfrm_v3` 返回后应用：从 MCMC 后验样本提取 Stage 1 和 Stage 3 的 covariance，计算修正因子，再 inflate c_n 的 posterior samples。这需要在 exp-003 的 runner 脚本中实现，而非改 model 定义本身。

---
