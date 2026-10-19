# code within topo f1 bias

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_within_topo_f1_bias_20260523T145204_result.json`
- **Structured JSON:** [`fa22eec91deddcf63b55.json`](../../sessions/fa/fa22eec91deddcf63b55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results written. Key findings:

**Overall**: ρ = −0.14 (p=0.07, n=161). HumAID alone gives ρ = −0.10 (p=0.46), consistent with the paper.

**Per-topology (pooled, n=23 each)**:

| Topology | ρ | p |
|---|---|---|
| confounding | −0.56 | 0.006 |
| mediation | −0.57 | 0.005 |
| collider | +0.31 | 0.150 |
| exposure | −0.53 | 0.009 |
| **mbias** | **+0.87** | **<0.001** |
| frontdoor | −0.57 | 0.005 |
| iv | −0.70 | <0.001 |

The weak overall ρ is a Simpson's paradox: within 5 of 7 topologies the correlation is strongly negative (−0.53 to −0.70, all p < 0.01), meaning higher F1 → lower |bias| as expected. But **M-bias** shows a strong *positive* ρ (+0.87) and **collider** a weak positive (+0.31) — consistent with Conjecture 1 (collider/M-bias have non-standard bias behavior). Pooling across topologies with opposing signs washes out the signal.

CivilComments gives ρ = −1.0 everywhere because K=2 makes bias a monotonic function of the confusion matrix, so F1 rank perfectly determines bias rank.

---
