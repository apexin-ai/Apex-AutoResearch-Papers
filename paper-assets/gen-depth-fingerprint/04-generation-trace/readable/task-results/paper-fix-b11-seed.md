# paper fix b11 seed

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-b11-seed_20260518T004447_result.json`
- **Structured JSON:** [`25db36e4b42e11636658.json`](../../sessions/25/25db36e4b42e11636658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `artifacts/_project/analysis/qualitative_example_best_seed.md`.

**Seed 120 (Aquarius)** replaces seed 5. Key advantages:
- **entropy_max range: 1.29%** (vs seed 5's 15%) — near-perfect shape stability
- **tail_decay range: 3.81%** — stable
- **TTR drop: 87.73%**, **hapax drop: 99.09%** — both monotonically decreasing
- Text shows clean progressive degradation: factual Wikipedia → templated mythology claims → single sentence on repeat. Much stronger support for the "shape stable, lexicon collapses" narrative.

---
