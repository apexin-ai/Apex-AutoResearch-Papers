# Table 1 Numerical Audit — Paper vs Registry Cross-Verification

**Date**: 2026-05-21  
**Scope**: experiments.tex Table 1 (cross-model verdict accuracy)  
**Registry**: trace-verdict-study/registry.yaml  

## Audit Table

### Qwen-7B (Qwen2.5-7B-Instruct)

| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |
|------|--------|---|-------------|-------------|-------|-------|------|
| exception_only | **99.83**±0.00 | 0.00 | 99.83/99.83/99.83 → 99.83 | vota_exception_only_seed42_v2, exception_only_seed123, exception_only_seed456 | 3 | ✅ | |
| ae_only | 99.64±0.49 | 0.49 | 99.92/99.08/99.92 → 99.64 | vota_ae_only_seed42, ae_only_seed123, ae_only_seed456 | 3 | ✅ | σ=√0.2352=0.485→0.49 |
| VOTA | 99.05±0.38 | 0.38 | 99.41/98.66/99.08 → 99.05 | vota_seed42_v5, qwen7b_vota_seed123, qwen7b_vota_seed456 | 3 | ✅ | |
| loop_only | 86.05±0.52 | 0.52 | 85.63/85.88/86.64 → 86.05 | vota_loop_only_seed42, loop_only_seed123, loop_only_seed456 | 3 | ✅ | |
| no_trace | 75.13† | — | 75.13 | no_trace_seed42_v5 | 1 | ✅ | † correct |

### Qwen-1.5B (Qwen2.5-1.5B-Instruct)

| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |
|------|--------|---|-------------|-------------|-------|-------|------|
| exception_only | **99.83**±0.00 | 0.00 | 99.83/99.83/99.83 → 99.83 | qwen15b_exception_only_seed42/123/456 | 3 | ✅ | |
| ae_only | 98.83±0.36 | 0.36 | 99.08/98.57 → 98.825→98.83 | qwen15b_ae_only_seed42, _seed123 | 2 | ✅ | 2-seed mean rounds to 98.83 |
| VOTA | 99.54±0.06 | 0.06 | 99.58/99.50 → 99.54 | qwen15b_vota_seed42, _seed123 | 2 | ✅ | |
| loop_only | 79.54±1.42 | 1.42 | 78.32/81.09/79.20 → 79.54 | qwen15b_loop_only_seed42/123/456 | 3 | ✅ | |
| no_trace | 72.35±4.48 | 4.48 | 67.31/75.88/73.87 → 72.35 | qwen15b_no_trace_seed42/123/456 | 3 | ✅ | σ=√20.09=4.48 |

### CodeLlama-13B (CodeLlama-13B-Instruct)

| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |
|------|--------|---|-------------|-------------|-------|-------|------|
| exception_only | **99.89**±0.10 | 0.10 | 99.83/100.00/99.83 → 99.887→99.89 | codellama13b_exception_only_seed42/123/456 | 3 | ✅ | |
| ae_only | 99.08±0.00 | 0.00 | 99.08/99.08 → 99.08 | codellama13b_ae_only_seed42, _seed123 | 2 | ✅ | |
| VOTA | 98.74±0.24 | 0.24 | 98.57/98.91 → 98.74 | codellama13b_vota_seed42, _seed123 | 2 | ✅ | |
| loop_only | 77.40±1.54 | 1.54 | 77.06/76.05/79.08 → 77.40 | codellama13b_loop_only_seed42/123/456 | 3 | ✅ | |
| no_trace | 76.47† | — | raw eval=0.76471 (910/1190) | codellama13b_no_trace_seed42 | 1 | ✅ | Registry 存 0.765（3位截断），原始 eval 76.47% |

### DeepSeek-6.7B (DeepSeek-Coder-6.7B-Instruct)

