# analysis deepseek pairwise bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_pairwise_bootstrap_20260515T134922_result.json`
- **Structured JSON:** [`53a8ad7df3d218d0dfbb.json`](../../sessions/53/53a8ad7df3d218d0dfbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|------|
| Observed diff (VOTA − no_trace) | **+11.09pp** |
| 95% CI | **[+7.90pp, +14.37pp]** |
| p-value | **0.0000** (0/10000 resamples ≤ 0) |
| Significant | **Yes** |

VOTA 在 DeepSeek-Coder-6.7B 上的 +11.09pp 提升高度显著，CI 下界 +7.90pp 远离零点。使用了 unpaired bootstrap（因 DeepSeek 实验未保存 per-sample predictions）。已写入 registry `deepseek_vota_seed42.metrics.bootstrap_pairwise`。

---
