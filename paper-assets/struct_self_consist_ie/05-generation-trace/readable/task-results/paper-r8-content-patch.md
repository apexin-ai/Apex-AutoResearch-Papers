# paper r8 content patch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r8-content-patch_20260515T222032_result.json`
- **Structured JSON:** [`1e35c7d210bbbca36b01.json`](../../sessions/1e/1e35c7d210bbbca36b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files pass validation. Here's a summary of all changes:

**Task 1** (experiments.tex:118): Fixed `−3.4 pp` → `−2.2 pp` (LP worst case for 4B SciERC NER). Also tightened `≤0.2 pp` → `≤0.1 pp` for CoNLL to match data.

**Task 2** (appendix.tex:93–117): Added FK Independence permutation test paragraph with table (`tab:fk_independence`, `\label{app:fk_independence}`) inside the Robustness Analysis section. All three configs (SciERC Qwen n=529, CoNLL LLaMA n=2756, CoNLL Qwen n=2756) with exact numbers from the spec.

**Task 3** (appendix.tex:338–376): Updated TOST section — replaced "We lack an external anchor" with forward reference, then added "External equivalence margins" paragraph after `tab:tost` introducing δ\_SEM (0.43–1.33pp), δ\_practical (0.5pp, Ratinov & Roth 2009), δ\_literature (1.0pp, Berg-Kirkpatrick et al. 2012) with per-config results.

**Task 4** (experiments.tex): Compressed ~15–17 source lines:
- Merged two QE paragraphs into one tighter paragraph
- Shortened selection gap intro (removed "two layers" exposition duplicated in discussion)
- Trimmed 3 table captions and 2 footnotes
- Tightened robustness and scale robustness paragraphs

**Task 5** (discussion.tex): Compressed ~6 lines — removed redundant phrases, merged "The gap widens with N" into "Why the gap exists" paragraph, tightened practical recommendations and ablation paragraphs.

**Task 6**: Found and fixed 2 missing "preliminary" annotations:
- experiments.tex:50 — "LP RE collapses to ρ=0.011 **(preliminary)**"
- discussion.tex:15 — "On RE **(preliminary)**, LP reverses direction..."

---
