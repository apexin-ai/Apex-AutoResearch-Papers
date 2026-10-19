# viz dirichlet overlay

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_dirichlet_overlay_20260521T080413_result.json`
- **Structured JSON:** [`e74a0ca361542516b91a.json`](../../sessions/e7/e74a0ca361542516b91a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Figure saved to `figures/paper/fig7_dirichlet_overlay.{pdf,png}`.

**Layout**:
- Left (Exposure): gray violation-rate fill drops from 85% (min_diag=0) to 12% (min_diag=0.9); dashed sign-flip rate falls to 0 above 0.7
- Right (IV): violation rate ≡ 1; dashed sign-flip drops from 52% to 0 above 0.5
- 14 empirical points overlaid at min_diag positions

**Empirical landing zones**:
- VAST/qwen2.5-7b (K=3, orange squares): min_diag ≈ 0.11–0.13 → **deep danger zone**
- HumAID (K=10, blue circles): min_diag ≈ 0.29–0.43 → mid-range (~50–65% theoretical violation)
- CivilComments/qwen2.5-7b (K=2, green triangles): min_diag ≈ 0.68–0.74 → near safe zone for exposure, but IV sign-flip risk persists

---
