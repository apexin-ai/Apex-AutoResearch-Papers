# ops gamma prior sensitivity sf5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gamma_prior_sensitivity_sf5_20260517T182947_result.json`
- **Structured JSON:** [`2cf75d1ddbe294e8224f.json`](../../sessions/2c/2cf75d1ddbe294e8224f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results saved to `/root/autodl-tmp/exp006/gamma_prior_sensitivity/gamma_prior_sensitivity_results.json`.

---

## 结果

### 任务 A：γ Prior Sensitivity（MMLU, J=16, 2PL+γ）

| Prior | γ̂ mean | γ̂ median | SD | 95% CI | PPP | Rhat | ESS | Time |
|---|---|---|---|---|---|---|---|---|
| N(0, 0.5) | 0.3425 | 0.3480 | 0.4009 | [-0.45, 1.11] | 0.254 | 1.0005 | 5661 | 49s |
| **N(0, 1)** (baseline) | **0.6551** | **0.6528** | **0.5441** | **[-0.41, 1.74]** | **0.192** | **1.0004** | **4146** | **50s** |
| N(0, 2) | 0.8857 | 0.8848 | 0.6600 | [-0.37, 2.20] | 0.161 | 0.9999 | 3806 | 50s |

**关键发现**：γ posterior 对 prior 敏感。tight prior (sd=0.5) 将 γ̂ 从 0.66 压缩到 0.34，loose prior (sd=2) 将 γ̂ 推高到 0.89。95% CI 下界基本稳定（均包含 0），但上界从 1.11 到 2.20 变化显著。这表明 N=16 的 data information 不足以 override prior 的影响。所有配置的 convergence 指标均正常（Rhat < 1.01, ESS > 3800, 0 divergences）。

### 任务 B：e_ij Exposure 分布

**Overall (16 models × 300 items = 4800 entries)**：
- mean=0.0407, median=0.0161, sd=0.0773
- range=[0.0000, 0.8788], IQR=[0.0077, 0.0373]
- 高度右偏：中位数远小于均值，多数 e_ij 值很小

**Per-dosage 分布基本一致**（exposure 是 per-model per-item RRF 信号，不直接依赖 dosage level）：
- d000: mean=0.0434
- d005: mean=0.0407
- d025: mean=0.0416
- d100: mean=0.0373

**Per-item**: item-mean 跨 items 的 SD=0.0395, 最高 item mean=0.3077, 最低=0.0040。

---
