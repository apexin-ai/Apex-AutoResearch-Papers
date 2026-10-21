# analysis rf keff correction

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rf-keff-correction_20260522T201836_result.json`
- **Structured JSON:** [`c197a91b5ea3c7390dde.json`](../../sessions/c1/c197a91b5ea3c7390dde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**Results: RF K_eff Non-Independence Correction**

| Regime | Method | η\_max sig | K\_eff sig |
|---|---|---|---|
| Adaptive | OLS | 11/12 | 8/12 |
| Adaptive | Wild Bootstrap v2 | 5/12 | 1/12 |
| Adaptive | Clustered SE | 8/12 | 0/12 |
| **RF** | **OLS** | **2/2** | **2/2** |
| **RF** | **Wild Bootstrap v2** | **2/2** | **2/2** |
| **RF** | **Clustered SE** | **2/2** | **2/2** |

**Per-condition detail:**

| Dataset | Method | K\_eff p | η\_max p | R² |
|---|---|---|---|---|
| mmlu | OLS | 6.3e-10 | 1.1e-65 | 0.734 |
| mmlu | Clustered SE | 3.7e-04 | 3.8e-28 | — |
| mmlu | Bootstrap v2 | 0.0035 | 0.0013 | — |
| arc\_challenge | OLS | 3.0e-12 | 2.9e-22 | 0.813 |
| arc\_challenge | Clustered SE | 0.0085 | 2.7e-05 | — |
| arc\_challenge | Bootstrap v2 | 0.0185 | 0.0219 | — |

**Key findings:**

1. **RF K\_eff remains significant under ALL correction methods** (2/2 on both clustered SE and bootstrap v2), in stark contrast with adaptive regime where K\_eff drops to 0/12 (clustered SE) or 1/12 (bootstrap).

2. This supports Claim 2: under random faults, panel diversity (K\_eff) genuinely predicts robustness; under adaptive attacks, this diversity benefit is largely illusory (inflated by non-independence).

3. SE inflation is moderate: 1.76x (mmlu) to 2.71x (arc\_challenge) for K\_eff — comparable to adaptive regime — but the RF signal is strong enough to survive it.

4. RF uses 2 conditions (dataset-level clean accuracy), no FDR needed. The RF error rate (1 - clean\_acc) is attack-independent, so all 6 attacks within a dataset would produce identical regression results.

Output saved to `/root/cert_manip_resist_eval/artifacts/results/plan001/rf_keff_correction.json`.

---
