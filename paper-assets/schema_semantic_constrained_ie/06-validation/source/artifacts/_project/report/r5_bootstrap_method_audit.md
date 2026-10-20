# Bootstrap F1 计算方式核查报告

## 结论

**所有 bootstrap 脚本已使用 corpus micro-F1，与主表 (Table 2/4) 一致。无需修改。**

## 审计范围

| 脚本 | 用途 | F1 类型 |
|------|------|---------|
| `compute_bootstrap_ci.py` | ZS GPT-4o (SciERC + DocRED) | corpus micro-F1 ✓ |
| `compute_bootstrap_ci_ft.py` | FT LoRA composability (4 settings) | corpus micro-F1 ✓ |
| `compute_bootstrap_ci_llama.py` | ZS Llama (SciERC + DocRED) | corpus micro-F1 ✓ |

## 关键代码逻辑 (三个脚本均相同)

`bootstrap_f1` 函数 (以 `compute_bootstrap_ci.py:150` 为例):

```python
# 收集每个 sample 的 TP/gold/pred
tps = np.array([s["tp"] for s in sample_stats])
golds = np.array([s["gold"] for s in sample_stats])
preds = np.array([s["pred"] for s in sample_stats])

# Bootstrap: resample → SUM across resampled samples → compute F1
indices = rng.randint(0, n, size=(n_bootstrap, n))
tp_sums = tps[indices].sum(axis=1)      # 全局汇总
gold_sums = golds[indices].sum(axis=1)
pred_sums = preds[indices].sum(axis=1)
f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)  # micro-F1
```

**这是 corpus micro-F1**：先对 bootstrap sample 内所有 document 的 TP/gold/pred 求和，再从全局计数计算 P/R/F1。

如果是 document-level macro-F1，则会先对每个 document 独立算 F1，再取平均。代码中没有这种逻辑。

`paired_bootstrap_test` 使用同样的 sum-then-F1 逻辑。

## Registry Alignment

ZS v2 结果文件包含 registry alignment 校验：
- SciERC: delta ≤ 0.00pp (unconstrained, full_s1)
- DocRED: delta ≤ 0.01pp (rounding)

Llama 结果文件有 explicit tolerance check (0.05pp)。

FT composability 结果的 point estimate 直接从相同的 micro-F1 逻辑计算。

## ZS Bootstrap 一致性确认

- `compute_bootstrap_ci.py` (GPT-4o ZS): corpus micro-F1 ✓
- `compute_bootstrap_ci_llama.py` (Llama ZS): imports `bootstrap_f1` 和 `paired_bootstrap_test` from `compute_bootstrap_ci.py`,同一套代码 ✓
- DocRED p<0.001 (unconstrained vs full_s1): 基于 corpus micro-F1 的 paired bootstrap test，`p_value: 0.0` ✓

## 现有结果汇总 (无变化)

### ZS GPT-4o (compute_bootstrap_ci_results_v2.json)
| 对比 | Dataset | ΔR-F1 (pp) | 95% CI | p-value |
|------|---------|------------|--------|---------|
| unc vs full_s1 | SciERC | +0.13 | [-0.24, +0.58] | 0.582 |
| unc vs full_s1 | DocRED | +0.50 | [+0.23, +0.81] | <0.001 |

### ZS Llama (bootstrap_ci_results_llama.json)
| 对比 | Dataset | ΔR-F1 (pp) | 95% CI | p-value |
|------|---------|------------|--------|---------|
| unc vs full_s1 | SciERC | -0.04 | [-0.10, -0.01] | 0.011 |
| unc vs full_s1 | DocRED | +0.30 | [+0.06, +0.54] | 0.013 |

### FT LoRA (bootstrap_ci_ft_composability.json)
| Setting | ΔR-F1 (pp) | 95% CI | p-value |
|---------|------------|--------|---------|
| Qwen-LoRA-SciERC | -0.10 | [-0.30, 0.00] | 0.726 |
| Qwen-LoRA-DocRED | -0.37 | [-0.76, -0.05] | 0.014 |
| Llama-LoRA-SciERC | +0.02 | [0.00, +0.07] | 0.736 |
| Llama-LoRA-DocRED | +0.02 | [-0.15, +0.22] | 0.851 |

## 结论

无需修改任何脚本或重新运行实验。所有 bootstrap 统计量与主表的 corpus micro-F1 计算方式一致。
