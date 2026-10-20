# paper fig2 integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig2-integration_20260517T010117_result.json`
- **Structured JSON:** [`6524622b7a7ce12c080e.json`](../../sessions/65/6524622b7a7ce12c080e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Integration complete. The figure is placed in the F7 section (`\label{fig:civo_decomposition}`) with:

- **Updated F7 paragraph**: references `Figure~\ref{fig:civo_decomposition}`, reports the key percentages (-73% peak, -86% final for trained dt-emb; -51% and -96% for Full-SGS s1/s2), and frames SGS as "reduces but does not eliminate CIVO risk."
- **Self-contained caption**: defines all four conditions (Baseline, Trained dt-emb, Full-SGS s1/s2), reports quantitative findings, and explicitly notes the 50% prevention rate without overclaiming.
- **Figure path**: `figures/fig2_civo_decomposition.pdf` resolves correctly via the existing `\graphicspath{{../../artifacts/}}`.
- **Style compliance**: no em-dashes, no -ing phrase endings, no transition-word stacking.

---
