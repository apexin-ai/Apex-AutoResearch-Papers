# writing director rewrite primary metric

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_director-rewrite-primary-metric_20260515T140056_result.json`
- **Structured JSON:** [`dfc1c0f149ebaf445c7e.json`](../../sessions/df/dfc1c0f149ebaf445c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 7 modifications complete:

1. **results.tex §4.3** — Merged Table 3 + binary table into single table with 3-class F1, Binary F1, Per-gen std columns; rewrote all paragraphs with binary F1=0.723 as primary metric
2. **results.tex §4.1** — Added gen-0 caveat about shared seed text inflation
3. **abstract.tex** — Headline: "binary macro-F1 of 0.72 for gen-1 vs. gen-2+ depth discrimination" with std=0.051
4. **introduction.tex** — Updated both body text (line 25) and Contribution 2 (line 34) to binary F1=0.72 with per-generator consistency
5. **conclusion.tex** — "binary macro-F1 of 0.72 for leak-free depth discrimination, per-generator std of 0.051"
6. **discussion.tex** — Multi-detector paragraph: 3-class advantage driven by gen-0; binary shows 7-feature matches best multi-detector (0.723 vs 0.724)
7. No references to `tab:binary-logo` remain; Table 1 and Table 2 numbers unchanged; §4.2 and §4.4 untouched

---
