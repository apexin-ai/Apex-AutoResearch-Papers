# sim theory empirical mape

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sim_theory_empirical_mape_20260521T080347_result.json`
- **Structured JSON:** [`f30aff92c2f9caca18b8.json`](../../sessions/f3/f30aff92c2f9caca18b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `artifacts/theory_empirical_mape.json`.

**Setup**
- N_MC=200 replicates × N=10k samples each
- Scope: 8 valid humaid configs (K=10) × 7 topologies = **56 scenarios**
- 1 zero matrix excluded (humaid_qwen3_few-shot-5). VAST (K=3) and civil_comments (K=2) confusion matrices are not in `artifacts/plan006/asv_empirical_results.json` locally — they live in `plan006_full` on the remote server.
- Used plan_006's own K-dependent DGP (which is what produced the analytical biases), not `annot_sensitivity/dgp.py` (which is K=3-only).

**Results**

| Topology | MAPE | Median APE | Max APE |
|---|---|---|---|
| confounding | 0.70% | 0.58% | 1.68% |
| frontdoor | 1.24% | 1.12% | 2.78% |
| collider | 1.86% | 1.59% | 3.53% |
| mbias | 2.08% | 1.75% | 7.43% |
| exposure | 2.11% | 1.79% | 4.92% |
| mediation | 2.40% | 2.22% | 4.50% |
| iv | 3.32% | 2.01% | 9.60% |
| **grand** | **1.96%** | — | — |

All topologies well under the 15% benign-topology threshold. IV's worst-case APE (9.6%) is on `humaid_qwen3_zero-shot`, where the analytical IV bias is small (0.138) so any MC noise translates to a larger relative error — consistent with the "plim converges slowly when denominator is small" caveat in the task spec.

---
