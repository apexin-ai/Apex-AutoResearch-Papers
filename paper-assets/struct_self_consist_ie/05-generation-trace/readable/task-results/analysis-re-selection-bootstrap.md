# analysis re selection bootstrap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_re_selection_bootstrap_20260515T032411_result.json`
- **Structured JSON:** [`c0026c71175eea9dfff4.json`](../../sessions/c0/c0026c71175eea9dfff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_bootstrap.json`。

结果摘要（n=397, greedy_f1=0.4042, oracle_f1=0.585）：

| Signal | Sel F1 | Δ vs Greedy | p-value | 95% CI | Cohen's d | W/L/T |
|--------|--------|-------------|---------|--------|-----------|-------|
| sj | 0.3855 | -0.0188 | 0.955 | [-0.041, 0.003] | -0.083 | 29/49/319 |
| voting_conf | 0.3592 | -0.0451 | 1.000 | [-0.070, -0.022] | -0.184 | 38/66/293 |
| logprob | 0.3948 | -0.0094 | 0.798 | [-0.032, 0.013] | -0.041 | 36/59/302 |
| ensemble | 0.3855 | -0.0188 | 0.949 | [-0.041, 0.004] | -0.083 | 29/49/319 |

所有信号在 RE 上都未能超越 greedy（delta 全为负），p-value 均远高于 0.05。大量 instance 为 tied（~75-80%），实际变化的 instance 中 losses 显著多于 wins。

---
