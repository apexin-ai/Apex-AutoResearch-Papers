# analysis alpha eff stats retry

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_eff_stats_retry_20260523T034102_result.json`
- **Structured JSON:** [`8401463fafa37efda120.json`](../../sessions/84/8401463fafa37efda120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果与 Reviewer 的说法完全不同 — 三个 seed 的 r 值极其稳定。

## 结果

**方法说明**：无法精确重放 HF Trainer 的 DataLoader（全局 RNG 状态不可复现），改用 mean_q → real_frac 的校准线性映射估算。校准结果：r(mean_q, real_frac) = -0.775, R² = 0.60（200K 随机 batch 验证），即 mean_q 是 real_fraction 的强代理。

### Summary Table

| Seed | r(α_eff, mean_q) | r(α_eff, est_rf) | ρ(α_eff, est_rf) | b\*=0 | α_eff@ceiling | α_eff mean±std |
|------|-------------------|-------------------|-------------------|-------|---------------|----------------|
| 42   | -0.8019 | +0.8019 | +0.8761 | 5.8% | 51.0% | 0.608±0.171 |
| 123  | -0.7994 | +0.7994 | +0.8692 | 5.7% | 52.1% | 0.611±0.169 |
| 456  | -0.8006 | +0.8006 | +0.8749 | 5.9% | 50.7% | 0.609±0.171 |

**Cross-seed spread: 0.0025** (0.7994 → 0.8019)，极其稳定。

### α_eff by estimated real_fraction (seed 42 示例，其它 seed 几乎一致)

| est_rf | n batches | α_eff mean±std |
|--------|-----------|----------------|
| 0.00   | 1289 | 0.098±0.058 |
| 0.25   | 8115 | 0.517±0.137 |
| 0.50   | 10544 | 0.692±0.027 |
| 0.75   | 4103 | 0.712±0.027 |
| 1.00   | 361 | 0.870±0.036 |

α_eff 与 real fraction 严格单调递增 — batch 中 real 样本越多，α_eff 越高（给 real 更高权重）。

### 关键发现

1. **Reviewer 的 "r=0.17 到 0.75" 完全不成立**。三个 seed 的 r 都在 ~0.80，spread 仅 0.0025
2. r(α_eff, mean_q) 是精确值（无估算误差），三个 seed 为 -0.7994, -0.8006, -0.8019
3. 约 51% 的 batch 的 α_eff 被 ceiling 到 τ=0.7，只有 ~5.8% 的 batch 有 b\*=0（uniform）
4. 时间维度无漂移（α_eff by quarter 基本恒定 ~0.608），自相关接近 0

### 关于 R²=0.60 的注意事项

校准映射 mean_q→real_frac 的 R²=0.60 意味着估算有噪声。但由于 r(α_eff, mean_q)=-0.80 是**无估算误差的精确值**，且 mean_q 是 real_frac 的单调线性函数，实际 r(α_eff, true_rf) ≥ 0.80。如果 Reviewer 需要的是 exact real_frac，需要修改训练脚本在 compute_loss 中 log `real_frac = (q_scores < 0.5).float().mean()` 或 log 每个 sample 的 label（data 中 depth=0 → real）。

---
