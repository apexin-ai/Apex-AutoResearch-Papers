# paper abstract intro update

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract-intro-update_20260516T015157_result.json`
- **Structured JSON:** [`f6c076264a3136b1a60b.json`](../../sessions/f6/f6c076264a3136b1a60b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files are already correct. No changes needed.

**abstract.tex** (line 6):
- Headline: binary macro-F1 = 0.723, CI [0.717, 0.729] ✓
- "gen-1 vs. gen-2+ ... excluding gen-0 to avoid shared-seed overlap" ✓
- Per-generator: std = 0.051 (not old range) ✓

**introduction.tex**:
- Line 25: binary macro-F1 = 0.723, CI [0.717, 0.729], "leak-free depth discrimination (gen-1 vs. gen-2+)", std = 0.051 ✓
- Line 34 (contribution list): binary F1 = 0.723, CI [0.717, 0.729], same framing ✓
- Line 17: 0.42–0.81 range — this is **baselines** (individual detectors repurposed), not our method. Correctly used to motivate ensemble approach.
- Line 28: perplexity 2.367 vs 2.387 — downstream experiment, not F1.

No stale 3-class headline numbers remain in either file.

---
