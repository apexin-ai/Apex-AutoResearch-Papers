# code exp 011 causal forest

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-011-causal-forest_20260521T013156_result.json`
- **Structured JSON:** [`5e0323edb123ba387afd.json`](../../sessions/5e/5e0323edb123ba387afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment completed successfully. Here's a summary of the key results:

**exp-011 CausalForest EC-HTE: 100 MC runs, 8 configs, 800 total fits, ~35 min runtime**

### Key Findings

**1. ec_hte_forest has the lowest bias across all configs:**
- Overall mean |bias|: naive=0.1558, global=0.1073, **ec_hte=0.0608**
- With n_expert=500, ec_hte bias drops to near-zero (e.g., 0.0039-0.0098 in K=2 configs)

**2. Global correction HURTS low-misclassification subgroups (4 cases detected):**
- K=2 extreme: subgroup 0 (pi=0.05) naive |bias|=0.047 vs global=0.125 (2.6x worse)
- K=4 extreme: subgroup 0 (pi=0.05) naive |bias|=0.056 vs global=0.273 (4.9x worse)
- This is the "debiasing hurts" pattern — global over-corrects where misclassification is low

**3. Pattern consistent with exp-001 diff-in-means:**
- ec_hte best overall bias? **YES**
- Global hurts low-pi subgroups in extreme regimes? **YES**
- With more expert labels (n_expert=500), ec_hte bias approaches zero uniformly

**4. RMSE note:** ec_hte has higher RMSE in small-expert (n=100) K=4 configs due to noisy per-subgroup CM estimates (~25 experts per subgroup). With n_expert=500 the RMSE is competitive or better.

### Files
- Script: `/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py`
- Results: `results/exp011_causal_forest.csv` (144 rows)
- Log: `results/exp011_run.log` (298 lines)

---
