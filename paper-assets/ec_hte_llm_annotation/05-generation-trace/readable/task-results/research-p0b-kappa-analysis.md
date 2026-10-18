# research p0b kappa analysis

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p0b-kappa-analysis_20260523T135842_result.json`
- **Structured JSON:** [`f362c180e5b78dbed87a.json`](../../sessions/f3/f362c180e5b78dbed87a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/kappa_stratified_analysis.md`.

Key findings:

1. **520 synthetic configs**: All fall in bins 2–3 (κ ∈ [1.43, 2.22]). Bins 1, 4, 5 are empty because π̄=0.15 sets a floor of κ=1.43.

2. **EC-HTE is analytically unbiased** for all κ. In bin 3, global correction hurts at least one subgroup in 100% of configs.

3. **13 real LLM combinations**: 4 in bin 2 (κ ∈ [1.88, 1.96]), 9 in bin 3 (κ ∈ [2.21, 2.99]). None passes κ ≤ 1.25.

4. **Performance tradeoff**: At n_expert=500, EC-HTE matches global in bin 2 (RMSE ratio 1.01) but has 22% higher RMSE in bin 3 due to variance from estimating per-subgroup CMs with asymmetric K=4 errors. In the symmetric K=2 synthetic case, EC-HTE dominates at n_expert ≥ 100.

5. **Data limitation**: No per-config multi-method MC data exists for the 520 configs — only 3 regime-level comparisons available.

---
