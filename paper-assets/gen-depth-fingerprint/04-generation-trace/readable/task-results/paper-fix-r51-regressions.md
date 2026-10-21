# paper fix r51 regressions

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-r51-regressions_20260525T070500_result.json`
- **Structured JSON:** [`6838de5926a16c0203d0.json`](../../sessions/68/6838de5926a16c0203d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three fixes are already applied in the current files:

1. **N2 (48.4% attribution)** — No stale "depth-2+ misclassified" text found. Both results.tex:25 and discussion.tex:21 correctly attribute 48.4% to depth-2 specifically.
2. **N3 (tail_decay range)** — No `d=0.07--0.15` found. discussion.tex:5 already has `|d|=0.10--0.22`.
3. **N4 (QLoRA within-model)** — All 5 occurrences across introduction, results, discussion, conclusion, and limitations already carry `within-model` annotations.

No edits needed — all 3 R51 issues have already been fixed in the current working tree.

---
