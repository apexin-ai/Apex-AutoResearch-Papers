# code zeroshot llm 500 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_zeroshot_llm_500_001_20260515T163627_result.json`
- **Structured JSON:** [`879389b434e717918ecd.json`](../../sessions/87/879389b434e717918ecd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Zero-shot LLM 500-sample baseline completed.** Results:

| Metric | Value |
|--------|-------|
| **4-class accuracy** | **36.2%** |
| **95% bootstrap CI** | **[32.0%, 40.4%]** (width = 8.4pp) |
| MAE | 1.028 |
| Errors | 0/500 |

**Per-class breakdown:**

| Depth | Precision | Recall | F1 |
|-------|-----------|--------|----|
| d0 (human) | 0.39 | **0.952** | 0.55 |
| d1 | 0.33 | 0.128 | 0.18 |
| d2 | 0.30 | 0.248 | 0.27 |
| d3 | 0.38 | 0.120 | 0.18 |

**Key takeaways for R1-W4:**

1. **CI narrowed** from ~13.6pp (200 samples) to **8.4pp** (500 samples) — the tighter CI confirms the result is stable, not a fluke.
2. **500-sample acc (36.2%)** is within the 200-sample estimate (40.0%) range — consistent, slight drop due to larger sample regression to mean.
3. **RF baseline (78.2%) dominates by 42pp** — the gap is unambiguous even at the upper CI bound (40.4%).
4. **Failure mode is clear**: the LLM overwhelmingly predicts depth-0 (recall 95.2%) but collapses on d1/d2/d3 (recall 12–25%), confirming it cannot distinguish generation depths beyond "human vs. not quite human."

Artifact registered as `art_20260515_0d8eeb`. Remote results at `/root/autodl-tmp/recursive_gen_depth_est/results/zeroshot_llm_500/results.json`.

---
