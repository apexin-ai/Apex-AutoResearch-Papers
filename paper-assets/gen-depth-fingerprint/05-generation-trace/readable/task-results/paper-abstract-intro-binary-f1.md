# paper abstract intro binary f1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract-intro-binary-f1_20260516T011952_result.json`
- **Structured JSON:** [`4fc6f6c091bebb79b58b.json`](../../sessions/4f/4fc6f6c091bebb79b58b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files are already correct:

- **abstract.tex**: Headline is binary F1=0.723 with CI [0.717, 0.729], std=0.051. No old numbers.
- **introduction.tex**: Binary F1=0.723 appears in both the main text (line 25) and contributions (line 34), both with CI and std. No old numbers.
- No "consistently" in either file.
- Per-gen consistency uses std format (0.051), not raw range.
- No residual 0.82, 0.80, or 0.789 as headline numbers.
- The 0.42–0.81 range on intro line 17 correctly describes baseline detector weakness, not our ensemble.

No changes needed — both files already reflect the D017 decision with binary F1=0.723 as primary metric.

---
