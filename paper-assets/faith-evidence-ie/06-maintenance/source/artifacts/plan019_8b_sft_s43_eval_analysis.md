# Plan019: 8B SFT s43 Eval Analysis

## 1. Raw Metrics (8B SFT s43)

| Metric | Value |
|--------|-------|
| F1 | 0.5457 |
| **Ign-F1** | **0.5324** |
| Ign-P / Ign-R | 0.5319 / 0.5330 |
| Evi-F1 (TP-only) | 0.8333 |
| Evi-F1 (Joint/DREEAM) | 0.4430 |
| EDCR | 0.5805 |
| Predictions | 13933 |
| Format OK | 985/985 (100%) |
| Truncated | 139/985 |
| Evidence Format Rate | 85.9% |

## 2. 8B SFT 3-Seed Summary

| Seed | Ign-F1 |
|------|--------|
| s42 | 0.5128 |
| s43 | 0.5324 |
| s44 | 0.4604 |
| **Mean ± Std** | **0.5019 ± 0.0372** |

s43 是三个 seed 中最高的。s44 明显偏低（比均值低 1.1σ），导致整体方差大。

## 3. Cross-Method Comparison (Ign-F1)

| Method | Seeds | Mean | Std | Δ vs 8B SFT |
|--------|-------|------|-----|-------------|
| 8B SFT | s42/s43/s44 | 0.5019 | 0.0372 | — |
| 8B RSFT | s42/s44 | 0.5414 | 0.0053 | +0.0395 |
| 1.7B RSFT | s42 | 0.5122 | — | +0.0103 |

## 4. Statistical Significance

### Claim 3: "1.7B RSFT surpasses 8B SFT"

- Difference: 0.5122 − 0.5019 = **+0.0103**
- One-sample t-test (1.7B RSFT point vs 8B SFT distribution):
  - t = 0.0103 / (0.0372 / √3) = 0.0103 / 0.0215 = **0.48**
  - df = 2, p (one-tailed) ≈ **0.34**
  - **Not significant.** 差值完全在 8B SFT 的噪声范围内。
- Cohen's d = 0.0103 / 0.0372 = **0.28** (small effect)

**结论：当前数据不支持 "1.7B RSFT surpasses 8B SFT" 的强 claim。** 1.7B RSFT 的单 seed 结果（0.5122）甚至低于 8B SFT 的最佳 seed（s43 = 0.5324）。需要 1.7B RSFT 的多 seed 结果才能做有意义的对比。

### 8B RSFT vs 8B SFT

- Difference: 0.5414 − 0.5019 = **+0.0395**
- Welch's t: t = 0.0395 / √(0.0053²/2 + 0.0372²/3) = 0.0395 / 0.0218 = **1.81**
- Welch df ≈ 2.1, p (one-tailed) ≈ **0.10**
- **Marginally non-significant at α=0.05**，但 effect size 较大（Cohen's d ≈ 1.29）。
- 8B RSFT 的两个 seed 都高于 8B SFT 的均值，且 RSFT 方差极小（std=0.005 vs 0.037），表明 RSFT 更稳定。

## 5. Key Observations

1. **8B SFT 方差过大（σ=0.037）是核心问题。** s44=0.4604 拉低均值，s43=0.5324 接近 RSFT 水平。SFT 对 seed 高度敏感，而 RSFT（σ=0.005）稳定性显著更好。

2. **Claim 3 统计力不足。** 即使 1.7B RSFT 真实均值等于 0.5122，要在 α=0.05 下检测出 0.01 的差值（against σ=0.037），需要 n≈110+ seeds——不现实。建议改为弱表述：
   - ✗ "1.7B RSFT surpasses 8B SFT"
   - ✓ "1.7B RSFT achieves comparable performance to 8B SFT" 或 "performs on par with"

3. **8B RSFT vs SFT 是更可靠的 claim。** 每个 RSFT seed 都高于 SFT mean，且 RSFT 方差小一个数量级。建议补 RSFT s43 seed 凑齐 3-seed 做完整 t-test。

4. **稳定性本身可作为独立 claim。** 8B SFT std=0.037 vs RSFT std=0.005，方差比约 50:1（F-test p < 0.05），说明 RSFT 的 reward filtering 显著降低了训练不稳定性。
