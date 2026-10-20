# paper writing discussion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_discussion_20260514T204918_result.json`
- **Structured JSON:** [`cc137522787510c68cc8.json`](../../sessions/cc/cc137522787510c68cc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discussion section written to `docs/paper/sections/discussion.tex`. Five paragraphs covering all required topics:

1. **Practical recommendations** — voting for quality estimation, SJ for robustness/generalization, logprob for binary filtering, greedy near-optimal for NER selection
2. **Between-instance vs. within-stratum** — stratified correlations approach zero; signals suit routing/triage, not fine-grained ranking
3. **Task-difficulty-dependent signal selection** — EM on easy, Voting/SJ on hard, convergence at capability boundary; model-agnostic ordering
4. **Capability boundary framework** — sweet spot of sufficient capability + output complexity; high-complexity RE subset (n=81) with strong signals; conditional filtering separates SJ from logprob at N=16
5. **ρ-AUROC separation** — logprob for coarse binary separation vs. structural for fine-grained ranking; single-metric evaluation risks misselection

~490 words, no subsections, `\paragraph{}` organization, all table/section cross-references included.

---
