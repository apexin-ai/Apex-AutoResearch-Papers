# paper phase2 text changes

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_phase2_text_changes_20260522T113012_result.json`
- **Structured JSON:** [`c399f280fdad625fd239.json`](../../sessions/c3/c399f280fdad625fd239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The abstract text is correct — `pdftotext` just splits the line differently. All 8 modifications are verified.

Summary of all changes:

**MF1** (method.tex): Conjecture 1 verification updated to "10,000 random matrices per topology and K ∈ {3,5,7} with zero violations; adversarial search found no counterexamples"

**MF2** (abstract.tex): "five topologies never produce sign reversal" → "five topologies show no sign reversal across extensive numerical verification (proven analytically for confounding and collider via sufficient conditions; Appendix A)"

**SF2** (related_work.tex + references.bib): Added Feder et al. 2022 TACL citation with text-as-treatment/text-as-confounder taxonomy description; added `\cite{cheng_mayya_sedoc2024}` inline

**SF6** (conclusion.tex): Added DGP-independent sentence about the three core structural results

**M2** (method.tex → appendix_proofs.tex): Moved binarization collapse method + results to Appendix B.1 (`\label{app:binarization}`); left one-liner in method.tex; removed experiments subsection 4.3

**M5** (experiments.tex): Added "Complete ASV values across all topologies and error structures are reported in Appendix B" after N-sensitivity paragraph

**V1-V3** (appendix_proofs.tex → main.tex): Moved DAG taxonomy figure to main text (page 6, `figure*[t]`)

**M4** (appendix_proofs.tex): Added Notation section (Appendix C) with symbol table at end of appendix

Compilation: 0 errors, 0 undefined references, 20 pages total, main text ≤ 8 pages (Limitations starts page 9).

---
