# analysis oracle gsm8k extended v2 final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle-gsm8k-extended-v2-final_20260515T033606_result.json`
- **Structured JSON:** [`7dc20b3a8df9544590ed.json`](../../sessions/7d/7dc20b3a8df9544590ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success，cron 已清理。

---

## exp006-oracle-gsm8k-extended-v2 最终结果

**实验配置**: 4PL+γ IRT MCMC, Oracle exposure, 16 models (Qwen2.5-0.5B × 9 + 1.5B × 7), 1319 items, 4 chains × 4000 samples

### IRT Fit 收敛诊断 ✓

| 指标 | 值 | 判定 |
|---|---|---|
| max Rhat | **1.002** | ✓ (< 1.05) |
| min ESS | **1221.9** | ✓ (> 400) |
| Divergent | **0** (0%) | ✓ |
| Fit time | 6240.3s | — |

### Gamma (Contamination Effect)

| 指标 | 值 |
|---|---|
| **gamma mean** | **3.773** |
| gamma SD | 0.504 |
| **95% CI** | **[2.741, 4.714]** |
| CI excludes zero | **Yes** |
| 50% CI | [3.443, 4.119] |

γ 显著为正，95% CI 远离零 → oracle exposure 下 contamination effect 极强。

### Posterior Predictive Check

| 指标 | 值 |
|---|---|
| PPP | **0.0** |
| Obs mean acc | 0.487 |
| Pred mean acc | 0.394 |
| Residual MAE | 0.096 |

PPP=0 表明模型存在系统性 misfit（预测准确率偏低约 9.3pp）。

### Calibration 评估

| 指标 | IRT_4pl_gamma |
|---|---|
| **MAE** | **0.0917** |
| ECE | 0.0894 |
| Brier | 0.0179 |
| Coverage 95/80/50 | 0.31 / 0.25 / 0.25 |
| Sharpness 95 | 0.048 |
| Kendall τ | 0.505 (p=0.01) |

### Baseline 对比表

| Method | MAE | ECE | Brier | C50 | C80 | C95 | S95 | τ |
|---|---|---|---|---|---|---|---|---|
| **IRT_4pl_gamma** | **0.0917** | 0.0894 | 0.0179 | 0.25 | 0.25 | 0.31 | 0.048 | 0.505 |
| B0_raw | **0.0050** | 0.0049 | 0.0001 | 0.88 | 0.94 | 1.00 | 0.052 | 0.838 |
| B1_remove_rescore | **0.0050** | 0.0049 | 0.0001 | 0.88 | 0.94 | 1.00 | 0.052 | 0.838 |
| B2_2pl_gamma | 0.0240 | 0.0236 | 0.0011 | 0.25 | 0.56 | 0.88 | 0.060 | 0.725 |
| B3_vanilla_4pl | 0.0324 | 0.0324 | 0.0011 | 0.00 | 0.00 | 0.00 | 0.030 | 0.780 |
| B4_linear_regression | 0.0078 | 0.0078 | 0.0001 | 0.81 | 0.94 | 1.00 | 0.120 | 0.746 |
| B5_emperor_mitigation | **0.0050** | 0.0049 | 0.0001 | 0.88 | 0.94 | 1.00 | 0.052 | 0.838 |
| B6_dcr_fuzzy | 0.1381 | 0.1373 | 0.0477 | 0.56 | 0.56 | 0.56 | 0.037 | 0.415 |

### 关键发现

1. **IRT 4PL+γ 收敛良好**（Rhat=1.002, ESS=1222, 0 divergent），fit 本身可信
2. **γ=3.77 [2.74, 4.71]** 显著为正——模型检测到强 contamination effect
3. **校准精度不佳**：MAE=0.092 远高于 B0_raw (0.005)、B4_linear_regression (0.008)；coverage 仅 31%（95% CI）
4. **B0/B1/B5 表现最优**：MAE=0.005, coverage≈100%，说明 oracle GSM8K 场景下 raw score 本身就很准，IRT 反而 overcorrects
5. **B6_dcr_fuzzy 最差**：MAE=0.138，严重低估
6. **PPP=0** 表明 4PL+γ 模型存在 systematic misfit，可能是 GSM8K 的 item response 结构不完全符合 IRT 假设

---
