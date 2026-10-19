# sim iv dirichlet subspace

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sim_iv_dirichlet_subspace_20260521T051001_result.json`
- **Structured JSON:** [`b540ddef14ffdfbcc3ac.json`](../../sessions/b5/b540ddef14ffdfbcc3ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results delivered.

**Headline numbers** (K=3, 100k samples/threshold, seed 42):

| Subspace | Violation | Sign-Flip | Amplification | Worst |
|---|---|---|---|---|
| Full | 100.0% | **51.7%** | 48.3% | 10⁵× |
| d≥0.5 | 100.0% | 0.0% | 100.0% | 28.6× |
| d≥0.7 | 100.0% | 0.0% | 100.0% | 2.4× |
| d≥0.9 | 100.0% | 0.0% | 100.0% | 1.2× |

Full-space sign-flip 51.7% matches the paper's 52.6% within MC error (different precompute seed; well inside the 2% tolerance).

**Key qualitative finding**: diagonal-dominance does **not** rescue IV the way it rescues exposure. Because FS₁ is the unique max of FS, (C·FS)₁ < FS₁ almost surely for any C ≠ I, so the Wald denominator monotonically contracts → 100% amplification at every threshold. Increasing d only converts sign flips into same-sign amplification; it never restores correctness. Even at d≥0.9 every Wald estimate inflates |τ|.

**Artifacts written**:
- `artifacts/mvp_iv_dirichlet_subspace.py` — self-contained script
- `artifacts/mvp_iv_dirichlet_subspace_output.log` — console output
- `artifacts/iv_dirichlet_subspace_results.json` — structured results
- `artifacts/iv_dirichlet_subspace_appendix.tex` — appendix paragraph + table

(Ran locally rather than on home-1x5090: the project's `annot_sensitivity/` module lives only on the local box, and the analysis is pure-numpy ~1.3s — no GPU needed. JSON path matches the spec.)

---
