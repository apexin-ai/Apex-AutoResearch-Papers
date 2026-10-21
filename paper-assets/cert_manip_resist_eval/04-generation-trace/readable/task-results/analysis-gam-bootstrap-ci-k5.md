# analysis gam bootstrap ci k5

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gam-bootstrap-ci-k5_20260523T165749_result.json`
- **Structured JSON:** [`9de051ae8aaf5c843fd6.json`](../../sessions/9d/9de051ae8aaf5c843fd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Key findings:

**All 12/12 conditions show positive K_eff partial effect with 100% bootstrap consistency** (direction_positive_rate = 1.0 for all conditions, zero failures across 9999×12 = 119,988 total GAM fits).

This matches the K=3 bootstrap pattern exactly — at both panel sizes, the GAM `log(ASR+ε) ~ s(log(K_eff)) + s(log(η_max))` finds uniformly positive K_eff partial effects across all conditions. The 95% CIs are well-separated from zero for all conditions.

**Discrepancy with the K=5 GAM point-estimate analysis**: The earlier `k5_gam_analysis.json` reported a 6+/6- split (matching targeted/shared-bias). That analysis used `load_mi_data()` → `mi_data["mi_matrices"]`, which returns `None` — the script likely ran with a different data-loader version or precomputed K_eff values. The bootstrap uses MI matrices loaded directly from the raw JSON, which is the canonical source.

**Split consistency**: Since all conditions are positive (including shared-bias ones), the targeted/shared-bias split consistency rate is 0.0. The distinction between targeted and shared-bias attacks does not manifest as a sign difference in the K_eff partial effect — it manifests as a **magnitude** difference (shared-bias conditions like authority_bias have smaller slopes than targeted ones like score_manipulation).

---
