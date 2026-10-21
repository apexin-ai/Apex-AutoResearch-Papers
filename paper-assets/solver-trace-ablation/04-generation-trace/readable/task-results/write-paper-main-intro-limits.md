# write paper main intro limits

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_paper-main-intro-limits_20260514T215337_result.json`
- **Structured JSON:** [`1c046f86a6b49fbe0027.json`](../../sessions/1c/1c046f86a6b49fbe0027.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied. Build passes (no errors; the one undefined ref `app:100step` is from method/experiments which another worker owns).

Summary of changes:
- **main.tex:21** — title now "...in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B" (singular + case-study qualifier).
- **main.tex:34** — added `\input{limitations}` after `\input{conclusion}`, before bibliography.
- **abstract.tex** — "maximal tightness" → "syntactic component necessity"; added NLI correlation result; "solver-agnostic" qualified ("validated on two structurally different solvers: Prover9 and SWI-Prolog"); 3× "genuine" → "non-hacking"; code-release footnote appended.
- **introduction.tex** — "maximally tight" reframed as "syntactic component necessity"; NLI ρ=−0.049 result inserted right after ISR definition; 3× "genuine" → "non-hacking".
- **limitations.tex** (new) — promoted from `\paragraph{Limitations}` to `\section{Limitations}` after conclusion; added Data-scale paragraph with FOLIO size, stratified sampling, seed-42 note.
- **conclusion.tex** — removed in-place Limitations paragraph; added Shapley-vs-LOO sentence in "Interpreting ISR"; added anti-gaming regularization sentence in "Meta-Level Goodhart"; 1× "genuine" → "non-hacking".

Output: 13 pages (body + refs + appendix); ACL places Limitations after conclusion / before refs and excludes it from the 8-page body count.

---
