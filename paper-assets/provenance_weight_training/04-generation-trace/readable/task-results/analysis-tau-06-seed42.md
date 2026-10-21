# analysis tau 06 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_06_seed42_20260515T134957_result.json`
- **Structured JSON:** [`6f7ab43083ba1ca12c34.json`](../../sessions/6f/6f7ab43083ba1ca12c34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析报告：

---

## tau_06_seed42 实验结果

**结论: SUCCESS** — τ=0.6 与 τ=0.8 baseline PPL 差距仅 0.03，支持 Claim 3（τ 是 robust hyperparameter）。

### 核心指标

| 指标 | 值 |
|---|---|
| eval_ppl_holdout | **17.68** |
| eval_loss | 2.8725 |
| train_loss | 9.275 |
| total_steps | 6103 |
| train_runtime | 13437s (3h44m) |
| checkpoint | `/root/.../tau_0.6_seed42/final` |

### b* 分布

| 统计量 | τ=0.6 | τ=0.8 (baseline) |
|---|---|---|
| mean | 0.590 | 1.399 |
| median | 0.375 | 0.871 |
| std | 1.069 | — |
| p25/p75 | 0.12 / 0.66 | — |
| zero_frac | 15.6% | — |

τ=0.6 的 b* 显著更低（median 0.375 vs 0.871），符合预期——更低的 τ 意味着更严格的 α_eff 下限，更多 batch 触发 b*=0（15.6%）。

### 对比

| 实验 | eval_ppl | Δ vs τ=0.8 |
|---|---|---|
| golden_ratio_seed42 | 17.654 | -0.004 |
| **adaptive_fix_seed42 (τ=0.8)** | **17.65** | **baseline** |
| **tau_06_seed42 (τ=0.6)** | **17.68** | **+0.03** |
| uniform_seed42 | 17.69 | +0.04 |
| ess_only_seed42 | 17.73 | +0.08 |

τ=0.6 PPL (17.68) 与 τ=0.8 (17.65) 差距 0.03 < 0.05 阈值，且仍优于 uniform (17.69)。τ 在 [0.6, 0.8] 范围内对最终 PPL 不敏感。

---
