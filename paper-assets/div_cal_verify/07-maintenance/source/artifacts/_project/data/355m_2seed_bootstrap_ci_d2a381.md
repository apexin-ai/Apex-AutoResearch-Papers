Bootstrap CI (10000 resamples, gen7 PPL, 2-seed data)
| 比较 | 差异 | 95% CI | 排除零 |
|------|------|--------|--------|
| RGDS vs Random-50 | +15.15 | [12.60, 17.70] | Yes |
| RGDS vs External | +7.90 | [5.10, 10.70] | Yes |
| RGDS vs Uncurated | -2.81 | [-8.82, 3.20] | No |

不对称 Gap 模式（125M → 355M）
| 比较 | 125M gap | 355M gap | 变化率 | CI |
|------|----------|----------|--------|-----|
| RGDS vs Random-50 | +35.85 | +15.15 | -57.7% | [-60.5%, -55.6%] |
| RGDS vs Uncurated | +30.11 | -2.81 | -109.3% | [-135.6%, -91.0%] |
| RGDS vs External | +30.74 | +7.90 | -74.3% | [-82.7%, -66.5%] |

Note: 当前为 2-seed 数据（seed=456 训练尚未完成）。seed=456 到齐后自动升级为 3-seed 完整检验。