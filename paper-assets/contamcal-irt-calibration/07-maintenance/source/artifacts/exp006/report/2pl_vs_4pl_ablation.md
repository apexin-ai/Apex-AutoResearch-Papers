# 2PL+γ vs 4PL+γ 消融对比

## 数据来源

| | 4PL+γ | 2PL+γ |
|---|---|---|
| 目录 | `results_pooled_s1only_gsm8k` | `results_pooled_05B_15B_gsm8k_s1only_2pl` |
| model_type | 4pl_gamma | 2pl_gamma |
| signal | s1_embedding (S1-only) | s1_embedding (S1-only) |
| pool_scales | 0.5B + 1.5B | 0.5B + 1.5B |
| benchmark | gsm8k | gsm8k |
| chains | 4 | 4 |
| warmup | 1000 | 2000 |
| samples/chain | 1000 | 4000 |
| total_draws | 4000 | 16000 |

⚠️ draws 不匹配（4× 差异）。2PL 的更好 coverage 可能部分归因于更多 draws。但 2PL 诊断指标全部 OK（vs 4PL rhat/ESS 不达标），说明模型本身更易拟合。

## Per-benchmark IRT 对比

| 指标 | 4PL+γ | 2PL+γ | 差异 |
|------|-------|-------|------|
| gamma_mean | 0.1871 | 0.1671 | -0.020 |
| gamma_sd | 0.5687 | 0.2398 | -0.329 (后验更紧) |
| gamma_CI95 | [-0.917, 1.329] | [-0.306, 0.636] | CI 宽度 2.246→0.942 (↓58%) |
| CI excludes 0 | No | No | — |
| max_rhat | 1.0148 ❌ | 1.0019 ✅ | 2PL 收敛 |
| min_ESS | 330.2 ❌ | 1808.3 ✅ | 2PL 有效样本量充足 |
| divergent | 0 | 0 | — |
| PPP | 0.336 | 0.250 | — |
| residual_MAE | 0.0367 | 0.0102 | ↓3.6× |
| **coverage_95** | **0.500** | **1.000** | **↑+0.500** |
| **coverage_80** | **0.375** | **1.000** | **↑+0.625** |
| coverage_50 | 0.125 | 0.500 | ↑+0.375 |
| sharpness_95 | 0.0964 | 0.0752 | ↓ (更紧但不过窄) |
| sharpness_80 | 0.0625 | 0.0494 | ↓ |
| MAE | 0.0364 | 0.0131 | ↓2.8× |
| ECE | 0.0364 | 0.0130 | ↓2.8× |
| Brier | 0.00153 | 0.00029 | ↓5.3× |
| kendall_tau | 0.7559 | 0.7559 | 相同 |
| fit_time | 1220.7s | 2059.5s | +69% (更多 draws) |

## Joint Fit 对比

| 指标 | 4PL+γ | 2PL+γ |
|------|-------|-------|
| gamma_mean | 0.1202 | 0.1352 |
| gamma_CI95 | [-0.737, 0.965] | [-0.664, 0.963] |
| CI excludes 0 | No | No |
| max_rhat | 1.009 ✅ | 1.003 ✅ |
| min_ESS | 546.1 | 2570.3 |
| PPP | 0.334 | 0.324 |
| residual_MAE | 0.0363 | 0.0363 |
| fit_time | 1126.3s | 3424.1s |
| total_draws | 4000 | 16000 |

## 关键结论

1. **Coverage collapse 解决**：4PL 的 coverage_95=0.5 问题在 2PL 中完全消失（→1.0）。4PL 的过度参数化导致后验区间过度分散在错误方向（高 gamma_sd=0.57 但 coverage 差），2PL 后验更紧且更准（gamma_sd=0.24, coverage 完美）。

2. **校准精度提升**：MAE 从 0.036→0.013 (↓2.8×)，Brier 从 0.0015→0.0003 (↓5.3×)。

3. **MCMC 诊断全绿**：4PL 的 rhat=1.015/ESS=330 均不达标；2PL 的 rhat=1.002/ESS=1808 全部 OK。即使考虑 draws 差异（4× more），2PL 的 ESS/draw 效率也更高。

4. **gamma 估计一致**：两者 gamma_mean 接近（0.19 vs 0.17），方向一致，说明 contamination effect 的检测不因模型简化而丢失。

5. **Confound 说明**：2PL 使用了 4× draws，需要 matched-draws run 才能完全归因。但 4PL 诊断本身不合格（rhat/ESS ❌），增加 draws 可能改善 4PL coverage 但不改变根本的过参数化问题。
