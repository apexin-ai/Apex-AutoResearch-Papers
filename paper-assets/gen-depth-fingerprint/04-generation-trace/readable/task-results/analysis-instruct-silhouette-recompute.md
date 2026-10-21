# analysis instruct silhouette recompute

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_instruct_silhouette_recompute_20260521T032058_result.json`
- **Structured JSON:** [`0aafe9cf989cc736d76d.json`](../../sessions/0a/0aafe9cf989cc736d76d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Instruct silhouette recomputed: **0.338 → 0.372** (k=2 k-means, gen-1 vs gen-2+, StandardScaler).

Key findings:
- The k-means partition for instruct models is structurally different from base models — it groups {entropy_mean, entropy_std} together vs the rest, whereas base models group {entropy_mean, ttr, hapax_ratio} vs rest.
- Applying the base model's fixed partition to instruct data gives silhouette = -0.105, confirming the DDR structure genuinely differs between base and instruct.
- Results saved to `artifacts/_project/analysis/instruct_silhouette_recompute.txt`.

---
