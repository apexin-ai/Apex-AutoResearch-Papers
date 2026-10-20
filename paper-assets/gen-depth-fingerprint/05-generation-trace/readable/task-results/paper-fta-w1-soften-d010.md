# paper fta w1 soften d010

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fta-w1-soften-d010_20260521T183350_result.json`
- **Structured JSON:** [`ad760632ff9101672baa.json`](../../sessions/ad/ad760632ff9101672baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Summary of changes across both `artifacts/_project/paper/` and `docs/paper/`:

| File | Change |
|---|---|
| **abstract.tex** L5 | `remain near-stationary ($d < 0.10$)` → `remain largely near-stationary ($d \leq 0.10$ for core shape features)` |
| **introduction.tex** L10 | `vs.\ $d < 0.10$;` → `vs.\ $d < 0.10$ for near-stationary features; boundary features show intermediate stability;` |
| **introduction.tex** L18 | `($d < 0.10$)` → `($d < 0.10$ for near-stationary features)` |
| **results.tex** L70 (caption) | `non-drifting features (amber; $d < 0.10$)` → `near-stationary features (amber; $d \leq 0.10$)` |

Results.tex body text (L64, L78) already qualified as "three near-stationary features" and L82 already uses `$d \leq 0.08$`, so no changes needed there. The boundary features paragraph (L83-84) with entropy_min and tail_decay details was already precise.

---
