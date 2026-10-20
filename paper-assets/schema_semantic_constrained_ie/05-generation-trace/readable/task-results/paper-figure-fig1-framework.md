# paper figure fig1 framework

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_framework_20260520T174649_result.json`
- **Structured JSON:** [`82b8ce4bced4a897e068.json`](../../sessions/82/82b8ce4bced4a897e068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No TikZ errors. The figure compiled cleanly into the PDF (539KB, 33 pages).

The new `fig1_framework.tex` implements a three-section left-to-right layout:

- **Left (Schema Compilation)**: IE Ontology forks into grammar path (JSON Schema → XGrammar → M_g) and semantic path (σ(r) pairs → TypeConstraintProcessor → Semantic Rules)
- **Middle (Constraint Layers)**: Grammar Layer (blue, L1: Context-Free, G(t)⊆V) and Semantic Layer (orange, L2: Prefix-Decidable, S(t)⊆V) with dashed enabling dependency arrow and Entity Registry D (dashed border, yellow)
- **Right (Token Masking)**: M_final composition, decision diamond (G∩S=∅?), No→Sample G∩S / Yes→red dashed fallback G(t) with CF risk annotation, autoregressive loop back via t+1

---
