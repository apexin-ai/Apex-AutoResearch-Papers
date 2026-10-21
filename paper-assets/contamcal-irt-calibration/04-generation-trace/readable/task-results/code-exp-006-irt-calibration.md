# code exp 006 irt calibration

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-006-irt-calibration_20260513T174017_result.json`
- **Structured JSON:** [`15fff1e14bf45d7e8ead.json`](../../sessions/15/15fff1e14bf45d7e8ead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7 个文件全部创建完成：

| 文件 | 说明 |
|------|------|
| `contam_irt_4pl_me.stan` | 4PL+γ + measurement error (tau latent + sigma_e jointly estimated) + generated quantities (calibrated_score, log_lik) |
| `contam_irt_4pl_simple.stan` | 4PL+γ 无 ME (ablation baseline) + generated quantities |
| `contam_irt_2pl.stan` | 2PL+γ (baseline 2 用) + bernoulli_logit + generated quantities |
| `fit_irt.py` | IRT fitting 主脚本，`--model-type me/simple/2pl`，CmdStanPy NUTS 4chains×2000samples，收敛诊断 (Rhat/ESS/divergent)，输出 posterior summary + calibrated CSV |
| `compute_baselines.py` | 7 baselines (B0-B6)，B2/B3 用 Stan fit，B1/B4/B6 带 bootstrap CI |
| `evaluate_calibration.py` | 5 metrics (MAE/Coverage/Sharpness/Kendall τ/Dose-response) + bootstrap 95% CI + LaTeX table 输出 |
| `run_exp006.sh` | 编排脚本，per-benchmark fit + baselines + evaluate + aggregate |

---
