# paper n2a bootstrap ci

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_n2a-bootstrap-ci_20260516T054107_result.json`
- **Structured JSON:** [`8a21fe0c44b28fb2ee8c.json`](../../sessions/8a/8a21fe0c44b28fb2ee8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's a summary of what was computed and added:

**Key numbers:**
- **Paired bootstrap 95% CI** (size-matched − depth 0-1): **[−0.0203, −0.0193]** — excludes zero, all 3 seeds consistently favor size-matched
- **Paired bootstrap 95% CI** (all − size-matched): **[−0.0326, −0.0316]** — data quantity effect
- **Cohen's d = −34.8**, **Hedges' g = −19.9** for size-matched vs depth 0-1

**Changes to `appendix_downstream.tex`:**
1. Added **Boot 95% CI column** to Table 5 (10,000 seed-level resamples)
2. Added **paired bootstrap CI** for the two key comparisons in the text
3. Added **Hedges' g** alongside Cohen's d
4. Added **Statistical caveats paragraph** explaining the n=3 limitation: bootstrap with 3 observations produces only 10 distinct means; narrow CIs reflect low seed variance, not high statistical confidence; document-level bootstrap not possible (no per-sample losses retained)

---
