# analysis conll 4b inference v2 check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conll_4b_inference_v2_check_20260515T194957_result.json`
- **Structured JSON:** [`27696ce2b0e124f74b87.json`](../../sessions/27/27696ce2b0e124f74b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, cron deleted. Summary:

## exp_qwen3_4b_conll_scs_inference_v2 — SUCCESS

**状态**: 原始 PID 229738 被中止（57%处 shutdown），tmux 重新启动了 PID 232198 并成功完成。

### v2 (ckpt-4200) vs v1 (ckpt-3800) 对比

| 指标 | v1 | v2 | Delta |
|------|-----|-----|-------|
| greedy_f1 | 0.9251 | 0.9234 | **-0.17pp** |
| oracle_headroom | 1.57pp | 1.70pp | +0.13pp |
| SJ_rho_full | 0.4045 | 0.4217 | **+0.0172** |
| SJ_rho_cond | 0.4306 | 0.4590 | **+0.0284** |
| FK_rho_full | 0.3961 | 0.4181 | **+0.0220** |
| FK_rho_cond | 0.4200 | 0.4538 | **+0.0338** |
| LP_rho_full | 0.3186 | 0.3313 | +0.0127 |
| LP_auroc_full | 0.7689 | 0.7761 | +0.0072 |

**结论**: ckpt-4200 的 greedy_f1 略降 0.17pp，但所有 correlation 指标全面提升。结构化一致性指标（SJ/FK）提升幅度大于 logprob baseline（LP），尤其 conditional 场景下 FK_rho 提升 +0.034。Verdict 为 MARGINAL。

---
