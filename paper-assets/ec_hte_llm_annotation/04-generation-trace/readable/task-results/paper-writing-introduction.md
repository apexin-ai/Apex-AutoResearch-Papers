# paper writing introduction

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260521T051630_result.json`
- **Structured JSON:** [`1e1c6d12c205ef13524e.json`](../../sessions/1e/1e1c6d12c205ef13524e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`introduction.tex` written and registered. Summary:

- **P1** (Hook): LLM annotation in CSS, heterogeneous error rates (Ashwin et al.), propagation to CATE estimates
- **P2** (Importance): HTE guides policy, biased CATEs cause misallocation, subtle failure mode where correction hurts low-error subgroups
- **P3** (Gap): PPI/DSL correct marginals; PPCI targets outcome-side; Mozer limited to ATE; ForestIV targets outcome model; no method handles effect-modifier misclassification
- **P4** (Insight): Exact bias decomposition identity (not a bound), "debiasing can hurt" in 50% of configs, EC-HTE with HB + CausalForestDML, computable diagnostic AUC=0.833, conditional advantage explicitly stated
- **P5** (Contributions): 5 items, each mapped to a specific section, with exact experimental numbers

All style constraints satisfied: no em-dashes, no -ing endings, no AI markers, no forward claims, no "bias bound," EC-HTE framed as conditionally advantageous. ~800 prose words.

---
