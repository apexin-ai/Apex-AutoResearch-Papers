## 2PL+γ vs 4PL+γ Joint Fit 消融对比 (S1-only, GSM8K, pooled 0.5B+1.5B)

Both runs use identical data (8 models × 1319 items) and MCMC settings (4 chains × 4000 samples = 16000 draws).

| 指标 | 4PL+γ | 2PL+γ | 差异 |
|------|-------|-------|------|
| gamma_mean | 0.1352 | 0.1389 | +0.004 (一致) |
| gamma_sd | 0.4168 | **0.2274** | **-46%** |
| gamma_CI95 | [-0.664, 0.963] | **[-0.306, 0.591]** | **宽度 1.63→0.90, 缩窄 45%** |
| CI excludes 0 | No | No | 均未排除零 |
| max_rhat | 1.0026 | 1.0024 | 均 OK |
| min_ESS | 2570 | **3604** | **+40%** |
| divergences | 0 | 0 | 均无 |
| PPP | 0.3244 | **0.2835** | 改善 |
| residual_MAE | 0.0363 | **0.0083** | **-77%** |
| fit_time_sec | 3424 | 2103 | **-39%** |

**结论**: 2PL 严格优于 4PL。4PL 额外 c/d 参数只增加噪声，未捕获有用信号。

**Coverage 缺失**: 两个 run 只有 joint_fit/ 子目录，需重跑完整 pipeline 获取 coverage。