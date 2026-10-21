# math mf1b k3 symmetric proof

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_math_mf1b_k3_symmetric_proof_20260523T173653_result.json`
- **Structured JSON:** [`dc5dfdc67cf288520c7a.json`](../../sessions/dc/dc5dfdc67cf288520c7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Proof is complete and verified. Here's a summary of the results:

---

**Proof completed successfully.** Theorem covers all three topologies under proportional effects.

### Core result

For K=3 symmetric C₀ with C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3):

| Topology | Direction | Proven |
|----------|-----------|--------|
| Confounding (f=λg) | \|B\| non-decreasing | exact ✓ |
| Mediation (f=λg) | \|B\| non-decreasing | exact ✓ |
| Collider (h=λg) | \|B\| non-increasing | exact ✓ |
| Confounding (general f) | \|B\| non-decreasing | ε-approximate only (~10% violations, max deviation 0.004) |

### Key insight

C(δ) = (1-3cδ)I + cδ𝟏𝟏ᵀ stays in the one-parameter symmetric family. This yields:

$$V_B(s) = (1-3s)^2 \sum_j \frac{p_j^2 h_j^2}{(1-3s)p_j + s}$$

with derivative decomposing as a sum of terms, each containing the factor Λ_j(s) = -3(1-3s)p_j - 1 - 3s < 0. So dV_B/ds < 0 at **every** point, not just endpoints — stronger than the general-K proof which needs convexity + endpoint conditions.

### Outputs

- **Proof**: `artifacts/k3_symmetric_proof.tex` (ready to `\input{}` into appendix)
- **Verification**: `artifacts/k3_symmetric_verify.py` + `artifacts/k3_symmetric_verify_results.json`
- All 6 numerical tests pass (100k derivative sign checks, 10k configs per topology, derivative accuracy < 5e-10)

---
