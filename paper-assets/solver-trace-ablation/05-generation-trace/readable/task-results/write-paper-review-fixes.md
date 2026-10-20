# write paper review fixes

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_paper-review-fixes_20260514T231354_result.json`
- **Structured JSON:** [`cc3b50f9eaa8967ed28c.json`](../../sessions/cc/cc3b50f9eaa8967ed28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass:

1. **`\bibliographystyle{acl_natbib}`** is set automatically by `acl.sty` (line 195) — main.tex doesn't need it separately.
2. **Code/data release** (m3): footnote exists only in `abstract.tex` — no duplicates.
3. **discussion.tex vs conclusion.tex**: `discussion.tex` doesn't exist. `conclusion.tex` has "Discussion and Conclusion" as combined section. main.tex only includes `conclusion.tex`. No duplication.
4. **main.tex vs paper.tex**: `main.tex` is the active file (complete includes, proper packages). `paper.tex` is an older version that references a non-existent `discussion.tex`.

## Summary of all changes:

**M4 (Kim et al. differentiation)** — `related_work.tex`: Expanded the Kim et al. comparison to explicitly name their findings (axiom fabrication, premise mistranslation) and sharpen the contrast (inference-time prompting vs. RL training emergence, seven-mode taxonomy + cross-logic transfer).

**M7 (Reference coverage)** — `references.bib`: Added 3 new entries:
- `processbench` (Zheng et al., ACL 2025, arXiv 2412.06559) — PRMs fail to generalize
- `school-reward-hacks` (Taylor et al., arXiv 2508.17511) — reward hacking generalizes to misalignment
- `macdiarmid-emergent-misalignment` (MacDiarmid et al., Anthropic, arXiv 2511.18397) — production RL reward hacking

`related_work.tex`: Cited all 3 new papers in appropriate paragraphs. Total references: 39 → 42.

**m1 (Classifier precision/recall)** — `appendix.tex`: Expanded classifier validation from 3 sentences to a full paragraph explaining: deterministic rule-based nature, manual precision verification (50 samples, >95%, Wilson CI), recall limitations, functional LOO cross-validation procedure, and the query-as-fact false negative discovery.

**m3 (Code/data release)** — Confirmed: single footnote in `abstract.tex`, no duplicates.

**M3 (Solver-agnostic weakening)** — `introduction.tex`: Changed "solver-agnostic diagnostic" to "diagnostic...adaptable in principle to any solver supporting component-level input manipulation". `method.tex`: Changed "solver-agnostic" to "solver-agnostic in principle---applicable to any solver accepting component-level input manipulation".

**Extra checks** — `acl.sty` already sets `\bibliographystyle{acl_natbib}`. No discussion/conclusion duplication. `paper.tex` is stale (references non-existent `discussion.tex`), `main.tex` is the active file.

---
