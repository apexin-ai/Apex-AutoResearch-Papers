# writing llm confidence depth

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_llm-confidence-depth_20260514T084315_result.json`
- **Structured JSON:** [`2269d46ccd57237d0c9a.json`](../../sessions/22/2269d46ccd57237d0c9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inserted at `discussion.tex:101-103` (Section 5.5, between the existing qualitative argument and the future-work caveat). Full paragraph (~80 words):

> Per-depth analysis sharpens this conclusion. Both models achieve high depth-0 recall (GPT-5.5: 0.77, Claude: 0.69), indicating reliable human-text identification, but recall for depths 1–4 collapses to 0.08–0.38, with confusion matrices (Table S3) showing predictions scattered nearly uniformly across non-human classes. The resulting Spearman correlations between predicted and true depth are weak (ρ = 0.38 for GPT-5.5, ρ = 0.42 for Claude), confirming that frontier LLMs function as binary human-vs.-AI detectors augmented by near-random depth guessing—confidence scores cannot serve as a depth proxy.

Data sources: Spearman ρ values from the exp-011 checkpoint; per-depth recall and confusion matrices from Table S3 in appendix.tex.

---
