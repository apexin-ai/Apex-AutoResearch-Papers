# writing formula dedup v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_formula_dedup_v2_20260524T064704_result.json`
- **Structured JSON:** [`406a58ec0069fe2889fa.json`](../../sessions/40/406a58ec0069fe2889fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation results:
- **0 undefined references**
- **0 errors**
- 36 pages total; appendix starts page 12
- Conclusion (Section 5) starts on page 9 — main text exceeds 8 pages by ~1 page (limitations don't count per EMNLP rules, but conclusion does)

## Summary

### 1. Formula de-duplication

**No formulas removed.** After systematically comparing all labeled equations in `method.tex` (3 equations: `eq:confounding`, `eq:exposure`, `eq:mediation`) and `experiments.tex` (0 equations) against the entire `appendix_proofs.tex` (19+ labeled equations), **no meaningful duplication exists**:

| Appendix equation | Closest main-text match | Relationship | Action |
|---|---|---|---|
| `eq:plim_conf` (scalar FWL form) | `eq:confounding` (matrix form) | Different representation | Keep — different math form |
| `eq:med_bias` (R(C)/D(C) form) | `eq:mediation` (lambda form) | Same result, different parameterization | Keep — already cross-references `\eqref{eq:mediation}` |
| `eq:fwl`, `eq:bias_decomp`, `eq:R`, `eq:D` | No main-text equation | Proof-internal Lemma | Keep — proof derivation steps |
| `eq:bias_conf`, `eq:lotc`, `eq:convex`, `eq:bov`, `eq:bbar` | Inline mentions in main text | Formal definitions for proofs | Keep — needed by proofs |
| `eq:dVB`, `eq:dd_condition` | Not in main text | Monotonicity proof steps | Keep — appendix-only |
| `eq:bias_col`, `eq:bbar_col`, `eq:fd_decomp` | Paragraph descriptions in main text | Formal derivations | Keep — different content |
| `eq:lambda_def`, `eq:vb_ratio` | Not in main text | Mediation leakage analysis | Keep — appendix-only |

Every appendix formula is either a different mathematical form, a proof derivation step, or a definition unique to the proof infrastructure. The appendix correctly cross-references main-text equations where relevant (e.g., `\eqref{eq:mediation}` at lines 438, 445, 473, 488).

### 2. Compilation

- 0 undefined references
- 0 errors
- Main text: conclusion starts on page 9 (exceeds 8-page limit by ~1 page; limitations excluded per EMNLP rules but conclusion counts)

---
