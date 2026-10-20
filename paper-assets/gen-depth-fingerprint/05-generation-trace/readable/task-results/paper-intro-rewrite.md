# paper intro rewrite

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_intro-rewrite_20260522T024653_result.json`
- **Structured JSON:** [`94a8de54299a9a14f99f.json`](../../sessions/94/94a8de54299a9a14f99f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No "Boundary mapping" references in actual paper tex files (only in logs). Both copies are updated and consistent.

**Report:**

| | Before | After |
|---|---|---|
| File lines | 21 | 19 |
| P1 approach | "AI text detection asks a single binary question" (methodological framing) | "An estimated 7-17% of recent scientific publications..." (urgency-first, contamination numbers) |
| P1 structure | 4 sentences: binary question → web contamination → drift → provenance need | 4 sentences: contamination stat → depth accumulation → detector gap → DDR preview |
| C1 length | ~3.5 rendered lines (includes "per-generator split analysis and convergent effect-size measures confirm this partition") | ~2 rendered lines (cut intermediate evidence, kept "what converges vs what is preserved" core) |
| C3 name | "Boundary mapping" | "Scope characterization" |
| C3 scope | "establishes where DDR-based detection succeeds and fails" | "maps the operational envelope... and provides a concrete roadmap for extending depth fingerprinting to instruction-tuned models, cross-domain transfer, and perturbation-robust deployment" |

All numbers, citations, and hard constraints preserved. Net character count slightly shorter (C1 savings offset C3 expansion + DDR preview addition).

---
