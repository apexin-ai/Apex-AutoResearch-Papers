# paper writing method

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260521T050131_result.json`
- **Structured JSON:** [`38e9ec2aacf2a5ea3c88.json`](../../sessions/38/38e9ec2aacf2a5ea3c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `docs/paper/method.tex`. The section covers all five content blocks within ~700 words:

- **Stage 1** (~200w): Dirichlet-Multinomial HB model with Gamma(2,1) hyperprior, Gibbs sampler specs, convergence diagnostics, and the n_expert/K ≥ 25 boundary condition
- **Stage 2** (~150w): Per-subgroup CM inversion with explicit invertibility assumption, κ > 100 singularity guard with global fallback, and contrast to global correction via Proposition 1
- **Stage 3** (~130w): CausalForestDML with honest splitting, plug-in SE propagation formula, and explicit statement that CM estimation uncertainty is not propagated (valid at n_expert ≥ 100)
- **Diagnostic** (~80w): Δπ×Δτ product as practical corollary, pilot sample requirements, AUC = 0.833
- **Composition** (~90w): EC-HTE + PPCI complementarity, bias reduction from 0.179 to <0.01

All three boundary conditions are stated. Notation matches theory.tex (δ_s, Δτ, π̄, C_s, κ, n_expert). No em-dashes, no -ing phrase endings, no AI style markers.

---
