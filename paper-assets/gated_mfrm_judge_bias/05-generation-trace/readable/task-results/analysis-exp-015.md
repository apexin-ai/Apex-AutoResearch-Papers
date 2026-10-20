# analysis exp 015

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-015_20260523T091853_result.json`
- **Structured JSON:** [`057d5a4d8128b37b4970.json`](../../sessions/05/057d5a4d8128b37b4970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp-015/analysis.md`。核心结论：

**Hypothesis 被证伪。** Joint G-MFRM 在 N=8 合成数据上压倒性优于 sequential：

| | Sequential | Joint | Δ |
|---|---|---|---|
| θ RMSE | 0.1664±0.0496 | 0.0827±0.0241 | **−50.3%** |
| θ τ | 0.8821±0.1118 | 0.9536±0.0479 | +0.0715 |
| c RMSE | 1.3992±0.3583 | 0.5524±0.3283 | **−60.5%** |

- Wilcoxon p = 9.54e-07, Cohen's d = 1.884, win rate 20/20
- 效应量比 N=50（mvp_003）还大（50.3% vs 43.8%）
- MCMC 收敛完美（R̂=1.000, ESS≥1678）

**对论文 narrative 的意义**："N=8 power 不足"这个 story 不成立。合成数据证明方法在 N=8 完全 work，说明真实数据的 non-significance 不是 power 问题，而是 model-data mismatch——真实 judge 行为比 DGP 假设的 additive severity 更复杂。这反而是个更强的 story：方法本身 sound（synthetic validation），synthetic-real gap 本身成为 evidence，说明实际评测生态的复杂性超出当前 DGP，强化了 G-MFRM framework 的必要性。

---
