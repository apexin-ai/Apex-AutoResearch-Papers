# code exp d hatespeech upgrade

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-d-hatespeech-upgrade_20260523T184152_result.json`
- **Structured JSON:** [`08fb912d1e444cdda800.json`](../../sessions/08/08fb912d1e444cdda800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both outputs are complete. Here's the summary:

---

**Outputs produced:**

1. **`artifacts/hatespeech_analysis.csv`** — 12 rows (3 LLMs × 4 subgroups), with columns: FPR, FNR, accuracy, κ(C_s), π_s, δ_s, predicted/observed bias (at Δτ=0.3), SE, max |bias|, debiasing-hurts fraction.

2. **`artifacts/hatespeech_analysis_report.md`** — Full report with tables and takeaways.

**Key numbers:**

| Metric | Value |
|--------|-------|
| Pooled R² (CivilComments, all 3 LLMs) | **0.944** |
| gpt-4o R² | 0.979 |
| gpt-3.5-turbo R² | 0.935 |
| gpt-4o-mini R² | 0.756 |
| Debiasing hurts | **55.0%** of LLM×subgroup×z×Δτ combos (66/120) |
| Most extreme bias | gpt-4o × S3 (long+question), max |bias| = 0.099, κ = 2.68 |
| κ range | 1.64 – 2.99 |
| FPR range across subgroups | 0.241 – 0.569 |
| FNR range across subgroups | 0.045 – 0.295 |

**Key findings:**
- Theorem 1 predictions match MC simulations well (R² ≥ 0.93 for gpt-4o and gpt-3.5-turbo; gpt-4o-mini is lower at 0.76 due to near-singular confusion matrices from very high FPR ~0.5)
- S3 (long text + question mark) is consistently the worst-conditioned subgroup across all LLMs
- 3 LLM-subgroup combinations show extreme bias amplification (max |bias| > 0.05), all involving S3 or S1 (question-containing subgroups)
- CivilComments R² is comparable to TweetEval (0.944 vs 0.951 pooled across overlapping LLMs)

---
