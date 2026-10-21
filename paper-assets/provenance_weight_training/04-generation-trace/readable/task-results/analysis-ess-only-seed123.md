# analysis ess only seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ess_only_seed123_20260515T214322_result.json`
- **Structured JSON:** [`90bed1d286c494f5f525.json`](../../sessions/90/90bed1d286c494f5f525.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（status=DONE, conclusion=success）。

---

## ess_only_seed123 实验结果汇总

| 指标 | 值 |
|------|-----|
| **eval_ppl_holdout** | **17.72** |
| eval_loss_holdout | 2.8746 |
| eval_holdout_tokens | 4,077,068 |
| train_loss (weighted) | 10.2159 |
| train_steps | 6103 |
| train_runtime | 3h 36m |

### 对比基线

| 方法 | PPL | vs ess_only_seed123 |
|------|-----|-----|
| **ess_only_seed123** | **17.72** | — |
| ess_only_seed42 | 17.73 | -0.01 |
| uniform_seed123 | 17.6861 | +0.0339 |
| adaptive_fix_seed123 | 17.6432 | +0.0768 |

**vs_uniform_delta = +0.034** (ESS-only 更差)
**vs_adaptive_delta = +0.077** (ESS-only 更差)

### b* 统计

| 统计量 | 值 |
|--------|-----|
| mean | 3.55 |
| median | 1.59 |
| std | 4.72 |
| min / max | 0.23 / 20.0 |
| p10 / p25 / p75 / p90 | 0.54 / 0.84 / 3.83 / 9.60 |

b* 分布高度右偏（median=1.59 远小于 mean=3.55），说明大部分 batch 的 b* 较小（权重差异不大），但有长尾 batch b* 很大（极端 downweight）。约 10% 的 batch b* > 9.6，这些 batch 中部分样本被过度 downweight。

### 结论

结果符合预期：ESS-only 的 PPL 高于 uniform（+0.034）和 adaptive（+0.077），因为没有 α_eff 下界保护，过度 downweight 了部分有效数据。两个 seed（42 和 123）的 ESS-only PPL 高度一致（17.73 vs 17.72），验证了实验的可复现性。

---
