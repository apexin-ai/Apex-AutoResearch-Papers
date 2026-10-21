# research 2pl vs 4pl ablation compare

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_2pl-vs-4pl-ablation-compare_20260515T103247_result.json`
- **Structured JSON:** [`5986c8573162bacf4dd0.json`](../../sessions/59/5986c8573162bacf4dd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the comparison report.

---

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
| coverage_95 | — | — | 均无（需重跑 pipeline） |

**数据来源**：
- 4PL: `results_pooled_05B_15B_gsm8k_s1only_2pl/` (D041 修复前，标记为 2pl 但实际跑的 4PL)
- 2PL: `results_pooled_05B_15B_gsm8k_s1only_2pl_v2/` (D041 修复后，真正的 2PL)

---

**结论**：2PL 在所有维度上优于 4PL——gamma 后验标准差缩窄 46%（可辨识性显著提升），残差 MAE 降低 77%（拟合质量大幅改善），ESS 提高 40%（采样效率更高），拟合时间缩短 39%。gamma 点估计几乎不变（0.135→0.139），说明 4PL 的额外 c/d 参数只增加了噪声而未捕获有用信号。但两者 CI 均未排除零，contamination 信号仍不显著。

**Coverage 数据缺失**：两个 16k-draw run 都只有 `joint_fit/` 子目录，无 coverage 评估。如需 coverage 对比，需用 `run_exp006.py --model-type 2pl_gamma` 重跑完整 pipeline。原始 4PL（4000 draws）的 coverage_95=0.5、coverage_80=0.375 可作参考基线。

---