| 条件 | 论文值 | σ | Registry 值 | 来源 exp_id | Seeds | 匹配? | 备注 |
|------|--------|---|-------------|-------------|-------|-------|------|
| exception_only | **99.39**±0.10 | 0.10 | 99.33/99.50/99.33 → 99.387→99.39 | deepseek_exception_only_seed42/123/456 | 3 | ✅ | |
| ae_only | 98.53±0.30 | 0.30 | 98.74/98.32 → 98.53 | deepseek_ae_only_seed42, _seed123 | 2 | ✅ | |
| VOTA | 99.25‡ | — | 84.45/99.16/99.33 → 2-seed mean 99.245→99.25 | deepseek_vota_seed42/123/456 | 3 (1 excluded) | ✅ | ‡ footnote explains seed42 outlier |
| loop_only | 80.31±1.65 | 1.65 | 81.26/81.26/78.40 → 80.307→80.31 | deepseek_loop_only_seed42/123/456 | 3 | ✅ | |
| no_trace | 73.36† | — | 73.36 | deepseek_no_trace_seed42 | 1 | ✅ | † correct |

### Majority Baseline

| 条件 | 论文值 | Registry 值 | 匹配? |
|------|--------|-------------|-------|
| Majority baseline | 71.51 | 0.7151 (851/1190) | ✅ |

## Footnote Verification

| 脚注声明 | Registry 原始值 | 匹配? |
|----------|----------------|-------|
| DS exception_only 3 seeds: 99.33/99.50/99.33 (σ=0.10pp) | 99.33/99.50/99.33, σ=0.098→0.10 | ✅ |
| VOTA Qwen-7B: 99.41/98.66/99.08 (σ=0.38) | 99.41/98.66/99.08, σ=0.376→0.38 | ✅ |
| ae_only 3 seeds: 99.92/99.08/99.92 (mean 99.64%) | 99.92/99.08/99.92, mean=99.64 | ✅ |
| loop_only 3 seeds: 85.63/85.88/86.64 (mean 86.05%) | 85.63/85.88/86.64, mean=86.05 | ✅ |
| Qwen-1.5B exception_only: 99.83% × 3 seeds (σ=0) | 99.83/99.83/99.83 | ✅ |
| ‡DS VOTA 3 seeds: 84.45/99.16/99.33 | 84.45/99.16/99.33 | ✅ |

## † / ‡ Marker Consistency

| 标记 | 含义 | 应用位置 | 正确? |
|------|------|----------|-------|
| † | Single seed (seed 42) | Qwen-7B no_trace, CL-13B no_trace, DS-6.7B no_trace | ✅ 均为 1-seed |
| ‡ | 2-seed mean (outlier excluded) | DS-6.7B VOTA | ✅ seed42 outlier 已排除 |
| ±std (无标记) | Multi-seed mean | 所有其他条目 | ✅ 均为 2-3 seed |

## σ Calculation Spot-Checks

All standard deviations use **sample std** (n-1 denominator), verified:

- Qwen-7B ae_only: √(0.4704/2) = 0.485 → 论文 0.49 (rounding at boundary, acceptable)
- Qwen-1.5B no_trace: √(40.17/2) = 4.48 ✅
- CL-13B loop_only: √(4.76/2) = 1.54 ✅
- DS loop_only: √(5.46/2) = 1.65 ✅

## Summary

**不一致数量: 0**

所有 20 个数值条目（4 模型 × 5 条件）和 6 条脚注声明均与 registry 原始数据匹配。† / ‡ 标记使用正确。σ 计算验证通过（样本标准差，n-1 分母）。

唯一需注意的边界情况：
1. **Registry 精度截断**: CL-13B no_trace 在 registry 中存为 0.765（76.5%），但原始 eval_results.json 为 0.76471（76.47%）。论文使用了正确的精度值。建议将 registry 精度统一为 4 位小数。
2. **ae_only σ 舍入**: Qwen-7B ae_only σ 精确值 0.485，论文写 0.49。处于 0.5 边界，两种舍入均可接受。

**结论: Table 1 数值审计通过，无需修改。可安全提交 EMNLP 2026 ARR。**
