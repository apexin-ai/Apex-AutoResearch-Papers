# paper prop1 algebraic proof

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prop1-algebraic-proof_20260520T183523_result.json`
- **Structured JSON:** [`f73d2d85d323284d235c.json`](../../sessions/f7/f73d2d85d323284d235c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The appendix proof is complete at `docs/paper/appendix_proofs.tex`. Here's a summary of what it contains:

**Structure:**

1. **Notation & Key Identities** — Misclassified moments factor linearly through C: q=Cp, ct=C·E[TD], cy=C·E[YD].

2. **FWL Decomposition** — Lemma 1: plim τ̂ = τ + R(C)/D(C), where R(C) = E[Cov(T, f(A)|A*)] (residual within-A*-group covariance) and D(C) = E[Var(T|A*)] > 0.

3. **Confounding Proof** — Two results:
   - *Proportional case* (f=λg): B(C) = (1−η)·B_OV with η∈[0,1], giving exact interpolation between 0 and the OV bias.
   - *General case*: Rigorous Cauchy-Schwarz bound |B(C)| ≤ √(Var(g)·Var(f))/σ²_T. For the paper's parameters, this gives 0.590 < τ=2.0, guaranteeing sign preservation for ALL C.

4. **Mediation Proof** — Bias = weighted average of conditional indirect effects δ_j. Endpoints: B=0 at C=I, B=τ_ind at C=uniform. Sign preserved when sign(τ_dir)=sign(τ_total). Verified for paper parameters (0.5 vs 0.851).

5. **Exposure Counterexample** — Explicit K=3 construction with β=(0,1,−10), uniform prior, diagonal-dominant C (diag 0.60, 0.60, 0.51). plim β̂₁ = −1.903 while true β₁ = +1: clear sign flip. Mechanism: off-diagonal C₁₂=0.39 routes category-2 contamination into the A*=1 bin.

6. **Summary Table** — Sufficient conditions per topology with verification for the paper's DGP.

---
