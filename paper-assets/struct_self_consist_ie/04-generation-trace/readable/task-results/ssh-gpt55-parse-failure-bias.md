# ssh gpt55 parse failure bias

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpt55_parse_failure_bias_20260522T082636_result.json`
- **Structured JSON:** [`0ac730cbe460bcba8c8c.json`](../../sessions/0a/0ac730cbe460bcba8c8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the results:

---

## GPT-5.5 Parse Failure Bias Analysis

**Data**: 200 instances x 8 samples = 1,600 total

**Key finding**: The reported 10.1% parse failure rate is inflated.
- 142/161 "zero-entity" samples are on **gold-empty instances** (n_gold=0; predicting empty is correct, F1=1.0) — these are NOT failures
- Only **19/1600 (1.2%)** are true parse failures (gold non-empty, pred empty, F1=0), across 5 instances
- 31/200 instances have n_gold=0 in text-based matching

**How the code handles failures**: Parse failures are treated as empty entity sets and **included** in all metrics (not excluded as the paper states). The 5 affected instances have greedy=0.0, MV=0.11, oracle=0.25.

| Metric | All (n=200) | Excl PF (n=195) | \|Δ\| | Material? |
|---|---|---|---|---|
| SJ ρ | 0.3461 | 0.3252 | 0.0209 | Borderline |
| Agree ρ | 0.3551 | 0.3350 | 0.0201 | Borderline |
| FK ρ | 0.3515 | 0.3286 | 0.0229 | Borderline |
| MV Δ (pp) | 1.39 | 1.13 | 0.26 pp | No |
| Degeneracy % | 50.00 | 50.77 | 0.77 pp | No |
| Greedy F1 | 0.6382 | 0.6546 | 0.0164 | No |
| MV F1 | 0.6521 | 0.6659 | 0.0138 | No |
| Oracle F1 | 0.7203 | 0.7324 | 0.0121 | No |
| Selection gap (pp) | 6.82 | 6.66 | 0.17 pp | No |

**Direction of bias**: Including the 5 true-PF instances (all greedy=0) pulls down means and slightly inflates correlation ρ by ~0.02. The bias is **conservative** — it makes MV Δ appear +0.26 pp larger and SJ ρ appear +0.02 higher, slightly favoring the paper's claims.

**Conclusion**: Exclusion does NOT materially affect estimates. All selection metrics (MV Δ, selection gap, degeneracy) shift < 0.5 pp. Correlation ρ shifts ~0.02 (borderline, not material). The true parse failure rate is 1.2%, not 10.1%.

---
