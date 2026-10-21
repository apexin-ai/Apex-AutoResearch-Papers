# analysis n8 bootstrap ci

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n8_bootstrap_ci_20260515T030809_result.json`
- **Structured JSON:** [`11acf92272476f18359c.json`](../../sessions/11/11acf92272476f18359c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/n8_bootstrap_ci.json`。

结果 (n=529, B=10000, seed=42):

**Signal ρ with 95% CI:**

| Signal | ρ | 95% CI |
|---|---|---|
| voting_conf | +0.3792 | [+0.2987, +0.4556] |
| SJ | +0.3599 | [+0.2766, +0.4373] |
| EM | +0.2945 | [+0.2117, +0.3713] |
| FK | +0.2665 | [+0.1758, +0.3537] |
| logprob | +0.2052 | [+0.1186, +0.2908] |

**Δρ comparisons:**

| Comparison | Δρ | 95% CI | Significant? |
|---|---|---|---|
| SJ − logprob | +0.1547 | [+0.0737, +0.2340] | **Yes** |
| voting − SJ | +0.0193 | [−0.0327, +0.0725] | No |
| EM − SJ | −0.0653 | [−0.1296, −0.0027] | **Yes** (borderline) |

SJ 显著优于 logprob；voting_conf 与 SJ 无显著差异（CI 跨 0）；SJ 显著优于 EM（CI 刚好不包含 0，下界 −0.0027）。

---
