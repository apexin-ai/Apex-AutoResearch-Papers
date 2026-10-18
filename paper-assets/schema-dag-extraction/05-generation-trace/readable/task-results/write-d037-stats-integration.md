# write d037 stats integration

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_d037_stats_integration_20260516T034255_result.json`
- **Structured JSON:** [`efd0b0ba082d4edb2d11.json`](../../sessions/ef/efd0b0ba082d4edb2d11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation successful, no errors. 16 pages.

**Summary of edits made:**

**results.tex:**
- **2A**: NER paragraph — 0.52→0.522, 0.55→0.549, added "bootstrap" before CIs, reformatted as "overlap: ... vs.\ ..."
- **C2 (9.1pp)**: Table caption reframed from "widens from 9.1 to 31.2" to slope-consistency narrative; line 90 now shows 9.1pp as extreme-batch with quartile gap $-$7.42pp alongside; line 119 replaced "31.2 vs.\ 9.1" with quartile gaps from Table 4
- **C3 (31.2pp)**: Added "extreme-batch" caveat to all remaining 31.2pp mentions (line 90 count=16 reference)
- **W12**: "model-invariant" → "consistent across tested models (Qwen3-32B and Llama-3.1-8B)" (2 occurrences)

**abstract.tex:**
- Removed `\S\ref{sec:centrality_confound}` cross-reference (abstracts should be self-contained)
- C2, W7, W12 were already applied by the other worker

---
