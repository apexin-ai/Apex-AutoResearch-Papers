# code bootstrap 10k holm cohensd

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_10k_holm_cohensd_20260521T074616_result.json`
- **Structured JSON:** [`2d8a85e14ddddfb84e0b.json`](../../sessions/2d/2d8a85e14ddddfb84e0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The user's ATE=0.074 matches `|mean(orig - cf)|` = 0.0745 (NLI filtered). Sign convention difference. My Cohen's d = -0.073 uses the exact formula requested: (mean_academic - mean_conversational) / pooled_SD.

Results:

## Bootstrap 10k
GPT-4o formality: P(formal)=63.0%, CI [55.7%, 70.3%], raw p = 0.0004
  (N pairs=88, N comps=173, 10k iterations, 4/10000 below 0.5)

## Holm-Bonferroni (family=6)
| Judge | Axis | Raw p | Adjusted p | Significant? |
|---|---|---|---|---|
| GPT-4o | formality | 0.0004 | 0.0012 | Yes |
| GPT-4o | verbosity | 0.0001 | 0.0006 | Yes |
| GPT-4o | register | 0.0400 | 0.0800 | No |
| Qwen3-32B | formality | 0.0001 | 0.0006 | Yes |
| Qwen3-32B | verbosity | 0.0001 | 0.0006 | Yes |
| Qwen3-32B | register | 0.0763 | 0.0800 | No |

4/6 significant after Holm correction. Register axis loses significance for both judges.

## Cohen's d
Qwen3-32B Register: d = −0.073
  (N=94, mean_acad=6.011, mean_conv=6.128, ATE=−0.117, pooled_SD=1.609)

Negligible effect size. The ATE sign differs from your stated 0.074 because yours is likely `mean(orig − cf)` = +0.074, while mine is `mean(acad − conv)` = −0.117 (paired, direction-adjusted). Absolute magnitude is consistent: tiny effect, non-significant.

Script saved at `csd_pipeline/bootstrap_10k_holm.py` on both local and server.

---
