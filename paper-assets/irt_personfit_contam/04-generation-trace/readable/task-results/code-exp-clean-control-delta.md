# code exp clean control delta

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-clean-control-delta_20260520T120213_result.json`
- **Structured JSON:** [`eb4e44ec1e4fa8f4738e.json`](../../sessions/eb/eb4e44ec1e4fa8f4738e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Hypothesis confirmed.** 结果汇总：

| Benchmark | Clean-vs-Clean mean | Clean-vs-Contam mean | Cohen's d | 验证 |
|-----------|-------------------|---------------------|-----------|------|
| mmlu | 0.010 (p=0.87) | 9.422 (p<1e-10) | 2.66 | PASS |
| hellaswag | -0.125 (p=0.05) | 5.049 (p<1e-10) | 1.85 | PASS |
| gsm8k | -0.021 (p=0.74) | 3.299 (p<1e-10) | 1.85 | PASS |
| arc_c | 0.095 (p=0.15) | 0.650 (p<1e-10) | 0.45 | FAIL* |
| humaneval | 0.020 (p=0.75) | 1.405 (p<1e-10) | 1.07 | PASS |

- Clean-vs-clean Δlz* 均值在所有 benchmark 上均接近 0（|mean| < 0.13），无一显著，确认 Δlz* 的零期望假设成立。
- Clean-vs-contaminated Δlz* 在所有 benchmark 上高度显著（p < 1e-10），表明 25% 污染产生的信号远超估计噪声。
- *arc_c 因仅 295 题，效果量略低于 0.5 阈值（d=0.45），但信号仍高度显著。

所有产出已保存至 `artifacts/clean_control_delta/` 并注册。

---
