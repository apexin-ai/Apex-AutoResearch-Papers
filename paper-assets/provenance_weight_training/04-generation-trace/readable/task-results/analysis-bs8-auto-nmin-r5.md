# analysis bs8 auto nmin r5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bs8_auto_nmin_r5_20260517T173855_result.json`
- **Structured JSON:** [`48d4a5cbf575c12eacb5.json`](../../sessions/48/48d4a5cbf575c12eacb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bs8_auto_nmin_r5 分析结果

### 训练完成状态
- **正常结束**（EXIT_CODE=0）
- train_loss: 5.163
- total_steps: 6103
- runtime: 14064s (~3.9h), 4.07 GPU-hours

### 评估指标
- **eval_ppl_holdout: 17.66**
- eval_loss_holdout: 2.8716
- eval_holdout_tokens: 4,077,068

### b* 分布
- mean=1.0957, median=0.9000, std=0.7563
- min=0.0, max=17.82
- pct_zero (b<0.01): 0.11%
- pct_below_0.5: 10.43%
- ESS mean=4.49, median=4.04 (n_min=4 约束生效)
- alpha_eff mean=0.70, median=0.76
- alpha_eff 达到上限(0.8)比例: 38.88%

### 对比分析
| 实验 | PPL | vs bs8_auto_nmin |
|------|-----|-----------------|
| uniform_seed42 | 17.6939 | **-0.034** (本实验更好) |
| adaptive_fix_seed42 (bs=16, n_min=2) | 17.6527 | +0.007 (几乎持平) |
| bs8_nmin2_seed42_r2 (bs=8, n_min=2) | 17.73 | **-0.070** (大幅改善) |
| nmin4_seed42 (bs=16, n_min=4) | 17.6947 | **-0.035** (本实验更好) |

### 结论判断
- **SUCCESS**
- PPL=17.66 < 17.6939 (uniform)，reweighting 有效
- 相比 bs8_nmin2 (17.73) 改善 0.07，证明 n_min=2 对 bs=8 确实太松
- 与 adaptive_fix (bs=16, n_min=2) 的 17.6527 几乎持平（差 0.007），验证了 coupling rule n_min=max(2, bs//2) 的有效性
- ESS median≈4.04 精确对应 n_min=4 约束，alpha_eff 非平凡（38.88% 在上限），说明自适应机制在积极调节权重而非退化为 uniform

**Hypothesis 验证**: coupling rule `n_min=max(2, bs//2)` 成功恢复了 bs=8 的性能至与 bs=16 相当水平。

---
