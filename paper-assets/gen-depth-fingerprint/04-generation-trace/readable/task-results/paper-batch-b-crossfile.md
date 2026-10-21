# paper batch b crossfile

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_batch-b-crossfile_20260518T003242_result.json`
- **Structured JSON:** [`15acab1ca9970a64048d.json`](../../sessions/15/15acab1ca9970a64048d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Here's the summary:

## Completed

### B4: Shape Preservation Weakening
- **abstract.tex**: "approximately preserves distributional shape" → "whose shape remains comparatively stable"
- **method.tex**: "approximately preserving distributional shape" → "with distributional shape remaining comparatively stable"
- **discussion.tex**: "approximately preserves distributional shape" → "leaves distributional shape comparatively stable" + added Levene reconciliation sentence
- **conclusion.tex**: "approximately preserves distributional shape" → "whose shape remains comparatively stable"
- Remaining occurrences are only in introduction.tex, results.tex, related_work.tex (outside scope)

### B10: Missing References
Added 3 verified references:
1. **Briesch et al. 2023** (`briesch_self_consuming`) — confirmed: arXiv:2311.16822
2. **Jovanović et al. 2024** (`jovanovic_watermark_stealing`) — note: the paper titled "Watermark Stealing in Large Language Models" is by Jovanović/Staab/Vechev at ICML 2024, not Zhang. A separate Zhang et al. ACSAC 2024 paper has a different title.
3. **McGovern et al. 2025** (`mcgovern_fingerprints`) — GenAIDetect workshop, confirmed

**Skipped:**
- **Tang et al. 2024**: No paper by Tang with that title exists. The Nature Reviews Physics article "Science in the age of large language models" is by Birhane et al. 2023.
- **Geng et al. 2026** (`markovian_chains`): Still arXiv preprint, under review at ICLR 2026. Current bib entry is up-to-date.

### B11: Qualitative Examples Appendix
- Created `appendix_qualitative_examples.tex` with feature table populated from actual data (seed 5, Pythia-2.8B, depths 0/1/2)
- Text cells left as TODO (generated texts not available locally, only on server)
- Added `\input{appendix_qualitative_examples}` to main.tex

### B12: Bib Check
- `self_consuming_mad` first author confirmed correct: Sina Alemohammad (verified via arXiv and multiple sources)

---
