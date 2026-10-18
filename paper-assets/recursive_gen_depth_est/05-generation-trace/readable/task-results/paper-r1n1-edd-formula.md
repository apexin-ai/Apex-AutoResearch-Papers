# paper r1n1 edd formula

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r1n1_edd_formula_20260515T222601_result.json`
- **Structured JSON:** [`85b9d8e1c1fe9544f543.json`](../../sessions/85/85b9d8e1c1fe9544f543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both edits look correct. Summary of changes:

**method.tex §3.4** — Formalized EDD with:
- Explicit notation setup: depth set $\mathcal{D}$, threshold range $T \in (0.5, 1.0]$
- Formal specification of AUC(d, d+1): binary RF (500 trees, √19 features, class-balanced), 5-fold stratified CV
- `\begin{definition}` environment with label `def:edd`
- Post-definition interpretation explaining the universal quantifier and contiguous prefix semantics
- Footnote clarifying equivalence under monotonicity

**atlas.tex §4.4** — Updated "Cross-model convergence" paragraph with D027-compliant narrative:
- Bootstrap p-values: Pythia p=0.001 (significant), OLMo p=0.091 (marginal), GPT-2 XL p=0.505 (non-significant)
- Emphasizes directional consistency + graded confidence, never claims "all three significantly EDD=4"
- d4v5 saturation (0.681–0.684) described as unambiguous

**main.tex** — Added `amsthm` package and `\newtheorem{definition}` to support the Definition environment.

---
