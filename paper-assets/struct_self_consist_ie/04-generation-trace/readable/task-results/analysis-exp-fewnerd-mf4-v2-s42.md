# analysis exp fewnerd mf4 v2 s42

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_fewnerd_mf4_v2_s42_20260521T074321_result.json`
- **Structured JSON:** [`4ac85ddf35b72aefd2df.json`](../../sessions/4a/4ac85ddf35b72aefd2df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`exp_fewnerd_mf4_v2_s42` 已推进到 DONE (conclusion=negative)。

**s42 vs s123 对比：**

| 指标 | s42 | s123 |
|------|-----|------|
| greedy_f1 | 0.7883 | 0.7883 |
| oracle_f1 | 0.8783 | 0.8891 |
| oracle_headroom | 0.090 | 0.101 |
| rho_SJ_full | **0.163** | **0.307** |
| rho_kappa_full | 0.048 | 0.159 |
| rho_SJ_cond | 0.199 | 0.197 |
| rho_kappa_cond | -0.033 | 0.003 |
| logprob_rho_full | 0.154 | 0.219 |
| logprob_auroc_full | 0.577 | 0.606 |
| verdict | **FAIL** | **MARGINAL** |

s42 的 full-set 相关性指标全面低于 s123，尤其 rho_SJ_full 几乎腰斩（0.163 vs 0.307）。seed 间方差很大，信号不稳定。

---
