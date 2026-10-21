# CodeLlama-13B loop_only Seed Robustness Analysis

## Results Summary

| Metric | seed42 | seed123 | Δ |
|--------|--------|---------|---|
| Accuracy | 77.06% | 76.05% | -1.01pp |
| Pass Recall | 0.72 | 0.70 | -0.02 |
| Fail Recall | 0.89 | 0.90 | +0.01 |
| Pass Precision | 0.94 | 0.95 | +0.01 |
| Fail Precision | 0.56 | 0.55 | -0.01 |
| Lift over majority | +5.5pp | +4.5pp | -1.0pp |

seed123 95% CI: [73.9%, 78.6%] — seed42 的 77.06% 落在此 CI 内。

## Hypothesis Verification

- **假设**: accuracy ∈ [74%, 80%] → ✅ 76.05% 落在区间内
- **seed 差异**: 1.01pp，统计上不显著（两个 CI 大幅重叠）

## Tier 2 Collapse Conclusion

CodeLlama-13B loop_only 跨 seed 稳定表现为：
- Accuracy ≈ 76-77%（仅比 majority baseline 71.5% 高 ~5pp）
- 强 fail-recall (~90%) + 弱 pass-recall (~70%) 的偏置模式一致
- 与 no_trace baseline 的 gap 极小，确认 loop_only 信息对 CodeLlama-13B 不足

**结论**: Tier 2 collapse 是 seed-robust 的模型特性，非随机波动。CodeLlama-13B 无法从 loop-only trace 中提取足够判别信息。
