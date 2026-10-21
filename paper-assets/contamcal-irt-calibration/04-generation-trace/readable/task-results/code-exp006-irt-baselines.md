# code exp006 irt baselines

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_irt_baselines_20260514T044450_result.json`
- **Structured JSON:** [`96330d79a0acac6a8835.json`](../../sessions/96/96330d79a0acac6a8835.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是在 `/root/contamcal-irt-calibration/exp006/` 写入的 4 个文件：

| 文件 | 大小 | 功能 |
|------|------|------|
| `run_irt_calibration.py` | 17KB | CmdStanPy MCMC 4PL+γ IRT fitting，支持 eval-dir 和直接矩阵两种输入模式 |
| `baselines.py` | 18KB | 7 个 baseline（B0-B6），统一 `BaselineMethod.fit()` 接口，返回 calibrated_scores + 50/80/95% CIs |
| `evaluate_calibration.py` | 11KB | 5 个评估指标（MAE/Coverage/Sharpness/Kendall τ/Dose-response）+ LaTeX 表格输出 |
| `run_exp006.py` | 11KB | 端到端 pipeline：加载 exp-001 eval + exp-002 exposure → IRT + baselines → 评估 |

**Dry-run 验证通过**（4 benchmarks: mmlu, gsm8k, arc_challenge, humaneval）：
- IRT convergence: Rhat < 1.01, ESS > 1400, 0 divergences
- Stan 模型编译+采样正常（contam_irt_4pl_simple.stan）
- B0/B1/B5/B6 baselines 正常执行
- B4 已修复 constant-exposure 边界情况
- B2/B3 Stan baselines 通过 `--skip-stan` 跳过（dry-run 中可用）
- 输出 JSON + LaTeX 格式正确

---
