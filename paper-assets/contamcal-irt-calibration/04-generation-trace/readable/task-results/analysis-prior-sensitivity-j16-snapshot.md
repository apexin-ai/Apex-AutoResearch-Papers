# analysis prior sensitivity j16 snapshot

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prior-sensitivity-j16-snapshot_20260521T183742_result.json`
- **Structured JSON:** [`25cc768c375ec78a5477.json`](../../sessions/25/25cc768c375ec78a5477.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 快照结果

### 进程状态
**PID 599770 仍在运行**，已运行 24:46，正在执行 baseline_10 的 MCMC sampling（日志显示 chain 4 完成，CmdStan done，sampling completed in 596.3s）。

### 文件状态

| 文件 | 状态 |
|------|------|
| `tight_05_results.json` | **已完成** |
| `baseline_10_results.json` | 不存在（正在采样中） |
| `loose_20_results.json` | 不存在 |
| `sensitivity_comparison.json` | 不存在 |

### tight_05_results.json 完整内容

```json
{
  "prior": "tight_05",
  "stan_file": "contam_irt_2pl_gamma_tight.stan",
  "n_models": 16,
  "n_items": 2000,
  "gamma": {
    "mean": -0.5412,
    "median": -0.5391,
    "sd": 0.2131,
    "q025": -0.9554,
    "q975": -0.1293,
    "p_negative": 0.9935
  },
  "diagnostics": {
    "max_rhat": 1.0083,
    "rhat_ok": true,
    "min_ess": 1472.5,
    "ess_ok": true,
    "divergent_count": 0,
    "divergent_pct": 0.0,
    "divergent_ok": true,
    "total_draws": 4000,
    "all_ok": true
  },
  "ppp": {
    "overall_ppp": 0.6577,
    "obs_mean_acc": 0.7198,
    "pred_mean_acc": 0.7207,
    "residual_mae": 0.0214
  },
  "fit_time_sec": 603.6
}
```

### MODEL_WHITELIST (16 models)

```python
MODEL_WHITELIST = {
    # Qwen 1.5B (8)
    "Qwen2.5-1.5B_d000_s123",
    "Qwen2.5-1.5B_d000_s42",
    "Qwen2.5-1.5B_d005_s123",
    "Qwen2.5-1.5B_d005_s42",
    "Qwen2.5-1.5B_d025_s123",
    "Qwen2.5-1.5B_d025_s42",
    "Qwen2.5-1.5B_d100_s123",
    "Qwen2.5-1.5B_d100_s42",
    # Qwen 3B (8)
    "Qwen2.5-3B_d000_s123",
    "Qwen2.5-3B_d000_s42_a32",
    "Qwen2.5-3B_d005_s123",
    "Qwen2.5-3B_d005_s42_a32",
    "Qwen2.5-3B_d025_s123",
    "Qwen2.5-3B_d025_v3_s42",
    "Qwen2.5-3B_d100_a32_s123",
    "Qwen2.5-3B_d100_a32_s42",
}
```

### 小结

tight_05 prior 结果良好：γ 后验 median=-0.539, 95% CI=[-0.955, -0.129], P(γ<0)=99.4%，诊断全部通过（Rhat≤1.008, ESS≥1472, 0 divergences），PPP=0.658。baseline_10 的 MCMC 采样刚完成（~596s），结果 JSON 应很快写出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "prior": "tight_05",
    "stan_file": "contam_irt_2pl_gamma_tight.stan",
    "n_models": 16,
    "n_items": 2000,
    "gamma": {
      "mean": -0.5412,
      "median": -0.5391,
      "sd": 0.2131,
      "q025": -0.9554,
      "q975": -0.1293,
      "p_negative": 0.9935
    },
    "diagnostics": {
      "max_rhat": 1.0083,
      "rhat_ok": true,
      "min_ess": 1472.5,
      "ess_ok": true,
      "divergent_count": 0,
      "divergent_pct": 0.0,
      "divergent_ok": true,
      "total_draws": 4000,
      "all_ok": true
    },
    "ppp": {
      "overall_ppp": 0.6577,
      "obs_mean_acc": 0.7198,
      "pred_mean_acc": 0.7207,
      "residual_mae": 0.0214
    },
    "fit_time_sec": 603.6
  }
}
```

</details>

---
